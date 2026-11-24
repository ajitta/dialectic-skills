# Handoff

The current state and what is open, for the next session. Each fact is stated once and is true as of the date in its heading; replace a fact when it changes, do not stack dated entries. Rules are in `AGENTS.md`; what each skill does is in its `SKILL.md`. Earlier handoff entries, including the numbered items that older records cite ("handoff item 27"), are in `docs/history/handoff-to-2026-11-23.md`, which is a record and not instructions.

## Released (2026-11-24)

- Plugin `dia` 5.3.0: tag `v5.3.0` on `main` at `b621ac5` (pull request #130, spec D123, probes Part CG). Release assets match the committed zips (sha256). 5.2.0 (`v5.2.0`, #128, D122) is the release before it.
- Skill versions: dia-adjudicate, dia-conjecture, dia-counterplan, dia-reductio 4.0.1; dia-warrant 4.0.2; dia-skopos 4.2.1; dia-techne 4.2.2; dia-elenchus 3.2.1; dia-negative 3.1.2; dia-quaestio, dia-regula 3.1.1; dia-router 3.0.3; dia-emend, dia-ratchet 3.0.2.
- Companion `dia-panel` 0.5.0: tag `dia-panel--v0.5.0` at `694f159` (unchanged since).
- Last decision row D123, last probes part CG. **Next free: D124 and Part CH.**
- OpenAI zip on chatgpt.com: 5.3.0, uploaded by the owner (his word, 2026-11-24); it carries 5.1.0's new sample prompts. The upload recorded before it is 4.1.0.

## Open

Each waits for the owner's approval of a plan before any run or edit. The items were analysed on 2026-11-24 with no run (ten read-only sub-agents, each named cause checked by a second one; two blind readers); the outputs are in `C:/Users/ajitta/work/dia-probes/regula-audit-2026-11-24/` (`open-items-analysis-2026-11-24.json`, `out/reading-floor3.json`, the packs `blind-floor3a/` and `blind-floor3b/`) and are not yet a part of `docs/probes.md`. The facts below include what that analysis found and the session checked in the run files.

- **Faults the runs of 5.3.0 showed and its text does not remove (D123, Part CG):**
  - dia-warrant: text for the user to send concedes flatly a cause the evidence did not show ("I accept the help center cut billing tickets") in 1 of 5 runs on the released wording: 3 of 5 before the sentence on standing was rewritten, and 1 of 5 on each of the three wordings after it. Part CG's 3, 3, 2, 2 also counts hedged lines ("likely", "Granting"). The judgment and the workload figures stood in all 20 runs. No cause is named. The best-supported candidate: the assistant grants the cause for the argument in its own voice (the plain model does too, 3 of 3 in the batch of 2026-11-20) and the grant goes into the user's text without its "say" or "suppose"; the sentence on standing still opens "is a reason for the step their knowledge is about". One run conceded with no such grant.
  - dia-negative: one of two runs edited the file two turns after the pick. The user had not said yes: he gave one of the two facts the assistant's offer asked for, and the edit wrote a line he had not seen, under the runner's `acceptEdits`. The plain model did the like on its own offer (`verify-six-2026-11-20`, `policy-plain-run2`). One of two runs inferred `user` for a text the user was about to announce; she had in fact written it, and the class changed nothing she received. The runs do not show "has said" doing better than "the conversation shows" (1 of 2 against 1 of 1). The case in which the class matters (someone else's text, an aim the user states, authorship unsaid) has not been run.
  - dia-quaestio: two asks in 2 of 9 messages of one run; in every such message on record the user answered both parts, and no cause is named.
- **Not shown for 5.3.0:**
  - dia-skopos and dia-techne against the release before: no run of 5.2.0 on the floor case exists. Two blind readers ranked ten replies to that case: the floor reply 2nd and 1st; the five of 5.3.0 at ranks 1, 5, 6, 7, 8 and 2, 3, 5, 8, 10; the four claude-opus-5-5 runs of the 4.0.0 candidates, recorded in D114 as at the floor, at 3, 4, 9, 10 and 4, 6, 7, 9. The spread Part CG reports is therefore not new with 5.3.0; the readers differ by up to five places on one reply.
  - The changes listed in D123 as not run or not reached. One of them was reached: the sign of aporia in dia-elenchus (`estall-b53-run1` holds an "I don't know" before any definition fell, and no aporia was declared). dia-reductio's wait ("only once the questions you put to the user are answered") has no stated result when no user will reply, which is how `dia-panel` calls it.
  - `companions/dia-panel`, which the audit did not review; its last whole run was on dia 5.1.1 (Part CD).
  - Held for a later change: moving the not-known limit in the four siblings of dia-warrant. In dia-warrant the move itself showed no effect.
- **claude-fable-5-2 on the five texts remade in 5.0.0:** one cell each on a task that exists, 5 runs. The owner said on 2026-11-24 that Fable is available again, so only his approval of the plan is open; run it on the texts of 5.3.0.
- **dia-elenchus (D122; 3.2.1 since D123):** 3.2.0 was released on the owner's word as an improvement on 3.1.0; it takes the user's own cases in about half the runs, and both runs of 3.2.1 in Part CG asked about made-up cases after the first test. Worth a plan of its own if real use shows the made-up-case runs: a structural change (the first premise question to each definition is a case from the user's situation) rather than another sentence. Six of the seven candidate runs of Part CF never opened `elenchus-patterns.md`, which was readable, and the one that did is the only `oncall2` run whose first test asked for her own case; the made-up runs still brought out her fork between equal counts and equal burden in general form, and missed what sits only in her facts. dia-quaestio stays (ahead of the plain model 2 of 2, Part CE).
- **Reported and left in the repository:** none since D121, which ruled the list D119 left (README examples recorded again, the dia-conjecture figures, dia-warrant's theory source fixed, dia-adjudicate's doubt closed with no change, the review-panel figures kept, dia-panel run whole once).
- **Held back:** one run of the pilot's A/B request with the end stated and no skill, beside the floor reply (`outcome-pilot-2026-11-19/out/e-abtest-chain-run1-turn2.md`).
- **Directory listings (owner's):** the account steps in `docs/directory-submission.md` § Owner steps.

## Where the work is

- Probe batches and their records are on the owner's PC under `C:/Users/ajitta/work/dia-probes/`. The latest is `regula-audit-2026-11-24/` (`PLAN.md`; `run_audit.py`, one arm on a copy of the build, with a check that the new text is in the events; `mk_tasks2.py` and `gen.py` for tasks written by sub-agents and first messages written by the simulated user; `trace_agents.py` for runs that start sub-agents). Before it, `verify-six-2026-11-20/` (`REMAKE.md`; `run_six.py`; the task method in `newtasks/`; `gen_requests.py` has the simulated user write first messages).
- `run_six.py` loads `plugins/dia` from the main checkout `C:/Users/ajitta/Repos/ajitta/dialectic-skills` and stops unless it is on `main` with no changes under `plugins/`, so a run on `main` tests the released build. To check a branch build, stay on the branch and set `DIA_ALLOW_BRANCH=1` (or point `--plugin-dir` at that branch's `plugins/dia`), and confirm in the run's events which text loaded.

## How a run is set up (Claude Code)

- `claude -p` with `--plugin-dir <absolute path to plugins/dia>`, `--model claude-opus-5-5 --effort medium`, `--output-format stream-json --verbose`, started in an empty folder outside the repository (at the repository root `CLAUDE.md` loads `AGENTS.md`, which confounds routing and language).
- Every run gets a fresh `CLAUDE_CONFIG_DIR` holding only a copy of `.credentials.json`, deleted afterwards; check `out/` for `cfg-*` folders after a crash. Set `ENABLE_CLAUDEAI_MCP_SERVERS=false`. The account's plugins and skills sync into a run's config during a turn: remove `<config>/plugins/synced` and `<config>/skills/synced` before each resumed turn, and discard a run whose `system/init` event, in any turn, lists an `@synced` plugin.
- Never run on the home configuration: its hook `~/.claude/hooks/dia-lab-before.py` changes how dia skills start.
- Reference files: with the plugin outside the working folder, a skill's `Read` of its `references/` file is denied (probes Part AL). dia-elenchus, dia-ratchet and dia-regula read references in ordinary runs, and dia-quaestio's question bank has been opened in no recorded run; for those four, pass `--add-dir` with a copy of `plugins/dia` outside the repository (never the repository folder, which shows the repository to the run) and check in the events that the read succeeded.
- A resumed `claude -p` reports cost cumulatively; tool-less runs use `--tools Skill`; cells that act on files need `--max-turns` 12 or more.

## Install surfaces (owner's observations, 2026-10-20)

- Web installs are saved to the account and reach its web and mobile apps: claude.ai (Add marketplace or zip upload) and chatgpt.com (zip upload only).
- Desktop installs stay on that computer: Claude desktop (Customize › Plugins) and Codex in the ChatGPT desktop app.
- Uploaded zips do not update; re-upload on each release. claude.ai on Add marketplace updates on Check for updates, or by itself with Sync automatically on.
- Claude mobile: the `/` menu does not list plugin skills, but a message starting with the skill's name starts it.
