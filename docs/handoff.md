# Handoff

The current state and what is open, for the next session. Each fact is stated once and is true as of the date in its heading; replace a fact when it changes, do not stack dated entries. Rules are in `AGENTS.md`; what each skill does is in its `SKILL.md`. Earlier handoff entries, including the numbered items that older records cite ("handoff item 27"), are in `docs/history/handoff-to-2026-11-23.md`, which is a record and not instructions.

## Released (2026-11-24)

- Plugin `dia` 5.3.0: tag `v5.3.0` on `main` at `b621ac5` (pull request #130, spec D123, probes Part CG). Release assets match the committed zips (sha256). 5.2.0 (`v5.2.0`, #128, D122) is the release before it.
- Skill versions: dia-adjudicate, dia-conjecture, dia-counterplan, dia-reductio 4.0.1; dia-warrant 4.0.2; dia-skopos 4.2.1; dia-techne 4.2.2; dia-elenchus 3.2.1; dia-negative 3.1.2; dia-quaestio, dia-regula 3.1.1; dia-router 3.0.3; dia-emend, dia-ratchet 3.0.2.
- Companion `dia-panel` 0.5.0: tag `dia-panel--v0.5.0` at `694f159` (unchanged since).
- Last decision row D124, last probes part CH. **Next free: D125 and Part CI.**
- OpenAI zip on chatgpt.com: 5.3.0, uploaded by the owner (his word, 2026-11-24); it carries 5.1.0's new sample prompts. The upload recorded before it is 4.1.0.

## Open

Each waits for the owner's approval of a plan before any run or edit.

- **Stage 3 of the source-of-truth work: a candidate build (its plan is not yet written or approved).** The owner raised the item on 2026-11-24 and confirmed the session's reading of it (D124). Stage 1 (analyses, no run) and stage 2 (32 runs of the released text) are recorded in Part CH; the plan, tasks, runner and runs are in `C:/Users/ajitta/work/dia-probes/source-2026-11-24/`. What stage 2 left for a text change, each seen on the released text:
  - dia-skopos: in 1 of 2 runs the review proposed the request "for the result", said a bare proceed takes that, and at "Go ahead." changed three existing files the request had not pointed to. The cell's two runs disagree; raising it to 5 needs the owner's word.
  - dia-reductio: both runs asked for tonight's notice, one also for an earlier notice; where the earlier promise never came in, the new notice replaced it without mention (1 of 2; the plain model 2 of 2). Candidate: the ask moved into the question list of The reply, naming what was already said or promised, with the half that can be printed removed.
  - dia-warrant: stated that the trial had run on line 2 only, which the material does not show, in 2 of 2 runs (once in a draft to send); answered a Korean user in English; gave as fetched a claim from the part of a page its fetch had not returned. Of the five texts of D118 only dia-reductio says "in the user's language".
  - `dia-panel`: `review-panel` was called with the path alone, so its seven agents never had the fact the user had stated and both judges let the plan stand; the main session added the fact in its own summary and gave its conclusion as the panel's, and the user saw the summary, not the reports. Candidate: an argument that carries the user's words and the material, and "(target: text)" removed. A change needs dia-panel 0.6.0.
  - dia-router: its reviewers were given the user's purpose and facts in 2 of 2 runs, as the caller's English paraphrase; in one run the caller added a constraint and a hint of its own.
  - Read in the texts, not run: dia-techne's "say when a claim rests on recall" stands under "if the tools for that are available"; dia-adjudicate's second run gets "the same input" where D86 had "unchanged".
  - Statements of the assistant that nothing showed were found in almost every run, the plain arm included; no cause is named.
- **claude-fable-5-2 on the five texts remade in 5.0.0:** one cell each on a task that exists, 5 runs. The owner said on 2026-11-24 that Fable is available again, so only his approval of a plan is open; run it on the texts of 5.3.0.
- **dia-elenchus (D122; 3.2.1 since D123):** it takes the user's own cases in about half the runs. Worth a plan of its own if real use shows the made-up-case runs; the owner has not seen them in his own use (2026-11-24), so none is planned. Six of the seven candidate runs of Part CF never opened `elenchus-patterns.md`, and the one that did is the only `oncall2` run whose first test asked for her own case.
- **Closed by D124, no change:** dia-warrant's concession in text to send (about 1 run in 5, the judgment unaffected; the sentence on standing is not the cause); dia-negative's later edit and its inferred `user`; dia-quaestio's two asks; the not-run list of D123 except dia-skopos; the floor comparison and the plain run held back since D114 (the plain model ranks below every skill reply in two blind readings); the move of the not-known limit to the four siblings of dia-warrant (not done).
- **Directory listings (owner's):** the account steps in `docs/directory-submission.md` § Owner steps.

## Where the work is

- Probe batches and their records are on the owner's PC under `C:/Users/ajitta/work/dia-probes/`. The latest is `source-2026-11-24/` (`PLAN.md` with what happened; `run_source.py`: arms `rel`, `diag`, `plain` and `panel`, fixed second messages, pushes sent when the persona has its answer; `mk_tasks.py`, whose keys name the deciding source, the act that secures it and the target course; `gen.py` for first messages and the persona dry check; `show_reading.py`). Before it, `regula-audit-2026-11-24/` (`PLAN.md`; `run_audit.py`, one arm on a copy of the build, with a check that the new text is in the events; `mk_tasks2.py` and `gen.py` for tasks written by sub-agents and first messages written by the simulated user; `trace_agents.py` for runs that start sub-agents). Before it, `verify-six-2026-11-20/` (`REMAKE.md`; `run_six.py`; the task method in `newtasks/`; `gen_requests.py` has the simulated user write first messages).
- `run_six.py` loads `plugins/dia` from the main checkout `C:/Users/ajitta/Repos/ajitta/dialectic-skills` and stops unless it is on `main` with no changes under `plugins/`, so a run on `main` tests the released build. To check a branch build, stay on the branch and set `DIA_ALLOW_BRANCH=1` (or point `--plugin-dir` at that branch's `plugins/dia`), and confirm in the run's events which text loaded.

## How a run is set up (Claude Code)

- `claude -p` with `--plugin-dir <absolute path to plugins/dia>`, `--model claude-opus-5-5 --effort medium`, `--output-format stream-json --verbose`, started in an empty folder outside the repository (at the repository root `CLAUDE.md` loads `AGENTS.md`, which confounds routing and language).
- Every run gets a fresh `CLAUDE_CONFIG_DIR` holding only a copy of `.credentials.json`, deleted afterwards; check `out/` for `cfg-*` folders after a crash. Set `ENABLE_CLAUDEAI_MCP_SERVERS=false`. The account's plugins and skills sync into a run's config during a turn: remove `<config>/plugins/synced` and `<config>/skills/synced` before each resumed turn, and discard a run whose `system/init` event, in any turn, lists an `@synced` plugin.
- Never run on the home configuration: its hook `~/.claude/hooks/dia-lab-before.py` changes how dia skills start.
- Reference files: Part AL found a skill's `Read` of its `references/` file denied when the plugin is outside the working folder; on Claude Code 2.1.331 one run without `--add-dir` read dia-ratchet's reference (Part CH), so check the events either way. dia-elenchus, dia-ratchet and dia-regula read references in ordinary runs, and dia-quaestio's question bank has been opened in no recorded run; for those four, pass `--add-dir` with a copy of `plugins/dia` outside the repository (never the repository folder, which shows the repository to the run) and check in the events that the read succeeded.
- A resumed `claude -p` reports cost cumulatively; tool-less runs use `--tools Skill`; cells that act on files need `--max-turns` 12 or more.

## Install surfaces (owner's observations, 2026-10-20)

- Web installs are saved to the account and reach its web and mobile apps: claude.ai (Add marketplace or zip upload) and chatgpt.com (zip upload only).
- Desktop installs stay on that computer: Claude desktop (Customize › Plugins) and Codex in the ChatGPT desktop app.
- Uploaded zips do not update; re-upload on each release. claude.ai on Add marketplace updates on Check for updates, or by itself with Sync automatically on.
- Claude mobile: the `/` menu does not list plugin skills, but a message starting with the skill's name starts it.
