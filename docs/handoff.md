# Handoff

The current state and what is open, for the next session. Each fact is stated once and is true as of the date in its heading; replace a fact when it changes, do not stack dated entries. Rules are in `AGENTS.md`; what each skill does is in its `SKILL.md`. Earlier handoff entries, including the numbered items that older records cite ("handoff item 27"), are in `docs/history/handoff-to-2026-11-23.md`, which is a record and not instructions.

## Released (2026-11-24)

- Plugin `dia` 5.3.0: tag `v5.3.0` on `main` at `b621ac5` (pull request #130, spec D123, probes Part CG). Release assets match the committed zips (sha256). 5.2.0 (`v5.2.0`, #128, D122) is the release before it.
- Skill versions: dia-adjudicate, dia-conjecture, dia-counterplan, dia-reductio 4.0.1; dia-warrant 4.0.2; dia-skopos 4.2.1; dia-techne 4.2.2; dia-elenchus 3.2.1; dia-negative 3.1.2; dia-quaestio, dia-regula 3.1.1; dia-router 3.0.3; dia-emend, dia-ratchet 3.0.2.
- Companion `dia-panel` 0.5.0: tag `dia-panel--v0.5.0` at `694f159` (unchanged since).
- Last decision row D123, last probes part CG. **Next free: D124 and Part CH.**
- OpenAI zip on chatgpt.com: 5.3.0, uploaded by the owner (his word, 2026-11-24); it carries 5.1.0's new sample prompts. The upload recorded before it is 4.1.0.

## Open

Each waits for the owner's approval of a plan before any run or edit.

- **Faults the runs of 5.3.0 showed and its text does not remove (D123, Part CG):** dia-warrant writes a concession of what the evidence did not show into text for the user to send ("I accept ...") in 2 of 5 runs, after four wordings, cause not found; dia-negative edited the file two turns after an option was picked in 1 of 2 runs and inferred `user` for a text the user was about to announce in 1 of 2; dia-quaestio joined two asks in 2 of 9 messages of one run. Each needs a plan of its own.
- **Not shown for 5.3.0:** whether dia-skopos and dia-techne work as well as 4.2.x on the floor case (a blind reader put the floor reply first, 2 of 5 new replies close and 2 clearly below, and no 4.2.x run was read beside them: three runs of the released 5.2.0 on `floor`, read with these, would settle it); the changes listed in D123 as not run or not reached; `companions/dia-panel`, which the audit did not review. Held for a later change: moving the not-known limit in the four siblings of dia-warrant.
- **claude-fable-5-2 on the five texts remade in 5.0.0:** one cell each on a task that exists, 5 runs. The owner said on 2026-11-24 that Fable is available again, so only his approval of the plan is open; run it on the texts of 5.3.0.
- **dia-elenchus (D122; 3.2.1 since D123):** 3.2.0 was released on the owner's word as an improvement on 3.1.0; it takes the user's own cases in about half the runs, and both runs of 3.2.1 in Part CG asked about made-up cases after the first test. Worth a plan of its own if real use shows the made-up-case runs: a structural change (the first premise question to each definition is a case from the user's situation) rather than another sentence. dia-quaestio stays (ahead of the plain model 2 of 2, Part CE).
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
- Reference files: with the plugin outside the working folder, a skill's `Read` of its `references/` file is denied (probes Part AL). dia-elenchus, dia-quaestio, dia-ratchet and dia-regula read references in ordinary runs; for those, pass `--add-dir` with a copy of `plugins/dia` outside the repository (never the repository folder, which shows the repository to the run) and check in the events that the read succeeded.
- A resumed `claude -p` reports cost cumulatively; tool-less runs use `--tools Skill`; cells that act on files need `--max-turns` 12 or more.

## Install surfaces (owner's observations, 2026-10-20)

- Web installs are saved to the account and reach its web and mobile apps: claude.ai (Add marketplace or zip upload) and chatgpt.com (zip upload only).
- Desktop installs stay on that computer: Claude desktop (Customize › Plugins) and Codex in the ChatGPT desktop app.
- Uploaded zips do not update; re-upload on each release. claude.ai on Add marketplace updates on Check for updates, or by itself with Sync automatically on.
- Claude mobile: the `/` menu does not list plugin skills, but a message starting with the skill's name starts it.
