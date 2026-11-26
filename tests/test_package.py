"""Developer-only checks for tools/package.py and the shipped output.

Run: python -m unittest discover -s tests -v   (stdlib only; PyYAML is used when installed)
"""

from __future__ import annotations

import importlib.util
import io
import re
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
_spec = importlib.util.spec_from_file_location("package", ROOT / "tools" / "package.py")
assert _spec is not None and _spec.loader is not None
pkg = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(pkg)

try:
    import yaml  # type: ignore
except ImportError:  # pragma: no cover
    yaml = None


class TestSource(unittest.TestCase):
    def setUp(self):
        self.skills = pkg.skill_dirs()
        self.files = pkg.plugin_files(self.skills)

    def test_validation_passes(self):
        self.assertEqual(pkg.collect_errors(self.skills, self.files), [])

    def test_committed_output_is_current(self):
        self.assertEqual(pkg.check_release(self.files) + pkg.check_generated(self.files), [])

    def test_skills_match_expected_table(self):
        self.assertEqual(sorted(s.name for s in self.skills), sorted(pkg.EXPECTED_IMPLICIT))

    def test_implicit_invocation_table(self):
        got = {s.name: pkg.openai_policy(s) for s in self.skills}
        self.assertEqual(got, pkg.EXPECTED_IMPLICIT)

    def test_no_upstream_in_shipped(self):
        self.assertFalse([k for k in self.files if k.startswith("upstream/") or "/upstream/" in k])

    def test_shipped_files_are_lf(self):
        for f in (ROOT / "plugins" / "dia").rglob("*"):
            if f.is_file():
                self.assertNotIn(b"\r", f.read_bytes(), f)

    @unittest.skipIf(yaml is None, "PyYAML not installed")
    def test_frontmatter_and_openai_yaml_parse(self):
        for s in self.skills:
            text = (s / "SKILL.md").read_text(encoding="utf-8")
            fm = yaml.safe_load(text.split("---\n")[1])
            self.assertEqual(fm["name"], s.name)
            data, _, _ = pkg.frontmatter(text)
            self.assertEqual(fm["description"], data["description"], s.name)
            oy = yaml.safe_load((s / "agents" / "openai.yaml").read_text(encoding="utf-8"))
            self.assertEqual(oy["policy"]["allow_implicit_invocation"], pkg.EXPECTED_IMPLICIT[s.name])
            self.assertTrue(oy["interface"]["default_prompt"].startswith(f"Use $dia:{s.name} "))


