# Candidates: modern Western dialectic and philosophy of science

Candidate methods for new `dia-*` skills from Hegel, Kant, Lakatos, Popper and Peirce. Written 2026-10-21 against `main` at `becc4b3`. Proposals only; no skill file is changed. Sources were fetched and registered in a citation ledger; claims without a source are marked [unverified].

Two criteria carry the most weight. **Fidelity:** a method's name obliges the skill to follow it, or to say how it departs. **Fit for human-AI chat:** the skills run with one model in a chat and the user as the other party. Fit covers four AI-specific risks:

- **yielding under pushback** (sycophancy);
- **over-reliance:** the user adopts the model's answer instead of judging it;
- **one model playing both sides;**
- **invented premises or sources** that the user never gave.

## 1. Scope

- **Hegel (determinate negation, *Aufhebung*, the "thesis–antithesis–synthesis" legend):** covered. The question is whether a "synthesis" skill can be honest.
- **Kant (antinomies, the "sceptical method"):** covered. Hegel's dialectic grew out of it.
- **Lakatos (*Proofs and Refutations*):** covered. It has the most explicit procedure in this family, and the original is a dialogue.
- **Popper (conjectures and refutations):** covered as a dialogue, checked against dia-negative's Popperian falsifier.
- **Peirce (inquiry, abduction):** covered briefly, then dropped; there is no dialogue procedure to follow.
- **Dropped without a section:** Lakatos's research programmes (an appraisal of theory series, not a chat procedure); Fichte's synthetic method (it survives only as the popular triad, discussed under Hegel); Marx/Engels "laws of dialectics" (not a procedure).
- **An AI/HCI-origin method:** the LLM "devil's advocate" is used below as the nearest human-AI evidence. It is not proposed as a skill: dia-brainstorm's `stress` mode already plays that role.

## 2. Candidates

### 2.1 Hegel: determinate negation and sublation

**Sources.**
- Hegel's account in the Encyclopaedia Logic (§§79–82) gives three "moments" of every concept, not three steps of an argument.[1]
  - The understanding fixes a determination.
  - The dialectical moment exposes its one-sidedness, so it "sublates itself" into its opposite.
  - The speculative moment grasps the unity of the two as a positive result.
- *Aufheben* means to cancel and to preserve at once.[1] Popper lists four senses: reduced to components, cancelled, preserved and elevated.[10]
- **Determinate negation.** Against scepticism, which "always sees in the result only pure nothingness", "this nothing is determinate, is the nothing of that out of which it comes as a result", and so "a new form has thereby immediately arisen" (*Phenomenology*, Introduction §79).[7]
- **The Introduction's procedure.**[7]
  - Consciousness "furnishes its own criterion in itself", so "we do not require to bring standards with us" (§84).
  - When knowledge and object fail to correspond, consciousness alters its knowledge, and "the examination is not only an examination of knowledge, but also of the criterion" (§85).
  - The philosopher's part is "simply and solely to look on" (§85).

**The triad is not Hegel's.**
- Hegel "never adopted Fichte's triadic 'thesis—antithesis—synthesis' language" for his own philosophy (SEP, citing Mueller 1958).[1]
- He attacked triadic formalism as "a lifeless schema, to nothing better than a mere shadow", an "external and empty application of the formula" (Preface §§50–51).[2]
- Popper adds three points:[10]
  - "It is only our critical attitude which produces the antithesis."
  - A synthesis "will, in every case, embody some new idea which cannot be reduced to earlier stages".
  - The triad "will hardly ever help to develop thought by its suggestion that a synthesis should be constructed out of the ideas contained in a thesis and an antithesis".
- Popper's charge that dialectic tolerates contradictions is disputed: Priest calls it question-begging (SEP).[1]

**Fidelity in a chat.** Low for "Hegelian synthesis".
- The movement must come from the content itself: "nothing extraneous is introduced".[1] An assistant that writes the synthesis is exactly the outside party Hegel excludes.
- The honest kernel is a test that any proposed resolution must pass:
  - it names each side's specific one-sidedness, with a case;
  - it says what it cancels and what it preserves;
  - it names what is new in it;
  - it states its own one-sidedness.
- **Shape and inputs:** one pass or serial. The user supplies one position, or two.

