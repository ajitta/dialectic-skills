# dia-negative: research and fidelity audit

| | |
|---|---|
| Skill | `skills/dia-negative/` (SKILL.md 115 lines, `references/theory.md` 54, `references/output-template.md` 61, `agents/openai.yaml` 7), version 1.0.0 |
| Upstream | `upstream/installed/negative-dialectics/` (installed copy, unversioned) |
| Method named | "Immanent critique in the manner of Adorno's negative dialectics" (SKILL.md:3) |
| Status of this document | Research and proposals only. Nothing in `skills/`, `plugins/` or `releases/` was changed. |

## 1. Scope and summary of what the skill says

The skill takes one identifying claim C ("X is Y", "this policy is fair", "the goal is G") and, in a single response, does the following:

- **Frames the method.** It opens with a three-sentence thesis: to think is to identify; the thing never enters its concept without remainder; critique shows specific contradictions between what a claim says and what it delivers, by its own standards, without a reconciling synthesis (SKILL.md:14). It then says this is "a practical adaptation of Adorno's method, not Adorno's own procedure" (SKILL.md:16).
- **Sets the target.** `--target=user|claude|text|all` chooses the target. When the flag is absent, the target is inferred and stated in the first line (SKILL.md:20-29).
- **Ten hard rules (SKILL.md:33-42):**
  1. Immanent standard only, with a quote for each standard.
  2. A finding is strict only with three parts: claim C, particular D, and an argument that C and D cannot both hold.
  3. One reading at a time; ambiguity alone is not a finding.
  4. Cases come from the target's material first, then logic, then facts with evidence classes. Conditional findings are listed separately.
  5. Determinate, not abstract, negation.
  6. A stated purpose or function is an inference, needs evidence, and must name a falsifier. Speak about what the text does, not about motives.
  7. No forced synthesis; a revised claim must state its own remainder.
  8. Recommend one option; the user decides.
  9. Write in the user's language, with Adorno's terms in parentheses at most.
  10. The whole analysis goes in one response.
- **Eight steps (SKILL.md:46-92):** fix C; list its own standards C1…Cn and its stated purpose; gather particulars; write findings as Claims / Delivers / Why both can't hold / Evidence / What escapes; set the "operative function" against the stated purpose, with a falsifier and an optional "depends on" constellation; give five option types; recommend one; write a record whose status is **open**, **holding against the tested particulars**, or **stopped**.
- **Follow-ups (SKILL.md:103-106):** a chosen option is examined again as a new identification; disputed findings are re-checked; a disowned standard drops its findings.
- **`references/theory.md`:**
  - Summarises identity thinking, the nonidentical, determinate negation, contradiction, immanent critique, no final synthesis, constellation, the priority of the object, and exchange (theory.md:9-27).
  - Lists what the skill keeps and changes: strict gaps and recommendations are labelled as departures (theory.md:29-35).
  - Answers three objections: Habermas, Rosen, and Jaeggi's internal/immanent distinction (theory.md:37-41).
  - Separates the skill from reductio (theory.md:43-45).
- **`references/output-template.md`:** a phone-friendly layout with translated headings. It lists options A–E and a nine-line record.

## 2. The method in its primary sources

### 2.1 Hegel: the object's own criterion and determinate negation

- **The examined consciousness supplies its own standard.** In the Introduction to the *Phenomenology*, the measure lies in the object of the inquiry: "Consciousness furnishes its own criterion in itself", so "we do not require to bring standards with us, nor to apply our fancies and thoughts in the inquire" (Baillie translation, §84 and following).[10]
- **Determinate negation.** Against scepticism, which sees only "pure nothingness" in a refutation, Hegel holds that "this nothing is determinate, is the nothing of that out of which it comes as a result" (§79).[10] The negation has content because it is the failure of a particular shape of knowledge.
- **The start of a lineage.** Stahl reads this as the origin of immanent critique as a model of social critique: a form of knowledge is measured by its own standard of self-evaluation, and the mismatch can force that standard itself to change, which is more than mere internal critique.[13]

### 2.2 Marx and Horkheimer

- **Marx (1843).** Marx refuses a "dogmatic banner": "we do not anticipate the world with our dogmas but instead attempt to discover the new world through the critique of the old", and "we shall develop for the world new principles from the existing principles of the world".[12]
- **Horkheimer (1937), "Traditional and Critical Theory".**
  - He gives the classic social form of the move: "If we take seriously the ideas by which the bourgeoisie explains its own order — free exchange, free competition, harmony of interests, and so on — and if we follow them to their logical conclusion, they manifest their inner contradiction and therewith their real opposition to the bourgeois order."[11]
  - The same essay says critical theory "is suspicious of the very categories of better, useful, appropriate, productive, and valuable" as the existing order defines them.[11] That bears on the skill's recommendation step (§4, §7 F4).
  - The SEP treats this essay as the "largely undisputed reference" for defining Frankfurt School critical theory.[3]

### 2.3 Adorno: the concepts the skill borrows

**Identity thinking and the remainder.**
- "To think is to identify." The opening of *Negative Dialectics* (ND) says that "objects do not go into their concepts without leaving a remainder", and that contradiction "indicates the untruth of identity, the fact that the concept does not exhaust the thing conceived" (Ashton trans., p. 5).[5]
- In the IEP's summary, quoting ND p. 149: "dialectics seek to say what something is, while 'identarian' thinking says what something comes under, what it exemplifies or represents, and what, accordingly, it is not itself."[2]
- Geuss (REP) glosses negative dialectics as tacking "back and forth between concept and instances, continually pointing out in what concrete ways they are not identical".[4]

