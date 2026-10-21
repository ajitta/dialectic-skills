#!/usr/bin/env python3
"""Validate the dia skills and build the shipped plugin (developer-only, stdlib only).

Source: skills/<skill>/ are plain Agent Skills (SKILL.md, references/, agents/openai.yaml)
with no manifest inside. The one manifest lives in plugin-manifest.json and is injected
only into the generated output (docs/spec.md §7.5):

    plugins/dia/                       marketplaces point here (committed)
      .claude-plugin/plugin.json       from plugin-manifest.json
      README.md                        from packaging/plugin-README.md (directory listings need it)
      skills/<skill>/...               copied from skills/
    releases/dialectic-skills.zip      the same under one top-level dia/ folder (committed)
    releases/dialectic-skills-openai.zip
                                       OpenAI directory upload (spec D32): the same files, but
                                       .codex-plugin/plugin.json (manifest + packaging/openai/
                                       interface.json) instead of .claude-plugin/, plus assets/

The zip is byte-reproducible on every OS: fixed timestamps, modes and create_system,
LF line endings, and entries stored without compression (deflate output differs between
zlib builds, e.g. zlib-ng in some CPython builds, so a deflated zip is not reproducible).

plugin-release.json (not shipped) records a digest of the skill files for the current
plugin version; changed skill files under an unchanged version fail, because Claude Code
updates an installed plugin only when its version changes. Before a version is first
released, delete the record and rebuild.

Usage:
    python tools/package.py           validate, then write plugins/dia/ and the zip
    python tools/package.py --check   validate, and check the committed output is current
"""

from __future__ import annotations

import hashlib
import io
import json
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"
PLUGINS = ROOT / "plugins"
DIST = ROOT / "releases"
ZIP_NAME = "dialectic-skills.zip"
OPENAI_ZIP_NAME = "dialectic-skills-openai.zip"
PACKAGING = ROOT / "packaging"
PLUGIN_README = PACKAGING / "plugin-README.md"
OPENAI_DIR = PACKAGING / "openai"
README_MIN_WORDS = 40  # Anthropic directory: README of at least 40 words outside code blocks
# OpenAI directory final-submission limits (developers.openai.com/plugins/deploy/submission-errors)
OPENAI_CATEGORIES = {
    "Productivity", "Creativity", "Developer Tools", "Business & Operations", "Data & Analytics",
    "Communication", "Education & Research", "Security", "Finance", "Healthcare", "Travel",
    "Entertainment", "Other",
}
MANIFEST = ROOT / "plugin-manifest.json"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
RELEASE = ROOT / "plugin-release.json"

ALLOWED_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
REQUIRED_META = ("author", "version", "lineage", "source")
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SKILL_PREFIX = "dia-"
MAX_BODY_LINES = 200
SHORT_DESC_MIN, SHORT_DESC_MAX = 25, 64  # interface.short_description, openai/skills openai_yaml.md
# A source folder stays a plain skill (spec §7.5).
FORBIDDEN_SOURCE_DIRS = ("skills", "bin", ".claude-plugin", ".codex-plugin")
# The shipped package is instructions only (spec §7.1).
SHIPPED_SUFFIXES = {".md", ".json", ".yaml", ".yml"}
FORBIDDEN_SHIPPED_DIRS = {"scripts", "bin", "hooks", "monitors"}
FORBIDDEN_SHIPPED_FILES = {".mcp.json", ".lsp.json"}
HANGUL_RE = re.compile("[\u1100-\u11ff\u3130-\u318f\ua960-\ua97f\uac00-\ud7ff]")
KO_DIR = "/references/ko/"
KO_HEADER = ("Scope:", "Source:", "As of:", "Use when:")
SKILL_REF_RE = re.compile(r"\bdia-[a-z]+(?:-[a-z]+)*\b")
# Names of the skills dia was rebuilt from; they may appear only in metadata.lineage.
OLD_NAMES_RE = re.compile(
    r"\b(socratic-brainstorm|socratic-elenchus|confirm-intent|dia-intent|negative-dialectics|self-refine|recursive-refine)\b"
)
EXPECTED_IMPLICIT = {
    "dia-confirm": True,
    "dia-elenchus": True,
    "dia-brainstorm": True,
    "dia-reductio": True,
    "dia-negative": True,
    "dia-refine": True,
    "dia-iterate": True,
}


