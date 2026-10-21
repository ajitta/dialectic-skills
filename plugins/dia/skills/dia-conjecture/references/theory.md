# Proofs and refutations: theory reference

Read this only when the user asks about the method or the sources. The rules are in SKILL.md; this file says where they come from and where the skill departs from Lakatos. Sources are listed at the end; everything here is paraphrased from them unless quoted.

## 1. The method

- Imre Lakatos's *Proofs and Refutations* (British Journal for the Philosophy of Science, 1963-64; book 1976, edited by Worrall and Zahar) is a classroom dialogue on Euler's conjecture that V − E + F = 2 for polyhedra. Chapter 1 names the moves this skill uses (CUP contents).
- **Proof:** a "thought experiment" that decomposes the conjecture into lemmas (SEP). Listing the lemmas is proof-analysis.
- **Local and global counterexamples:** a local counterexample "refutes a lemma (without necessarily refuting the main conjecture)"; a global one "refutes the main conjecture itself" (*Proofs and Refutations* I, BJPS 1963).
- **The combinations** (SEP): global but not local, unearth the "hidden lemma"; local but not global, replace the lemma; both, incorporate the lemma as a condition.

## 2. Rules 1-4

As quoted by Easwaran (Rule 4 in his note 5):

- **Rule 1.** "If you have a conjecture, set out to prove it and to refute it. Inspect the proof carefully to prepare a list of non-trivial lemmas (proof-analysis); find counterexamples both to the conjecture (global counterexamples) and to the suspect lemmas (local counterexamples)."
- **Rule 2.** "If you have a global counterexample discard your conjecture, add to your proof-analysis a suitable lemma that will be refuted by it, and replace the discarded conjecture by an improved one that incorporates that lemma as a condition. Do not allow a refutation to be dismissed as a monster. Make all 'hidden lemmas' explicit."
- **Rule 3.** "If you have a local counterexample, check to see whether it is not also a global counterexample."
- **Rule 4.** For a local but not global counterexample, the proof is improved by "replacing the refuted lemma by an unfalsified one"; the conjecture stands.

SKILL.md Step 3 applies Rules 1 and 3; Step 5 branches on Rules 2 and 4.

## 3. The responses Lakatos rejects

Chapter 1 section 4 ("Criticism of the conjecture by global counterexamples") names surrender, monster-barring, exception-barring, monster-adjustment and lemma-incorporation (CUP contents).

- **Monster-barring** claims the counterexample "never was a member of the domain"; **exception-barring** shrinks the domain to exclude it (Easwaran). Easwaran calls these "unproductive responses to counterexamples that he rejects". SKILL.md offers exception-barring and monster-adjustment only on request, labelled that way. Monster-adjustment (ch. 1 section 4d) is not in Easwaran's list; the skill groups it with them because, like monster-barring, it saves C by reinterpreting the case instead of improving the proof. That grouping is the skill's reading, not a quoted source.
- Restriction without explanation risks "an empty tautology" (SEP), as in "For all Eulerian polyhedra … V − E + F = 2". SKILL.md Step 5 refuses a weaker lemma that only restates B for this reason.
- The Teacher refuses "surreptitious changes in my position by sentences starting with 'I meant …'" (*Proofs and Refutations* I). This is SKILL.md hard rule 5.
- **Surrender** is voiced by the "Popperian" student Gamma (SEP). SKILL.md keeps it as "give up C".

## 4. What is implemented, and what is not

- **Implemented:** chapter 1 sections 1-6 and Rules 1-4. Section 6, "Increasing content by deeper proofs", is the content-increasing half of the method; SEP calls it "a deeper problem than finding the domain of validity". SKILL.md uses this deeper-proof move (6a) in one place: for a local case against a lemma already built into C, a replacement lemma that widens the revised claim. For a global case it also offers a weaker lemma to build in than the one first named; that is the skill's reading of Rule 2's "a suitable lemma", not section 6. So repairs are not only restrictions.
- **Not implemented:** section 7 (Rule 5 and "deductive guessing versus naive guessing", "increasing content by deductive guessing"), and the concept-stretching analysis of sections 8 ("Refutation by concept-stretching. A reappraisal of monster-barring") and 9 ("Unlimited concept-stretching destroys meaning and truth") (CUP contents). In those sections Lakatos partly re-legitimises monster-barring against counterexamples that stretch a concept; SEP asks whether there is "any distinction to be drawn between interesting and frivolous concept-stretching". This skill only classifies such a case as concept-stretching and does not count it against the reading of the claim fixed at the start; a narrowing first stated after a case is raised is monster-barring, not concept-stretching.

## 5. Departures from Lakatos (labelled)

