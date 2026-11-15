# Review of the field record (2026-11-15)

Status: a review of `README.md` in this folder and of issues #49 to #53. Written by an assistant session (Claude Fable 5.2) that read the issues, the released text and the session's write-up, ran the released plugin 21 times, and then had its own verdicts attacked: five independent reviewers (three Claude Opus 5.5, two Codex) and two separate dia-adjudicate runs on their reports (Fable 5.2 and Opus 5.5, report order reversed). The verdicts below are the ones that stood after that; §3 lists what the reviewers overturned. Nothing in `skills/` or `companions/` was changed. The runs are not in `docs/probes.md`: they compare no arms and decide no wording, and their plan, prompts and outputs are kept outside the repository.

## 1. The issues' facts

Confirmed:

- Kim & Park (2020), *Frontiers in Psychology* 11:1988, read in full: the abstract names the boundary variable without a direction, and the body reports the effect for autonomy-related transgressions and none for community-related ones, as #51 says.
- The pairs in #50 (about 37 for a 70% per-pair win rate, about 158 for 60%, 80% power) are right for a one-sided exact sign test at 0.05. Two-sided they are 49 and 199; the issue does not say which.
- The cost ratio in #50 (about 100k against 640k tokens) is the session's own figure and was not recounted.

Corrections and limits:

1. #50 reads as if the plan had no power calculation. The write-up records that the plan carried a sign-test table and power values (low ones, which it stated), and that two reviewers recomputed them and found them correct. What the judge accepted against the plan is a rule that keeps adding pairs and deciding again, the pairs a decisive test would need (the issue's 37 and 158), a one-metric rule set against two of the cards, and the fixed order, which the issue also names. The plan lacked a design its executor could carry out, not a calculation.
2. #52 says the source-audit lens found the most damaging error. By count it raised 2 of the 16 major items and none of the four the write-up calls decisive. A count does not rank damage, so this neither confirms nor refutes the issue.
3. #49 says the judge omitted the claim inventory and "Checked and clean". The write-up is the caller's summary, so the judge's sections cannot be checked from it.
4. The second judge run was not made, for the third time on record. On 2026-11-08 the judge, asked for a one-shot result, skipped it in 9 of 9 runs, and the review concluded that the caller has to start it (`../2026-11-08-review-panel/review.md` §2). The pipeline record of 2026-11-09 lists it among the caller's pitfalls (`../../pipeline-use-2026-11-09/review.md` §2, item 2). In this session the caller did not start it.
5. `docs/handoff.md` keeps dia-techne's comparison against no skill postponed with the condition "run it only if real use falls short". Issues #50 and #51 are that case.

## 2. What the runs added

Released text (`plugins/dia` at `0a461e6`, 2.15.1) except the two runs with no plugin loaded, Claude Code headless, one run per cell and model unless stated, 21 runs plus a smoke run, about US$7. One run shows a direction, not a rate.

