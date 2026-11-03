"""Developer-only checks for tools/package.py and the shipped output (docs/spec.md §12.1).

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
        files = {"skills/dia-a/SKILL.md": b"use dia-b, then self-refine\n  lineage: \"self-refine\"\nsee https://x/negative-dialectics"}
        errs = pkg.crossref_violations(files, ["dia-a"])
        self.assertEqual(len(errs), 2, errs)  # unknown dia-b; old name on line 1 only

    def test_renamed_dia_confirm(self):
        files = {"skills/dia-a/SKILL.md": b"run dia-confirm first\n  lineage: \"confirm-intent; named dia-confirm from 1.1.0 to 1.4.0\""}
        errs = pkg.crossref_violations(files, ["dia-a"])
        self.assertTrue(any("old skill name 'dia-confirm'" in e for e in errs), errs)
        self.assertFalse([e for e in errs if ":2:" in e], errs)  # lineage line is exempt

    def test_renamed_2_0_0(self):
        for old in ("dia-intent", "dia-brainstorm", "dia-refine", "dia-instruct", "dia-menu"):
            errs = pkg.crossref_violations({"skills/dia-a/SKILL.md": f"run {old} first".encode()}, ["dia-a"])
            self.assertTrue(any(f"old skill name {old!r}" in e for e in errs), errs)

    def test_former_names_only_on_router_alias_lines(self):
        line = b"- Former names: a first word dia-refine reaches this skill"
        self.assertTrue(pkg.crossref_violations({"skills/dia-emend/SKILL.md": line}, ["dia-emend"]))
        self.assertTrue(pkg.crossref_violations({"skills/dia-router/SKILL.md": b"see dia-refine"}, ["dia-router"]))
        version = pkg.plugin_version()
        errs = pkg.crossref_violations({"skills/dia-router/SKILL.md": line}, ["dia-router"])
        if pkg.version_tuple(version) < pkg.FORMER_NAMES_UNTIL:
            self.assertEqual(errs, [])
        else:
            self.assertTrue(any("remove the former-name text" in e for e in errs), errs)

    def test_former_name_lines_still_check_new_names(self):
        if pkg.version_tuple(pkg.plugin_version()) >= pkg.FORMER_NAMES_UNTIL:
            self.skipTest("aliases expired")
        errs = pkg.crossref_violations({"skills/dia-router/SKILL.md": b"former names: dia-refine now dia-quaesto"}, ["dia-router"])
        self.assertTrue(any("unknown skill 'dia-quaesto'" in e for e in errs), errs)
        errs = pkg.crossref_violations({"skills/dia-router/SKILL.md": b"formerly dia-refine"}, ["dia-router"])
        self.assertTrue(any("old skill name" in e for e in errs), errs)

    def test_former_name_aliases_expire(self):
        real = pkg.plugin_version
        try:
            pkg.plugin_version = lambda: "2.1.0"
            errs = pkg.crossref_violations({"skills/dia-router/SKILL.md": b"former name dia-menu"}, ["dia-router"])
            self.assertTrue(any("remove the former-name text" in e for e in errs), errs)
        finally:
            pkg.plugin_version = real

    def test_every_description_is_gated(self):
        for s in pkg.skill_dirs():
            fm, _, _ = pkg.frontmatter((s / "SKILL.md").read_text(encoding="utf-8"))
            if s.name == "dia-router":
                self.assertIn("first word of the message is dia on its own", fm["description"])
            else:
                self.assertIn(f"Use only when the message starts with {s.name},", fm["description"])
                self.assertIn("when dia-router selects it", fm["description"])

    def test_router_menu_codes(self):
        body = (ROOT / "skills" / "dia-router" / "SKILL.md").read_text(encoding="utf-8")
        rows = re.findall(r"^\| (\d+) \| (dia-[a-z]+) \| `([a-z]{3})` \|", body, re.M)
        self.assertEqual([int(n) for n, _, _ in rows], list(range(1, 14)))
        self.assertEqual({n for _, n, _ in rows}, set(pkg.EXPECTED_IMPLICIT) - {"dia-router"})
        codes = [c for _, _, c in rows]
        self.assertEqual(len(set(codes)), 13)
        for _, name, code in rows:
            self.assertTrue(name[4:].startswith(code), (name, code))

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
    """README.<lang>.md files mirror README.md's structure (spec D31)."""

    LANGS = ("ko", "ja", "zh-CN")
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
            for target in ("README.md", "README.ko.md", "README.ja.md", "README.zh-CN.md"):
                if not target.endswith(f".{lang}.md"):
                    self.assertIn(f"]({target})", switcher, f"{path.name}: switcher misses {target}")
            anchors = {self._slug(h) for h in re.findall(r"^#{2,6} (.+)$", text, re.M)}
            for anchor in re.findall(r"\]\(#([^)]+)\)", text):
                self.assertIn(anchor, anchors, f"{path.name}: dead anchor #{anchor}")


class TestDirectoryPackages(unittest.TestCase):
    """Directory listing requirements (spec D32, docs/directory-submission.md)."""

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
