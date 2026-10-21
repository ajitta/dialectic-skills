# Candidates: argumentation theory and practical reasoning

Research note, 2026-10-21, against `main` at `becc4b3`. Proposals only; no skill file changed. Every outside claim carries a ledger citation; claims I could not source are marked [unverified]. Two owner inputs arrived mid-task and are applied throughout: a check of another agent's proposal (section 3) and "fit for human-AI chat" as a primary criterion beside fidelity (one model in a chat, the user as the other party).

## 1. Scope

- Covered: Toulmin's layout (2.1); pragma-dialectics (2.2); Walton's dialogue types and argumentation schemes with critical questions (2.3); Rapoport's rules, steelmanning and the Ideological Turing Test (2.4); Double Crux (2.5); Street Epistemology (2.6); dialectical inquiry and devil's advocacy (2.7); pre-mortem, as a contrast (2.8); LLM debate research and a single-assistant "debate" (2.9).
- Merged: Walton's schemes are treated with Toulmin, because the LLM work that operationalises Toulmin uses critical questions [6] and the critical-questions benchmarks find schemes help [14].
- Dropped: Rogerian argument as a separate candidate (it is Rapoport's rule 1, credited to Carl Rogers [16][18]); multiple advocacy and assumption surfacing (SAST) as separate candidates (variants of dialectical inquiry [26]).
- Out of scope (a sibling handles them): dia-commit, consider-the-opposite, learning-by-teaching.

Criteria used for every candidate: fidelity to the named method; **fit for human-AI chat** (who plays which role; how the structure handles the AI-specific risks: yielding under pushback, the user over-relying on the assistant, one model playing both sides, invented sources or premises); overlap and routing against the seven skills; tool-less feasibility.

## 2. Candidates

### 2.1 Toulmin's layout of arguments

- **Source.** *The Uses of Argument* (1958; updated ed. 2003), ch. III "The Layout of Arguments", pp. 87–134, with sections on data and warrants (p. 89) and on backing (p. 95) [3]. Toulmin's aim was to attack the assumption that any significant argument can be put in formal deductive terms [1][4]. The six elements are claim, data, warrant, modal qualifier, rebuttal and backing [2][4].
- **Procedure as the source gives it.** It is a sequence of challenges. A claim is met with "What have you got to go on?", which yields the data. "How do you get there?" yields the warrant, a general rule-like licence, often only "generally" true. That calls for a qualifier ("presumably"). "Why do you think that the warrant holds?" yields the backing (in the Harry/Bermuda example, statutes). Conditions of rebuttal are "circumstances in which the general authority of the warrant would have to be set aside" [4]. Backing is field-dependent [2].
- **Known problems.** Several authors object that data and warrant cannot always be told apart (Schellens, Johnson, Freeman) [2]. Warrants are general statements, which sits badly with singular data [2]. The layout describes; it does not by itself tell good warrants from bad.
- **Roles in a chat.** The user owns or brings the argument; the assistant asks Toulmin's questions or fills in the layout. It works in one pass over a pasted text or the assistant's own answer, or turn by turn with the user answering each question.
- **AI risks.** *Invented premises:* the warrant is usually unstated, so the assistant must supply it. That is the core danger, and it is countered only if every supplied warrant is labelled as a reconstruction and the user can reject it (as dia-reductio does with [A]). *Over-reliance:* a tidy diagram can look authoritative, though it is the assistant's reading. *Sycophancy:* low; the layout makes no verdict for the user to push against, unless the skill adds one.
- **Human-AI evidence.** LMs prompted with "According to Toulmin model" produce claim, reason and warrant triples, judged by humans for coverage and validity [5]. Toulmin-based critical questions improved LLM reasoning on MT-Bench [6]. Neither study measures whether a *user* reasons better; the 0.8 SD argument-mapping figure comes from students mapping intensively themselves in courses, not from receiving a map (section 3).
- **Overlap.** dia-reductio is partial: both list premises with sources, but reductio needs a strict Q and not-Q and gives "no contradiction found" for defeasible arguments, which is Toulmin's home ground. dia-refine is partial ("logical leaps", one pass, but it revises a draft). dia-negative and dia-elenchus are low. dia-confirm, dia-brainstorm and dia-iterate have none.
- **Routing risk.** It would attract "analyze this argument" and "what is the hidden assumption" requests, which today fall to dia-reductio ("follows from its premises") or to no skill at all. The description must keep "contradiction" and "follows strictly" out.
- **Tool-less.** Yes.

### 2.2 Pragma-dialectics (van Eemeren & Grootendorst)

- **Source.** *A Systematic Theory of Argumentation* (CUP 2004): ch. 3 on the model of a critical discussion, ch. 6 on the rules (p. 135), ch. 7 on fallacies, and ch. 8 "Ten commandments for reasonable discussants" (p. 190) [7]. The full procedure has 15 rules [8][9]. The approach aims at the reasonable resolution of a difference of opinion [1].
- **Procedure.** There are four stages. In the confrontation stage the difference is externalised; in the opening stage the parties fix common starting points and roles (protagonist, antagonist); in the argumentation stage the protagonist defends and the antagonist challenges; in the concluding stage the standpoint is either retracted or accepted [9]. The ten rules are: freedom, burden of proof, standpoint, relevance, unexpressed premise, starting point, argument scheme, validity, closure and usage [10]. A violation of a rule is a fallacy [10].
- **Roles in a chat.** In the canonical analytic use, the assistant reconstructs an exchange (the user's, or a pasted one) and reports which moves broke which rule. A live use is possible, with the assistant as antagonist and the user as protagonist, but the model is an ideal for two parties who both commit to it.
- **AI risks.** The starting-point and closure rules suit an assistant well: argue only from agreed premises, and retract when the defence fails, which is a rule against yielding without grounds. The unexpressed-premise rule is a direct guard against inventing premises the user never held. Labelling the user's move a "fallacy" invites defensive pushback.
- **Human-AI evidence.** None that I opened. I found fallacy-classification papers but did not read them, so I cite none.
- **Overlap.** High with dia-elenchus (agreed premises only), dia-reductio (the validity rule) and candidate 2.1.
- **Routing risk.** It would attract "is this a fallacy" requests, which have no home today.
- **Fidelity.** Medium: a one-sided audit of a two-party ideal is a reduced use.
- **Verdict.** Fold the unexpressed-premise, standpoint and usage rules into 2.1 as charity rules. No standalone skill.

### 2.3 Walton: dialogue types and argumentation schemes

- **Source.** Walton & Krabbe (1995, p. 66) list six types of dialogue, each with an initial situation and a goal: persuasion, negotiation, inquiry, deliberation, information-seeking and eristic [11]. In *Argumentation Schemes* (Walton, Reed & Macagno 2008), schemes are defeasible forms, 65 of them in the compendium, each assessed by its critical questions (CQs). An instance is acceptable if its premises are acceptable and its CQs can be answered. Example: two-person practical reasoning, with CQ1–CQ5 on conflicting goals, alternative means, side effects, possibility and further actions [12]. A reviewer notes that real arguments often fit several schemes, and that the set of schemes is open-ended [12].
- **Roles in a chat.** The assistant names the scheme and asks or answers its CQs; the user owns the argument.
- **AI risks.** CQs *ask* rather than assert counter-facts. The CQ-generation task was proposed precisely to avoid LLM hallucination in counterargument, since it needs no outside knowledge [13]. That fits a tool-less chat and lowers the risk of invented sources.
- **Human-AI evidence.** LLMs are "reasonable CQ generators" with "a wide margin for improvement" [13]. In the 2025 shared task the best accuracy was 67.6, and three of the top four teams used scheme annotations [14]. Both are LLM-only evaluations, without users.
- **Verdict.** Dialogue types: low value as a skill; useful at most as a routing note. Schemes and CQs: fold into 2.1 as the warrant test, keeping a short reference table of common schemes (practical reasoning, expert opinion, cause to effect, analogy, sign) in the skill's own wording.

### 2.4 Rapoport's rules, steelmanning, Ideological Turing Test

- **Source.** Dennett, *Intuition Pumps* (2013), ch. 2, gives four rules: re-express the target's position so well that the target says "Thanks, I wish I'd thought of putting it that way"; list points of agreement; mention what you learned; only then criticise [15][16]. Dennett's footnote says this wording is his own, "done from memory". The source is Rapoport's *Fights, Games, and Debates* (1960) and "Three Modes of Conflict" (1961), which credit rule 1 to Carl Rogers [16]. Rapoport's Part III chapters are "The Assurance of Understanding", "The Region of Validity" and "The Assumption of Similarity" [17]. They state the opponent's case to their satisfaction, state the conditions under which it is justified, and look for one's own flaws as well as theirs [18]. Research on role reversal found that it works depending on the issue and the situation [18]. Caplan's Ideological Turing Test asks people to state opposing views "as clearly and persuasively as their proponents". It is a *test* judged by adherents of the view, for example in a chat room where members vote on who is not really one of them [19].
- **Roles in a chat.** Either the assistant restates a third party's view (an absent opponent), or it restates the user's own view and the user judges it.
- **AI risks.** *Invented positions:* restating an absent opponent invites a plausible but unsourced caricature, or an over-strong one. It must quote or mark what is reconstruction. *Sycophancy:* steelmanning the user's own view is flattery-shaped. *ITT:* only adherents can judge, so an assistant cannot pass or grade one alone; the user can judge only a restatement of their own side.
- **Human-AI evidence.** None specific that I opened.
- **Overlap.** dia-brainstorm Step 1 already steelmans the user's idea (partial); dia-reductio's "charity first" (partial).
- **Routing risk.** Low: no sibling description says "steelman" or "the other side's best case".
- **Fidelity.** High for Dennett's four steps as written, honestly labelled as his reformulation. Medium for Rapoport's three principles. Low for the ITT, which needs judges a chat does not have.

### 2.5 Double Crux (CFAR)

- **Source.** Sabien (CFAR, 2017). For a disagreement over A, both parties seek a B such that they disagree about B, and B is crucial to each side's view of A. The handbook algorithm: find a disagreement; operationalise it (define terms, test cases, actions over beliefs); seek double cruxes, alone and then together, with falsifiability prompts ("It would take A, B, or C to make me stop believing X"); "resonate"; repeat. Its preconditions are epistemic humility, good faith, belief in objective truth, and curiosity. It warns against "guessing at the shape of our opponent's belief structure". CFAR calls it "a folk recipe" whose algorithm "has some holes and weirdnesses" [20]. The only efficacy work I found is a 2019 proposal for a test, not a result [50].
- **Roles in a chat.** Both parties must hold beliefs. With one user, either the assistant adopts not-A, which manufactures a disagreement and its cruxes, or it models an absent person, which is the guesswork CFAR warns against.
- **AI risks.** All four are worsened: the assistant's "belief" can be bent to please the user, and the absent party's cruxes are invented.
- **Fit for AI chat.** Low.
- **Verdict.** Skip. The one transferable move, "what would change your mind", is already dia-brainstorm's falsification pull.

### 2.6 Street Epistemology (Boghossian; Magnabosco)

- **Source.** The term comes from Boghossian, *A Manual for Creating Atheists* (2013); *How to Have Impossible Conversations* (2019) is the broader update [21]. The community guide drops the book's "virus/intervention" metaphors and extends the method to all beliefs. Its steps: elicit a claim; ask for confidence on a 0–100 scale; ask how the person originally concluded the claim was true (their method of knowing); test that method's reliability with outsider and defeasibility tests; ask for confidence again at the end. Throughout it keeps "doxastic openness", and the aim is "changing the way people form beliefs", not the belief itself [22]. The guide describes itself as Socratic method/elenchus plus reliabilism [22].
- **Roles in a chat.** The assistant questions; the user holds the belief.
- **AI risks.** It inverts sycophancy into sustained, agenda-driven pressure on the user's beliefs (the method's origin is persuasion out of faith [22]). The 0–100 rating invites the user to report a change in order to please.
- **Human-AI evidence.** None found.
- **Overlap.** High with dia-elenchus (one question at a time, Socratic, ends in "knowing you don't know"; the guide's ideal end is the "spider moment" [22]) and with dia-brainstorm's evidence probes.
- **Routing risk.** High against dia-elenchus.
- **Verdict.** Skip.

### 2.7 Dialectical inquiry (DI) and devil's advocacy (DA)

- **Source.** Mason (1969, *Management Science* 15(8): B403–B414) sets two criteria: a planning technique should expose the assumptions under a plan, and it should suggest new, more relevant ones. His case was a field study at RMK Abrasives [23]. There, the plan's ten underlying assumptions were identified, a counterplan was built on opposite assumptions, and the two were debated in a structured way before management [27]. DA identifies the assumptions and builds a critique of them *without* a counterplan [27][26]. Cosier: "dialectical inquiry requires specification of an alternative course of action", and DA may get the benefit without it [28].
- **Evidence.**
  - DI and DA both gave higher-quality recommendations and assumptions than consensus. DI beat DA on the quality of assumptions. Consensus groups were more satisfied [24].
  - In the 1989 longitudinal study: DI = DA > consensus on decision quality, more re-evaluation of one's own assumptions, and lower acceptance of the group decision [25].
  - DI and DA groups exceeded the average of their members, and on several measures the best member [43].
  - Lab studies favoured DA over DI for performance [27]. A "carping critic" DA did not help where an objective DA did, and DA works only if decision-makers sincerely accept questioning [26].
  - Schwenk's meta-analyses (1989, 1990) exist [29][30]; I read only an abstract that reports conclusions differing from an earlier review, without stating them [30], so their direction is [unverified].
- **Roles in a chat.** The user is the decision-maker and judge. The assistant extracts the plan's assumptions, negates them, and writes the counterplan (DI) or the assumption critique (DA). Synthesis is the user's.
- **AI risks.**
  - *One model plays both sides.* This departs from the original's separate advocates. It is mitigated because the counterplan is built mechanically from listed negated assumptions, so the user can check that each side rests on its stated premises.
  - *Sycophancy.* The structure counters it, because the assistant must argue against the user's plan or its own earlier recommendation. Under pushback, a counter-assumption should go only when the user supplies a fact.
  - *Over-reliance.* The decision stays with the user, and the assistant does not pick.
  - *Invented facts.* The counterplan rests on the plan's own data reinterpreted; outside facts carry evidence classes.
- **Human-AI evidence (nearest analogues).** LLM devil's advocates that argued against the *AI's* recommendation promoted appropriate reliance on AI in group decisions; interactive ones felt more collaborative [40]. An LLM devil's advocate in power-imbalanced groups raised process and outcome satisfaction; accuracy is not reported in the abstract [41]. Both studied groups, not one user.
- **Overlap.** dia-brainstorm is partial: its `stress` mode "pokes holes", but one question at a time, with user-generated options and no counterplan. dia-negative is low (claim against delivery, not assumptions against counterplan). dia-reductio is low. dia-refine and dia-iterate have none.
- **Routing risk.** High against dia-brainstorm, whose description owns "poke holes" and "stress-test". The new description must use "devil's advocate", "argue the other side", "counterplan", "what if our assumptions are wrong", and must cede "poke holes" and "stress-test".
- **Tool-less.** Yes; one pass.

### 2.8 Pre-mortem (contrast)

- **Source.** Klein (2007): assume that the project "has just failed", then generate plausible reasons [31]. The cited basis is Mitchell, Russo & Pennington (1989). That paper found the effect came from outcome *certainty*, not temporal perspective. Sure outcomes yielded more reasons (Exp. 2: 4.60 vs 3.28) and more episodic ones. The authors say this is "seeing more, which is not necessarily the same as seeing better" [45].
- **Later evidence.** In Veinott, Klein & Wiggins (2010), with 178 participants and five conditions, the premortem reduced confidence more than critique, pros/cons or cons-only [46]. In Gallop et al. (2016), premortem teams found better-quality risks, more quality plan changes and more "black swan" risks than brainstorming teams [47]. In a thesis supervised by Veinott, the *individual* premortem produced the least change in confidence: "group discussion is an important factor" [48].
- **Fit for AI chat.** Medium. A one-user chat is the individual case [48], and the assistant writing failure stories invents rather than surfaces team knowledge.
- **Verdict.** Keep it as dia-brainstorm's existing premortem lens; add no skill.

### 2.9 LLM debate, and a single-assistant "debate" skill

- **Source.**
  - Irving et al.: two agents in a zero-sum game, a human judge, trained by self-play. The PSPACE argument assumes optimal play [32].
  - Du et al.: several instances debate over rounds and gain on reasoning and factuality [33].
  - Khan et al.: two expert debaters see a hidden text the judge lacks, and quotes are checked by a tool. Human judges reach 88% with debate, 78% with consultancy (one advocate) and 60% with no expert [34]. Incorrect consultants mislead judges; consultancy accuracy falls as consultants are optimised for persuasiveness; LLM judges sometimes credit unverified quotes [34].
  - Smit et al.: multi-agent debate does not reliably beat self-consistency [35].
  - Wang et al.: a single agent with strong prompts nearly matches the best discussion [37].
  - Huang et al.: debate is no better than self-consistency at equal responses [38].
  - Liang et al.: self-reflection suffers "Degeneration-of-Thought", and LLM judges may be unfair [36].
- **What transfers to one assistant.** Not the mechanism: there is no information asymmetry, no independent or trained debaters, and no quote verifier on a tool-less surface. What transfers is the *format*: two strongest cases, one per answer, put before a human judge, with any quotation tied to material the user supplied. That is DI's plan versus counterplan (2.7).
- **Consultancy and ordinary chat.** Khan's consultancy, one advocate for an assigned answer [34], resembles an ordinary chat answer only loosely, since an assistant is not assigned a side at random. Treating the two as the same is interpretation, not a finding.
- **AI risks.** Sycophancy is broad: assistants match the user's views, and people prefer such answers [39]. Across 11 models, assistants affirm users' actions 50% more than humans do, and people trust sycophantic models more [42]. A two-sided format does not prevent the assistant from writing the user's preferred side stronger. I found no evidence that one model writing both sides counters sycophancy.
- **Verdict.** Do not name a skill "debate". The name implies mechanisms and results that a single chat lacks.

## 3. Check of the external proposal

| Claim | Status | Why |
|---|---|---|
| Khan: humans 60% / 78% / 88% (naive / consultancy / debate) | confirmed | Exact figures in the paper [34] |
| Khan: a more persuasive consultant lowered accuracy | partly | Shown for consultancy under persuasiveness optimisation; for humans the paper reports incorrect consultants cause low accuracy [34] |
| "Consultancy has the same structure as ordinary chat" | unverifiable | Interpretation. The consultant is assigned a side; an assistant is not [34] |
| Schweiger & Sandberg 1989: DI/DA groups beat their members' average | confirmed | Also beat the best member on several measures [43] |
| "Better than consensus" comes from prior work cited | confirmed | The abstract says "previous research" [43], i.e. 1986 [24] (also shown again in 1989 AMJ [25]) |
| Lee 2025 (48 people): an LLM devil's advocate raised satisfaction; no accuracy in the abstract | confirmed | 12 four-person power-imbalanced groups; process and outcome satisfaction [41] |
| Cheng 2025: 11 models affirm users ~50% more than humans | confirmed | [42] |
| Cheng 2025: "a 1,604-person experiment"; people preferred and trusted sycophantic AI | partly | Two preregistered experiments, N = 1,604 in total; higher quality ratings and more trust confirmed [42] |
| dia-debate "structurally counters sycophancy" | unverifiable | No study of one model writing both sides was found; see 2.9 |
| dia-debate is the best fit for the name "dialectic" | not evidence | Matter of naming; the procedure proposed is Mason's DI (2.7), which has a primary source to be faithful to |
| Premortem 1989: ~30% more reasons | partly | The effect is from outcome certainty, not "already happened" (no temporal effect); Exp. 2 shows about 40% more (4.60 vs 3.28); quality was not assessed [45]. The 30% wording is Klein's [44] |
| Premortem: 178 students; confidence fell ~twice as much as pros/cons; rebound after fixes | partly | 178, five conditions, and "more than each" are confirmed from the abstract [46]; "twice" and the rebound appear only in secondary summaries [44] |
| Premortem: 101 practitioners; more high-quality risks than brainstorming | partly | The direction is confirmed [47]; N = 101 only in the secondary summary [44] |
| Premortem: no study tracks real project outcomes | partly | A field exercise with cadets found fewer fouls and less fixation [48]; I found no business-outcome study |
| Argument mapping: ~0.8 SD in intensive courses; author conflict of interest | confirmed | 0.8 SD attributed to van Gelder (2015); van Gelder co-wrote the chapter and "developed Rationale" [49] |
| Argument mapping "overlaps dia-reductio" | wrong | dia-reductio handles only strict contradiction; defeasible support (Toulmin, schemes) is outside it (2.1) |
| Double crux: only a proposal post to test efficacy | confirmed | [50]; no result found |

The check changes my ranking in one way. The external dia-debate *procedure* is dialectical inquiry, so I recommend it under that method's own source and honest label, as `dia-counterplan`, not as "debate". dia-premortem stays a lens.

## 4. Comparison

| Candidate | Fidelity | Fit for AI chat | Overlap | User value | Recommendation |
|---|---|---|---|---|---|
| Dialectical inquiry / devil's advocacy | high | high | partial (dia-brainstorm stress) | high | **ADD** `dia-counterplan`: lab and LLM evidence, user judges, counters yielding |
| Toulmin + Walton critical questions | high | high | partial (dia-reductio, dia-refine) | high | **ADD** `dia-warrant`: covers defeasible arguments that no skill covers |
| Rapoport's rules / steelman | high (Dennett's form) | medium | partial (dia-brainstorm Step 1) | medium | **ADD later** `dia-steelman`, or hold |
| Pragma-dialectics | medium | medium | high (dia-elenchus, dia-reductio) | medium | FOLD three rules into dia-warrant |
| Walton dialogue types | high | low | none | low | SKIP: a taxonomy, not a procedure |
| Ideological Turing Test | low | low | none | low | SKIP: needs adherent judges |
| Double Crux | medium | low | partial (dia-brainstorm) | low | SKIP: needs two believers; no efficacy data |
| Street Epistemology | medium | low | high (dia-elenchus) | low | SKIP: overlap; agenda pressure |
| Pre-mortem | high | medium | high (dia-brainstorm lens) | medium | SKIP: lens exists; the individual case is weak |
| Single-assistant "debate" | low | low | partial | medium | SKIP the name; the format lives in dia-counterplan |

## 5. Ranked recommendation

1. **`dia-counterplan`.**
   - *Label:* "Dialectical inquiry after Mason (1969), with a devil's-advocate variant, adapted for one assistant and one decision-maker: the same assistant writes both sides, the groups and separate advocates of the original are absent, and the synthesis is the user's."
   - *Steps:*
     1. State the plan or recommendation, which may be the user's, a pasted text or the assistant's own earlier answer.
     2. List its assumptions, numbered, each quoted or marked as reconstructed.
     3. Mark the assumptions that do the work.
     4. Negate those and build the most credible counterplan on the same data (DI), or, if the user asks for a critique only, an assumption critique (DA).
     5. Set plan and counterplan side by side, assumption by assumption.
     6. Name the observation that would favour each side.
     7. Hand the decision to the user and end with a record.
   - *Stop rule:* one pass; follow-ups only re-run with changed assumptions.
   - *Never:* pick the winner unasked; weaken the counterplan under pushback without a supplied fact (the "withdraw only a named defect" rule of the siblings); be a "carping critic" [26]; invent figures or sources; use "poke holes" or "stress-test" in the description.
2. **`dia-warrant`.**
   - *Label:* "Argument layout after Toulmin (1958), with each warrant tested by the critical questions of its argumentation scheme (Walton, Reed & Macagno 2008); a reconstruction, not Toulmin's own critique of formal logic."
   - *Steps:*
     1. Quote the claim.
     2. Ask or fill in the data, warrant, backing, qualifier and rebuttal conditions, marking each as stated or reconstructed.
     3. Name the likely scheme (two candidates if it is ambiguous [12]).
     4. Pose its critical questions and mark each as answered by the text, by the user, or open.
     5. Report which link is weakest.
   - *Stop rule:* one pass, or one question per turn if the user asks for that.
   - *Never:* call a defeasible argument "invalid"; attribute a warrant the author would disown (pragma-dialectical unexpressed-premise rule [10]); assert counter-facts instead of asking.
3. **`dia-steelman`** (lower priority).
   - *Label:* "Rapoport's rules in Dennett's 2013 wording, which Dennett calls his own; not an Ideological Turing Test, which only adherents can judge."
   - *Steps:* restate the target view, quoting it; state its region of validity; list the agreements; say what you learned; only then criticise.
   - *Never:* invent the opponent's words; steelman the user's own view as praise.

## 6. Open questions for the owner

1. One skill with a DA variant, or DI only? Lab studies favour DA on performance [27][26]; the AMJ studies find DI = DA on quality [25].
2. Should dia-counterplan run on the assistant's *own* earlier recommendation by default, which is the condition with LLM evidence for appropriate reliance [40]?
3. Should dia-brainstorm's description give up "poke holes" or "stress-test" if dia-counterplan is added, or keep them and route "devil's advocate" and "counterplan" only?
4. Is a short table of argumentation schemes, in our own wording, acceptable as a shipped reference for dia-warrant?
5. Is `dia-steelman` wanted at all, given its overlap with dia-brainstorm Step 1?

## Sources

[1] https://plato.stanford.edu/entries/argument — SEP — Argument and Argumentation
[2] https://link.springer.com/rwe/10.1007/978-94-007-6883-3_4-1 — van Eemeren et al. (2014), Toulmin's Model of Argumentation, Handbook of Argumentation Theory (abstract and notes)
[3] http://assets.cambridge.org/97805218/27485/sample/9780521827485ws.pdf — Toulmin, The Uses of Argument, updated ed. (CUP 2003), sample with contents
[4] https://www.ai.rug.nl/~verheij/publications/pdf/toulmin2009.pdf — Verheij (2009), The Toulmin Argument Model in Artificial Intelligence
[5] https://aclanthology.org/2024.acl-long.552 — Gupta, Zuckerman, O'Connor (ACL 2024), Harnessing Toulmin's theory for zero-shot argument explication
[6] https://arxiv.org/abs/2412.15177 — Castagna, Sassoon, Parsons (2024), Critical-Questions-of-Thought
[7] https://api.pageplace.de/preview/DT0400.9780511162459_A23689806/preview-9780511162459_A23689806.pdf — van Eemeren & Grootendorst (2004), A Systematic Theory of Argumentation, CUP preview (contents)
[8] https://link.springer.com/article/10.1023/A:1026334218681 — van Eemeren & Grootendorst (2003), A Pragma-dialectical Procedure for a Critical Discussion, Argumentation 17
[9] https://pure.uva.nl/ws/files/1374083/108207_jv_1_.pdf — Visser, Bex, Reed, Garssen (2011), Correspondence between the pragma-dialectical discussion model and AIF
[10] https://en.wikipedia.org/wiki/Pragma-dialectics — Wikipedia — Pragma-dialectics (ten rules)
[11] https://philarchive.org/archive/WALTOD-2 — Walton & Macagno (2007), Types of Dialogue, Dialectical Relevance and Textual Congruity
[12] https://ndpr.nd.edu/reviews/argumentation-schemes — Groarke (2009), NDPR review of Walton, Reed & Macagno, Argumentation Schemes (CUP 2008)
[13] https://doi.org/10.18653/v1/2024.conll-1.9 — Calvo Figueras & Agerri (CoNLL 2024), Critical Questions Generation: Motivation and Challenges
[14] https://aclanthology.org/2025.argmining-1.23 — Calvo Figueras et al. (ArgMining 2025), Overview of the Critical Questions Generation Shared Task
[15] https://www.themarginalian.org/2014/03/28/daniel-dennett-rapoport-rules-criticism — The Marginalian — Dennett on Rapoport's Rules
[16] http://tparent.net/Dennett_excerpts.pdf — Dennett (2013), Intuition Pumps, ch. 2 excerpts (Rapoport's Rules and footnote 2)
[17] https://press.umich.edu/Books/F/Fights-Games-and-Debates — Rapoport, Fights, Games, and Debates — University of Michigan Press (contents)
[18] https://en.wikipedia.org/wiki/Rogerian_argument — Wikipedia — Rogerian argument (Rapoport's principles, role-reversal research)
[19] https://www.econlib.org/archives/2011/06/the_ideological.html — Caplan (2011), The Ideological Turing Test, Econlib
[20] https://www.lesswrong.com/posts/exa5kmvopeRyfJgCy/double-crux-a-strategy-for-resolving-disagreement — Sabien (CFAR, 2017), Double Crux — A Strategy for Mutual Understanding
[21] https://www.streetepistemology.com/blog/how-to-get-started-with-street-epistemology — Magnabosco (2020), How to Get Started with Street Epistemology
[22] https://capturingchristianity.com/wp-content/uploads/2017/11/The-Complete-Street-Epistemology-Guide.pdf — The Complete Street Epistemology Guide (community guide, 2016)
[23] https://ideas.repec.org/a/inm/ormnsc/v15y1969i8pb403-b414.html — Mason (1969), A Dialectical Approach to Strategic Planning, Management Science (abstract)
[24] https://journals.aom.org/doi/abs/10.5465/255859?journalCode=amj — Schweiger, Sandberg, Ragan (1986), AMJ 29 (abstract)
[25] https://journals.aom.org/doi/abs/10.5465/256567 — Schweiger, Sandberg, Rechner (1989), AMJ (abstract)
[26] https://hdl.handle.net/2142/29170 — Schwenk (1984), The use of devil's advocates in strategic decision-making (working paper)
[27] http://hdl.handle.net/2142/27062 — Schwenk, Dialectical inquiry: decision-makers' perceptions of its effectiveness, BEBR 814
[28] https://journals.aom.org/doi/10.5465/amr.1981.4285716 — Cosier (1981), Dialectical Inquiry in Strategic Planning: A Case of Premature Acceptance, AMR
[29] https://ideas.repec.org/a/eee/jobhdp/v47y1990i1p161-176.html — Schwenk (1990), Effects of devil's advocacy and dialectical inquiry: a meta-analysis, OBHDP (record)
[30] https://doi.org/10.1002/smj.4250100309 — Schwenk (1989), A meta-analysis on the comparative effectiveness of DA and DI, SMJ (abstract)
[31] https://hbr.org/2007/09/performing-a-project-premortem — Klein (2007), Performing a Project Premortem, HBR
[32] https://arxiv.org/abs/1805.00899 — Irving, Christiano, Amodei (2018), AI safety via debate
[33] https://arxiv.org/abs/2305.14325 — Du et al. (2023), Improving Factuality and Reasoning through Multiagent Debate
[34] https://arxiv.org/html/2402.06782v4 — Khan et al. (ICML 2024), Debating with More Persuasive LLMs Leads to More Truthful Answers
[35] https://arxiv.org/abs/2311.17371 — Smit et al. (ICML 2024), Should we be going MAD?
[36] https://arxiv.org/abs/2305.19118 — Liang et al. (2023), Encouraging Divergent Thinking through Multi-Agent Debate
[37] https://arxiv.org/abs/2402.18272 — Wang et al. (2024), Rethinking the Bounds of LLM Reasoning: Are Multi-Agent Discussions the Key?
[38] https://arxiv.org/abs/2310.01798 — Huang et al. (ICLR 2024), Large Language Models Cannot Self-Correct Reasoning Yet
[39] https://arxiv.org/abs/2310.13548 — Sharma et al. (2023), Towards Understanding Sycophancy in Language Models
[40] https://dl.acm.org/doi/fullHtml/10.1145/3640543.3645199 — Chiang, Lu, Li, Yin (IUI 2024), LLM-Powered Devil's Advocate
[41] https://arxiv.org/abs/2503.14263 — Lee, Hwang, Kim, Lee (2025), Conversational Agents as Catalysts for Critical Thinking
[42] https://arxiv.org/abs/2510.01395 — Cheng et al. (2025), Sycophantic AI Decreases Prosocial Intentions and Promotes Dependence
[43] https://ideas.repec.org/a/bla/stratm/v10y1989i1p31-43.html — Schweiger & Sandberg (1989), The utilization of individual capabilities in group approaches, SMJ 10 (abstract)
[44] https://corporate.jcx.au/premortem — Course notes on behavioural economics, ch. 30 The premortem (secondary summary)
[45] https://www.onsecondthought.me/8/TIP5_MitchellRussoandPennington1989JBDM.pdf — Mitchell, Russo, Pennington (1989), Back to the Future, JBDM 2:25-38 (full text)
[46] https://www.academia.edu/103566494/Evaluating_the_Effectiveness_of_the_PreMortem_Technique_on_Plan_Confidence — Veinott, Klein, Wiggins (2010), Evaluating the effectiveness of the PreMortem technique, ISCRAM (abstract)
[47] https://doi.org/10.1080/19488289.2016.1240118 — Gallop, Willy, Bischoff (2016), How to catch a black swan, J. Enterprise Transformation (abstract)
[48] https://doi.org/10.37099/mtu.dc.etdr/374 — Peabody (2017), Improving Planning: Quantitative Evaluation of the Premortem Technique, MTU thesis
[49] https://ecampusontario.pressbooks.pub/criticalthinking1234/chapter/introduction — Davies, Barnett, van Gelder, Using Computer-Aided Argument Mapping to Teach Reasoning
[50] https://www.greaterwrong.com/posts/mnszbzJ2XawR4wXJh/testing-the-efficacy-of-disagreement-resolution-techniques — Fernandez (2019), Testing the Efficacy of Disagreement Resolution Techniques (proposal)
