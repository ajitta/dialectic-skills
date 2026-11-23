# Handoff

The current state and what is open, for the next session. Each fact is stated once and is true as of the date in its heading; replace a fact when it changes, do not stack dated entries. Rules are in `AGENTS.md`; what each skill does is in its `SKILL.md`. Earlier handoff entries, including the numbered items that older records cite ("handoff item 27"), are in `docs/history/handoff-to-2026-11-23.md`, which is a record and not instructions.

## Released (2026-11-24)

- Plugin `dia` 5.1.1: tag `v5.1.1` on `main` at `5c83adb` (pull request #124, spec D121, probes Parts CD and CE). Release assets match the committed zips (sha256). 5.1.0 (`v5.1.0`, #121, D120) is the release before it.
- Skill versions: dia-adjudicate, dia-conjecture, dia-counterplan, dia-reductio 4.0.0; dia-warrant 4.0.1; dia-skopos 4.2.0; dia-techne 4.2.1; dia-elenchus, dia-quaestio, dia-regula 3.1.0; dia-negative 3.1.1; dia-router 3.0.2; dia-emend, dia-ratchet 3.0.1.
- Companion `dia-panel` 0.5.0: tag `dia-panel--v0.5.0` at `694f159` (unchanged since).
- Last decision row D122, last probes part CF. **Next free: D123 and Part CG.**
- OpenAI zip on chatgpt.com: the last upload recorded is 4.1.0; the 5.1.1 zip (which carries 5.1.0's new sample prompts) is the owner's to upload.

## Open

Each waits for the owner's approval of a plan before any run or edit.

- **claude-fable-5-2 on the five 4.0.0 texts:** one cell each on a task that exists, 5 runs, when the owner says Fable is available.
- **dia-elenchus 3.2.0 (D122):** released on the owner's word as an improvement on 3.1.0; it takes the user's own cases in about half the runs. Worth a plan of its own if real use shows the made-up-case runs: a structural change (the first premise question to each definition is a case from the user's situation) rather than another sentence. dia-quaestio stays (ahead of the plain model 2 of 2, Part CE).
- **Reported and left in the repository:** none since D121, which ruled the list D119 left (README examples recorded again, the dia-conjecture figures, dia-warrant's theory source fixed, dia-adjudicate's doubt closed with no change, the review-panel figures kept, dia-panel run whole once).
- **Held back:** one run of the pilot's A/B request with the end stated and no skill, beside the floor reply (`outcome-pilot-2026-11-19/out/e-abtest-chain-run1-turn2.md`).
- **Directory listings (owner's):** the account steps in `docs/directory-submission.md` § Owner steps.

## Where the work is

- Probe batches and their records are on the owner's PC under `C:/Users/ajitta/work/dia-probes/`. The latest is `verify-six-2026-11-20/` (`REMAKE.md`; `run_six.py`; the task method in `newtasks/`; `gen_requests.py` has the simulated user write first messages).
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
