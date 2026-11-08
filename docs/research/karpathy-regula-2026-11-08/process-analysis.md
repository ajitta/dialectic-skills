# Process: instruction following and visible method choices

## Why the outcome comparison was insufficient

The owner clarified that the object of interest was the process induced by instructions and the model's own decisions, rather than final task success. Existing logs were re-read without new model calls. These process categories were selected post hoc. The pilot's 36 completed runs and the follow-up's 11 completed runs were kept separate.

Observable process consists here of public assistant messages, executed commands, file-change events, and source-state checks. These are not direct access to private internal reasoning, and a stated reason is not established as the cause of a choice.

## Specific intermediate policy messages

An intermediate policy message excludes the generic opening announcement and the final report. It occurs after inspecting task files and before changing source, and specifies such matters as the chosen interpretation, edit boundary, input condition, or checks. The timing was checked against file-change events and source hashes. The clarification-only task is excluded from the editing denominator.

| Pilot editing task | Original | Revised |
|---|---:|---:|
| minimal | 3/3 | 3/3 |
| surgical | 1/3 | 3/3 |
| cleanup | 0/3 | 3/3 |
| verification | 0/3 | 3/3 |
| trivial | 0/3 | 0/3 |
| Total | 4/15 | 12/15 |

The clearest observed change was more frequent disclosure of the intended condition, boundary, and verification choice before action. It is not a score for deeper thought or a requirement that every judgment be narrated. Silence in the original runs does not imply absence of judgment. A separate plan-tool event was not required for a short public plan to exist.

## Correspondence to instructions

- Both arms asked fixed-fee versus percentage questions in ambiguity, 3/3 each, without editing. This matches the clarification instruction; a no-skill arm is needed to distinguish the skill's additional influence from existing model behavior.
- Both arms stated their whitespace interpretation and split/join approach in minimal, 3/3 each. Assumption/approach disclosure was not unique to the rewrite.
- In cleanup, both preserved the pre-existing unused code in 3/3 runs. Only the revision explicitly announced preservation of legacy_helper before editing in two runs. The behavior tied; the public boundary explanation differed.
- In verification, the revision stated the nonempty-input condition and intended narrow fix/checks in 3/3 pilots. The original had no separate post-inspection message in those runs. Both avoided adding an empty-input guard. The condition also came directly from the task, so it cannot be attributed to the skill alone.
- Trivial typo edits stayed short in both arms, with no extra intermediate policy message. The revision did not make every task verbose.

## Mean bug: three different pre-fix strategies

Original pilot runs:

1. Read source; assert the correct result 4.0 and observe failure; fix; check correct and singleton results.
2. Read source; verify that the current wrong result is 6.0; fix; check normal results.
3. Read source; fix; check normal results, with no observed execution of the old behavior.

All three revised pilots first publicly connected the nonempty-input condition to the narrow edit and planned checks. Each then executed one script that loaded the old source, asserted the current wrong value 6.0, wrote the replacement, loaded the new source, and checked 4.0 and a singleton. Statement order and successful execution support this sequence even though it was one command.

| Pilot mean process | Original | Revised |
|---|---:|---:|
| Execute a pre-fix confirmation of the wrong behavior, including a failing normal-expectation check | 2/3 | 3/3 |
| First fail against the correct expected value | 1/3 | 0/3 |
| State input condition/boundary in a separate pre-action message | 0/3 | 3/3 |
| Check correct result after fixing | 3/3 | 3/3 |

The revised arm's 0/3 on failure-first is not 0/3 on pre-fix diagnosis. Checking that a known wrong result exists and retaining a regression assertion against the correct result are different procedures. The assistant exercised method choice rather than uniformly implementing a single literal sequence.

The same instruction text also yielded different strategies across tasks: in surgical, both arms executed a failing discount check before the fix in 3/3 runs. Retained test-file additions were original 2/3 and revised 3/3. In minimal, retained test changes were 2/3 and 3/3, and observed failure-first runs were 1/3 and 2/3. Task context mattered; the logs do not establish which cue caused the choice.

## Cleanup: method selection with the same edit result

All three original cleanup runs read labels.py, made the narrow change, then extracted the target function through AST for direct checks. They did not separately read helpers.py/test_app.py or run the existing test suite.

The revision described the intended change in all three runs. Two also read helpers.py and test_app.py and ran the existing suite plus direct checks. The other used function-level checking. Both styles preserved the requested boundary. The revision sometimes inspected more context; this is an observed method difference, not proof that broader checking was always necessary or better.

## Follow-up, separately

| Completed mean follow-up | Original | Revised |
|---|---:|---:|
| Pre-action condition/boundary message | 0/6 | 5/5 |
| Execute confirmation of current wrong value before edit | 5/6 | 4/5 |
| Fail first against correct expected value | 0/6 | 0/5 |
| Check normal result after edit | 6/6 | 5/5 |

The disclosure pattern appeared in these completed follow-up runs too. Actual old-behavior checks occurred frequently in both arms. Public explanation and actual checking must remain separate categories. These incomplete samples do not constitute a full replication.

## What can be attributed

Observed: the revised text was associated with more specific pre-action policy messages and some method changes. Hypothesis: bundling conditions, actions, and reasons may encourage visible articulation of an applicability judgment. Not established: that the explanations reflect better internal reasoning, that the added reasons caused the effect, or that literal adherence improved overall.

The wrapper forced skill reading. Some tasks directly supplied nonempty inputs, excluded future features, or named the exact edit. No no-skill arm or instruction-component ablation was run. The effect of a directive cannot be separated completely from the task, host instructions, and learned coding habits. Tradeoff disclosure and justified pushback were not sufficiently elicited by these tasks to grade their absence.

For a user who wants to inspect interpretation and scope before action, the extra public messages supply more observable material. This does not imply a new universal duty to narrate decisions. Mandatory steps, allowed discretion, and useful explanations need separate treatment in future instruction design and evaluation.
