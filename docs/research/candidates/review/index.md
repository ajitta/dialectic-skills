Verdict: SOUND WITH FIXES

Review of `docs/research/candidates/README.md` (the index) at `eb7ab54`, against the six family documents, `external-proposal.md`, `docs/research/README.md` and `skills/*/SKILL.md`. Read-only; nothing else was changed. Paths below are relative to `docs/research/candidates/` unless they start with `skills/` or `docs/`.

What checks out. All table counts match: lines (`wc -l`: 273/278/299/241/245/206) and sources (50/41/25/25/50/17; scholastic has no [18] and modern-dialectic has no [6], so 41 and 25 are correct). Every cited `[n]` in the six documents resolves to an entry in that document's source list (my own script; no unused entries either). The "Recommends adding" column matches each document's ranked recommendation, and the dia-elenchus, dia-negative and dia-reductio folds name files and steps that exist. The faults are in the external-proposal summary (one error), the clusters (reasons that are wrong or unsourced, and missing counter-evidence), and the fold list (one attribution, one status).

## 1. Claims vs the documents

**F1 (medium): dia-debate summary names a missing element that is not missing.**
- Index :25 says the debate gains need "separate debaters, hidden source text and a separate judge; one model in one chat has none of them".
- argumentation.md:113 lists what is missing as "no information asymmetry, no independent or trained debaters, and no quote verifier on a tool-less surface". It then keeps "two strongest cases … put before a human judge".
- The proposal itself has "the user judges" (external-proposal.md:23).
- Correction: "…separate debaters, hidden source text and a quote verifier; a single chat has none of them, although the user can still act as judge."

**F2 (low): Bastani filed under "Corrected" although the proposal made no claim to correct.**
- The proposal said the agent "could not confirm what the safeguards were" (external-proposal.md:10). commit-first.md:20 marks this "now resolved".
- The safeguards also included lists of common mistakes and the feedback for each (commit-first.md:20), which the index omits.
- Correction: move it to a "Resolved" item: "hint-not-answer prompt plus teacher-written solutions, common mistakes and feedback for each problem".

**F3 (low): the pre-mortem summary gives only the negative evidence.** The index rests the rejection on Mitchell 1989 (:24). argumentation.md:99–101 also records favourable later evidence (Veinott 2010; Gallop 2016, better-quality risks), and its actual reason to skip is "lens exists; the individual case is weak" (argumentation.md:154). Correction: state that reason.

**F4 (low): the scholastic row understates Sic et Non.**
- Index :10 has "(+ *Sic et Non* path)".
- scholastic.md:174 and :215 rank it third: "ADD `dia-sic-et-non`, or FOLD into dia-quaestio". Its input and output are distinct.
- Correction: "`dia-munazara`, `dia-quaestio`; `dia-sic-et-non` or a path inside quaestio."

**F5 (low): the `sources.py verify` claim (index :16) cannot be checked from this tree.** No `sources.py` or ledgers are committed. Internal resolution passes (see above), but "fetched" is a self-report. Correction: say where the tool and ledgers live, or reword to "every `[n]` resolves to an entry in the document's source list".

## 2. Clusters and picks

