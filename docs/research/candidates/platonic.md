# Candidates: the Socratic-Platonic remainder and Aristotle's dialectic

Proposals only, written 2026-10-21 against `main` at `becc4b3`. The question is which methods from Plato's later dialogues and Aristotle's *Topics* and *Sophistical Refutations* would make new `dia` skills beyond the seven. They are judged on fidelity to the named method and on fit for a chat between one user and one AI assistant (owner clarification, 2026-10-21). Plato is cited by Stephanus page from the Perseus Loeb translations (Fowler, Lamb, Shorey), Aristotle by chapter from the Pickard-Cambridge and Ross translations in the Internet Classics Archive. Every `[n]` is a page that was fetched; claims I could not source are marked `[unverified]`.

## 1. Scope

Covered:

- **A. Maieutics as a standalone method** (Theaetetus 148e–151d, 157c–d, 160e, 210b–d). Covered because the brief asked for it; it is mostly absorbed by dia-elenchus already.
- **B. Method of hypothesis** (Meno 86e–89e, Phaedo 99d–101e, Republic VI 510b–511d). Covered.
- **C. Collection and division** (Phaedrus 265d–266c, 277b; Sophist 219a–e, 253d–e; Statesman 262a–263e, 285a–b, 287c). Covered.
- **D. Aristotle's dialectic in the Topics** (gymnastic question and answer, endoxa, the peirastic examination, plus the endoxic review of Nicomachean Ethics VII.1). Covered.
- **E. Fallacy diagnosis after the Sophistical Refutations.** Covered.

Dropped:

- **The "cathartic" cross-examination of Sophist 230b–d.** It is the elenchus described from outside, and dia-elenchus covers it. It is cited here only as evidence: it describes refuting by collecting a person's opinions and showing "that they contradict one another".[15]
- **Recollection by questioning (Meno 82b–85d).** It is tutoring toward an answer the questioner already knows. Vendor study modes already do this, and the elenchus research put it out of scope.
- **The Parmenides' hypothetical exercise (135c–137b) and the Philebus division into a definite number (16c–17a).** I did not fetch them `[unverified]`. They overlap B and C and add no step a chat skill could run.
- **The Republic VII dialectician's ascent.** It needs the unhypothetical first principle, which no chat can reach; see B.

Section 6 is the Sources list.

## 2. Candidates

### A. Maieutics (the Theaetetus midwife)

**The method in the source.** Theaetetus cannot define knowledge but "cannot get rid of a feeling of concern", and Socrates diagnoses "the pangs of labor ... because you are not empty, but pregnant".[1] Midwives know "who are pregnant and who are not" and can arouse or soothe the pangs.[2] Socrates' art differs from theirs because his patients bring forth "at one time real children and at another mere images", and its greatest part is to "test in every way" which is which. He is "sterile in point of wisdom", and his associates progress "not because they have ever learned anything from me, but because they have found in themselves many fair things".[50]

Two further points matter for a skill:

- Those who are not pregnant he hands over "as match-maker" to Prodicus and others.[3]
- The respondent is warned not to "bite" when a notion is taken away.[3]

**Procedure as the text gives it.**

1. Diagnose pregnancy: the person is perplexed but not empty.[1]
2. If they are not pregnant, refer them elsewhere.[3]
3. Ask them to "answer the questions I ask as I ask them" and to say what X is.[3]
4. Deliver the offspring ("knowledge is nothing else than perception").[3]
5. Develop it. Socrates gives "a taste of each of the philosophical theories ... until I may help to bring your own opinion to light", claiming none as his own.[25] He links the offspring to Protagoras and Heraclitus and calls the result "your new-born child and the result of my midwifery".[26]
6. Test it by "running round with it in a circle" to see whether it is "a wind-egg".[26]
7. Discard what fails, kindly.[3]
8. End. All the offspring are "wind-eggs", but the respondent will be "pregnant with better thoughts" or "gentler", not thinking he knows what he does not.[4]

The SEP calls this "one of the most detailed descriptions of the Socratic maieutic method". It notes that reading the passage as alluding to recollection is disputed.[30]

**Fidelity in chat.** High for steps 1–4 and 6–8, which are what dia-elenchus already does under the midwife image. Step 5 is where a standalone skill would differ: the midwife may offer others' theories, labelled as not his, to help the respondent's view take shape. dia-elenchus is deliberately stricter here and hands over nothing (its theory.md §2). A faithful maieutic skill would therefore loosen a rule the owner chose. Multi-turn, one question at a time. It needs the user's own attempts. It runs without tools.

