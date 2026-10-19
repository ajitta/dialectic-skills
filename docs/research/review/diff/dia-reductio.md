Verdict: PASS WITH FIXES

Scope: `git diff cae2e4d 7115d2a -- skills/dia-reductio` (D19 commit fcaf7a2 + D20 commit 7115d2a), plus the reductio parts of docs/spec.md, README.md, tests/. Line numbers refer to the tree at 7115d2a.

Checks run in the tree (read-only):
- `python3 tools/package.py --check` -> "ok" for all seven skills, exit 0.
- `python3 -m unittest discover -s tests` -> "Ran 13 tests ... OK (skipped=1)", exit 0.
- SKILL.md 134 lines (limit 200); description 824 chars (limit 1024); no Hangul and no product names in any reductio file (scripted scan); `claude` appears only as the D14 target value.
- Version: plugin stays 0.1.0 with a re-recorded digest. tools/package.py:17-20 sanctions this before a first release ("delete the record and rebuild"), so it is not a finding.

Verified correct (no action):
- F1: SKILL.md:57, :108, :112, template:48 replace consistency/independence with "no contradiction found". The logic holds.
- F2 in the review's corrected form: SKILL.md:34 says "[L] a law of logic or mathematics" (not "arithmetic"), and "A definition is [T] only when the target states it (quote it)" (no "or accepted").
- F4 in the review's corrected form: SKILL.md:33. "all X are Y" / "some X is not Y" are contradictories. "all X are Y" / "no X is Y" conflict only given that some X exists. Both checked.
- F5: SKILL.md:35 keeps "and so on" and adds "simplification, arithmetic". SKILL.md:67 adds the letter-substitution reread. template:51 adds the "Checked by" line. The closed rule list was not adopted, as the review asked.
- F6: the SKILL.md:83-96 worked example follows the review's fix. I checked it line by line. P1 is (Fh∧Sh)→Rh by UI; line 3 is a conjunction of lines 1 and 2; line 5 is MP; line 6 is simplification. Lines 5 and 6 are contradictories. The depends-on set {T,P1,P2} is all [T], so "internal" is correct, and Rule 6 correctly withholds "the thesis is false". The example is more granular than the review's version (it adds the conjunction step), which makes it more correct.
- F7/theme 2: SKILL.md:117 keeps only "do not invent a contradiction", per the review. SKILL.md:124 adds the named-defect criterion.
- F9/theme 3: SKILL.md:34 and template:17 add "supplied by the user" and "Your own recall is never 'verified'".
- M1 and M2 for the grades: SKILL.md:73-79 and template:27, :31-32, :49-50. The "carried" test now reads "without the assumption ... its negation". That is valid in both directions.
- F3 / theory.md:32: the IEP §5 title "Doctrinal Annihilation: Sets of Statements that Are Collectively Inconsistent" is verbatim (fetched iep.utm.edu/reductio). The Duhem credit matches SEP "Underdetermination" (Duhem: "the experiment does not designate which one should be changed"). The Quine credit is fair ("revise even beliefs about logic"). The review's objection to "and says so when that matters" is met: the clause was dropped.
- M3/theme 1: agents/openai.yaml:4 uses `$dia:dia-reductio`. tests/test_package.py:62 and spec §7.3 and §12.2 P3 agree.

Findings

1. should-fix — SKILL.md:79 (and :100). This rule is new and logically wrong. Neither the research nor the review asked for it.
   Text: "For **premise set inconsistent**, the premises both derivations share (apart from T and not-T) are what must be revisited; the options turn on them."
   Problem: suppose derivation A uses {T} ∪ S_A and derivation B uses {not-T} ∪ S_B. Then S_A entails not-T and S_B entails T. The inconsistent set is therefore S_A ∪ S_B, not S_A ∩ S_B. Counter-example: S_A = {T→Q, not-Q} and S_B = {not-T→R, not-R}. They share nothing, yet the set is inconsistent. Under this rule the options would be empty. Dropping any non-shared premise is a legitimate option. A shared premise is merely one that breaks both derivations at once. Separately, Step 6 (:100) says "T included", which conflicts with :56 ("the fault is in the premises, not T").
   Replacement for :79: "When the direction is both, state and grade each contradiction separately, and the record gives one line per direction. For **premise set inconsistent**, one derivation's premises entail T and the other's entail not-T, so the premises of both derivations together (apart from T and not-T) cannot all hold. The options are the premises of either derivation, not T; a premise both derivations use breaks both at once, so name it if there is one."
   Replacement for :100, first sentence: "One option per member of that set that could be given up, T included (except when the result is premise set inconsistent)."
   Also add the rule to the D20 reductio list in spec.md:65.

