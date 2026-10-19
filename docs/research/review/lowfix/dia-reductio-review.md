Verdict: PASS WITH FIXES

Scope: `git diff 1b3f139 b430a97 -- skills/dia-reductio` plus the reductio parts of docs/spec.md, README.md and tests/. Line numbers refer to the tree at b430a97. The implementer's report (lowfix-reports/dia-reductio.md) was checked claim by claim against the files.

Checks run (read-only)
- `python3 tools/package.py --check`: "ok" for all seven skills, exit 0.
- `python3 -m unittest discover -s tests`: "Ran 13 tests ... OK (skipped=1)", exit 0.
- `diff -r skills/dia-reductio plugins/dia/skills/dia-reductio`: identical. plugin-release.json stays 0.1.0 with a new digest, which handoff.md:7 allows before the first release.
- SKILL.md is 135 lines (limit 200). The description is 846 characters (limit 1024). A scripted scan found no Hangul and no product names; `claude` appears only as the D14 target value. No tool use was added.
- `git diff 1b3f139 b430a97 --stat -- docs README.md tests` is empty. The commit changes no spec, README, test, research README, handoff or probes file (finding 1).

Verified correct (no action)
- F8: SKILL.md:3 uses the pass-2 wording ("holds together or follows from its premises"). Step 2's "default when the user asks whether T is true" (SKILL.md:53) still reads correctly.
- F11: SKILL.md:132 says "the usual weak point", not "the fault", as the review asked. Sorites logic: each step is modus ponens on the tolerance premise, so "each step may be valid" is correct.
- F12: SKILL.md:67 replaces "stop at the first" instead of contradicting it, which was the review's objection. The two declined parts are justified: the depends-on part is covered by SKILL.md:63 and :71, and [27] concerns the order of input premises, not output numbering.
- F13: SKILL.md:59 and theory.md:26 use the review's corrected form ("does not accept in general (it does when T is itself a negation)"). Logic: from not-T ⊢ ⊥ one gets ¬¬T intuitionistically, and ¬¬¬S → ¬S is intuitionistically valid, so the exception holds. The SEP quote is verbatim: "Intuitionistically, reductio ad absurdum only proves negative statements, since ¬¬A → A does not hold in general." Declining the template line is justified, because the derivation ends at the contradiction (SKILL.md:67) and the result value carries the conclusion.
- F14: theory.md:55. *Apology* 27b–e covers the horses analogy, daimonia, "sons of gods" and the mules. Jowett has "therefore I may assume that your silence gives consent", verbatim. Dropping Madhyamaka is one of the two options F14 offered. Declining the "(Rescher presents both as looser…)" note follows the review ("mostly redundant").
- F15: theory.md:66-70.
  - (a) Joyce's IX.20 text has "If possible, let it be so … which is absurd. Therefore G is not the same with any one of the numbers": a negation-introduction sub-step inside a direct proof. Correct.
  - (b) SEP has "so large as to be unlimited" and "he apparently assumes, an infinite sum of finite parts is infinite", and it hedges ("He might have had the intuition…"). "On one reconstruction" matches; SEP's second reading (equal parts) is a different argument.
  - (c) Liar: assuming T leads to contradiction and assuming not-T leads to contradiction, which is "premise set inconsistent" by SKILL.md:56. SEP Dialetheism: "true contradictions", with paraconsistency "in tandem", not "needs". Correct.
- M5: the Step 8 field list (SKILL.md:108) matches template:47-54 one to one (8 fields).
- M6 declined: it concerns the research text and probes, and the neutral-directory re-runs (probes.md:76) have since addressed it. Justified.

Findings