# ---------------------------------------------------------------- parsing


def frontmatter(text: str) -> tuple[dict, dict, str]:
    """Return (top-level keys, metadata map, body). Minimal YAML subset: `key: value`
    lines plus one indented level of `key: value` under metadata."""
    text = text.replace("\r\n", "\n")
    if not text.startswith("---\n"):
        raise ValueError("SKILL.md must start with '---' on line 1")
    end = text.index("\n---\n", 4)
    block, body = text[4:end], text[end + 5 :]
    data: dict = {}
    meta: dict = {}
    current = None
    for line in block.splitlines():
        if not line.strip():
            continue
        if line.startswith((" ", "\t")):
            if current != "metadata":
                raise ValueError(f"unexpected indented line: {line!r}")
            k, _, v = line.strip().partition(":")
            meta[k.strip()] = v.strip().strip('"')
            continue
        key, _, value = line.partition(":")
        current = key.strip()
        value = value.strip()
        if value and not value.startswith('"') and (": " in value or " #" in value):
            raise ValueError(f"{current}: plain YAML scalar contains ': ' or ' #'; quote it or reword")
        data[current] = value.strip('"')
    return data, meta, body


def skill_dirs() -> list[Path]:
    return sorted(p for p in SKILLS.iterdir() if (p / "SKILL.md").is_file())


def openai_short_description(skill_dir: Path) -> str | None:
    path = skill_dir / "agents" / "openai.yaml"
    if not path.is_file():
        return None
    m = re.search(r'^\s*short_description:\s*"([^"]*)"\s*$', path.read_text(encoding="utf-8"), re.M)
    return None if m is None else m.group(1)


def openai_policy(skill_dir: Path) -> bool | None:
    path = skill_dir / "agents" / "openai.yaml"
    if not path.is_file():
        return None
    m = re.search(r"^\s*allow_implicit_invocation:\s*(true|false)\s*$", path.read_text(encoding="utf-8"), re.M)
    return None if m is None else m.group(1) == "true"


