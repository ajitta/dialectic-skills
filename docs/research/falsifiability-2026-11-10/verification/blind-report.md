# Blind judgment: can dia v2.11.0's existing skills handle P1–P5?

Material read in full: every `skills/*/SKILL.md` (13), plus `dia-conjecture/references/theory.md`, the quaestio, counterplan and elenchus templates, the negative output template, `dia-regula/references/evidence.md` (the relevant parts), README.md and plugin.json. All paths below are under `/mnt/skills/plugin-files/dia/skills/`. I did not open anything under /home/claude/.

Labels used below. **[text]** means the file says it, with a quote. **[inference]** means my own reading. **[web]** means a public source I fetched: IEP, "Karl Popper: Philosophy of Science", https://iep.utm.edu/pop-sci/. **[recall]** means my unverified memory.

---

## P1. Popper's prior refutation criterion: available everywhere, or only in some skills?

**What the text says**
- Only one skill asks for an explicit prior criterion. That is dia-conjecture Step 2: "**Prior criterion** (Popper's prior refutation criterion; an addition to Lakatos): if C is empirical, … ask it with the first case" (`dia-conjecture/SKILL.md`). The record has a field for it: "**Prior criterion:** the user's answer … | not asked (C is not empirical)".
- That criterion only works inside conjecture's scope. Step 0 accepts "only a claim about every member of a class", so a claim that is empirical but not universal never reaches it.
- dia-quaestio has a near equivalent, the falsification pull: "what would you have to see to drop this? A belief nothing could disconfirm is a finding, not a strength." It is required only in stress mode ("in `stress`, at least one falsification pull"). It is a probe, though. Nothing records the answer as a criterion that later probes must respect, and the brief template has no field for it (`dia-quaestio/references/brief-template.md`: its sections are Thesis, Decisions, Assumptions, Open questions, …).
- dia-counterplan names a deciding observation for each key assumption, before the user rules on it: "Favours the plan if: an observation the user could make" (Step 6). The assistant writes that observation; the user does not agree to it.
- dia-negative applies a falsifier only to the skill's own inference about function: "name the observation that would falsify it" (Rule 6). It does not apply one to the target's claim.
- dia-warrant does not test claims at all: "You judge how well the reasons support the claim, never whether the claim is true" (Rule 1).
- dia-reductio treats an empirical claim as a premise, never as a test: "an empirical or causal claim is never a step: … it goes into the premise list" (Rule 3).

**Is the problem real?**
- **[inference]** Only partly. A prior criterion means something only where (a) a claim is confronted with observations and (b) two parties agree in advance. [web] Popper ties basic statements to "the consensus of the relevant scientific community", which is an agreement between parties.
- dia-negative, dia-warrant and dia-reductio run in one pass: "Whole analysis in one response", "One pass in audit mode", "Whole chain in one response". There is no second party to agree with beforehand, so a "prior agreed criterion" cannot exist there.
- dia-warrant and dia-reductio also do not test against observation at all.
- That leaves the dialogue skills that confront claims with cases: conjecture (already has the criterion) and quaestio (has a probe, but no record of it and no rule that holds later probes to it).

**Verdict: solved by changing an existing skill (dia-quaestio only).** For the rest of the plugin it is **not a real problem**.
- What would fix quaestio: record the falsification-pull answer in the brief, and hold later "Evidence" probes to it.
- Optionally, require one falsification pull in develop mode too, at standard or deep depth.

---

## P2. Recording test severity for results that say a claim "held"

