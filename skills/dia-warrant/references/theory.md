# dia-warrant: theory reference

Everything here is paraphrased from the sources at the end unless quoted. Bracketed numbers refer to the numbered sources at the end; the unnumbered sources there were added for this skill.

## 1. Toulmin's layout

- **Source.** Stephen Toulmin, *The Uses of Argument* (1958; updated edition 2003), ch. III, "The Layout of Arguments" [3]. Toulmin's aim was to attack the assumption that any significant argument can be put in formal, deductive terms [1][4].
- **The six elements** [2][4]: claim, data, warrant, qualifier, backing, rebuttal. Page references below follow Verheij (2009) [4], which gives the 1958 page before the slash and the 2003 page after it.
  - Claim: the assertion one is committed to and must justify when challenged (97/90).
  - Data: the answer to "What have you got to go on?" (97–8/90).
  - Warrant: the answer to "How do you get there?"; warrants are "general, hypothetical statements, which can act as bridges" (98/91). They are often true only "generally".
  - Qualifier: the strength the warrant confers on the step, such as "presumably" (101/94).
  - Rebuttal: "circumstances in which the general authority of the warrant would have to be set aside" (101/94).
  - Backing: why the warrant holds; it is field-dependent, as statutes back the Bermuda warrant (103–4/95–6) [2].
- **The Harry example.** Harry was born in Bermuda (data); a man born in Bermuda will generally be a British subject (warrant), backed by statutes; so, presumably (qualifier), Harry is a British subject, unless, for example, his parents were aliens or he has become a naturalized American (rebuttal) [4].
- **Wording.** Toulmin's own questions are "What have you got to go on?" and "How do you get there?". The backing question in the form "Why do you think that the warrant holds?" is Verheij's paraphrase, not Toulmin's [4]. The questions for backing, qualifier and rebuttal that SKILL.md puts to a user who asks to be questioned (why that rule holds, how sure they are, when it would not apply; SKILL.md, The reply) are this skill's wording.
- **Known problems.** Several authors (Schellens, Johnson, Freeman) object that data and warrant cannot always be told apart, and warrants are general statements, which sits badly with singular data [2]. The layout describes an argument; it does not by itself tell good warrants from bad. That is why this skill adds critical questions.

## 2. Walton's argumentation schemes and critical questions

- **Source.** Walton, Reed & Macagno, *Argumentation Schemes* (CUP 2008): defeasible forms of argument, sixty-five of them in the compendium, each assessed by its critical questions. An instance is acceptable if its premises are acceptable and its critical questions can be answered. Real arguments often fit several schemes, and the set of schemes is open-ended [12]. SKILL.md (The steps) therefore names kinds of step rather than fitting each argument to one scheme, and asks only the questions that bear on the step at hand.
- **Why questions.** Critical questions ask rather than assert counter-facts. The critical-questions generation task was proposed because it needs no outside knowledge, which avoids invented counterarguments [13]; that suits a chat with no tools and is the basis of SKILL.md's rule that the assistant's recall closes no question (The steps). LLMs are "reasonable" question generators with a wide margin for improvement; in the 2025 shared task the best accuracy was 67.6, and three of the top four teams used scheme annotations [13][14]. These are LLM-only evaluations, without users.
- **The schemes' critical questions**, which SKILL.md (The steps) gives in a few words under the kind of step each scheme covers (from someone's word, from a like case, from before and after to a cause, from an action to its results, from a measure or a sign), come from these sources:
  - *Expert opinion*: six questions (expertise, field, opinion, trustworthiness, consistency, backup evidence), Walton, Reed & Macagno 2008, p. 310, as tabulated in Wikipedia, "Argumentation scheme". An earlier five-question version (Walton 1996, p. 65) is quoted by Verheij [4].
  - *Analogy*: three questions (differences between the cases, whether A is right in the source case, a counter-analogy), Walton, Reed & Macagno 2008, p. 315, as quoted by Walton (2014). The question whether the cited similarities bear on A turns the scheme's similarity premise into a question; it is this skill's addition, not one of the three.
  - *Correlation to cause*, the scheme of the step from before and after to a cause (it runs from an observed change back to a cause, the opposite direction of argument from cause to effect): three questions (whether the correlation is real, whether it is more than a coincidence, whether some third factor causes both), Walton 2006, pp. 101–103, as quoted by Walton & Gordon (2009); a fuller list of seven is in Walton 1995, p. 142. SKILL.md's "what else changed" is the third-factor question and "what would have happened anyway" the coincidence question, in this skill's words.
  - *Consequences*: the positive and negative forms, Walton, Reed & Macagno 2008, p. 101 (Macagno, Walton & Reed 2017); three questions (likelihood, the evidence for it, opposite consequences), p. 102, as quoted by Fan (2019) (secondary source).
  - *Sign*: two questions (strength of the correlation, other events that would account for the sign better), Walton 1996, p. 48, after Hastings (1962), as quoted by Blair (1998).
  - The general question whether the reasons are true and how they are known turns each scheme's minor premise (whether X really occurs here, whether S is really present) into a question; it is this skill's addition.