# ---------------------------------------------------------------- checks


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    try:
        data, meta, body = frontmatter((skill_dir / "SKILL.md").read_text(encoding="utf-8"))
    except ValueError as e:
        return [f"{skill_dir.name}: {e}"]
    extra = set(data) - ALLOWED_KEYS
    if extra:
        errors.append(f"unexpected frontmatter keys (claude.ai upload fails on them): {sorted(extra)}")
    name = data.get("name", "")
    if not (1 <= len(name) <= 64 and NAME_RE.match(name)):
        errors.append(f"invalid name {name!r}")
    if name != skill_dir.name:
        errors.append(f"name {name!r} != folder {skill_dir.name!r}")
    if not name.startswith(SKILL_PREFIX):
        errors.append(f"name {name!r} lacks the {SKILL_PREFIX!r} prefix (spec D9)")
    desc = data.get("description", "")
    if not 1 <= len(desc) <= 1024:
        errors.append(f"description length {len(desc)} not in 1..1024")
    if "<" in desc or ">" in desc:
        errors.append("description contains angle brackets")
    if len(data.get("compatibility", "")) > 500:
        errors.append("compatibility > 500 chars")
    if data.get("license") != "MIT":
        errors.append("license must be MIT")
    for key in REQUIRED_META:
        if not meta.get(key):
            errors.append(f"metadata.{key} missing")
    for d in FORBIDDEN_SOURCE_DIRS:
        if (skill_dir / d).exists():
            errors.append(f"{d}/ must not be in a source skill folder (spec §7.5)")
    n = len(body.splitlines())
    if n > MAX_BODY_LINES:
        errors.append(f"body {n} lines > {MAX_BODY_LINES}")
    for link in re.findall(r"\]\(([^)#]+)\)", body):
        if not link.startswith("http") and not (skill_dir / link).exists():
            errors.append(f"broken relative link {link}")
    policy = openai_policy(skill_dir)
    if policy is None:
        errors.append("agents/openai.yaml missing or has no policy.allow_implicit_invocation")
    elif name in EXPECTED_IMPLICIT and policy != EXPECTED_IMPLICIT[name]:
        errors.append(f"allow_implicit_invocation is {policy}, spec §7.3 says {EXPECTED_IMPLICIT[name]}")
    short = openai_short_description(skill_dir)
    if short is None or not SHORT_DESC_MIN <= len(short) <= SHORT_DESC_MAX:
        errors.append(f"agents/openai.yaml short_description must be {SHORT_DESC_MIN}-{SHORT_DESC_MAX} chars (OpenAI UI guidance)")
    for ko in sorted((skill_dir / "references" / "ko").glob("*.md")):
        head = ko.read_text(encoding="utf-8").replace("\r\n", "\n").split("\n")[:4]
        if tuple(line.split(":")[0] + ":" for line in head) != KO_HEADER:
            errors.append(f"references/ko/{ko.name}: must start with {', '.join(KO_HEADER)} (spec L4)")
        if f"references/ko/{ko.name}" not in body:
            errors.append(f"references/ko/{ko.name} is not named in SKILL.md (spec L5)")
    return [f"{skill_dir.name}: {e}" for e in errors]


def validate_names(names: list[str]) -> list[str]:
    """No skill name is a prefix of another (first-word invocation, spec §4)."""
    errors = []
    for a in names:
        for b in names:
            if a != b and b.startswith(a):
                errors.append(f"skill name {a!r} is a prefix of {b!r}")
    if set(names) != set(EXPECTED_IMPLICIT):
        errors.append(f"skill set {sorted(names)} != spec §4 {sorted(EXPECTED_IMPLICIT)}")
    return errors


def validate_manifest() -> list[str]:
    try:
        data = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        return [f"plugin-manifest.json: {e}"]
    errors = []
    if data.get("name") != "dia":
        errors.append("name must be 'dia' (spec §4)")
    if data.get("displayName") != "Dialectic Skills":
        errors.append("displayName must be 'Dialectic Skills' (spec §4)")
    for key in ("version", "description", "author", "license", "homepage", "repository"):
        if not data.get(key):
            errors.append(f"{key} missing (spec §7.4)")
    if "skills" in data:
        errors.append("'skills' key: skills/ is scanned by default")
    if HANGUL_RE.search(json.dumps(data, ensure_ascii=False)):
        errors.append("contains Hangul (spec L1)")
    return [f"plugin-manifest.json: {e}" for e in errors]


def validate_marketplace() -> list[str]:
    try:
        data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        return [f"marketplace.json: {e}"]
    errors = []
    if data.get("name") != "dialectic-skills":
        errors.append("name must be 'dialectic-skills'")
    plugins = data.get("plugins", [])
    if [(p.get("name"), p.get("source")) for p in plugins] != [("dia", "./plugins/dia")]:
        errors.append("must list exactly one plugin: dia -> ./plugins/dia")
    return [f".claude-plugin/marketplace.json: {e}" for e in errors]


def validate_plugin_readme(files: dict[str, bytes]) -> list[str]:
    text = files.get("README.md", b"").decode("utf-8")
    words = len(re.sub(r"```.*?```", "", text, flags=re.S).split())
    if words < README_MIN_WORDS:
        return [f"packaging/plugin-README.md: {words} words outside code blocks, need {README_MIN_WORDS} (Anthropic directory)"]
    return []


