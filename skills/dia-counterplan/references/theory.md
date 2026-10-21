# Dialectical inquiry: theory reference

Read this only when the user asks about the method or its sources. The rules are in SKILL.md; this file says where they come from and where the skill departs from them. Everything is paraphrased from the sources at the end unless quoted. Mason's 1969 paper was read in abstract only; the procedure below comes from Schwenk's summary, so fidelity is medium-high and the procedure rests on secondary sources.

## 1. The method

- **Mason (1969).** Richard O. Mason proposed two criteria for a planning technique: it should expose the assumptions under a plan, and it "should suggest new and more relevant assumptions" (Mason, abstract). His case was a field study at RMK Abrasives.
- **The procedure, as Schwenk summarises it.** The plan's underlying assumptions (ten at RMK) were identified; a counterplan was built on opposite assumptions; the two were argued in a structured debate before management, after which the managers formed "a 'new, encompassing view'" (Schwenk, BEBR 814). This skill keeps the order (plan, assumptions, counterplan, side by side, synthesis) and makes the synthesis the user's.
- **A counterplan is a course of action.** Cosier: "dialectical inquiry requires specification of an alternative course of action" (Cosier 1981). Hence SKILL.md Step 5: the counterplan is a different plan, not the original with a part removed.
- **Lineage.** Mason's approach follows C. West Churchman's Hegelian inquiring system: Mitroff, Emshoff and Kilmann write of "the dialectical approach to strategic planning first suggested by Churchman … and Mason" (1979), and a later comparison says dialectical inquiry "derives from the work of C. West Churchman (1971), as further developed by R. O. Mason (1969)" (TQR 2006). Mitroff and Mason (1982) later formalised it in a way that "extends the work of Toulmin on argumentation".
- **Not Hegel's synthesis.** Hegel "never adopted Fichte's triadic 'thesis—antithesis—synthesis' language", and in his dialectic the movement comes from the content itself, with "nothing extraneous" introduced (SEP, "Hegel's Dialectics"). An assistant that writes the antithesis is such an outside party. So the skill does not call its result a Hegelian synthesis: the user's set of assumptions is the synthesis, in Mason's sense of new and more relevant assumptions.

## 2. Which assumptions do the work (SAST)

Strategic Assumption Surfacing and Testing (SAST; Mason & Mitroff 1981) is a later variant of dialectical inquiry. Its test asks of each assumption: "If the opposite of this assumption is true, does it have any significant bearing on the issue?", and then rates each for importance and certainty (IfM SAST page). SKILL.md Step 3 uses the test, narrowed to the decision ("would it change the decision?"), and omits the ratings to keep the output short.

## 3. Contraries, not negations

The negation of "demand grows 10%" is not a premise a plan can rest on; the assistant has to pick a contrary, and that choice is where bias enters (compare dia-reductio, which distinguishes contradictories from contraries). Schwenk summarises Mason's step as "the negation of these assumptions" and a counterplan "based on opposite assumptions" (BEBR 814); taken item by item, a bare negation gives a plan nothing to rest on, so the skill picks contraries instead (a departure, §7). Hence Rule 2 and Step 4: each contrary is specific and plausible, marked as the assistant's choice, checked for joint coherence and fitted to the same data, so the user can reject any of them.

## 4. Evidence on dialectical inquiry (DI) and devil's advocacy (DA)

All of these studies used human participants. In the group studies, separate subgroups or advocates developed the plan and the counterplan or critique; in the lab studies, participants received written reports presented as coming from different experts or planning committees. None tested a person who knows that one author wrote both sides.