2. should-fix — SKILL.md:63, :36 and output-template.md:18. The narrowed Rule 2 conflicts with the unlabelled "key terms" line.
   Rule 2 (:34) now says "a definition the target did not state" is [A]. Rule 3 (:35) allows only "substitution of a listed definition". But Step 3 (:63, "labels [T], [L], [A] and the meaning of key terms"), Rule 4 ("Fix the meaning of each key term in the premise list") and the template line "- Key terms: X = …, Y = …" record meanings with no label. A meaning the assistant supplied can therefore be substituted into a line and still leave the grade at "internal". That is exactly the definitional smuggling D19 meant to close (research §6.1 item 4).
   Replacement for :63: "Number them P1, P2, … with labels [T], [L], [A]. A key term's meaning that the derivation relies on is a premise too: [T] if the target stated it (quote it), otherwise [A]. Keep the list to what the derivation uses."
   Replacement for template:18: "- Key terms: X = … [T \"quote\" | A], Y = … (a meaning a line substitutes gets its own P-line)"

3. should-fix — SKILL.md:33, last sentence: "List it [L] or [A] and let the contradiction depend on it."
   This came from the review's text, which was written before [L] was narrowed. "some X exists" is almost never "a law of logic or mathematics" (:34), so offering [L] invites an existence premise to pass as [L]. That would make the grade "internal" and, under Rule 6, could license "the thesis is false". The sentence also omits [T] for the case where the target said it.
   Replacement: "List it with its label ([T] if the target said it, [L] only if it is a theorem of mathematics, otherwise [A]) and let the contradiction depend on it."

4. should-fix — M1 was applied only in part. It was fixed in the grades but not in the rest of the template or text.
   output-template.md:20-21 ("## Derivation (assume T)" / "1. T — assumption") and :26-27 ("(assume not-T) (only when the direction is "both" …)") leave a prove-only run with no derivation block. template:30 "Depends on: T, P1, P3 [A]" is refute-only. SKILL.md:112 "…or that the thesis is true" is the wrong non-claim in a prove run. SKILL.md:38 (Rule 6) has no prove-direction counterpart.
   Replacements:
   - template:20 "## Derivation (assume T; when proving, assume not-T)"
   - template:21 "1. T (not-T when proving) — assumption"
   - template:27 "(only when the direction is "both": the not-T derivation, same format, and its own contradiction and strength below)"
   - template:30 "Lines a and b. Depends on: T (or not-T), P1, P3 [A]."
   - SKILL.md:112, quoted sentence "no contradiction found with these premises; this does not show they are consistent, or settle whether the thesis is true"
   - SKILL.md:38 "Write "the thesis is false" (when proving, "the thesis follows") only when every other premise it depends on is [L]."

5. should-fix — theory.md:32 vs theory.md:3 and :66-70. The new sentence credits "Duhem and Quine". But :3 says "Sources are listed at the end; everything here is paraphrased from them", and the Sources list still holds only IEP, EoM and Wikipedia. Research F3 asked for these URLs to be added; that part was not applied. The attribution itself is correct (verified above).
   Add to Sources:
   "- \"Underdetermination of Scientific Theory\", *Stanford Encyclopedia of Philosophy* (Duhem's and Quine's holism). https://plato.stanford.edu/entries/scientific-underdetermination/"
   "- W. V. O. Quine, \"Two Dogmas of Empiricism\" (1951), §6. https://www.ditext.com/quine/quine.html"

6. nit — SKILL.md:34 and output-template.md:17. "verified this session" is still undefined. Research F9 proposed "(a tool ran)". Without it, "supplied by the user" and the assistant's own re-derivation overlap with "verified", which is the theme-3 ambiguity.
   Replacement in both places: "verified this session (a tool ran)".

7. nit — SKILL.md:133. F1's proposed pitfall was not added. The pitfall reads only "Treating "no contradiction found" as "true"."
   Replacement: "Treating "no contradiction found" as "true" or as "consistent"."

8. nit — documentation drift.
   (a) spec.md:65 (D20) omits the Step 4 letter-substitution reread (:67) and the own-scheme label (:81).
   (b) spec.md:64 (D19) omits the `claude`-target line (:117), which is a behaviour change.
   (c) docs/research/README.md:49 lists reductio F10 as open, although its label half is applied at SKILL.md:81. F8 and M5–M7 are listed nowhere.
   (d) docs/handoff.md:27 still points to "`docs/research/README.md` § Not applied yet", a heading that no longer exists. The current heading is "Applied, second batch", and item 9 should say D19 and D20.
   Suggested text for handoff.md:27, Notes: "High findings and themes 1–4 (D19) and the second batch (D20) applied 2026-10-20, still as 0.1.0. Remaining findings: `docs/research/README.md` § Still open; settle them with the owner before P1."

Summary by check: (1) every intended item uses the review's corrected form; one rule goes beyond intent (finding 1). (2) Contradictions: findings 1–4; the worked example agrees with the rules. (3) The citations hold; only the Sources entry is missing (finding 5). (4) Logic is valid except finding 1. (5) Partial: findings 4–7; M5–M7, F8 and F10–F15 are open by design. (6) D19/D20 match, with the omissions in finding 8. (7) Both commands pass.