- **Why these schemes.** The research note proposed practical reasoning, expert opinion, cause to effect, analogy and sign. This skill puts argument from correlation to cause in place of cause to effect, because SKILL.md's causal step reasons from an observed change, and argument from consequences in place of practical reasoning: practical reasoning's questions (conflicting goals, alternative means, side effects, feasibility) examine a plan or decision. Argument from consequences covers the common "do X, because it brings Y" argument as an argument. SKILL.md also names a step from some cases to most, with its own question (which cases, and how they were picked); no scheme source for it is cited here.

## 3. Why Toulmin and Walton are joined

Verheij (2009) distinguishes four types of critical questions [4]: questions about the scheme's conclusion (other reasons for or against it), about the elements of its premises, about its exceptions ("Some critical questions are like Toulmin's notion of rebuttal"), and about its conditions of use. This skill's questions of any step follow the four: what reasons the argument left out (conclusion), whether the reasons are true and how they are known (premises), whether this case is an exception to the rule (exceptions), and the rule that carries the step and whether it holds here (conditions of use) (SKILL.md, The steps). Verheij sorts Walton's 1996 expert-opinion questions this way and adds a conditions-of-use question of his own.

That is the basis for joining Toulmin and Walton here. An earlier basis, that "the LLM work that operationalises Toulmin uses critical questions" [6], does not hold: Gupta et al. operationalise Toulmin without critical questions [5], and Castagna et al. apply Toulmin-derived questions to the model's own reasoning on MT-Bench, not Walton's scheme questions to a user's argument [6].

## 4. What is taken from pragma-dialectics

Van Eemeren and Grootendorst model a critical discussion between two parties, in four stages, under ten rules ("ten commandments", *A Systematic Theory of Argumentation*, 2004, p. 190) [7][10]; a violation of a rule is a fallacy [10]. Taken over (SKILL.md, The steps and The exchange):

- **Standpoint rule (3):** "A party's attack on a standpoint must relate to the standpoint that has indeed been advanced by the other party" [10].
- **Unexpressed premise rule (5):** "A party may not deny premise that he or she has left implicit or falsely present something as a premise that has been left unexpressed by the other party" [10]. This skill keeps the second half and departs from the first: when the user is the arguer and disowns a rule the assistant supplied, it goes, because the assistant cannot tell whether its reconstruction is the premise the user left implicit, and the user's word is the only evidence of it. The step still needs a rule, so the assistant asks which rule the user does rely on, and until they name one the step has nothing carrying it (SKILL.md, The exchange). For a pasted text or an earlier answer the user is not the arguer, and a rejection moves the reading only as far as a defect it names holds.
- **Usage rule (10):** "a party must interpret the other party's formulations as carefully and accurately as possible" [10].

SKILL.md's least general rule (The steps) adapts the **validity rule (8)** to defeasible steps (it supplies the premise the step needs, not one that makes it deductively valid): arguments must be "logically valid or capable of being made logically valid by making explicit one or more unexpressed premises" [10]. It replaces the research note's rule "never attribute a warrant the author would disown", which cannot be checked for a third-party text.

Not taken over: the freedom, burden-of-proof, relevance, starting-point, argument-scheme and closure rules, which govern a discussion that both parties have committed to. The argument-scheme rule (7) is close to what the critical questions do, but it is not adopted as a rule here. A one-sided audit of a two-party ideal is a reduced use of pragma-dialectics.

## 5. Departures and additions