**Contradiction and determinate negation.**
- "Contradiction is nonidentity under the aspect of identity", and "Dialectics is the consistent sense of nonidentity. It does not begin by taking a standpoint."[5]
- The SEP: access to the nonidentical is possible only "via conceptual criticisms of false identifications", which "must be 'determinate negations,' pointing up specific contradictions between what thought claims and what it actually delivers". Through them, the misidentified aspects of the object "receive an indirect, conceptual articulation".[1]
- SKILL.md:14 and theory.md:15 paraphrase exactly this SEP sentence.

**Immanent critique.**
- The SEP connects Adorno's method to his diagnosis of an "integrated" society, which "eliminates the possibility of external or 'transcendent' social critique". It quotes him: "one can tackle it only where it is inconsistent with itself" (1969a).[1]
- Adorno's 1957 formulation, quoted in the SEP *Critical Theory* entry, says more than "use the target's stated norms". Immanent critique "must transform the concepts which it brings, as it were, from outside into those which the object has of itself, into what the object, left to itself, seeks to be, and confront it with what it is".[3]
- "The Essay as Form" describes critique of texts in the same way, as the "confrontation of texts with their own emphatic concept, with the truth that each text intends even in spite of itself".[8]

**No affirmative synthesis.**
- The Prologue says the book "would like to emancipate dialectics from these types of affirmative essence, without relinquishing anything in terms of determinacy", and calls the book "an anti-system" (Redmond trans.).[6]
- Geuss: the movement "has no natural stopping point and will not ever result in some positive, detachable conclusion or new, more adequate concept".[4]
- This is not plain pessimism. The SEP stresses a "fragile, transformative horizon" of reconciliation: "dialectics is the ontology of the false condition".[1]

**Constellations, models and the priority of the object.**
- Concepts are rearranged "in 'constellations' around a specific subject matter" to unlock the "process stored in the object".[1]
- The aim of thought is to honour objects "in their difference from what a restricted rationality declares them to be".[1]
- The worked parts of ND are "models", and the Prologue insists "They are not examples".[6] Adorno rejects the Platonic use of examples as "something indifferent in themselves".[6]

**Totality and suffering.**
- *Minima Moralia* §29 states it as an aphorism: "The whole is the false."[7]
- The SEP ties false identity to the exchange principle, which "demands the equivalence … of what is inherently nonequivalent".[1]
- It also gives the motive: "The need to let suffering speak is a condition of all truth."[1]
- Neither the totality claim nor the appeal to suffering appears in the skill. Section 5 discusses this.

### 2.4 Adorno on method, stringency, exaggeration and advice

These passages bear directly on the skill's step procedure, its strictness rule and its recommendation step.

- **Against method as a recipe.**
  - Dialectics is not "a method slapped on outwardly, at random".[5]
  - The Prologue: "The procedure is not grounded, but justified."[6]
  - The essay "proceeds, so to speak, methodically unmethodically". Adorno calls Descartes' rule of exhaustive enumeration "a supposition of a philosophy of identity".[8]
  - The IEP: "Adorno's complaint against identity-thinking is a moral and not a methodological one."[2]
  - Adorno held that "philosophy is not expoundable" and that "no philosophical thinking of quality allows of concise summary".[1]
- **Stringency and exaggeration together.**
  - ND: "expression and stringency are not two dichotomous possibilities. They need each other". Also: "what is vaguely put is poorly thought", and philosophy "requires observance of stringency to break the authoritarian power claim of stringency".[5]
  - *Minima Moralia* §82: thought has "an element of exaggeration, of over-shooting the object", and "as soon as thought repudiates its inviolable distance and tries with a thousand subtle arguments to prove its literal correctness, it founders".[7]
  - §29: "In psycho-analysis nothing is true except the exaggerations." (The OCR text reads "bUe" for "true".)[7]
- **Advice.**
  - *Minima Moralia* §89: "Those who cannot help ought also not advise".[7]
  - Adorno's late statement, quoted in the SEP, is negative in form: the good life today "would consist in resistance to the forms of a wrong life that have been seen through and critically dissected".[1]

### 2.5 The Positivist Dispute: Adorno on Popper, refutation and solutions

Section 4 needs this most, because the skill's falsifier rule is a Popperian device. The SEP calls Adorno "the most prominent challenger" to Popper's philosophy of science in the 1960s.[1] In "On the Logic of the Social Sciences" (1961/1976), Adorno says the following.[9]

- **Refutation from outside.** "Refutation is only fruitful as immanent criticism. … Viewed from without, everything and nothing is refutable." (p. 112)[9]
- **Not every claim is a test case.** If criticism means "reduction to so-called facts", it "would reduce thought to hypothesis". "Not all theorems are hypotheses." Some essential thoughts "recoil from tests and yet they have a truth content". (pp. 112–113)[9]
- **The solution grows from the critique.** "criticism and the solution can in no way be separated from one another"; the construct of criticism "can … already imply the solution; the latter hardly ever appears from without. It was to this that the philosophical concept of determinate negation referred." (p. 113)[9]
- **Structural contradictions are not definitional.** When liberal society claims freedom and equality while power is unequal, "these are not logical contradictions which could be eliminated by means of more sophisticated definitions … they are the structural constitution of society itself"; "criticism does not merely mean the reformulation of contradictory statements for the sake of consistency". (p. 115)[9]
- **Ideology critique owes concrete proof.** It "was under obligation to provide concrete proof of the falsehood of a theorem or of a doctrine; the mere mistrust of ideology … was not sufficient"; Marx "would have ridiculed it as abstract negation". (p. 115)[9]
- **Immanent critique is also concrete.** In his Introduction to the volume: "Immanent criticism is never solely purely logical but always concrete as well — the confrontation of concept and reality."[9]