**What the text says.** Every skill that can return a "holding" result already has to list what was tried, and most say outright that the result is not a proof:
- dia-conjecture: "A holding result must fill **Tried**: a claim nobody pressed has not held." The Tried field holds "the lemmas and the kinds of case tried; the most suspect lemma now; 'C′ not yet tested'". It also says "never call C proved".
- dia-elenchus sets a minimum bar for holding: "**holding (provisional)** when the current definition passed at least one real breadth test and one goal or consequence test (the holding bar)". Its record template has a "Not examined" section.
- dia-quaestio: "**Sharpened**: … Say which tests did not happen". The brief has a section "Not tested this session".
- dia-negative: "say that C holds against the particulars tested, list them, and say where a gap would most likely show up".
- dia-warrant: "**no weak link found among the questions asked; not a proof** (list the questions and name the one you would ask next)".
- dia-reductio: "list the directions and premise sets you tried". It also warns against "Treating 'no contradiction found' as 'true'".
- dia-counterplan: "Hearing both sides is not evidence that the plan was tested."
- Conjecture's case selection aims for hard tests: "Aim first at the lemma marked most suspect".

**What is missing.**
- **[inference]** No skill grades how severe each test was. [web] In Popper's sense, a severe test is one whose prediction was "highly improbable in the lights of our previous knowledge". No field says whether a case was one the claim would probably have failed if it were false.
- Whether to add such a grade is open. The plugin consistently avoids grades the model assigns to itself without outside evidence:
  - warrant, reductio and negative, when another agent fixes the output format: "In a severity field, write that this method does not give it".
  - dia-adjudicate allows severity only "by effect on the conclusion".
- A severity grade the model gives its own test would be exactly that kind of unverified label.

**Verdict: solved by existing skills.**
- The "Tried / tested particulars / not tested" fields already let a reader judge how hard the claim was pressed.
- A graded severity field would be a change to dia-conjecture. Its value is doubtful, and it is not needed to stop a weak "held" from passing as strong.

---

## P3. Falsifiability audit of empirical claims that are not strictly universal

The sub-parts get different answers.

### (a) A user asking "is this falsifiable?"
- **[text]** No skill takes this question as its task.
  - Conjecture Step 0 sends non-universal claims elsewhere: "'generally', 'usually', 'most' … dia-warrant; a plan … dia-counterplan …; what a word means: dia-elenchus; … Q and not-Q: dia-reductio".
  - That list has **no destination** for existential claims ("there is X"), for ∀∃ claims with no time bound ("it will eventually …"), or for statistical claims put as point hypotheses.
  - dia-warrant explicitly declines questions about truth or testability: "If the user asks whether the claim is true, say that this audit does not decide it."
- **[web]** These claim types are exactly where falsifiability turns on logical form. On existential claims: "there is no way of definitively showing that they are false".

### (b) Detecting methodological immunization
**What exists:**
- dia-conjecture names the Lakatosian version of this move: "**Monster-barring:** the user excludes a case that meets the reading in force by narrowing a term …"; "Do not allow a refutation to be dismissed as a monster".
- dia-conjecture also rules: "No silent redefinition" (hard rule 5), and "**Disputed:** a bare 'no', or insistence, with no condition named".
- dia-quaestio: "A belief nothing could disconfirm is a finding".

**What is missing:**
- No skill says what to do when the holder refuses **every** refutation criterion.
- Conjecture Step 2 just records "the user's answer"; refusing the criterion has no named classification and no effect on the result.
- **[inference]** P3 mixes two different things:
  - **logical unfalsifiability**: the claim's form, e.g. "eventually", or an existential claim;
  - **methodological immunization**: the holder's behavior.
  
  [web] Popper's term is theories "permanently immunized from falsification by the introduction of untestable ad hoc hypotheses". The plugin partly covers the behavioral kind (monster-barring), and only inside dia-conjecture. It does not cover the logical kind.

### (c) A decision rule for probabilistic claims
- **[text]** None. dia-warrant handles "probable rather than certain" claims, but only the strength of their support, and Rule 5 forbids supplying counter-facts: "you do not settle an open one with counter-facts of your own".
- [recall] Popper's own answer in *Logic of Scientific Discovery* ch. 8 was a methodological decision to treat highly improbable outcomes as prohibited. Probability statements are not strictly falsifiable without that decision. I did not verify this; the IEP page only says experimental results "allow us to test hypotheses concerning the values of certain probabilities".
- **[inference]** A concrete decision rule (endpoint, threshold, sample size) is something dia-techne can produce when the user asks for a test design, under Five questions Q3: "Which methods and tools would they use". Nothing triggers it from an audit, though.

