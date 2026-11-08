# Review of this record (2026-11-08)

Status: a review of the files in this folder (commit `5623699`), written by the agent that built dia 2.9.0. The record is kept as written; where the two differ, this review wins. Probes: `docs/probes.md` Part AF. Decision: spec D65.

## 1. What holds

Re-tallied by script from `data/`: 60 attempts, 49 observed loads, 47 completed; pilot functional 18/18 per arm and strict primary 15/18 per arm; follow-up 6 of 12 and 5 of 12 completed, 13 interruptions (11 before loading, 2 after), no timeouts; median 23.46 and 23.81 seconds. The process tables match `process-observations.csv`: intermediate messages in the editing pilots 4/15 against 12/15 (surgical 1/3 against 3/3, cleanup and verification 0/3 against 3/3, minimal 3/3 in both, trivial 0/3 in both), follow-up 0/6 against 5/5, pre-fix wrong-value checks 5/6 against 4/5.

Both input hashes match `provenance.json`; `inputs/original-SKILL.md` is byte-identical to the pinned upstream file (blob `6a62d04`, also the upstream `main` at review time); body lengths 2,224 and 2,618 characters (+17.7%). `inputs/dia-regula-2.2.0.md` equals `skills/dia-regula/SKILL.md` at `v2.7.0`, and the five skill versions match that release. The quoted lines (L17–18, L27, L41, L42, L60) match the original, and the Rule 2 withdrawal follows Rule 2's wording. No local path, account detail or credential appears in the folder.

The "intermediate policy message" category equals "the run posted a third public message" in all 47 completed runs, so coding it after the runs, with the arms known, could not move the counts. The words "specific" and "consequential" describe more than was measured.

## 2. Corrections

1. **The rewrite changed meaning in section 1, and that section carries the effect.** In the original, "Surface tradeoffs." appears only in the section 1 slogan (L15); it is not a repetition. The revision makes it a duty under "Before implementing" and adds a reason the original does not give: "because the user needs to see these choices before implementation commits to an approach". `review-and-adjudication.md` describes the revision as removing slogan repetitions and adding reasons, and none of the four reports or two judgments mentions this move. A section-swap probe on the cleanup task (Codex, n = 4 per arm, rule fixed before the runs) gave: original 0/4, revision 4/4, original with only the revised section 1 4/4, revision with only the original section 1 1/4. The messages state the edit, what will be left alone and the checks before editing, which is what the added reason asks for. Which sentence inside section 1 carries it was not isolated. The hypothesis in `process-analysis.md` (bundling conditions, actions and reasons) and the layout-only/reasons-only design in P4 aim wider than the observed cause.
2. **Only the cleanup message difference recurred.** With the record's prompts and fixtures on Codex CLI 0.166.0 (the record used 0.167.0) on a later run, the verification task did not reproduce: the original posted the message in 4 of 4 runs (record: 0 of 3 in the pilot, 0 of 6 in the follow-up). The cleanup method difference did not recur either: every arm ran the existing suite (4 of 4 each), and the original read `helpers.py` in 4 of 4 runs against 2 of 4 for the revision. "Some method changes" (`process-analysis.md`) and the verification example (`README.md`, `trace-excerpts.md`) are observations of one build and day.
3. **P2 does not match the data and lies outside dia-regula.** The added messages came on edits with no interpretive choice (cleanup, verification); on the task with one (minimal: what counts as whitespace) both versions posted it 3/3. The rewrite produced announcement before editing, not selective disclosure of consequential choices. What a coding agent should disclose is a policy for the author of that text; dia-regula covers how instructions are written.
4. **P1 mostly repeats existing Leads** (number steps only where their order or completeness matters; end each step on a done-when). **P3 belongs in `references/evidence.md`**, not in SKILL.md, whose Writing step 1 is already one long paragraph read on every run.
5. **P4 is right, and dia-regula already implied it.** Rule 3 keeps reasons because "a reason lets the model generalize a rule to cases it does not name", so an added reason changes what a model does, which is Writing step 1's definition of a meaning change. The session recorded the reasons as editorial interpretations rather than counting them as meaning changes; the probe above is a case where an added reason changed behaviour.
6. **Findings the static review missed.** L11, "For trivial tasks, use judgment.", limits all four sections from a separate paragraph, which Rule 1 reports ("a condition, limit or fallback sitting on another line … from the result or action it gates"); it is also the clause closest to the strict verification criterion that no completed run met (0 of 17 retained a regression test). The original names one thing twice, "verifiable goals" (L55) and "success criteria" (L53, L67), a Rule 4 finding the record reports as absent; the revision in effect keeps one name.
7. **Process.** The repository's run budget (AGENTS.md, from 2026-11-04) asks the owner first above 30 runs; the record documents the owner's approval of the 36-run pilot but not of the 24-run follow-up. dia-regula's own A/B standard (12 or more runs per arm on a differing case) and that budget pull apart; the follow-up followed the skill and stopped at an account limit. Writing step 1 also asks for "a model that does not already pass every case", which the pilot's functional checks (18/18 per arm) did not meet. The data call the follow-up phase "confirm" while the text calls it exploratory.

## 3. Decisions (spec D65)

- dia-regula 2.3.0: Writing step 1 names an added reason as a meaning change.
- `references/evidence.md` gains the observation (Leads) and a line on naming process measures before the runs (Checking a change).
- Not adopted: P1 as a new Lead, P2, P3 in SKILL.md.
- The record stays as written; `docs/research/README.md` indexes this folder.

## 4. Limits

The probe is one engine on one day with 2 to 4 runs per cell; the verification arms other than the original and the revision ran twice. The record's full event archive is not public, so the review used its public messages and data files.
