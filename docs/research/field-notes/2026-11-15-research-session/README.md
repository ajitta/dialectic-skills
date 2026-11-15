# Field record: five issues from one research project (2026-11-15)

Status: observation record, not a verified finding. The observations are issues #49 to #53, filed on 2026-11-15 from work in which the installed plugin (`dia` 2.15.1) was used on a research project in the owner's private repository. Issues #49 to #52 describe one session; #53 says "one session" without saying which; the project it describes matches. This file lists what the issues report and what the session's own write-up adds; the write-up is not reproduced; counts, roles and the kinds of defect are given. Nothing in `skills/` was changed. Reviewed in [review.md](review.md), which checks the facts, records the baseline runs and gives a verdict on each proposed condition; where the two differ, the review wins.

## 1. Setting

| Step | Skill or flow | How |
|---|---|---|
| Review of the request | dia-skopos | Main assistant |
| The work | dia-techne | Main assistant; its outside check was one separate agent |
| Review of the result | three reviewers written by hand, then one judge | Three subagents with lenses chosen by the assistant (source and fact audit; reasoning and method; practice), blind to each other, then one subagent told to follow dia-adjudicate. dia-panel was not used |

Target of the review: 13 notes, about 80,000 characters. The single outside check took about 100k tokens; the three reviewers and the judge about 640k (issue #50).

## 2. What the issues report

| Issue | Skill | Observation | Conditions proposed |
|---|---|---|---|
| #49 | dia-adjudicate | The caller did not start a second judge run. Its brief said its own table wins on conflict; the judge's output lacked the claim inventory and "Checked and clean", and one reviewer item was called an error on the basis of a summarising fetch. No rule narrows the inventory for a large target | 4 |
| #50 | dia-techne | The outside check was aimed at the parts the author doubted. 16 major items remained, among them a paper's direction stated backwards and an experiment plan the user could not run as written | 3 |
| #51 | dia-techne | A source marked "abstract checked" was cited for a direction its abstract does not state; the paper says the opposite. Search and fetch results were model summaries | 3 |
| #52 | dia-panel | The workflow takes one target and four fixed lenses, so the panel was written by hand and the second judge run was dropped. The source-audit lens found the reversed direction; none of the four stock lenses compares quotations with sources | 3 |
| #53 | dia-skopos | Five items: an outcome hypothesis where the project's recorded goal and the request pointed apart; stopping on evidence that confirmed the user's framing; an offer with no recommendation; the search rule read literally; a scope approved in dia-skopos that dia-techne could widen | 5 |

## 3. What the session's write-up adds

The issues do not give the models. The write-up (one note, written by the session's assistant, Claude Opus 5.5) records:

- Reviewers: Claude Opus 5.5, with 8, 18 and 12 findings. Judge: Claude Fable 5.2, one run, 33 merged items, 16 of them major.
- Of the 16 major items, the source-audit reviewer raised 2 (one shared with another reviewer), the reasoning-and-method reviewer 11 (three shared) and the practice reviewer 7 (four shared). 9 of the 16 touch the experiment note.
- The four items the write-up calls decisive come from the reasoning-and-method reviewer (three) and the practice reviewer (one).
- The experiment note carried a sign-test table and power values; two reviewers recomputed them and found them correct. The defects the judge accepted for the plan are a decision rule applied again as pairs accumulate, the number of pairs a decisive test would need, a one-metric rule set against two of the cards, and a fixed A-then-B order.
- The judge's order of items to check, its table of items not verified, its closing line and "via summary" marks are in the write-up. A claim inventory is not.

The write-up is the caller's summary of the judge's output, not that output. It cannot show which sections the judge printed.
