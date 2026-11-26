# AGENTS.md

Guidance for coding agents in this repository. Claude Code reads it through the `@AGENTS.md` import in `CLAUDE.md`; Claude-only notes go in `CLAUDE.md`, everything else goes here.

## What this repo is

`dialectic-skills` packages thirteen reasoning-and-review skills and `dia`, the one skill that calls them, as one plugin named `dia`. Each of the thirteen is a function: one purpose, worked from what it is handed, one thing returned, and no knowledge of the others.

What is true, in this order:

1. `skills/*/SKILL.md` and their `references/` define what each skill does. Nothing else does.
2. `plugin-manifest.json`, `packaging/`, `tools/package.py` and `tests/` define the package and what is enforced.
3. `docs/handoff.md` (top section) holds the current state and the open items.
4. `docs/spec.md` holds the design in force (§3) and the package rules (§4 names, §6 language, §7 package format, §8 layout; read the section before changing descriptions, references or packaging). Where the spec disagrees with 1 or 2, the skill or the code holds and the spec is corrected.

The reason for a change goes in its commit and pull request. Evidence from runs stays in the batch folder of the run, outside the repository. The records up to plugin 5.4.2 (decision rows, probe records, research) are in git at the tag `v5.4.2`; they describe texts that no longer exist and are not instructions.

## Commands

```bash
python tools/package.py            # validate, then regenerate plugins/dia/ and both zips in releases/
python tools/package.py --check    # validate; fail if the committed output lags the source
python -m unittest discover -s tests -v
```

Release: after the version bump is on `main` with green CI, push an annotated tag `vX.Y.Z`; `.github/workflows/release.yml` attaches both zips to the GitHub release.

The tools are stdlib-only; the tests use PyYAML when it is installed. CI (`.github/workflows/check.yml`) runs them plus `claude plugin validate --strict`.

## Rules

- A skill text is written from the skill's purpose, in one order: what it is for, what it works from, what it does, what it returns (spec §3). It names no other dia skill; only `dia` names the others. It carries no protection of files, data or accounts, no limit on sending or installing, no paragraph for a particular caller, no fixed label and no list of cases.
- Skill text names no product and no other project.
- `upstream/` is read-only provenance. Never edit it; its SHA-256 values in `upstream/README.md` must stay valid. It is never shipped, and it is not a baseline for current behaviour.
- The shipped package (`plugins/dia/`, both zips in `releases/`) is instructions only: Markdown, YAML, JSON and the listing images. No scripts, hooks, binaries, MCP or LSP config.
- No Hangul in `skills/`, `packaging/`, manifests or `plugins/` (`tools/package.py` allows it only under `skills/<skill>/references/ko/`, which no skill uses now). `README.ko.md` and, in `docs/`, the owner's words are the exceptions.
- When `README.md` changes, update `README.ko.md` in the same commit; `tests/test_package.py` checks that it keeps the structure.
- The table of contracts lives in `skills/dia/SKILL.md`, and `packaging/plugin-README.md` carries the same lines; a test holds them equal.
- `plugins/dia/` and `releases/` are generated from `skills/`, `plugin-manifest.json` and `packaging/`. Edit the source, then regenerate; never hand-edit generated output.
- Changing any shipped file (a skill file or `packaging/`) requires a new plugin `version` in `plugin-manifest.json`, and a changed skill also needs a new `metadata.version`.
- Editing a skill again on an unreleased branch after its version bump: `tools/package.py` refuses because `plugin-release.json` records the earlier digest, and with output silenced the failure is easy to miss. Delete `plugin-release.json`, rebuild, and confirm the new text is in `plugins/dia/` (grep or a hash) before any run, since runs load a copy of `plugins/dia/`, not `skills/`.
- Text files use LF line endings (`.gitattributes`). On Windows, write files with LF explicitly.

## Judging a skill

The owner (2026-11-26): what matters is whether the skill's behaviour produces the right result, and whether its input, output and behaviour fit its purpose.

A skill passes a run when all four hold, each read against the skill's purpose (its opening paragraph) and the task's key:

1. **Input.** It worked from the input its purpose needs: the material that settles the matter, read itself (the user's words, the target's text, the files or data). What only the respondent can answer it asked; what was missing or contradictory it said, and did not guess.
2. **Behaviour.** It did its own job by its own method and finished it in this invocation: not another skill's job, not stopping short, not going past what its purpose is for.
3. **Output.** It returned what its purpose promises, complete and usable.
4. **Result.** The result is right on the task: checked against the key (figures recomputed, tests and commands run, facts looked up), and it serves what the user is after.

