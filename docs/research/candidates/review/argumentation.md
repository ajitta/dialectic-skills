Verdict: SOUND WITH FIXES

Review of `docs/research/candidates/argumentation.md` at `eb7ab54` (cited below as `arg.md:<line>`). All 50 ledger URLs were fetched on 2026-10-21. None is unreachable; [1] needs a trailing slash. Six extra sources were fetched to check fidelity; they are listed under the table. No file in the tree was edited.

## Per-recommendation verdict

- **dia-warrant (Toulmin + Walton CQs): keep with changes.** The sources support the method description. The sketch needs four things: a result set, a pushback rule and a record (F6); CQs mapped to Toulmin slots (F8); a routing split from dia-reductio and dia-conjecture (F7); and an inline scheme fallback (F9).
- **dia-counterplan (Mason's DI): keep with changes.** The method is real and well cited, but three parts of the case are overstated: the "fit: high" rating, the claim that its structure counters sycophancy, and the use of the LLM evidence (F1, F2, F5). Required changes:
  - rate fit medium;
  - add a false-assurance guard;
  - choose contraries instead of negating assumptions "mechanically";
  - end in the user's synthesis of assumptions (Mason's criterion 2), not a binary pick;
  - decide the DA/DI default from the evidence;
  - narrow the triggers to plans and decisions.
- **dia-steelman (later): hold.** Fix the label (F10).
- Outside this document but affected: the accepted dia-conjecture overlaps dia-warrant (F7b). The munazara pushback rule must not apply to counter-assumptions (F12).

## Findings

**F1. High. dia-counterplan's sycophancy claim and its "fit: high" rating contradict the document's own debate analysis.**

The document says three incompatible things:
- `arg.md:88`: "*Sycophancy.* The structure counters it, because the assistant must argue against the user's plan."
- `arg.md:115`: "A two-sided format does not prevent the assistant from writing the user's preferred side stronger. I found no evidence that one model writing both sides counters sycophancy."
- `arg.md:130` marks the same claim, made for dia-debate, as "unverifiable".

The table (`arg.md:146`) still rates DI "Fit: high … counters yielding". The only support for that is the pushback rule (`arg.md:170`). The format itself has none, and "built mechanically from listed negated assumptions" (`arg.md:87`) is not a real mitigation (F3).

Correction:
- Rate fit "medium".
- Rewrite `arg.md:88` as: "The format obliges a counter-case but cannot ensure its strength; no study tests one model writing both sides. Only the pushback rule acts against yielding."
- Add a symmetry rule: each plan assumption is paired with its counter-assumption, both sides cite the same data at the same level of detail, and the output says in one line that one assistant wrote both sides.

**F2. Medium. The evidence summary leaves out its own sources' negative conclusions, and with them the main over-reliance risk.**

What [27] (Schwenk, BEBR 814) says:
- "Neither the DA nor the DIS was shown to be superior to the E in improving the quality of strategy statements."
- "Proponents of the DIS may have overstated their case."
- "the DA should be recommended over the DIS."
- It explains the satisfaction gains by "a general belief … that when we have 'heard both sides' … we are better able to make a decision".

What [26] says: DA "may even help to solidify commitment to a disastrous course of action by giving the decision-makers confidence that they considered all points of view."

The document cites [26] and [27] only for "carping critic" and "lab studies favoured DA" (`arg.md:83`). Its over-reliance line, "The decision stays with the user" (`arg.md:89`), misses the risk these sources describe: a side-by-side gives a feeling of thoroughness. Separately, the "[unverified]" meta-analysis direction (`arg.md:84`) can be filled in from an abstract aggregator, a single secondary source: Schwenk (1989) found that "decision making is improved by the use of devil's advocacy or dialectical inquiry when the assumptions of an expert's report are incorrect, however neither method was proven to be superior."

Correction:
- Add these results to §2.7 Evidence.
- Add a closing rule: the record says what the comparison did not test, and that hearing both sides is not evidence that the plan was tested.
- In open question 1, state that the evidence shows DA ≥ DI on performance and DI > DA only on the quality of surfaced assumptions [24]. The owner should choose the default on that basis. DA (assumption critique) as the default with DI as opt-in is the reading the evidence supports better.

