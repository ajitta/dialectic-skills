Verdict: PASS WITH FIXES

# Diff review: skills/dia-conjecture (next b30344d vs main eb7ab54)

Scope: `skills/dia-conjecture/{SKILL.md, agents/openai.yaml, references/theory.md}`, checked against `docs/research/candidates/design/dia-conjecture.md`, `review/modern-dialectic.md` and `review/index.md`. Line numbers are from `skills/dia-conjecture/SKILL.md` unless another file is named.

## What I ran

- In a scratch copy: `tools/package.py --check` all `ok`; `unittest`: `Ran 19 tests ... OK (skipped=1)`; `skills/dia-conjecture` identical to `plugins/dia/skills/dia-conjecture`.
- Check 6 (repo rules) passes: description 1,018 chars; body 124 lines; frontmatter keys name/description/license/metadata(author, version, lineage, source); no Hangul; no product names; tool use conditional (lines 32, 126); theory.md read only on request (line 14) and the body is self-sufficient; `openai.yaml` short_description 54 chars, `$dia:dia-conjecture`.
- Sources fetched 2026-10-21 (SEP Lakatos, SEP Popper, Easwaran PDF, CUP front matter, BJPS 1963 scan, arXiv 2605.03936). Every quotation in theory.md I tested is verbatim, including Rules 1-3 and Rule 4 (Easwaran n. 5), "unproductive responses ... that he rejects", the local/global definitions and "I meant" (BJPS), "hidden lemma", "empty tautology", "deeper problem", "Popperian Gamma", "frivolous concept-stretching" (SEP), "laid down beforehand", "flatly denies" (SEP Popper), and 60 CEs / 32% vs 60% / 69% to 17-30% / "upper bounds" / "laundry list" (Counterexample Game).

## Check 1: review findings vs skill text

