# Review: docs/research/dia-reductio.md

Verdict: **SOUND WITH FIXES**

I opened every file:line cited in §1, §5 and §7; all are accurate. A re-run of `diff -r upstream/installed/reductio skills/dia-reductio` matches §5.1 exactly. Citations hold apart from the nuances in §2. Two proposed text changes would put errors into the skill if applied as written: finding 4, which gets the logic of contraries backwards, and finding 6, whose worked example breaks the skill's own Rule 3. Four more proposals conflict with existing rules (findings 2, 5, 12 and 13). The document also misses one real skill defect: the strength grades are defined only for the refute direction.

Document length: 280 lines, so it meets the 500-line limit. It contains no Hangul.

## 1. Findings in §7

**F1. "No contradiction found" is reported as consistency or independence (high). Confirmed.**
SKILL.md:57 says "these premises do not decide T". SKILL.md:93 tells the assistant to write "consistent with these premises". SKILL.md:89 has the result value "undecided by these premises". A failed search establishes none of these. The proposed wording is correct, minimal and neutral.
- One nuance: citing undecidability [19] goes further than needed. Finite propositional consistency is decidable. The real reason is that the model's search is incomplete [21].
- Severity: high is defensible. Medium would also fit, because SKILL.md:93 already makes the assistant list the directions and premise sets it tried.

**F2. [L] merges logical truths with definitions (high). Partly.**
The problem is real. With SKILL.md:34, :38 and :75 together, a definition the assistant supplied and labelled [L] can yield both the "internal" grade and the sentence "the thesis is false". The proposed text needs two fixes:
- (a) "[L] a law of logic or arithmetic" is too narrow: the skill's model reductio (theory.md:47) uses the Pythagorean theorem, which would become [A]. Use "logic or mathematics".
- (b) "A definition is [T] if the target stated or accepted it" clashes with [T]'s "(quote it)" requirement (SKILL.md:34) and with the tidied-quote pitfall (SKILL.md:115). Rule 9 also means the target cannot "accept" anything during a one-pass run. Drop "or accepted it", or require a quote of the acceptance.

**F3. theory.md misattributes "which premise goes" (medium). Partly.**
theory.md:32 over-cites IEP §5, but "says the opposite" (line 66) is too strong. §5 ("Sets of Statements that Are Collectively Inconsistent") supports half the sentence, and its conclusion, "untenable (false) in the context of this family of givens", is relative to fixed givens and compatible with "cannot all hold". IEP does not support "only" or "Logic alone does not say which member is false".
- The replacement is fine except its last clause, "this skill holds classical logic fixed and says so when that matters": SKILL.md says no such thing. Add it there or drop it. Severity: low-to-medium (a citation fix in a reference file).

**F4. Contradictories versus contraries (medium). Wrong as written.**
The concern is fair (negation errors [25]), but the proposed text, "add the premise that rules out both being false", is logically wrong. To derive Q and not-Q from contraries you need the premise that rules out both being *true*: for "All X are Y" / "No X is Y" that is "some X exists". Ruling out both being false (excluded middle) is what separates contradictories from contraries; it produces no contradiction.
- Replacement: "If the two lines are only contraries ('all X are Y' / 'no X is Y'), they conflict only given a further premise, here that some X exists. List it [L] or [A] and let the contradiction depend on it."
- Rule 1 already demands "its negation" (SKILL.md:33), so the "'All X are Y' contradicts 'some X is not Y'" example is the useful part.

**F5. A named rule per line is not a check (medium). Partly.**
The letter-substitution reread and the "Checked by" record line are reasonable, and tool use stays conditional. The closed list "Use only common rules (…)" is the problem:
- It drops the open-ended "and so on" in Rule 3 (SKILL.md:35).
- It forbids arithmetic steps (n² even → n even, theory.md:47), hypothetical syllogism and existential generalization.
- Fix: keep the list as examples, add "arithmetic", and keep "and so on".
- [22]/[23] concern whether a chain of thought reflects latent reasoning, not whether a displayed derivation is valid; [25]/[29] fit better.