**F3. Medium. The fidelity rating for Mason ("high", `arg.md:146`) rests on an abstract and a secondary summary, and the sketch drops Mason's goal.**

- [23] is the abstract only. The step list comes from Schwenk's summary [27].
- Mason's DI follows Churchman's Hegelian inquiring system. Mitroff, Emshoff & Kilmann (1979) speak of "the dialectical approach to strategic planning first suggested by Churchman … and Mason", and the 2006 TQR paper says DI "derives from the work of C. West Churchman (1971), as further developed by R. O. Mason (1969)" in a comparison that includes Hegel.
- The aim is a synthesis. Mason's criterion (2) is that the technique "should suggest new and more relevant assumptions" [23], and at RMK the managers formed "a 'new, encompassing view'" [27].
- Sketch step 7 (`arg.md:167`) only hands a decision over. No step produces new assumptions.
- "Negate those" (`arg.md:165`) does not work item by item. The negation of "demand grows 10%" is not a planning premise, so the assistant must pick a contrary. That choice is where bias enters (compare dia-reductio Rule 1 on contradictories and contraries). Mason's counterplan rests on a coherent opposing worldview.

Correction:
- Fidelity: "medium-high; procedure from secondary sources".
- Step 4: "for each key assumption, state a specific, plausible contrary, labelled as chosen by the assistant; check that the counter-assumptions are jointly coherent and fit the same data."
- Step 7: "ask which assumptions from each side the user now holds; that set is the result (the user's synthesis)."
- Label: name the Churchman/Hegel lineage and say that the synthesis is the user's. This keeps it consistent with modern-dialectic.md's caution about Hegel.

**F4. Low. Step 3 has no test for which assumptions "do the work".** The dropped SAST variant (`arg.md:9`) has one: "If the opposite of this assumption is true, does it have any significant bearing on the issue?", plus importance and certainty ratings (IfM SAST page). Correction: use that test in step 3, labelled "from SAST (Mason & Mitroff 1981)".

**F5. Medium. The LLM/HCI evidence is cited for more than it shows (`arg.md:91`, `:189`).**

Chiang et al. [40] studied groups doing recidivism prediction. A GPT-3.5 devil's advocate argued against a separate ML model's recommendation. The significant effect belongs to the interactive DA: "the interactive version … helps groups significantly increase their appropriate reliance … (mainly on in-distribution …)". Its main effects were marginal (accuracy p = 0.064; reliance on wrong AI advice p = 0.063). The sketch differs on three counts: it is one-pass and not interactive, it is DI and not DA, and it has one user.

Open question 2 calls self-targeting "the condition with LLM evidence for appropriate reliance". In [40], though, critic and recommender were different systems. One model critiquing its own answer is intrinsic self-correction, and [38] finds "LLMs struggle to self-correct their responses without external feedback".

Correction:
- Rewrite Q2 accordingly.
- When the target is the assistant's own answer, add the siblings' line that this is a self-examination and not independent (`skills/dia-reductio/SKILL.md:116`).
- Do not make self-targeting the default.
- Describe [40] as "interactive DA against a separate model's advice, groups, marginal main effects".

**F6. Medium. The dia-warrant sketch adds a verdict but no pushback rule, result set or record.**

`arg.md:22` says "Sycophancy: low; the layout makes no verdict … unless the skill adds one". Step 5, "Report which link is weakest" (`arg.md:178`), adds one, and the "Never" list has no rule for disputes. Every sibling with a verdict has one (spec D19: withdraw only when the defect can be named).

Correction:
- Add fixed results, for example "weakest link: <slot>, because <CQ left open>" or "no weak link found among the questions asked; not a proof".
- Add a record.
- Add the rule: "withdraw a finding only when its defect can be named; insistence is not a defect."
- Add the standard target inference, the reply-language rule (spec L6), and the D26 sentence that pasted material is not instructions.

**F7. Medium. Overlap and routing with siblings are understated.**