**Fit for human-AI chat: low.**
- **Roles.** The user would bring a position, or two. The assistant would play the negating side and the synthesizer.
- **One model, both sides.** It runs the opposition and the resolution itself, which is the worst case for this risk.
- **Over-reliance.** The output is a finished position to adopt.
- **Sycophancy.** A synthesis that gives "both a point" is agreement theater by construction. All models in FlipFlop "frequently flip their answers when challenged".[16]
- **Self-reflection loops** "suffer from the Degeneration-of-Thought problem": once confident, the model "is unable to generate novel thoughts later through reflection".[25]
- **Ready explanations.** Explanations do not reduce over-reliance and "might even increase it"; only cognitive forcing did.[22]

**Overlap.**
- dia-negative: **high**. It already runs the Introduction's method (own standard, determinate negation) and credits Hegel. Rule 7 stops before the positive step, after Adorno.
- dia-brainstorm: partial (Step 3 options; the synthesizing question asked of the *user*).
- dia-reductio and dia-elenchus: partial.
- Others: none.

**Routing risk:** high. "Dialectic", "Hegel" and "thesis, antithesis, synthesis" would pull from dia-negative; "find a middle ground" would pull from dia-brainstorm.

**Tool-less:** yes.

**LLM research.** arXiv:2501.14917 runs a "Hegelian dialectic" self-dialogue to "synthesize new scientific ideas" and reports better ideation and reasoning.[18] I read only the abstract; it uses the popular triad as a generation loop.

### 2.2 Kant: the antinomies and the "sceptical method"

**Sources** (*Critique of Pure Reason*, Antinomy of Pure Reason; Meiklejohn translation).
- **Antithetic** (Section II) studies "the self-contradiction of seemingly dogmatical cognitions (thesis cum antithesis), in none of which we can discover any decided superiority".[11]
- **The method:** "watching, or rather of originating, a conflict of assertions, not for the purpose of finally deciding in favour of either side, but to discover whether the object of the struggle is not a mere illusion".[11]
  - This "sceptical method" aims "at certainty" by finding "the point of misunderstanding".
  - It is judged by "impartial umpires".
  - Kant warns that the side "permitted to make the attack" wins.
- **Scope.** The method "is essentially peculiar to transcendental philosophy, and can perhaps be dispensed with in every other field". Kant also likens it to legislators learning from "the embarrassment of judges".[11]
- **Structure.** Each side is an apagogic proof that refutes the other.[3]
- **Diagnosis** (Section VII).
  - Of two "dialectically opposed judgements both may be false", since one "enounces more than is requisite for a full and complete contradiction". Kant's example: "Everybody has either a good or a bad smell" omits "no smell at all".
  - "If two opposite judgements presuppose a contingent impossible, or arbitrary condition, both … fall away."
  - The proofs are valid "under the supposition" that is at fault.[11]
- **Two outcomes.**
  - Mathematical antinomies: both conclusions are false.[3]
  - Dynamical antinomies: "both sides … might turn out to be correct", each with its domain limited.[3] Kant: "both may be true".[11]

**Fidelity in a chat.**
- **The pattern can be followed closely:** argue both sides; test whether they are contradictories or only dialectical opposites; name the shared presupposition; conclude "both false" or "both true, each in a narrower domain".
- **Kant's content cannot be followed:** the presupposition is always transcendental realism, and the cure is transcendental idealism. Using the method outside metaphysics also goes against his scope remark, so it needs a label.
- **Shape and inputs:** one pass. The user supplies two opposed positions.

**Fit for human-AI chat: medium.**
- **Roles.** Kant's roles are two combatants and an umpire. In a chat the assistant argues both sides and the user should be the umpire.
- **One model, both sides.** This is the built-in risk: the model can steelman the side it favours and weaken the other. Kant's own warning that the last attacker wins argues for giving both sides the last word.
- **Sycophancy.** The structure counters it: by design no side is declared the winner. A user who presses "so which is right?" gets the diagnosis, not a verdict.
- **Invented premises.** The shared presupposition must be quoted from the two positions or labelled as added.
- **Evidence (nearest analogue).** In debate where two LLM experts each argue a different answer, human non-expert judges reached 88% accuracy against a 60% baseline.[26] That used separate debaters with hidden evidence, which is stronger than one model writing both sides.

**Overlap.** dia-reductio: **high**.
- Its "both" direction ends in **premise set inconsistent**, "the fault is in the premises, not T", and names "a premise both derivations use".
- Its Rule 1 already separates contradictories from contraries.
- Its theory.md already cites the antinomies (IEP).

