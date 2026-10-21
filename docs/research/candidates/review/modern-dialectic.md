Verdict: SOUND WITH FIXES

# Review of docs/research/candidates/modern-dialectic.md (tree at eb7ab54)

Method: all 25 ledger citations were fetched (2026-10-21) and every quoted sentence was searched for in the fetched text. That covers the 20 citations behind the recommendations, the fidelity verdicts and the fit ratings, plus 5 spot-checks: [9], [14], [15], [18], [19]. All direct quotations were found. The defects are in how the procedure was assembled from the sources, in how far the HCI/LLM evidence is stretched, and in overlap with candidates the author could not see.

This document researches `dia-conjecture` only. dia-warrant and dia-counterplan come from argumentation.md, the munazara rule from scholastic.md. Mason appears here only as open question 6, "[unverified]" (line 270). I note only where those items touch this document.

## Per-recommendation verdicts

| Recommendation | Verdict | Change |
|---|---|---|
| ADD `dia-conjecture` (Lakatos) | **keep with changes** | Add Rules 3–4 and the hidden-lemma step (F1); split "doesn't count" into three cases (F2); add boundaries against dia-warrant, dia-negative and dia-reductio (F3); fix the roles claim (F4); label the departures (F5); fit "medium-high, conditional" (F6) |
| FOLD Popper's prior criterion into dia-conjecture | **keep with changes** | Label it as a Popperian addition (F9) |
| FOLD Kant's antinomy pattern into dia-reductio | **keep with changes, or defer** | New result value, reworded "last word", routing against dia-counterplan (F7) |
| FOLD Hegel's test into dia-negative Step 6 | **keep with changes** | Word it as the skill's own check; Hegel credit in theory.md only (F8) |
| SKIP Hegel "synthesis" skill, Peirce, Popper as a skill | **keep** | Well sourced |

## Findings

### F1 (high): the steps drop Rules 3 and 4 and the hidden-lemma step, so local counterexamples have no handling

- The document quotes Rules 1–4 (lines 137–141) and the three combinations (lines 132–135). Easwaran [21] confirms "Rule 3. If you have a local counterexample, check to see whether it is not also a global counterexample" and Rule 4, "replacing the refuted lemma by an unfalsified one".
- Step 5 (line 236) offers only "surrender, exception-barring, monster-adjustment, lemma-incorporation". The CUP contents [13] place these under "4 Criticism of the conjecture by global counterexamples".
- What is missing:
  - a local-but-not-global case (Rule 4: repair the proof, keep C) has no branch;
  - Rule 3 is never applied;
  - for a global-not-local case, "unearth the 'hidden lemma'" (SEP [4]) is not a step, though lemma-incorporation presupposes it.
- Every option on the menu shrinks C. Lakatos's content-increasing direction is absent: ch. 1 §6 "Increasing content by deeper proofs" [13]; SEP [4]: "a deeper problem than finding the domain of validity". The sketch therefore produces the "laundry list of exceptions" its own evidence warns of [17]. The round cap treats only the symptom.
- **Correction:** branch Step 5 on the Step 3 label.
  - Local only: apply Rule 4 (replace the lemma); C is unchanged.
  - Global only: name the hidden lemma the case refutes, add it to the proof-analysis, then apply Rule 2.
  - Both: lemma-incorporation.
  - Apply Rule 3 to every local case first.
  - Offer exception-barring and monster-adjustment only on request, as responses Lakatos rejects ([21]: "unproductive responses to counterexamples that he rejects").

### F2 (high): the ruling rules contradict each other and call correct rejections monster-barring

- Step 4 (line 235) says "A 'doesn't count' is named as monster-barring". The Never list (lines 245–246) bans both "rule on a counterexample's validity for the user" and "flip a verdict without naming a defect".
- Per [17], most model counterexamples are invalid: "the five human raters together judged 32% of them valid … compared to … 60% rated valid by Opus 4.5". A user who rejects one is usually right, and that is not monster-barring. Monster-barring is claiming that a *valid* case "never was a member of the domain" [21]; Pease et al. [20] treat it as a definitional move.
- The rules leave a bare "doesn't count" undecided: the assistant has no named defect, yet the user rules.
- **Correction:**
  1. Each counterexample shows, condition by condition, that it meets C's antecedent and violates its consequent.
  2. A case whose check the user faults is withdrawn as **invalid**. That is a named defect.
  3. A case that is conceded to meet C's stated terms but is excluded by redefining a term is **monster-barring**. It is accepted only as an explicit definition change with its lost content stated, labelled as a departure from Rule 2 ("Do not allow a refutation to be dismissed as a monster" [21]).
  4. A bare denial is recorded as **disputed**: neither dropped nor ruled on.