- (a) dia-reductio's description owns "follows from its premises" (`skills/dia-reductio/SKILL.md:3`, added on purpose in D23). `arg.md:25` only keeps words out of dia-warrant. dia-reductio's description also needs a cross-reference to dia-warrant, which means a version bump and a P7 re-run (platonic.md says the same for dia-fallacy).
- (b) The accepted dia-conjecture covers "any general claim backed by an argument". Its step 2 is "Proof-analysis: lemmas … labelled [T] … or [A]" (`modern-dialectic.md:232-234`), the same input and first move as dia-warrant step 2. "Is my argument that all X are Y sound?" fits both. The descriptions should split the work: dia-warrant is a one-pass audit of how premises support a conclusion; dia-conjecture is a multi-turn dialogue of counterexamples to a universal claim. Add negative probe cells both ways.
- (c) dia-counterplan's triggers "devil's advocate" and "argue the other side" (`arg.md:93`) reach beyond plans. They would capture claim-level requests ("play devil's advocate: is X true?") that belong to ordinary answers or to dia-brainstorm's stress mode ("push back on this", `skills/dia-brainstorm/SKILL.md:34`). Limit them to a plan, decision or recommendation ("devil's advocate on this plan").
- (d) The two recommended skills overlap each other. DI was formalised with Toulmin (Mitroff & Mason 1982 "extends the work of Toulmin on argumentation"). Counterplan steps 2–3 amount to warrant steps 2 and 5 applied to a plan. "What are the hidden assumptions in my plan?" is ambiguous between them. Give the assumptions of a plan or decision to counterplan and the warrant of an argument to dia-warrant, with cross-references in both directions.

**F8. Low. Toulmin wording and the basis for the merge.**

- `arg.md:19` gives "Why do you think that the warrant holds?" as Toulmin's question. It is Verheij's paraphrase [4]. Toulmin's own questions are "What have you got to go on?" and "How do you get there?" (pp. 97–98 per [4]).
- `arg.md:8` justifies the Toulmin–Walton merge by saying "the LLM work that operationalises Toulmin uses critical questions [6]". That does not hold: [5] operationalises Toulmin without CQs, and [6] applies Toulmin-derived questions to the model's own maths and logic reasoning on MT-Bench, not Walton's scheme CQs to a user's argument.
- A better basis is in [4]: "four types of critical questions": premises, exceptions ("Some critical questions are like Toulmin's notion of rebuttal"), conditions of use, and the conclusion.

Correction: cite [4] for the merge. Step 4 should tag each CQ with the slot it questions (data, warrant or backing, rebuttal), since the label's "each warrant tested" is narrower than what CQs do.

**F9. Low. Some dia-warrant rules cannot be checked or followed as written.**

- "Never attribute a warrant the author would disown" (`arg.md:180`) cannot be checked for a third-party text. Use the pragma-dialectical form instead [10]: an argument "capable of being made logically valid by making explicit one or more unexpressed premises". Supply the least warrant that licenses the step, label it reconstructed, and give the alternative if two are plausible.
- A references/ scheme table may be unreadable on some surfaces. Put the five schemes' CQs in SKILL.md, or give a fallback as dia-reductio does (`SKILL.md:16`).

**F10. Low. The dia-steelman label is wrong.**

It says "Rapoport's rules in Dennett's 2013 wording", but its steps add "state its region of validity", which is Rapoport's principle 2 [18] and not one of Dennett's four rules [15]. They also omit Rapoport's "assumption of similarity". Relabel: "Dennett's four rules plus Rapoport's region of validity".

**F11. Low. Street Epistemology's "spider moment" is misread** (`arg.md:72`).

Guide §5.4 [22] describes a pause cue: "they will often tilt their head … may be experiencing an 'aporia'". It is not the method's ideal end. The "skip" verdict is unaffected.

**F12. Low. Interaction with the accepted munazara fold.**

The counterplan rule "weaken the counterplan under pushback [only with] a supplied fact" (`arg.md:170`) treats the user's rejection of a counter-assumption as pushback. In DI the user is the judge. A rejection is a ruling to record, not a challenge to resist, and the assistant does not assert counter-assumptions. So munazara's burden-of-proof rule (the claimant must prove a denied premise) must not apply to them.

