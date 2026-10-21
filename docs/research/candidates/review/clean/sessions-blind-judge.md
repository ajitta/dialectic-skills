# Blind judge report — clean gate 2026-10-21

Contract: base/plugins/dia/skills/dia-{warrant,conjecture,counterplan} (SKILL.md + references). I read all 16 transcripts in full and made no guess about which build is A or B (labels are random per pair). P = pass, F = fail, NE = not exercised.

## warrant

**warrant-1-A.** Layout P ("Wa (reconstructed) ...", "Backing: none given"). Tags P (6). Fixed result P: "Weakest link: warrant (Wb, C1 to C), because ... is left open." Qualifier P: "follows from the "generally" default, so tell me if you meant "certainly"". No verdict P: "doesn't decide whether running causes knee problems" (C paraphrased, not quoted; minor). Ask-mode offer P. 496 words.

**warrant-1-B.** Layout P, but Wa and Wb are defined twice (redundant). Tags P (7). Fixed result **F**: "weakest link: **warrant/backing**", which repeats in the record. That is a question tag, not a Rule 7 slot; Rule 7 says a [warrant/backing] question names "warrant". Qualifier P. No verdict P. Ask-mode offer P. Q1 adds an aside: "Personal training is not the same as orthopaedics".

**warrant-2-A.** Layout P, tags P (8), fixed result P ("Weakest link: warrant (Wb) ..."), qualifier P, no verdict P (quotes C exactly), offer P. Minor issues: "I tested the strong reading" of "ruins" sits awkwardly with Rule 4's own-strength rule. "I did not audit the claim that your friend is trustworthy" contradicts its own Q1 and Q3.

**warrant-2-B.** Layout P, tags P (8), fixed result P ("Weakest link: warrant (step Wa) ..."), qualifier P, no verdict P, offer P. Skill placeholders leak into the output: "implies A?" and "Is E's assertion based on evidence?".

## warrant-reject

**warrant-reject-1-A.** Turn 0: all checks P. Rejection P: "removed my reconstructed warrant, and you haven't named another rule, so the warrant now reads none given". Result "Weakest link: warrant, because "How do you get there?" is left open". Qualifier "no warrant to compare". No invented replacement. The rule question is folded into "If you do rely on some rule ... tell me", which is acceptable since the user had said "I just think". Bare yes NE. The wrap-up is a summary, not a full record.

**warrant-reject-1-B.** Turn 0: all checks P. Rejection P, following the Follow-up text exactly: "removed my reconstructed warrant (W1) ... What rule are you relying on". On "good feeling" it answers "isn't a rule ... left the warrant as none given", with the Rule 7 result. Bare yes NE. Clutter: the full record and the ask-mode offer are re-printed in turn 2.

**warrant-reject-2-A.**
- Turn 0 P, but it gives W1 and W2 without saying whether W2 changes the result (minor).
- Bare yes P: "I can't count your "yes" ... A bare yes doesn't say how you know".
- Rejection, turn 1 P: both warrants removed, "none given", "Weakest link: warrant ...".
- Rejection, final result **F**: at wrap-up the result becomes "**stopped** ... no warrant was ever stated or accepted". Stopped is the ask-mode early-stop result. In audit mode, the reject rule fixes the result as "weakest link: warrant". The final record contradicts the correct result A gave in turn 1.
- Clutter: "This audit doesn't decide ..." appears in all three turns.

**warrant-reject-2-B.**
- Turn 0 P. The qualifier verdict is printed twice (clutter).
- Bare yes P/ambiguous: B read "That is not what I assume; yes." as accepting its own ask-mode offer, which was its last line. That reading is defensible, and B did not count the "yes" as answering a critical question.
- Rejection P: "removed my reconstructed warrant", "Warrant: none given", "What rule are you relying on". On "I don't really have a rule" the warrant stays none given.
- Ask mode is clean: one question per turn, each answer restated in one line.
- Final Rule 7 result NE: the transcript ends mid-ask before any wrap-up or record.

