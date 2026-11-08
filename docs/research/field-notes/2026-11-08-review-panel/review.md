# Review of the field note (2026-11-08)

Status: a review of `README.md` in this folder. The agent that built dia 2.8.0 wrote it; the first draft was then checked by an independent reviewer (a separate agent session that re-tallied the source tables and the probe runs; verdict "sound with fixes", all fixes taken here). The note's source tables live in the owner's private research repository and are not reproduced; only counts are given. Probe runs: `docs/probes.md` Part AE. Decision: spec D64.

## 1. The note's facts

Confirmed by recounting the three judgement tables: 24, 23 and 21 findings; raised by one reviewer 7, 7 and 9; by all four 2, 9 and 5; verdicts as stated; 0 rejected; single-reviewer findings by skill counterplan 9, negative 5, warrant 4. The missing `.git` was raised by dia-negative alone, and the two dry runs between R2 and R3 did not catch it either.

Corrections:

1. dia-reductio's 5 single-reviewer findings are 1 in R1 and 4 in R3, not "all in R3".
2. The R3 reversal is recorded in the table as raised by all four reviewers in one row that joins three points, so the table does not show which three skills made it.
3. The R1 option that was adopted was also raised by dia-warrant.
4. "The four lenses do not [carry an evidence class]" is partly wrong: all four require an evidence class on facts (dia-negative Rule 4, dia-reductio Rule 2, dia-counterplan Rule 4, dia-warrant Rule 5); only dia-negative puts one on every finding.
5. "No one-shot review mode in three of the four": dia-negative (Rule 10) and dia-reductio (Rule 9) already give the whole analysis in one response and ask nothing. Only dia-counterplan ended its first message with a question.
6. "0 of 68 rejected" does not show by itself that the judging was lax. dia-adjudicate also overturned 0 report items when it judged real reviews of a document with real defects (Part AE). Strictness is measured with report items known to be wrong.

## 2. What the probes added

One target (an 11.5k-character experiment design from the private repository, in its reviewed version), Claude Code, Opus 5.5 at medium effort, 36 runs:

- A findings table imposed by the caller (location, problem, evidence, severity, fix) cut the methods. Without it, 8 of 8 lens runs carried out their method in full and in scope (two dia-reductio runs added a short section outside the derivation). With it, 1 of 8 did; 3 kept the method and added a generic findings list, 3 dropped steps (dia-reductio's derivation cut to one table row, dia-counterplan's assumption list and checks), and 1 dia-reductio run gave no derivation at all while calling 11 table rows "strict contradictions". The field panel's 10–17 items per lens per round look like the table cells, not like the free ones (1–7 items); the note says each prompt carried an output format, but the prompts were not available to check.
- Overlap: the design's main defect (the definition of a valid run) was raised in 4 of 8 lens runs without the table, none of dia-counterplan's 3, whose method builds an alternative rather than listing flaws, and in 7 of 8 with it. The table added to the overlap.
- Each lens examines one central claim (Step 1 of each skill), and different runs picked different claims. Coverage of a whole document comes from dia-adjudicate's claim inventory, not from adding lenses.
- dia-adjudicate merged the four lenses' native reports into issues with verdicts in 2 of 2 runs, named the same two decisive issues, and added one aspect no report raised. It handled the counterplan's pairs as options, not as true or false claims. Asked for a one-shot result, it skipped its recommended second run in every run (9 of 9), so the caller has to start the second run.
- The note's evidence-class incident (an observation from the reviewer's own session used as evidence about another runtime) did not occur in 8 lens runs with the shell tool visible, but did in dia-adjudicate, 2 of 2: it ruled a claim about the author's session "holds" from its own session's tool description, under an evidence class its Rule 8 does not list. Two Rule 8 wordings were tried: the first scoped the verdict in 1 of 2 runs, the second in 5 of 5; under both, the judge stated, without anything to quote, that its own session was not in the `-p` mode it was running in (2 of 2, then 4 of 5). Neither is released (Part AE).
- No lens run out of 16 noticed the missing `.git`. Nothing in the reviewed text bears on it, so a text review cannot see it; a dry run that reads one session's environment block as the model sees it can.

## 3. The candidates

- I1, a shared findings table for the lenses: not adopted. The table does not fit fixed result values (dia-reductio, dia-warrant) or dia-counterplan's rules against carping and verdicts, and a caller-imposed table cut the methods in the probes. I1 itself, a table inside each skill, was not tested.
- One-shot behaviour: adopted for dia-counterplan only (D64): a run asked for in one response ends with the record, every pair open, result undetermined, and the question as the record's last line.
- I2, a panel flow in dia-router: not adopted. dia-adjudicate starts only by name, so the router never picks it from a request, and the orchestration was left to another plugin when dia-adjudicate was designed (`docs/research/dia-adjudicate.md` §3). The README now describes the panel use instead.
- I3, narrower lens charters: not adopted, untested. Without the caller's table half the lens runs raised the shared main defect; dropping the table (README) addresses the rest of the overlap seen here.
- I4, an environment step in the lenses: not adopted; it belongs in the dry-run checklist of the work being reviewed.
- I5, evidence class on lens findings: the lenses already have it on facts; the defect showed in the judge. A dia-adjudicate Rule 8 wording is under test, not released.
- I6, a shared context pack: not adopted. In the round-2 lens runs each model call took 28k–56k input tokens, of which the document, once read, was about 12k, and a shared inventory would set every lens's scope the same way, which is why dia-adjudicate builds its own before reading reports.
- Cross-engine panel member: no change; a report written on Codex or ChatGPT can be pasted into dia-adjudicate, whose Inputs line records independence.

## 4. Limits

One target, one engine, one to five runs per cell; the probe target is the reviewed version of the R2 design, not the draft the panel saw, and removing its review section left two dangling references every lens reported (ignored in the counts). The field prompts and outputs were not available.