**Roles and AI risks.** *Roles.* The assistant is the midwife; the user is the one in labour. *Inventing premises or sources.* Step 5 is the risky one. "A taste of the theories of the wise" from recall can invent attributions, or plant the model's own idea under a sage's name, which is advisor drift in another form. *Yielding under pushback.* The method counters it: the midwife takes away wind-eggs despite anger.[3] It still needs the sibling rule that a step is withdrawn only when its defect can be named. *Over-reliance.* Low, because the user produces every offspring. *Human-AI evidence for the stance.* In a field experiment with nearly a thousand students, GPT-4 access without guardrails raised practice grades 48% but cut later unaided grades by 17%. A tutor prompted to withhold answers "largely mitigated" this.[40] AI-framed questions improved users' discernment of logically flawed statements more than causal explanations did.[45] *Name-only LLM work.* "Maieutic prompting" builds a tree of the model's own explanations and solves for consistency with a SAT solver.[32] It uses the name, not the dialogue, and needs code.

**Overlap.** dia-elenchus: high; it already runs the midwife, the wind-egg test and the aporia ending. dia-brainstorm: partial; it borrows "the user owns the idea" and labels its departure from the midwife. dia-reductio, dia-negative, dia-refine, dia-iterate, dia-confirm: none.

**Routing risk.** High. "Draw it out of me" and "be my midwife" would compete with dia-elenchus and dia-brainstorm for the Socratic requests that D21 and D22 just settled.

### B. The method of hypothesis (Meno, Phaedo, Republic VI)

**The method in the source.**

- **Meno.** Meno insists on asking whether virtue can be taught before what it is, so Socrates examines it "by means of hypothesis ... what the geometricians often do".[5] The geometer says, "if this area is such that ... then I take it you have one consequence, and if it is impossible ..., then some other".[6] The hypothesis is "what kind of thing must virtue be ... so as to be teachable or not?". "If virtue is a kind of knowledge, clearly it must be taught", so the question becomes "whether virtue is knowledge". That is then supported from "our hypothesis ... that it is good".[6]
- **Meno 89c–e, the turn.** Meno says the matter "seemed to be a correct statement a moment ago". Socrates replies that it must seem correct "not only a moment ago ... but now also and hereafter", and tests a consequence: if virtue is teachable there must be teachers of it, and he "cannot find one".[42]
- **Phaedo.** After his "second voyage" to "conceptions",[43] Socrates assumes "in each case some principle which I consider strongest". Whatever agrees with it he regards as true, and whatever disagrees as untrue.[7] The rules: if the principle is attacked, do not reply "until you had examined the consequences to see whether they agreed with one another or not". To justify it, assume "some other principle which seemed to you the best of the higher ones ... until you reached one which was adequate". Do not "mix things up, as disputants do, in talking about the beginning and its consequences".[8]
- **The SEP on the Phaedo.** "Agreement" there "is not a notion of entailment". The test is whether cases in the domain are "not adequately explained by" the hypothesis. How the Phaedo method connects to the Republic's is "a subject of controversy".[28]
- **Republic VI.** The geometers "postulate the odd and the even ... and do not deign to render any further account of them".[9] Dialectic instead treats assumptions "literally as hypotheses ... springboards", in order "to rise to that which requires no assumption", and then descends "making no use whatever of any object of sense".[10]