class TestRules(unittest.TestCase):
    def test_short_description_length(self):
        import shutil, tempfile
        with tempfile.TemporaryDirectory() as d:
            s = Path(d) / "dia-emend"
            shutil.copytree(ROOT / "skills" / "dia-emend", s)
            y = s / "agents" / "openai.yaml"
            y.write_text(y.read_text(encoding="utf-8").replace('short_description: "', 'short_description: "' + "x" * 64, 1), encoding="utf-8", newline="\n")
            self.assertTrue(any("short_description" in e for e in pkg.validate_skill(s)))

    def test_prefix_rule(self):
        errs = pkg.validate_names(["dia-emend", "dia-emend-loop"])
        self.assertTrue(any("prefix" in e for e in errs))
        # the caller is a first word of its own, so it is not a prefix of the thirteen
        self.assertFalse([e for e in pkg.validate_names(sorted(pkg.EXPECTED_IMPLICIT)) if "prefix" in e])

    def test_metadata_holds_the_version_only(self):
        import shutil, tempfile
        with tempfile.TemporaryDirectory() as d:
            s = Path(d) / "dia-emend"
            shutil.copytree(ROOT / "skills" / "dia-emend", s)
            self.assertFalse([e for e in pkg.validate_skill(s) if "metadata" in e])
            f = s / "SKILL.md"
            f.write_text(f.read_text(encoding="utf-8").replace("metadata:\n", "metadata:\n  author: x\n", 1), encoding="utf-8", newline="\n")
            self.assertTrue(any("metadata" in e for e in pkg.validate_skill(s)))

    def test_caller_name_is_admitted(self):
        self.assertFalse([e for e in pkg.validate_skill(ROOT / "skills" / "dia") if "prefix" in e or "name" in e])

    def test_hangul_boundary(self):
        bad = {"skills/dia-x/SKILL.md": "설명".encode()}
        ok = {"skills/dia-x/references/ko/law.md": "설명".encode()}
        self.assertTrue(pkg.shipped_violations(bad))
        self.assertEqual(pkg.shipped_violations(ok), [])

    def test_forbidden_shipped_paths(self):
        for rel in (
            "skills/dia-x/scripts/run.md",
            "bin/tool.md",
            "hooks/hooks.json",
            ".mcp.json",
            "skills/dia-x/helper.py",
            "upstream/README.md",
        ):
            self.assertTrue(pkg.shipped_violations({rel: b"x"}), rel)

    def test_crossrefs(self):
        files = {"skills/dia-a/SKILL.md": b"use dia-b, then self-refine\nsee https://x/negative-dialectics"}
        errs = pkg.crossref_violations(files, ["dia-a"])
        self.assertEqual(len(errs), 2, errs)  # unknown dia-b; the old name on line 1; a URL is no reference

    def test_retired_names(self):
        for old in ("dia-confirm", "dia-intent", "dia-brainstorm", "dia-refine", "dia-instruct", "dia-menu", "dia-router", "dia-panel"):
            errs = pkg.crossref_violations({"skills/dia-a/SKILL.md": f"run {old} first".encode()}, ["dia-a"])
            self.assertEqual(errs, [f"skills/dia-a/SKILL.md:1: old skill name {old!r}"])

    def test_every_description_is_gated(self):
        for s in pkg.skill_dirs():
            fm, _, _ = pkg.frontmatter((s / "SKILL.md").read_text(encoding="utf-8"))
            if s.name == pkg.CALLER:
                self.assertIn("Use only when the first word of the message is dia on its own, or when this skill is invoked by name;", fm["description"])
            else:
                self.assertTrue(fm["description"].endswith(
                    f" Use only when the message starts with {s.name}, or when the skill is invoked by name;"
                    " a request that only sounds like this is not an invocation."), s.name)

    TABLE_HEAD = "| Skill | What it is for | Hand it | It returns | Someone to answer |"

    def _contract_table(self, text):
        lines = text.split("\n")
        start = lines.index(self.TABLE_HEAD)
        rows = []
        for line in lines[start:]:
            if not line.startswith("|"):
                break
            rows.append(line)
        return rows

    def test_contract_table_in_two_places(self):
        # the model reads the table in `dia`; a person reads it in the plugin README; they are one table
        body = (ROOT / "skills" / "dia" / "SKILL.md").read_text(encoding="utf-8")
        readme = (ROOT / "packaging" / "plugin-README.md").read_text(encoding="utf-8")
        rows = self._contract_table(body)
        self.assertEqual(rows, self._contract_table(readme))
        names = [r.split("|")[1].strip() for r in rows[2:]]
        self.assertEqual(sorted(names), sorted(set(pkg.EXPECTED_IMPLICIT) - {pkg.CALLER}))
        self.assertNotRegex(body, pkg.MENU_NUMBER_RE)

    def test_no_skill_names_another(self):
        # a skill is a function: only the caller knows the others
        for s in pkg.skill_dirs():
            if s.name == pkg.CALLER:
                continue
            for f in sorted(s.rglob("*")):
                if f.is_file():
                    others = set(pkg.SKILL_REF_RE.findall(f.read_text(encoding="utf-8"))) - {s.name}
                    self.assertFalse(others, f"{f.relative_to(ROOT).as_posix()} names {sorted(others)}")

    def test_no_menu_numbers_in_skills(self):
        errs = pkg.selector_violations({"skills/dia-x/SKILL.md": "picked by `dia 11 \u2026` here".encode(), "skills/dia-y/SKILL.md": b"the form `dia <number> <request>`", "skills/dia-z/SKILL.md": b"send dia 10 --max 2 <draft>", "skills/dia-w/agents/openai.yaml": b"or dia 11 <reports>", "skills/dia/SKILL.md": "`dia 4 \u2026` runs it".encode()})
        self.assertEqual(len(errs), 5)
        ok = {"skills/dia/SKILL.md": "a number (`3 reasons \u2026`) is a request".encode(), "skills/dia-skopos/SKILL.md": "as in `dia 1 thing I keep forgetting: \u2026`".encode(), "docs/probes.md": "`dia 4 \u2026`".encode()}
        self.assertEqual(pkg.selector_violations(ok), [])

    def test_docs_name_only_working_forms(self):
        self.assertEqual(pkg.docs_violations(pkg.doc_files()), [])
        self.assertEqual(set(pkg.doc_files()), set(pkg.DOC_PATHS))
        bad = ["`dia-intent` is now `dia-skopos`", "send `dia refine \u2026`", "a code (`dia red \u2026`)", "`dia 3 reasons \u2026`",
               "the form `dia <number> <request>`", "Short codes were removed", "menu numbers stopped in 2.13.0", "\uc9e7\uc740 \ucf54\ub4dc", "\uba54\ub274 \ubc88\ud638", "\u77ed\u3044\u30b3\u30fc\u30c9", "\u30e1\u30cb\u30e5\u30fc\u756a\u53f7", "\u7b80\u77ed\u4ee3\u7801", "\u83dc\u5355\u7f16\u53f7", "a three-letter code", "the code `dia int \u2026`", "dia-refine\uc744 \uc4f0\uba74", "dia-instruct\u306e\u30eb\u30fc\u30eb", "dia 3", "dia 12 items", "`dia-router` picks one"]
        for line in bad:
            self.assertEqual(len(pkg.docs_violations({"README.md": line.encode()})), 1, line)
            self.assertEqual(len(pkg.docs_violations({"site/index.html": line.encode()})), 1, line)
        ok = ["`dia menu` lists the skills", "`dia reductio \u2026` or `dia dia-reductio \u2026`", "`dia negative feedback on my draft?`", "`dia ratchet --max 2 <draft>`",
              "three letters, no hyphen", "> \"against the dia-instruct rules\"", "`dia-regula` reads a prompt", "media consumption", "`dia redo the outline`", "dia 2.16.0 adds a skill", "dia 12.5 is not a release", "`dia interview notes into themes`"]
        self.assertEqual(pkg.docs_violations({"README.md": "\n".join(ok).encode()}), [])
        self.assertEqual(len(pkg.docs_violations({"site/index.html": b"> dia-instruct"})), 1)  # the quote exemption is for Markdown

    def test_plain_scalar_guard(self):
        with self.assertRaises(ValueError):
            pkg.frontmatter("---\nname: x\ndescription: Delegated form: y\n---\nbody\n")