- DI and DA both gave higher-quality recommendations and assumptions than consensus; DI beat DA on the quality of assumptions; consensus groups were more satisfied (Schweiger, Sandberg & Ragan 1986).
- In a longitudinal study, DI = DA > consensus on decision quality, with more re-evaluation of one's own assumptions and lower acceptance of the group decision (Schweiger, Sandberg & Rechner 1989).
- DI and DA groups exceeded the average of their members, and on several measures the best member (Schweiger & Sandberg 1989).
- Lab studies favoured DA over DI on performance. Schwenk also wrote that "Neither the DA nor the DIS was shown to be superior to the E in improving the quality of strategy statements", that "Proponents of the DIS may have overstated their case", and that "the DA should be recommended over the DIS". He explained the satisfaction gains by "a general belief … that when we have 'heard both sides' … we are better able to make a decision" (Schwenk, BEBR 814).
- A "carping critic" DA did not help where an objective DA did, and DA works only if decision-makers sincerely accept questioning. DA "may even help to solidify commitment to a disastrous course of action by giving the decision-makers confidence that they considered all points of view" (Schwenk 1984).
- Schwenk's 1989 meta-analysis, as given by an abstract aggregator (a single secondary source): "decision making is improved by the use of devil's advocacy or dialectical inquiry when the assumptions of an expert's report are incorrect, however neither method was proven to be superior."

What follows for the skill:

- **Why DI and not DA.** The evidence favours DA on performance and DI only on the quality of surfaced assumptions. This skill is DI anyway because its distinct output is the counterplan, which no sibling produces; the critic's role is already played by dia-brainstorm's stress mode, which questions the user. The choice rests on that division of work, not on DI being better. There is no separate DA mode.
- **The false-assurance guard.** Schwenk's two warnings are why the record states what the comparison did not test and that "hearing both sides is not evidence that the plan was tested", and why Rule 1 forbids carping.

## 5. One assistant in one chat

Fit for an AI chat is medium, not high.

- **No study tests one model writing both sides.** The format obliges a counter-case but cannot ensure its strength; assistants tend to match the user's views and people prefer such answers (Sharma et al. 2023), and across eleven models assistants affirmed users' actions about 50% more than humans did, while people trusted sycophantic models more (Cheng et al. 2025). The symmetry rule (Rule 3) and the pushback rule (Rule 6) are the only guards, and only Rule 6 acts against yielding.
- **The nearest LLM studies are about groups.** Chiang et al. (2024) tested an LLM devil's advocate arguing against a separate model's advice in group decisions; the significant effect belonged to the interactive version ("helps groups significantly increase their appropriate reliance"), and the main effects were marginal (p = 0.064 and 0.063). Lee et al. (2025) found higher process and outcome satisfaction in 48 people in power-imbalanced groups; accuracy is not reported in the abstract. Neither studied one user, one-pass DI, or a model critiquing itself.
- **Self-examination.** Critiquing its own earlier recommendation is intrinsic self-correction, and "LLMs struggle to self-correct their responses without external feedback" (Huang et al. 2024). So `claude` is never the default target, and the output says it is a self-examination and not independent.
- **Debate studies do not transfer.** Debate gains with human judges (Khan et al. 2024) came from separate debaters, a hidden source text and a quote verifier; a single chat has none of them, although the user can still act as judge. That is why the skill is named for Mason's method and not "debate".
- **The user's ruling.** In DI the decision-maker judges. A user who rejects a contrary is ruling, not challenging, so the assistant records it and does not defend the contrary; it rewrites one only on a named defect (Rule 6). For the plan's own assumption list, the sibling rule applies: withdraw only on a named defect; insistence is not a defect.

## 6. Borrowed: the open question and the kept minority view

Two elements come from the Talmud, not from Mason, and are labelled as borrowings:

- **Undetermined (*teyku*).** A Talmudic problem with two balanced sides and no deciding authority ends *teyku*, "let it stand", unsolved; there are more than 300 such cases in the Babylonian Talmud (Jacobs). The result **undetermined** keeps a key pair open, with the balanced considerations and the observation that would decide it, instead of forcing a choice. Unlike *teyku*, which Jacobs calls inherently insoluble, an undetermined pair here is open only for now; the borrowing is the refusal to force a choice, not a claim that the pair cannot be decided.
- **The strongest argument for the side set aside.** The Mishnah records a minority opinion so that a later court may rely on it (Mishnah Eduyot 1:5). The record keeps the strongest argument for each assumption the user did not hold, for the same reason. Eduyot 1:6 gives a rival reason (Rabbi Judah: the minority view is recorded so it can be identified as set aside); the skill follows 1:5.

## 7. Departures, in one list

