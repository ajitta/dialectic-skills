# AGENTS.md

Guidance for coding agents (Codex, Hermes Agent, Claude Code) in this repository. Codex and Hermes read this file directly; Claude Code reads it through the `@AGENTS.md` import in `CLAUDE.md`. Claude-only notes go in `CLAUDE.md`; everything else goes here.

## What this repo is

`dialectic-skills` packages thirteen reasoning-and-review skills and the `dia-router` entry point as one plugin named `dia`; its marketplace also lists `dia-panel`, a Claude Code-only companion workflow. The skills are general-purpose and independent of any other project: they must run unchanged on Claude (web, desktop, mobile, Claude Code), Codex and ChatGPT, including chats with no tools.

What is true, in this order:

1. `skills/*/SKILL.md` and their `references/` define what each skill does. Nothing else does.
2. `plugin-manifest.json`, `packaging/`, `tools/package.py` and `tests/` define the package and what is enforced.
3. `docs/handoff.md` (top section) holds the current state, the open items and the next free decision and probe numbers.
4. `docs/spec.md` is the decision record: why things are as they are. Where it disagrees with 1 or 2, the skill or the code holds and the spec is corrected. Search it for earlier rulings on a topic (grep with several synonyms, including "not done", "dropped", "declined"); do not read it whole.
5. `docs/probes.md`, `docs/skill-effect.md`, `docs/token-cost.md`, `docs/research/`, `docs/writing-for-models/` and `docs/history/` are records of past versions. They are evidence about the text they measured, not instructions and not a description of the current skills.

## Commands

```bash
python tools/package.py            # validate, then regenerate plugins/dia/ and both zips in releases/
python tools/package.py --check    # validate; fail if the committed output lags the source
python -m unittest discover -s tests -v
```

Release: after the version bump is on `main` with green CI, push an annotated tag `vX.Y.Z`; `.github/workflows/release.yml` attaches both zips to the GitHub release.

The tools are stdlib-only; the tests use PyYAML when it is installed. CI (`.github/workflows/check.yml`) runs them plus `claude plugin validate --strict`.

## Rules

- Skill text stays assistant-neutral: write "you" or "the assistant", not a product name, and make every tool use conditional ("if a search tool is available"). No references to other projects or their commands.
- `upstream/` is read-only provenance. Never edit it; its SHA-256 values in `upstream/README.md` must stay valid. It is never shipped, and it is not a baseline for current behaviour.
- The shipped package (`plugins/dia/`, both zips in `releases/`) is instructions only: Markdown, YAML, JSON and the listing images. No scripts, hooks, binaries, MCP or LSP config.
- No Hangul in `skills/`, `packaging/`, manifests or `plugins/` (`tools/package.py` allows it only under `skills/<skill>/references/ko/`, which no skill uses now). The README translations (`README.ko.md`, `README.ja.md`, `README.zh-CN.md`) and the owner's quoted words in `docs/` are the exceptions.
- When `README.md` changes, update the three translations in the same commit; `tests/test_package.py` checks that they keep its structure.
- `plugins/dia/` and `releases/` are generated from `skills/`, `plugin-manifest.json` and `packaging/`. Edit the source, then regenerate; never hand-edit generated output.
- Changing any shipped file (a skill file or `packaging/`) requires a new plugin `version` in `plugin-manifest.json`, and a changed skill also needs a new `metadata.version`.
- Editing a skill again on an unreleased branch after its version bump: `tools/package.py` refuses because `plugin-release.json` records the earlier digest, and with output silenced the failure is easy to miss. Delete `plugin-release.json`, rebuild, and confirm the new text is in `plugins/dia/` (grep or a hash) before any probe or eval run, since runs load `plugins/dia/`, not `skills/`.
- `companions/dia-panel/` is a hand-maintained, Claude Code-only companion plugin: a JavaScript workflow, outside the dia package and both zips. A change to it needs a new `version` in its `plugin.json` and in its marketplace entry (`tools/package.py --check` compares them) and a tag `dia-panel--v<version>`; it does not change the dia version.
- Text files use LF line endings (`.gitattributes`). On Windows, write files with LF explicitly.