### (d) Recording the auxiliary hypotheses held fixed
**What exists:**
- **dia-reductio** is built for exactly this, for a deductive test. Lay out the claim, the auxiliaries as [A] premises and the observed result as [T]/supplied premises. It requires "No hidden premises", and Rule 6 says "Logic shows inconsistency, not which member is false … present the choice". That is the Duhem–Quine point. Its "carried by added premises" grade flags a test decided by the auxiliaries rather than the claim.
- **dia-conjecture** hard rule 2 makes each case state its background conditions: "A check that rests on arithmetic or on how the case behaves states every condition its result needs". Its [A] lemmas are recorded.
- **dia-counterplan** lists assumptions, labelled [T]/[A].

**What is missing:**
- Conjecture's record has no field for the auxiliaries in force across the whole test. They appear only inside each case's check line.
- No skill links the auxiliaries to the prior criterion ("this observation refutes C given A1–A3").

**Verdict: needs a new dia skill** for the core: a falsifiability audit that sorts claim types (universal, existential, ∀∃ without a bound, statistical), elicits or proposes a criterion, names immunization, and records auxiliaries.
- Sub-part (d) is **already solvable by dia-reductio**, with the gap noted under (d).
- The decision rule in (c) is **reachable through dia-techne** when the user asks for a test design.
- Squeezing the audit into dia-conjecture would distort that skill. **[inference]** Its whole method assumes "one counterexample" settles a case; [text] it says itself that a defeasible claim gets "a rebuttal condition, not a refutation". That method does not apply to existential or statistical claims.
- **Minimum change if no new skill is wanted:** give conjecture Step 0 a destination line for existential, open-ended and statistical claims. Today there is none (see routing inputs 4 and 5).
- **Reality check:** the gap is real. But router's fallback "**None fits:** say so in one line and answer without a dia skill" (`dia-router/SKILL.md`) already gives the user an unstructured answer, so a new skill is a scope decision, not a fix for broken behavior.

---

## P4. Checking whether a run of a dia skill obeyed its own rules (format)

**What the text says**
- README: "The plugin contains only Markdown, YAML and JSON files. It has no scripts, hooks, MCP servers or binaries".
- dia-regula reviews the **text** of instructions ("Write or review text a model follows"), not transcripts of runs.
- dia-emend could take a transcript as its target, with "check against dia-X's hard rules" as the criteria. But that is a check by the same model reviewing its own run, and the plugin warns against relying on it: "Do not launch subagents to check your own work"; "rechecking … on your own judgment alone … tends not to improve correctness" (citing Huang et al.).
- dia-adjudicate needs reports that already exist: "Do not write the reports yourself".
- dia-ratchet counts "checked against the user's instructions" as an outside method. Format rules could be checked that way, but ratchet edits the target, it does not audit compliance.

**Is the problem real?** Yes. `dia-regula/references/evidence.md` documents unstable compliance and loading: "Haiku loaded the skill under test in 1 of 4 runs of a baseline check"; "prose on Haiku's logo case went 1/6, then 8/12".

**Verdict: belongs outside the plugin.**
- Fixed labels, record fields, "one question per message" and "no tables" in dialogue messages can be checked mechanically: a linter or eval over transcripts.
- The plugin deliberately ships no code, and its own skills reject self-review as evidence.
- dia-adjudicate could serve as the judge layer over a linter's reports, but it does not replace the linter.

---

## P5. Judgment-dependent conformance, and whether the plugin improves reasoning at all

**What the text says**
- The plugin admits it has no evidence of effect:
  - "No study has tested this method with users" (`dia-conjecture/references/theory.md` §6).
  - "hearing both sides is not evidence that the plan was tested" (counterplan).
  - The regula evidence comes from "an unpublished study by this skill's author … Its runs, prompts and traces are not public".