So Adorno does not reject criticism, rigour or even refutation. He rejects (a) refutation from an external standpoint, (b) reducing every claim to a testable hypothesis, and (c) treating structural contradictions as definitional slips. The skill's rules agree with some of this and conflict with some of it (§4).

## 3. Relevant modern research

### 3.1 Internal versus immanent critique

- **The SEP *Critical Theory* entry** describes the Frankfurt School's "third model". Immanent critique "avoids the dichotomy between an internal critique that refers to standards and standpoints that are already recognized by those criticized and an external critique that refers to standards … not (or not yet) recognized" (citing Jaeggi 2005, 2014; Celikates 2009; Stahl 2013a).[3]
- **Stahl (2013)** gives definitions.[13]
  - Internal critique measures a practice against members' self-understanding. His example is a foreign policy that claims to protect human rights but does not.
  - Immanent critique evaluates "both the empirical behavior … and the explicit self-understanding" by standards internal to the practice, and "aims at a transformation of such practices that encompasses both actions and self-understandings".
  - He lists three open questions any immanent critique must answer: the social ontology of immanent norms, how a critic can know them, and why they bind.
  - On Adorno, Stahl (following O'Connor) says the key immanent standard is "the promise of autonomous subjectivity", which structurally cannot be realised now. Adorno's standards are therefore immanent in "forms of subjectivity" rather than in the practices themselves.
- **Stahl's 2022 book** restates the aim: immanent critique "draws on norms already present within these practices to demand social change, rather than merely conservatively reproducing them".[14]
- **Jaeggi (2005)**, on *Minima Moralia*: Adorno's immanence "must mean something more and other than connecting to the value convictions available within a society (as conceived, e.g., by Michael Walzer)". Immanent critique as determinate negation also "depends on an overburdening (or an unclear use) of the concept of contradiction".[15]
- **Jaeggi (2015)** proposes criteria that are "immanent and transformative at the same time", without being "constrained to the kind of internal criticism that confines itself to re-establishing the adherence to norms that a certain community already holds".[16]
- **A reviewer of *Critique of Forms of Life*** notes the cost: deciding "what is and is not a contradiction" can be "a murky matter".[17]

What this means for the skill:

- Rule 1 ("Never bring in an outside value the target does not hold", SKILL.md:33) is the definition of **internal** critique.
- theory.md:41 admits this ("The skill does internal critique by default").
- Yet the description and the first line of the body sell the skill as "immanent critique" (SKILL.md:3, 14).
- The upgrade to immanent critique that theory.md claims (Step 5 plus the option to change the standard) is real but thin.
- Jaeggi's "overburdened contradiction" worry supports the skill's choice to narrow contradiction to checkable gaps (theory.md:34).

### 3.2 Objections to Adorno that theory.md cites

- **Habermas.** He charged a "performative contradiction" in totalized critique and a "normative deficit". The SEP quotes him: "Adorno was quite aware of this performative contradiction".[1] The IEP adds the charge that Adorno is an "inveterate 'nay-sayer'".[2]
- **Rosen.** Stopford's thesis argues that negative dialectics "does not amount to a system, a standpoint, or even a set of principles. Rather, it is a critical activity". It sets out to answer "Michael Rosen's claim that Adorno's rejection of Hegelian determinate negation leaves his dialectics without any dynamic force".[18]
- **Accuracy of the attributions.** theory.md:31 attributes the "not a system, standpoint or set of principles" reading to "SEP; Stopford 2012". The fetched SEP entry does not say this; Stopford's abstract does, and ND's section heading "Dialectics Not a Standpoint" is the primary basis.[5][18]

### 3.3 How LLMs behave when asked to critique

- **Feedback sycophancy in both directions.** Five assistants gave "more positive" feedback when the user said they liked or wrote a passage. When the user said they disliked it, the assistant "tailors its feedback to be more negative".[20] A user who invokes a critique skill signals that they want gaps found. The research predicts pressure towards manufactured findings, not only towards flattery.
- **"Are you sure?" sycophancy.** Assistants "frequently wrongly admit mistakes when questioned by the user" and switch correct answers to wrong ones.[20] This bears on the follow-up rule "The user disputes a finding" (SKILL.md:104).
- **Hallucinated defects.** Trained critics catch more bugs than paid contractors but have "hallucinated bugs that could mislead humans". Human–model teams hallucinate less than models alone.[21] Saunders et al. found models "may still have relevant knowledge they cannot or do not articulate as critiques".[24]
- **Self-critique is weak without external feedback.** LLMs "struggle to self-correct their responses without external feedback, and at times, their performance even degrades".[22] A critical survey finds "no prior work demonstrates successful self-correction with feedback from prompted LLMs" outside specially suited tasks.[25] On CriticBench, "weaker models can surprisingly surpass stronger ones in their self-critique", and logic tasks are easier to correct.[26]
- **Self-preference.** LLM evaluators score their own outputs higher, and this correlates linearly with their ability to recognise their own text.[23] This bears on `--target=claude`.
- **Fluent indifference to truth.** Hicks et al. argue LLM output is "bullshit" in Frankfurt's sense, "indifferent to the truth of their outputs".[27] For this skill the concrete form is Adorno-flavoured jargon that sounds like critique ("reification", "the nonidentical escapes") with no particular case under it. The skill lists this as a pitfall (SKILL.md:114).
- **No direct study found.** I found no published study of LLMs doing immanent critique or Adorno-style ideology critique specifically. The transfer from code/QA/summary critique to concept critique is my inference.[unverified]

## 4. Fidelity audit

Verdicts: **matches**, **loose** (borrows the idea and simplifies it), **departs** (contrary to the source; may be justified), **unsupported** (no source backs it).

| # | Skill rule (file:line) | What the source says | Verdict |
|---|---|---|---|
| A1 | Thesis: to think is to identify; no thing enters its concept without remainder (SKILL.md:14) | ND p. 5: "To think is to identify"; objects do not go into concepts "without leaving a remainder"[5] | matches |
| A2 | Critique by "specific contradictions between what a concept or claim says and what it actually delivers" (SKILL.md:14) | Near-verbatim from the SEP's gloss of determinate negation[1] | matches (secondary wording) |
| A3 | Rule 1: judge only by the target's own claims; never an outside value (SKILL.md:33) | Hegel: the object "furnishes its own criterion"[10]. Adorno: one can tackle it only "where it is inconsistent with itself"[1]. But Adorno also transforms outside concepts into "what the object, left to itself, seeks to be"[3], and Jaeggi says his immanence is more than a community's held values[15] | loose: this is internal critique; it captures Hegel's anti-dogmatic point but not Adorno's "emphatic concept" |
| A4 | Rule 2: strict gaps only, C + D + "cannot both hold" (SKILL.md:34) | Adorno demands "concrete proof of the falsehood" and rejects mere mistrust[9]; "what is vaguely put is poorly thought"[5]. He also prizes exaggeration and warns that thought trying to "prove its literal correctness … founders"[7]; contradictions may be structural, not logical[9] | loose to departs; theory.md:34 labels this a departure, honestly |
| A5 | Rule 3: one reading at a time; ambiguity is not a finding (SKILL.md:35) | No Adornian counterpart; this is an analytic safeguard. Adorno's aesthetics stresses polarities and ambiguity[1] | unsupported by Adorno (defensible as an engineering rule) |
| A6 | Rule 4 and Step 3: particular cases, the target's own material first (SKILL.md:36, 56) | Geuss: tacking between concept and instances[4]. ND's "models" "are not examples"[6] | loose: cases are used as counterexamples, closer to reductio than to Adorno's models |
| A7 | Rule 5: determinate, not abstract, negation (SKILL.md:37) | Hegel §79[10]; SEP on Adorno[1]; Adorno on Marx ridiculing "abstract negation"[9] | matches |
| A8 | Step 4 "What escapes: … (the nonidentical remainder)" (SKILL.md:66) | No direct access to the nonidentical; it gets only "an indirect, conceptual articulation"[1] | loose: naming the remainder as content risks treating the nonidentical as one more concept |
| A9 | Rule 6 and Step 5: operative function as an inference with a falsifier (SKILL.md:38, 72) | Ideology critique targets the "functional" features of consciousness[3]; exchange drives identity[1]. Falsifiability is Popper's criterion; Adorno says "Not all theorems are hypotheses"[9] | the function idea borrows loosely from Adorno; the falsifier departs from him (Popperian) |
| A10 | "Speak about what the text does, not … hidden motives" (SKILL.md:38, 98) | ND: "The need to let suffering speak"[1]; Adorno reads texts against "what each text intends even in spite of itself"[8] | matches the spirit (critique of objective function, not psychology) |
| A11 | Optional "depends on" two or three concepts (SKILL.md:74) | Constellations unlock "the process stored in the object"[1]; Benjaminian constellation and "critical models"[3] | loose (theory.md:23 says "a light version"; fair) |
| A12 | Rule 7: no forced synthesis; a revision states its remainder (SKILL.md:39) | Prologue: freed from "affirmative essence"[6]; no "new, more adequate concept"[4] | matches; the remainder clause is a good operationalisation |
| A13 | Step 6: options, including narrowing C to C′ (SKILL.md:80) | Adorno: the solution "hardly ever appears from without", which supports options derived from the critique[9]. But structural contradictions "could [not] be eliminated by means of more sophisticated definitions"[9] | loose; Option A can conflict with Adorno when the gap is structural |
| A14 | Rule 8 and Step 7: recommend one option (SKILL.md:40, 88) | "Those who cannot help ought also not advise"[7]; Horkheimer distrusts the categories of "better, useful"[11]; Geuss: no "positive, detachable conclusion"[4] | departs (theory.md:35 admits it) |
| A15 | Rule 10 and the eight steps: one pass, a fixed procedure (SKILL.md:42-92) | Not "a method slapped on outwardly"[5]; "methodically unmethodically"[8]; "not expoundable"[1] | departs (SKILL.md:16 admits it) |
| A16 | Status "open … by design nothing is closed" (SKILL.md:92) | "no natural stopping point"[4] | matches |
| A17 | Follow-up: a revision is a new identification with its own remainder (SKILL.md:103) | Determinate negation as continuing movement[10][4]; theory.md:40 uses this to answer Rosen[18] | loose but well judged |
| A18 | theory.md:27: the operative function draws on exchange and interest | SEP on the exchange principle[1] | matches as background; the skill does not, and should not, import the totality thesis |
| A19 | theory.md:34: Adorno writes by "rhetorical exaggeration and constellation … (SEP)" | The fetched SEP does not say this; *Minima Moralia* §29 and §82 do[7], and ND pairs expression with stringency[5] | the claim is right, the citation is wrong |
| A20 | theory.md:41: internal vs immanent (Jaeggi) "(SEP)" | Supported by the SEP *Critical Theory* entry[3] and Stahl[13], not by the SEP *Adorno* entry that theory.md lists | the claim is right, the citation is wrong |

**Overall.** The skill is faithful on four things: determinate rather than abstract negation, the remainder, refusing a final synthesis, and critiquing what a text does rather than its author's psyche. It is honest about two departures: steps, and a recommendation. It **silently narrows** immanent critique to internal critique (A3). It **imports a Popperian falsifier** without saying so (A9). On strictness it agrees with half of Adorno and contradicts the other half (A4). Two attributions in theory.md are wrong (A19, A20).

## 5. Lineage: what changed from upstream

`diff` between `upstream/installed/negative-dialectics/` and `skills/dia-negative/`:

- **SKILL.md frontmatter.**
  - `name` changed to `dia-negative`.
  - Added `license: MIT` and `metadata` (author, version 1.0.0, lineage, source) per spec §7.2.
  - Description: "Claude's earlier answer" became "the assistant's own earlier answer". "in any language" became "or the same in any language". `reductio`/`socratic-elenchus` became `dia-reductio`/`dia-elenchus`.
- **The Hangul line in the description (spec §5.5).** The upstream description (line 3) carried two Korean glosses after the method name, transliterated *bujeong-ui byeonjeungbeop* and *bujeongbyeonjeungbeop* ("negative dialectics"). Its trigger list carried two Korean trigger terms, *bujeong-ui byeonjeungbeop* and *naejaejeok bipan* ("immanent critique").
  - All four were removed. Their English equivalents ("negative dialectics", "immanent critique") remain as triggers, and the catch-all became "or the same in any language".
  - Probe P7 (Claude Code, n=2 per cell) routed Korean "negative dialectics" prompts to the skill 2/2, the same as the old skill (docs/probes.md:47-56).
  - The routing content survived. What is untested is the Korean term for "immanent critique" alone. P7 used only the "negative dialectics" phrasing for Korean, and the English prompt used "immanent critique".
- **The body.** "Claude" became "you" or "your own earlier answer" (SKILL.md:25, 38, 97). A clause was added: "the value is `claude` on every assistant". No rule, step or pitfall changed.
- **The Hangul line in `references/theory.md` (line 52).**
  - Upstream cited a Sogang University thesis by its Korean author name and Korean title. The rebuild romanised the author ("Kwon Hae-kyung") and gave an ad-hoc English rendering of the title, with the same URL.
  - The thesis record itself gives an official English title: "Adorno's Negative Dialectics as 'Immanent Critique': A Comparative Analysis of Hegel and Adorno's Dialectics in the Epistemological Realm".[28] The rebuild's rendering differs from it.
  - Nothing else was lost; the URL still resolves to the record.[28]
  - No sentence in theory.md's body draws on this thesis, so it is a listed but unused source.
- **`references/output-template.md`.** Only the title changed.
- **Upstream design notes.** `upstream/superclaude-stable-47f791b/docs-features/` has no notes on negative dialectics (searched for Adorno, negative, dialectic, immanent). The only design rationale available is the skill's own theory.md. The general portable-skills principles (mobile-sized turns, no tool dependence, plain-word invocation) come from the socratic-brainstorm research notes, which do not cover this skill.
- **Summary.** The rebuild was a faithful rename. It neither fixed nor introduced any fidelity problem in §4; every issue there is inherited from upstream.

## 6. Risks and failure modes

### 6.1 On LLMs generally

1. **Manufactured gaps.** Invoking the skill signals that the user wants criticism. Feedback sycophancy runs negative when the user signals a negative stance.[20] Critics hallucinate defects.[21] The template has a full Findings section and a fixed Options A–E list (output-template.md:19-44), which pressures the model to fill them. SKILL.md:68 ("Do not invent findings") and the "holding" status are the right counterweights, but the template does not show what a no-findings output looks like in full.
2. **Strictness theatre.** The three-part form (Claims / Delivers / Why both can't hold) can be filled with a "why" that does not show incompatibility. CriticBench suggests critique quality depends on the task, and logic-like checks fare better.[26] The skill has no self-test such as "could both hold under any reasonable reading?" Rule 3 helps only for ambiguity.
3. **Pseudo-falsifiers.** "Would be falsified if the organisation stated otherwise" is not an observation. Since falsifiability is the skill's own guard against mind-reading (A9), a weak falsifier lets the operative-function inference become ideology-critique speculation. That is exactly the "mere mistrust of ideology" Adorno himself rejected.[9]
4. **Jargon.** Rule 9 and output-template.md:3 keep Adorno's terms in parentheses. But the field label "What escapes … (the nonidentical remainder)" (SKILL.md:66) invites high-register filler. Hicks et al.'s point applies to fluent but empty critique.[27]
5. **Self-examination (`--target=claude`).** Self-preference bias[23] and weak intrinsic self-correction[22][25] push the self-examination towards whitewashing. Under "Do not defend the answer" (SKILL.md:97) the opposite failure is also likely: conceding gaps that are not strict, the "Are you sure?" pattern.[20] The one-line "not independent" disclaimer is accurate but does not prevent the second failure.
6. **Follow-up capitulation.** "The user disputes a finding: check it. If the objection holds, withdraw" (SKILL.md:104) is correct. Sycophancy research predicts withdrawal even when the objection fails.[20] The rule does not ask the model to say explicitly when a finding stands.
7. **Structural gaps narrowed away.** Option A ("narrow C to C′") is often the cheapest recommendation. For structural contradictions Adorno says narrowing the definition shifts the problem rather than solving it.[9] Rule 7's "remainder" clause partly covers this.

### 6.2 Tool-less and mobile surfaces

- **No tools.** The skill needs no tools: facts are labelled "unverified recall" and become conditional findings (SKILL.md:36). It degrades cleanly.
- **Unread references.** In the headless probe runs the Read tool needed approval, so some runs worked from SKILL.md alone (docs/probes.md:77). The record format exists only in the template; SKILL.md:92 points there. Without the template the model improvises the record. A short in-body fallback would remove the dependency.
- **Length on a phone.** A typical output has eight sections plus a nine-line record. That runs to roughly 50–80 short lines on a phone (my estimate from the template, not measured).[unverified] The template lists A–E even though SKILL.md:78 says "Offer the responses that fit". The two disagree.

### 6.3 Cross-surface (Claude, Codex, ChatGPT)

- **Over-triggering in Codex.** `allow_implicit_invocation: true` (openai.yaml:7), and P3 showed `dia:dia-negative` in Codex's model-visible list (docs/probes.md:31). Trigger phrases such as "what is this really for" and "what does this concept hide" (SKILL.md:3) are common in coding talk ("what is this flag really for?"). Codex is a coding agent, so implicit over-triggering is a real risk there. No probe has tested it.
- **The target name.** `--target=claude` on ChatGPT/Codex is settled by spec D14, but it reads oddly to users. Natural-language inference (SKILL.md:29) carries the practical load.
- **Probe coverage.** Only Claude Code has been probed (P7). ChatGPT desktop and mobile (P4, P5) are not yet run (docs/probes.md:21-22).

## 7. Findings and recommendations (proposals only)

**F1 — high. The label promises immanent critique; the rules deliver internal critique.**
- Evidence:
  - Rule 1 (SKILL.md:33) is the definition of internal critique.[13][3]
  - theory.md:41 admits "The skill does internal critique by default".
  - Adorno's own formula goes beyond held standards to "what the object, left to itself, seeks to be".[3]
  - Jaeggi says Adorno's immanence is "more and other than" held values.[15]
- Proposal, either (a) or (b):
  - (a) Relabel honestly. Description first sentence: "Internal critique, adapted from Adorno's negative dialectics, run in one pass." Keep "immanent critique" as a trigger term only.
  - (b) Add a labelled immanent step. In Step 2: "Optionally add Cx: what the claim, by its own logic, would have to mean to be true (its 'emphatic' sense). Label it 'reconstructed standard — inference', quote the passages it is built from, and never let a firm finding rest on it alone."
- Either way, change theory.md:41 to name which one the skill does.

**F2 — medium. The falsifier is Popper's device and the text does not say so.**
- Evidence:
  - Rule 6 and Step 5 (SKILL.md:38, 72) require a falsifier for the operative function.
  - Adorno, against Popper: "Not all theorems are hypotheses"; "Viewed from without, everything and nothing is refutable".[9]
- Proposal:
  - Keep the rule. It is the main guard against confabulated "hidden purpose" claims, a risk LLM critique research makes concrete.[21]
  - Add to theory.md §3 "Changed": "The falsifier on the operative-function inference is not Adorno's; it is borrowed from Popper, whom Adorno opposed in the Positivist Dispute. It is kept because a model's inference about function needs a check the user can run."
  - Tighten SKILL.md:72: "name an observation the user could actually make (a document, a practice, a case) that would show the stated purpose explains the pattern as well; a statement of intent is not such an observation."

**F3 — medium. The strictness rule is half-Adornian and is attributed to the wrong source.**
- Evidence:
  - Adorno demands "concrete proof" against mere mistrust,[9] and says "what is vaguely put is poorly thought".[5] Both support Rule 2.
  - *Minima Moralia* §82 says thought that tries to "prove its literal correctness … founders".[7] That opposes it.
  - theory.md:34 cites the SEP for "rhetorical exaggeration", but the SEP does not say that.
- Proposal: rewrite theory.md:34 as "Changed: 'contradiction' is narrowed to a checkable gap, and a finding must be strict. Adorno asked for concrete proof against mere suspicion of ideology (Positivist Dispute, p. 115) and for stringency in presentation (ND pp. 18–19, as cited in the SEP), but he also held that thought needs 'an element of exaggeration' and founders when it tries to prove its literal correctness (*Minima Moralia* §82). The skill keeps the first and drops the second, so findings can be checked and disputed." Cite *Minima Moralia* and ND, not the SEP, for the exaggeration point.

**F4 — medium. Option A can hide structural contradictions, and the recommendation should be allowed to be "keep it open".**
- Evidence:
  - Adorno: structural contradictions "could [not] be eliminated by means of more sophisticated definitions".[9]
  - Adorno: "Those who cannot help ought also not advise".[7]
  - Adorno: a solution "hardly ever appears from without", so options are best derived from the critique.[9]
- Proposal:
  - Add to Step 6, Option A: "If the gap comes from how the practice works rather than from how C is worded, say that narrowing C moves the gap rather than closing it."
  - Add to Step 7: "Each option names the finding it answers. If every finding is conditional, or the gap is structural, Option E may be the recommendation; say why."

**F5 — medium. Template pressure produces findings and options when none fit.**
- Evidence:
  - Sycophancy runs negative under a critical framing.[20]
  - Critics hallucinate defects.[21]
  - output-template.md:39-44 always lists A–E, against SKILL.md:78 "Offer the responses that fit".
- Proposal:
  - Template: replace the fixed A–E list with "Options (only those that fit; usually 2–3)".
  - Add a full no-findings variant: "Findings: none strict. Tested: …. Most likely gap: …. Options and Recommendation are omitted. Status: holding against the tested particulars."
  - Add to Pitfalls: "Filling the template: an empty section is a result."

**F6 — medium. Self-examination and disputed findings need a guard against capitulation as well as defence.**
- Evidence:
  - Self-preference bias.[23]
  - Weak intrinsic self-correction.[22][25]
  - "Are you sure?" sycophancy.[20]
- Proposal:
  - SKILL.md:97: "Do not defend the answer, and do not concede a gap that fails Rule 2."
  - SKILL.md:104: "check it against Rule 2; if the objection holds, withdraw the finding; if it does not, say so and give the reason in one line."

**F7 — medium. Implicit over-triggering in Codex.**
- Evidence:
  - `allow_implicit_invocation: true`, and the skill is visible to Codex (docs/probes.md:31).
  - The triggers "what is this really for" and "what does this concept hide" (SKILL.md:3) are generic.
- Proposal:
  - Narrow the description triggers to "what is this claim/concept/policy really for", "what does this concept hide", "where does this claim fail its own standard".
  - Add "Not for questions about what code or a setting does."
  - Add a probe: three coding prompts using "really for" in Codex with the plugin installed. Pass if dia-negative does not load.

**F8 — low. "What escapes … (the nonidentical remainder)" over-claims.**
- Evidence: the nonidentical gets only "an indirect, conceptual articulation".[1]
- Proposal: SKILL.md:66 should read "**What escapes:** what case D shows that C does not capture. This is itself stated in concepts, so it is partial, not the thing itself." Drop the parenthetical, or move it to theory.md.

**F9 — low. "Particular cases" are counterexamples, not Adorno's models.**
- Evidence: ND's models "are not examples".[6]
- Proposal: add to theory.md §3 "Changed": "Particulars are used as test cases (counterexamples). Adorno's 'models' were extended interpretations of one subject matter, not instances that test a rule; this skill does not attempt them."

**F10 — low. theory.md source attributions.**
- Evidence:
  - (a) The internal/immanent distinction is cited to the SEP *Adorno* entry (theory.md:41), but it is in the SEP *Critical Theory* entry §2.1.[3]
  - (b) "not a system, standpoint, or set of principles (SEP; Stopford)" (theory.md:31) comes from Stopford's abstract[18] and ND's heading "Dialectics Not a Standpoint".[5]
  - (c) "cannot be given in a digest" (theory.md:31) paraphrases "not expoundable" / "no philosophical thinking of quality allows of concise summary".[1]
  - (d) The Kwon thesis has an official English title[28] and is not used in the body.
- Proposal:
  - Add the SEP *Critical Theory* entry and Stahl (2013) to the Sources.
  - Fix the three attributions.
  - Use the thesis's official English title, or drop it.
  - Replace the Wikipedia citation for the Prologue (theory.md:7)[19] with ND itself.[6]

**F11 — low. The record format depends on reading the template.**
- Evidence: some headless runs could not open `references/` (docs/probes.md:77). SKILL.md:92 defers the record to the template.
- Proposal: add to SKILL.md:92: "If the template cannot be read, the record is: target and C; stated purpose; findings (n firm, m conditional); remainder; operative function; options and recommendation; decision; status."

**F12 — low. The "whose aim" wording invites motive attribution.**
- Evidence: SKILL.md:72 "whose aim or what process it serves" sits beside SKILL.md:38 "not about a person's hidden motives". Ideology critique targets functional features of consciousness, not psychology.[3]
- Proposal: SKILL.md:72 should read "what process it serves, or whose interests the pattern favours (as a function, not an intention)".

**F13 — low. Korean routing for "immanent critique" alone is unprobed.**
- Evidence: P7 used only the Korean "negative dialectics" phrasing (docs/probes.md:47). The removed Hangul included the Korean term for "immanent critique" (upstream SKILL.md:3).
- Proposal: add one P7 cell, a Korean prompt using only the Korean term for "immanent critique", at n=2. No text change unless routing drops (spec L7).

## 8. Open questions for the owner

1. **F1:** relabel the skill as internal critique "adapted from Adorno", or add the labelled "reconstructed standard" step? The second is closer to Adorno and Jaeggi but gives the model more room to infer.
2. Should the recommendation stay mandatory (Rule 8)? Adorno argues against advice[7], and the skill already allows "keep the tension open". One option: recommend only when at least one firm finding exists.
3. Adorno grounds critique in suffering[1] and in social totality ("The whole is the false"[7]). The skill imports neither, by design (Rule 1). Should theory.md say so explicitly under "Changed", so the omission is a stated choice?
4. Is a compact mobile layout wanted (findings and record only, options on request), or should the one-response rule (Rule 10) keep the full layout on every surface?
5. Should the skill's display name stay "Negative Dialectics" (openai.yaml:2, SKILL.md:12), or become "Immanent Critique (after Adorno)" to match what it does?

## Sources

[1] https://plato.stanford.edu/entries/adorno — Zuidervaart et al., Theodor W. Adorno, Stanford Encyclopedia of Philosophy (rev. 4 Nov 2024)
[2] https://iep.utm.edu/adorno — Theodor Adorno, Internet Encyclopedia of Philosophy
[3] https://plato.stanford.edu/entries/critical-theory — Critical Theory (Frankfurt School), Stanford Encyclopedia of Philosophy (2023)
[4] https://www.rep.routledge.com/articles/thematic/critical-theory/v-1/sections/negative-dialectics — Geuss, Critical theory §6 Negative dialectics, Routledge Encyclopedia of Philosophy
[5] https://hegel1313.law.columbia.edu/files/2026/03/Adorno-Reader-for-Hegel-1313-Updated.pdf — A Reader on Adorno for Hegel 13/13 (Columbia): Negative Dialectics, Ashton trans., Introduction excerpts
[6] http://rarre.org/documents/Adorno/Negative%20Dialectics-%20Prologue.pdf — Adorno, Negative Dialectics, Prologue (Redmond trans.)
[7] https://cominsitu.files.wordpress.com/2019/09/5580-minima_moralia_reflections_on.pdf — Adorno, Minima Moralia (Jephcott trans.)
[8] https://commons.princeton.edu/hum583-f24/wp-content/uploads/sites/420/2024/10/Adorno_EssayAsForm-copy.pdf — Adorno, The Essay as Form, New German Critique 32 (1984)
[9] http://autodidactproject.org/other/positivismusstreit/positivist_dispute.pdf — Adorno et al., The Positivist Dispute in German Sociology (Heinemann 1976)
[10] https://www.marxists.org/reference/archive/hegel/works/ph/phintro.htm — Hegel, Phenomenology of Mind, Introduction (Baillie trans.), marxists.org
[11] https://criticaltheoryworkshop.com/wp-content/uploads/2018/03/horkheimer_traditional-and-critical-theory.pdf — Horkheimer, Traditional and Critical Theory (1937), in Critical Theory: Selected Essays
[12] https://www.marxists.org/archive/marx/works/1843/letters/43_09-alt.htm — Marx, Letter to Arnold Ruge, September 1843
[13] https://pure.rug.nl/ws/portalfiles/portal/35734818/SSRN_id2357957.pdf — Stahl, What is Immanent Critique? SSRN working paper (2013)
[14] https://www.titusstahl.net/stahlImmanentCritique2022.html — Stahl, Immanent Critique (Rowman & Littlefield) abstract page
[15] https://cef.pucp.edu.pe/wp-content/uploads/2014/08/Rahel-Jaeggi-_No-Individual-Can-Resist_-Minima-Moralia-as-Critique-of-Forms-of-Life.pdf — Jaeggi, No Individual Can Resist: Minima Moralia as Critique of Forms of Life, Constellations 12/1 (2005)
[16] https://www.cairn.info/revue-raisons-politiques-2015-1-page-13.htm — Jaeggi, Towards an Immanent Critique of Forms of Life, Raisons politiques 57 (2015)
[17] https://ndpr.nd.edu/reviews/critique-of-forms-of-life — NDPR review of Jaeggi, Critique of Forms of Life
[18] http://etheses.dur.ac.uk/3650 — Stopford, Adorno's Critique of Judgement, Durham PhD thesis (2012), abstract
[19] https://en.wikipedia.org/wiki/Negative_Dialectics — Negative Dialectics, Wikipedia
[20] https://arxiv.org/html/2310.13548v4 — Sharma et al., Towards Understanding Sycophancy in Language Models (ICLR 2024)
[21] https://arxiv.org/abs/2407.00215 — McAleese et al., LLM Critics Help Catch LLM Bugs (2024)
[22] https://arxiv.org/abs/2310.01798 — Huang et al., Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2024)
[23] https://arxiv.org/abs/2404.13076 — Panickssery et al., LLM Evaluators Recognize and Favor Their Own Generations (2024)
[24] https://arxiv.org/abs/2206.05802 — Saunders et al., Self-critiquing models for assisting human evaluators (2022)
[25] https://arxiv.org/abs/2406.01297 — Kamoi et al., When Can LLMs Actually Correct Their Own Mistakes? (TACL 2024)
[26] https://arxiv.org/abs/2402.14809 — Lin et al., CriticBench (ACL Findings 2024)
[27] https://link.springer.com/article/10.1007/s10676-024-09775-5 — Hicks, Humphries, Slater, ChatGPT is bullshit, Ethics and Information Technology (2024)
[28] https://dcollection.sogang.ac.kr/dcollection/srch/srchDetail/000000065299 — Sogang University thesis record: Adorno's Negative Dialectics as 'Immanent Critique' (dCollection)