- One assistant restates the plan and writes the counterplan; in Mason's study the plan and counterplan had different authors and were debated before a group of managers.
- The synthesis is the user's set of assumptions; the assistant writes none and picks no winner.
- Contraries are chosen by the assistant and labelled, not presented as the opposition's own view.
- Contraries replace the negated ("opposite") assumptions of Schwenk's summary.
- SAST's test is used without its importance and certainty ratings.
- *Teyku* and the kept minority view are borrowed from the Talmud.

## Sources

- Mason, "A Dialectical Approach to Strategic Planning", *Management Science* 15(8), 1969, B403–B414 (abstract). https://ideas.repec.org/a/inm/ormnsc/v15y1969i8pb403-b414.html
- Schwenk, "Dialectical inquiry: decision-makers' perceptions of its effectiveness", BEBR Faculty Working Paper 814. http://hdl.handle.net/2142/27062
- Schwenk, "The use of devil's advocates in strategic decision-making" (working paper, 1984). https://hdl.handle.net/2142/29170
- Cosier, "Dialectical Inquiry in Strategic Planning: A Case of Premature Acceptance", *Academy of Management Review* (1981). https://journals.aom.org/doi/10.5465/amr.1981.4285716
- Schweiger, Sandberg, Ragan, *Academy of Management Journal* 29 (1986), abstract. https://journals.aom.org/doi/abs/10.5465/255859?journalCode=amj
- Schweiger, Sandberg, Rechner, *Academy of Management Journal* (1989), abstract. https://journals.aom.org/doi/abs/10.5465/256567
- Schweiger, Sandberg, "The utilization of individual capabilities in group approaches", *Strategic Management Journal* 10 (1989). https://ideas.repec.org/a/bla/stratm/v10y1989i1p31-43.html
- Schwenk, "A meta-analysis on the comparative effectiveness of devil's advocacy and dialectical inquiry", *Strategic Management Journal* (1989). https://doi.org/10.1002/smj.4250100309 ; abstract via aggregator (secondary): https://www.readabstracts.com/Business/Uncertainty-in-the-transaction-environment-an-empirical-test.html
- Schwenk, "Effects of devil's advocacy and dialectical inquiry: a meta-analysis", *OBHDP* 47 (1990), record only. https://ideas.repec.org/a/eee/jobhdp/v47y1990i1p161-176.html
- Mitroff, Emshoff, Kilmann, *Management Science* 25(6) (1979). https://doi.org/10.1287/mnsc.25.6.583
- *The Qualitative Report* (2006), comparison of inquiry approaches. https://doi.org/10.46743/2160-3715/2006.1652
- Mitroff and Mason (1982). https://link.springer.com/article/10.1007/BF00126172
- Institute for Manufacturing, Cambridge, "Strategic Assumptions Surfacing and Testing". https://www.ifm.eng.cam.ac.uk/research/dstools/strategic-assumptions-surfacing-and-testing/
- Maybee, "Hegel's Dialectics", *Stanford Encyclopedia of Philosophy* (citing Mueller 1958 on the triad). https://plato.stanford.edu/entries/hegel-dialectics
- Sharma et al., "Towards Understanding Sycophancy in Language Models" (2023). https://arxiv.org/abs/2310.13548
- Cheng et al., "Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence" (2025). https://arxiv.org/abs/2510.01395
- Chiang, Lu, Li, Yin, "Enhancing AI-Assisted Group Decision Making through LLM-Powered Devil's Advocate", IUI 2024. https://dl.acm.org/doi/fullHtml/10.1145/3640543.3645199
- Lee, Hwang, Kim, Lee, "Conversational Agents as Catalysts for Critical Thinking" (2025). https://arxiv.org/abs/2503.14263
- Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet", ICLR 2024. https://arxiv.org/html/2310.01798v2
- Khan et al., "Debating with More Persuasive LLMs Leads to More Truthful Answers", ICML 2024. https://arxiv.org/html/2402.06782v4
- Louis Jacobs, *Teyku: The Unsolved Problem in the Babylonian Talmud* (1981), introduction. https://booksof.louisjacobs.org/book/teyku
- Mishnah Eduyot 1:5–6 (Sefaria, Kulp tr.). https://www.sefaria.org/Mishnah_Eduyot.1.5-6