Not part of the test: word counts or reply length, whether a labelled line was printed, whether the skill's own steps were followed.

- Take each skill's purpose from its own opening paragraph; do not judge one skill by another's purpose.
- dia-elenchus is right when it brings to the surface a fork in the respondent's own thinking that they did not know of and leaves it in its record; dia-quaestio when its brief's next step tests the assumption that most threatens what the idea is for (owner, 2026-11-24).
- For dia-skopos and dia-techne, the owner's floor of excellence (2026-11-19, set for now) is the reply in `C:/Users/ajitta/work/dia-probes/outcome-pilot-2026-11-19/out/e-abtest-chain-run1-turn2.md`.
- The key is written before the runs, from the task's own material, and one auditor checks it against that material. A key that rests on a named theory is checked against a primary source.
- One reader per run gives pass or fail on each of the four with the evidence, and a checker confirms any fail. Two texts on one task are read blind, as packets under neutral names with whatever tells them apart cut out. The session reads every reply, and the owner sees the verdicts with the replies.
- One pair cannot show that a text is better; it can show a gross loss: a line of the key that the released text meets and the new one misses. Then both are run twice more on that task, and it is a loss when the new text misses the line in at least 2 of its 3 runs and the released text meets it in at least 2 of 3.
- When a run shows a fault, change what in the design causes it and run that skill once more; never add a sentence, case or exception per symptom. If the cause cannot be named, leave the fault and report it.

## Runs

- No run without the owner's approval of a written plan: the runs and their total, the task, the key, and the decision it informs. Propose the smallest batch that decides, read results while it runs, and stop once the answer is clear.
- The engine is claude-fable-5-2 at effort high on Claude Code, every skill started by its name as the first word. The simulated user runs on claude-fable-5-2 at effort low; readers, reviewers and auditors on claude-fable-5-2 at effort high. No other model is run.
- The simulated user writes every first message where the task has a persona, and answers in a dialogue; the session gives it the persona and does not write the request itself. In a comparison, the rule that ends a dialogue is fixed before the runs and is the same in every arm.
- A run uses a fresh configuration folder and a copy of the built plugin at a neutral path, never the home configuration; `docs/handoff.md` has the runner's facts.
- Each new or changed skill text gets one independent review before its run, by a sub-agent that is given the text it replaces and asked two things: what would harm the user or defeat the skill's purpose, and which behaviour of the replaced text that the purpose needs the new text no longer produces. A fix of a finding is read again by the same reviewer.
- An edit that changes only form is checked by one independent review instead of a run.

## Review findings (owner, 2026-11-13)

- Fix only a finding under which a model would act wrongly in an ordinary case; report the others with the change and leave their text as it is.
- Three things are not grounds for leaving a fault (owner, 2026-11-24): that its harm is low or it shows only in some runs; that the behaviour was never run and no wrong act was seen; and that an earlier decision made the text deliberate. Judge that decision on its merits.
- A fix that adds words names the words it removes, or says that it removes none and why the addition is still needed.
- Ask a reviewer for what would harm the user or defeat the skill's purpose, a few findings at most, not for every condition lost.

## Working with the owner

- The owner's charge to every session (2026-11-24): "You are the owner and long-term maintainer of this codebase, and its design is up to you." Design decisions are the session's to make and to defend with evidence; the approval steps below still hold.
- The owner writes in Korean; reply in Korean, briefly. Repository files are written in English.
- The session owns the skills' outcome: bring one whole plan with its decisions made, its reasons and evidence, not a list of rulings for him, and hold your own work to the measure the skills are held to.
- His answers in a design discussion are premises, not decisions (2026-11-26): where your judgment finds a better way, propose it. His approval of a plan is what decides.
- Runs, releases and every edit outside `docs/` wait for his approval of the plan. Reading files and preparing a plan need none. Under `docs/`, the spec and the handoff may be brought up to date with the skills without asking. An approval covers the step it was given for, not the next one.
- Sub-agents are started one at a time for reviews and readings; a workflow only when he asks for one.
- A fact only the owner holds (a preference, an account step, what he observed) is asked, not guessed.
