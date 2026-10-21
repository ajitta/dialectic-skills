Verdict: SOUND WITH FIXES

All 50 sources were fetched on 2026-10-21. A script matched all 146 quoted fragments against the fetched pages; every fragment attributed to a source matched verbatim except three (finding 13). The primary-text procedures are accurately sourced. What needs fixing is the evaluation layer: fit ratings, evidence strength and overlap with siblings, including the owner's accepted candidates.

## Per-recommendation verdict

| Recommendation | Verdict | Change |
|---|---|---|
| 1. `dia-fallacy` | **drop** as a standalone skill | It answers the same requests as the accepted `dia-warrant` (README cluster 1, "Ship one"), and its own evidence does not support "fit: high" (findings 1, 2). Fold three labelled items into dia-warrant: the Topics VIII.10 solution rule, a two-senses check and the many-questions / assumed-conclusion checks (finding 10). |
| 2. `dia-hypothesis` | **keep with changes, defer** past the current batch | Rate fit medium, not high. Label the Meno's concession and its provisional result, and the ad hominem reading of "adequate". Complete the status rule. Rerun the routing analysis against dia-warrant, dia-conjecture and dia-counterplan (findings 3–7). |
| 3. `dia-division` (later) | **keep with changes** (later, after probes) | Label user-led cutting as a departure from Plato's practice (finding 8). Probe routing against dia-elenchus and against make-something requests (D34). |
| SKIP maieutics; SKIP Topics dialectic; fold one peirastic line into dia-elenchus theory.md | **keep** | Note that `skills/dia-elenchus/references/theory.md:15` already cites SE 183b, so put the new line next to that citation and do not add a second Aristotle credit elsewhere. |

On the accepted set: this document's evidence favours dia-warrant over dia-fallacy; it contains an unused Aristotelian precedent for the munazara pushback rule (finding 9); nothing in it undermines dia-conjecture or dia-counterplan, though dia-hypothesis overlaps both (finding 3).

## Findings

**1. High: the "ask first" mode and the fit rating of dia-fallacy are said to have "direct support" from Danry et al.; the study shows much less.**
Evidence: platonic.md:174 ("An optional 'ask first' mode (which point does this depend on?) has direct support") and :188. [45] is the abstract page only. The full text (dspace.mit.edu/bitstream/handle/1721.1/150613/3544548.3580672.pdf) used one fixed template, "If premise does it follow that claim?", for valid and invalid items alike, with an "always correct" AI, and: "Our current study chose to evaluate AI-feedback on hasty generalization fallacies". Hasty generalization is inductive and is not one of Aristotle's thirteen (mapping it to *secundum quid* is the modern-mapping problem the document flags at :170). commit-first.md:40–43 already records these limits.
Correction: "Templated 'does it follow?' questions improved discernment of hasty-generalization statements over an always-correct AI's explanations; no other fallacy type and no diagnosis question was tested, so the ask-first mode is untested." Lower the fit claim. modern-dialectic.md:163 cites the same study for dia-conjecture and needs the same limit.

**2. High: "Fit for AI chat: high" for dia-fallacy is contradicted by the document's own sources and by the accepted dia-warrant.**
Evidence: in MAFALDA [34] human annotators averaged F1 0.186 ("The low scores of human annotators ... show that the task is difficult"), beat GPT-3.5 on "these 20 samples" only, and the task is "inherently subjective". The document cites only "humans outperform GPT-3.5" (:174), as if users could referee the diagnosis. Sketch step 2 tests "against the definition of a deduction or refutation" (:195; SE 6 [23]: the conclusion must "compel us necessarily"). On the defeasible arguments most chats contain, that marks nearly everything "inconclusive", which the accepted dia-warrant forbids: "Never: call a defeasible argument 'invalid'" (argumentation.md:180).
Correction: fit medium-low in general, medium only for fully quoted deductive arguments; state that the frame does not apply to defeasible arguments. This supports dropping dia-fallacy for dia-warrant.

**3. High: overlap for dia-hypothesis is understated, and README cluster 4 ("Distinct, no competitor") is wrong.**
Evidence: platonic.md:86 lists only partial overlaps with the existing skills. Against the siblings:
- dia-reductio's default "both" direction already ends with "name the premise that would decide it" (skills/dia-reductio/SKILL.md:57).
- dia-warrant's backing question, "Why do you think that the warrant holds?" (argumentation.md:19), is Benson's upward step [2a].
- dia-conjecture's proof-analysis decomposes a claim into lemmas and tests them against cases (modern-dialectic.md:233–236), which is close to [1a]–[2b].
- dia-counterplan negates key assumptions into a rival plan (argumentation.md:165), the same shape as the sketch's rival branch "if not-H then B" (:202).
- dia-elenchus already has the Meno move (elenchus-patterns.md:22).

