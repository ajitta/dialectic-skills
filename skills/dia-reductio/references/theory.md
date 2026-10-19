# Reductio ad absurdum: theory reference

Read this when the user asks about the method, or when you are unsure whether a step is strict. Sources are listed at the end; everything here is paraphrased from them unless quoted.

## 1. What it is

Reductio is refutation by consequences: you show that accepting a claim leads to an untenable result, so the claim (or something it was combined with) must be rejected. The name traces to the Greek phrase Aristotle uses repeatedly in the *Prior Analytics*, "reduction to the impossible" (IEP, Rescher).

Rescher distinguishes three kinds of untenable result:

1. a self-contradiction (*ad absurdum* in the strict sense)
2. a falsehood (*ad falsum*)
3. an implausibility or anomaly (*ad ridiculum*, *ad incommodum*)

Logicians and mathematicians usually mean the first. The other two are looser, attenuated uses (IEP).

**This skill allows only the first.** A falsehood or an implausibility becomes usable only after its negation is written into the premise list as an explicit premise. Then the contradiction is strict again, and the user can see exactly which premise it depends on and reject it if they want.

## 2. The logical form

From the set {assumption + already accepted premises} derive a contradiction, then reject the assumption by modus tollens (IEP). The propositional core: if p yields not-p, then not-p.

Two directions:

- **Refutation:** assume A, derive a contradiction, conclude not-A. This is valid in classical and intuitionistic logic alike.
- **Indirect proof:** assume not-A, derive a contradiction, conclude A. This is valid in classical logic but not in intuitionistic logic (Encyclopedia of Mathematics), where reductio proves only negative statements because not-not-A does not imply A in general (SEP, "Intuitionistic Logic"); it does when A is itself a negation. The intuitionist objection bites hardest on existence claims: refuting "nothing is F" does not, for them, show that something is F unless an instance is produced (IEP).

So when the skill proves T by refuting not-T and T is not itself a negation, note that the conclusion relies on classical logic, above all when T says something exists.

## 3. Which premise goes

When a set of statements is collectively inconsistent, the reductio shows that they cannot all hold together (IEP, section on "doctrinal annihilation"). Which member to give up is not settled by logic alone; that point comes from Duhem and Quine, not from the IEP entry, and this skill holds classical logic itself fixed. Choosing which to give up is a further judgment about which premises are best supported. That is why the skill presents options and a recommendation instead of a verdict, unless every other premise is a law of logic or mathematics.

## 4. What reductio can be applied to

Rescher lists propositions, sets of propositions (doctrines), modes of reasoning, definitions, instructions and rules of procedure, and practices and policies (IEP). Examples from the entry:

- A self-defeating instruction: "Never say never."
- An unsatisfiable definition: a bird defined as a vertebrate that flies, together with the ostrich as a flightless bird.
- A rule that self-destructs when applied across the board: a will letting the sister pick "any three" valuables, read so that she could take the house, bank account and business and leave the daughter nothing.
- Kant's universalizability test treats maxims like lying as self-defeating when generalized (IEP's reading).

Applying reductio to a rule or practice still needs a strict contradiction in this skill: the rule's own stated aim or another stated rule must be written as a premise, and the generalized application must contradict it.

## 5. Classic example

The incommensurability of a square's diagonal with its side: assume d/s = n/m in lowest terms; d² = 2s² gives n² = 2m², so n is even; then m is even too, contradicting "lowest terms" (IEP, after Heath). This is the model of a strict reductio: every step is a rule of arithmetic or logic, and the contradiction is explicit.

## 6. Reductio and per impossibile reasoning

Both start from a supposition that conflicts with known facts. Reductio aims to reject the supposition. *Per impossibile* reasoning keeps the impossible supposition in order to study what follows from it, as in "if, per impossibile, there were finitely many primes, there would be a largest prime" (IEP). The difference is in the goal, not the inference. If the user is exploring consequences rather than testing a claim, say that this is per impossibile reasoning and that no refutation is being claimed.

## 7. History in dialogue

Plato used reductio dialectically (IEP cites *Republic* I, 338c–343a and *Parmenides* 128d). Socrates' defence in the *Apology* (27b–e) is a reductio on his accusers: they say he does not believe in gods yet believes in divine beings, and a divine being presupposes gods (Aristotle, *Rhetoric* II.23, uses the same argument). It is not a model of strictness: Socrates takes one premise from Meletus' silence ("your silence gives consent"). Kant's antinomies in the *Critique of Pure Reason* rest on reductio arguments (IEP).

## 8. Failure modes to watch

- **Loose absurdity:** a bad or unlikely outcome treated as a contradiction.
- **Hidden premise:** the contradiction comes from something the target never said and the premise list did not include.
- **Equivocation:** a term changes meaning between steps.
- **Strawman:** a weak reading of the thesis is refuted.
- **Slippery slope:** a chain of "would lead to" claims, each a causal prediction, presented as deduction.
- **Over-claiming:** "the thesis is false" when only the set's inconsistency was shown.

## 9. Hard cases

- **A local reductio is not an indirect proof.** Euclid's proof that there are infinitely many primes (*Elements* IX.20) is often retold as a proof by contradiction, but it is direct: from any finite list of primes it constructs another. Only one sub-step ("If possible, let it be so … which is absurd") is a reductio, a negation-introduction step (Joyce; Hardy and Woodgold).
- **A premise that looks like mathematics can be false.** On one reconstruction, Zeno's argument that the parts of a body make it "so large as to be unlimited" assumes that an infinite sum of finite quantities must be infinite; some such sums are finite (SEP, "Zeno's Paradoxes"). A mathematical-sounding premise is [L] only if it is a theorem; otherwise it is [T] if the target stated it (quote it) and [A] if you supplied it, as Zeno's premise is on this reconstruction.
- **Paradoxes.** For a paradox such as the Liar, the classical result is "premise set inconsistent". Dialetheists hold that some such contradictions are true, and paraconsistent logics keep a contradiction from implying everything (SEP); this skill holds classical logic fixed.

## Sources

- Nicholas Rescher, "Reductio ad Absurdum", *Internet Encyclopedia of Philosophy*. https://iep.utm.edu/reductio/
- "Reductio ad absurdum", *Encyclopedia of Mathematics*. https://encyclopediaofmath.org/wiki/Reductio_ad_absurdum
- "Underdetermination of Scientific Theory", *Stanford Encyclopedia of Philosophy* (Duhem's and Quine's holism). https://plato.stanford.edu/entries/scientific-underdetermination/
- W. V. O. Quine, "Two Dogmas of Empiricism" (1951), §6. https://www.ditext.com/quine/quine.html
- "Intuitionistic Logic", *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/logic-intuitionistic/
- Plato, *Apology*, tr. B. Jowett (Project Gutenberg). https://www.gutenberg.org/files/1656/1656-h/1656-h.htm
- Euclid, *Elements* IX.20, tr. and commentary D. E. Joyce. https://mathcs.clarku.edu/~djoyce/java/elements/bookIX/propIX20.html
- M. Hardy and C. Woodgold, "Prime Simplicity", *Mathematical Intelligencer* 31 (2009). https://link.springer.com/article/10.1007/s00283-009-9064-8
- "Zeno's Paradoxes", *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/paradox-zeno/
- "Dialetheism" and "Paraconsistent Logic", *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/dialetheism/ ; https://plato.stanford.edu/entries/logic-paraconsistent/
- Aristotle, *Rhetoric* II.23, 1398a (topic from definition: the divine is a god or the work of a god); pointed to by IEP.