- **Who supplies the warrant.** In Toulmin's layout the arguer answers the challenges. Here the assistant usually reconstructs an unstated warrant. That is the method's main risk in a chat (an invented premise) and the reason for saying it is the assistant's reading, keeping it least, and letting the user reject it when the user is the arguer.
- **This skill's additions:** the strength check, the chained-step rule and the rule that the assistant's recall closes no question (all in The steps), the judgment (Your judgment), and the reply that leads with the judgment before the working. The judgment keeps weak support apart from evidence against the conclusion, names the weakest step and why it matters for what the conclusion has to carry, and says whether the assistant would act on the conclusion as things stand. A disputed point gives way only as far as a defect the user names holds, and repetition moves nothing (The exchange).
- **Questioning the user.** Toulmin's layout is itself a sequence of questions put to the arguer [4]. Most of the argument-mapping evidence concerns learners who build maps themselves: about 0.8 of a standard deviation in intensive courses, a figure attributed to van Gelder, who co-wrote the chapter and developed the Rationale software [49]. Receiving a finished map is not what was measured, so a user who asks to be questioned fills the steps themselves, one question a message (SKILL.md, The reply).
- **Human-AI evidence.** LMs prompted with Toulmin's model produce claim, reason and warrant triples judged by humans [5]; Toulmin-based critical questions improved LLM reasoning on MT-Bench [6]. Neither study measures whether a user reasons better.
- **Not used:** Walton and Krabbe's six dialogue types, a taxonomy rather than a procedure.

## Sources

- [1] "Argument and Argumentation", *Stanford Encyclopedia of Philosophy*. https://plato.stanford.edu/entries/argument/
- [2] F. H. van Eemeren et al. (2014), "Toulmin's Model of Argumentation", *Handbook of Argumentation Theory*. https://link.springer.com/rwe/10.1007/978-94-007-6883-3_4-1
- [3] S. Toulmin, *The Uses of Argument*, updated ed. (CUP 2003), sample with contents. http://assets.cambridge.org/97805218/27485/sample/9780521827485ws.pdf
- [4] B. Verheij (2009), "The Toulmin Argument Model in Artificial Intelligence". https://www.ai.rug.nl/~verheij/publications/pdf/toulmin2009.pdf
- [5] Gupta, Zuckerman, O'Connor (ACL 2024), "Harnessing Toulmin's theory for zero-shot argument explication". https://aclanthology.org/2024.acl-long.552
- [6] Castagna, Sassoon, Parsons (2024), "Critical-Questions-of-Thought". https://arxiv.org/abs/2412.15177
- [7] van Eemeren & Grootendorst (2004), *A Systematic Theory of Argumentation*, CUP preview (contents). https://api.pageplace.de/preview/DT0400.9780511162459_A23689806/preview-9780511162459_A23689806.pdf
- [10] "Pragma-dialectics", Wikipedia (the ten rules). https://en.wikipedia.org/wiki/Pragma-dialectics
- [12] L. Groarke (2009), review of Walton, Reed & Macagno, *Argumentation Schemes*, *Notre Dame Philosophical Reviews*. https://ndpr.nd.edu/reviews/argumentation-schemes
- [13] Calvo Figueras & Agerri (CoNLL 2024), "Critical Questions Generation: Motivation and Challenges". https://doi.org/10.18653/v1/2024.conll-1.9
- [14] Calvo Figueras et al. (ArgMining 2025), "Overview of the Critical Questions Generation Shared Task". https://aclanthology.org/2025.argmining-1.23
- [49] Davies, Barnett, van Gelder, "Using Computer-Aided Argument Mapping to Teach Reasoning". https://ecampusontario.pressbooks.pub/criticalthinking1234/chapter/introduction
- "Argumentation scheme", Wikipedia (expert-opinion questions from Walton, Reed & Macagno 2008, p. 310). https://en.wikipedia.org/wiki/Argumentation_scheme
- D. Walton (2014), "Argumentation Schemes for Argument from Analogy", in H. J. Ribeiro (ed.), *Systematic Approaches to Argument from Analogy*. https://uwindsor.scholaris.ca/server/api/core/bitstreams/4aba3121-37eb-43ae-9d25-e1e024c77ec2/content
- D. Walton, T. F. Gordon (2009), "Jumping to a Conclusion: Fallacies and Standards of Proof", *Informal Logic* 29(2) (correlation-to-cause questions from Walton 2006, pp. 101–103; seven in Walton 1995, p. 142). https://doi.org/10.22329/il.v29i2.1227
- Y. Fan (2019), *The Effects of Critical Questions on Undergraduate Students' Argumentative Writing*, PhD dissertation, University of Delaware (consequences questions from Walton, Reed & Macagno 2008, p. 102). https://udspace.udel.edu/server/api/core/bitstreams/d3a41025-e0b2-4db4-bbce-00ac51e1c82a/content
- F. Macagno, D. Walton, C. Reed (2017), "Argumentation Schemes. History, Classifications, and Computational Applications". https://philarchive.org/archive/MACASH-10
- J. A. Blair (1998), "Walton's Argumentation Schemes for Presumptive Reasoning: A Critique and Development", ISSA Proceedings. https://rozenbergquarterly.com/issa-proceedings-1998-waltons-argumentation-schemes-for-presumptive-reasoning-a-critique-and-development/