The trigger "when a question can't be settled directly, find what it depends on" (:88) would also catch ordinary hard factual questions: the capture modern-dialectic.md:215 rejected for Peirce, and the D34 failure.
Correction: overlap partial-high with dia-reductio, dia-warrant and dia-conjecture, partial with dia-counterplan; routing risk high. Key the description on an explicit request for a conditional answer ("what would it depend on", "if we assume H"), with negative routing cells against all four.

**4. Medium: fidelity. The Meno frames the method as a concession whose result stays uncertain; the document omits both.**
Evidence: Meno 86e [5]: "relax just a little of your authority, and allow the question ... to be examined by means of hypothesis". Meno 100b (fetched, Perseus Meno:page=100): "the certainty of this we shall only know when, before asking in what way virtue comes to mankind, we set about inquiring what virtue is, in and by itself." The document presents the method as freestanding (:60–71), and the sketch can end "supported" (:202).
Correction: label it "as in the Meno, a second-best route when 'what is X' is set aside; the answer is provisional until X is defined", and close by offering dia-elenchus when H turns on an undefined term. That also gives a clean routing boundary.

**5. Medium: reading "something adequate" as a premise the user accepts makes the method ad hominem, against the Benson passage the document relies on.**
Evidence: :73 quotes Benson [31]: the method "is precisely not ad hominem". :80 and step 4 (:202) then stop the upward path at "a premise the user accepts", which is the elenchus's criterion (the interlocutor's belief).
Correction: label it as a departure ("adequacy taken as agreement between the parties"), or stop at a premise neither party questions that rests on stated evidence, with its evidence class.

**6. Medium: "Fit: high" for dia-hypothesis ignores that the assistant generates the hypotheses, and that without tools the downward test mostly cannot run.**
Evidence: the assistant "proposes candidate hypotheses" (:84; step 2 at :202, one to three). modern-dialectic.md:214 rejects abduction because the assistant as hypothesis generator "maximizes over-reliance and invented facts"; the documents never reconcile this. Buçinca [46] tested decide-first, wait and on-demand interfaces, not conditional answers, so "mirrors" (:84) is interpretation. Without tools every downward fact is user-supplied or "unverified recall", so H will usually end "untested".
Correction: fit medium; default to "the user names H first; the assistant proposes only on request, labelled" (settles open question 4, :218); state that the tool-less outcome is usually "untested", which lowers the value claimed at :185.

**7. Medium: the dia-hypothesis status rule is incomplete and uses an undefined notion of "derivation".**
Evidence: step 6 (:202) allows "supported, doubtful (a consequence conflicts), or untested": no outcome for an upward chain ending at a rejected premise, and "supported" is undefined. Step 3 demands "the derivation from H to the answer", but [28] says Phaedo "'agreement' here is not a notion of entailment or logical consequence", and Benson's note 13 [31] calls his own "derive" language "relatively figurative".
Correction: define supported as "the upward chain ends in an agreed premise and no tested consequence conflicts". Add "unsupported: the upward chain ends in a rejected premise". Write step 3 as "show how H yields the answer, saying whether the step is strict or only plausible".

**8. Medium: dia-division turns one episode into the whole procedure without labelling the departure.**
Evidence: the sketch has the user make every cut (:209), generalising :115. In the fetched texts the Stranger leads: Sophist 219 [14] (Theaetetus: "It appears so, at any rate, from what you have said"); Statesman 262a [17] is one invited cut by Young Socrates ("one kind is the care of men"), at once corrected as an "error". The label (:208) does not say who cuts.
Correction: add to the label "the user proposes the cuts; in the dialogues the Stranger leads them and the respondent assents".

**9. Medium: missed evidence. Topics VIII gives an Aristotelian rule against bare denial, which bears on the accepted munazara pushback batch and on dia-conjecture.**
Evidence: [22] (Topics VIII.8, fetched by the document but not used): "if a man refuses to admit the proposition without having either a negative instance or some counter-argument to bring against it, clearly he is ill-tempered: for ill-temper in argument consists in answering in ways other than the above, so as to wreck the reasoning." In the same chapter: "against the universal one should try to bring some negative instance". This is the Greek counterpart of munāẓara's mukābara rule (scholastic.md:139, :155); the duty to bring a negative instance also anticipates Lakatos's global counterexample.
Correction: cite Topics VIII.8 beside munāẓara in the pushback batch's research, as lineage (scholastic.md:134: the discipline drew on Aristotelian logic), not as independent confirmation. No recommendation changes.

**10. Low: the solution rule is narrower than Aristotle's, and its scope is dropped.**
Evidence: Topics VIII.10 [22] opens "Of all arguments that reason to a false conclusion the right solution is to demolish the point on which the fallacy ... depends". SE 18 [24] gives two modes: "we may effect the solution either by drawing some distinction or by demolishing something". Sketch step 5 (:195) keeps only "the one point to demolish".
Correction (for the dia-warrant fold): "name the one point the failure depends on, and either draw the distinction (two senses) or reject that premise; rejecting some other false premise is not a solution (Topics VIII.10; SE 18)".

