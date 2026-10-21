# AGENTS.md

Guidance for coding agents (Codex, Hermes Agent, Claude Code) in this repository. Codex and Hermes read this file directly; Claude Code reads it through the `@AGENTS.md` import in `CLAUDE.md`. Claude-only notes go in `CLAUDE.md`; everything else goes here.

## What this repo is

`dialectic-skills` packages seven reasoning-and-review skills as one plugin named `dia`. The skills are general-purpose and independent of any other project: they must run unchanged on Claude (web, desktop, mobile, Claude Code), Codex and ChatGPT, including chats with no tools. `docs/spec.md` is the authority for names, layout, package rules and acceptance; surface probe results are in `docs/probes.md`; the current state and remaining work are in `docs/handoff.md`.

## Commands

```bash
python tools/package.py            # validate, then regenerate plugins/dia/ and releases/dialectic-skills.zip
python tools/package.py --check    # validate; fail if the committed output lags the source
python -m unittest discover -s tests -v
```

Release: after the version bump is on `main` with green CI, push an annotated tag `vX.Y.Z`; `.github/workflows/release.yml` attaches both zips to the GitHub release.

All are stdlib-only. CI (`.github/workflows/check.yml`) runs them plus `claude plugin validate --strict`.

## Rules

- Skill text stays assistant-neutral: write "you" or "the assistant", not a product name, and make every tool use conditional ("if a search tool is available"). No references to other projects or their commands.
- The reference material the skills were rebuilt from lives on the orphan branch `upstream` (tag `archive/upstream`), not on `main` (spec D36). It is read-only: never edit it, and never add it back to `main`, because skill directories crawl the default branch and would list the old skills as installable. Paths such as `upstream/installed/<skill>/SKILL.md` in research and review documents refer to that branch.
- The shipped package (`plugins/dia/`, `releases/dialectic-skills.zip`) is instructions only: Markdown, YAML, JSON. No scripts, hooks, binaries, MCP or LSP config (spec §7.1).
- No Hangul outside `skills/<skill>/references/ko/` (spec §6). This covers SKILL.md, `agents/openai.yaml`, manifests and other references. The README translations (`README.ko.md`, `README.ja.md`, `README.zh-CN.md`) are the one repository-level exception (spec D31).
- When `README.md` changes, update the three translations in the same commit; `tests/test_package.py` checks that they keep its structure.
- `plugins/dia/` and `releases/` are generated from `skills/`, `plugin-manifest.json` and `packaging/` (plugin README, OpenAI listing fields and images; spec D32). Edit the source, then regenerate; never hand-edit generated output.
- Changing any skill file requires a new plugin `version` in `plugin-manifest.json` and the skill's `metadata.version` (spec §12.1). Before the first install or release, a change may keep the plugin at 0.1.0 and each skill's `metadata.version` at 1.0.0 (`docs/handoff.md`, State).
- Text files use LF line endings (`.gitattributes`). On Windows, write files with LF explicitly.

## Working with the owner

- The owner writes in Korean; reply in Korean, briefly. Repository files are written in English (spec D11).
- Settle open decisions in chat before acting; list open items rather than guessing (spec §13).