| Cell | Issue | Result |
|---|---|---|
| A caller's brief with its own table that "wins on conflict", on case 2 of `docs/writing-for-models/ab-dia-adjudicate` (Fable, 1 run) | #49 | 12 of 12 verdicts match the key. The output is the caller's table and one summary line: no claim inventory table and no "Checked and clean" section, their content folded into the line. Evidence class on 11 of 12 rows. The must-check list is present. Inputs says "single run (no second run possible)"; nothing tells the caller to start one |
| The issue's eval as worded: the paper's URL and the question (Fable, 1 run) | #51 | Right direction, with the study's means and a second read told to argue against it. Says the page came through the fetch tool's summarising model. No verbatim quote, which the issue's pass rule asks for |
| The abstract only, no tools (3 runs each on Fable, Opus, Sonnet) | #51 | Opus 3 of 3 and Sonnet 3 of 3 write the wrong direction into the result as an inference from the abstract's wording. Fable 2 of 3 put it in the result as recall or as tentative, and the third names it outside the result as recall. So 8 of 9 results carry the wrong direction. 9 of 9 mark it as inference, recall or tentative; none repeats the field form, a plain statement marked as checked |
| The issue's eval as worded: an A/B plan for a solo creator (Fable, Opus) | #50 | Both compute or simulate the power, randomise the order within pairs and fix the rule beforehand. No separate checker is started |
| A research note plus experiment cards the user runs alone (Fable, Opus) | #50 | Both simulate power against the stated upload rate, randomise and fix one look. Both simulate a paired t statistic while the card decides by a count of wins or a sign-flip test with a margin; at one card's stated limit its own rule has about 60% power where the card says 80%. No separate checker. Of three runs in this table that fetched pages, one named the summarising step and two called the page checked |
| The same request with no plugin loaded (Fable, Opus) | #50 | Neither runs a calculation or marks which sources were read; both add a second look on a borderline count (extend four weeks at 5 or 6 of 8 on Opus, at 6 of 8 on Fable) |
| Ten project notes whose README records a self-reflection purpose; the request points to an explanatory note; one note contradicts the framing (Fable, Opus, Sonnet) | #53 items 1, 2 | No run lists the outcome as an open decision. Opus and Sonnet write "not stated" and a hypothesis although the README states a purpose; Fable quotes the purpose and reads the outcome as the same. All three raise the mismatch in the kind of note as a decision. All three cite the contradicting note, which says outright that the framing is reversed, after reading every note |
| A song the user calls very popular now, search tools listed (Fable, 1 run) | #53 item 4 | Two searches carrying the title and the singer were attempted (the run's permission mode denied them) |

Not run: #52 (a dia-panel run), #53 items 3 and 5, a large target for #49, a summarising fetch inside dia-adjudicate, a large folder for #53 item 2, a separate checker briefed by the author for #50.

## 3. What the independent review overturned

The session's second set of verdicts was written from one run per cell. Both dia-adjudicate runs found the conclusion to hold in part and named the withdrawal for #49 as decisive; one added the basis for #50 as equally decisive. Otherwise they differed mainly on severity labels.

1. "The caller's table did not remove the sections" was wrong. Two planned items (claim inventory present, "Checked and clean" present) had not been reported, and the output has neither section. The withdrawal of the output-side fix for #49 is itself withdrawn, and the run cannot tell format from target size.
2. "#50 does not reproduce" was too strong. No run exercised a checker briefed by the author, and the composite runs checked a different test from the one on the card.
3. "The issue's eval for #51 passes on the released text" was wrong on the issue's own pass rule (no quote).
4. The count of major items was used against #52's "most damaging"; it cannot carry that.
5. #53 item 4: spec D74 was missed. The owner has ruled on this family of lines with run results ("The 'never' lines stay").
6. The session read the caller's write-up as if it were the judge's output.
7. Both judges also found that the #53-1 result mixed two kinds of failure, that the acceptance rule for #51-1 had to be rewritten (the mark is already there), and that the lighter alternative in #52-2, a README recommendation, had not been weighed. §4 takes the first two; the third is in its #52-2 row.

The reviewers erred too: the two judge runs ruled 5 and about 10 report items wrong or overstated, and lowered the severity of 5 and 12 more.

## 4. Verdict on each condition