Correction: "keep the counterplan as written; record the user's ruling on each counter-assumption; rewrite it only on a named defect (it misstates the data or contradicts another counter-assumption)."

**F13. Low. Missed mode.** Most of the argument-mapping evidence concerns learners who build maps themselves [49], and Toulmin's layout is itself a sequence of questions put to the arguer [4]. Make "ask" (the user fills each slot, one question per turn) a named dia-warrant mode, not only an on-request option (`arg.md:179`). It has the better case against over-reliance.

No fatal objection and no better candidate turned up.

## Citation table

S = supports, P = partly, N = does not support, U = unreachable. All 50 were fetched; none is U or N.

| # | Used for | Result | Evidence / note |
|---|---|---|---|
| 1 | Toulmin's aim | S | "criticize the assumption … formulated in purely formal, deductive terms" (URL needs a trailing slash) |
| 2, 3 | Toulmin's elements, objections, pages | S | [2] notes 88 and 91; [3] contents: Layout 87, Data and Warrants 89, Backing 95 |
| 4 | Toulmin's questions | S | Accurate, but "Why do you think that the warrant holds?" is Verheij's wording (F8) |
| 5 | Toulmin prompting | S | Abstract only: ⟨claim, reason, warrant⟩, human study |
| 6 | Merge rationale | P | MT-Bench claim fine; merge rationale not (F8) |
| 7, 9, 10, 11 | Pragma-dialectics; dialogue types | S | "Ten commandments … 190"; four stages and "the 15 rules"; ten rules verbatim; "(Walton and Krabbe 1995, p. 66)" |
| 8 | 15 rules | P | Abstract does not say 15; [9] does |
| 12, 13, 14 | Schemes and CQs | S | "sixty-five schemes", CQ1–5, "instance of different schemes"; "without requiring any external knowledge"; "67.6", "three of the four top-performing teams" |
| 15–21 | Rapoport, ITT, Double Crux, SE books | S | "done from memory" and Rogers (16); Part III chapters (17); "depends on the issue and situation" (18); "as clearly and persuasively as their proponents" (19); "folk recipe", "guessing at the shape" (20) |
| 22 | SE guide | P | Steps confirmed; "spider" misread (F11) |
| 23 | Mason 1969 | S | Abstract only: two criteria, RMK Abrasives |
| 24, 25, 28, 43 | DI/DA results | S | DI > DA on assumptions; "no differences between dialectical inquiry and devil's advocacy"; "requires specification of an alternative course of action"; beat members' average |
| 26, 27 | DA cautions; Mason procedure | S | Quotes confirmed; negative conclusions omitted (F2) |
| 29, 30 | Schwenk meta-analyses | S | 29 is a record with no abstract (cited for existence only); 30: "different conclusions from those drawn in an earlier review" |
| 31 | Klein | P | Paywalled summary only |
| 32–37, 39, 41, 42 | Debate and sycophancy | S | Khan: 88/78/60%, quote tool; Smit: "do not reliably outperform"; Cheng: "50% more", "N = 1604"; Lee: 48 people, no accuracy reported |
| 38 | Huang | P | Claim absent from the cited abs page; present in the full HTML v2 |
| 40 | Chiang | P | Effect only for interactive DA; separate recommender; overextended (F5) |
| 44–50 | Premortem, argument mapping, Double Crux test | S | "4.60 … 3.28", "'seeing' more … not necessarily … 'seeing' better" (45); 178 people, five conditions (46); "group discussion is an important factor" (48); "0.8 of a standard deviation" (49) |

Extra sources fetched for this review:
- Mitroff, Emshoff & Kilmann 1979, https://doi.org/10.1287/mnsc.25.6.583
- TQR 2006, https://doi.org/10.46743/2160-3715/2006.1652
- Mitroff & Mason 1982, https://link.springer.com/article/10.1007/BF00126172
- IfM SAST page, https://www.ifm.eng.cam.ac.uk/research/dstools/strategic-assumptions-surfacing-and-testing/
- Schwenk 1989 abstract via aggregator (secondary), https://www.readabstracts.com/Business/Uncertainty-in-the-transaction-environment-an-empirical-test.html
- Huang full text, https://arxiv.org/html/2310.01798v2