**F6. No worked example (medium). Partly; the example itself must be fixed.**
The need is supported by [20] (verified in the PDF). The proposed example breaks the skill's own rules:
- Line 4, "the hotfix did not ship only after review — P2", is not P2 ("shipped without review"); it needs an unlisted meaning step with no rule. That is the hidden-premise and Rule 3 failure the skill forbids, in the one example models will copy.
- T is given a premise label ([T]), but T is the thesis, not a premise.
- "ships" (habitual) vs "shipped" (past) is a small Rule 4 shift.
- Fix: P1 "every feature that shipped was reviewed before it shipped"; P2 "the hotfix shipped and was not reviewed before it shipped". Line 3: reviewed before shipping (1, 2, modus ponens). Line 4: not reviewed before shipping (P2, simplification).
- Length is fine: 115 + ~12 lines is far below 200.

**F7. Sycophancy on disputed steps (medium). Confirmed.**
SKILL.md:105 gives no criterion for withdrawing a step. The proposed text is good. Its `claude` addition "do not soften…" mostly repeats SKILL.md:98 ("say so directly; do not defend it"); keep only "do not invent a contradiction to look self-critical". docs/research/README.md theme 2 makes this a cross-skill decision.

**F8. The description over-promises "true" (medium). Partly; downgrade to low.**
Over-routing is speculative (no negative probe exists). Removing "true" also conflicts with the body: Step 2 makes "Both" the default "when the user asks whether T is true" (SKILL.md:53), and "follows from these premises" answers that question relative to premises. Run the negative probe first; any description change also needs a new P7 run (spec L7). The proposed description is 875 characters (limit 1024).

**F9. Evidence classes lack "supplied by the user" (medium). Confirmed; low-medium.**
The gap is real, and it is inconsistent with the P8 fix (probes.md:69). However, "do not fit tool-less chats" overstates it: the skill still completes with "unverified recall". The proposed text is fine. "Single source" stays undefined next to "verified this session", which is a nit.

**F10. Label the strength grades as the owner's design (low). Confirmed.**
The Locke quote is verbatim in SEP. Adding [L] to the SKILL.md:77 check is a quiet improvement. Fix together with M1.

**F11. Vagueness (low). Partly.**
"Valid but unsound" is from SEP's supervaluationist section, not a consensus diagnosis; some theories keep tolerance and reject transitivity. The pitfall should say "the tolerance premise is the usual weak point" rather than "the fault is the tolerance premise".

**F12. Prefer the least-assumed contradiction (low). Partly.**
"If more than one contradiction is reachable, report the one with the fewest [A] premises" conflicts with "Stop at the first contradiction" (SKILL.md:67) in the same step, and the proposal does not remove that sentence. Either replace it, or say "before stopping, check whether a shorter set with fewer [A] premises gives the same contradiction". "The depends-on set lists only premises the derivation uses" is already covered by SKILL.md:63 and :71.

**F13. The classical-logic note is too narrow (low). Partly.**
I verified SEP [4]: "Intuitionistically, reductio ad absurdum only proves negative statements, since ¬¬A → A does not hold *in general*." The proposed text "intuitionistic logic rejects [it] for any T that is not itself a negation" is too strong. ¬¬A → A is intuitionistically valid for decidable or stable A, such as atomic arithmetic equations. Say "does not accept in general (it does when T is itself a negation)". §2.2 line 56 ("for every non-negative T") makes the same overstatement.

**F14. theory.md source fixes (low). Confirmed.**
IEP never names the *Apology* ("the exchange between Socrates and his accusers … Compare Aristotle, Rhetorica 1398a12"); Madhyamaka rests on Wikipedia only; the will and Kant cases sit under IEP's "More loosely … anomaly" paragraph. Add a Stephanus reference (*Apology* 27b–e for the daimonia step). The "(Rescher presents both as looser…)" note is mostly redundant with theory.md:43.

**F15. "Hard cases" section (low). Confirmed.**
Joyce IX.20 and the Hardy–Woodgold acknowledgment ("the fact that Euclid's proof was not by contradiction") are verbatim. SEP's Zeno account is hedged ("He might have had the intuition…"), so word (b) as a reconstruction.

## 2. Citations

I fetched [1]–[31]. All URLs resolve; the Springer page [12] is paywalled, but its acknowledgments are visible. Every quote supporting F1–F9, §2 and §4 is verbatim in its source (IEP, EoM, SEP entries, Quine, Jowett, Joyce, and the [20]–[31] abstracts; the [20] quote is in the PDF body). No dead links, no misattributed quotes.