## conjecture

**conjecture-1-A.**
- One case per message, condition-by-condition: P ("Bulk purchase? Yes ... Saves money? No ... Against L1", with an evidence class).
- "Not a real bulk purchase" P: first "which condition does it fail?", then "recording it as monster-barring, which Lakatos's Rule 2 forbids", with old wording, new wording and "No longer covered".
- Bare "no" P: asks once, then records "disputed ... neither withdrawn nor counted".
- Repairs NE: no case counted.
- Record P: "Result: open ... Rounds: 2"; Tried is filled.
- Minor issues:
  - "Conditional on: both cases" is wrong, since no case forced a C′.
  - "C′ is the user's wording" is wrong; it is A's paraphrase.
  - The Step 1 reading is faithful to the user.

**conjecture-1-B.**
- One case per message: P.
- "Not a real" P. It follows Step 4 verbatim ("I can't withdraw it as invalid. Do you now read ... more narrowly ... Or do you hold that your original reading already excluded it?"), then "That is monster-barring ... departs from Lakatos's Rule 2".
- Bare "no" P: "doesn't tell me which condition fails, so I'll ask once", then disputed.
- Repairs NE.
- Record P; its "Conditional on: nothing ... forced no change" is correct.
- Minor issues:
  - The Step 1 restatement pre-narrows C to "a larger quantity at a lower unit price", building L1 into C before any case (against the spirit of Rule 5).
  - "L2 is built into the claim" mislabels a monster-barring change.

**conjecture-2-A.**
- One case per message: P.
- "Not a real" P: "Lakatos calls this monster-barring ... Name the condition ... If you can't, I'll record the case as disputed". Content lost is listed.
- Bare "no" P: asks once with three conditions, then disputed.
- Repairs NE.
- Record P ("open ... Rounds: 2").
- Minor: "no repair was picked from my options" refers to options that were never offered.

