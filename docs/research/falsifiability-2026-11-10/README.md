# Falsifiability audits: is a new dia skill needed?

Session date: 2026-11-10. Status: research record. Nothing here is adopted; the light-fix patch was applied only to a scratch copy of the installed plugin (dia 2.11.0), never to `skills/`.

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
| [verification/](verification/) | The four agent reports behind verification-result.md |
| [experiment-v1-result.md](experiment-v1-result.md) | v1 comparison: 3 arms × 3 inputs × 1 run, one blind grader |
| [exp1/](exp1/) | v1 protocol, relay log, transcripts (`t/`, labeled), blinded copies (`blind/`), key, grades, and `light-fix-B.patch` (arm B's four edits against dia 2.11.0) |
| [experiment-v2-result.md](experiment-v2-result.md) | v2 comparison: 3 runs per cell, wrap-up after the 5th reply, two blind graders |
| [exp2/](exp2/) | v2 protocol, relay log, transcripts, blinded copies, key, rubric and inputs given to graders, both graders' sheets, and the relay, blinding and tally scripts |

## Limits

- The orchestrator wrote arm B's edits and relayed every simulated-user reply. The relays are logged in each `relay-log.md`.
- All arms and graders were Claude models.
- The blinding hides routing lines and skill names. The dia brief formats still reveal which transcripts came from a dia arm.
- The scripts in `exp2/` keep the session's absolute scratch paths, so they are records and do not run as-is.
