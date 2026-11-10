# Adversary report: dia-falsification-skill-need.md

Checked against the installed plugin `dia` v2.11.0 at `/mnt/skills/plugin-files/dia` (all paths below are relative to that folder). I read in full the SKILL.md of router, conjecture, quaestio, warrant, negative and most of adjudicate; the others (reductio, counterplan, emend, ratchet, regula, techne, elenchus) by targeted passages only. No skill was run. Popper/Lakatos/Duhem points are from recall, with one public lookup (IEP, "Karl Popper: Philosophy of Science", https://iep.utm.edu/pop-sci/) where marked.

Labels: **refutes** / **weakens** / **fails** (attack tried and did not hold).

## Verdict in brief

| Conclusion | Outcome |
|---|---|
| (가-1) edits to existing skills suffice | Survives as a direction. "Small cost, just move the fields" falls: one edit is already in the plugin, one cuts against a mode's identity, and the plugin's own rules make each a measured meaning change |
| (가-2) gap exists and justifies a new conversational skill | Gap is narrower than stated; the new-skill case is weakened to the point that the document's own "lighter alternative" should be the primary recommendation. Not strictly refuted |
| (나) no new skill; eval suite / rubric / experiments outside the plugin | Survives. Two supports are overstated: how much is "mechanical", and how well dia-adjudicate fits as re-judge |

## A. Attacks on (가-2), strongest first

### A1. quaestio already holds the methodological layer, and the document's reason for excluding it rests on a wrong claim — weakens (strongly)

The document says only the methodological layer needs a dialogue, and rejects quaestio because it "ends in a brief with options and a plan". The SKILL.md says otherwise:

- `skills/dia-quaestio/SKILL.md`: "**Falsification pull**: "what would you have to see to drop this?" A belief nothing could disconfirm is a finding, not a strength." This is the immunization finding, stated as a result.
- Same file, Step 3: "If the session was pure stress-testing and the user doesn't want options, skip this step and Step 4's questions". So a stress run can end with no options and no plan.
- Same file, probe table, all modes: "Evidence | what supports it; what would count against it".
- `skills/dia-quaestio/references/question-bank.md`: "What would you need to see to drop this? A number or an event?" That already asks for a threshold or a dated event.
- The brief records "assumptions (validated, unvalidated, or risky…), open questions, … what was not tested".

What quaestio lacks: a one-pass verdict on logical form (its verdicts are only Sharpened / Open / Refuted), a `--target` for pasted text, and record fields for a decision rule and fixed auxiliaries. Its description ("develop an idea into options and a plan") also would not make the router pick it for "is this falsifiable?". So the attack does not close the gap entirely; it shows the conversational half is present and the "different end product" argument is wrong.

### A2. The remaining half (logical form) is one-shot, so by the document's own reasoning it does not need a conversational skill — weakens

The document says formal unfalsifiability is judged "without asking" from the text alone. The router already has a path for that: `skills/dia-router/SKILL.md`: "**None fits:** say so in one line and answer without a dia skill." A one-turn classification with no user rulings and no record is what a plain answer does. The document gives no evidence that a skill beats that baseline, while its own §2.3 says effect claims need a baseline experiment. Adding A1: the distinct content of the proposed skill shrinks to two record fields (decision rule, fixed auxiliaries) and an ordering of criteria, which is edit-sized.

### A3. The document's own one-shot labels are wrong for its own examples — weakens (design), see also D

- "숨은 패턴이 있다는 가설" is labelled formally unfalsifiable as an existential. A claim about one finite, named dataset is a restricted existential, not a pure one; what blocks refutation is the undefined word "pattern". The proposed rule ("do not attach a criterion to an existential") would mislabel it, where asking for a definition would make it testable.
- "결국 시장이 교정한다" is filed under "auxiliary-shielded" and "methodological immunization (ask for a deadline)". As worded it is unfalsifiable by form (no time bound); adding a deadline changes the claim. conjecture treats that kind of move as a change to C ("No silent redefinition"). The two layers are confused in the example that motivates the dialogue requirement.

### A4. conjecture already covers the empirical-universal part, including the document's market example — weakens

- `skills/dia-conjecture/SKILL.md`, Prior criterion: "if C is empirical, resting on observation (people, systems, markets, measurements), ask it with the first case".
- Step 0: "If it is unclear whether the user means "every" strictly, make that your one question."

"Markets (always) correct eventually" would plausibly go to conjecture today, not to "no skill". The real hole there is small: when the user accepts no observation, conjecture has no label for it (it records the answer and ends as disputed or "stopped before testing"). One sentence in the Prior criterion fixes that. Also, the proposed border ("for a strict universal the new skill agrees the criterion, then hands to conjecture") means two skills ask the same prior-criterion question, and the router rule "**Two fit about equally:** … ask which, and stop" would fire for every empirical universal.

### A5. counterplan already gives falsifying observations for the assumptions under a plan — weakens (row 1 of the routing table)

`skills/dia-counterplan/SKILL.md`, Step 6: "Favours the plan if: an observation the user could make. Favours the counterplan if: …", and Rule 5: "name the observation that would decide each open pair". For "is this marketing strategy falsifiable?" the document's new skill would take "only the underlying empirical assumptions" — the same Kn that counterplan extracts.

### A6. warrant's rebuttal slot and critical questions — fails (minor overstatement found)

Attack failed: the rebuttal slot is "the circumstances, as stated, in which the warrant would be set aside", i.e. defeaters of the inference, not falsifiers of the claim; Rule 2 forbids filling it ("do not fill backing or rebuttal to complete the layout"); Rule 1 bars any verdict on the claim. The document's reading stands. Only overstated: "does not ask what refutes" — ask mode does ask "When would that rule not apply?" and the general question "[conclusion] Are there other reasons for or against C?".

### A7. negative rule 6 falsifier — fails

Attack failed: the falsifier applies to the skill's own inference about function ("name the observation that would falsify it"), not to the target's claim. Rule 1 ("The target's own standard only") confirms the document's point that immunization counts only when the target professes testability.

### A8. elenchus, techne — fails

Attack failed: elenchus tests definitions and beliefs against the user's other beliefs (menu row), with no observation criterion; techne's question 4 is an outside check on a task result, and the router says techne "never start[s] from a request". Neither audits falsifiability. (elenchus was read only by description and menu row.)

### A9. Holder problem in the proposed skill — weakens (design)

The methodological layer needs "the holder's commitment", yet the proposal accepts `--target` text and earlier answers, where the holder is absent. The document's own failure observation ("labels methodological immunization without asking the holder") would then make that label unassignable. conjecture solves this explicitly ("the user takes the claim up for this dialogue"); the document does not.

## B. Where the document is too conservative or too optimistic

### B1. (가-1) "small cost" is overstated — weakens

- Already present: the document says the only severity record is conjecture's Tried. Not so. `skills/dia-reductio/SKILL.md`: "list the directions and premise sets you tried"; `skills/dia-negative/SKILL.md` Step 4: "say that C holds against the particulars tested, list them, and say where a gap would most likely show up"; `skills/dia-warrant/SKILL.md`: "no weak link found among the questions asked; not a proof (list the questions and name the one you would ask next)"; quaestio: "Say which tests did not happen". The proposed Tried edit for reductio and negative is mostly a rename.
- Identity conflict: a mandatory falsification pull in develop mode cuts against "`develop` (default: grow a fragile idea, gentle probes)" and "don't manufacture doubt" in quaestio.
- Turn structure: counterplan shows the observations in Step 6 and asks one question in Step 7; making them a pre-agreed field adds a turn to a skill whose Step 7 says "do not suggest an answer".
- Process cost: `skills/dia-regula/SKILL.md` ("Writing, editing or reviewing text", item 1) treats each of these as "a meaning change", which "stays only when the user asked for it or a finding requires it", and where an eval exercises it "also needs an A/B with old and new text … 12 or more such runs per arm". Item 2 adds a review by a sub-agent that did not write the change.

The conclusion "edit, not a new skill" still stands.

### B2. Recommendation order contradicts its own reasoning — weakens

§3 puts the edits first and the eval suite second, while saying the suite is what lets the edits be falsified. regula's A/B rule points the same way: measurement comes with the change, not after.

### B3. (나) really needs a skill? — fails

Attack failed, and the check strengthens the document. Existing skills already cover the grading chain: emend accepts "a standard or reference given there, which is supplied material" and confirms defects "by the user's instructions or supplied material"; adjudicate names report-writing as "dia-emend's job". regula already assumes evals live outside the skill text ("any further check a repository rule requires (an eval, a probe, a review)"). The document's dismissal of emend ("fixes output, does not judge compliance") is overstated, but in the direction of its own conclusion. One point stays open: users on a host without tools have no harness, so a Markdown-only check is the only form that reaches them; the document does not weigh this.

### B4. "Mechanically decidable" is overstated — weakens (나-1)

- "One question per message" is not countable by question marks: quaestio says "two asks joined into one sentence still count as two, even under one question mark" and "offering possible answers to the same ask … is still one ask".
- Fixed labels and banned phrases are translated: conjecture rule 11 "Reply in the user's language, including labels and the fixed result values". String checks need a table per language.

More of the checks belong in the judged rubric (나-2) than the document allows.

### B5. adjudicate as re-judge fits poorly — weakens

`skills/dia-adjudicate/SKILL.md` Step 1: "Quote T's conclusion C"; Rule 7 grades severity "by effect on the conclusion"; Step 2 inventories "every checkable claim in T". A run transcript has no single conclusion, and its content claims are beside the point for rule compliance. Rule 2 also says "a judge from the same family inflates the reports it agrees with" — the same objection the document raises against a grading skill applies to its remedy. Workable by explicit invocation, but strained.

## C. Factual claims and quotes about the plugin

Wrong or overstated:

1. "The only severity record is conjecture's Tried" — wrong. See B1; e.g. `skills/dia-reductio/SKILL.md`: "list the directions and premise sets you tried".
2. "quaestio ends in a brief with options and a plan" (as a reason its end product differs) — overstated. `skills/dia-quaestio/SKILL.md`: "skip this step and Step 4's questions".
3. "No skill names an unfalsifiable belief" (implied by the gap table) — overstated. Same file: "A belief nothing could disconfirm is a finding, not a strength."
4. Market example "goes nowhere" — overstated. `skills/dia-conjecture/SKILL.md`: "(people, systems, markets, measurements)".
5. counterplan observations to be moved "before the user picks" — they already come before. `skills/dia-counterplan/SKILL.md`: Step 6 lists them, Step 7 asks. Only "agreed" would be new.
6. regula Rule 4 used across separately loaded skills — stretched. `skills/dia-regula/SKILL.md`: "**One name per thing** across the files a model reads together".
7. "Same handling as conjecture Step 4" (hand over to elenchus) — conjecture only offers: "say so and offer dia-elenchus for that question; the case stays disputed".
8. "Trigger phrases" — overstated framing. Every skill description says "a request that only sounds like this is not an invocation"; phrases matter only after a leading `dia`. The document concedes this later, which leaves "the only clean trigger" without force.
9. Cost list incomplete: besides "print the thirteen rows", the router also has "A number from 1 to 13", and Step 0 of conjecture, Step 0 of quaestio and Scope of warrant each carry their own border lists.
10. "emend and ratchet fix output, they do not judge compliance" — overstated for emend (B3).
11. "Whether an eval system exists was not checked" — the plugin itself carries evidence: regula's A/B rule, and adjudicate's "a misruling that judges made in trials".

Checked and correct: Prior criterion sits in conjecture Step 2 and is asked with the first case; "in `stress`, at least one falsification pull"; reductio Step 7 and negative Step 7 "the observation that would change the recommendation"; reductio Step 2 refute default; warrant "Support, not truth"; negative Rule 1; router "Choose the one dia skill whose description…", fixed numbers; README "only Markdown, YAML and JSON files … no scripts, hooks, MCP servers or binaries"; "Thirteen" in README and `.claude-plugin/plugin.json`; adjudicate "Do not write the reports yourself", Rule 2 with arXiv:2506.07962, "Running twice"; Huang et al. ICLR 2024 in emend and ratchet; techne question 4; regula Rule 3.

## D. Popper / Lakatos / Duhem-Quine claims

1. "A pure existential statement is the typical unfalsifiable case" — correct (IEP: "there is no way of definitively showing that they are false"). The example is not a pure existential (A3). Missing: such statements are verifiable, so "unfalsifiable" is not "empty".
2. "Probabilistic claims are not strictly falsifiable; a decision rule is needed" — correct (recall: *Logic of Scientific Discovery*, ch. VIII).
3. Two layers (logical / methodological) — roughly correct (IEP: falsifiability as a logical feature; falsificationism as "a normative, methodological proposal"). The market example is placed in the wrong layer (A3).
4. Auxiliary hypotheses listed as an immunization device — overstated. IEP: a theory "can be legitimately saved from falsification by the introduction of an auxiliary hypothesis" that yields new testable predictions; only ad hoc ones are barred. "If there is no effect, the dose was too low" is itself testable. The skill needs the ad hoc test, or it will name legitimate auxiliaries as devices. Lakatos's later standard (progressive versus degenerating shifts) says the same and is not used.
5. Duhem-Quine used to record fixed auxiliaries — correct use. It also undercuts "the text alone suffices" for the logical layer: most empirical claims yield no observation statement without auxiliaries (IEP: "in many cases impossible to test scientific theories in isolation").
6. conjecture described as Lakatos's repair procedure — correct per `skills/dia-conjecture/references/theory.md`.

## E. Routing table (§1.2) against today's router

All rows assume a leading `dia`; without it no skill runs.

| Row | Today | Effect on the new-skill case |
|---|---|---|
| Marketing strategy falsifiable? | None fits (plain answer), or counterplan/quaestio offered | Undermines: counterplan already yields deciding observations per assumption (A5) |
| Sorted lists, refute | conjecture (reductio's refute default could make the router ask) | Neutral |
| Refute this argument | reductio or warrant, router asks | Neutral; matches the document |
| Drug works — what would show it false? | None fits → plain answer | Supports the gap; closest existing path is quaestio stress |
| Market corrects eventually | conjecture plausible via Step 0 question and Prior criterion | Undermines; with the new skill two would fit (A4) |
| Hidden pattern | None fits → plain one-turn answer | Undermines: one-shot, and the proposed label is wrong (A2, A3) |
| Design an experiment | None fits | Neutral |
| What "fair" means | elenchus | Neutral |

Three of the five rows assigned to the new skill route or resolve differently today in a way that weakens the case; one supports it.

## F. What survives, what falls

- **Survives:** (나) no new skill, evaluation outside the plugin; H1–H3 need controlled experiments. (가-1) as a direction. The narrow reading of warrant and negative. The real residue of (가-2): no skill records a decision rule for probabilistic claims or the auxiliaries held fixed, and the router has no path for "is this falsifiable?".
- **Falls or shrinks:** "no existing skill covers it" (quaestio stress, conjecture's Prior criterion and counterplan cover most of it); "putting it in quaestio blurs the border because the end product differs"; "Tried is the only severity record"; "(가-1) is cheap"; "many checks are mechanical"; "adjudicate serves as re-judge" without strain; the one-shot labels for the document's own examples.

**Single best argument.** The document says only the methodological layer needs a dialogue. quaestio already runs that dialogue in its own words ("what would you have to see to drop this?"), already calls an undisconfirmable belief a finding, and can end without options. The layer quaestio lacks is, by the document's own account, a one-turn judgment, which the router's "None fits" path already gives. What is left for a fourteenth skill is two record fields, so the document's fallback (route to quaestio stress, add one line to conjecture) should be its main recommendation.
