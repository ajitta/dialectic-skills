Verdict: PASS WITH FIXES

Second pass on `skills/dia-counterplan/` and `docs/research/candidates/design/dia-counterplan.md` at `275e1aa`. I checked the fixes from `b30344d` to `275e1aa` against my first-pass report (`review/diff/counterplan.md`, cited F1–F13). Line numbers are current-tree lines. No blockers. Most fixes are in and correct; the new problems are gaps the two real sessions exposed, two inaccurate doc claims, and one unsupported theory.md claim that came from my own first-pass replacement text.

Re-verified in a scratch `cp -r`: `package.py --check` exit 0; unittest 19 OK (skipped=1); source = plugin copy; no Hangul; description 1,019 chars, body 124 lines, `short_description` 57. Part O counterplan counts recomputed from `~/work/dia-review/new-skills-2026-10-21/out*/`: they match (var2 Claude 12/12, Codex 8/8; `n-da-claim` var2 0/3 and 0/2). BEBR 814 re-fetched. D35's 1,922-token total not verified (no tiktoken).

## Status of first-pass findings

1. Rule 3 vs Rule 4 on figures: **fixed** (SKILL.md:41, template:35). The new wording opens a loophole; see N1.
2. Overlapping result set and the "always" lines: **fixed** (:99, :101, :107, template:52 and :65).
3. Phone length: **fixed** (:50, :135), consistent.
4. Post-record pick: **fixed**, option (a) (:124). The label "Picks no winner" now holds without exception. N8 is a small wording mismatch with Rule 5.
5. Mason's procedure: **fixed** (:16, theory.md:19, :56, :59). It matches BEBR 814 ("obtained a strategic planning document from the company's planning department … constructed a counterplan based on opposite assumptions").
6. Teyku / Eduyot 1:6: **fixed** (:97, theory.md:51–52).
7. theory.md:23: **applied as I worded it, but my wording overclaims** (N2).
8. Rule 2 example: **fixed** (:40). Both sessions write contraries as "supposing …", as intended.
9. Undefined ruling cases: **fixed** (:103, :120, template:59).
10. Procedure intro: **fixed and extended** (:50).
11. Kept-view label: **fixed** (:103).
12. Routing: **partly fixed.**
    - (a) is in the body (:35), but it now conflicts with the description and with the probes (N5).
    - (b) "covered by P-F8": P-F8 is a theory.md:34 sentence, not routing; no cell tests "strongest case against my plan".
    - (c) "left to probe cells": none was added to `run.py`/`run2.py`.
    - Leaving (b), (c) open is sound; calling them covered is not.
13. Stale design note: **fixed** (design:38, :40).

## New findings

**N1 (should-fix): "not supplied" now lets the counterplan skip choices it should make.** Rule 3 (:41) allows "not supplied" for "a figure that neither side has". Session out-283-b, counterplan step 4, says: "Revisit the move later (C1, C5) … The date is not supplied." A revisit date is the counterplan's own decision, not a missing fact. out-283-a filled it ("when the younger child is nearer school age"). The F1 fix can thus produce the "vaguer" strawman of the Pitfalls.
Replace :41 sentence 3 with:
"Where a slot needs a fact that neither side has (a price, a measured quantity), write the slot with \"not supplied\" and list it under \"not tested\"; that counts as matching detail, and Rule 4 wins. A step, date or condition the counterplan itself chooses is not a fact: name it."
In template:35, change "whose figure neither side has" to "whose fact (a price, a measured quantity) neither side has; a step or date the counterplan chooses is named, never \"not supplied\"".

**N2 (should-fix, my own error): theory.md:23 claims more than its source says.** The text reads: "prepared by different people … none had one author write both sides." BEBR 814 describes lab participants who received "this same \"expert\" report plus a critique" and "the first planning committee report plus a second planning committee report". These were experimenter-supplied materials presented as from different committees; the paper does not say who wrote them, and experimenters typically write all such materials. The real difference is that participants were told the sides had different sources; here the user is told one author wrote both.
Replace theory.md:23 with:
"All of these studies used human participants. In the group studies, separate subgroups or advocates developed the plan and the counterplan or critique; in the lab studies, participants received written reports presented as coming from different experts or planning committees. None tested a person who knows that one author wrote both sides."

**N3 (should-fix): an added assumption gets past Step 7 and the five-pair cap.** :122 sends an added assumption "through Steps 3 to 6", which stops before Step 7. In out-283-a, turn 1, the user explained that the kids need their own rooms. The assistant then created "K6 = A4" and wrote C6. In the same message it recorded "K6/C6 space: plan held" and printed the record, even though the user never saw C6. That made six key pairs, against Step 3's "at most five".
Replace the last sentence of :122 with:
"An assumption the user adds goes through Steps 3 to 7: show only the new lines and ask for their ruling on the new pair before the record. If it would make more than five key pairs, say which pair it displaces, or list it as passed but not paired."