### F3 (medium): overlap is understated, and "policies" belongs to a sibling

- **dia-warrant** (owner-accepted):
  - Toulmin's rebuttal conditions, "circumstances in which the general authority of the warrant would have to be set aside" (argumentation.md:19), are counterexamples to a warrant.
  - Both skills take a claim plus its argument and label the parts they reconstruct, so "find holes in my argument that every X is Y" fits both.
  - **Correction:** dia-conjecture takes only strictly universal claims (all / always / never) and does iterated repair. "Generally / usually" claims and one-pass argument analysis go to dia-warrant: one counterexample to a defeasible claim is a rebuttal condition, not a refutation.
- **dia-negative** (rated "low", line 177):
  - It already tests a "claim, concept, plan or policy" against "a particular case or consequence D" (dia-negative SKILL.md:3, :34).
  - Its "narrow C to the scope where it holds" (:80) is exception-barring.
  - Line 221 and candidates/README.md:33 name "policies" as dia-conjecture's object. A counterexample to a policy needs a standard, and that is dia-negative's input.
  - **Correction:** drop "policies" from dia-conjecture's object.
- **dia-reductio** (line 175, "reductio seeks Q and not-Q, not cases"):
  - A single global counterexample *is* a refute run: Rule 1 says "'all X are Y' contradicts 'some X is not Y'" (SKILL.md:33).
  - Its worked example's repair, "every feature except emergency fixes" (:96), is exception-barring.
  - What dia-conjecture adds is local counterexamples and iterated repair.
  - **Correction:** say this in the overlap section, and keep "contradiction" and "follows from its premises" out of the description.
- **dia-elenchus:**
  - [17] tests counterexamples to *definitions* (friend, neighbor), which is dia-elenchus's "too broad / too narrow" step (SKILL.md:71–72).
  - **Correction:** once the dispute becomes what X means, route to dia-elenchus.

### F4 (medium): "no model plays both sides" is contradicted by the sketch

- Line 160: "The roles split cleanly, so no model plays both sides." Yet line 157 has the assistant reconstruct the proof as [A] lemmas and then attack them, and Step 5 has it recommend the repair. In that path the assistant writes the proof, the refutation and the fix.
- Separately, the user owns C *and* judges the cases against it. That is an incentive to monster-bar, and the document does not analyse it.
- **Correction:**
  - State that a run on [A] lemmas is the assistant arguing both sides and is conditional on the user accepting the lemmas.
  - Default to asking for the argument first (open question 2).
  - F2's per-case check makes the user's rulings checkable.

### F5 (medium): the fidelity label omits ch. 1 §§6–9 and misplaces Rule 5