**Procedure (Benson's reconstruction, which fits the fetched texts).**

1. Proof stage, 1a: find a hypothesis H from which the answer to Q can be derived.
2. Proof stage, 1b: show that H entails the answer.
3. Confirmation stage, 2a: derive H from a higher hypothesis, "until one reaches 'something adequate'".
4. Confirmation stage, 2b: test whether H's consequences "agree with one another".[31]

Benson also contrasts the two methods: the elenchus is "essentially ad hominem", testing the interlocutor's beliefs, whereas the method of hypothesis "is precisely not ad hominem".[31]

**Fidelity in chat.** Medium-high for the Meno and Phaedo form. Two elements are not achievable and must carry an honest label:

- The Republic's ascent to an "unhypothetical first principle" and its reasoning "through ideas" alone.[10]
- The Phaedo's metaphysical content (Forms as causes).[7]

"Something adequate" has to be read as adequate to both parties: a premise the user accepts and that is not itself in question.

**Turns and needs.** The proof stage fits one pass. The confirmation stage needs the user's assent at each step up and facts for each test downward. The Meno's downward test was an observation (no teachers of virtue[42]), which in chat must come from the user or a tool. It runs without tools, with facts graded by evidence class as dia-reductio does.

**Roles and AI risks.** *Roles.* In the Meno, Socrates proposes the hypothesis and Meno assents.[6] In chat the assistant is the geometer and proposes candidate hypotheses with their rival branch ("if H, one answer; if not-H, another"[6]). The user decides whether H is acceptable and supplies the facts for the downward test. *Inventing premises or sources.* The model may invent a convenient H, or a fact that "confirms" it. Counter: every H is labelled as the assistant's proposal, its rival branch is always shown, and a downward test that rests on recall is marked unverified. *Yielding under pushback.* The method has a built-in check: agreement "a moment ago" is not enough, and H must still hold "hereafter".[42] Insisting on H, or dropping it, then needs a named consequence, not pressure. "Are you sure?" challenges flipped answers 46% of the time, with a 17% average accuracy drop,[38] and sycophancy is "a general behavior" of assistants.[39] So the skill must say that only a named consequence or a user-supplied fact moves H's status. *Over-reliance.* The output is conditional ("A holds if H"), so the open decision about H stays with the user. That mirrors cognitive-forcing designs, which reduced over-reliance on AI advice, though users rated them least favourably.[46] *One model playing both sides.* Not needed. *Human-AI evidence.* None for this method. The nearest LLM work is model-internal: recursive sub-questions ("Socratic Questioning")[35] and abductive explanation trees.[32]

**Overlap.** dia-elenchus: partial. Its patterns file already has the Meno 86e–87b move as a single premise question ("If X were [condition], what would follow?"), but no proof or confirmation stage. dia-reductio: partial. It derives consequences and, when no contradiction is found, "names the premise that would decide it". The method of hypothesis starts from that premise, and its test is agreement, not contradiction. dia-brainstorm: partial; its assumption probe "what must be true for this to work". dia-confirm: minimal; it treats explanations as hypotheses. dia-negative, dia-refine, dia-iterate: none.

**Routing risk.** Medium, toward dia-reductio ("assume it's true and show where it breaks"). The description must say "when a question can't be settled directly, find what it depends on", and send contradiction-finding to dia-reductio.

### C. Collection and division (Phaedrus, Sophist, Statesman)

**The method in the source.**

- **Phaedrus.** Two principles: "bringing together in one idea the scattered particulars, that one may make clear by definition", and "dividing things again by classes, where the natural joints are, and not trying to break any part, after the manner of a bad carver".[11] Socrates calls those able to do this "dialecticians".[12] The art requires defining each thing and dividing "by classes until further division is impossible".[13]
- **Sophist.** The angler is the paradigm: art is divided into productive and acquisitive, acquisitive into exchange and coercive, coercive into fighting and hunting, and so on, with the respondent assenting at each cut ("Agreed"; "It appears so, at any rate, from what you have said").[14] Dialectic is "the division of things by classes and the avoidance of the belief that the same class is another, or another the same".[16]
- **SEP on the Sophist.** The sophist "turns up all over the tree" in six divisions. The Stranger reads the many names as a sign that the "appearance is not sound", because the one feature has not been seen (Sophist 232a).[29]
- **Statesman 262–263.** "The part must be also a species". "It is safer to proceed by cutting through the middle". Splitting "Hellenic" from all others called "barbarian" is the error, and the remedy is "odd and even", "male and female".[17] "When there is a class of anything, it must necessarily be a part ..., but there is no necessity that a part be also a class", and a crane could equally oppose cranes to all other animals.[18]
- **Statesman 285, 287.** The two-way rule: whoever first sees "the unity ... must not give up until he sees all the differences". Conversely, among dissimilarities one must not stop "until he has gathered into one circle of similarity" the related things.[19] When bisection fails, "divide them ... like an animal that is sacrificed, by joints ... as near two as possible".[20]
- **Aristotle's critique.** He holds that division "cannot actually prove anything but rather assumes the very thing it is supposed to be proving" (Prior Analytics I.31, per the SEP).[27]

**Procedure.**

1. Agree what the name refers to.[29]
2. Collect the cases under one kind.[11][19]
3. Place the target in the widest relevant kind.[14]
4. Cut into two kinds (or into as few as the joints allow), each side a real kind and not a remainder held together only by a name.[17][18][20]
5. Choose the side the target falls on and repeat until no further cut is possible.[13]
6. Read the definition off the path.[29]
7. If the target turns up under several branches, collect again: what one feature explains all of them?[29]

**Fidelity in chat.** Medium. The procedural rules (each part a kind, no "barbarian" remainder, cut through the middle, divide in both directions) can be followed exactly. "Natural joints" presupposes real kinds, so the skill must be labelled: it cuts the user's concept into kinds the user accepts and claims no natural kinds. It must also carry Aristotle's caveat: each cut is an assertion to be agreed, not a proof.[27]

**Turns, needs, tools.** Multi-turn if every cut is agreed, as in the dialogues; it could also show a one-pass tree for the user to correct. It needs the user's domain knowledge for which cases fall where. It runs without tools.

**Roles and AI risks.** *Roles.* In the Sophist the Stranger cuts and the respondent assents.[14] In the Statesman the respondent makes a cut and the Stranger corrects it.[17] The second pattern fits AI chat better. The user proposes each cut; the assistant tests it against the Statesman rules and proposes a cut only when asked, labelled as its own. *Inventing premises.* A model-led tree invites the user to assent to the model's taxonomy (the respondent's "It appears so, at any rate, from what you have said"[14]), and the model may invent kinds or cases. Taxonomy induction with LLMs needed an "Ensemble-based Ranking Filter to reduce the hallucinated content generated at each iteration".[36] *Over-reliance.* Worse under the Sophist pattern, better under the Statesman pattern. *Yielding under pushback.* A cut the user rejects is simply re-cut, which is the method's normal path, so yielding is low-stakes here. The rules themselves must not be dropped under pressure. *Human-AI evidence.* None found.

