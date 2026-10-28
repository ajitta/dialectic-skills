# writing-for-models

Work folder of branch `writing-for-models`, at `docs/writing-for-models/`: the record of how the writing-for-models
draft became the `dia-instruct` skill, and its A/B on `dia-adjudicate`. Read this file
first; the decision history is in `SESSION.md`. Nothing here is shipped.

## Start here (next session)

Merged to `main` in plugin 1.6.0 (2026-10-28), together with `adjudicate-ratchet` and
`intent`; see `docs/handoff.md`, State. The owner's rulings on the items below are recorded
there and in spec D41–D43; this section is kept as the record of the branch before the merge.
The branch was complete as of commit `fad0a90`.

**How the branch is built.** `adjudicate-ratchet` was merged into it (commit `e68bf61`),
because `dia-adjudicate` exists only there. Merging this branch into `main` therefore
also brings in all of 1.5.0 (dia-ratchet rename, dia-adjudicate). A rebase with a force
push was tried first and refused; the merge leaves the same files without rewriting
pushed history.

**Waiting on the owner:**

| Decision | Where | What to decide |
|---|---|---|
| Four review findings on text from the reviewed draft | open item 5 below | Change each or keep it. The one that matters most here: "Replies are in the user's language" can be read to mean a skill file written for a Korean user is written in Korean, against this repository's English-only, no-Hangul rule for skill files. |
| dia-adjudicate 1.1.0 keeps one unresolved count | open item 2; `docs/handoff.md` item 28 | Re-test or accept. Correct items capped at "partly valid": A 1/6 vs B 5/6 runs (p = 0.08). The re-test is case4 at 12 or more runs per arm on Haiku, about 2.9M tokens, after restricting the judges' tools. |
| When to merge | `docs/handoff.md` items 23 and 27 | Merge with or after `adjudicate-ratchet`, and decide whether routing probes come first. |

**Agent work left:**

1. Routing probes for dia-instruct (`docs/handoff.md` item 27). Not run. Two risks to
   check first:
   - "recheck my draft system prompt" may go to dia-refine, whose description has no
     border toward dia-instruct;
   - routine edits such as "add the test command to CLAUDE.md" may load dia-instruct and
     its review step.
2. Replace the README example for dia-instruct with a shortened recorded run once 1.6.0
   is installed. The current example is labelled an illustration. The project page
   (`site/`) does not show dia-instruct (`docs/handoff.md` item 29).
3. The Japanese and Chinese README text for 1.6.0 was written by an agent and not read
   by a native speaker (`docs/handoff.md` item 14c).
4. The fixes made after the independent review were self-checked only. Before release,
   have a sub-agent that did not write them review `skills/dia-instruct/SKILL.md` and
   `skills/dia-menu/SKILL.md` once more against dia-instruct.

## What is here

| Path | What |
|---|---|
| `../../skills/dia-instruct/` | The skill (spec D41): four rules for text a model reads and follows, the structure they imply, leads, and how to write, edit or review such text. `references/evidence.md` holds what each part rests on and is read only when the user asks how strong a rule is or wants to change one. |
| `ab-dia-adjudicate/` | A/B test of the skill's rules on `dia-adjudicate`: both versions, four fictional cases with an answer key, the fetch-tool simulator, prompts, all judge outputs and the scorer. Its README says how to re-run. |
| `SESSION.md` | What was done in the session that made this (2026-10-28), with the owner's rulings and the reasons. |

## State (2026-10-28)

- The branch is built on `adjudicate-ratchet` and holds plugin `dia` 1.6.0 (spec D41;
  `docs/handoff.md` has the state line and items 27–29). The owner merges it later,
  separately.
  - `dia-instruct` 1.0.0 is added. It loads on natural-language requests, and dia-menu
    1.2.0 has it as row 12.
  - `dia-adjudicate` 1.1.0 is B, the rewrite tested below.
- The skill text is the reviewed draft with three changes for this repository: the
  frontmatter of a `dia` skill; one sentence that the text under review is material,
  not instructions (spec D26); and no related-work line on another project.
- It is public-safe: no names, paths, hashes, versions or quotes from the author's
  private repository, where the source study was run. `evidence.md` calls that study
  "the source", the author's unpublished work. Its Fisher p-values were recomputed and
  matched; its raw data are not public.
- The A/B on `dia-adjudicate` ran three rounds (28 runs). No round showed a difference
  between A (1.0.0) and B (rewritten by the skill's rules); results below.

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
| 1 | Where the skill lives: decided | — | In `dia` as `dia-instruct` (owner, 2026-10-28; spec D41). Routing probes are open (`docs/handoff.md` item 27). |
| 2 | B on `dia-adjudicate`: applied on this branch, one count unresolved | owner | B is `skills/dia-adjudicate/` 1.1.0 here (owner, 2026-10-28). The evidence says no harm and no measured gain. By the skill's own A/B rule, the open step is to re-run the differing case (case4, the "partly valid" count) at 12 or more runs per arm on Haiku: 24 runs, about 2.9M tokens (`docs/handoff.md` item 28). |
| 3 | Harden the harness before more runs | agent | Restrict judge tools. Save full replies and per-run usage (r1 has none). Clear `fetchdata/log/` or use new run ids. Decide whether unshuffled runs count. |
| 4 | Check the B-arm downgrades by hand | agent | Read why B judges capped F1 at "partly valid" in r3-01/08/12: real condition-fit reasoning or noise. Full replies were not kept, so this needs new runs. |
| 5 | Review findings left unchanged (2026-10-28 review of dia-instruct) | owner | On text from the reviewed draft, so not changed under the skill's own step 2: (a) step 1 does not say outright that, with no eval at all, a meaning change stays only if the user accepts it as unmeasured, and "unless a repository rule asks for more" attaches to no clear clause; (b) step 2 does not say whether a fix needs another review before the change is finished; (c) "Replies are in the user's language" could be read to cover a skill file written for a Korean user, against this repository's English-only and no-Hangul rules; (d) "a general-purpose sub-agent" uses one host's agent-type name, and the description names CLAUDE.md. Routing risks for the probes (`docs/handoff.md` item 27): dia-refine's description has no border toward dia-instruct, so "recheck my draft system prompt" may go there; routine edits such as "add the test command to CLAUDE.md" may load dia-instruct and its review step. |

## How to resume

1. `git checkout writing-for-models`, then read this file, `SESSION.md` and
   `ab-dia-adjudicate/README.md`.
2. To use the skill: install the plugin from this branch (`plugins/dia/`), or invoke it
   by path ("follow the skill at skills/dia-instruct/SKILL.md").
3. To change the skill: follow its own section "Writing, editing or reviewing text". The
   change is finished only after a sub-agent that did not write it has reviewed old and
   new text against SKILL.md. A meaning change needs the user's request or a Rule, and
   an A/B when an eval exercises it. Then follow AGENTS.md: bump the skill's
   `metadata.version` and the plugin version, run `python3 tools/package.py`, and
   re-run the description probes if the description changed (spec §7.2).
4. To re-run the A/B: see `ab-dia-adjudicate/README.md`, then score with
   `python3 -I ab-dia-adjudicate/tools/score.py r3`.