def _one_line(s: object) -> bool:
    return isinstance(s, str) and s.strip() != "" and "\n" not in s and "\r" not in s


def validate_openai_interface(interface: dict, assets: dict[str, bytes]) -> list[str]:
    """The OpenAI directory's final-submission rules for interface fields and images."""
    e = []
    if not (_one_line(interface.get("displayName")) and len(interface["displayName"]) <= 30):
        e.append("displayName: one line, at most 30 characters")
    if not (_one_line(interface.get("shortDescription")) and len(interface["shortDescription"]) <= 30):
        e.append("shortDescription: one line, at most 30 characters")
    long = interface.get("longDescription")
    if not (isinstance(long, str) and long.strip() and len(long) <= 4000):
        e.append("longDescription: required, at most 4,000 characters")
    if not (_one_line(interface.get("developerName")) and len(interface["developerName"]) <= 80):
        e.append("developerName: one line, at most 80 characters")
    if interface.get("category") not in OPENAI_CATEGORIES:
        e.append(f"category must be one of {sorted(OPENAI_CATEGORIES)}")
    caps = interface.get("capabilities", [])
    if len(caps) > 20 or not all(_one_line(c) and len(c) <= 120 for c in caps):
        e.append("capabilities: at most 20, each one line and at most 120 characters")
    prompts = interface.get("defaultPrompt", [])
    if isinstance(prompts, str):
        prompts = [prompts]
    if len(prompts) > 3 or len(set(prompts)) != len(prompts) or not all(
        _one_line(p) and len(p) <= 128 and "@" not in p for p in prompts
    ):
        e.append("defaultPrompt: at most 3 unique one-line prompts of at most 128 characters, no @mention")
    for key in ("websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"):
        if key in interface and not (isinstance(interface[key], str) and interface[key].startswith("https://") and len(interface[key]) <= 1024):
            e.append(f"{key}: an https:// URL of at most 1,024 characters")
    for key in ("logo", "composerIcon"):
        path = interface.get(key, "")
        if not (isinstance(path, str) and path.startswith("./assets/") and path.endswith(".svg")):
            e.append(f"{key}: must be ./assets/<name>.svg")
            continue
        data = assets.get(path[2:])
        if data is None:
            e.append(f"{key}: {path} not found in packaging/openai/")
            continue
        m = re.search(r'<svg\b[^>]*\bviewBox="0 0 (\d+(?:\.\d+)?) (\d+(?:\.\d+)?)"', data.decode("utf-8"))
        if not m or m.group(1) != m.group(2) or float(m.group(1)) < 48 or float(m.group(1)) > 4096:
            e.append(f"{key}: SVG needs a square numeric viewBox between 48 and 4,096")
    return [f"packaging/openai/interface.json: {x}" for x in e]


def openai_parts() -> tuple[dict, dict[str, bytes]]:
    interface = json.loads(OPENAI_DIR.joinpath("interface.json").read_text(encoding="utf-8"))
    assets = {
        f"assets/{f.name}": _normalized(f) for f in sorted((OPENAI_DIR / "assets").glob("*")) if f.is_file()
    }
    return interface, assets


