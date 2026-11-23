# Handoff

The current state and what is open, for the next session. Each fact is stated once and is true as of the date in its heading; replace a fact when it changes, do not stack dated entries. Rules are in `AGENTS.md`; what each skill does is in its `SKILL.md`. Earlier handoff entries, including the numbered items that older records cite ("handoff item 27"), are in `docs/history/handoff-to-2026-11-23.md`, which is a record and not instructions.

## Released (2026-11-23)

- Plugin `dia` 5.0.0: tag `v5.0.0` on `main` at `694f159` (pull request #115). Release assets match the committed zips.
- Skill versions: dia-adjudicate, dia-conjecture, dia-counterplan, dia-reductio, dia-warrant 4.0.0; dia-skopos 4.2.0; dia-techne 4.2.1; dia-elenchus, dia-quaestio 3.1.0; dia-negative 3.1.1; dia-emend, dia-ratchet, dia-router 3.0.1; dia-regula 3.0.0.
- Companion `dia-panel` 0.5.0: tag `dia-panel--v0.5.0` on the same commit.
- Last decision row D120 (on branch `regula-router-5.1.0`), last probes part CB. **Next free: D121 and Part CC.**
- OpenAI zip on chatgpt.com: the last upload recorded is 4.1.0; later zips are the owner's to upload.

## Open

Each waits for the owner's approval of a plan before any run or edit.

- **dia 5.1.0 (D120, branch `regula-router-5.1.0`, not released):** dia-regula 3.1.0 no longer requires two labelled outcome lines; dia-router 3.0.2's menu line for dia-skopos; the ChatGPT listing's sample prompts start with a skill's name. Before release: a check of dia-regula 3.1.0 in 4 runs (it reviews `skills/dia-skopos/SKILL.md` and reports no breach for the missing lines; it reviews a prompt that reads in the user's goal without showing it and reports that), waiting for the owner's approval.
- **claude-fable-5-2 on the five 4.0.0 texts:** one cell each on a task that exists, 5 runs, when the owner says Fable is available.
- **What "for the result" means for dia-elenchus and dia-quaestio**, the two skills that only ask: not yet planned.
- **Reported and left in the repository:** the README's example sessions for dia-elenchus, dia-quaestio, dia-negative, dia-emend and dia-ratchet predate the 3.x rewrites, and its dia-router subsection and review-panel figures quote 2.x outputs (all labelled with their version); the dia-conjecture example repeats the run's own mismatch (89 phone bookings against 66 + 26); `dia-warrant/references/theory.md` places Walton's cause-to-effect questions under the body's step from a change back to its cause; dia-adjudicate once made decisive a doubt the material already answered (D119 (4), seen in one run of two); dia-panel was not run on 5.0.0, and its dia-reductio lens has no clause for a run where no user will reply.
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
