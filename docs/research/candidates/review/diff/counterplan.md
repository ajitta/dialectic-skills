Verdict: PASS WITH FIXES

Scope: `skills/dia-counterplan/` (SKILL.md, agents/openai.yaml, references/theory.md, references/output-template.md) at `b30344d`, against `docs/research/candidates/design/dia-counterplan.md` (cited "design"), `review/argumentation.md` (A-Fn), `review/scholastic.md` and `review/index.md` (I-Fn). Line numbers are file lines in the frozen tree. No blockers. Six should-fix findings (rule conflicts, the result set, phone length, the post-record pick, two fidelity gaps) and seven nits.

## What was verified and holds

- Scratch copy: `package.py --check` exit 0; `unittest` "Ran 19 tests … OK (skipped=1)"; `skills/` and `plugins/dia/` copies identical.
- Repo rules: no Hangul (L1 ranges); keys name/description/license/metadata; description 1,008 chars; body 122 lines; `short_description` 57 chars; one tool use, conditional (SKILL.md:41); theory.md read on request, template read "if you can open it" with the Step 8 field fallback (:16, :91), matching output-template.md:54-63; L6 = Rule 7 (:44), D26 = Rule 8 (:45), D19 at :119.
- Applied findings present and correct: A-F1 (theory.md:39, :41; Rule 3), A-F2 (theory.md:28-29; :104), A-F3 (:3, :14, :39, :65-70, :87; theory.md:11), A-F4 (:61; theory.md:15, :59), A-F5 (:25, :28, :111; theory.md:42-43), A-F7(c) (:3, :33), A-F12 (:43, :117), I-F1 (theory.md:44), I-F9 (:96, :102). The DA-default and DA-mode declines rest on owner decision, honestly reasoned at theory.md:34.
- Re-fetched and confirmed: Mason abstract (criterion 2); Cosier "requires specification of an alternative course of action"; Schwenk BEBR 814 (all four quotes, "new, encompassing view"); SEP Hegel quotes; IfM SAST test; Jacobs "more than 300", "let it stand"; Eduyot 1:5. Chiang/Cheng/Sharma/Lee/Huang not re-fetched (A-F5 table checked them).

## Findings

1. should-fix — Rule 3 and Rule 4 conflict on figures (check 2).
   Evidence: Rule 3: "if the plan names steps, costs or dates, so does the counterplan" (SKILL.md:40). Rule 4: "Never invent figures … a fact a side would need but neither has goes under 'not tested'" (:41). The follow-up at :118 lets the user name "a datum left out" as an asymmetry. Take a plan that says "build for $5M by Q3" and a counterplan of "outsource". The outsourcing cost exists in no datum. Rule 3 then demands a figure that Rule 4 forbids, and either way the user can claim the skill broke a rule.
   Replace the last two sentences of Rule 3 (:40, from "Write the counterplan at the same level of detail…") with:
   "Write the counterplan at the same level of detail as the plan and cite the same data: if the plan names steps, costs or dates, the counterplan names the same slots. Where a slot needs a figure that neither side has, write the slot with "not supplied" and list it under "not tested"; that counts as matching detail, and Rule 4 wins. Say in one line of the output that one assistant wrote both sides."

2. should-fix — The result set overlaps, and the "always" record lines do not fit one result (check 2).
   Evidence: "**undetermined:** at least one pair left open" against "**stopped:** the user stopped before ruling" (:96, :98). A user who rules on two of four pairs and then says "enough" fits both. The sibling dia-conjecture defines it precisely: "**stopped before testing** (no case was ruled on)" (dia-conjecture/SKILL.md:112). Separately, "The record always says" (:100) requires "Written by: one assistant wrote both sides of this comparison" and "Kept for the side set aside". Under **no key assumption found** (:63) no counterplan, comparison or pair exists.
   Replace :98 with:
   "- **stopped:** the user stopped before ruling on any pair. If they stop after ruling on some, the result is **undetermined** and the unruled pairs are open."
   Replace :100 with:
   "Unless the result is **no key assumption found**, the record always says:"
   Add after :104:
   "For **no key assumption found**, the record says instead: Not tested: whether the shared data are accurate, assumptions not listed, and alternatives to the plan; no counterplan was written, which does not show the plan is sound."

3. should-fix — The phone-screen rule cannot hold for several follow-ups the skill prescribes (check 2).
   Evidence: "Each follow-up turn fits a phone screen without scrolling" (:49; pitfall :132). Yet these follow-ups are long: a rewrite has to "redo Steps 4 to 6 for what rests on it" (:117); "An assumption the user adds goes through Steps 3 to 6" (:119); a changed plan means "rerun" (:120). The Step 8 record has nine fields with up to five pair lines, plus "Kept for the side set aside" per pair (output-template.md:54-63). None of these fits one screen.
   Replace the second sentence of :49 with:
   "A follow-up that only records rulings or answers a question fits a phone screen without scrolling. A rewrite or an added assumption shows only the changed lines (the new Cn, the counterplan steps that rest on it, the changed pair). A rerun on a changed plan, and the record, may be longer but use numbered lines, not tables."
   Change :132 to "- A ruling-only follow-up that needs scrolling on a phone."