class TestZip(unittest.TestCase):
    def test_reproducible_and_rooted(self):
        files = pkg.plugin_files(pkg.skill_dirs())
        a, b = pkg.zip_bytes(files), pkg.zip_bytes(files)
        self.assertEqual(a, b)
        with zipfile.ZipFile(io.BytesIO(a)) as zf:
            for info in zf.infolist():
                self.assertTrue(info.filename.startswith("dia/"), info.filename)
                self.assertEqual(info.date_time, (1980, 1, 1, 0, 0, 0))
                self.assertEqual(info.create_system, 3)
            self.assertIn("dia/.claude-plugin/plugin.json", zf.namelist())


if __name__ == "__main__":
    unittest.main()


class TestReadmeTranslations(unittest.TestCase):
    """README.ko.md mirrors README.md's structure."""

    LANGS = ("ko",)
    VERBATIM_PREFIXES = ("/plugin", "codex ", "python ", "skills/", "ajitta/")

    @staticmethod
    def _parse(text):
        heads, blocks, tables, links = [], [], 0, set()
        in_code, buf = False, []
        for line in text.split("\n"):
            if line.lstrip().startswith("```"):
                if in_code:
                    blocks.append("\n".join(buf).strip())
                    buf = []
                in_code = not in_code
                continue
            if in_code:
                buf.append(line)
                continue
            m = re.match(r"^(#{1,6}) ", line)
            if m:
                heads.append(len(m.group(1)))
            if re.match(r"^\|[-|: ]+\|$", line):
                tables += 1
            links |= {u for u in re.findall(r"\]\(([^)#][^)]*)\)", line) if not re.match(r"README(\.[\w-]+)?\.md$", u)}
        return heads, blocks, tables, links

    @staticmethod
    def _slug(heading):
        s = heading.strip().lower()
        s = re.sub(r"[^\w\- ]", "", s)
        return s.replace(" ", "-")

    def test_translations_mirror_english(self):
        en = (ROOT / "README.md").read_text(encoding="utf-8")
        en_heads, en_blocks, en_tables, en_links = self._parse(en)
        for lang in self.LANGS:
            path = ROOT / f"README.{lang}.md"
            self.assertTrue(path.is_file(), path)
            text = path.read_text(encoding="utf-8")
            self.assertNotIn("\r", text, path)
            heads, blocks, tables, links = self._parse(text)
            self.assertEqual(heads, en_heads, f"{path.name}: heading levels differ")
            self.assertEqual(len(blocks), len(en_blocks), f"{path.name}: code block count")
            self.assertEqual(tables, en_tables, f"{path.name}: table count")
            self.assertEqual(links, en_links, f"{path.name}: link targets differ")
            for a, b in zip(en_blocks, blocks):
                if a.startswith(self.VERBATIM_PREFIXES):
                    self.assertEqual(a, b, f"{path.name}: command block changed")
            switcher = text.split("\n")[2]
            for target in ("README.md", "README.ko.md"):
                if not target.endswith(f".{lang}.md"):
                    self.assertIn(f"]({target})", switcher, f"{path.name}: switcher misses {target}")
            anchors = {self._slug(h) for h in re.findall(r"^#{2,6} (.+)$", text, re.M)}
            for anchor in re.findall(r"\]\(#([^)]+)\)", text):
                self.assertIn(anchor, anchors, f"{path.name}: dead anchor #{anchor}")