- **Domain:** Lakatos wrote about informal mathematics. The skill takes any strictly universal claim (all / always / never), a rule or generalization about what is the case, not a policy to adopt.
- **Roles:** Lakatos's class of many students is compressed into one assistant, which raises cases, and the user, who owns the claim. The user rules on each case; in the book the class argues it out.
- **Reconstructed proofs:** when the user has no argument and accepts lemmas the assistant reconstructs, the assistant writes the proof it attacks, that is, it argues both sides. The skill says so and asks for the user's argument first.
- **Monster-barring:** Rule 2 forbids it. The skill names any narrowing of a term against a case that meets the claim as first read, whether or not the user calls it a change, and accepts it only as an explicit definition change, with the lost content stated and the departure from Rule 2 named.
- **Ruling classes:** invalid, concept-stretching, monster-barring and disputed are the skill's own classification of the user's rulings. "Disputed" (a bare denial, neither dropped nor counted) applies the repository's rule that a finding is withdrawn only when its defect can be named.
- **Popper's prior refutation criterion; an addition to Lakatos.** For a claim that rests on observation, the skill asks in advance what would count against it. Popper: "criteria of refutation have to be laid down beforehand: it must be agreed which observable situations, if actually observed, mean that the theory is refuted" (*Conjectures and Refutations* 38 n.3, via SEP "Karl Popper"). Lakatos himself "flatly denies that there are critical tests, in the Popperian sense" (same entry), so this is not his method.
- **One case per message, a three-round cap, fixed result values and the record** are the skill's own. A "holding" result means holding against the cases tried, never proved.

## 6. Why each case carries its check, and why rounds are capped

The reason is a risk finding, not support for the method. In *The Counterexample Game* (Drucker and Mahowald, 2026), one model instance proposed counterexamples to a definition, another repaired it, and the loop repeated:

- on a sample of 60 counterexamples, five human raters together judged 32% valid, while the model judge rated 60% valid; the judge accepts roughly twice as many as humans do;
- validity fell from 69% to 17-30% over a chain of counterexamples and repairs, as rated by the model; the authors say these figures are "probably best read as upper bounds";
- repairs became "a laundry list of exceptions", which is exception-barring.

The setup was model against model, on definitions, with no human in the loop. So the skill asks the user to rule on every case, shows the check that lets the user fault it, raises one case at a time, offers to stop after three rounds, and makes a repair forced by an unverified case conditional. No study has tested this method with users; studies of AI that asks questions or plays devil's advocate (Danry et al.; Chiang et al.) used different setups and are distant analogues at best.

## 7. Lineage and neighbours

- SEP: Lakatos thought "Hegelian language" could describe the growth of mathematics (*Proofs and Refutations*, p. 146). IEP: "Lakatos extended the range of critical rationalism into mathematics".
- Pease et al. formalised the same moves as a dialogue game.
- **dia-reductio:** one global counterexample to "all X are Y" is also a refute run there ("all X are Y" contradicts "some X is not Y"), and its narrowed thesis is exception-barring in Lakatos's terms. This skill adds local counterexamples, proof-analysis and repair over several rounds.
- **dia-elenchus:** its too-broad and too-narrow tests are counterexamples to a definition. When the dispute becomes what a word means, it goes there.
- **dia-warrant:** a claim that holds only generally or usually is defeasible; one counterexample is a rebuttal condition for it, not a refutation.
- **dia-negative:** a policy or plan judged against its own standard goes there; its "narrow C to the scope where it holds" is exception-barring in Lakatos's terms.

## Sources

- "Imre Lakatos", *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/lakatos
- "Karl Popper", *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/popper
- "Karl Popper: Critical Rationalism", *Internet Encyclopedia of Philosophy*. https://iep.utm.edu/karl-popper-critical-ratiotionalism
- I. Lakatos, "Proofs and Refutations (I)", *BJPS* 14 (53), 1963 (scan). https://m-u-l-t-i-p-l-i-c-i-t-y.org/media/pdf/Proofs-and-Refutations.pdf
- I. Lakatos, *Proofs and Refutations*, ed. J. Worrall and E. Zahar (Cambridge University Press), front matter and contents. https://assets.cambridge.org/97811071/13466/frontmatter/9781107113466_frontmatter.pdf
- K. Easwaran, "Rebutting and Undercutting in Mathematics", *Philosophical Perspectives* 29 (2015). https://www.kennyeaswaran.org/papers/rebutting-undercutting-math.pdf
- D. Drucker and K. Mahowald, *The Counterexample Game: Iterated Conceptual Analysis and Repair in Language Models* (arXiv:2605.03936, 2026). https://arxiv.org/html/2605.03936
- A. Pease et al., "Lakatos-style collaborative mathematics through dialectical, structured and abstract argumentation", *Artificial Intelligence* 246 (2017). https://www.pure.ed.ac.uk/ws/portalfiles/portal/33001190/pease_et_al_aij_1.pdf
- V. Danry et al., "Don't Just Tell Me, Ask Me" (CHI 2023). https://www.media.mit.edu/publications/don-t-just-tell-me-ask-me-ai-systems-that-intelligently-frame-explanations-as-questions-improve-human-logical-discernment-accuracy
- C.-W. Chiang et al., "Enhancing AI-Assisted Group Decision Making through LLM-Powered Devil's Advocate" (IUI 2024). https://dl.acm.org/doi/fullHtml/10.1145/3640543.3645199
