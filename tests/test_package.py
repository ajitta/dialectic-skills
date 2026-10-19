"""Developer-only checks for tools/package.py and the shipped output (docs/spec.md §12.1).

Run: python -m unittest discover -s tests -v   (stdlib only; PyYAML is used when installed)
"""

from __future__ import annotations

import importlib.util
import io
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

    def test_seven_skills_with_spec_names(self):
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
    def test_prefix_rule(self):
        errs = pkg.validate_names(["dia-refine", "dia-refine-loop"])
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