1. should-fix (process/docs). The commit changes behavior with no spec or doc record.
   - Spec §5 (spec.md:110, and "amended by D19–D22" in §5.1–5.3) says the skills keep reference behavior unless D19–D22 say otherwise. This batch changes behavior: Step 4's stop rule, the `all` record, the Step 8 fallback, the description, the classical-logic note and a new pitfall. No D23 records any of it; review M4 asked for exactly this record.
   - docs/research/README.md:53 still lists "reductio F8 …, F11–F15, M5–M7" as open, and handoff.md:27 still says three batches.
   - The description changed, but probes.md:56/:76 still report reductio routing for the old description. Neither the probes file nor "Still open" notes the P7 re-run that the pass-2 review (finding 5) and the implementer both say is needed.
   - Research §8 OQ5 (keep "or true"?) and OQ7 (dialetheism disclosure) were owner questions. Both are now applied, with no recorded owner direction.
   - Add to the spec.md decision log (reductio part; the other skills' reviewers supply theirs): "| D23 | Remaining low research findings (2026-10-20; owner direction). dia-reductio: the description asks whether a position \"holds together or follows from its premises\" (P7 re-run for reductio due); Step 4 reports a contradiction that depends on fewer [A] premises when one is within reach; Step 2's note covers indirect proof in general (intuitionistically acceptable when T is a negation); Step 8 names the record fields as a template fallback; `all` gives one combined record with one entry per target; a pitfall names the tolerance premise of small-step chains; theory.md cites the *Apology* (27b–e) directly, drops Madhyamaka, and adds a hard-cases section (Euclid IX.20, Zeno, paradoxes with a one-line dialetheism note). |"
   - Change "D19–D22" to "D19–D23" at spec.md:110 and in each "Behavior: the reference, amended by D19–D22." line.
   - research/README.md:53, reductio part: replace it with "reductio: F10's second half (show the 'carried' check, see review F10) and a P7 re-run for the D23 description".

2. should-fix (intended item not applied, not declined). F10's second half is missing.
   - Research F10 proposes adding at SKILL.md:77: "Show the short derivation of not-T from the [A] and [L] premises alone, or write 'not found'". Review F10 confirms it and calls adding [L] "a quiet improvement".
   - Only the own-scheme label (SKILL.md:81) was ever applied (research/README.md:53, "F10's label is applied"). The implementer's report never mentions F10.
   - SKILL.md:77 still asserts the check without showing it.
   - Replacement for SKILL.md:77: "- **carried by added premises:** the [A] premises, with any [L] premises but without the assumption, already entail its negation (not-T when refuting, T when proving). Check this every time an [A] premise is in the set, and show that short derivation or write \"not found\". If it holds, say plainly that the reductio only restates what you assumed, so the real question is whether those [A] premises are true. Make the options and the recommendation turn on them."
   - If the owner declines this, record the decline in research/README.md instead.

3. should-fix. theory.md:69 contradicts Rule 1/Rule 2 on labels.
   - Problem: "A mathematical-sounding premise is [L] only if it is a theorem; otherwise it is [A]." This drops [T]. Under SKILL.md:33 ("[T] if the target said it, [L] only if it is a theorem of mathematics, otherwise [A]") and :34, a false mathematical claim that the target states is [T].
   - Effect: labelling it [A] would downgrade an internal result to "conditional" and invent a fake added premise.
   - Replacement: "A mathematical-sounding premise is [L] only if it is a theorem; otherwise it is [T] if the target stated it (quote it) and [A] if you supplied it, as Zeno's premise is on this reconstruction."

4. nit. theory.md:28 was not updated for the new exception.
   - Problem: "So when the skill proves T by refuting not-T, especially when T says something exists, note that the conclusion relies on classical logic." After theory.md:26 and SKILL.md:59, the proof does not rely on classical logic when T is a negation.
   - Replacement: "So when the skill proves T by refuting not-T and T is not itself a negation, note that the conclusion relies on classical logic, above all when T says something exists."

5. nit. SKILL.md:59: "from a contradiction with not-T" can be read as "T contradicts not-T".
   - Replacement: "Concluding T because not-T led to a contradiction is indirect proof, which intuitionistic logic does not accept in general (it does when T is itself a negation); say so when it matters, above all for claims that something exists (see the theory reference)."

6. nit. SKILL.md:67: "fewer [A] premises" can now clash with "Keep the chain as short as the logic allows" in the next sentence, and the text does not say which wins. The research's criterion is the [A] count.
   - Replacement for the first two sentences: "Numbered lines, each with its rule and the lines it uses. Stop at the first contradiction, unless one that depends on fewer [A] premises is also within reach; then report that one, even if its chain is longer."

7. nit. SKILL.md:119: "one entry per target on each line" also applies to History, which template:54 makes "one line per follow-up turn". A follow-up usually concerns one target.
   - Replacement: "…then give one combined record whose lines carry one entry per target (History: one line per follow-up turn, naming its target). Skip absent targets with one line."

8. nit (sources). Two small problems in theory.md.
   - theory.md:55 now cites Aristotle directly ("*Rhetoric* II.23, uses the same argument"), but theory.md:3 says the sources are listed at the end, and the Sources list has no Aristotle entry. The pointer came from IEP ("Compare Aristotle, Rhetorica 1398a12"). Add to Sources: "- Aristotle, *Rhetoric* II.23, 1398a (topic from definition: the divine is a god or the work of a god); pointed to by IEP."
   - theory.md:68 lowercases Joyce's text inside quotation marks. Use "If possible, let it be so … which is absurd", which matches SKILL.md:135 on not tidying quotes.

Summary by check
- (1) Every applied hunk uses the review's corrected form and none widens a rule beyond intent; SKILL.md:67 prefers a different contradiction rather than the same one with fewer premises, which matches the research's own wording.
- (2) Contradictions: findings 3, 4, 6 and 7. The worked example (SKILL.md:83-96) still agrees with Steps 4 and 5.
- (3) Fidelity: every new citation was checked against its source and holds; finding 8 covers attribution only.
- (4) Logic is valid (F13 exception, Liar, sorites, Euclid).
- (5) Partial: F10 (finding 2).
- (6) The declines are justified.
- (7) Both commands pass.