**11. Low: "Fidelity: high" for the thirteen types glosses over their dependence on Greek.**
Evidence: SE 4 [23] says accent arguments are "not easy to construct in unwritten discussion", and form of expression concerns "a masculine thing by a feminine termination". Neither transfers to an English or Korean chat as written.
Correction: say that two of the six language-dependent types apply only by analogy outside Greek.

**12. Low: Bastani's safeguard is understated.**
Evidence: :50 says "A tutor prompted to withhold answers 'largely mitigated' this." The PNAS full text (europepmc PMC12232635 fullTextXML) adds a second safeguard: "the prompt provides a significant amount of problem-specific information provided by teachers, including one or more (correct) solutions to the practice problem, as well as common student mistakes".
Correction: "a tutor prompted to give hints, not answers, and given teacher-written solutions and common mistakes for each problem".

**13. Low: citation hygiene.**
- "unhypothetical first principle" (:77) is the SEP's phrase [28], not Shorey's [10] ("that which requires no assumption").
- "A taste of the theories of the wise" (:50) misquotes [25] ("a taste of each of the philosophical theories").
- "solver" (:174) does not occur in [24].
- :62 drops "seems to me" from Phaedo 100a [7].
- [27] and [30] return 301 before redirecting; store the final URLs.

**14. Low: LLM studies cited without their setup.** [47] is an LLM persuader against an LLM debater, not a user (:174). [36] induces taxonomies from given entity sets (:115). [33] tested 2021 classifiers. [33] and [37] were read as abstracts only. [49] studied groups. Correction: state each setup where it is used.

**15. Low: dia-fallacy sketch logic (moot if dropped).** The verdicts "genuine" and "no defect found" (:195) overlap with no rule for choosing between them; step 4 (premise acceptability) has no evidence classes.

Repository rules: no sketch names a product, requires a tool or contains Hangul; all steps run without tools (see finding 6).

## Citation table

S = supports, P = partly, N = does not support, U = unreachable. All 50 were fetched.

| # | Source | Verdict | Note |
|---|---|---|---|
| 1 | Theaet. 148 | S | pregnant, not empty |
| 2 | Theaet. 149 | S | |
| 3 | Theaet. 151 | S | match-maker, bite, perception |
| 4 | Theaet. 210 | S | wind-eggs, gentler |
| 5 | Meno 86 | S | concession at 86e omitted (F4) |
| 6 | Meno 87 | S | geometer's two branches |
| 7 | Phaedo 100 | S | drops "seems to me" (F13) |
| 8 | Phaedo 101 | S | consequences first; no mixing |
| 9 | Rep. 510 | S | |
| 10 | Rep. 511 | P | "unhypothetical" not Shorey's wording |
| 11 | Phaedrus 265 | S | |
| 12 | Phaedrus 266 | S | |
| 13 | Phaedrus 277 | S | |
| 14 | Sophist 219 | S | Stranger leads the cuts (F8) |
| 15 | Sophist 230 | S | |
| 16 | Sophist 253 | S | |
| 17 | Statesman 262 | S | one invited cut, corrected |
| 18 | Statesman 263 | S | |
| 19 | Statesman 285 | S | |
| 20 | Statesman 287 | S | |
| 21 | Topics I | S | |
| 22 | Topics VIII | S | VIII.8 ill-temper rule unused (F9) |
| 23 | SE 1–10 | S | thirteen types, SE 6 test |
| 24 | SE 11–20 | P | "solver" absent; SE 18's distinction mode dropped |
| 25 | Theaet. 157 | S | misquoted once at :50 |
| 26 | Theaet. 160 | S | |
| 27 | SEP Aristotle's Logic | S | 301 without trailing slash |
| 28 | SEP Plato middle period | S | |
| 29 | SEP Sophist/Statesman | S | |
| 30 | SEP Theaetetus | S | 301 without trailing slash |
| 31 | Benson, Divided Line | S | the "not ad hominem" point conflicts with the sketch (F5) |
| 32 | Maieutic Prompting | S | MAX-SAT, name only |
| 33 | Jin, fallacy detection | P | 2021 classifiers; abstract only |
| 34 | MAFALDA | P | humans also poor (F1 0.186), n = 20 |
| 35 | Socratic Questioning | S | |
| 36 | Chain-of-Layer | P | different task |
| 37 | Reason from Fallacy | P | abstract only |
| 38 | FlipFlop | S | 46%, 17% |
| 39 | Sharma, sycophancy | S | |
| 40 | Bastani (PNAS) | P | safeguard incomplete (F12) |
| 41 | SEP Fallacies | S | Hamblin |
| 42 | Meno 89 | S | |
| 43 | Phaedo 99 | S | |
| 44 | NE VII | S | |
| 45 | Danry (abstract page) | P | hasty generalization only, templated question (F1) |
| 46 | Buçinca | P | abstract supports; "mirrors" is interpretation |
| 47 | LOGICOM | P | agent-vs-agent setup |
| 48 | Liang, MAD | S | |
| 49 | Chiang, devil's advocate | P | groups, against AI advice |
| 50 | Theaet. 150 | S | |
