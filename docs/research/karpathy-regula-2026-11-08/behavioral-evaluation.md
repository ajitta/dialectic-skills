# Behavioral comparison

## Design fixed before the pilot

The owner asked whether the two versions could be tested and then authorized the proposed experiment. Six tasks, two arms, and three runs per task/arm gave 36 pilot runs. Each used a fresh process and working copy. The exact wrapper, prompts, fixtures, and functional checks are in [data/cases.json](data/cases.json).

Only the skill text changed between arms. The model request, reasoning effort, task text, local tools, starting code, and scoring rules were held fixed. The requested model was `gpt-6.1-sol`, effort `high`; CLI version was 0.167.0. The internal backend revision was not available. Order was deterministically shuffled, with at most three executions in parallel.

The common prompt explicitly required reading the entire local skill, working only in the task directory, not opening other skills, using local Python/stdlib, and not using the network. User config loading and automatic AGENTS document loading were disabled. Common runtime instructions and skill listings could remain. Thus the experiment did not isolate the skill from every existing coding prior or host instruction.

An exact full-text match in successful command output established observed skill loading. Each attempt had a 180-second limit. Timeouts, interrupted executions, and unobserved loading were to be recorded separately from task failures. The model's submitted tests did not replace the independent functional checks.

| Task | Primary criterion |
|---|---|
| ambiguity | Ask about an unspecified service fee without changing code; first response only. |
| minimal | Implement whitespace collapse/trim without future options, a single-use abstraction, or unrelated changes. |
| surgical | Correct discount subtraction while preserving adjacent functions and a separate presentation module. Regression-test changes are allowed. |
| cleanup | Remove only the newly unused wrap_label import, preserving the pre-existing unused import and function, while implementing normalization. |
| verification | Correct mean, retain a regression test, observe failure before the fix and test success after it. |
| trivial | Correct only the specified README typo. |

The verification criterion was intentionally strict. Retaining a test file can be a stronger reading than the skill's wording and its trivial-task discretion. Failure on that criterion is not automatically an objective instruction-following defect.

## Pilot outcomes

All 36 pilot executions loaded their assigned full text, completed, and were eligible. There were no timeouts or account interruptions in this phase.

| Task | Original functional/scope success | Revised functional/scope success |
|---|---:|---:|
| ambiguity | 3/3 | 3/3 |
| minimal | 3/3 | 3/3 |
| surgical | 3/3 | 3/3 |
| cleanup | 3/3 | 3/3 |
| verification | 3/3 | 3/3 |
| trivial | 3/3 | 3/3 |

For verification, neither arm retained a test file: 0/3 each. A failing check against the correct expected value before changing source was observed in original 1/3 and revised 0/3. All six performed successful checks after the fix. The strict primary total was therefore 15/18 in each arm, not a general code-quality score. [Process analysis](process-analysis.md) explains why the failure-first metric misses other forms of pre-fix diagnosis.

Pilot median elapsed time was 23.46 seconds for the original and 23.81 for the revision. Reported input-token sums were 1,856,615 and 1,867,001; cached-input subsets were 1,504,768 and 1,489,920; output-token sums were 7,918 and 8,682. These are usage records, not prices. Shared context, tool-call count, cache state, and parallelism prevent attributing these small timing differences to prompt length or claiming a speed advantage.

## Exploratory follow-up and usage interruption

Although primary scores tied, the small failure-first submetric difference prompted a new batch on verification alone: 12 attempts per arm. This selection was made after the pilot and was recorded as exploratory, not a preregistered primary hypothesis. Prompts, fixtures, model request, and scoring criteria stayed unchanged.

| Follow-up status | Original | Revised |
|---|---:|---:|
| Attempted | 12 | 12 |
| Full skill text observed | 7 | 6 |
| Eligible completed | 6 | 5 |
| Account-usage-limit interruption | 6 | 7 |
| Functional and scope success among completed | 6/6 | 5/5 |
| Retained regression file | 0/6 | 0/5 |
| Failing correct-expectation check before fix | 0/6 | 0/5 |
| Successful check after fix | 6/6 | 5/5 |

Of the 13 interruptions, 11 occurred before loading and two after loading but before completion. There were no timeouts. The interruption records are not counted as task failures or evidence that either text suppresses loading. There were 60 attempts, 49 observed loads, and 47 completed eligible executions across both phases.

The session initially announced that 24 additional executions had finished before distinguishing completion from attempted execution. The subsequent report explicitly corrected that statement. The requirement of at least 12 valid executions per arm was not met. There was no model/account substitution, purchase, or attempt to evade the limit. No new model executions were made after the interruption was identified in analysis.

The pilot and follow-up are not pooled to infer superiority. In the completed follow-up, the small pilot failure-first difference was not observed again; incomplete, unequal samples prevent treating this as a conclusive replication.

## Instrumentation corrections

Two setup probes could not read a local file in the selected restrictive execution modes. A probe using the parent session's permitted execution mode succeeded. These setup probes were excluded from the experiment; global user rules/config were not edited.

The first observer falsely classified file-list queries containing an excluded SKILL.md pattern as other-skill reads. It also missed Python assertions appearing before the interpreter invocation in a multiline command. The observer was corrected and applied to the same saved traces; tasks, model prompts, and primary criteria were not changed. Fourteen pilot records had an eligibility or observation-field correction. The original records and the correction ledger were retained in the local full archive. No favorable replacement runs were selected.

## Limits

Most tasks were small enough for both versions to pass every functional check. This ceiling does not establish behavior equivalence. The experiment used one requested model, synthetic Python tasks, a common host context, and no no-skill control. Layout and rationale changed together. It provides local observations, not a general improvement claim. The full follow-up standard was not reached.

For future repository work, this historical record is not an authorization for another large batch. The current repository AGENTS policy on planning, owner approval above 30 runs, and smaller probe counts applies to new experiments.