## Judging a skill (owner, 2026-11-19 and 2026-11-22)

- Take each skill's purpose from the opening paragraph of its SKILL.md, one skill at a time; do not judge one skill by another's purpose.
- A skill that does work (dia-skopos, dia-techne, dia-emend, dia-ratchet, dia-regula's writing) is judged by what its reply achieves for the outcome the user is ultimately after, against a target reply written before the runs, on a task whose end can be checked.
- A skill that examines a position or a text is judged by what the examination brings out that was not known (verified, false alarms counted), whether its judgment at the end is right, whether it holds under insistence and yields to a real correction, and what it cost.
- Word counts, reply length, whether a labelled line was printed and whether the skill's own steps were followed are not measures of a skill. Compression means cutting waste (what the model does anyway, what is said twice, needless examples), not making text or replies shorter.
- When a run or a review shows a fault, change what in the design causes it; do not add a sentence, case or exception per symptom. If the cause cannot be named, leave the fault and report it. A small imperfection is acceptable. Each skill carries only what belongs to its own purpose; what belongs to another skill's work goes there by a hand-over.
- For dia-skopos and dia-techne, the owner's floor of excellence (2026-11-19, set for now) is the reply in `C:/Users/ajitta/work/dia-probes/outcome-pilot-2026-11-19/out/e-abtest-chain-run1-turn2.md`.

## Probes and evals

- No run without the owner's approval of a written plan: cells × runs × engine = total, the task, the target reply, and the decision it informs. Propose the smallest batch that decides.
- Runs per cell: 1 to confirm unchanged or expected behaviour, 2 for a changed behaviour. Raise to 5 only when results disagree with the expectation or between arms; use 10 or more only for an arm-against-arm figure the release notes will quote.
- Read results while the batch runs and stop it once the answer is clear.
- The engine is claude-opus-5-5 at effort medium (or low), on Claude Code only. No Sonnet, Haiku, Codex, ChatGPT or claude.ai run, and a record does not list them among what was not run; a released text is unverified on those surfaces unless a record says otherwise.
- Sub-agents (readers, reviewers, task writers, auditors) run `model: opus` at effort high. No claude-fable-5-2, for runs or sub-agents, until the owner says it is available again (temporary, owner 2026-11-23).
- Rerun a baseline arm only when the record will compare arms; otherwise check the changed build against its expected behaviour and reuse earlier results. The baseline is the plain model given the same request without the skill; read what that arm was actually sent.
- The simulated user writes every first message, file tasks included; the session gives it the persona and does not write the request itself. Keep each task inside the skill's category.
- In a comparison whose arms hold a dialogue with a simulated user: the protocol fixes when a dialogue ends and applies it the same way in every arm; every skill arm loads its skill through the same mechanism; an answer key that rests on a named theory is checked against a primary source before the runs.
- Form-only edits (provenance moved out, sections merged) are checked by one independent review instead of runs.

## Review findings (owner, 2026-11-13)

- Fix only a finding under which a model would act wrongly in an ordinary case; report the others with the change and leave their text as it is.
- A fix that adds words names the words it removes, or says that it removes none and why the addition is still needed.
- Ask a reviewer for what would harm the user or defeat the skill's purpose, a few findings at most, not for every condition lost.

## Working with the owner

- The owner writes in Korean; reply in Korean, briefly. Repository files are written in English.
- The session owns the skills' outcome: bring one whole plan with its decisions made, its reasons and evidence, not a list of rulings for him, and hold your own work to the measure the skills are held to.
- Runs, edits to a skill or to `packaging/`, and releases wait for his approval of the plan. Reading files and preparing a plan need none, and documentation under `docs/` may be brought up to date with the skills without asking. An approval covers the step it was given for, not the next one.
- When he says a reply of his is not yet a decision, ask him to confirm wherever your judgment differs from it.