4. should-fix — The post-record pick contradicts the label, Rule 5's own reason, and the over-reliance case (checks 3 and 4).
   Evidence: the description says "Picks no winner" (:3) and the body says "You give no verdict" (:14). Rule 5 grounds this in authorship: "this skill gives no verdict because you wrote both sides" (:42). The follow-up at :121 then says: "After the record, if they still want your view, … give it labelled as your own". The reason does not expire with the record. The rule also makes the verdict available to anyone who asks twice, which is the pressure pattern the skill guards against elsewhere. Index I-F8 names "it never picks a winner, so the decision stays with the user" as "the defensible reason" for picking dia-counterplan over dia-quaestio. The design note leaves this to the owner (design:48).
   Recommended (a): drop the pick. Replace :121 with:
   "- **The user asks for your pick:** Rule 5, during and after the inquiry. Say the result is their set, and name the observation that would decide the pair they find hardest."
   Alternative (b), if the owner keeps the pick: change "Picks no winner" in the description to "Picks no winner during the inquiry", and replace :121 with:
   "- **The user asks for your pick:** Rule 5. After the record, if they ask again, say the inquiry is over and its recorded result stands unchanged; give your view labelled as your own, name the pair it turns on, and add that you wrote both sides, so it is not an independent judgment."

5. should-fix — Two claims about Mason's procedure are not supported by the cited sources (check 3).
   Evidence (a): SKILL.md:16 says "In Mason's field study separate advocates argued the two plans before the managers", and theory.md:56 says "Mason had separate advocates and a group of managers". The only procedural source is Schwenk BEBR 814. It says Mason "obtained a strategic planning document from the company's planning department, identified its ten underlying assumptions, and constructed a counterplan based on opposite assumptions. The plan and counterplan were then presented to management in a structured debate." It does not mention separate advocates. In Mason's study, one person (the researcher) both surfaced the plan's assumptions and wrote the counterplan, which is close to what the assistant does here. The real departures are that the plan and the counterplan had different authors and that a group of managers judged them.
   Evidence (b): theory.md:19 says "Mason's counterplan rests on a coherent opposing view, not on item-by-item denials". Schwenk describes "the negation of these assumptions, and the development of a counterproposal based on the counter assumptions". The design's switch from negations to chosen contraries is sound (A-F3), but it departs from the cited description, and the departure list (theory.md §7) omits it.
   Replace the first sentence of SKILL.md:16 with:
   "In Mason's field study the plan came from the company's planners, the counterplan was built separately on opposite assumptions, and the two were debated before the managers."
   Replace theory.md:56 with:
   "- One assistant restates the plan and writes the counterplan; in Mason's study the plan and counterplan had different authors and were debated before a group of managers."
   Replace the third sentence of theory.md:19 ("Mason's counterplan rests on…") with:
   "Schwenk summarises Mason's step as \"the negation of these assumptions\" and a counterplan \"based on opposite assumptions\" (BEBR 814); taken item by item, a bare negation gives a plan nothing to rest on, so the skill picks contraries instead (a departure, §7)."
   Add to theory.md §7:
   "- Contraries replace the negated (\"opposite\") assumptions of Schwenk's summary."

6. should-fix — The *teyku* borrowing reverses the source's sense, and the Eduyot citation omits 1:6 (check 3; scholastic review F9).
   Evidence (a): Jacobs (fetched) describes a problem "always one of definition". With no authority it is "not simply without a solution but inherently insoluble since the two halves are so equally balanced", and it "'stands' for ever". In this skill, an undetermined pair is an empirical assumption the user, who is the authority, has not ruled on yet, and the record gives "the observation that would decide it" (SKILL.md:102; theory.md:51). The borrowing is labelled, but the label claims more than the analogy supports. The owner holds named methods to their originals.
   Evidence (b): theory.md:52 cites "Mishnah Eduyot 1:5–6" for "so that a later court may rely on it". Sefaria 1:6 (fetched) gives Rabbi Judah's rival reason: the minority view is recorded so that someone who cites it can be told "According to the [refuted] opinion of that individual did you hear it". scholastic review F9 flagged exactly this omission in the research document, and theory.md repeats it.
   Replace "(*teyku*, \"let it stand\", borrowed from the Talmud)" at SKILL.md:96 with:
   "(named after *teyku*, \"let it stand\", borrowed loosely from the Talmud)"
   Append to theory.md:51:
   "Unlike *teyku*, which Jacobs calls inherently insoluble, an undetermined pair here is open only for now; the borrowing is the refusal to force a choice, not a claim that the pair cannot be decided."
   Append to theory.md:52:
   "Eduyot 1:6 gives a rival reason (Rabbi Judah: the minority view is recorded so it can be identified as set aside); the skill follows 1:5."