Problems, all minor:
- [1], §2.4 / A12: "says the opposite" overstates the source (see F3).
- [5], §2.6: dialetheism "needs a paraconsistent logic". SEP says only that paraconsistency is "a standard solution".
- [17], F11: the "valid but unsound" diagnosis belongs to supervaluationism, not to all views.
- [4], F13 / §2.2: "does not hold in general" became "for every non-negative T".
- [10] / [13], A10: Zeno's for-argument's-sake method and Locke's ad hominem are about arguing from the opponent's commitments, not about charitable interpretation. They do not source Rule 5.
- [18]: Jowett's own introduction calls the Meletus arguments "sophisms" and asks whether Socrates "is serious or jesting". One premise is obtained by "your silence gives consent". That weakens the *Apology* as a model strict reductio. Neither the document nor theory.md:55 mentions it.
- [22] / [23], F5: these show unfaithful chains of thought, not invalid displayed derivations (see F5).

## 3. Fidelity audit (§4) — verdicts I disagree with

- **A5 "departs" → unsupported (owner's design, with a real risk).** No source defines [L], so nothing is contradicted. IEP §6 ("Absurd Definitions and Specifications": bird/ostrich, "zor") treats definitions as *targets* of reductio, not as fixed truths. That supports the document's concern, and the document does not cite it.
- **A12 "departs (misattribution)" → loose (over-cited).** See F3.
- **A15 "departs by design" → matches the logical tradition.** IEP's central examples are monological proofs (incommensurability, division by zero, Aristotle's syllogistic completions); only the Socratic and Zenonian cases are dialogical. A1 already says the skill follows the logicians' sense.
- **B1 "departs" → unsupported/overclaim.** It misreports no source; it is an epistemic overclaim. The substance is right (F1), but the label is wrong under the document's own definitions (line 108).
- **A8 "matches" → loose.** IEP's point is about step probabilities. Moving causal links into premises is the skill's regimentation, not IEP's.

## 4. Missed issues

**M1 (should-fix). The strength grades and template are written only for the refute direction.**
SKILL.md:75 ("the set is only T plus [T] and [L] premises. The target contradicts itself"), SKILL.md:77 ("the [A] premises, without T, already entail not-T") and output-template.md:31 assume the refute direction. In the prove direction (SKILL.md:52) the assumption is not-T: an "internal" result means the target's premises entail T, which is not a self-contradiction, and the "carried" test must read "without not-T, already entail T". Literal application mis-grades every prove-direction run.

**M2 (should-fix). "Both" yields two contradictions, but Step 5, the strength grade and the record each hold one.**
See SKILL.md:69-77 and output-template.md:29-31, :49. For the "premise set inconsistent" case (SKILL.md:56), the text does not say which strength and depends-on set to record.

**M3 (should-fix, cross-skill). `agents/openai.yaml:4` default_prompt uses `$dia-reductio`.**
P3 showed that this does not resolve on the Codex plugin route; only `$dia:dia-reductio` does (probes.md:32-34). §6.3 covers cross-surface risk but omits this, although docs/research/README.md theme 1 lists it for other skills.

**M4 (should-fix, process). Most proposals change behaviour, and spec §5 says all skills "keep their reference behavior unless this section says otherwise".**
§5.1 of the document even cites this rule. Adopting F1, F2, F4–F13 needs a §5.4 amendment or decision-log entry, as well as the version bump in open question 8.

**M5 (nit). Unconditional reference reading and no fallback.**
SKILL.md:16 says "read it before writing the first output" unconditionally, and the record fields live only in the template. §6.2 notes that the record can drift (probes.md:77) but makes no proposal. A one-line fallback naming the record fields in SKILL.md would cover it.

**M6 (nit). Confounded probe evidence.**
§5.3 and §6.3 rely on the P7 Korean replies and call the P8 Korean reply "cause unknown". The probes ran at the repo root, where CLAUDE.md imports AGENTS.md ("reply in Korean"). docs/research/README.md theme 6 flags this; this document does not.

**M7 (nit). `--target=all` asks for "one combined record" (SKILL.md:100), but the template has no combined form.**