Applied and correct: MD-F4 for [A] lemmas (line 25), MD-F5 (line 14; precision nit in finding 11), MD-F6 (theory.md §6, figures match the paper, no fit rating), MD-F9 (line 65, theory.md:44, Gamma to SEP), MD-F10 (lines 123, 126), MD-F11 (line 30, repair its own message at 89), the recall-conditional note (lines 32, 100, 122), IX-F7 (line 24, theory.md:49).
Applied with defects: MD-F1 (deeper proof and §6 mapping, finding 3), MD-F2 (monster-barring class, finding 1), MD-F3 ("policies" missing from the description's exclusion, finding 5), MD-F4 (two undisclosed both-sides paths, finding 10), IX-F10 (decline reason for the brainstorm pointer stale, finding 6).
Declines: the replacements of "at most three", the old Step 5 menu, the old "doesn't count" rule and the stop rule, dropping "fit: high", and asking for the argument first are each justified by the finding cited. The OQ3 decline ("outside this batch") is contradicted by this commit, which edits dia-brainstorm's description (finding 6).

## Findings

### 1. should-fix: monster-barring is defined so that real monster-barring escapes it, and this contradicts hard rule 5

Evidence:
- Line 85: "**Monster-barring:** the user concedes that the case meets C's stated terms but excludes it by redefining a term". Lakatos's monster-barrer concedes nothing. Easwaran: monster barring is "claiming that a particular counterexample never was a member of the domain to begin with". BJPS, Delta: "of course I did not mean that any system of polygons is a polyhedron. By polyhedron I meant …".
- Under lines 83–84, that move becomes "disputed" (the user says they are not changing the term) or "concept-stretching" (the case "does not count against C as the user reads it"). Either way Rule 2's "Do not allow a refutation to be dismissed as a monster" is bypassed without being named.
- It also contradicts hard rule 5 (line 34: "a narrowed term is a change to C"): "the user's reading" has no anchor, so a post-hoc narrowing passes as concept-stretching, which is the yielding path. Step 1 (line 57) already fixes "what A covers"; use it as the anchor.

Replace lines 83–85 with:

```
- **Invalid:** the user names a condition the case fails under the reading of C fixed in Step 1. Check it. If the fault holds, withdraw the case and record "invalid: fails [condition]". If the case does meet that condition under that reading, show that line once more and ask whether the user now reads the term more narrowly: if so, it is monster-barring; if the user holds that the Step 1 reading already excluded it, the case is disputed.
- **Concept-stretching:** the case meets C only under a reading of a term wider than the one fixed in Step 1 (or stated by the user before the case was raised). Record it as concept-stretching; it does not count against C as so read, unless the user adopts the wider reading (then record the change, hard rule 5, and treat the case as counting). A narrower reading first stated after the case is never this class. Lakatos's further analysis of such cases (sections 8-9) is not implemented.
- **Monster-barring:** the user excludes a case that meets C as read in Step 1 by narrowing a term ("that's not a real A", "by A I meant …"), whether or not they call it a change. Name the move. Accept it only as an explicit definition change: the new definition, the content lost (the cases C no longer covers), and a note that this departs from Lakatos's Rule 2 ("Do not allow a refutation to be dismissed as a monster"). The changed claim becomes C′.
```

### 2. should-fix: the record lists Rule 4 as a reason C changed, but Rule 4 leaves C unchanged

Evidence: line 93, "Local only … Rule 4 … C is unchanged". Line 117, "**Claim:** C "…" → C′ "…", one arrow per change, each with its reason (Rule 4, lemma-incorporation, definition change, "I meant …")". Line 118 already has a place for replaced lemmas ("replaced: …").

Replace line 117 with:

```
- **Claim:** C "…" → C′ "…", one arrow per change, each with its reason (lemma-incorporation, hidden lemma built in, deeper proof, exception-barring, monster-adjustment, definition change, "I meant …"); a Rule 4 lemma replacement goes under Proof-analysis, not here
```

### 3. should-fix: the deeper-proof option can produce a C′ that the counting case still refutes, and §6 is mapped to the wrong branch

Evidence:
- Line 96: "**Deeper proof** … a different or weaker lemma the case does not refute, so that C′ keeps more of C's content, or covers the case as an instance instead of excluding it".
- For a global or "both" case (an A that is not B), building in a condition the case does not refute leaves the case inside C′'s antecedent, so C′ is refuted by the very case that counted. "Covers the case as an instance" is impossible for a global case.
- CUP contents: "6 Return to criticism of the proof by counterexamples which are local but not global. The problem of content … a. Increasing content by deeper proofs". Such a case (fails an incorporated condition, still B) reaches line 93, which says "C is unchanged"; but replacing an incorporated Lj widens C′, so the text is false and hard rule 7's pick is skipped.

Replace line 93 with:

```
- **Local only** (Lj fails, C survives the case): Rule 4. Replace Lj by a lemma the case does not refute and the proof can still use. C is unchanged, unless an earlier repair built Lj into C: then the replacement widens C′ to cover the case (Lakatos's deeper proof, ch. 1 section 6), and the user picks it like any C′.
```

Replace line 96 with:

```
- **Deeper proof**, where you can find one: for a global case, a weaker condition that the case still fails but more of C's other cases meet, so that C′ keeps more of C's content than lemma-incorporation (Lakatos, "increasing content by deeper proofs"). Never offer a C′ whose condition the counting case meets: that case is an A that is not B.
```

### 4. should-fix: the result values are "exactly one of" but overlap

Evidence: line 106, "Its result is exactly one of". Line 109, "revised … (C′ adopted)". Line 111, "open (a case is disputed …)". Line 86 sends a disputed case on to the next case, so a run with an early bare denial and a later adopted C′ fits both "revised" and "open". "Given up" can also coincide with an earlier dispute. With no precedence the assistant picks, and the friendlier value is the likely drift.

Replace line 106's last sentence and line 111 with:

```
… translated into the user's language. Its result is the first of these that applies:
```
and reorder the list as: **given up**; **stopped before testing**; **open** (a case against the current claim is disputed, or a counting case has no repair picked); **revised, holding against the cases tried**; **holding against the cases tried**.

### 5. should-fix (routing): "policies" is routed away in the body but not in the description

Evidence:
- Step 0 line 47: "a plan, policy, decision or idea: dia-counterplan …, dia-brainstorm …, dia-negative".
- MD-F3: "drop 'policies' from dia-conjecture's object. A counterexample to a policy needs a standard, and that is dia-negative's input."
- The description's object keeps "a rule" and the exclusion says only "Not for plans, decisions or ideas".
- Concrete collision: "Our policy: every refund is approved within 24 hours. Find counterexamples." The description claims it ("counterexamples to their … rule", "all/every"). dia-negative also claims it ("claim, concept, plan or policy … with particular cases"), and dia-negative has no pointer back.

Replacement in the description (measured result: 1,020 chars):
- "(all, every, always, never), such as a rule or generalization, splits" → "(all, every, always, never), a rule or generalization, splits"
- "Not for plans, decisions or ideas" → "Not for plans, policies, decisions or ideas"

### 6. should-fix (routing): the hardest pairs are not probed, and the brainstorm decline reason is stale

Evidence:
- Probes 5 and 7 (design note lines 67, 69) use each sibling's own keywords ("my idea", "its own standard"), so they cannot detect stealing.
- dia-brainstorm's description (edited in b30344d) still claims "poke holes in it, or … stress-test it"; its body keeps "hunt for counterexamples" (:34) and "Counterexample: general claim ('everyone needs X')" (:67); no pointer to dia-conjecture. This skill's "to poke holes or stress-test, dia-brainstorm" is scoped to plans and ideas but can be read globally.
- Design note line 30 ("outside this batch") is contradicted by the same commit's dia-brainstorm edit.

Add these rows to the probe table (exact prompts):

```
| 11 | "Poke holes in my claim that every microservice should own its own database." | dia-conjecture (universal claim; negative for dia-brainstorm) |
| 12 | "My definition: a game is any activity done for fun. Give me counterexamples." | owner to decide: dia-elenchus (definition) or dia-conjecture; record the choice in Step 0 |
| 13 | "Our policy says every refund is approved within 24 hours. Find counterexamples." | dia-negative (policy; negative for dia-conjecture) |
| 14 | "Here is my proof that every even perfect number ends in 6 or 8. Does it follow?" | dia-reductio (deductive step; negative for dia-conjecture) |
| 15 | "How well does my argument support the claim that all our users churn after a price rise?" | dia-conjecture or dia-warrant, owner to decide; the two descriptions currently both claim it |
```

Replace design note line 30 with: "Moving 'find counterexamples' requests from dia-brainstorm (open question 3): not done. This batch edits dia-brainstorm's description only for the dia-counterplan pointer; a dia-conjecture pointer would push it past 1,024 characters (now 1,014) and needs the owner to choose what to trim. Probes 5 and 11 measure the gap."

### 7. nit (fidelity): "monster-adjustment" is attributed to Lakatos's rejections without a cited source

Evidence: line 98, "Exception-barring … and monster-adjustment … labelled as responses Lakatos rejects". theory.md:27 cites Easwaran, whose list ("unproductive responses … that he rejects") names only monster barring and exception barring. Neither SEP Lakatos nor the cited BJPS part I discusses monster-adjustment beyond the contents line (§4d).

Append to theory.md:27:

```
Monster-adjustment (ch. 1 section 4d) is not in Easwaran's list; the skill groups it with them because, like monster-barring, it saves C by reinterpreting the case instead of improving the proof. That grouping is the skill's reading, not a quoted source.
```

### 8. nit: the worked example's check depends on an ambiguous term

Evidence: lines 71–75. C is "binary-searched in O(log n) steps", and the check says the search "takes O(n)". On a linked list binary search makes O(log n) comparisons but O(n) link walks, so whether the case is global turns on what "step" means.

Replace on line 71 "in O(log n) steps" with "in O(log n) time". Replace line 75 with:

```
> - Searched in O(log n) time? No: reaching the middle item walks n/2 links, so the search takes O(n) time, though it makes only O(log n) comparisons.
```

### 9. nit: after round three, two asks in one message

Evidence: line 104 puts the next case in the post-pick message and also "After three rounds, offer to stop in one line", so the third follow-up carries two asks (hard rule 1).

Replace "After three rounds, offer to stop in one line;" with:

```
After the third round, that message restates C and offers to stop instead of raising a case;
```

### 10. nit (AI-chat risk): two both-sides paths are not disclosed, and [T] covers only the user

Evidence:
- Line 53: for "your answer" the assistant attacks a proof it wrote, but it only says "self-examination".
- Line 94: a global-only case makes the assistant write the hidden lemma and then the repair, but [A, hidden] carries no acceptance step, unlike line 63.
- Line 61 defines [T] as "the user's words", yet Step 0 admits pasted texts and earlier answers.

Fixes:
- Line 61: "[T] the user's words" → "[T] the words of C's source (the user, the pasted text or your earlier answer; quote them)".
- Line 53, end: "…that you will not defend it, and that you are then arguing both sides."
- Line 94, after "marked [A, hidden],": "which the user accepts by picking this option,".

### 11. nit (label): §6 is only partly implemented, and "sections 7-9" mixes Rule 5 with concept-stretching

Evidence: line 14 says "ch. 1 sections 1-6 … Rule 5 and the concept-stretching analysis of sections 7-9". The CUP contents put Rule 5's deductive guessing in §7 and concept-stretching in §8–9. Of §6, only 6a ("deeper proofs") has a counterpart; 6b–c do not. theory.md:35 is already precise.

Line 14, replace "Rule 5 and the concept-stretching analysis of sections 7-9 are not implemented" with "of section 6 only its deeper-proof move (6a) is used; Rule 5 (section 7) and the concept-stretching analysis of sections 8-9 are not implemented".

### 12. nit: design-note citations point at files that do not exist

Evidence: design/dia-conjecture.md:3 and the headers at lines 33 and 47 cite `report-modern-dialectic.md` and `report-index.md`. The tree has `docs/research/candidates/review/modern-dialectic.md` and `review/index.md`.

On line 3, replace "`report-modern-dialectic.md` and `report-index.md`" with "`review/modern-dialectic.md` and `review/index.md`", and use the same paths in the two headers.

### 13. nit: Step 3's case order and the "Easy holding" pitfall point different ways

Evidence: line 69 says "Choose the case most likely to be valid, from the user's own material first, then logical or definitional cases, then facts". Line 134 says "Press the most suspect lemma first". Step 2 marks a suspect lemma (line 61), but Step 3 never uses the mark.

Line 69, replace "Choose the case most likely to be valid," with "Aim first at the lemma marked most suspect; choose the case most likely to be valid,".

## Checks 2-5: summary beyond the findings

- Logic and tool-less use (2): outside findings 1-4, 9 and 13 the flow is consistent; every step completes with no tools (recall makes C′ conditional); the worked case is 6 lines and a repair menu fits one phone screen.
- Fidelity (3): the label matches the body except findings 7 and 11; the one behavioural infidelity is finding 1 (Rule 2's ban evadable unnamed). Popper is labelled in place (line 65).
- AI-chat risks (4): yielding handled by hard rule 6 and the disputed class, weakened by finding 1; over-reliance handled (user rules and picks, one recommendation, "Advisor drift"); both-sides disclosed only for [A] lemmas (finding 10); invented premises handled by the per-case check, [A] acceptance, evidence classes and conditional C′.
- Routing (5): the exclusion sentences agree in direction (warrant, reductio and counterplan send all/always/never counterexamples here; this skill sends probable claims, Q and not-Q, and plans out). The unreciprocated borders are dia-brainstorm, dia-negative and dia-elenchus; findings 5 and 6 give the concrete requests and probe rows.