def openai_files(files: dict[str, bytes]) -> dict[str, bytes]:
    """The OpenAI directory upload: Codex manifest with interface, plus image assets (spec D32)."""
    interface, assets = openai_parts()
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    manifest.pop("displayName", None)  # interface.displayName carries it in the Codex manifest
    manifest["skills"] = "./skills/"
    manifest["interface"] = interface
    out = {k: v for k, v in files.items() if not k.startswith(".claude-plugin/")}
    out[".codex-plugin/plugin.json"] = (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode()
    out.update(assets)
    return out


def shipped_violations(files: dict[str, bytes]) -> list[str]:
    """Forbidden paths, non-text files, Hangul outside references/ko/ (spec §7.1, §6)."""
    errors = []
    for rel, data in sorted(files.items()):
        parts = rel.split("/")
        if parts[0] == "upstream" or "upstream" in parts:
            errors.append(f"{rel}: upstream/ material is never shipped")
        if FORBIDDEN_SHIPPED_DIRS & set(parts[:-1]):
            errors.append(f"{rel}: scripts/, bin/, hooks/ and monitors/ are not allowed")
        if parts[-1] in FORBIDDEN_SHIPPED_FILES:
            errors.append(f"{rel}: MCP/LSP config is not allowed")
        if Path(rel).suffix not in SHIPPED_SUFFIXES:
            errors.append(f"{rel}: only .md, .json, .yaml files are shipped")
        try:
            text = data.decode("utf-8")
        except UnicodeDecodeError:
            errors.append(f"{rel}: not UTF-8 text")
            continue
        if KO_DIR not in "/" + rel and HANGUL_RE.search(text):
            errors.append(f"{rel}: Hangul outside references/ko/ (spec L1)")
    return errors


def crossref_violations(files: dict[str, bytes], names: list[str]) -> list[str]:
    """Every dia-* name mentioned exists; old skill names appear only in metadata.lineage."""
    errors = []
    known = set(names)
    for rel, data in sorted(files.items()):
        if not rel.endswith((".md", ".yaml")):
            continue
        for lineno, line in enumerate(data.decode("utf-8").split("\n"), 1):
            line = re.sub(r"https?://\S+", "", line)  # URLs are not skill references
            if line.lstrip().startswith("lineage:"):
                continue  # lineage records former names, including dia-intent
            for ref in SKILL_REF_RE.findall(line):
                if ref not in known:
                    errors.append(f"{rel}:{lineno}: unknown skill {ref!r}")
            old = OLD_NAMES_RE.search(line)
            if old:
                errors.append(f"{rel}:{lineno}: old skill name {old.group(0)!r}")
    return errors


# ---------------------------------------------------------------- build


def _normalized(path: Path) -> bytes:
    return path.read_bytes().replace(b"\r\n", b"\n")


def plugin_files(skills: list[Path]) -> dict[str, bytes]:
    """Keys are paths relative to the plugin folder."""
    files = {".claude-plugin/plugin.json": _normalized(MANIFEST), "README.md": _normalized(PLUGIN_README)}
    for skill_dir in skills:
        for f in sorted(skill_dir.rglob("*")):
            if f.is_file() and "__pycache__" not in f.parts and f.name != ".DS_Store":
                files[f"skills/{skill_dir.name}/{f.relative_to(skill_dir).as_posix()}"] = _normalized(f)
    return files


def plugin_name() -> str:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))["name"]