Others: low or none.

**Routing risk:** a separate `dia-antinomy` would take dia-reductio's "does it hold together" requests.

**Tool-less:** yes.

**LLM research:** none found on the antinomy procedure itself.

### 2.3 Lakatos: the method of proofs and refutations

**Sources.** *Proofs and Refutations* (BJPS 1963–64; book 1976) is a classroom dialogue on Euler's V − E + F = 2, dedicated to Pólya and Popper.[4][12][13] Chapter 1 names the moves:[13]
- surrender;
- monster-barring;
- exception-barring ("piecemeal exclusions", "strategic withdrawal");
- monster-adjustment;
- lemma-incorporation;
- hidden lemmas.

The terms:
- **Proof:** a "thought experiment" that decomposes the conjecture into lemmas.[4]
- **Local counterexample:** "refutes a lemma (without necessarily refuting the main conjecture)". **Global counterexample:** "refutes the main conjecture itself".[12]
- **Combinations:**[4]
  - global but not local: unearth the hidden lemma;
  - local but not global: replace the lemma;
  - both: incorporate the lemma as a condition.

The rules (quoted by Easwaran):[21]
- **Rule 1.** "If you have a conjecture, set out to prove it and to refute it. Inspect the proof carefully to prepare a list of non-trivial lemmas (proof-analysis); find counterexamples both to the conjecture (global counterexamples) and to the suspect lemmas (local counterexamples)."
- **Rule 2.** "If you have a global counterexample discard your conjecture, add to your proof-analysis a suitable lemma that will be refuted by it, and replace the discarded conjecture by an improved one that incorporates that lemma as a condition. Do not allow a refutation to be dismissed as a monster. Make all 'hidden lemmas' explicit."
- **Rule 3.** Check whether a local counterexample is also global.
- **Rule 4.** For a local but not global counterexample, replace the refuted lemma "by an unfalsified one".

The failure modes:
- **Monster-barring** claims the counterexample "never was a member of the domain"; **exception-barring** shrinks the domain to exclude it.[21]
- Restriction risks "an empty tautology".[4]
- The Teacher refuses "surreptitious changes in my position by sentences starting with 'I meant …'".[12]

**Lineage.** SEP: Lakatos thought "Hegelian language" could describe mathematical growth (P&R: 146), and the "Popperian Gamma" voices surrender.[4] IEP: the book "extended the range of critical rationalism into mathematics".[8]

**Fidelity in a chat:** high, for a general claim that comes with an argument.
- Native to a chat: the rules are explicit, the original is a dialogue, and the moves have names. Pease et al. formalised the same moves as a dialogue game.[20]
- Departures that need a label:
  - use outside informal mathematics;
  - a class of students compressed into one assistant;
  - the assistant finds most counterexamples, so the user must rule on whether they count.
- **Shape:** one pass per turn, iterated by follow-ups.
- **The user supplies** a general claim (all / always / never) and ideally its reasons. If there are none, the assistant reconstructs them as labelled [A] lemmas.