**Overlap.** dia-elenchus: partial. Both seek "what is X"; elenchus refutes the user's definition, division builds one cut by cut. dia-negative: partial; what a classification leaves out. dia-brainstorm: partial; its "definition pressure" tactic. dia-reductio, dia-refine, dia-iterate, dia-confirm: none.

**Routing risk.** Medium-high. "Define X" competes with dia-elenchus ("make me define it first"), and "make a taxonomy" is a make-something request, the D34 failure in another form.

### D. Aristotle's dialectic in the Topics (gymnastic, endoxa, peirastic)

**The method in the source.**

- **Topics I.1–2.** Dialectical reasoning "reasons from opinions that are generally accepted".[21] It is useful for "intellectual training, casual encounters, and the philosophical sciences". For the last, "the ability to raise searching difficulties on both sides of a subject will make us detect more easily the truth and error".[21]
- **Topics I.10, I.14.** A dialectical proposition is "held by all men or by most men or by the philosophers".[21] Propositions are selected from those opinions, from opinions "in accordance with the arts", and "from the written handbooks".[21]
- **Topics VIII.4–5.** The questioner tries to make the answerer "utter the most extravagant paradoxes that necessarily follow because of his position". The answerer should grant views "more generally accepted" than the questioner's conclusion. If the thesis is the answerer's own, "the standard ... is himself"; if he defends another's, "the latter's judgement".[22]
- **Topics VIII.14.** Train by "converting" arguments and by looking "for a line of argument both pro and con"; "if we cannot find any one else to argue with, we should argue with ourselves".[22]
- **SEP reconstruction (not universally accepted).** The questioner asks yes/no questions to secure concessions from which a contradiction follows, with "judges or scorekeepers".[27]
- **The peirastic examination.** "Examination-arguments" reason "from premisses which are accepted by the answerer and which any one who pretends to possess knowledge of the subject is bound to know".[23] The art "has in view not the man who has knowledge, but the ignorant pretender". It can be held by "one without knowledge", and "everybody, including even amateurs, makes use in a way of dialectic and the practice of examining".[24] The SEP calls it "strongly reminiscent of Socrates' style of interrogation, from which it is almost certainly descended".[27]
- **Diaporia.** Nicomachean Ethics VII.1: "set the observed facts before us and, after first discussing the difficulties, go on to prove ... the truth of all the common opinions ... or, failing this, of the greater number and the most authoritative".[44] The SEP calls this review a *diaporia*, "a 'puzzling through'".[27]

**Fidelity in chat.**

- *Gymnastic exchange:* high. The yes/no format is explicit and fits a phone.
- *Peirastic test:* high, and it is close to Vlastos's elenchus (dia-elenchus research §2.3).
- *Endoxa:* low without tools. "What most people or the wise hold" would come from model recall, which is exactly the invented-sources risk. With a search tool it is feasible.
- *Diaporia:* a solo review with no second party, so the model plays both sides.

