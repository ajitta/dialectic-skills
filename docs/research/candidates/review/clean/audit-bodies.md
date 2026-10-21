# Clutter audit of skill bodies: dia-warrant, dia-conjecture, dia-counterplan (+ brainstorm Step 0, reductio)

Line numbers refer to 0d5a949; the tree stayed clean. Tokens are cl100k. I measured each edit on a copy (`$TMPDIR/body-audit/cuts.py`; `validate_skill` passes). Evidence: `out-283-a/b`, the Part O replies (`~/work/dia-review/new-skills-2026-10-21/out2`, opening ~600 characters only), the reviews and the design notes.

## 1. Growth per round (lines / chars / tokens)

| file | b30344d | 283f6fa | 0d5a949 | growth |
|---|---|---|---|---|
| warrant SKILL.md | 142 / 16,507 / 3,956 | 143 / 19,200 / 4,589 | 145 / 20,047 / 4,796 | +21% tok |
| warrant output-template | 57 / 2,520 / 673 | 60 / 2,938 / 765 | 61 / 3,189 / 842 | +25% |
| warrant theory | 77 / 12,488 / 3,196 | 77 / 13,235 / 3,365 | 77 / 13,295 / 3,377 | +6% |
| conjecture SKILL.md | 135 / 14,353 / 3,545 | 135 / 15,413 / 3,791 | 136 / 16,220 / 3,993 | +13% |
| conjecture theory | 77 / 9,788 / 2,431 | 77 / 10,515 / 2,599 | 77 / 10,718 / 2,660 | +9% |
| counterplan SKILL.md | 132 / 13,049 / 3,064 | 135 / 14,784 / 3,455 | 135 / 15,522 / 3,631 | +19% |
| counterplan output-template | 63 / 2,700 / 736 | 65 / 3,214 / 855 | 65 / 3,314 / 879 | +19% |
| counterplan theory | 85 / 12,314 / 3,130 | 86 / 13,426 / 3,392 | 86 / 13,572 / 3,415 | +9% |
| brainstorm SKILL.md (main eb7ab54: 3,073) | 3,069 | 3,145 | 3,185 | +112 vs main |
| reductio SKILL.md (main: 3,117) | 3,150 | 3,150 | 3,150 | description only |

Lines barely moved (warrant 142→145) while tokens rose 21%. The growth went inside existing sentences as clauses, parentheses and "unless" tails: patches on patches. The dia-reductio body is unchanged on `next`, so nothing is proposed for it.

## 2. Comparison with the seven older skills (SKILL.md body, frontmatter stripped)

| | tokens | sentences >40 words | ";" per 1k tok | "(" per 1k tok | Rule/Step cross-refs per 1k tok |
|---|---|---|---|---|---|
| older seven (range) | 1,819–2,892 | 1–5 | 3.4–12.8 | 4.9–13.1 | 0–6.6 |
| dia-warrant | **4,507** | **17** (13 without the scheme lists) | **16.2** | **16.4** | 4.4 |
| dia-conjecture | **3,680** | **12** | 10.9 | **18.2** | **7.9** |
| dia-counterplan | **3,334** | **7** | **15.3** | 9.9 | **7.8** |

dia-warrant is the clear outlier: 1.56× the largest older skill, with 3–4× as many long sentences. Exception words are not elevated (2.0–3.9 per 1k tokens against 2.1–6.0); the density is semicolon chains and parentheses. Pitfalls are the other outlier. dia-reductio's pitfalls add new content (slippery slope, sorites). Here they restate rules: 5/7 in warrant, 6/7 in conjecture, 7/7 in counterplan.

## 3. Findings

### 3.1 Restatements (same rule in several places)

- **warrant**
  - R1. "none given" warrant ends as weakest link: warrant, stated 6×: L42, L45, L78, L121, L122, L134.
  - R2. The qualifier-only result is stated 3× in SKILL.md (L45; twice at L82). The template has the qualifier check 3× (L33–34, L38–39, L54). Session a printed the overstatement verdict 3×.
  - R3. Bare "yes" is no answer: L120 and L133.
  - R4. Provenance inside operative rules: the validity rule at L16, L41 and theory:46; the rule-5 departure at L42 and theory:43.
  - R5. Rule 9 (L47) restates Parameters L31.
  - R6. Pitfalls L139, L140, L142 and L144 restate Rules 3, 5, 2 and 1. Session a broke Rule 5 with both the rule and the pitfall present.
  - R7. The claude/text rejection (L134) restates the dispute bullet (L132).