**Fit for human-AI chat: high.**
- **Roles.** The user is the proponent who owns the conjecture and its proof, like the Teacher. The assistant is the class that raises counterexamples. The user rules on each counterexample and chooses the repair. The roles split cleanly, so no model plays both sides.
- **Sycophancy.** The named moves make pushback classifiable. "That's not really an X" is monster-barring, which may be accepted only as an explicit definition change with its lost content stated. A verdict is withdrawn only if a defect can be named (the repo's rule). The method itself counters yielding.
- **Over-reliance.** The assistant proposes cases and the user decides. This is the questioning stance that HCI work favours:
  - AI-framed questions "significantly increase human discernment of logically flawed statements", compared with even "causal AI explanations of an always correct system".[23]
  - An interactive LLM devil's advocate that challenged AI recommendations "helps groups significantly increase their appropriate reliance".[24]
- **Invented content.** The [T]/[A] lemma labels expose reconstructed premises. The real weakness is invented or invalid counterexamples:[17]
  - humans judged 32% of model counterexamples valid, the model 60%;
  - validity fell from 69% to 17–30% over a chain;
  - repairs became "a laundry list of exceptions" (exception-barring).

  Consequences for the design: few counterexamples per pass, the user's ruling, a round cap.
- **Cost.** Effortful formats that reduce over-reliance got the "least favorable subjective ratings".[22] The skill must keep turns short.

**Overlap.**
- dia-elenchus: partial. It tests a *definition* with no advice; Lakatos tests a *claim and its proof* and recommends a repair. They meet at monster-barring.
- dia-reductio: partial. Its premise list resembles proof-analysis, but reductio seeks Q and not-Q, not cases.
- dia-brainstorm: partial. "Counterexample" and "falsification pull" are single tactics there, with no proof-analysis and no local/global distinction.
- dia-negative, dia-refine, dia-iterate: low. dia-confirm: none.

**Routing risk:** moderate. "Poke holes" and "stress-test" go to dia-brainstorm, and "follows from its premises" goes to dia-reductio. The description must key on a general claim plus its argument, with the triggers "proofs and refutations", "Lakatos", "counterexamples to my conjecture / rule / proof" and "monster-barring".

**Tool-less:** yes.

### 2.4 Popper: conjectures and refutations

**Sources.**
- P1 → TT → EE → P2: problem, tentative theory, error elimination, new problem.[5]
- Corroboration counts only for "risky" predictions.[5]
- "Criteria of refutation have to be laid down beforehand: it must be agreed which observable situations, if actually observed, mean that the theory is refuted" (*Conjectures and Refutations* 38 n.3).[5]
- Rescue "by the addition of ad hoc hypotheses" degrades a theory into dogma.[5]
- Outside science Popper "replaced refutation with criticism".[8] Criticism consists in "pointing out some contradiction".[10]

**Fidelity in a chat.** High as a dialogue: problem, conjecture, what it forbids, prior refutation criteria, attempted refutation, no ad hoc rescue. Low as testing without tools: the POPPER agent must "design and execute falsification experiments".[19]

**Fit for human-AI chat: medium.**
- **Roles.** The user conjectures; the assistant criticizes.
- **Goalposts.** The prior criterion is the method's best anti-sycophancy device: it fixes in advance what counts, so neither the user nor the assistant can reinterpret afterwards.
- **No tools.** The user, not the model, must run every test; recall is not a refutation.

**Overlap.**
- dia-brainstorm: **high** ("what would you have to see to drop this?"; `stress` mode).
- dia-negative: partial (its falsifier, labelled Popperian).
- Lakatos covers surrender and goes beyond it.[5]

**Routing risk:** high against dia-brainstorm. **Verdict:** fold the prior criterion into the Lakatos candidate.

### 2.5 Peirce: inquiry and abduction (dropped)

- **Inquiry:** "The irritation of doubt causes a struggle to attain a state of belief. I shall term this struggle inquiry." Peirce compares four methods of fixing belief: tenacity, authority, a priori and science (1877).[15]
- **Abduction:** "The surprising fact, C, is observed. But if A were true, C would be a matter of course. Hence, there is reason to suspect that A is true" (CP 5.189). It belongs to discovery.[9]
- **Scientific method:** abduction, deduction and induction are its three phases.[14]
- **Dialogue form:** SEP notes only the "dialogical aspects of semeiotic" and their game-theoretic readings.[14] That is not a procedure.

**Fit: low.**
- **Roles.** An "abduce" skill makes the assistant the hypothesis generator, which maximizes over-reliance and invented facts.
- **Routing.** It would capture factual "why is X happening?" questions.

## 3. Comparison

| Candidate | Fidelity | Fit for AI chat | Overlap | User value | Recommendation |
|---|---|---|---|---|---|
| Lakatos, proofs and refutations | high (domain label) | **high**: user proposes and rules, assistant raises cases; named moves resist yielding | partial: elenchus, reductio, brainstorm | high: rules, policies, generalizations; maths | **ADD** `dia-conjecture`: explicit rules, native dialogue, clean roles, distinct input |
| Kant, antinomy pattern | high (pattern), low (content) | medium: one model argues both sides; user as umpire; no winner | high: dia-reductio | medium-high: false dilemmas | **FOLD** into dia-reductio as a dispute reading |
| Hegel, determinate negation / sublation | low ("synthesis"), medium (as a test) | low: model plays both sides and synthesizer; a ready answer invites over-reliance | high: dia-negative | medium | **FOLD** the test into dia-negative Step 6; **SKIP** a synthesis skill |
| Popper, conjectures and refutations | high (dialogue), low (testing without tools) | medium: prior criterion fixes goalposts; user must run tests | high: brainstorm, negative | medium | **FOLD** the prior criterion into `dia-conjecture` |
| Peirce, abduction | low (no dialogue procedure) | low: assistant as hypothesis generator | partial: brainstorm | low-medium | **SKIP** |

## 4. Ranked recommendation

**1. ADD `dia-conjecture`: Lakatos's method of proofs and refutations.**
- **Label.** "Lakatos's method of proofs and refutations (*Proofs and Refutations*, ch. 1, Rules 1–4), applied to any general claim backed by an argument, not only mathematical conjectures. Lakatos's class is compressed into the assistant, which raises counterexamples, and the user, who owns the claim, rules on each counterexample and picks the repair."
- **Steps.**
  1. Quote the general claim C.
  2. Proof-analysis: lemmas L1…Ln, labelled [T] (said by the user) or [A] (reconstructed), with suspected hidden lemmas marked.
  3. At most three counterexamples, each a specific case labelled global, local or both, with its evidence class. For an empirical C, first state the observation that would refute it (Popper's prior criterion).[5]
  4. Ask the user to rule on each counterexample. A "doesn't count" is named as monster-barring and is accepted only as an explicit definition change with its lost content stated.
  5. For each counterexample the user accepts, lay out the named responses (surrender, exception-barring, monster-adjustment, lemma-incorporation), recommend one (Rule 2 by default), and state how much content C′ keeps. The user decides.
  6. Record: C → C′, lemmas, rulings, open suspect lemmas.
- **Stop rule.**
  - Stop when a pass finds no counterexample to C′: result "holding against the cases tested", never "proved".
  - Stop when the user stops.
  - After three rounds, or once repairs become lists of exceptions, offer to stop and name the pattern.[17]
- **Never:**
  - dismiss a counterexample as a monster without saying so;
  - redefine a term silently ("I meant …");[12]
  - rule on a counterexample's validity for the user;
  - flip a verdict without naming a defect;
  - write C′ before the user has picked a response;
  - run on plans or ideas (dia-brainstorm), on definitions alone (dia-elenchus), or on a search for Q and not-Q (dia-reductio).

**2. FOLD Kant's antinomy pattern into dia-reductio.**
- **Label** for theory.md: "The dispute reading follows the pattern of Kant's resolution of the antinomies (*Critique of Pure Reason*, Antinomy, Sections II and VII). Kant limited the method to transcendental philosophy and diagnosed one presupposition only."
- **Proposed text,** about three lines, for when the user brings two opposed positions:
  - state each at full strength, quoting its proponent where possible, and give both the last word;[11]
  - say whether the opposition is contradictory or only contrary (Rule 1);
  - if both directions reach a contradiction, name the shared premise and give the outcome plainly: "both false: the shared premise fails", or "both can hold, each in a narrower domain".[3]
- **The user is the umpire:** never declare a winner when the fault is the shared premise.

**3. FOLD Hegel's honest kernel into dia-negative Step 6.**
- **Label:** "The test on a revised claim borrows Hegel's determinate negation and *Aufhebung* (cancel and preserve), not the thesis–antithesis–synthesis triad, which is not Hegel's."
- **Proposed text.** A revised-claim option must cancel the specific failed part of C, preserve what C delivered, name what is new, and state its remainder (Rule 7 already). It is offered as an option for the user to pick, never as the resolution.
- **Why not a standalone skill:** a "synthesis" skill would either use the triad Hegel called "a lifeless schema",[2] or make the model play both sides and the judge, the lowest fit for AI chat in this family.

## 5. Open questions for the owner

1. **Name for candidate 1.** `dia-conjecture` (my pick), `dia-lemma` or `dia-refute`? `dia-refute` sits close to dia-reductio in routing.
2. **Claims without an argument.** Accept them with reconstructed [A] lemmas (more useful), or ask for the argument first (closer to Lakatos)?
3. **"Find counterexamples" requests.** Should they move from dia-brainstorm to `dia-conjecture`? That needs a description change and P7-style routing probes on Claude and Codex.
4. **Kant.** A dispute reading inside dia-reductio, or a separate `dia-antinomy` (easier to find, but high routing overlap)?
5. **"Thesis–antithesis–synthesis" requests.** After the Hegel fold they would reach dia-negative, which refuses a forced synthesis. Add an explicit pointer?
6. **An AI/HCI-origin alternative.** Mason's "dialectical approach to strategic planning" (1969, cited by Chiang et al.)[24] pits a plan against a counterplan built on opposite assumptions, with the human deciding [unverified: details not read]. Worth a separate candidate study?
7. **Rule 5.** Lakatos's Rule 5 ("deductive guessing" of a deeper theorem) appears only in later book sections, which I read on an unofficial copy and do not cite.[unverified] Leave it out?

## Sources

[1] https://plato.stanford.edu/entries/hegel-dialectics — Maybee, Hegel's Dialectics (SEP)
[2] https://www.marxists.org/reference/archive/hegel/works/ph/phprefac.htm — Hegel, Phenomenology of Spirit, Preface (Baillie trans., marxists.org)
[3] https://plato.stanford.edu/entries/kant-metaphysics — Kant's Critique of Metaphysics (SEP)
[4] https://plato.stanford.edu/entries/lakatos — Imre Lakatos (SEP)
[5] https://plato.stanford.edu/entries/popper — Karl Popper (SEP)
[7] https://www.marxists.org/reference/archive/hegel/works/ph/phintro.htm — Hegel, Phenomenology, Introduction (Baillie trans., marxists.org)
[8] https://iep.utm.edu/karl-popper-critical-ratiotionalism — Popper: Critical Rationalism (IEP)
[9] https://plato.stanford.edu/entries/abduction/peirce.html — Douven, Abduction > Peirce on Abduction (SEP)
[10] https://www.vordenker.de/ggphilosophy/popper_what-is-dialectic.pdf — Popper, What is Dialectic? (Mind 1940; vordenker.de PDF)
[11] https://www.gutenberg.org/cache/epub/4280/pg4280.txt — Kant, Critique of Pure Reason (Meiklejohn trans., Project Gutenberg plain text)
[12] https://m-u-l-t-i-p-l-i-c-i-t-y.org/media/pdf/Proofs-and-Refutations.pdf — Lakatos, Proofs and Refutations (I), BJPS 14(53), 1963 (scan)
[13] https://assets.cambridge.org/97811071/13466/frontmatter/9781107113466_frontmatter.pdf — Lakatos, Proofs and Refutations (CUP, Worrall & Zahar eds.), front matter and contents
[14] https://plato.stanford.edu/entries/peirce — Charles Sanders Peirce (SEP)
[15] https://en.wikisource.org/wiki/Popular_Science_Monthly/Volume_12/November_1877/Illustrations_of_the_Logic_of_Science_I — Peirce, The Fixation of Belief (1877), Wikisource
[16] https://arxiv.org/abs/2311.08596 — Laban et al., Are You Sure? FlipFlop experiment (arXiv:2311.08596)
[17] https://arxiv.org/html/2605.03936 — The Counterexample Game (arXiv:2605.03936)
[18] https://arxiv.org/abs/2501.14917 — Self-reflecting LLMs: A Hegelian Dialectical Approach (arXiv:2501.14917)
[19] https://arxiv.org/abs/2502.09858 — Huang et al., Automated Hypothesis Validation with Agentic Sequential Falsifications (arXiv:2502.09858)
[20] https://www.pure.ed.ac.uk/ws/portalfiles/portal/33001190/pease_et_al_aij_1.pdf — Pease et al., Lakatos-style collaborative mathematics through dialectical, structured and abstract argumentation, AIJ 246 (2017)
[21] https://www.kennyeaswaran.org/papers/rebutting-undercutting-math.pdf — Easwaran, Rebutting and Undercutting in Mathematics, Phil. Perspectives 29 (2015)
[22] https://arxiv.org/abs/2102.09692 — Buçinca et al., To Trust or to Think: cognitive forcing functions reduce overreliance (arXiv:2102.09692, CSCW 2021)
[23] https://www.media.mit.edu/publications/don-t-just-tell-me-ask-me-ai-systems-that-intelligently-frame-explanations-as-questions-improve-human-logical-discernment-accuracy — Danry et al., Don't Just Tell Me, Ask Me (CHI 2023), MIT Media Lab page
[24] https://dl.acm.org/doi/fullHtml/10.1145/3640543.3645199 — Chiang et al., Enhancing AI-Assisted Group Decision Making through LLM-Powered Devil's Advocate (IUI 2024)
[25] https://arxiv.org/abs/2305.19118 — Liang et al., Encouraging Divergent Thinking in LLMs through Multi-Agent Debate (arXiv:2305.19118)
[26] https://arxiv.org/abs/2402.06782 — Khan et al., Debating with More Persuasive LLMs Leads to More Truthful Answers (arXiv:2402.06782)