**Roles and AI risks.** *Gymnastic, assistant as questioner.* The user defends a thesis and the assistant asks yes/no questions. This is the elenchus minus the sincerity rule, since the Topics allows answering for another's position.[22] *Gymnastic, user as questioner.* The user practises questioning and the assistant answers as a declared role. The model then also keeps score, so it is player and judge at once. Multi-agent debate work found that "LLMs might not be a fair judge", and that self-reflection suffers "Degeneration-of-Thought".[48] *Peirastic test of the assistant.* The user examines the assistant's claimed knowledge, a non-expert testing an expert,[24] which is the best fit for over-reliance. But the skill text would have the model write the questions it must answer, so the model again plays both sides. *Yielding under pushback.* In the gymnastic game the answerer is supposed to hold the thesis, so yielding is a role violation. Sycophancy pulls the model either way.[39] *Human-AI evidence.* LLM devil's advocates arguing against the AI's own recommendation "have the potential to promote groups' appropriate reliance on AI".[49]

**Overlap.** dia-elenchus: high; the peirastic test and the gymnastic contradiction-hunt. dia-reductio: high; contradiction from concessions; Topics VIII.14 "conversion" is a reductio. dia-brainstorm: partial; its "viewpoints" probes. dia-negative, dia-refine, dia-iterate, dia-confirm: none.

**Routing risk.** High for "test me / argue with me", which already goes to dia-elenchus. Low for "practise debating".

### E. Fallacy diagnosis (On Sophistical Refutations)

**The method in the source.**

- **The four kinds of argument (SE 2).** "Didactic, Dialectical, Examination-arguments, and Contentious"; contentious arguments "reason or appear to reason ... from premisses that appear to be generally accepted but are not so".[23]
- **SE 1.** A refutation is "reasoning involving the contradictory of the given conclusion"; sophistical ones only appear to be refutations.[23]
- **SE 4: six fallacies that depend on language.** Ambiguity, amphiboly, combination, division of words, accent, form of expression.[23]
- **SE 4: seven outside language.** Accident; the absolute versus the qualified use of an expression; ignorance of what "refutation" is; the consequent; assuming the original conclusion; stating as cause what is not the cause; "the making of more than one question into one".[23]
- **SE 6.** All of them can be analysed "into breaches of the definition of a refutation": first check whether the argument is "inconclusive", then "take the definition bit by bit".[23]
- **The solution (Topics VIII.10).** "Demolish the point on which the fallacy ... depends": "the demolition of any random point is no solution, even though the point demolished be false".[22] Topics I.18: knowing the senses of a term keeps answerer and questioner "directing their minds upon the same thing".[21]
- **SE 16–17.** The study helps one see "in how many senses any term is used", and helps in "one's own personal researches". Against contentious arguers, the aim is to "dispel the appearance" of refutation.[24]
- **Scholarship.** The SEP adds a second type: valid arguments whose premises "seem to be acceptable" but are not ("you still have horns").[27] It reports Hamblin's view that "a dialectical framework is indispensable" for Aristotle's fallacies.[41]

**Procedure.**

1. Lay out the argument as conceded premises, the conclusion and the thesis it claims to overturn.
2. Check the definition of refutation part by part: does the conclusion follow, and is it the contradictory of the thesis?[23]
3. If it fails, locate the cause, in language (test each key term for two senses[21]) or outside it, and name the type.[23]
4. Check the premises' acceptability (the horns case).[27]
5. Give the solution: the one point on which the appearance depends, not merely some false premise.[22]

**Fidelity in chat.** High. The thirteen types, the definition test and the solution rule can be followed as written. Departures to label:

- Applying the method to any argument, not only to refutations in a question-and-answer contest.
- Modern fallacy names (straw man, slippery slope and the like) are later additions. Their mapping onto Aristotle's thirteen is mine `[unverified]` and should be shown as such, or they should be left out.

**Turns, needs, tools.** One pass. It needs the argument, quoted. It runs without tools.

**Roles and AI risks.** *Roles.* The assistant is the "solver" of SE 16 onward.[24] The argument may be the user's, a third party's or the assistant's own. The user judges the diagnosis. *Inventing premises.* Rule: a diagnosis must show its defect (the two senses side by side, the missing premise, the two questions fused into one), never just a label. Fallacy labelling is subjective, and humans outperform GPT-3.5 on it.[34] Earlier LLMs "perform poorly" at it,[33] and their reasoning suffers from not understanding fallacies.[37] *Yielding under pushback.* LLMs in multi-round debate are "erroneously convinced 41% and 69% more often" (GPT-3.5, GPT-4) by fallacious arguments than by logical ones.[47] When the user argues back, the skill should run the same diagnosis on the rebuttal and withdraw a finding only when its defect can be named, as the siblings do (research README, theme 2). *Over-reliance.* The single-point solution rule makes each finding checkable by the user. AI-framed questions improved human discernment of logically flawed statements more than explanations from an always-correct AI did.[45] An optional "ask first" mode (which point does this depend on?) has direct support. *One model playing both sides.* Not needed.

