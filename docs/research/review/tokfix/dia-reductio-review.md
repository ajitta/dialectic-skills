Verdict: PASS WITH FIXES

Scope: `git diff d135f8e 75d7ac1 -- skills/dia-reductio` plus D24 and §5 in `docs/spec.md`. All files read in full after the change. Old text taken from `git show d135f8e:<path>`.

Checks run in the tree (read-only):
- `python3 tools/package.py --check`: "ok" for all seven skills, exit 0 (so plugins/ matches skills/).
- `python3 -m unittest discover -s tests`: "Ran 13 tests ... OK (skipped=1)".
- SKILL.md is 133 lines (limit 200). No Hangul in skills/dia-reductio. LF endings.
- cl100k recount (tiktoken in a scratch venv): SKILL.md body 2,882 -> 2,819, whole file 3,136 -> 3,073, template 623 -> 593, theory 2,034 -> 1,877. The two added lines are 25 and 21 tokens. The implementer's numbers match.

Recommended-set coverage (check 5): S1, S2+S8, S3, S4, S5, S6, S7, O1, O2, T1 and T2 are all applied with the audit's proposed text. Nothing marked "keep" was touched: own-scheme label L81 (D22), independence non-claim L57, intuitionistic note L59 (D23), worked example, Step 8 field list, Rule 1 example and parenthetical, pitfalls, "Checked by" clause, the theory history and Apology passage, dialetheism line, and Sources. No D19-D23 label was lost or weakened. The only unapproved changes are the two additions in finding 1.

Findings

1. should-fix: items outside the approved set (check 5). Files: skills/dia-reductio/SKILL.md:47 and :63, docs/spec.md:69.
   Two sentences were added to the body. The audit lists them in §5 under "Gaps found during the audit (not savings; for the owner)". They are not in the §4 recommended set, and the owner approved only that set:
   - L47 (Step 1): "If the user only explores consequences, call it *per impossibile* reasoning and claim no refutation."
   - L63 (Step 3): "For a rule or practice, list its stated aim or another stated rule as a premise; its generalized application must contradict that."
   The account calls these "Owner-approved moves" (dia-reductio-applied.md:20). No owner ruling for them exists in docs/ (grep of handoff.md, research/README.md and spec.md finds nothing). D24 records them under the heading "recommended set". D24 also says "moves", but theory.md §4 L43 and §6 L51 are unchanged, so the text was copied, not moved. These lines put back 46 tokens, which cuts the net body saving from 109 to 63.
   Fix (default): revert both sentences to the d135f8e text.
   - L47: `State the target and the thesis T in one sentence, with a quote. If the input contains several claims, pick the one the rest depend on and list the others in one line as not tested.`
   - L63: `Number them P1, P2, … with labels [T], [L], [A]. A key term's meaning that the derivation relies on is a premise too: [T] if the target stated it (quote it), otherwise [A]. Keep the list to what the derivation uses.`
   - In D24, delete the sentence `dia-reductio moves its two theory-only instructions (rules or practices; *per impossibile*) into the body.`
   If the owner confirms the additions instead, keep them, apply finding 2, and change the D24 sentence to: `dia-reductio adds one-line rules for rules or practices and for *per impossibile* reasoning to the body, from theory.md §4 and §6 (owner ruling, outside the recommended set; theory.md keeps its text).`

2. should-fix (only if finding 1's additions are kept): the *per impossibile* label is now too broad (check 4, fidelity). File: SKILL.md:47.
   IEP §7 (fetched today) defines per impossibile reasoning by an impossible antecedent: "literally impossible suppositions that are not just dramatically but necessarily false", supposed "not in order to refute it as absurd ... but ... to indicate its 'natural' consequences". theory.md:51 keeps that condition ("Both start from a supposition that conflicts with known facts"). The body line drops it. As written, any request to "explore consequences" of an ordinary plan or claim would be labelled per impossibile. That is the loose method label that D19-D23 removed elsewhere. The line also does not say which of the five Step 8 results applies, and none fits a run that claims no refutation.
   Replacement for the added sentence: `If the user supposes something known to be impossible only to see what follows from it, not to test it, call it *per impossibile* reasoning, claim no refutation, and give the result as **stopped**.`

3. should-fix: a dangling pronoun weakens Rule 6, the over-claiming guard (checks 1 and 2). File: SKILL.md:38.
   The old Rule 6 read: "A contradiction shows only that the thesis and the premises cannot all be true together. Write "the thesis is false" (when proving, "the thesis follows") only when every other premise it depends on is [L]." In that version, "it" referred to "A contradiction". S4 cut that first sentence, so now "it" has no antecedent. The closest noun is "the thesis", which gives a different and wrong condition: premises the thesis depends on, instead of premises the contradiction depends on. This is the D19/D21 rule that stops over-claiming, so it should not be left ambiguous.
   Replacement for L38: `6. **Logic shows inconsistency, not which member is false.** Write "the thesis is false" (when proving, "the thesis follows") only when every other premise the contradiction depends on is [L]. Otherwise present the choice.`

4. nit: an unqualified cross-file rule number. File: references/output-template.md:3.
   The line reads "Translate headings and labels per Rule 8." The template has no rules of its own. theory.md:17 uses the qualified form "SKILL.md Rule 1". Content is not lost: Rule 8 does cover quotes in the original language and the fixed values, and SKILL.md is always in context when the template is read.
   Replacement: `Translate headings and labels per SKILL.md Rule 8. Use numbered lines, not wide tables, so it reads on a phone.`

5. nit: the lines shared with dia-negative have drifted. Files: skills/dia-negative/SKILL.md:16 and :107, compared with skills/dia-reductio/SKILL.md:16.
   The audit (§5, "Duplication shared with dia-negative") asked that S7 and S8 be decided for both skills together. S7 was cut in both. S8 was cut only here: dia-negative still has "- **The user asks about the method:** answer from the theory reference, briefly." and markdown links. The implementer disclosed this (applied.md:62). It changes no dia-reductio behavior. Record it as an open item for whoever applies dia-negative, or apply the same S2+S8 pair there.

Verified with no finding

- S1: still required by Rules 6-7, Steps 6-7 and the worked example's "Options:" line.
- S2+S8: same paths. "(then answer briefly)" in L16 keeps both the read condition and the brevity instruction. The no-reference fallback for method questions is unchanged (there was none before either).
- S3: kept as Pitfall L131. S6: no text relies on "strongest". S7: no instruction lost.
- S5: L71 "mark each [A] member". The format is still in the worked example (L96) and template (L30).
- O2: kept by template L27 ("its own contradiction and strength below"), L48-49 ("one per direction when both") and SKILL.md L79.
- T1: all six failure modes are in the body (Rules 1, 2, 4, 5, 6 and Pitfalls L128-132). No file cites theory §8 or §9 by number (grep). The renumbering is clean.
- T2: SKILL.md Rule 1 (L33) does state how a falsehood or implausibility becomes usable, so the pointer is correct. Only a reader-facing rationale clause was lost.
- No citation moved or changed in this diff. theory.md's IEP claims for §4 (Rescher's application list, the will example, Kant) and §6 (the finite-primes per impossibile example) still match the IEP text.
- Check 3: nothing that a first turn or a no-reference run needs was moved into references. All fallbacks the audit listed stay in the body.
