# Research: dia-reductio (strict reductio ad absurdum in one pass)

| | |
|---|---|
| Skill | `skills/dia-reductio/` (SKILL.md 115 lines, `references/theory.md` 70, `references/output-template.md` 52, `agents/openai.yaml` 7) |
| Upstream | `upstream/installed/reductio/` (installed copy, unversioned) |
| Spec | `docs/spec.md` §5.4, §6, §7 |
| Status | Research only. Every change below is a proposal; nothing in `skills/` was edited. |
| Date | 2026-10-20 |

Citations `[n]` refer to the Sources block at the end. File references are `path:line`. Claims marked `[unverified]` could not be tied to a fetched source.

## 1. Scope and summary of the skill

### 1.1 What the skill promises

The description (`SKILL.md:3`) promises a one-pass strict reductio: state the thesis, list every premise with its source, derive "Q and not-Q" line by line, lay out which premises could be given up, recommend one, leave the decision to the user, end with a record. It is triggered by "reductio, proof by contradiction, indirect proof, 'assume it's true and show where it breaks', 'find the contradiction'", and also when the user "wants to know whether a position is consistent or true". Implicit invocation is allowed (`agents/openai.yaml:7`, spec §7.3).

### 1.2 Rules and procedure, as written

| Element | Where | Content |
|---|---|---|
| `--target` | `SKILL.md:18-29` | `user`, `claude` (the assistant's own earlier answer, on every surface), `text`, `all`; inferred if absent and stated in the first output line |
| Rule 1 strict contradiction | `SKILL.md:33` | Only Q and not-Q counts; a false or implausible consequence counts only after its negation is written into the premise list |
| Rule 2 no hidden premises | `SKILL.md:34` | Labels [T] stated by the target (quoted), [L] logical or definitional truth, [A] added by the assistant, with a one-line reason and an evidence class (verified this session / single source / unverified recall) |
| Rule 3 named rule per line | `SKILL.md:35` | Each line cites lines and a rule; empirical or causal claims are never steps, only premises |
| Rule 4 one sense per term | `SKILL.md:36` | Equivocation is reported, not used |
| Rule 5 charity | `SKILL.md:37` | Test the strongest reasonable reading |
| Rule 6 inconsistency, not falsity | `SKILL.md:38` | "The thesis is false" only when every other premise is [L] |
| Rule 7 user decides | `SKILL.md:39` | Recommend one option and stop |
| Rule 8 language | `SKILL.md:40` | Output in the user's language; quotes in the original |
| Rule 9 one response | `SKILL.md:41` | The whole chain at once, no premise-by-premise questioning |
| Step 2 direction | `SKILL.md:49-59` | Refute (assume T), prove (assume not-T), or both, with a four-way reading of the pair; classical-logic caveat for existence claims |
| Step 5 strength | `SKILL.md:69-77` | internal / conditional / carried by added premises |
| Steps 6-8 | `SKILL.md:79-89` | Options (incl. a narrowed T′), recommendation with weakest premise and a changing observation, record with one of five results |
| No contradiction | `SKILL.md:91-93` | "consistent with these premises, which does not show it is true" |
| Follow-ups | `SKILL.md:102-107` | Rerun on a picked option; check disputed steps; drop rejected [A] premises |
| Pitfalls | `SKILL.md:109-115` | Loose absurdity, slippery slope, strawman, "not found = true", tidied quotes |

`references/theory.md` gives Rescher's three kinds of reductio (`theory.md:9-17`), the logical form and the classical/intuitionistic split (`theory.md:19-28`), "which premise goes" (`theory.md:30-32`), targets of reductio (`theory.md:34-43`), the incommensurability proof (`theory.md:45-47`), per impossibile reasoning (`theory.md:49-51`), history (`theory.md:53-55`), and failure modes (`theory.md:57-64`). It cites the IEP entry, the Encyclopedia of Mathematics and Wikipedia (`theory.md:66-70`).

`references/output-template.md` is a phone-friendly numbered layout (`output-template.md:3`) with sections Thesis, Premises, Derivation (one or two), Contradiction with strength, Options, Recommendation, Record (`output-template.md:7-52`).

## 2. The method in its primary and reference sources

### 2.1 Name and the three senses

Rescher's IEP entry traces the Latin name to Aristotle's Greek *hê eis to adunaton apagôgê*, "reduction to the impossible", used repeatedly in the *Prior Analytics* [1]. In its general sense reductio refutes something because "absurd – and patently untenable consequences would ensue", and the untenable consequence can be a self-contradiction (*ad absurdum*), a falsehood (*ad falsum*), or an implausibility or anomaly (*ad ridiculum*, *ad incommodum*) [1]. The first is "reductio ad absurdum in its strictest construction"; the other two are "a rather wider and looser sense", and "logicians and mathematicians generally have the first and strongest of them in view" [1]. The skill's choice of the strict sense (`SKILL.md:33`, `theory.md:17`) is thus the logicians' sense, not an idiosyncratic restriction.

### 2.2 Logical form: negation introduction versus indirect proof

Rescher gives the propositional core as "If p ⊢ ~p, then ⊢ ~p", derived from contraposition, the law of contradiction and modus ponens, and describes the general pattern as (to-be-refuted assumption + preestablished facts) ⊢ contradiction, followed by modus tollens [1]. The Encyclopedia of Mathematics states the rule as: if Γ and A imply both B and ¬B, then Γ implies ¬A; it is "sound in the majority of logico-mathematical calculi" [2]. The same entry adds that the informal name also covers the converse pattern (Γ with ¬A implies a contradiction, so Γ implies A), which is equivalent classically "but it is not a sound rule of inference in intuitionistic logic" [2].

The SEP entry on intuitionistic logic puts the point generally: "Intuitionistically, reductio ad absurdum only proves negative statements, since ¬¬A → A does not hold in general" [4]. In natural deduction, Gentzen's rule for indirect proofs first derives ⊥ from the two halves of a contradiction and then the negation of the assumption, and Jaśkowski's Reductio rule "deletes a negation sign from the assumption", which is "Jaśkowski's way to move from intuitionistic logic to classical logic" [3]. Classical natural deduction is usually built by adding one "classicizing" rule, for example indirect proof, to an intuitionistic system [3]. The intuitionistic system replaces double negation elimination with ex falso (INE) [4].

Consequence for the skill: the refute direction (assume T, derive ⊥, conclude not-T) is negation introduction and is valid intuitionistically; the prove direction (assume not-T, conclude T) uses a classical rule for every non-negative T, not only for existence claims. IEP illustrates the intuitionist objection with existence: one cannot establish (∃x)Fx by deducing an absurdity from (∀x)¬Fx [1]. The skill's caveat (`SKILL.md:59`, `theory.md:26-28`) is correct for existence and narrower than the SEP statement.

### 2.3 Aristotle: "through the impossible"

The SEP entry on Aristotle's logic says Aristotle's imperfect deductions are completed either directly or "through the impossible" (*dia to adunaton*): assume the denial of the conclusion and deduce, with one original premise, "the denial (or the contrary) of the other premises" [16]. Aristotle's own procedure therefore accepts a contrary as well as a contradictory as the impossible result. The SEP entry on contradiction explains the difference: contradictories cannot both be true and cannot both be false, while contraries ("Every man is just" / "No man is just") cannot both be true but can both be false [15]. A strict "Q and not-Q" requirement is stricter than Aristotle; a contrary becomes a strict contradiction only with an explicit exclusion premise.

### 2.4 Which premise goes

Logic shows only that a set is inconsistent. This is the Duhem-Quine point. The SEP entry on underdetermination reports Duhem's conclusion that "no experiment ever tells us precisely which belief it is that we must revise or give up as mistaken" [7]. Quine generalises it: "there is much latitude of choice as to what statements to re-evaluate in the light of any single contrary experience", and "Any statement can be held true come what may, if we make drastic enough adjustments elsewhere in the system", including "amending certain statements of the kind called logical laws"; "no statement is immune to revision" [8]. Quine names the criteria: "Conservatism figures in such choices, and so does the quest for simplicity" [8]. Formal belief revision makes the choice a ranking: an agent "should give up beliefs that have as little explanatory power and overall informational value as possible", which is Gärdenfors's epistemic entrenchment [9].

The skill's Rule 6 and Steps 6-7 (`SKILL.md:38`, `SKILL.md:79-85`) match this tradition well. Two details differ. First, `theory.md:32` cites the IEP section "Doctrinal annihilation" for the claim that logic does not say which member is false, but that section says the opposite in its example: after A is added to A→B, B→C, C→D, not-D, "the supposition that A can be refuted … Hence it is untenable (false) in the context of this family of givens" [1]. Rescher treats the background as fixed and the supposition as the refuted member; the "which member goes" point comes from Duhem and Quine [7][8], not from Rescher. Rescher's phrase "untenable … in the context of this family of givens" does match the skill's result label "untenable on these premises" (`SKILL.md:89`). Second, Rule 6 treats [L] premises as fixed; Quine explicitly does not [8], and intuitionists and dialetheists revise logic itself (§2.6).

### 2.5 Loose reductio, slippery slopes, vagueness

The SEP entry on fallacies describes the slippery slope as reaching an undesirable conclusion by "a series of incremental inferences", which can be causal or can depend on vague terms, as in "the beard" and "the heap" [13]. The IEP fallacies entry says the form "occurs in both good arguments and faulty arguments" and that its quality "depends crucially on the strength of the probabilities in going from one step to the next" [14]. The skill handles the causal variant (`SKILL.md:112`, `theory.md:63`) by forcing each causal link into the premise list. It does not handle the vague variant. The SEP sorites entry presents the paradox "most simply using modus ponens" and notes that classically valid sorites forms are diagnosed as "valid but unsound" because a tolerance premise fails [17]. A sorites chain therefore passes Rules 1 and 3 (every line is modus ponens, the end is Q and not-Q), and Rule 4 (one sense per term) does not catch it, because the term does not shift meaning; it is vague.

### 2.6 Paradox, paraconsistency, dialetheism

Dialetheism is "the view that some contradictions are true"; it is distinct from trivialism and needs a paraconsistent logic, one in which a contradiction does not entail everything [5]. Paraconsistency does not imply dialetheism [6]. The main motivation is the paradoxes of self-reference such as the Liar, where "there appears to be a perfectly sound argument ending in a contradiction" [5]. For a dialetheist, deriving a contradiction does not automatically refute the assumption; that is the one tradition in which a strict reductio is not decisive. Most users will hold classical logic, so this is a caveat for paradox inputs, not a reason to change the method. The skill has no paradox handling; for a Liar-type input, its "premise set inconsistent" result (`SKILL.md:56`) is the right classical reading, but the theory reference does not say so.

### 2.7 Classical examples

- **Incommensurability of the diagonal.** IEP gives the d² = 2s² proof, ending in m and n both even "contrary to the hypothesis that they do not", as the classic indirect proof [1]. `theory.md:47` reproduces it accurately.
- **Euclid IX.20 (infinitude of primes).** Joyce's translation shows a direct construction (take the least number measured by A, B, C and add one) with one local reductio inside: "If possible, let it be so … which is absurd. Therefore G is not the same with any one of the numbers A, B, and C" [11]. Hardy and Woodgold document how often the proof is misdescribed as a proof by contradiction, and thank Niesen for pointing out "the fact that Euclid's proof was not by contradiction" [12]. This is a useful caution for the skill: a chain can contain a negation-introduction sub-step without being an indirect proof overall. `theory.md:51` uses the primes only for per impossibile reasoning, which IEP supports [1].
- **Zeno.** SEP describes Zeno's arguments as supposing his opponents' assertions "for argument's sake" and deriving absurd consequences: "they are 'reductio ad absurdum' arguments (or 'dialectic' in the sense of the period)" [10]. The plurality argument rests on a hidden mathematical assumption, and "Zeno has not proven that the absurd conclusion follows" because "some infinite sums are after all finite" [10]. A famous reductio failed at a premise that would have looked like an [L] truth to its author.
- **Socrates and Meletus.** IEP cites the exchange between Socrates and his accusers, comparing Aristotle's *Rhetoric* [1], but does not name the *Apology*. The primary text does: Socrates gets Meletus to agree that spirits or demigods are "either gods or the sons of gods", then concludes that the charge makes him both disbelieve and believe in gods [18]. The contradiction depends on a definitional premise extracted from the opponent, which bears on how the skill labels definitions (finding 2).

### 2.8 Dialectical lineage: arguing from the opponent's concessions

The SEP fallacies entry quotes Locke's original *argumentum ad hominem*: "to press a man with consequences drawn from his own principles or concessions", that is, to show an opponent's view is inconsistent with other things he is committed to; Locke held that this "is not a fallacy but an acceptable mode of argumentation", though it serves agreement rather than truth [13]. This is the closest classical analogue to the skill's "internal" strength grade (`SKILL.md:75`). The same entry treats begging the question as an epistemic fallacy, including the version "where there are unsettled questions about key terms" [13]; this is the analogue of "carried by added premises" (`SKILL.md:77`) and of a contested definition labelled [L].

## 3. Relevant research on how language models do this

| Finding | Source | Bearing on the skill |
|---|---|---|
| GPT-3.5, PaLM, LLaMA and FLAN-T5 could not use proof by contradiction (or proof by cases) without explicit demonstrations, "suggesting that pretraining is not sufficient to teach the model to generate hypothetical subproofs" | [20] | The skill gives no worked derivation in SKILL.md; the only example is prose in `theory.md:47` |
| Models make correct single deduction steps but "have difficulty with proof planning" when several valid steps are available | [21] | Failing to find a contradiction is weak evidence that none exists; the first contradiction found may not be the best one |
| Chain-of-thought explanations "can systematically misrepresent the true reason for a model's prediction"; biased models "frequently generate CoT explanations rationalizing those answers" | [22] | A line labelled "modus ponens" can be a rationalization of a conclusion reached otherwise |
| "As models become larger and more capable, they produce less faithful reasoning on most tasks we study" | [23] | Named rules are a display for the user to check, not evidence that the model reasoned that way |
| Expert-written first-order logic problems: "a subset of FOLIO presents a challenge for" GPT-4 | [24] | Natural-language premises with quantifiers are still error-prone |
| LLMs "struggle with instances involving complex reasoning and negations" and "sometimes overlook contextual information" across 25 inference patterns | [25] | The decisive step of a reductio is a negation; negating "all" or "only" wrongly yields a contrary, not a contradictory |
| LLMs "achieve very limited performance" on abstract reasoning beyond memorization | [26] | Same direction, different task family |
| Permuting premise order "can cause a performance drop of over 30%" | [27] | Order the premise list as the derivation uses it |
| "LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades" | [28] | `--target=claude` self-examination is not independent; the skill already says so (`SKILL.md:98`) |
| LLMs "could struggle to identify fallacious reasoning steps accurately" | [29] | The model checking its own chain for equivocation or hidden premises is weak |
| Sycophancy is "a general behavior of state-of-the-art AI assistants" | [30] | Risk when the user disputes a step (`SKILL.md:105`) or defends their thesis |
| Like humans, models "answer more accurately when the semantic content of a task supports the logical inferences" | [31] | Belief bias: a valid chain to an implausible conclusion, or an invalid chain to a plausible one, is judged by content |

All of these studies predate the models the skill now runs on, so their size on current Claude and GPT models is [unverified]. The direction of each effect is what matters for skill design: rules that make each step checkable by the user, short chains, and an explicit statement that no machine check took place.

## 4. Fidelity audit

Verdicts: **matches** (agrees with the source), **loose** (borrows the idea with a change), **departs** (contradicts or misreports the source), **unsupported** (the owner's design; no source claims it).

| # | Skill rule or claim | What the sources say | Verdict |
|---|---|---|---|
| A1 | Strict contradiction only (`SKILL.md:33`, `theory.md:17`) | Rescher: strict sense is the first of three; logicians mean it [1]; EoM rule is B and ¬B [2] | matches |
| A2 | A falsehood is usable once its negation is a listed premise (`SKILL.md:33`) | Regimenting *ad falsum* into strict form; Rescher calls *ad falsum* attenuated [1] | loose (sound regimentation, the owner's) |
| A3 | Q and not-Q only, no contraries (`SKILL.md:33`) | Aristotle accepts "the denial (or the contrary)" [16]; contraries can both be false [15] | loose (stricter than Aristotle; the skill does not say how to handle a contrary) |
| A4 | Labels [T]/[L]/[A] (`SKILL.md:34`) | Natural deduction tracks which assumptions a line depends on (Suppes-style numbering) [3]; no source has these three labels | unsupported (sound design) |
| A5 | [L] = "logical or definitional truth" (`SKILL.md:34`) | Begging the question can sit in "unsettled questions about key terms" [13]; Socrates' definitional premise was conceded by Meletus [18]; Quine rejects a sharp analytic/synthetic line [8] | departs (merges a contestable category into the fixed one) |
| A6 | Evidence classes (`SKILL.md:34`) | None | unsupported (owner's; lacks a "user-supplied" class) |
| A7 | Every line names its rule (`SKILL.md:35`) | Gentzen, Jaśkowski, Fitch, Suppes annotate rule and lines [3] | matches (as a format); faithfulness not guaranteed [22][23] |
| A8 | Empirical or causal claims are premises, never steps (`SKILL.md:35`) | Slippery-slope quality turns on step probabilities [14] | matches |
| A9 | One sense per term (`SKILL.md:36`) | Equivocation is a classical fallacy [13]; vagueness is a different problem [17] | matches for equivocation; gap for vagueness |
| A10 | Charity (`SKILL.md:37`) | Zeno's arguments are aimed at the opponents' own views [10]; Locke's ad hominem uses the opponent's concessions [13]; theory.md cites nothing | loose (standard norm, unsourced in theory.md) |
| A11 | Inconsistency, not falsity (`SKILL.md:38`) | Duhem and Quine [7][8]; belief revision [9] | matches the tradition |
| A12 | theory.md attributes A11 to IEP §5 (`theory.md:32`) | IEP §5 says A is "untenable (false) in the context of this family of givens" [1] | departs (misattribution) |
| A13 | "Thesis is false" only if every other premise is [L] (`SKILL.md:38`) | Quine: logical laws are revisable [8]; intuitionist and dialetheist revisions [4][5] | loose (fine under classical logic held fixed; should say so) |
| A14 | Recommend one, user decides (`SKILL.md:39`, `SKILL.md:83-85`) | Entrenchment orders what to give up [9]; Quine's conservatism and simplicity [8] | loose (the "weakest premise" test is an informal entrenchment) |
| A15 | Whole chain in one response (`SKILL.md:41`) | Historical reductio is dialectical: concessions extracted in turn [18][10] | departs by design (monological; dialogue is dia-elenchus's job) |
| A16 | Refute valid in both logics; prove only classical (`theory.md:25-26`) | [2][4] | matches |
| A17 | Classical caveat only for existence claims (`SKILL.md:59`, `theory.md:26-28`) | Intuitionistically reductio proves only negative statements [4]; IEP's example is existence [1] | loose (narrower than the general point) |
| A18 | Four-way reading of "both" (`SKILL.md:53-57`) | Both-contradict implies the premises are inconsistent (an elementary consequence of negation introduction, valid intuitionistically too; this report's own derivation) | matches for three cases; the "neither" case overclaims (B1) |
| B1 | "neither does → these premises do not decide T" (`SKILL.md:57`) and "consistent with these premises" (`SKILL.md:93`) | There is no decision method for first-order provability [19]; models are weak at proof search [21] | departs (failure to find is reported as independence and consistency) |
| B2 | Strength grades (`SKILL.md:73-77`) | No source grades reductio this way; "internal" ≈ Locke's ex concessis argument [13]; "carried by added premises" ≈ begging the question [13] | unsupported (useful owner design; should be labelled as such) |
| B3 | "Stop at the first contradiction" (`SKILL.md:67`) | Greedy proof search [21] | loose (may report a contradiction that needs more [A] premises than necessary) |
| B4 | Reductio applies to rules and practices (`theory.md:34-43`) | Rescher's list [1]; but the will and Kant cases are his "more loosely" / "anomalous" cases [1] | matches the list; slightly overstates the strictness of the examples |
| B5 | Per impossibile distinction (`theory.md:49-51`) | IEP §7: same format, "pragmatic difference in objectives" [1] | matches |
| B6 | History (`theory.md:55`) | Republic, Parmenides, Kant: IEP [1]; Apology: IEP does not name it, primary text does [18]; Madhyamaka: Wikipedia only | matches content; attribution loose; Madhyamaka weakly sourced |
| B7 | Incommensurability example (`theory.md:47`) | IEP §3 [1] | matches |

## 5. Lineage: upstream to dia

### 5.1 What changed

`diff` of `upstream/installed/reductio/` against `skills/dia-reductio/` shows only these changes:

- `name` `reductio` → `dia-reductio`; frontmatter gains `license: MIT` and `metadata` (`SKILL.md:4-9`), per spec §7.2.
- Description: Hangul trigger terms (the Korean words for reductio and reductio argument, twice) removed; "in any language" became "or the same in any language"; "Claude's own earlier answer" became "the assistant's own earlier answer"; cross-references now name `dia-negative` and `dia-elenchus` (spec §5.4, D14).
- `--target=claude` row: "Claude's own earlier answer" → "your own earlier answer …; the value is `claude` on every assistant" (`SKILL.md:25`).
- Rule 2 and Step 5: "added by Claude" / "what Claude assumed" → "added by you" / "what you assumed" (`SKILL.md:34`, `SKILL.md:77`); Targets: "Claude's earlier answer" → "your earlier answer" (`SKILL.md:98`).
- `theory.md:60`: "something … Claude did not list" → "something … the premise list did not include".
- `output-template.md:1`: title rename.
- New `agents/openai.yaml` with `allow_implicit_invocation: true` (spec §7.3).

No rule, step, grade, result value or pitfall was added, removed or reworded beyond the product-name substitutions. Behaviour is the same as the reference, as spec §5.4 requires.

### 5.2 Design notes

`upstream/superclaude-stable-47f791b/docs-features/` holds design notes for socratic-brainstorm, socratic-elenchus and the portable plugin only; a search finds no design or research note for reductio. The rationale for the strength grades, the evidence classes and the [T]/[L]/[A] labels is not recorded anywhere in the repository. The only stated rationale is `theory.md` itself. The upstream negative-dialectics theory note draws the boundary from the other side: reductio shows a set of statements is inconsistent, negative dialectics shows concept and thing do not fit (`upstream/installed/negative-dialectics/references/theory.md:45`). The dia descriptions keep that split.

### 5.3 Anything lost

- The Hangul triggers. P7 found no routing drop at n=2 in Claude Code (`docs/probes.md:45-56`). Codex and ChatGPT routing in Korean is untested.
- The "Claude did not list" wording in `theory.md:60` named the agent responsible for a hidden premise; the new wording is neutral and loses nothing important.
- Nothing else. The rebuild preserved the reference's defects too (findings 1-3).

## 6. Risks and failure modes

### 6.1 On language models generally

1. **Manufactured contradictions.** Asked to "find the contradiction", a model under instruction pressure may produce one. The skill guards against this (`SKILL.md:93`), but the result vocabulary has no honest outcome for "I searched and found nothing" that does not claim consistency or independence (B1).
2. **Rationalized derivations.** Rule labels can be attached after the fact [22][23]. A line like "4. not-Q — from 2, P3, modus tollens" looks checked whether or not it is.
3. **Negation errors.** Negating "all X are Y" as "no X is Y" produces a contrary; the "contradiction" then depends on an unstated existence or exclusion premise [15][25].
4. **Definitional smuggling.** An assistant-supplied definition labelled [L] lets the skill grade a contradiction "internal" and even write "the thesis is false" (Rule 6) while the real disagreement is over the definition [13].
5. **Belief bias.** Content effects [31] make it more likely that the model accepts invalid steps toward a conclusion it already finds plausible, and misses a contradiction in a thesis it likes.
6. **Greedy search.** The first contradiction found may depend on more [A] premises than another available one [21]; Step 4 stops there.
7. **Self-examination and pushback.** With `--target=claude`, the model checks its own answer without external feedback [28]; when the user disputes a step, sycophancy pulls toward withdrawal [30]. Step "check it" (`SKILL.md:105`) gives no criterion for when an objection "holds".
8. **Vague predicates.** Sorites-style chains pass every formal rule [17].

### 6.2 Tool-less and mobile surfaces

- The method needs no tools; it is pure derivation, so it is well suited to G2. The only tool-dependent part is the evidence class "verified this session". On a tool-less chat, an [A] fact can only be "unverified recall" unless the user supplied it, and there is no class for user-supplied material. dia-refine's P8 fix lists "the user's instructions or supplied material" as a confirmed basis (`docs/probes.md:67-71`); dia-reductio is inconsistent with that.
- Nothing checks the derivation mechanically on any surface. With a code tool the model could run a small truth-table or SAT check for propositional chains; the skill never mentions it, which is consistent with spec §7.1 (tool use only conditional) but leaves the user unaware.
- The output template and theory live in `references/`. In headless probes the Read tool sometimes needed approval and runs "worked from the SKILL.md body alone" (`docs/probes.md:77`). The SKILL.md body names the result and strength values (`SKILL.md:73-77`, `SKILL.md:89`) but not the record's fields, so the record can drift on surfaces that skip references. [unverified for mobile; not probed]
- Length: a "both" run produces two derivations, options and a record. On a phone this is long but readable because the template forbids wide tables (`output-template.md:3`).

### 6.3 Cross-surface

- **Implicit routing.** Codex lists `dia:dia-reductio` among model-visible skills (`docs/probes.md:31`). The description's trigger "wants to know whether a position is consistent or true" (`SKILL.md:3`) could fire on ordinary fact questions ("is it true that …?"). P7 tested only positive routing (`docs/probes.md:45-54`); no negative probe exists.
- **`--target=claude` on non-Claude assistants.** D14 keeps the value name; on ChatGPT and Codex a user must type `claude` to mean "your own answer". The natural-language inference rule (`SKILL.md:29`) covers most real use.
- **Language.** Rule 8 requires translating fixed result and strength values; on mixed-language turns the "latest message" rule decides. One P8 run replied in Korean to an English prompt, cause unknown (`docs/probes.md:76`).

## 7. Findings and recommendations (proposals only)

**1. "No contradiction found" is reported as consistency or independence. Severity: high.**
Evidence: `SKILL.md:57` ("neither does → these premises do not decide T; name the premise that would"), `SKILL.md:93` ("consistent with these premises"), result "undecided by these premises" (`SKILL.md:89`). Provability in first-order logic has no decision method [19], and models are weak at proof search [21]; a failed search shows neither consistency nor independence. Proposed text, `SKILL.md:57`: "neither does → no contradiction found in either direction. This does not show that the premises leave T open; name the premise that, if added, would decide it." Proposed text, `SKILL.md:93`: "write 'no contradiction found from these premises; this shows neither that they are consistent nor that T is true'". Proposed record value (`SKILL.md:89`, `output-template.md:47`): replace "undecided by these premises" with "no contradiction found". Add to Pitfalls: "Treating 'no contradiction found' as 'consistent'."

**2. [L] merges logical truths with definitions. Severity: high.**
Evidence: `SKILL.md:34` defines [L] as "a logical or definitional truth"; Rule 6 (`SKILL.md:38`) and the "internal" grade (`SKILL.md:75`) both treat [L] as fixed. Contested definitions are a known seat of question-begging [13]; Socrates' definitional premise had to be conceded by Meletus [18]; Quine denies a sharp analytic line [8]. Proposed text for Rule 2: "**[L]** a law of logic or arithmetic. A definition is [T] if the target stated or accepted it (quote it), otherwise [A] with the reason it is needed. Never label a definition you supplied [L]." Proposed addition to Step 5 "internal": "… [T] and [L] premises, and no definition you supplied."

**3. theory.md misattributes "which premise goes" and treats logic as unrevisable. Severity: medium.**
Evidence: `theory.md:32` cites IEP §5, which concludes A is "untenable (false) in the context of this family of givens" [1]. The point is Duhem's and Quine's [7][8]; choice criteria come from belief revision [9]. Proposed `theory.md` §3: "When a set is inconsistent, logic shows only that its members cannot all hold (Duhem; Quine, 'Two Dogmas'). Rescher's IEP entry treats the background as fixed and calls the supposition 'untenable … in the context of this family of givens', which is the skill's result label. Which member to give up is a further judgment; belief-revision theory ranks members by entrenchment, and Quine names conservatism and simplicity. Quine adds that even logical laws are revisable; this skill holds classical logic fixed and says so when that matters." Add the Quine, Duhem/SEP and belief-revision URLs to `theory.md` Sources.

**4. No rule for contradictories versus contraries, and negation is error-prone. Severity: medium.**
Evidence: Aristotle accepts a contrary [16]; contraries can both be false [15]; models struggle with negation [25]. Proposed addition to Rule 1: "not-Q must be the contradictory of Q (exactly one is true), not a contrary. 'All X are Y' contradicts 'some X is not Y', not 'no X is Y'. If the two lines are only contraries, add the premise that rules out both being false, labelled [L] or [A], and let the contradiction depend on it."

**5. A named rule per line is not a check, and the output should say so. Severity: medium.**
Evidence: CoT unfaithfulness [22][23]; weak fallacy detection [29]; content effects [31]. Proposed addition to Step 4: "Use only common rules (modus ponens, modus tollens, conjunction, simplification, disjunctive syllogism, universal instantiation, substitution of a listed definition, negation introduction, indirect proof). Before stating the contradiction, reread each line with the content words replaced by letters and confirm the rule still applies." Proposed record line in `output-template.md`: "- Checked by: rereading only | a tool (name it)".

**6. No worked example where it is needed. Severity: medium.**
Evidence: models could not use proof by contradiction without demonstrations [20]; the only example is prose in `theory.md:47`; headless runs sometimes did not open references (`docs/probes.md:77`). Proposal: add a ~12-line example to SKILL.md (still far under the 200-line guideline, spec §7.2), for instance: T [T] "the hotfix is a feature"; P1 [T] "every feature ships only after review"; P2 [T] "the hotfix shipped without review". 1. T — assumption; 2. if the hotfix is a feature, it shipped only after review — P1, universal instantiation; 3. the hotfix shipped only after review — 1, 2, modus ponens; 4. the hotfix did not ship only after review — P2; contradiction lines 3 and 4, depends on T, P1, P2, strength internal; options A give up T, B narrow P1 to "every feature except emergency fixes", C give up P2; record. Any short self-contained example works; it should show labels, rule names, the depends-on set and the grade.

**7. Disputed steps and self-examination are exposed to sycophancy. Severity: medium.**
Evidence: sycophancy is general [30]; intrinsic self-correction is weak [28]; `SKILL.md:105` says only "check it". Proposed text: "**The user disputes a step:** check it. Withdraw it only if you can name what fails: the rule does not apply, a premise is missing, or a term shifted. Otherwise restate the step with its rule and the lines it uses, and say why it stands. Disagreement alone does not withdraw a step." For `claude` (`SKILL.md:98`) add: "Do not soften the result because the answer is yours, and do not invent a contradiction to look self-critical."

**8. The description over-promises "true" and may over-route. Severity: medium.**
Evidence: `SKILL.md:3` "wants to know whether a position is consistent or true"; implicit invocation on Codex/ChatGPT (`agents/openai.yaml:7`, `docs/probes.md:31`); the skill cannot establish truth, only consistency relative to premises (`SKILL.md:93`). Proposed wording: "… or wants to know whether a position is consistent, or whether it follows from or contradicts stated premises, or the same in any language." Add a negative routing probe to P7's protocol (a plain fact question "is it true that …" must not load dia-reductio).

**9. Evidence classes lack "supplied by the user" and do not fit tool-less chats. Severity: medium.**
Evidence: `SKILL.md:34`, `output-template.md:17`; dia-refine's tool-less fix treats user-supplied material as a basis and recall as not verification (`docs/probes.md:67-71`). Proposed: "evidence: verified this session (a tool ran) | supplied by the user | single source | unverified recall. Recall is never 'verified'." Make the same change in `output-template.md:17`.

**10. The strength grades are the owner's design; label them and make the key check visible. Severity: low.**
Evidence: no source grades reductio this way; the grades correspond to Locke's ex concessis argument [13] and to begging the question [13]. The "carried by added premises" check (`SKILL.md:77`) is asserted, not shown. Proposed `theory.md` addition: "The three strength grades are this skill's own scheme. 'Internal' is what Locke called pressing someone 'with consequences drawn from his own principles or concessions'; 'carried by added premises' is a form of begging the question." Proposed `SKILL.md:77` addition: "Show the short derivation of not-T from the [A] and [L] premises alone, or write 'not found'."

**11. Vagueness slips through. Severity: low.**
Evidence: sorites chains are valid modus ponens with a failing tolerance premise [17][13]; Rule 4 covers only meaning shift. Proposed Pitfall: "A chain of small steps over a vague term ('one more grain does not make a heap'): each step may be valid, and the fault is the tolerance premise. List it as a premise and offer it as an option."

**12. Prefer the minimal, least-assumed contradiction. Severity: low.**
Evidence: greedy proof search [21]; premise order effects [27]; Step 6 builds one option per member of the set, so an idle member yields a fake option. Proposed Step 4 text: "Number premises in the order the derivation uses them. If more than one contradiction is reachable, report the one whose set has the fewest [A] premises. The depends-on set lists only premises the derivation actually uses."

**13. The classical-logic note is too narrow and the step is unnamed. Severity: low.**
Evidence: intuitionistically reductio proves only negative statements [4], not just existence [1]; `SKILL.md:59`, `theory.md:26-28`; the template has no line for the step that concludes T from a refuted not-T. Proposed `SKILL.md:59`: "In the prove direction, concluding T from a contradiction with not-T uses indirect proof, a rule of classical logic that intuitionistic logic rejects for any T that is not itself a negation. Name it on its line, and say so when it matters, above all for claims that something exists." Template: add "n+1. T — indirect proof (classical), discharging line 1".

**14. theory.md source and example fixes. Severity: low.**
Evidence: `theory.md:55` cites IEP for the *Apology*, which IEP does not name [1]; the primary text supports it [18]. The Madhyamaka line rests on Wikipedia (`theory.md:70`). The will and Kant cases are Rescher's "more loosely" / "anomalous" cases [1], while `theory.md:40-41` presents them neutrally. Proposed: cite the *Apology* directly (cross-examination of Meletus); either drop the Madhyamaka sentence or source it to a scholarly reference; add "(Rescher presents both as looser, anomaly-based uses)" after `theory.md:41`.

**15. Add a short "hard cases" section to theory.md. Severity: low.**
Evidence: Euclid IX.20 is a direct proof with a local reductio and is often misdescribed [11][12]; Zeno's plurality argument failed at a hidden mathematical premise [10]; paradoxes such as the Liar lead dialetheists to accept some contradictions [5][6]. Proposed section: three bullets: (a) a chain may contain a negation-introduction sub-step without being an indirect proof; (b) a premise that looks like an [L] truth can be false (Zeno's infinite sums); (c) for a paradox, the classical result is "premise set inconsistent"; mention that dialetheists and paraconsistent logicians treat some such contradictions differently, and that the skill holds classical logic fixed.

## 8. Open questions for the owner

1. Should the result value "undecided by these premises" be renamed (finding 1)? It appears in SKILL.md, the template and possibly in records the owner keeps.
2. Splitting definitions out of [L] (finding 2) changes how often "internal" and "the thesis is false" are reachable. Is that intended strictness, or is a separate [D] label preferred over folding definitions into [T]/[A]?
3. Is a worked example in SKILL.md acceptable under the "instructions only" and length rules (finding 6), or should it go in `output-template.md` with a pointer?
4. Should the skill mention, conditionally, that a code tool can check a propositional chain (truth table or SAT) when one is available, or would that invite tool-dependence on chat surfaces (spec §7.1)?
5. Keep "or true" in the description for Korean and English routing, given P7 passed with it? A narrower description needs a new P7 run.
6. On non-Claude surfaces, should `--target=self` be accepted as an alias of `claude` (D14 keeps `claude`)?
7. Paradox inputs: should the skill say anything about dialetheism, or is classical logic simply assumed with one line of disclosure (finding 15)?
8. Should a change set from this report bump `metadata.version` to 1.1.0 with a plugin version bump (spec §12.1), or wait for the sibling research files to be merged into one release?

## Sources

[1] https://iep.utm.edu/reductio — Rescher, Reductio ad Absurdum, Internet Encyclopedia of Philosophy
[2] https://encyclopediaofmath.org/wiki/Reductio_ad_absurdum — Reductio ad absurdum, Encyclopedia of Mathematics
[3] https://plato.stanford.edu/entries/natural-deduction — Natural Deduction Systems in Logic, SEP
[4] https://plato.stanford.edu/entries/logic-intuitionistic — Intuitionistic Logic, SEP
[5] https://plato.stanford.edu/entries/dialetheism — Dialetheism, SEP
[6] https://plato.stanford.edu/entries/logic-paraconsistent — Paraconsistent Logic, SEP
[7] https://plato.stanford.edu/entries/scientific-underdetermination — Underdetermination of Scientific Theory, SEP
[8] https://www.ditext.com/quine/quine.html — Quine, Two Dogmas of Empiricism (1951), full text
[9] https://plato.stanford.edu/entries/logic-belief-revision — Logic of Belief Revision, SEP
[10] https://plato.stanford.edu/entries/paradox-zeno — Zeno's Paradoxes, SEP
[11] https://mathcs.clarku.edu/~djoyce/java/elements/bookIX/propIX20.html — Euclid, Elements IX.20, tr. D. E. Joyce
[12] https://link.springer.com/article/10.1007/s00283-009-9064-8 — Hardy and Woodgold, Prime Simplicity, Mathematical Intelligencer (2009)
[13] https://plato.stanford.edu/entries/fallacies — Fallacies, SEP
[14] https://iep.utm.edu/fallacy — Fallacies, IEP
[15] https://plato.stanford.edu/entries/contradiction — Contradiction, SEP
[16] https://plato.stanford.edu/entries/aristotle-logic — Aristotle's Logic, SEP
[17] https://plato.stanford.edu/entries/sorites-paradox — Sorites Paradox, SEP
[18] https://www.gutenberg.org/files/1656/1656-h/1656-h.htm — Plato, Apology, tr. Jowett (Project Gutenberg)
[19] https://plato.stanford.edu/entries/church-turing — The Church-Turing Thesis, SEP
[20] https://arxiv.org/pdf/2305.15269v3 — Saparov et al., Testing the General Deductive Reasoning Capacity of LLMs Using OOD Examples (NeurIPS 2023)
[21] https://arxiv.org/abs/2210.01240 — Saparov and He, Language Models Are Greedy Reasoners (PrOntoQA)
[22] https://arxiv.org/abs/2305.04388 — Turpin et al., Language Models Don't Always Say What They Think (NeurIPS 2023)
[23] https://arxiv.org/abs/2307.13702 — Lanham et al., Measuring Faithfulness in Chain-of-Thought Reasoning
[24] https://arxiv.org/abs/2209.00840 — Han et al., FOLIO: Natural Language Reasoning with First-Order Logic
[25] https://arxiv.org/abs/2404.15522 — Parmar et al., LogicBench (ACL 2024)
[26] https://arxiv.org/abs/2305.19555 — Gendron et al., Large Language Models Are Not Strong Abstract Reasoners
[27] https://arxiv.org/abs/2402.08939 — Chen et al., Premise Order Matters in Reasoning with LLMs (ICML 2024)
[28] https://arxiv.org/abs/2310.01798 — Huang et al., Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2024)
[29] https://arxiv.org/abs/2311.07954 — Hong et al., A Closer Look at the Self-Verification Abilities of LLMs in Logical Reasoning
[30] https://arxiv.org/abs/2310.13548 — Sharma et al., Towards Understanding Sycophancy in Language Models
[31] https://arxiv.org/abs/2207.07051 — Dasgupta et al., Language models show human-like content effects on reasoning tasks