**F6 (medium): cluster 1's reasons are partly unsourced. The pick holds, on a reason the index leaves out.**
- Unsourced: "the defeasible, practical arguments most chats contain" (index :32). No document gives a frequency for this.
- Overstated: "Aristotle's list leans on ambiguity and deduction". Seven of the thirteen are outside language, including false cause and many-questions (platonic.md:153).
- The better argument, which the index omits: dia-reductio already covers most of dia-fallacy's ground. Its rules handle "equivocation (one sense per term), hidden premises, contraries versus contradictories, loose absurdity and slippery slopes" (platonic.md:176). Defeasible support is the gap no sibling covers (argumentation.md:24, :137).
- Strongest case against dia-warrant:
  - Its core move is supplying the unstated warrant. argumentation.md:22 calls that "the core danger" (invented premises, one of the owner's named risks).
  - dia-fallacy works on the quoted argument and must show each defect, never just a label (platonic.md:174, :197).
  - Users type "fallacy" (platonic.md:216; argumentation.md:36). "Warrant" is jargon, so routing on the user's own word favours dia-fallacy.
  - dia-warrant needs a shipped table of schemes (argumentation.md:191).
  - The one human-AI study cited for either skill is Danry. It tested hasty generalization with question prompts (commit-first.md:42), so it supports critical-question asking at least as much as Aristotle's list.
- Also wrong at :32: "dia-refine reviews the assistant's own answer". Its description covers "the previous answer or a named draft" (skills/dia-refine/SKILL.md:3), and its target is "another target the user names" (:24). commit-first.md:116 flags the same overlap.
- Correction: replace the frequency claim with the reductio-coverage argument. List the warrant-reconstruction risk as the price of the pick. Fix the dia-refine scope.

**F7 (high): cluster 2 is mis-framed, and its main reason reads a negative finding as support.**
- Heading: "the assistant only questions" (index :33). dia-conjecture does more: its step 5 has the assistant "recommend one (Rule 2 by default)" repair (modern-dialectic.md:236), and the assistant writes the counterexamples. So it is not the same role shape. The index itself says it differs in object and output.
- "Has a 2026 LLM study behind its limits": that study [17] found humans judged only 32% of model counterexamples valid, and validity fell to 17–30% over a chain (modern-dialectic.md:165–168). It is evidence against the reliability of the skill's core move. It supports only the cap of three counterexamples.
- Strongest case for dia-defend or dia-munazara instead:
  - Invented premises: each consequence must rest on the user's own quoted words or numbered agreed items, so an invented premise shows up as one the user can reject (asian.md:144). The asian document calls it "the only candidate with roles, answer types and an end rule that run unchanged in a chat" (asian.md:171).
  - Yielding under pushback: both have a reverse mode aimed at the "are you sure?" flip (asian.md:145, :195; scholastic.md:155–156). dia-conjecture has nothing comparable.
  - Over-reliance: the assistant asserts nothing in either.
- What does favour dia-conjecture:
  - Routing separability: elenchus overlap is partial, versus partial-high for defend (asian.md:134).
  - Mobile: "consequence chains are long on a phone" (asian.md:148).
  - If the munāẓara pushback rule is folded into existing skills (F12), most of the reverse-mode value arrives without a new skill.
- Correction:
  - Move dia-conjecture to cluster 4 ("distinct").
  - Make cluster 2 an explicit choice between dia-defend and dia-munazara, or neither if the fold ships.
  - State the counterexample-validity finding as a risk, not a credential.

**F8 (high): cluster 3's contrast is wrong on the one-model point, and a conflicting document is ignored.**
- "Quaestio has one model writing both sides" (index :34) implies dia-counterplan does not. It does whenever the plan is the assistant's own answer. argumentation.md:87 lists "One model plays both sides" as counterplan's departure from the original, and open question 2 (:189) proposes the assistant's own recommendation as the default.
- argumentation.md:115: "I found no evidence that one model writing both sides counters sycophancy."
- "Stronger evidence" (index :34) is relative only:
  - The DI/DA results come from human groups with separate advocates.
  - The LLM devil's-advocate studies "studied groups, not one user" (argumentation.md:91).
  - Lab studies favour DA over DI (argumentation.md:83).
- Not reconciled: modern-dialectic.md:20 declines the LLM devil's advocate because "dia-brainstorm's `stress` mode already plays that role". That contradicts adding dia-counterplan with a DA variant.
- Strongest case against dia-counterplan:
  - Routing risk against dia-brainstorm is "High" (argumentation.md:93). It needs dia-brainstorm's description to cede "poke holes"/"stress-test", which is a sibling edit with its own bump and probes. dia-quaestio's routing risk is medium (scholastic.md:45).
  - The two candidates do not answer the same request: a plan or decision versus a contested yes/no proposition.
- What does favour dia-counterplan: it never picks a winner, so the decision stays with the user. dia-quaestio always "determines", which invites over-reliance (scholastic.md:32). That is the defensible reason.
- Dropping quaestio also orphans the Sic et Non path, which has its own trigger, conflicting sources (scholastic.md:79, :232).
- Correction:
  - Restate the reasons as "user as judge; no verdict".
  - Add one-model-both-sides as a shared risk.
  - Note modern-dialectic.md:20 and that brainstorm's description must change.
  - List `dia-sic-et-non` under cluster 4.

**F9 (medium): pick-dependent folds are not tracked.**
- Several folds land inside candidates the index recommends against:
  - pragma-dialectics' three rules go into dia-warrant (argumentation.md:149). Fine, since warrant is picked.
  - *teyku*, the kept minority view and the quodlibet mode go into dia-quaestio (scholastic.md:130, :175, :177).
  - Kathavatthu and Mohist pushing go into dia-defend (asian.md:177–178).
- With the index's picks, the last two groups disappear silently. *Teyku* and "keep the strongest argument for the rejected side" would fit dia-counterplan's hand-off to the user.
- Correction: add a line under "Folds" for pick-contingent items and where each would go.

## 3. Routing among the three picks

**F10 (medium): the picks collide with each other and with four siblings, and two siblings would need text changes the index does not mention.**

Collisions:
- **counterplan vs dia-brainstorm.** Brainstorm's description owns "poke holes in it, or to stress-test it before committing" (skills/dia-brainstorm/SKILL.md:3), and its body has "push back on this".
- **counterplan vs dia-negative.** Negative takes a "claim, concept, plan or policy" (skills/dia-negative/SKILL.md:3).
- **warrant vs dia-reductio.** Reductio claims "whether a position holds together or follows from its premises", with no "strictly" (skills/dia-reductio/SKILL.md:3). argumentation.md:25 assumes that "follows strictly" is reductio's phrase. It is not, so reductio's description must change too.
- **warrant vs dia-refine.** Both cover "logical leaps" in the previous answer.
- **warrant vs counterplan.** Both claim "what is the hidden assumption" (argumentation.md:25 for warrant; counterplan step 2).
- **warrant vs conjecture.** A Toulmin warrant is a general rule, and testing it by cases is conjecture's move.
- **conjecture vs dia-elenchus.** Elenchus's too-broad/too-narrow tests are counterexamples to a definition (skills/dia-elenchus/SKILL.md:71–72).
- **conjecture vs counterplan and dia-negative.** modern-dialectic.md:221 lists "policies" in conjecture's scope. dia-negative also offers "narrow C … state C′ exactly" (skills/dia-negative/SKILL.md:80).

Exclusion sentences each description would need:
- **dia-warrant:** "For a strict contradiction, or whether a conclusion follows deductively, use dia-reductio; to fix errors and logical leaps in the previous answer or a draft, use dia-refine; for counterexamples to a general rule or claim, use dia-conjecture; for the assumptions under a plan or decision, use dia-counterplan."
- **dia-conjecture:** "Not for plans, decisions or ideas (for the opposing case use dia-counterplan; to poke holes or stress-test, dia-brainstorm), for what a word means (dia-elenchus), for finding Q and not-Q (dia-reductio), or for the gap between what a claim promises and what it delivers (dia-negative)."
- **dia-counterplan:** "Writes the opposing case; it does not question the user. To poke holes in or stress-test the user's idea through questions, use dia-brainstorm; for counterexamples to a general rule or claim, dia-conjecture; for where a plan fails its own standard or what it really serves, dia-negative."

Sibling edits these require:
- dia-reductio: "follows from its premises" becomes "follows strictly from its premises", plus "For how well reasons support a conclusion that is only probable, use dia-warrant".
- dia-brainstorm: "For the other side's case or a counterplan built from negated assumptions ('devil's advocate'), use dia-counterplan".

Each added cross-reference grows the always-loaded listing. scholastic.md:234 flags that budget (1,342 o200k tokens for seven skills). Probes P7 needs negative cells for every pair above, not only "against every sibling" (index :52). The pick-to-pick pairs are new.

## 4. Folds

**F11 (low): the reductio, negative and elenchus folds are correctly attributed:** Kant (modern-dialectic.md:250–256), prasanga (asian.md:175), Hegel's test for Step 6 (modern-dialectic.md:258–260; skills/dia-negative/SKILL.md:76), the peirastic line (platonic.md:187). All three `theory.md` files exist. One small inaccuracy: tarka is "SKIP: name it in dia-reductio theory" (asian.md:174), a note rather than a fold.

**F12 (medium): the munāẓara pushback rule is attributed with the wrong status and the wrong scope.**
- Status. scholastic.md recommends ADD `dia-munazara`, including configuration (b) (:172, :186). Folding only the rule is an alternative, posed as open question 1 (:229), not a recommendation. The index adopts it as a fold without saying it replaces configuration (b).
- "Open research theme 2" is wrong. Theme 2 was applied as D19 (docs/research/README.md:28, :33: "withdrawn only when its defect can be named"). Only multi-turn pushback probes remain open (:68). The rule would extend D19, not close an open theme.
- Scope. It is the claimant's rule: it binds whoever defends a stated proof (scholastic.md:155).
  - It fits where the assistant holds findings or a verdict: dia-reductio, dia-negative, dia-refine, and dia-brainstorm's verdict.
  - It does not fit dia-elenchus, where the assistant asserts nothing and already withdraws only a named defect (skills/dia-elenchus/SKILL.md:27, :88).
  - It is stricter than D19: a bare denial obliges the assistant to prove the denied premise, and failing that is *ifḥām* (defeat of that proof), not "show the step again and keep it".
- Parallel rule not credited: the Tibetan three-answer rule (asian.md:145, :195) does the same job.
- Correction: "Extends D19 (theme 2) in the skills where the assistant holds a finding (reductio, negative, refine, brainstorm's verdict): a bare denial obliges proof of the named premise, and failure concedes that proof; a charge that the proof fails, without a witness, is *mukābara* and not a reason to concede. Offered in scholastic.md open question 1 as the alternative to shipping dia-munazara's configuration (b); compare dia-defend's three answers."
