# writing-for-models

Work folder of branch `writing-for-models`. Everything for this work lives here, so the
branch does not touch `docs/` or any file other branches edit. Read this file first; the
decision history is in `SESSION.md`.

## What is here

| Path | What |
|---|---|
| `skill/writing-for-models/SKILL.md` | The skill: four rules for text a model reads and follows, the structure they imply, leads, and how to write, edit or review such text. Self-contained. |
| `skill/writing-for-models/references/evidence.md` | What each part rests on. The skill points to it only for when the user asks how strong a rule is or wants to change one, so it is not loaded in normal use. |
| `ab-dia-adjudicate/` | A/B test of the skill on `dia-adjudicate`: both versions, four fictional cases with an answer key, the fetch-tool simulator, prompts, all judge outputs and the scorer. Its README says how to re-run. |
| `SESSION.md` | What was done in the session that made this (2026-10-28), with the owner's rulings and the reasons. |

The skill is not part of the `dia` plugin: it is outside `skills/`, so `tools/package.py`
does not ship it and CI ignores it. It is written for any assistant that reads skills
(Claude Code plugin, claude.ai), and it assumes a sub-agent may be available but works
without one.

## State (2026-10-28)

- The skill is finished as far as the owner's review in the session went. The last
  changes were reviewed by an independent sub-agent against the skill itself, and the
  findings it rated by severity were applied.
- It is public-safe: no names, paths, hashes, versions or quotes from the author's
  private repository, where the source study was run. `evidence.md` calls that study
  "the source", the author's unpublished work. Its Fisher p-values were recomputed and
  matched; its raw data are not public.
- The A/B on `dia-adjudicate` ran three rounds (28 runs). No round showed a difference
  between A (current text) and B (rewritten by the skill's rules); results below. B is
  not applied to `skills/dia-adjudicate/` on any branch.

## A/B results

| Round | Model, sources, runs | Correct items overturned | Wrong items missed | Tokens, mean A / B (p) | Time, mean A / B (p) |
|---|---|---|---|---|---|
| r1 | Opus, local, 8 | 0 / 0 | 0 / 0 | 89,334 and 91,622 (p = 0.20)¹ | 131 s and 166 s (p = 0.11)¹ |
| r2 | Haiku, local, 8 | 0 / 0 | 0 / 0 | 116,952 / 114,733 (p = 0.49) | 175 s / 169 s (p = 0.69) |
| r3 | Haiku, summarizing fetch, 12 | 0 / 0 | 1 run / 0 | 117,037 / 120,191 (p = 0.31) | 176 s / 192 s (p = 0.24) |

¹ r1 per-run usage was not saved; the two means were reported in the session without a
record of which arm was which. The time gap was put down to concurrency at the time.

Round 3 in detail (6 runs per arm; Fisher exact on runs, Mann-Whitney on means):

- Summary traps are correct items whose support the fetch summary leaves out. No judge
  overturned one. A downgrade to "partly valid" came in A 1/6 runs and B 2/6.
- Correct items downgraded to "partly valid": A 1/6 runs, B 5/6 (p = 0.08). This is the
  nearest thing to a difference. Three of B's five are one item (case4 F1). The
  Condition-fit sentence that caps items at "partly valid" is identical in A and B. Many
  metrics were compared, and in r1 and r2 the same count was A 2/4 vs B 3/4 and 3/4 vs
  3/4. Read it as unresolved, not as an effect.
- Correct items listed in Step 6 as errors: A 1/6, B 1/6 (D3 both times). In r2, Z2 was
  listed once in each arm.
- Unraised target errors missed (any): A 2/6, B 3/6. The night-cooling claim (M5) was
  caught 1/3 in each arm. The desert claim (M6) was left "unverifiable" in B 2/3 and A 1/3
  runs, which is defensible since no arid site was studied.
- Writing-for-models Rule 3 diagnostic, asking the fetch tool a direct question before
  ruling: questions per run A 20.2, B 19.3; bare fetches A 0, B 0.8.
- Tool calls A 20.8, B 27.5 (p = 0.26).
- Judges said they did not shuffle the reports: A 2/6, B 3/6.

What this supports: B did not make judging worse in these cases, and nothing shows it
made judging better. With 2–3 runs per cell only large effects were detectable.

## Incidents (round 3)

- Run r3-07 (B): the judge sub-agent tried one command on the owner's linked computer
  (`true`, a no-op). It was refused because no folder was connected, so nothing ran.
- Run r3-12 (B): one unneeded GitHub repository-list call. Read-only; it had no effect
  on the verdicts.
- Cause: the judge prompt forbade web search and other files but not other tools. Add a
  tool restriction before the next round (`ab-dia-adjudicate/prompts/judge-fetch.md`).
- While setting up, the session author printed file hashes that revealed which blinded
  skill was A. The judges stayed blind, and all scoring was done by script.

## Open items

| # | Item | Who | Notes |
|---|---|---|---|
| 1 | Where the skill lives | owner | It stays in this folder for now. Options: (a) a project skill for this repo (`.claude/skills/writing-for-models/`), so agents editing `dia` skills load it; (b) its own repo or plugin; (c) part of `dia`. (c) conflicts with spec rules: the `dia-` name prefix, assistant-neutral text, and "no references to other projects" (its evidence names outside sources). It would need a spec decision row. |
| 2 | Apply B to `dia-adjudicate`? | owner | The evidence says no harm and no measured gain. By the skill's own A/B rule, the next step is to re-run the differing case (case4, the "partly valid" count) at 12 or more runs per arm on Haiku: 24 runs, about 2.9M tokens. The alternative is to accept B as unmeasured and say so. If applied, it goes on `adjudicate-ratchet` (or after its merge), with a `metadata.version` bump per AGENTS.md. |
| 3 | Harden the harness before more runs | agent | Restrict judge tools. Save full replies and per-run usage (r1 has none). Clear `fetchdata/log/` or use new run ids. Decide whether unshuffled runs count. |
| 4 | Check the B-arm downgrades by hand | agent | Read why B judges capped F1 at "partly valid" in r3-01/08/12: real condition-fit reasoning or noise. Full replies were not kept, so this needs new runs. |

## How to resume

1. `git checkout writing-for-models`, then read this file, `SESSION.md` and
   `ab-dia-adjudicate/README.md`.
2. To use the skill: copy `skill/writing-for-models/` into a skills folder, or invoke it
   by path ("follow the skill at writing-for-models/skill/writing-for-models/SKILL.md").
3. To change the skill: follow its own section "Writing, editing or reviewing text". The
   change is finished only after a sub-agent that did not write it has reviewed old and
   new text against SKILL.md. A meaning change needs the user's request or a Rule, and
   an A/B when an eval exercises it.
4. To re-run the A/B: see `ab-dia-adjudicate/README.md`, then score with
   `python3 -I ab-dia-adjudicate/tools/score.py r3`.
