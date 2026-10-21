# Output template (dia-counterplan)

Translate headings and labels per SKILL.md Rule 7. Use numbered lines, not wide tables, so it reads on a phone. Print plain Markdown, not a code block.

---

**Target:** user | claude | text (inferred from … — correct me if wrong)
(claude only: This is a self-examination and not independent: the same assistant wrote the plan and the counterplan.)

## Plan
Recommendation: one or two sentences. Quote: "…"
Data:
- D1 … — evidence: verified this session (a tool ran) | supplied by the user | single source | unverified recall
- D2 …
Not examined: (other plans in the input, one line, if any)

## Assumptions
- A1 [T] … — "quote"
- A2 [A] … — the plan needs it because …
- A3 [A] D2 holds (the decision turns on a datum that is only single source or unverified recall)

## Key assumptions (SAST test: if the opposite were true, would the decision change?)
- A1 → yes: … → K1
- A2 → no: …
- A3 → yes: … → K2
Passed but not paired: (beyond five, one line, if any)

## Contraries (my choice)
- C1 (against K1): …
- C2 (against K2): …
Coherent: C1 … Cn can hold together | replaced Ck because it conflicted with Cj
Same data: no contrary contradicts D1 … Dn | C2 reads D2 as …

## Counterplan
Recommendation: one or two sentences, at the plan's level of detail. A slot (step, cost, date) whose fact (a price, a measured quantity) neither side has reads "not supplied" and goes under Not tested; a step or date the counterplan chooses is named, never "not supplied".
1. … (rests on C1; cites D1)
2. … (rests on C2)

## Side by side
1. K1 (plan) … / C1 (counterplan) …
   Favours the plan if: … Favours the counterplan if: …
2. K2 (plan) … / C2 (counterplan) …
   Favours the plan if: … Favours the counterplan if: …
Plan recommends: … Counterplan recommends: …
One assistant wrote both sides.

## Your synthesis
Which assumption from each pair do you now hold? Per pair: the plan's, the counterplan's, your own wording, or "can't tell".

---

Printed after the user rules on every pair, or stops, or when Step 3 finds no key assumption:

## Record
- Target / plan: (and the self-examination line for claude)
- Key assumptions: n of m listed
- Pairs and rulings: K1 plan | counterplan | own: "…" | open — one line per pair
- Result: plan side held | counterplan side held | synthesis | undetermined | no key assumption found | stopped
- Kept for the side set aside: one line per pair with the strongest argument for the assumption not held (for a ruling in the user's own words, for whichever of Kn and Cn it departs from more); for an open pair, the strongest argument on each side and the observation that would decide it
- Written by: one assistant wrote both sides of this comparison
- Not tested: the accuracy of the shared data; assumptions not listed; alternatives other than these two; how either plan would play out; (anything else). Hearing both sides is not evidence that the plan was tested.
- Rewrites: Cn rewritten because … (named defect) | none
- History: (one line per follow-up turn)

For no key assumption found, the record has only Target / plan, Key assumptions (0 of m listed), Result, and: Not tested: whether the shared data are accurate, assumptions not listed, and alternatives to the plan; no counterplan was written, which does not show the plan is sound.