**N4 (should-fix): quotation marks around paraphrases in 2/2 sessions.** Step 1 asks for "a quote" (:54), and Step 2 says "[T] stated by the target (quote it)" (:58).
- out-283-a, Step 1: "\"Move from our two-bedroom city apartment to a bigger suburban house before our kids…\"". The user wrote "we want to move from our two-bedroom city apartment to a bigger house in the suburbs before our kids…".
- out-283-b rewords it the same way; both label A1 [T] with no quote.
- In out-283-a, "A5 [T]: Good reviews mean the school is good for your kids" is a reconstruction; the user only said "the school there has good reviews".
Under Rule 4 ("never invent … quotes") these are fabricated quotes.
At :54, replace "with a quote" with "with an exact quote (copy the target's words; never reword inside quotation marks)".
Add to :58: "A line you had to reword or infer is [A], even if it restates what the target said."

**N5 (should-fix): the docs contradict each other on assumptions-only requests.**
- The design note (:49) says "\"What are the hidden assumptions in my plan?\" … routes here".
- The description now says "Use only when asked for a counterplan or a devil's advocate" (:3).
- In Part O, the nearest cell ("What hidden assumptions is my case for the four-day week resting on?") is expected to go to **dia-warrant**: Codex var2 loaded dia-warrant 2/2, and Claude loaded nothing 3/3.
- spec §5.9 (line 214) gives warrant's border as "a plan's assumptions to dia-counterplan". No cell probes a pure plan prompt.

The :35 fallback is sound; the routing claim is unsupported. Replace design:49 with:
"\"What are the hidden assumptions in my plan?\" without a request for a counterplan is not in this skill's triggers (\"Use only when\"). If the skill is loaded for it anyway, it runs Steps 1 to 3 and offers the counterplan in one line (diff review, finding 12). Routing is unprobed for a pure plan prompt; the nearest Part O cell (\"my case for the four-day week\") was expected and loaded as dia-warrant on Codex (2/2) and loaded no skill on Claude (0/3)."
Also add one Part O cell ("What are the hidden assumptions in our plan to open a second warehouse?") with an owner-chosen expectation.

**N6 (nit): the design note's probe paragraph is inaccurate (design:87).**
- "the four positive cells (1-4) loaded dia-counterplan": cell 3 (Postgres, `claude` target) was never run. `run.py` replaced it with `p-assume` ("Play devil's advocate on our plan to move to a four-day week …"), so the `claude` target is unprobed.
- Cell 9 was not run as written (`w-oped` asks for the unstated warrant, not "how well do the reasons … support").
- "Cell 7 on Codex needs a re-probe" is stale: var2 gives 0/2 (Part O).

Replace the first and last sentences with:
"Routing probes (Part O; cell 3 was replaced by \"Play devil's advocate on our plan to move to a four-day week: what if our key assumptions are wrong?\", so the `claude` target is unprobed; cell 9 ran as an unstated-warrant prompt): the four positive cells loaded dia-counterplan 3/3 on Claude and 2/2 on Codex in both var and var2." … "On var2, cell 7 loads no skill on Codex (0/2)."

**N7 (nit): a leaning is recorded two ways.** Near-identical commute answers ("I lean toward the counterplan", drive untried) became "counterplan held (leaning)" in a and "Open, leaning counterplan" in b; no rule covers it. Add to Step 7 (:88):
"A leaning (\"I lean toward …\") counts as held only if the user says so; otherwise record the pair as open and note the lean in one word."

**N8 (nit): Rule 5 and the pick follow-up prescribe different replies.**
- Rule 5 (:43): say "no verdict because you wrote both sides" and point to the observations for "the key pairs".
- The follow-up (:124): "the result is their set" and the observation for "the pair they find hardest". The assistant cannot know that pair unless the user has said, and before any ruling there is no set yet.

Replace :124 with:
"- **The user asks for your pick:** Rule 5, during and after the inquiry; add that the result is their set (or will be, once they rule), and name the observation that would decide each open pair, or the one pair they name as hardest."

**N9 (nit): the assumptions-only branch has no ending defined.** :35 sits under "When this skill does not fit" but tells the skill to run anyway, and it does not say whether a record or the "one assistant wrote both sides" line follows. Append to :35: "No record; the output names the key assumptions only, not the plan's flaws (Rule 1)."
Also, spec §5.10 says "the record says one assistant wrote both sides". That is false for **no key assumption found** (:107). Append to it: "(except when no key assumption is found)".

## Real sessions vs the skill text

Mostly compliant: target line, evidence classes, SAST test, "supposing …" contraries, coherence and same-data lines, no verdict, a correct **undetermined**, the kept / Written by / Not tested lines with the fixed sentence, no tables. Violations: fabricated quotes and [T] labels (N4, 2/2); an unasked, over-cap K6 ruled (N3, out-283-a); "The date is not supplied" (N1, out-283-b). Minor, out-283-b only: text after Step 7's question ("Not tested so far"), against :50; Step 6 lacks the "Kn (plan) … / Cn (counterplan)" lines (:81); the closing "The three checks you named … decide four of the five pairs" (the user named two; they bear on three pairs). The changed F4/F9 branches were not exercised.

## Claims about counterplan

Design note D-F1–D-F11, D-F13, :5, :9: true. D-F12: (b), (c) not covered. Design:49 unsupported (N5); design:87 inaccurate (N6). Spec D35 and §4 rows: true (token total unverified); §5.10 nit in N9. Part O counterplan rows and the n-da-claim reading: true, but the design-note table was not the cell set run (N6).