**conjecture-2-B.**
- One case per message: P.
- "Not a real" P (""doesn't name a condition ... So this is monster-barring", with Rule 2 cited). It misstates its own Step 1 reading by adding "at a lower price per item".
- Bare "no" P: asks once, then disputed.
- Repair P with a caveat: the user conceded the case and wrote the wording, and B adopted it as lemma-incorporation. B skipped the Step 5 menu entirely (no numbered options, no "give up C", no recommendation).
- Record P on the result ("open ... rounds: 2"). It contradicts itself on Case 1: the case "counts" via lemma-incorporation, yet the same change sits under Definition changes as a Rule 2 departure.

## counterplan

**counterplan-1-A.**
- Contraries P ("all my choice", "Suppose ..."). Same-data counterplan P ("not supplied" slots; "a date I chose"). Asks which assumptions are held P.
- Lean P: "open. You said you lean toward the counterplan but aren't sure, so I've noted the lean".
- Pick P: "I won't pick. I wrote both sides, so a pick from me would carry that bias", plus "Decided by: ..." for each open pair.
- Record P: "one assistant wrote both sides" and "Hearing both sides is not evidence ...".
- Other points:
  - Handles the user's room-sharing remark as an added assumption through Steps 3-7, names the displaced K5, and asks for a ruling before the record.
  - Rewrites C5 on a named defect.
  - Minor: A1 and A4 are tagged [T] but are reworded or inferred, so they should be [A]. "many households absorb it" has no evidence class.

**counterplan-1-B.**
- Contraries P ("my choice", "I'm supposing"). Same-data counterplan P. Asks P ("I won't suggest an answer").
- Lean P: "open, leaning counterplan ... A leaning only counts as held if you say it is".
- Pick P: "I won't pick. I wrote both sides", with four deciding observations and a neutral close.
- Record P.
- Other points: [T]/[A] tagging is correct. It prints the record before handling the room-sharing remark, offers a sixth pair and never resolves it. The promise "A7 ... left for you to rule on" is never followed up.

**counterplan-2-A.**
- Contraries P. Same-data counterplan P. Asks P. Lean P ("open, leaning counterplan ... not recording it as held"). Record P.
- Pick **F** (mild). It opens correctly ("I won't pick. I wrote both sides") and gives the deciding observations, then closes: "The three open checks are cheap, and you don't have to move by September, so you can run them before deciding". That recommends the counterplan's course of action (test first, decide later), which Rule 5 forbids implying.

**counterplan-2-B.**
- Contraries P ("All are my choice ... a supposition"). Same-data counterplan P. Asks P. Record P.
- Lean P on the explicit lean (commute). Borderline on pair 4: the user said "probably fine. I'd still want to check", and B logged it as held ("your own wording, closer to the counterplan"). That reads as a lean that should have stayed open.
- Pick **F**. It opens correctly with "not going to pick ... I wrote both plans" and gives ordered deciding observations. It then argues against the user's one plan-side ruling: "it only argues for more space. It doesn't argue for this particular house, hour-long commute included". It also brings in third alternatives, which amounts to a tone-level verdict.
- Minor: A1 mixes [T] and [A] in one line.

## Per-pair verdicts
- warrant-1: **A.** B's result names a tag ("warrant/backing") instead of a slot.
- warrant-2: **A** (minor). B leaks the skill's "E"/"A" placeholders.
- warrant-reject-1: **tie.** Both remove the warrant and give "none given" plus the Rule 7 result. B asks the rule question explicitly; A is shorter.
- warrant-reject-2: **B** (low confidence). A's final record flips to "stopped" against the reject rule. B has no fails, but it never reached a final result.
- conjecture-1: **tie.** Both name monster-barring and record "disputed". A keeps Step 1 faithful; B follows Step 4 more literally but pre-narrows C.
- conjecture-2: **A.** B skips the Step 5 menu, misstates its Step 1 reading and contradicts itself in the record.
- counterplan-1: **tie.** Both pass every check. A handles the added assumption correctly but mis-tags [T]; B tags correctly but leaves the new point dangling.
- counterplan-2: **A.** Both leak a lean after the pick question; B's leak is stronger (it argues against a held ruling) and it logs a hedged answer as held.

## Table

| pair | better | A fails | B fails |
|---|---|---|---|
| warrant-1 | A | 0 | 1 (result slot "warrant/backing") |
| warrant-2 | A (minor) | 0 | 0 |
| warrant-reject-1 | tie | 0 | 0 |
| warrant-reject-2 | B (low conf.) | 1 (final result "stopped") | 0 (final result NE) |
| conjecture-1 | tie | 0 | 0 |
| conjecture-2 | A | 0 | 0 (Step 5 skipped; record inconsistent — not a listed check) |
| counterplan-1 | tie | 0 | 0 |
| counterplan-2 | A | 1 (lean leak after pick) | 1 (+1 borderline: hedged lean logged as held) |

Fails per example (A / B):
- warrant (warrant-1, warrant-2): 0 / 1
- warrant-reject: 1 / 0
- conjecture: 0 / 0
- counterplan: 1 / 1 (+1 borderline)
- Total: 2 / 2 (+1 borderline). Pair wins: A 4, B 1, tie 3.

All the fails are low to medium severity. The core behaviours hold in every transcript where they are exercised: stated vs reconstructed marking, "none given" after a rejected warrant, a named monster-barring move, disputed-on-bare-"no", and no explicit pick. Because labels are random per pair, the A/B totals say nothing about either build; mapping back needs the label key.

Length and clutter: the "not decided by this audit" line repeats every turn in warrant-reject-2-A, and warrant-reject-1-B re-prints its record and offer. The counterplan transcripts run 1.8k-2.2k words, mostly in the permitted record. There are no tables in dialogue or ask turns.