- dia-regula step 1 sets an A/B standard for meaning changes, but it presupposes an eval: "when an eval exercises the changed condition … a meaning change also needs an A/B … 12 or more such runs per arm".
- When no eval exists, "the change stays only if you report it as unmeasured and the user accepts it".
- dia-adjudicate's "Running twice (recommended)" is a usable method for disagreement between judges on judgment-dependent rules: "the judge's own errors gathered almost entirely in these differing items".

**Verdict: belongs outside the plugin.**
- Effect hypotheses need task suites with ground truth, blind or human raters, and baseline-versus-skill arms.
- No skill can measure its own effect from inside a conversation.
- Parts of the protocol already exist in the text: regula's A/B rules and adjudicate's two runs plus a human must-check list. The suite, the cases and the raters do not.

---

## Routing today

Assumption: each input is sent as `dia <input>`. The router chooses "the one dia skill whose description in your skill list fits". **[inference]** That choice is a model judgment, so I give the most likely pick and the realistic alternative.

| # | Input | Router pick (and alternatives) | What the chosen skill's own Step 0 / Scope does | Does it give what the request needs? |
|---|---|---|---|---|
| 1 | 이 마케팅 전략은 반증 가능한가? (Is this marketing strategy falsifiable?) | Likely dia-quaestio, or "Two fit about equally" with dia-counterplan / dia-negative. The request is about a plan, and conjecture Step 0 sends "a plan, policy, decision or idea" to those three. | quaestio Step 0 probably picks `stress` mode, so at least one falsification pull. | **Partly.** The user is asked what would make them drop the strategy, and an unfalsifiable answer becomes "a finding". There is no analysis of which of the strategy's parts are testable hypotheses and which are choices, and no criterion is recorded. [inference] The closest existing output is a full **dia 8** (counterplan): Step 6 gives "Favours the plan if: an observation" for each key assumption. The router will not pick it, because the request does not ask for the opposing plan. |
| 2 | 모든 정렬 리스트는 이분 탐색이 된다, 반박해 봐 (Every sorted list can be binary-searched; refute it) | dia-conjecture (menu: "always or never … by counterexamples"). It might be offered as a tie with dia-reductio, whose theory says "one global counterexample … is also a refute run there". | Step 0 accepts it as strictly universal. Step 1 fixes the reading ("in my words" if paraphrased; "이분 탐색이 된다" is ambiguous between correctness and O(log n)) and asks for the user's proof. Step 2: for a mathematical C, "the check of hard rule 2 is the criterion". | **Yes.** It is the skill's own worked example (a sorted singly linked list). Friction: the user asked for a refutation, but Step 1 first asks "why they hold it". dia-reductio would give a one-response refutation instead. |
| 3 | 그 약이 효과 있다는 걸 뭘 보면 틀렸다고 할래? (What would you have to see to say that drug doesn't work?) | Most likely "**None fits**" → plain answer. dia-warrant (cause-to-effect scheme) or dia-quaestio are possible. Conjecture Step 0 rejects it: drug efficacy is a "generally" claim → dia-warrant. | If warrant: no reasons are given, so the slots read "none given" and the result is a weakest link. Rule 1 forbids deciding truth. Rule 5 forbids supplying counter-facts. quaestio would turn the question back to the user one ask at a time, and it is for "an idea", not for a claim (possibly Claude's own, given "그 약"). | **No.** The request asks for a prior refutation criterion for a statistical causal claim: endpoint, effect size, decision threshold. No skill does that from a request (P3c). The plain answer is unstructured. |
| 4 | 결국 시장이 교정한다는 말, 반증 가능해? (Is "the market eventually corrects" falsifiable?) | dia-conjecture if read as "every mispricing is eventually corrected"; otherwise "None fits". | In conjecture, Step 0 asks whether "every" is meant strictly. Hard rule 2 then **blocks every global case**: a case must show it "violates the consequent", and no finite observation shows "never corrected" ("a case whose check you cannot write is not raised"). If one is raised anyway, the user can name the condition "not yet", which under an unbounded reading is an **Invalid** ruling, and the case is withdrawn. The run ends "when you find no further case you can check" with result "stopped before testing". | **No.** The skill implicitly shows the claim cannot be tested, but never names this as unfalsifiable by form (∀∃ with no time bound). It never offers the obvious repair, a bounded operationalization. The result label hides the actual finding. |
| 5 | 숨은 패턴이 있다는 가설 반증 가능해? (Is the hypothesis that there is a hidden pattern falsifiable?) | "**None fits**" → plain answer. | It is an existential claim. Conjecture Step 0 would reject it, and its redirect list has **no entry** for existential claims. dia-reductio mentions existence claims only about indirect proof ("claims that something exists"). | **No.** There is no home in the plugin. [web] Existential claims are the textbook unfalsifiable case. |
| 6 | 이 가설 시험할 실험 설계해 줘 (Design an experiment to test this hypothesis) | The router picks dia-techne but must not run it: "**dia-skopos, dia-ratchet, dia-adjudicate and dia-techne** never start from a request: reply in one line with the form to send (`dia <number> <request>`) and stop." So the output is one line: `dia 13 이 가설 시험할 실험 설계해 줘`. | Once it is sent as `dia 13 …`: no hypothesis is given, so it becomes "a visible placeholder", and only reversible steps run "while a placeholder remains". Q3 and Q4 bring in field methods and an outside check, e.g. a power calculation run as code. | **Partly** (after an extra turn). A good design is likely, but nothing *requires* a prior refutation criterion, a pre-specified decision rule or a list of auxiliaries. [inference] Q1 ("what would a top practitioner do") will usually produce them, but that is not guaranteed by any rule. |

