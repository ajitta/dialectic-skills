# AGENTS.md

Guidance for coding agents (Codex, Hermes Agent, Claude Code) in this repository. Codex and Hermes read this file directly; Claude Code reads it through the `@AGENTS.md` import in `CLAUDE.md`. Claude-only notes go in `CLAUDE.md`; everything else goes here.

## What this repo is

`dialectic-skills` packages seven reasoning-and-review skills as one plugin named `dia`, for Claude Code, Codex, Claude/ChatGPT desktop and the mobile apps. `docs/spec.md` is the authority for names, layout, package rules and acceptance. Its status is "Draft for owner approval": do not start building `skills/`, `plugins/` or `tools/` until the owner approves it.

## Rules

- `upstream/` is read-only reference material (spec §11). Never edit it; its SHA-256 values in `upstream/README.md` must stay valid. It is never shipped.
- The shipped package (`plugins/dia/`, `releases/dialectic-skills.zip`) is instructions only: Markdown, YAML, JSON. No scripts, hooks, binaries, MCP or LSP config (spec §7.1). Developer scripts live in `tools/` and `tests/` only.
- No Hangul outside `skills/<skill>/references/ko/` (spec §6). This covers SKILL.md, `agents/openai.yaml`, manifests and other references.
- `plugins/dia/` and `releases/` are generated from `skills/` and `plugin-manifest.json`. Edit the source, then regenerate; never hand-edit generated output.
- Changing any skill file requires a plugin `version` bump (spec §12.1).
- Text files use LF line endings (`.gitattributes`). On Windows, write files with LF explicitly.
- Python tooling runs through `uv run`.

## Working with the owner

- The owner writes in Korean; reply in Korean, briefly. Repository files are written in English (spec D11).
- Settle open decisions in chat before acting; list open items rather than guessing (spec §13).