7. nit — theory.md:23 overstates the study designs.
   Evidence: "All of these studies used human groups with separate advocates." The BEBR 814 lab study cited at :28 gave individual "Subjects in the DIS condition … the first planning committee report plus a second planning committee report". These are written reports, not groups or advocates.
   Replace with:
   "All of these studies used human participants who received a plan and a critique or counterplan prepared by different people, in groups or as written reports; none had one author write both sides."

8. nit — The worked example in Rule 2 asserts a new event, which brushes against Rule 4 (check 2).
   Evidence: "write \"demand stays flat as the two largest buyers merge\"" (:39). As written, it states a merger as fact.
   Replace with:
   "write \"demand stays flat (supposing, for example, that the two largest buyers merge)\""
   Add after "mark each one \"my choice\"":
   "A mechanism in a contrary is a supposition, never a reported fact."

9. nit — Two ruling cases are undefined (check 2).
   Evidence (a): :117 says "The user rejects a contrary: that is a ruling on the pair". It does not say which value the pair takes, and :142 of the template offers only "plan | counterplan | own | open". Evidence (b): "Kept for the side set aside: … the assumption the user did not hold" (:102) is unclear when the user answers in their own words; arguably both Kn and Cn were set aside. Also, "can't tell" (:87) maps to "open" only by inference.
   Add to :117 after "record it with their reason if they give one":
   "; the pair counts as the plan's assumption held unless they give their own wording or say they can't tell."
   Add to :102:
   "For a pair answered in the user's own words, keep the strongest argument for whichever of Kn and Cn their wording departs from more. \"Can't tell\" records the pair as open."

10. nit — The Procedure intro ignores its own early exits.
   Evidence: "The first response runs Steps 1 to 7 in one message and ends with Step 7's question" (:49). Step 1 can "ask … and stop" (:53), and Step 3 can "Go to Step 8" (:63).
   Replace with:
   "The first response runs Steps 1 to 7 in one message and ends with Step 7's question, unless Step 1 stops to ask or Step 3 finds no key assumption."

11. nit — The kept minority view is not labelled as a borrowing in the body.
   Evidence: teyku is labelled at :96, but "Kept for the side set aside" (:102) is labelled only in theory.md §6. The design note says "both labelled as Talmudic borrowings" (design:39). The intro (:14-16) never says the body has any non-Mason element.
   At the end of the first bullet at :102, add:
   "(borrowed from the Mishnah's kept minority opinion, theory.md §6)"

12. nit — Routing (check 5).
   The exclusion sentences agree: counterplan → brainstorm, conjecture, warrant, negative (:3); brainstorm, conjecture and warrant each point back here, and "universal claim" agrees with conjecture's "strictly universal". Remaining collisions:
   - (a) "What are the hidden assumptions in my plan?" or "in your recommendation above?" route here (warrant cedes them), but the skill always writes a full counterplan. The design note leaves this open (design:49); the skill has no rule for it.
   - (b) "Devil's advocate on my plan" usually means a critique, which theory.md:34 says the skill does not do, and "What's the strongest case against my plan?" or "Argue against my reorg plan" match no description phrase. They could land in counterplan, brainstorm's stress mode ("push back on this", brainstorm/SKILL.md:34) or negative.
   - (c) "Recheck your recommendation above; what if your assumptions are wrong?" fits dia-refine and the `claude` target here; neither excludes the other. dia-negative takes a "plan or policy" but has no pointer back.
   Add to "When this skill does not fit" after :34:
   "- The user asks only what the plan rests on, or only for its weak points, with no request for the opposing plan: run Steps 1 to 3, then offer the counterplan in one line."
   Otherwise, add probe cells for (a) to (c). docs/probes.md has no results for design:51-64 (grep "counterplan": none).

13. nit — The design note is stale: design:38 and :40 say the dia-brainstorm pointer is "not done here", but the diff adds it (brainstorm 1.2.0: "For a counterplan or devil's advocate on a plan, use dia-counterplan."). Replace design:38's last sentence with "dia-brainstorm's description gained the pointer in this batch (1.2.0)." In design:40, change the last sentence to "The dia-brainstorm pointer is made here; a dia-negative pointer is not."

## AI-chat risks (check 4)

Yielding: handled for contraries (Rule 6), the plan's assumptions (D19, :119) and "it's weak" (:118); the leak is the post-record pick (finding 4). Over-reliance: Rule 5, no suggested answer (:87), observations per pair (:81), false-assurance line (:104). One model both sides: disclosed at :83, :103, :111, theory.md §5. Invented premises: [T]/[A], "my choice", evidence classes, weak data turned into assumptions (:57); gaps are findings 1 and 8. The first response is several phone screens by design, ending in the one question the user must answer; follow-ups are finding 3.