**Overlap.** dia-reductio: partial. Its rules already cover equivocation (one sense per term), hidden premises, contraries versus contradictories, loose absurdity and slippery slopes, but it builds a contradiction and does not diagnose someone else's argument. dia-refine: partial; "logical leaps" in the assistant's own draft. dia-negative: minimal. dia-elenchus, dia-brainstorm, dia-iterate, dia-confirm: none.

**Routing risk.** Medium, toward dia-reductio ("follows from its premises"). Requests such as "what's wrong with this argument" or "is this a fallacy" belong to no sibling today, which is a gap and not a conflict. The dia-reductio description would need a cross-reference.

## 3. Comparison

| Candidate | Fidelity achievable | Fit for AI chat | Overlap | User value | Recommendation |
|---|---|---|---|---|---|
| A. Maieutics | high, except step 5 | medium-high | high (dia-elenchus) | low beyond dia-elenchus | **SKIP**: dia-elenchus already is the maieutic test; the only new step (offering others' theories) loosens an owner rule and invites invented attributions. |
| B. Method of hypothesis | medium-high (Meno/Phaedo; Republic ascent labelled out) | high | partial (dia-reductio, dia-elenchus patterns) | high: turns "can't answer Q" into "A if H", and H is testable | **ADD** as a new skill: no sibling has the proof and confirmation stages, and the conditional output keeps the decision with the user. |
| C. Collection and division | medium (procedure yes, "natural joints" no) | medium (high only if user-led) | partial (dia-elenchus) | medium: definitions and classifications | **ADD later**, user-led cuts only: real gap, but routing toward dia-elenchus and "make a taxonomy" needs probes first. |
| D. Topics dialectic | high (gymnastic, peirastic); low (endoxa without tools) | low-medium (player and judge at once; endoxa from recall) | high (dia-elenchus, dia-reductio) | medium (debate practice) | **SKIP** for now; **FOLD** at most one line into dia-elenchus theory.md, crediting the peirastic examination (SE 2, 11). |
| E. Fallacy diagnosis (SE) | high | high | partial (dia-reductio, dia-refine) | high: a common request no sibling owns | **ADD** as a new skill: a one-pass, checkable diagnosis with direct human-AI evidence for its question form. |

## 4. Ranked recommendation

**1. `dia-fallacy`.**

- *Honest label:* "Fallacy diagnosis after Aristotle's On Sophistical Refutations: his thirteen sources of apparent refutation and his rule that the solution names the one point the appearance depends on, applied to any argument and not only to refutations in a question-and-answer contest; modern fallacy names are later additions, marked as such."
- *Steps:* (1) Quote the argument and lay it out as premises, conclusion, and the thesis it claims to overturn (if any). (2) Test it against the definition of a deduction or refutation, part by part. (3) For each failure, name the type (language: show the two senses or groupings side by side; outside language: show the accident, the dropped qualification, the converted consequent, the assumed conclusion, the false cause or the fused questions). (4) Check whether a premise only appears acceptable. (5) Give the solution: the one point to demolish. (6) Close with a record: argument, verdict (genuine / apparent: type / valid but premise only apparently acceptable / no defect found), solution and what was not checked. (7) Optional "ask first" mode: ask the user which point the argument depends on before showing the solution.
- *Stop rule:* one pass. A follow-up dispute reruns step 2 or 3 on the disputed finding, including on the user's rebuttal.
- *Never:* label without showing the defect; call a conclusion false because the argument for it fails; withdraw a finding without naming its defect; invent the argument's premises (an unstated premise is marked as added); treat "no defect found" as "true".

**2. `dia-hypothesis`.**

- *Honest label:* "The method of hypothesis of Plato's Meno and Phaedo, in Benson's two-stage reconstruction; not the Republic's ascent to an unhypothetical first principle, and without its metaphysics."
- *Steps:* (1) State the question Q and why it cannot be settled directly. (2) Propose one to three candidate hypotheses H, labelled as the assistant's unless the user named them, each with its rival branch ("if H then A; if not-H then B"). (3) Show the derivation from H to the answer. (4) Upward: what H rests on, stopping at a premise the user accepts and that is not itself in question. (5) Downward: H's consequences, checked against each other and against facts, each with its evidence class (tool / supplied by the user / unverified recall). (6) Verdict: Q's answer holds if H. H's status is exactly one of: supported, doubtful (a consequence conflicts), or untested. (7) Record.
- *Stop rule:* one pass, then the user decides about H. A follow-up reruns only the stage the user changed.
- *Never:* present the conditional answer as unconditional; mix arguments about H with arguments from H (Phaedo 101e[8]); count recall as confirmation; change H's status without a named consequence or a supplied fact.

**3. `dia-division` (after routing probes).**

- *Honest label:* "Collection and division after Plato's Phaedrus, Sophist and Statesman, applied to the user's concept; the cuts are kinds the user accepts, not claims about natural kinds, and, as Aristotle objected, each cut is agreed, not proved."
- *Steps:* (1) Agree what the name covers and collect the cases. (2) Ask the user to name the widest kind and the first cut. (3) Test each cut: both sides kinds? no remainder held together only by a name? near the middle? cases left over? (4) Repeat one cut per message until no further cut is possible. (5) Read off the definition. (6) If the target appears under several branches, ask what single feature unites them. (7) Record the tree.
- *Stop rule:* no further cut, or the user stops.
- *Never:* make a cut the user did not ask for without labelling it as the assistant's; invent cases; call the result "the" definition.

## 5. Open questions for the owner

1. Should `dia-fallacy` use only Aristotle's thirteen, or also the modern textbook names (a later tradition, to be labelled)? The first is more faithful; the second matches what users type.
2. Name: `dia-fallacy` (routes on the user's word) or `dia-sophistic` (closer to the title of the method)?
3. Should dia-reductio's description gain a cross-reference ("to diagnose what is wrong with an argument, use dia-fallacy"), and should a Part-F-style routing probe run before it ships?
4. For `dia-hypothesis`: may the assistant propose the hypotheses, as Socrates does in the Meno, or must the user name them first, as dia-brainstorm's user-first order would suggest?
5. Is a debate-practice skill (Topics VIII gymnastic, user as answerer) wanted at all, given that the model would be both questioner and scorekeeper?
6. Should dia-elenchus's theory.md credit the peirastic examination (SE 2, 11) as the Aristotelian description of what it does? That is a text change, so it needs a version bump.

## Sources

[1] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Theaet.:page=148 — Plato, Theaetetus (Fowler tr.), Perseus 148
[2] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Theaet.:page=149 — Plato, Theaetetus (Fowler tr.), Perseus 149
[3] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Theaet.:page=151 — Plato, Theaetetus (Fowler tr.), Perseus 151
[4] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Theaet.:page=210 — Plato, Theaetetus (Fowler tr.), Perseus 210
[5] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Meno:page=86 — Plato, Meno (Lamb tr.), Perseus 86
[6] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Meno:page=87 — Plato, Meno (Lamb tr.), Perseus 87
[7] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0170:text=Phaedo:page=100 — Plato, Phaedo (Fowler tr.), Perseus 100
[8] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0170:text=Phaedo:page=101 — Plato, Phaedo (Fowler tr.), Perseus 101
[9] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0168:book=6:page=510 — Plato, Republic VI (Shorey tr.), Perseus 510
[10] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0168:book=6:page=511 — Plato, Republic VI (Shorey tr.), Perseus 511
[11] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0174:text=Phaedrus:page=265 — Plato, Phaedrus (Fowler tr.), Perseus 265
[12] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0174:text=Phaedrus:page=266 — Plato, Phaedrus (Fowler tr.), Perseus 266
[13] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0174:text=Phaedrus:page=277 — Plato, Phaedrus (Fowler tr.), Perseus 277
[14] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Soph.:page=219 — Plato, Sophist (Fowler tr.), Perseus 219
[15] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Soph.:page=230 — Plato, Sophist (Fowler tr.), Perseus 230
[16] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Soph.:page=253 — Plato, Sophist (Fowler tr.), Perseus 253
[17] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Stat.:page=262 — Plato, Statesman (Fowler tr.), Perseus 262
[18] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Stat.:page=263 — Plato, Statesman (Fowler tr.), Perseus 263
[19] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Stat.:page=285 — Plato, Statesman (Fowler tr.), Perseus 285
[20] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Stat.:page=287 — Plato, Statesman (Fowler tr.), Perseus 287
[21] https://classics.mit.edu/Aristotle/topics.1.i.html — Aristotle, Topics I (Pickard-Cambridge tr.), Internet Classics Archive
[22] https://classics.mit.edu/Aristotle/topics.8.viii.html — Aristotle, Topics VIII (Pickard-Cambridge tr.), Internet Classics Archive
[23] https://classics.mit.edu/Aristotle/sophist_refut.1.1.html — Aristotle, On Sophistical Refutations 1-10 (Pickard-Cambridge tr.), Internet Classics Archive
[24] https://classics.mit.edu/Aristotle/sophist_refut.2.2.html — Aristotle, On Sophistical Refutations 11-20 (Pickard-Cambridge tr.), Internet Classics Archive
[25] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Theaet.:page=157 — Plato, Theaetetus (Fowler tr.), Perseus 157
[26] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Theaet.:page=160 — Plato, Theaetetus (Fowler tr.), Perseus 160
[27] https://plato.stanford.edu/entries/aristotle-logic — SEP: Aristotle's Logic (Smith)
[28] https://plato.stanford.edu/entries/plato-metaphysics — SEP: Plato's Middle Period Metaphysics and Epistemology
[29] https://plato.stanford.edu/entries/plato-sophstate — SEP: Method and Metaphysics in Plato's Sophist and Statesman
[30] https://plato.stanford.edu/entries/plato-theaetetus — SEP: Plato on Knowledge in the Theaetetus
[31] https://www.ou.edu/content/dam/cas/philosophy/docs/faculty-staff/benson/dialectic_republic.pdf — Benson, Plato's philosophical method in the Republic: the Divided Line (510b-511d)
[32] https://arxiv.org/abs/2205.11822 — Jung et al., Maieutic Prompting (EMNLP 2022), arXiv:2205.11822
[33] https://arxiv.org/abs/2202.13758 — Jin et al., Logical Fallacy Detection, arXiv:2202.13758
[34] https://arxiv.org/html/2311.09761v2 — Helwe et al., MAFALDA (NAACL 2024), arXiv:2311.09761
[35] https://arxiv.org/abs/2305.14999 — Qi et al., The Art of Socratic Questioning (EMNLP 2023), arXiv:2305.14999
[36] https://arxiv.org/abs/2402.07386 — Zeng et al., Chain-of-Layer taxonomy induction (CIKM 2024), arXiv:2402.07386
[37] https://arxiv.org/abs/2404.04293 — Li et al., Reason from Fallacy (NAACL Findings 2024), arXiv:2404.04293
[38] https://arxiv.org/abs/2311.08596 — Laban et al., Are You Sure? The FlipFlop Experiment, arXiv:2311.08596
[39] https://arxiv.org/abs/2310.13548 — Sharma et al., Towards Understanding Sycophancy in Language Models, arXiv:2310.13548
[40] https://pmc.ncbi.nlm.nih.gov/articles/PMC12232635 — Bastani et al., Generative AI without guardrails can harm learning (PNAS 2025)
[41] https://plato.stanford.edu/entries/fallacies — SEP: Fallacies
[42] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Meno:page=89 — Plato, Meno (Lamb tr.), Perseus 89
[43] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0170:text=Phaedo:page=99 — Plato, Phaedo (Fowler tr.), Perseus 99
[44] https://classics.mit.edu/Aristotle/nicomachaen.7.vii.html — Aristotle, Nicomachean Ethics VII (Ross tr.), Internet Classics Archive
[45] https://www.media.mit.edu/publications/don-t-just-tell-me-ask-me-ai-systems-that-intelligently-frame-explanations-as-questions-improve-human-logical-discernment-accuracy — Danry et al., Don't Just Tell Me, Ask Me (CHI 2023), MIT Media Lab
[46] https://arxiv.org/abs/2102.09692 — Bucinca et al., To Trust or to Think: Cognitive Forcing Functions (CSCW 2021), arXiv:2102.09692
[47] https://arxiv.org/abs/2308.09853 — Payandeh et al., How susceptible are LLMs to Logical Fallacies? (LREC-COLING 2024), arXiv:2308.09853
[48] https://arxiv.org/abs/2305.19118 — Liang et al., Encouraging Divergent Thinking through Multi-Agent Debate (EMNLP 2024), arXiv:2305.19118
[49] https://dl.acm.org/doi/fullHtml/10.1145/3640543.3645199 — Chiang et al., LLM-Powered Devil's Advocate (IUI 2024), ACM
[50] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Theaet.:page=150 — Plato, Theaetetus (Fowler tr.), Perseus 150