def zip_bytes(files: dict[str, bytes]) -> bytes:
    top = plugin_name()
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_STORED) as zf:
        for rel in sorted(files):
            info = zipfile.ZipInfo(f"{top}/{rel}", (1980, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_STORED
            info.create_system = 3  # unix; ZipInfo defaults to 0 on Windows
            info.external_attr = 0o644 << 16
            zf.writestr(info, files[rel])
    return buf.getvalue()


def content_digest(files: dict[str, bytes]) -> str:
    """sha256 over the plugin files minus the manifest, plus the OpenAI listing and assets,
    so a version bump alone leaves it unchanged and any shipped change needs one."""
    h = hashlib.sha256()
    extra = {}
    if OPENAI_DIR.is_dir():
        interface, assets = openai_parts()
        extra = {"openai:interface.json": json.dumps(interface, sort_keys=True).encode()}
        extra.update({f"openai:{k}": v for k, v in assets.items()})
    for rel, data in sorted({**files, **extra}.items()):
        if rel != ".claude-plugin/plugin.json":
            h.update(rel.encode() + b"\0" + data + b"\0")
    return h.hexdigest()


def _release_state(files: dict[str, bytes]) -> tuple[str, str, dict]:
    version = json.loads(MANIFEST.read_text(encoding="utf-8"))["version"]
    try:
        recorded = json.loads(RELEASE.read_text(encoding="utf-8"))
    except FileNotFoundError:
        recorded = {}
    return version, content_digest(files), recorded


def _bump_error(version: str) -> str:
    return f"skill files changed since plugin {version}: bump version in plugin-manifest.json, then run tools/package.py"


def check_release(files: dict[str, bytes]) -> list[str]:
    version, digest, recorded = _release_state(files)
    if recorded.get("version") != version:
        return [f"plugin-release.json records {recorded.get('version')!r}, plugin-manifest.json says {version!r}: run tools/package.py"]
    if recorded.get("digest") != digest:
        return [_bump_error(version)]
    return []


def record_release(files: dict[str, bytes]) -> list[str]:
    version, digest, recorded = _release_state(files)
    if recorded.get("version") == version and recorded.get("digest") != digest:
        return [_bump_error(version)]
    RELEASE.write_bytes((json.dumps({"version": version, "digest": digest}, indent=2) + "\n").encode())
    return []


def check_generated(files: dict[str, bytes]) -> list[str]:
    """plugins/dia/ and the zip match the source byte for byte (spec §12.1)."""
    errors = []
    out = PLUGINS / plugin_name()
    on_disk = {f.relative_to(out).as_posix(): f.read_bytes() for f in out.rglob("*") if f.is_file()} if out.is_dir() else {}
    if on_disk != files:
        stale = sorted(set(on_disk) ^ set(files)) + sorted(k for k in files if k in on_disk and on_disk[k] != files[k])
        errors.append(f"plugins/{plugin_name()}/ lags the source ({', '.join(stale[:5]) or 'missing'}): run tools/package.py")
    zpath = DIST / ZIP_NAME
    if not zpath.is_file() or zpath.read_bytes() != zip_bytes(files):
        errors.append(f"releases/{ZIP_NAME} lags the source: run tools/package.py")
    opath = DIST / OPENAI_ZIP_NAME
    if not opath.is_file() or opath.read_bytes() != zip_bytes(openai_files(files)):
        errors.append(f"releases/{OPENAI_ZIP_NAME} lags the source: run tools/package.py")
    return errors


def write_outputs(files: dict[str, bytes]) -> None:
    out = PLUGINS / plugin_name()
    if out.exists():
        for f in sorted(out.rglob("*"), reverse=True):
            f.unlink() if f.is_file() else f.rmdir()
    for rel, data in files.items():
        dest = out / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
    DIST.mkdir(parents=True, exist_ok=True)
    (DIST / ZIP_NAME).write_bytes(zip_bytes(files))
    (DIST / OPENAI_ZIP_NAME).write_bytes(zip_bytes(openai_files(files)))


def collect_errors(skills: list[Path], files: dict[str, bytes]) -> list[str]:
    names = [s.name for s in skills]
    return (
        validate_manifest()
        + validate_marketplace()
        + [e for s in skills for e in validate_skill(s)]
        + validate_names(names)
        + shipped_violations(files)
        + crossref_violations(files, names)
        + validate_plugin_readme(files)
        + validate_openai_interface(*openai_parts())
        + [f"openai zip: {e}" for e in shipped_violations({k: v for k, v in openai_files(files).items() if not k.startswith("assets/")})]
    )


def main(argv: list[str]) -> int:
    check_only = "--check" in argv
    skills = skill_dirs()
    files = plugin_files(skills)
    errors = collect_errors(skills, files)
    if not errors:
        if check_only:
            errors = check_release(files) + check_generated(files)
        else:
            errors = record_release(files)
    for e in errors:
        print("ERROR", e)
    if errors:
        return 1
    for s in skills:
        print("ok", s.name)
    if not check_only:
        write_outputs(files)
        print(f"-> plugins/{plugin_name()}/ + releases/{ZIP_NAME} + releases/{OPENAI_ZIP_NAME}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
