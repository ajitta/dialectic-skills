# AGENTS.md

Guidance for coding agents (Codex, Hermes Agent, Claude Code) in this repository. Codex and Hermes read this file directly; Claude Code reads it through the `@AGENTS.md` import in `CLAUDE.md`. Claude-only notes go in `CLAUDE.md`; everything else goes here.

## What this repo is

`dialectic-skills` packages thirteen reasoning-and-review skills as one plugin named `dia`; its marketplace also lists `dia-panel`, a Claude Code-only companion workflow (spec D69). The skills are general-purpose and independent of any other project: they must run unchanged on Claude (web, desktop, mobile, Claude Code), Codex and ChatGPT, including chats with no tools. `docs/spec.md` is the authority for names, layout, package rules and acceptance; surface probe results are in `docs/probes.md`; the current state and remaining work are in `docs/handoff.md`.

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
- `upstream/` is read-only reference material (spec §11). Never edit it; its SHA-256 values in `upstream/README.md` must stay valid. It is never shipped.
- The shipped package (`plugins/dia/`, `releases/dialectic-skills.zip`) is instructions only: Markdown, YAML, JSON. No scripts, hooks, binaries, MCP or LSP config (spec §7.1).
- No Hangul outside `skills/<skill>/references/ko/` (spec §6). This covers SKILL.md, `agents/openai.yaml`, manifests and other references. The README translations (`README.ko.md`, `README.ja.md`, `README.zh-CN.md`) are the one repository-level exception (spec D31).
- When `README.md` changes, update the three translations in the same commit; `tests/test_package.py` checks that they keep its structure.
- `plugins/dia/` and `releases/` are generated from `skills/`, `plugin-manifest.json` and `packaging/` (plugin README, OpenAI listing fields and images; spec D32). Edit the source, then regenerate; never hand-edit generated output.
- Changing any skill file requires a new plugin `version` in `plugin-manifest.json` and the skill's `metadata.version` (spec §12.1). Before the first install or release, a change may keep the plugin at 0.1.0 and each skill's `metadata.version` at 1.0.0 (`docs/handoff.md`, State).
- Editing a skill again on an unreleased branch after its version bump: `tools/package.py` refuses because `plugin-release.json` records the earlier digest, and with output silenced the failure is easy to miss. Delete `plugin-release.json`, rebuild, and confirm the new text is in `plugins/dia/` (grep or a hash) before any probe or eval run, since runs load `plugins/dia/`, not `skills/`.
- `companions/dia-panel/` is a hand-maintained, Claude Code-only companion plugin (spec D69): a JavaScript workflow, outside the dia package and both zips. A change to it needs a new `version` in its `plugin.json` and in its marketplace entry (`tools/package.py --check` compares them) and a tag `dia-panel--v<version>`; it does not change the dia version.
- Text files use LF line endings (`.gitattributes`). On Windows, write files with LF explicitly.

## Probes and evals (owner, 2026-11-04)

- Before a probe or eval batch, write the plan: cells × runs × engines = total, and the decision it informs. Ask the owner first when the total is over 30 runs.
- Runs per cell: 1 to confirm unchanged or expected behaviour, 2 for a changed behaviour. Raise to 5 only when results disagree with the expectation or between arms or engines; use 10 or more only for an arm-against-arm figure the release notes will quote.
- Read results while the batch runs and stop it once the answer is clear.
- One engine by default; add Codex, at 1 run per cell, only when Codex-specific text or the skill listing changed.
- Rerun a baseline arm only when the record will compare arms; otherwise check the changed build against its expected behaviour and reuse earlier results.
- Form-only edits (provenance moved out, sections merged) are checked by one independent review instead of runs.
- A comparison whose arms hold a dialogue with a simulated user follows rule 6 of `docs/writing-for-models/README.md` § Rules for A/B records, wherever its record sits (owner, 2026-11-11; spec D70).

## Review findings (owner, 2026-11-13)

- Fix only a finding under which a model would act wrongly in an ordinary case; report the others with the change and leave their text as it is.
- A fix that adds words names the words it removes, or says that it removes none and why the addition is still needed.

## Working with the owner

- The owner writes in Korean; reply in Korean, briefly. Repository files are written in English (spec D11).
- Settle open decisions in chat before acting; list open items rather than guessing (spec §13).