**Routing finding.** Inputs 3, 4 and 5 are the core of P3, and today they get either no dia skill or a skill whose rules quietly produce a misleading result (input 4).

---

## Overall verdict

| Problem | Verdict |
|---|---|
| P1 | Solved by changing an existing skill (dia-quaestio: record the falsification pull and hold later probes to it). Elsewhere not a real problem: one-pass skills have no second party to agree with in advance. |
| P2 | Solved by existing skills: the "Tried" / "tested particulars" / "not tested" fields are required wherever "holding" can be the result. A graded severity is optional and at odds with the plugin's avoidance of self-assigned grades. |
| P3 | Needs a new dia skill for the falsifiability audit itself: sorting claims by logical form, existential and unbounded claims, naming immunization. Already solvable: auxiliaries with dia-reductio, decision-rule design with dia-techne on request. The minimum change if no new skill: give dia-conjecture Step 0 a destination for existential, open-ended and statistical claims, and stop it returning "stopped before testing" for a claim that cannot be tested by form. |
| P4 | Belongs outside the plugin: a transcript linter or eval. The plugin ships no code and rejects self-review as evidence. |
| P5 | Belongs outside the plugin: an eval suite with baseline arms and independent raters. regula's A/B protocol and adjudicate's two-run method can be reused as protocol. |

**Strongest argument against this verdict (aimed at the P3 call, the only one that adds a skill).**

By the plugin's own standards, a new skill is the one change it cannot justify yet. Three reasons:
1. P5 is unsolved, so there is no evidence that any dia skill improves reasoning over the router's built-in "None fits: answer without a dia skill". A plain model answer to "is this falsifiable?" is a single-turn analysis that Claude handles reasonably without a method.
2. dia-regula's Rule 3 says "Compliance tends to fall as instructions pile up". Its evidence shows skills loading in as few as 1 of 4 runs. A fourteenth skill that overlaps conjecture, warrant and quaestio adds instruction load and new router ties.
3. Under regula step 1, an unmeasured change "stays only if you report it as unmeasured and the user accepts it".

On those standards, the defensible order is P5's eval first, then the small dia-conjecture Step 0 change, and a new skill only if the eval shows the plain-answer fallback actually fails on inputs 3–5.

Sources (web): [IEP, Karl Popper: Philosophy of Science](https://iep.utm.edu/pop-sci/). Search results consulted but not relied on: [Wikipedia, The Logic of Scientific Discovery](https://en.wikipedia.org/wiki/The_Logic_of_Scientific_Discovery).