- Open question 7 (line 271) says "deductive guessing" appears "only in later book sections". The cited contents [13] put it in chapter 1: "7 … c. Deductive guessing versus naive guessing … d. Increasing content by deductive guessing".
- The same chapter has "8 … a. Refutation by concept-stretching. A reappraisal of monster-barring" and "9 a. Unlimited concept-stretching destroys meaning and truth". SEP [4] asks whether there is "any distinction to be drawn between interesting and frivolous concept-stretching".
- So Lakatos partly re-legitimises monster-barring against concept-stretching counterexamples. That is the invalid-case class [17] measures, and the sketch treats it purely as a failure.
- **Correction:** label the skill "ch. 1 §§1–6, Rules 1–4; Rule 5 and the concept-stretching analysis of §§7–9 not implemented". Classify a case that is valid only under a stretched reading of a term as concept-stretching (F2's invalid class).

### F6 (medium): HCI/LLM studies are cited beyond their setups; "fit: high" is overstated

- **[24] Chiang et al.** The quote is exact ("helps groups significantly increase their appropriate reliance on AI assistance"). But the setup is groups predicting recidivism, with a devil's advocate arguing against a *separate AI model's* recommendation. dia-conjecture attacks the *user's* claim; its over-reliance risk is the user accepting the assistant's cases and repair, which [24] does not test.
- **[23] Danry et al.** Read as the abstract only. The intervention was one templated question asked before the user judged, and the effect held only for flawed statements (full-text reading in commit-first.md:33–40). dia-conjecture asserts counterexamples rather than asking.
- **[17].** The 69% → 17–30% curve is rated by Opus, which the authors call "probably best read as upper bounds". The chains are model-versus-model, on definitions, with no human in the loop.
- **[22] Buçinca et al.** "Might even increase it" is the abstract's background ("some studies suggest"). "Only cognitive forcing did" (line 62) is not shown: the three designs were pooled and overall over-reliance was not significant (commit-first.md:53).
- **Correction:** rewrite lines 162–170.
  - No study tests this method with users; [23] and [24] are distant analogues.
  - [17] shows model counterexamples are mostly invalid and that the model rates their validity about twice as high as humans do.
  - Fit: "medium-high, conditional on F2's check and the round cap".

### F7 (medium): the Kant fold breaks dia-reductio's fixed results and borders dia-counterplan

- "Both can hold, each in a narrower domain" (line 255) is not among dia-reductio's five results ("exactly one of", SKILL.md:108).
- "Give both the last word" (line 254) is impossible. Kant ([11]: "that side obtains the victory which has been permitted to make the attack") supports one reply each.
- "Two opposed positions" overlaps the owner-accepted dia-counterplan (argumentation.md:159–170) and README cluster 3.
- **Correction:**
  - Add a result value (for example "both hold in narrower domains") with its record field.
  - Change "both the last word" to "each side answers the other once".
  - Restrict the fold to opposed *claims* that come with arguments; plans and decisions go to dia-counterplan.
  - Run routing probes. This is more than "about three lines".

### F8 (low): the Hegel fold is labelled Hegel inside an Adorno skill

- dia-negative's theory.md:7 says Adorno "wanted a dialectic freed from the affirmative result". Calling the Step 6 check *Aufhebung* (line 259) imports that affirmative result.
- The four checks themselves are sound and fit Rule 7.
- **Correction:** in SKILL.md, word them as the skill's own check (cancel, keep, new, remainder). Put the Hegel credit, and Adorno's rejection of it, in theory.md.

### F9 (low): the Popper fold has no label, and one citation is misplaced

- The prior criterion (line 234) is an addition to Lakatos. SEP Popper [5] even reports that Lakatos "flatly denies that there are critical tests, in the Popperian sense".
- Line 202, "Lakatos covers surrender and goes beyond it.[5]", is not in [5]. The surrender point is in [4] (Gamma: "You have to surrender").
- **Correction:** label the criterion "Popper's prior refutation criterion; an addition", and cite [4] on line 202.

### F10 (low): the stop rule has an easy exit

- "Stop when a pass finds no counterexample" (line 239) lets the assistant declare "holding" without searching hard.
- **Correction:** a "holding" record lists the lemmas and kinds of case tried and names the most suspect lemma, as dia-negative does (SKILL.md:68).

### F11 (low): turn length and turn count

- The pattern lemma list + up to three labelled cases, then a ruling turn, then a repair-menu turn costs at least three phone turns per round. Siblings cap a turn at one phone screen (dia-elenchus SKILL.md:36).
- **Correction:** one counterexample per message by default.

### F12 (low): minor citation issues

- [16] measures flips under "Are you sure?" on classification tasks. Line 60 applies it to syntheses, which is interpretation, not a finding about syntheses.
- The ledger skips [6].

### Repo rules and tool-less operation

- The sketches are assistant-neutral, need no tool, contain no Hangul and are instructions only. No step is impossible on a tool-less mobile chat; line 197 already says recall is not a refutation.
- With F2, a global counterexample that rests only on recall should make C′ "conditional".

### Interaction with the owner-accepted items

- dia-warrant: both descriptions need the F3 boundary before either ships.
- dia-counterplan: the Kant fold must cede plans and decisions to it (F7).
- The munazara batch should list dia-conjecture among the dialogue skills. Its burden rule fits F2's "disputed" class only if the assistant still has to show that its case meets C's terms.

### Missed

- No fatal objection, and no better candidate in this family was overlooked.
- The material miss is Lakatos's content-increasing half (F1, F5). It is what separates the method from exception-listing, and it is the answer to the failure [17] reports.

## Citation table

| # | Source | Result | Evidence |
|---|---|---|---|
| 1 | SEP Hegel's Dialectics | supports | "never adopted Fichte's triadic … language"; "nothing extraneous is introduced"; Popper "begs the question (Priest 1989…)" |
| 2 | Hegel, Preface | supports | "a lifeless schema, to nothing better than a mere shadow" (§50); "external and empty application of the formula" (§51) |
| 3 | SEP Kant's Critique of Metaphysics | supports | "thesis and antithesis arguments are apagogic"; "both sides … might turn out to be correct" |
| 4 | SEP Lakatos | supports | "thought experiment which suggest a decomposition…"; "unearth the 'hidden lemma'"; "an empty tautology threatens"; "(P&R: 146)"; Gamma "surrender" |
| 5 | SEP Popper | partly | "criteria of refutation have to be laid down beforehand" (1963: 38 n.3) confirmed; line 202 unsupported (F9) |
| 7 | Hegel, Introduction | supports | §79 determinate negation; §84 "furnishes its own criterion in itself"; §85 "simply and solely to look on" |
| 8 | IEP Critical Rationalism | supports | "Lakatos extended the range of critical rationalism into mathematics"; "replaced refutation with criticism" |
| 9 | SEP Peirce on Abduction (spot) | supports | "The surprising fact, C, is observed…" (CP 5.189) |
| 10 | Popper, What is Dialectic? | supports | "only our critical attitude which produces the antithesis"; "(4) elevated" |
| 11 | Kant, Critique (Gutenberg) | supports | "thesis cum antithesis"; "impartial umpires"; "peculiar to transcendental philosophy"; "good or a bad smell"; "both may be true" |
| 12 | P&R (I), BJPS 1963 | supports | "a 'local counterexample' an example which refutes a lemma…"; "surreptitious changes … 'I meant'" |
| 13 | CUP P&R front matter | supports; contradicts OQ7 | §4 move names; ch. 1 §7 "Deductive guessing", §8 "concept-stretching" (F5) |
| 14 | SEP Peirce (spot) | supports | "integrate the three argument forms into … 'scientific method'"; "dialogical aspects of semeiotic" |
| 15 | Peirce 1877 (spot) | supports | "The irritation of doubt causes a struggle… I shall term this struggle inquiry" |
| 16 | FlipFlop | supports (loosely applied) | "All models frequently flip their answers when challenged"; 46%, 17% |
| 17 | Counterexample Game | partly | 32% vs 60%, 69% → 17–30% confirmed; Opus-rated, definitions, LM–LM (F6) |
| 18 | Hegelian self-reflection (spot) | supports | abstract: "self-dialectical approach … synthesize new scientific ideas" |
| 19 | POPPER agent (spot) | supports | "LLM agents that design and execute falsification experiments" |
| 20 | Pease et al. 2017 | supports | Lakatos "through the lens of dialogue game theory"; proponents' five moves |
| 21 | Easwaran 2015 | supports | Rules 1–3 verbatim, Rule 4 in n. 5; "unproductive responses … that he rejects" |
| 22 | Buçinca et al. | partly | "some studies suggest … might even increase it" (background); "least favorable subjective ratings" confirmed |
| 23 | Danry et al. (MIT page) | partly | abstract quote exact; abstract-only; flawed-only limit (F6) |
| 24 | Chiang et al. | partly | quote exact; groups, recidivism, devil's advocate against the AI's recommendation (F6) |
| 25 | Liang et al. | supports | "unable to generate novel thoughts later through reflection" |
| 26 | Khan et al. | supports | "76% and 88% accuracy … (naive baselines obtain 48% and 60%)"; setup caveat correct |

No citation was unreachable.