- **conjecture**
  - R8. "Narrowing after the case = monster-barring, anchored to the Step 1 reading" appears at L31, L34, L83–85, L132 and theory:35, 42.
  - R9. Roles (L22–26) duplicates hard rules 4 and 7, Step 2 L63–64 and theory §6.
  - R10. The shape list (L16–20) summarises Steps 1–6.
  - R11. Conditional C′: L32, L100, L122.
  - R12. Pitfalls L130–136: 6 of 7 restate rules or steps.
- **counterplan**
  - R13. "One assistant wrote both sides": L41, L84, L104, template L45 and L60. Both sessions printed it 3× per output.
  - R14. The pick request is answered at L43 and L124.
  - R15. "Not supplied": L41, L42, template L35.
  - R16. "No key assumption found" is handled in 7 places (L50, L64, L98, L101, L107, template L52 and L65).
  - R17. Phone length / changed lines: L50, L122, L135.
  - R18. All 7 pitfalls (L129–135) restate rules.

### 3.2 Unexercised edge rules, long sentences, misreadings

No session or probe on any build exercises these reviewer-added rules:

- **warrant:** the target split on rejection (diff #5); the bare-answer rule (#4); the qualifier-only result (#2); "no warrant to compare" (pass2 N3); the "generally"-default note (N7); the close-case tiebreak (#8; pass2 itself found no routing effect); ask mode after its first question.
- **conjecture:** every Step 4 class except "counts" (diff #1); the three-level chain at L93 + L117 (local-only → built into C → deeper proof → record reason; diff #3 + pass2 N1); the record and the results.
- **counterplan:** the own-words kept argument and a rejected contrary's default (D-F9); stop-after-some and the no-key record (D-F2); the assumptions-only path (D-F12).

Sentences over 40 words with three or more nested qualifications:

- warrant: L35 (85 words), L82 (58; a double negative), L86 (71), L134 (52).
- conjecture: L83 (47), L96 (53 + 52), L117 (50; an exception inside an exception).
- counterplan: L50 (43), L124 (44).

Likely misreadings:

- **warrant Rules 3 + 5.** Every unqualified claim on a "generally" reconstruction is "overstated" (2/2 sessions), so "no weak link found" cannot occur for such claims. That is a design point, not clutter.
- **conjecture L44.** It forbids restating a policy as a claim, then supplies a sample restatement that the model may echo.
- **brainstorm L41.** "Add one line naming that skill, then continue" is unproven. On 283f6fa the analogous conjecture pointer produced no line in `cc-var2-c-poke-micro-2`, and cell 12 has not been re-run with the dia-warrant pointer.

### 3.3 Contradictions and drift

Nothing changes a result; I re-checked the result forms against the templates and theory. Minor drift:

- D1. In the warrant template, the record's Warrant field (L51) lacks Wa/Wb, which Step 7 L86 and template L18 have. Its reconstructed-warrant field has 4 values; Step 7 has 3.
- D2. "eight-question cap" (L55) vs "at most about eight" (L74).
- D3. warrant theory §5 (L53) omits the chain rule and the bare-answer rule as the skill's additions.
- D4. [T]/[A] translation: warrant Rule 8 translates tags, counterplan Rule 7 keeps them, and conjecture rule 11 translates them.
- D5. counterplan template L65 says "only" where SKILL.md L107 does not.

### 3.4 Real sessions on 283f6fa

**warrant (one audit turn each)**

- *Followed:* the target and mode line; stated / reconstructed / "none given"; the Usage rule (both flagged "ruins"); tags and statuses; 7 questions; two schemes; "compared with my reconstructed W…"; the fixed result; the tag→slot mapping; the Step 7 *fallback* record; the truth line and the ask-mode offer.
- *Ignored:* "read [the template] … if you can open it" (L16). Neither run called Read, although the counterplan runs in the same harness did, so the Step 7 fallback is load-bearing. Also ignored or broken: Rule 5 (a); "report beside the weakest link" (b); W1/W2 used for a chain (both; now the Step 1 chain rule); the truth line named the data (both).

**conjecture (6 turns each; two rounds; no record)**

- *Followed:* whose claim; "in my words"; one ask per message; [T]/[A] lemmas; the prior criterion in its own message; one checked case per message; local/global/both labels; numbered repairs with a recommendation; the definition change (b t5); the reconstruction offer (b t0, from Roles L25); the hidden lemma accepted by picking (b t6; an edge case that was exercised and followed).
- *Violated:* the "deeper" option was met by the counting case (a t6) and was near-tautological in both runs; user b said "just saying I save when I spend less". Round 3's Weaker-lemma and empty-tautology text answers this, so it is load-bearing.

**counterplan (the template was read)**

- *Followed:* nearly every structural rule.
- *Violated:* reworded quotes and [T] (2/2); a lean counted as held (a); K6 unruled and over the cap (a); "the date is not supplied" (b). All were fixed in round 3, so those fixes are session-driven.
- *Output clutter:* the both-sides line 3× and "no verdict" 2×.

No run of any kind exists on 0d5a949.

## 4. Proposals (exact text; savings measured one edit at a time; negative = adds tokens)

Ranked by saving against risk; "Del" deletes exactly the quoted span.

### dia-warrant: SKILL.md 4,796 → 4,427 (−369, −7.7%); template 842 → 811 (−31)

| # | Edit | Δ tok | Risk |
|---|---|---|---|
| W9 | Del Pitfalls L139, L140, L142 and L144 (strawman warrant; counter-facts; filling empty slots; "no weak link" as true). Keep L141, L143 and L145 (L143 is cited by design note Index F6). | −71 | low |
| W1 | Rule 3 L41: del " This adapts the pragma-dialectical validity rule (…) to a defeasible step: supply the premise the step needs, not one that makes it deductively valid." The label stays at L16 and theory §4. | −52 | low |
| W3 | Del Rule 9 (L47). Parameters L31 already defines the modes. | −30 | low |
| W5 | Step 6 L82, from "If no question asked is open…" to the end, becomes: `If every question asked is answered for the step, the result is **weakest link: qualifier** when Step 5 found an overstatement, and otherwise **no weak link found among the questions asked; not a proof** (list the questions and name the one you would ask next). Never invent a weak link. Give the Step 5 result next to the result in every case.` The logic is identical and the double negative is gone. | −41 | low |
| W8 | Follow-up L134, from "if they name none…" to "…changes the result.", becomes: `` if they name none, the warrant reads "none given" (Rule 7). For `claude` or `text` the user is not the arguer: the rejection is a dispute (above); a rule they propose becomes W2. `` | −38 | low |
| W4 | Step 5 L78, its last three sentences become: `If the warrant is your reconstruction, say so in the same line; if the overstatement comes only from the "generally" default, ask whether "certainly" was meant. With no warrant, write "no warrant to compare".` | −29 | low |
| W2 | Rule 4 L42, "When the user is the arguer … left implicit." becomes: `If the user is the arguer and disowns it, remove it (Follow-up turns; a departure, theory.md §4).` The honest label is kept. | −23 | low |
| W7 | Ask L121, "a "no" removes it; … on an early stop)." becomes: `a "no" removes it, and with no other rule the warrant stays "none given" (Rule 7).` L122 already covers "stopped". | −19 | low |
| W6 (merge R3) | Del from L133 " An answer counts only … keep its status." (−55). Append to Rule 5 after "say which.": ` An answer counts only if it supplies what the question asks for (a measure, a similarity, a reason, a source); a bare "yes" or "trust me" leaves it open.` (+39). L120: replace the sentence with ` A bare yes or no (Rule 5): ask once for the content, then mark it open.` (−2). | −18 net | low |
| WT1+2 | Template: del the "## Qualifier check" section (L33–34, −62). L39 becomes: `Qualifier check (always): the warrant (stated \| my reconstruction) licenses "…"; the claim says "…" → matches \| overstated (from the "generally" default? ask whether "certainly" was meant) \| no warrant to compare` (+33). L38's parenthesis becomes `(only if every question is answered for the step)` (−2). | −31 net | low (not read by Claude) |
| W10 | Scope L35, "Close cases: …" becomes: `Close cases: an argument (reasons given for a conclusion) stays here when the user asks to poke holes in it, for its hidden assumptions, or how well cases support an all claim; the same words about an idea or plan, or a request for counterexamples, go to the skills above.` | −48 | medium (after load; cells 12, 13, i-churn-all) |

Keep: the scheme lists (501 tokens; by design), the worked example (253; both sessions copied it), the Step 7 fallback, the chain rule, Rule 4 Usage, the Rule 5 evidence classes, and the L16 fidelity label. The cut body is still about 1.4× the largest older skill; the remainder is the owner's structural choice.

### dia-conjecture: SKILL.md 3,993 → 3,452 (−541, −13.5%)

| # | Edit | Δ tok | Risk |
|---|---|---|---|
| C2 (merge R9) | Del the whole `## Roles` section L22–26 (−150). Step 1 L57: after "argument or proof" add ` (if they have none, offer to reconstruct it as [A] lemmas)` (+16). Step 2 L63 becomes: `- An [A] lemma counts only after the user accepts it. If you reconstructed the proof, say in that message that you are then arguing both sides: you wrote the proof you attack.` (+22). | −112 net | low–medium: design-note F7 cites Roles; rules 4 and 7 and L14 still cover it (owner) |
| C6 | Del Pitfalls L130 and L133–136 (invented cases, bundling, empty repairs, easy holding, advisor drift). Keep "Exception lists" and "Unnamed monster-barring". | −129 | low (Step 5 keeps the empty-repair ban) |
| C4 (merge R8) | Step 4 L83–85 become:<br>`- **Invalid:** the user names a condition the case fails under the Step 1 reading. Check it: if the fault holds, withdraw the case ("invalid: fails [condition]"); if not, show that line once more. A reply that then narrows the term is monster-barring; one that keeps the Step 1 reading leaves the case disputed.`<br>`- **Concept-stretching:** the case meets C only under a reading of a term wider than the Step 1 reading. It does not count unless the user adopts the wider reading (a change to C, hard rule 5).`<br>`- **Monster-barring:** the user excludes a case that meets the Step 1 reading by narrowing a term ("that's not a real A", "by A I meant …"). Name the move and accept it only as a definition change: the new definition, the content lost, and that Lakatos's Rule 2 forbids it ("Do not allow a refutation to be dismissed as a monster"). The changed claim becomes C′.` | −115 | medium: never exercised; drops the explicit "ask whether" |
| C1 | L14: del " The shape:" and the list L16–20. The steps and the Step 6 cap say the same. | −112 | low–medium |
| C7 | Step 5 L96 becomes: `- **Weaker lemma** (Rule 2's "a suitable lemma"), for a global case, if you can find one: a condition weaker than the one you would build in, still usable by the proof, that more of C's cases meet but the counting case fails (show that in one line). Never offer a condition the counting case meets, or one that only restates B ("every A that ends up B is B"): that empties C (SEP's "empty tautology") and is not a repair.` | −41 | medium: session-driven, reworded only |
| C5 | Record L117: the tail "; a Rule 4 lemma replacement goes under Proof-analysis, not here, unless it widens C′ (then the reason is deeper proof)" becomes `; a lemma replacement that leaves C unchanged goes under Proof-analysis` | −16 | low (same rule; the exception chain is gone) |
| C3 | Step 5 L100: del " If the case rests only on your recall, mark the resulting C′ conditional." Hard rule 3 keeps it. | −16 | low |
| C9 (owner) | Optional: drop the local-only deeper-proof clause at L93 ("unless an earlier repair built Lj into C: … like any C′"), with "deeper proof" in L117, and relabel L14 "sections 1-5 …; section 6 not implemented". Not measured into the total. | ≈ −45 | label change: owner |

### dia-counterplan: SKILL.md 3,631 → 3,415 (−216, −5.9%); template 879 → 830 (−49)

| # | Edit | Δ tok | Risk |
|---|---|---|---|
| P6 | Del Pitfalls L129, L131, L132, L134 and L135. Keep L130 (strawman counterplan) and L133 (side-by-side as proof). | −75 | low |
| P2 (merge R14) | Rule 5 L43, second sentence becomes: `If the user asks which wins, during the inquiry or after it, say in one line that this skill gives no verdict because you wrote both sides and that the result is their set, and name the observation that would decide each open pair.` (+13). Del Follow-up L124 (−55). The owner's D-F4 (a) is kept. | −42 net | low |
| PT1 | Template L35: del " A slot (step, cost, date) whose fact … never "not supplied"." Rule 3 keeps it. | −49 | low–medium (the model read the template) |
| P3 (R17) | L50 becomes: `The first response runs Steps 1 to 7 in one message and ends with Step 7's question, unless it stops earlier (Step 1, Step 3, or an assumptions-only request). Later turns show only what changed (a new Cn, the counterplan steps on it, the changed pair) and fit a phone screen; a rerun or the record may be longer, in numbered lines, not tables.` (−38). L122: "Steps 3 to 7: show only the new lines and ask" becomes `Steps 3 to 7; ask` (−6). | −44 | low |
| P7 | Step 3 L64 becomes: `If none passes, say so, write no counterplan, and go to Step 8: the result is **no key assumption found**.` | −17 | low (L107 keeps "does not show the plan is sound") |
| P1 | Rule 3 L41: del " Say in one line of the output that one assistant wrote both sides." Step 6 and the record keep it; sessions printed it 3×. | −14 | low |
| P5 | Rule 3 L41: " Where a slot needs … and Rule 4 wins." becomes ` Where a slot needs a fact neither side has (a price, a measured quantity), write "not supplied" (Rule 4); that counts as matching detail.` | −13 | low |
| P4 | L103: del ` "Can't tell" records the pair as open.` (Step 7 and the result definitions say it.) | −11 | low |
| P8 (theory) | theory.md:34: del the two sentences from "A request for a devil's advocate on a plan …" to "… does not belong to this skill." They are routing text, restated from the description and from "When this skill does not fit". | −72 | low (read only on request) |

Keep (session-driven): L54, L58, L88, L122, and "…is not a fact: name it" (L41).

### dia-brainstorm Step 0: 3,185 → 3,163 (−22)

B1, L41: the first sentence becomes `A request for the opposing plan, a counterplan or a devil's advocate on a plan belongs to dia-counterplan; counterexamples to an all, always or never claim about what is the case (not a policy), to dia-conjecture; how well the reasons given support a conclusion (an argument, not an idea or plan), to dia-warrant.` Keep the second sentence. Low risk; the paragraph's effect is unproven (3.2).

**Total, non-optional edits: −1,228 tokens** (warrant −400, conjecture −541, counterplan −265, brainstorm −22), plus −72 in theory. Conjecture ends below b30344d (3,452 vs 3,545); counterplan gives back 38% of its growth, warrant 44%.

## 5. Re-runs before adopting (A/B: 0d5a949 vs the cut build; 0d5a949 has never been run)

1. **README example sessions** (`run_example_sessions.py`, n≥2 per arm):
   - warrant: W4, W5 and WT, the chain warrants, and the truth line naming C.
   - conjecture: C2 and C7, with `turns` ≈8 plus "wrap up" so the record, the result order and C5 are exercised.
   - counterplan: P1, P3, P5 and PT1.
2. **New personas** for rules nothing exercises today:
   - warrant: a user who rejects the reconstructed warrant and answers one question with a bare "yes" (W6–W8).
   - conjecture: a user who says "that's not a real bulk purchase", and one who says "no" with no condition (C4).
   - counterplan: a user who asks "which would you pick?" (P2).
3. **Part O cells** (Claude n=3, Codex n=2):
   - warrant: w-churn, w-expert-ko, w-oped, w-ask-ko, w-darkmode; for W10, w-poke-arg (cell 12), w-hidden (13) and i-churn-all.
   - conjecture: c-memo, c-micro, c-regular-ko, c-deploy-ko, c-neg-friday, c-neg-refund.
   - counterplan: p-4day, p-warehouse-ko, p-outsource-ko, p-assume, n-da-claim.
   - brainstorm (B1): w-poke-arg, c-poke-micro, s-poke-cafe, s-poke-startup, s-verify-ko. Check for the pointer line.
4. **`tools/package.py` after the version bump, then the unit tests.**

Adopt an edit only if the cut arm is equal or better. Where the 0d5a949 arm already fails, the failure is not the cut's, and it must not be fixed with new text first.
