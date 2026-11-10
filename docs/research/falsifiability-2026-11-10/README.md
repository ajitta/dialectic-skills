# Falsifiability audits: is a new dia skill needed?

Session date: 2026-11-10. Status: research record. Nothing here is adopted; the light-fix patch was applied only to a scratch copy of the installed plugin (dia 2.11.0), never to `skills/`. Reviewed in [review.md](review.md), which re-counts the data, re-runs the routing on a second harness and corrects the Gaps, the surviving changes and the resume steps below (it supports neither line and no regrade); where they differ, the review wins.

The reports are written in Korean, the language of the session, and the dialogue transcripts are Korean because the test inputs were Korean. This README is the English index.

## Question

Can the falsifiability problems raised in the session be handled with the existing dia skills, or does it take a new skill? The problems are:

- prior refutation criteria;
- decision rules for probabilistic claims;
- auxiliary hypotheses;
- immunization by refusing every criterion;
- audits of non-universal claims (existential, unbounded and statistical).

## Findings to carry forward

- **No new skill.** Both pre-registered comparisons point this way.
  - v1: 9 dialogues, 1 grader.
  - v2: 27 dialogues, 3 runs per cell, 2 independent blind graders.
  - Under every grader, at least one existing path met the bar. The three paths compared were:
    - A: a plain answer;
    - B: a light fix to dia;
    - C: dia 2.11.0 unchanged.
- **v2 does not settle whether B or C passes; that depends on the grader.**
  - opus: A and B meet the bar; C does not (K1 5/9).
  - fable: A (exactly at the bar) and C meet it; B does not (K1 7/9).
  - Only A met the bar under both graders.
- **Gaps actually observed in the current dia (C):**
  - Routing varies between runs of the same input.
  - An existential claim ("there is a hidden pattern") routed to dia-conjecture was declined at the first reply.
  - A statistical claim, fixed by conjecture as a strict universal, lost the decision-rule point.
- **What survives as a change worth considering:**
  - one router border line;
  - one dia-conjecture Step 0 destination line for existential and statistical claims.
  - The quaestio brief fields in the light fix showed no gain on the pattern input.
  - Both changes are semantic changes under dia-regula step 1, so adopting them is the owner's decision.
- **Rubric weakness.** All 10 grader disagreements (out of 116 applicable items) were on items one or both graders flagged as borderline. The 4 that flipped a bar verdict were all K1. K1 does not separate unfalsifiable by form from unfalsifiable because the holder refuses every criterion. Splitting it and regrading the same transcripts is the cheapest next check.

## Contents

| File | Purpose |
|---|---|
| [analysis.md](analysis.md) | Analysis of the dia skills against Popper's falsifiability (logical and methodological layers) |
| [skill-need.md](skill-need.md) | Case for and against a new falsification skill, revised by dia-emend and a deep-dive on routing |
| [verification-result.md](verification-result.md) | Adversarial and independent verification of skill-need.md (blind reader, adversary, two adjudications) |
| [verification/](verification/) | The four agent reports behind verification-result.md, and `prompts.md` with each agent's launch prompt |
| [experiment-v1-result.md](experiment-v1-result.md) | v1 comparison: 3 arms × 3 inputs × 1 run, one blind grader |
| [exp1/](exp1/) | v1 protocol, relay log, transcripts (`t/`, labeled), blinded copies (`blind/`), key, grades, `prompts.md` (each arm's and the grader's launch prompt), and `light-fix-B.patch` (arm B's four edits against dia 2.11.0) |
| [experiment-v2-result.md](experiment-v2-result.md) | v2 comparison: 3 runs per cell, wrap-up after the 5th reply, two blind graders |
| [exp2/](exp2/) | v2 protocol, relay log, transcripts, blinded copies, key, rubric and inputs given to graders, both graders' sheets, `prompts.md` (all 27 cell prompts and both graders' prompts), and the relay (`u.sh`), blinding (`mkblind.py`) and tally (`tally.py`) scripts, which default to their own folder |
| [review.md](review.md) | Review of this record (2026-11-11): what holds, corrections, a 21-run routing re-run, a verdict per proposal |

## Session record (owner decisions, 2026-11-10)

The owner's requests and choices, in order. The quotes are the owner's own words, in Korean.

1. Analyse the dia skills against falsifiability (`/dia:dia-skopos`). The owner chose scope (C) and a Markdown report. → `analysis.md`.
2. Is a new falsification skill needed? (`/dia:dia-skopos`) The owner chose option (다) and a Markdown report. → `skill-need.md`. It was then revised by `/dia:dia-emend`, and the owner asked for a deeper look at the requests "what would refute this", "is it falsifiable" and "how do I test it", and for that deep-dive to be merged in.
3. "Decide whether this is solved by the current dia skills or needs a new skill; verify it with adversarial and independent agents." → `verification-result.md`.
4. "Actually run the comparison test." → v1, `experiment-v1-result.md`.
5. "I'll do as you recommend." The owner chose a full rerun at 3 runs per cell. → v2, `experiment-v2-result.md`.
6. Standing constraints for the whole session:
   - The installed plugin was never modified; arm B ran from a scratch copy.
   - No private material was sent to outside services.
   - The web lookups were the public IEP and SEP Popper entries only.

## How to resume

- **Decide on the two-line change.** The two lines are the dia-router hunk (the border line) and the first dia-conjecture hunk (the Step 0 destination) of `exp1/light-fix-B.patch`. The whole patch applies cleanly to 2.11.0 with `patch -p0` from the repository root; drop the other three hunks first. Then follow `AGENTS.md`: version bump, regenerate, and probe at 2 runs per cell for the changed behaviour.
- **Regrade before any new runs.** Split K1 in `exp2/scoring.md` into two items: form, and the holder's refusal of every criterion. Then give `exp2/blind/` to two graders with the prompt in `exp2/prompts.md`, and run `tally.py` on each sheet. This needs no new dialogues.
- **Rerun dialogues.** Reuse `exp2/prompts.md`, replacing the scratch paths with a working folder. The simulated-user rules are in `exp1/protocol.md` and `exp2/protocol.md`. A full rerun is 27 runs plus 2 grader runs, inside the 30-run limit in `AGENTS.md`.

## Limits

- The orchestrator wrote arm B's edits and relayed every simulated-user reply. The relays are logged in each `relay-log.md`.
- **Arms B and C loaded the skills differently.**
  - Arm B read its scratch copy's SKILL.md files directly.
  - Arm C loaded the installed plugin through the Skill tool.
  - The two arms therefore differ in more than the patch. See `prompts.md`.
- All arms and graders were Claude models: Opus 5.5 ran the arms and one grader, and Fable 5.2 ran the other grader. The serving models are recorded in each `prompts.md`.
- The blinding hides routing lines and skill names. The dia brief formats still reveal which transcripts came from a dia arm.
- The prompts and protocols name the session's absolute scratch paths. In this repository the same files sit in this folder.