| Condition | Verdict | Basis and next step |
|---|---|---|
| #49-1 a "For the caller" block in the skill | Not as worded | A caller that briefs a subagent does not read the skill (the reason D68 gave against a README checklist). What reaches a caller is the judge's output and the workflow's code: one line beside "single run" telling a caller that can start agents to start the second run, and the judge stage of dia-panel made usable on reports written elsewhere (#52-3) |
| #49-2 a brief cannot drop the evidence class, the must-check list or "Checked and clean" | Candidate | One run shows two sections missing under a caller's table. Needs two runs of a changed text and a sibling cell |
| #49-3 evidence class on every Step 6 entry; summary-only moves to "Not verified" | Untested | The text says so already (Rules 3 and 8, Step 6). No run had a summarising fetch |
| #49-4 a size rule | Open | No large-target cell |
| #50-1 the check reaches the plan the user will execute | Candidate, narrowed | The released text already reaches the plan in 4 of 4 runs. What it misses in 2 of 2 composite runs: the check tests the rule the user will apply, as written |
| #50-2 the checker is not anchored on the author | Untested | Candidate wording: hard outside evidence first, a separate adversarial session when that is not available. The skill's `theory.md` cites that order from a secondary report of an interview and notes that the tutorial does not give it; question 4 lists the four checks with "or" |
| #50-3 several lenses and dia-adjudicate when stakes are high | Not adopted | dia-adjudicate starts by name only (D40, D64), and the cost is about six times |
| #51-1 a quote that states the direction | Adopt as a tightening | The mark is already there in 9 of 9. The rule to hold is that the result states no direction, size or condition that the words read do not state. Accept on the abstract-only cell and the URL cell (quote required), each with a sibling, since both have now been used to judge wording |
| #51-2 a "via summary" class | Adopt the mark | 2 of 3 fetching runs called a summarised page checked. The limit on what rests on it follows the issue's wording (a figure that rests only on a summary) |
| #51-3 recheck later sections after a correction | Not now | No run made a correction. Item 1 addresses the spread at its source |
| #52-1 a list of lenses and several target files | Files: adopt, with `claim` required for more than one. Custom briefs: owner's design call | A custom brief is a lens with no named method; the issue itself notes it may be weaker |
| #52-2 a source-fidelity lens by default | Open | Comparing quotations with sources is the judge's step by design (dia-adjudicate Rule 5). One panel run on the issue's eval case shows whether the stock panel misses it (about US$4.6 at D69's figure). If it does, the issue's lighter alternative, a README recommendation, costs no code and no default cost |
| #52-3 two judges, reversed order, the differ list | Adopt and extend | See #49-1 |
| #53-1 outcome "open" when the recorded goal and the request point apart | Candidate | Fails in form on 3 of 3, though each run raised the mismatch. Any wording runs the six-case regression of `docs/writing-for-models/ab-dia-intent.md` |
| #53-2 one attempt to find disconfirming material | Untested | The cell's contrary note was too easy to find |
| #53-3 every offer carries a recommendation | Not adopted | In the field the assistant asked once more, which is the safe step the skill asks for when a reply leaves an item unsettled. The [recommended]/[optional] alternative was not evaluated |
| #53-4 the search rule | Keep the text | D74. If it is changed, dia-skopos and dia-techne change together |
| #53-5 an approved scope binds dia-techne | Probe first | Not observed in the field; not run |

## 5. Order

1. #54 (docs; separate pull request).
2. The judge stage as its own dia-panel workflow, with the caller line in dia-adjudicate's output (#52-3, #49-1). dia-panel version only for the workflow.
3. dia-techne source marking (#51-1, #51-2), with a no-skill arm as handoff's condition now allows.
4. #49-2 to #49-4, after a cell that separates format from size and one with a summarising fetch.
5. #53-1 with the six-case regression; #53-2 and #53-5 after cells that can tell.
6. #50-1 and #50-2, after a cell in which the author briefs a separate checker.

## 6. Limits

- One run per cell except the abstract-only cell. Every cell was written by the reviewing session; none is the field session's prompt, which is not available.
- The targets are small (the adjudicate case's target is 406 bytes; the notes folder has ten short notes) against 13 notes of about 80,000 characters in the field.
- The field judge's raw output and the brief given to the first outside checker were not seen.
- The two judge runs confirmed the paper's direction only through summarised records; the reviewing session read the paper's page itself.
- The same session wrote the verdicts and chose which reviewer findings to take, with the two judge runs as the check on that choice.
