# Candidate improvements for dia-regula

Status: proposals from the session, not accepted rules or shipped edits. Their effects have not been measured. The existing four Rules are retained as the starting point; the record does not justify a new universal requirement to explain every decision.

## P1. Distinguish mandatory procedure from permitted method choice

Candidate placement: an experimental Lead, with a cross-reference to completion criteria where needed.

When process is part of the requirement, the writer should identify the non-substitutable action/order and what evidence shows it happened. When method is deliberately delegated, the writer should bound the permitted actions and the state that counts as complete without silently imposing one implementation.

The mean task illustrates the distinction. Confirming the current wrong value and then checking the fixed value differs from making the same correct-expectation test fail before and pass after the fix. Retaining the regression test is another requirement again. A grader must not add these requirements after the fact; the author should decide which are intended.

Discretion clauses such as `For trivial tasks, use judgment.` belong to this boundary discussion. They may concern explanation length, verification method, required order, or some combination. The author must decide the permitted relaxation; the editor should not invent it. The logs do not establish that the assistants actually invoked this clause to waive a step.

## P2. Selectively expose consequential applicability choices

Candidate placement: an experimental conditional Lead, not a fifth Rule.

When plausible readings would materially change the action boundary or acceptance condition and the user needs to inspect that choice, a short statement of the relied-on condition and intended boundary before action may help. Straightforward work need not acquire an extra explanation stage.

The revision produced specific intermediate policy messages in 12/15 editing pilots versus 4/15 for the original. The completed mean follow-up showed 5/5 versus 0/6. This supports the availability of more public material to inspect; it does not demonstrate that extra narration improves decisions or that humans successfully intervened because of it.

The proposed message is a brief public policy/assumption statement. It is not a request for private chain-of-thought or an exhaustive account of every considered option. Whether such a statement adds value, cost, or merely plausible justification requires a separate test.

## P3. Record outcome, process correspondence, discretion, and explanation separately

Candidate placement: Writing, editing or reviewing text, especially the evaluation conditions in item 1.

Before a comparison, specify whether the changed requirement concerns the final state, an obligatory sequence, allowed method choice, or observable disclosure. Score each applicable part from the evidence that can establish it. Inspect command contents and within-command order when needed; command count, a plan-tool event, or a single exit status is not a complete process measure.

In this session, a failure-first score of zero coexisted with a pre-fix wrong-value check in all three revised mean pilots. A retained-test-file score of zero also coexisted with successful inline checks. Those scores answer different questions. Likewise, no intermediate message does not establish no judgment, and more explanation does not establish better judgment.

The intended distinction is instruction correspondence versus delegated method choice versus public explanation. Existing outcome checks remain necessary. The new process categories should be fixed before the next experiment, with explicitly exploratory treatment for categories discovered afterward.

## P4. Audit added reasons for semantic consequences

Candidate placement: Rule 3 application guidance and the meaning-change accounting in Writing item 1, without duplicating existing instructions.

A new because-clause can supply a criterion, exception, or justification that the original author did not state. Its addition should therefore be inspected for behavioral meaning, rather than assumed to be wording-only cleanup. The change report should distinguish a source's reason from an editor's reconstruction. This need not add provenance clutter to the reusable skill body itself.

The session observed more public condition/boundary explanations after layout and reasons changed together. It did not isolate either factor. A future factorial comparison would use the original, layout-only, reasons-only, and combined versions under the same conditions. There should also be a no-skill control if the question is whether the text adds anything beyond existing model habits.

## Priority and acceptance boundary

P1 and P2 are candidates for small experiments in a revised instruction file. P3 and P4 can guide how the next edit and its evidence are recorded. None should be promoted to a mandatory Rule on the strength of this session alone. Any proposed behavioral change still needs the owner's decision and the repository's current review/evaluation requirements.

No further batch is authorized by this document. In particular, the current repository owner policy requires an advance plan and approval above 30 runs; smaller probes should be used where they can answer the question. The interrupted historical comparison should not be completed by silently mixing models, days, or user accounts.