class TestDirectoryPackages(unittest.TestCase):
    """What a directory listing needs of the two packages."""

    def setUp(self):
        self.files = pkg.plugin_files(pkg.skill_dirs())

    def test_plugin_readme_shipped(self):
        self.assertIn("README.md", self.files)
        self.assertEqual(pkg.validate_plugin_readme(self.files), [])
        self.assertTrue(pkg.validate_plugin_readme({"README.md": b"too short"}))

    def test_openai_zip_layout(self):
        names = zipfile.ZipFile(ROOT / "releases" / pkg.OPENAI_ZIP_NAME).namelist()
        self.assertEqual({n.split("/")[0] for n in names}, {"dia"})
        self.assertIn("dia/.codex-plugin/plugin.json", names)
        self.assertFalse([n for n in names if n.startswith("dia/.claude-plugin/")])
        self.assertIn("dia/assets/logo.svg", names)
        self.assertIn("dia/assets/icon.svg", names)
        self.assertEqual(
            sorted(n for n in names if "/skills/" in n),
            sorted(f"dia/{k}" for k in self.files if k.startswith("skills/")),
        )

    def test_openai_interface_rules(self):
        interface, assets = pkg.openai_parts()
        self.assertEqual(pkg.validate_openai_interface(interface, assets), [])
        bad = dict(interface, shortDescription="x" * 31, category="Games", defaultPrompt=["a", "b", "c", "d"])
        errs = pkg.validate_openai_interface(bad, assets)
        for field in ("shortDescription", "category", "defaultPrompt"):
            self.assertTrue(any(field in e for e in errs), (field, errs))
        self.assertTrue(pkg.validate_openai_interface(dict(interface, logo="./assets/missing.svg"), assets))
