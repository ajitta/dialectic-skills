# Research: dia-elenchus and the Socratic elenchus

| | |
|---|---|
| Skill | `skills/dia-elenchus` (version 1.0.0, lineage socratic-elenchus 1.3.1) |
| Upstream | `upstream/superclaude-stable-47f791b/socratic-elenchus/`, `docs-features/socratic-brainstorm-skill/` (02, 09, 10, 12, 13) |
| Date | 2026-10-20 |
| Status | Research only. Every text change below is a proposal; nothing in `skills/` was edited. |

## 1. Scope and summary of the skill

This document checks dia-elenchus against the method it names: the elenchus of Plato's early dialogues. It also checks it against what is known about how language models behave when asked to question rather than answer. Plato is cited from the Perseus Fowler/Lamb translations, one Stephanus section per source. Secondary scholarship comes from SEP, IEP and a survey chapter on the elenchus debate. LLM claims come from arXiv/ACL papers and vendor pages.

What the skill says, with file:line references (`SKILL.md` unless noted):

- **Identity.** It claims to be "Socratic dialogue (elenchus) as in Plato's Socratic dialogues" (description, l.3). It says it runs "the method of Plato's early (Socratic) dialogues such as the Euthyphro, Laches and Charmides". Aporia-as-gain (Meno) and the midwife (Theaetetus) are framed as "aids, not as the method itself", and the modern list of Socratic question types is excluded (l.14).
- **Shape.** Six steps (l.16-21): ask "What is X?"; get a definition; collect agreed premises one question at a time; show the contradiction; the user revises; most dialogues end in aporia.
- **Brainstorm reading.** "For brainstorming, **the revisions are the ideas**." The assistant is the midwife with no ideas of its own (l.23). The description repeats that each revision is "a new idea the user gives birth to" (l.3).
- **Stance** (l.27-31):
  - "You don't know" (Apology 21d), with no answers, advice or options.
  - Sincerity: irony means only disclaiming knowledge.
  - "The user says what they believe" (Crito 49c-d, Gorgias 495a).
  - Short questions and answers (Protagoras 334c-335c).
  - "Examine statements, not the person."
- **Rules** (l.35-41): one ask per message; phone-sized turns; only agreed premises; quote only real words; stop means stop; never advise; reply in the user's language.
- **Steps 1-6** (l.43-100):
  - Find X and ask "What is X?" in exactly one form.
  - Force a definition rather than examples (Euthyphro 6d-e, Meno 72a-c).
  - Restate the definition and put the first premise in the same turn.
  - Use four premise types: too broad, too narrow (Laches 190e-191c), stated goal, consequence.
  - Keep a "silent numbered list" of premises (l.76).
  - Lay out the contradiction in four lines or fewer (l.80-84).
  - "The user writes [the revision], not you" (l.92).
  - End in aporia, holding (provisional), partly tested, or stopped before testing (l.98-100).
- **After the dialogue.** Suggestions only on request, labeled as the assistant's (l.102-104).
- **References.**
  - `references/elenchus-patterns.md` holds the definition-forcing moves, the premise templates (including the Meno 86e-87b hypothesis move, l.21), pushback replies and "Noticing a birth" (l.42-50). That last section says the moves "are the brainstorm's output" (l.50).
  - `references/record-template.md` is the end-of-dialogue record.

**Summary verdict.** The skill is a careful, mostly faithful operationalisation of the Socratic definition dialogue. Its central logical choice is that a contradiction shows only that the set cannot all stand, and the user decides what to drop. That choice matches the more defensible, non-constructivist side of the scholarly debate. The main fidelity problems:

1. A brainstorming purpose ("ideas born") is grafted on from the one-skill era and presented as part of the method. The source of the midwife image (Theaetetus 210b) actually ends by calling every offspring a wind-egg.
2. Three rules are presented as Socratic but are design choices that go *beyond* or *against* the dialogues: the assistant never proposes a definition, the person is never examined, and no irony is used.
3. One example line overstates the logic: "So ① can't stand as it is" (l.84), against the patterns file's correct "① and ② can't both stand" (patterns l.31).

On the LLM side, the largest risks are sycophantic withdrawal of valid steps under pushback, the "silent" premise list that has no storage on most surfaces, and drift toward advice over long dialogues.

## 2. The method in its primary sources

### 2.1 What the early dialogues show

Vlastos's "elenctic dialogues" are the Apology, Charmides, Crito, Euthyphro, Gorgias, Hippias Minor, Ion, Laches, Protagoras and Republic 1. The Meno and Theaetetus are not on that list.[3]

**The "What is F?" question and its requirements.**

- Euthyphro first answers with an instance ("what you are now doing"). Socrates rejects it: he asked not for "one or two of the many holy acts" but for "the essential aspect, by which all holy acts are holy".[7]
- In the Meno, Socrates asks for the "one common character" by which the many virtues are virtues.[8]
- SEP summarises three requirements on an answer: generality, exclusion, and explanatory power (an essence, not a mere attribute).[1]
- Aristotle credits Socrates with being first to ask *ti esti*, "what is it?".[2]

**Priority of definition.** Socrates asks, "if I do not know what a thing is, how can I know what its nature may be?"[9] SEP distinguishes two priority claims. It notes that the first was attacked by Geach as the "Socratic fallacy", and that "no text unequivocally assigns either claim to Socrates".[1]

**Counterexample from both sides.**

- Laches defines courage as staying at one's post and not running away.[10]
- Socrates offers the Scythians, who fight "as much fleeing as pursuing".[59] He adds the Spartans at Plataea, who won by turning back in flight, and concludes that his own question was put badly.[11]
- That is a too-narrow counterexample. The second definition, endurance of the soul, falls on the too-broad side (foolish endurance). It falls because Laches agrees that courage is always fine (*kalon*).[1]
- The same premise ("X is always fine") drives the Charmides refutation of temperance as quietness.[1]

**Sincere assent.**

- Crito: "be careful, Crito, that you do not, in agreeing to this, agree to something you do not believe".[14]
- Gorgias: Callicles says pleasure and good are the same only "so that my statement may not be inconsistent". Socrates replies that he "can no longer be a fit partner ... in probing the truth, if you are going to speak against your own convictions".[15]
- SEP states the general rules: the partner "must answer every question according to his own beliefs", and "the partner (not the audience if there is one) judges the outcome".[1]
- Socrates tells Polus he is "satisfied with your sole and single assent".[42]

**Brevity.** Socrates asks Protagoras to "cut up your answers into shorter pieces". When Protagoras resists, he insists on "brevity".[16][17]

**Disavowal of knowledge.** "what I do not know I do not think I know either."[13] Socrates says he is "in more doubt than anyone else", which is why he makes others doubt.[19] He examines arguments "mainly for my own sake".[40] He is "glad to be refuted if I say anything untrue".[39]

**Aporia.**

- Meno complains that his "soul and ... tongue [are] quite benumbed" by the "torpedo sea-fish".[44][18]
- In the slave-boy scene, Socrates argues that the boy now "does not think he knows". The "torpedo's shock" did him no harm and will make him "push on in the search gladly".[20][21][22]
- Euthyphro simply leaves: "Some other time, Socrates. Now I am in a hurry".[41]
- Socrates also urges persistence: "let us too be steadfast and enduring in our inquiry".[43]
- SEP notes that the Euthyphro, Charmides and Hippias Major end in impasse, "as is usual for works in this group".[1]

**Surviving theses are provisional.** In the Gorgias, Socrates says his conclusion is "held firm ... with reasons of steel and adamant". He adds in the same breath "that I cannot tell how the matter stands".[38]

**The elenchus examines lives, not only propositions.**

- Nicias: whoever talks with Socrates "cannot stop until he is led into giving an account of himself ... and of the kind of life he has lived". Socrates "will never let him go until he has thoroughly ... put all his ways to the test".[34][35]
- Apology: "the unexamined life is not worth living".[37]

**Socrates also proposes, teaches by example, and exhorts.**

- He offers Euthyphro the idea that holiness is a part of the right, and gets agreement to it.[32][33]
- He gives Laches a model definition of *quickness* before asking for courage "in the same way".[12]
- He gives Meno a sample definition of *figure*.[24]
- In the Hippias Major, four of the seven definitions come from Socrates.[1]
- In the Apology, he says he will never "stop exhorting you".[36]

**Irony.** Thrasymachus calls it "the well-known irony of Socrates" and accuses him of refusing to answer and dissembling.[60] IEP lists the competing senses: saying the opposite of what is meant, Aristotle's self-deprecation, Kierkegaard's ironic character.[2] Vlastos's "complex irony" reads the disavowal of knowledge as true in one sense and false in another, without intent to deceive.[6]

### 2.2 The midwife (Theaetetus) and how it differs from the elenchus

The midwife passage belongs to a later dialogue. IEP says the Theaetetus "is not generally considered Socratic", though it is elenctic and aporetic.[2] In it:

- Socrates says his art tests "whether the mind of the young man is bringing forth a mere image ... or a real and genuine offspring".[26]
- He calls himself "sterile in point of wisdom" and accepts the reproach that he questions others "but make[s] no reply myself".[26]
- His associates progress "not because they have ever learned anything from me, but because they have found in themselves many fair things".[27]
- He warns that people have been "ready to bite me, if I take some foolish notion away from them".[28]
- He opens the examination by asking "whether it is a real offspring or a mere wind-egg".[29]
- The dialogue ends with the art declaring "all the offspring that have been born are mere wind-eggs and not worth rearing". The gain is that Theaetetus will be "gentler to your associates, for you will have the wisdom not to think you know that which you do not know".[30][31]

The SEP Theaetetus entry describes the dialogue as ending in aporia, with no alternative offered.[4] It reports that interpreters disagree about whether the midwife passage alludes to recollection.[4] Burnyeat's thesis that midwifery is a Platonic, not historically Socratic, image is known by its title ("Socratic midwifery, Platonic inspiration"). I could not read the text, so its content is [unverified] here.

IEP also distinguishes three methods: the elenchus ("Socrates the Refuter"), maieutic ("the Midwife"), and dialectic ("the Constructer"), the last thought "more Platonic than Socratic".[2]

### 2.3 Vlastos's standard elenchus and the debate

Vlastos (1983) defined the elenchus as "a search for moral truth by adversary argument in which a thesis is debated only if asserted as the answerer's own belief and is regarded as refuted only if the negation of his thesis is deduced from his own beliefs".[5] His "standard elenchus" has five steps:[5]

1. The interlocutor asserts p, which Socrates targets.
2. Socrates secures agreement to premises Q.
3. The argument is from Q, not to it.
4. Both agree that Q entails not-p.
5. Socrates claims not-p is proven and p false.

**The problem of the elenchus.** Logically, only the inconsistency of p with Q has been shown. The interlocutor could reject a premise instead.[5][2] Vlastos also stresses an "existential dimension": the elenchus tests "the single human being that is doing the answering".[5]

**Responses.**

- Kraut argued that every argument has unargued premises, so Socrates may treat his as simply true.[5]
- Brickhouse and Smith (1984) argued that Vlastos's meta-assumptions cannot be justified by elenchus. Later (2002) they argued "there is no such thing as 'the Socratic elenchus'", which on their view is an artifact of modern scholarship.[5]
- Benson's non-constructivist reading: the elenchus shows only inconsistency, aims to persuade the interlocutor of his ignorance, and requires that the interlocutor *understand* the argument (an "availability constraint").[5][1]
- Tarrant argued the word *elenchus* is rare for Socrates' own activity, and that *exetasis* (examination) fits the Apology better.[5]
- Robinson (1941/1953) held that Socrates shows the thesis to be self-contradictory; Vlastos rejected that view.[5]

IEP summarises the two camps. Constructivists hold that the elenchus establishes truth or falsity. Non-constructivists hold it shows only that the conjunction is false and serves to expose confusion, "and, according to some scholars, to use that confusion as a stepping stone".[2]

## 3. Modern research on LLM "Socratic" behavior

**The word means something else in most LLM work.**

- Tutoring research defines Socratic questioning as guiding "the student ... towards solving a problem on their own, instead of being given the solution directly".[45] That is the hint-and-scaffold sense, not the definition-and-refutation sense.
- Chang's prompting paper treats "definition, elenchus, dialectic, maieutics" as interchangeable prompt techniques for getting better answers *from* the model.[48]
- Vendor "Socratic" modes are of the same kind:
  - ChatGPT study mode "combines Socratic questioning, hints, and self-reflection prompts".[52]
  - Claude's Learning mode illustrates Socratic questioning with "What evidence supports your conclusion?"[53]
  - That example is an evidence question from Paul & Elder's critical-thinking scheme, which also lists clarification, assumption, viewpoint and implication questions.[55]
- This is the "question-type tour" the skill explicitly rejects (l.108).

**Models drift toward telling.**

- MathDial reports that LLMs "fail at tutoring because they ... are prone to revealing solutions to students too early".[47]
- In Socratic debugging, GPT-4's poor turns include "overly direct" and "premature" utterances. Even GPT-4's precision and recall fall below human experts.[46][45]
- The LearnLM team states that generative AI systems "are tuned to present information by default".[56]
- An EMNLP 2025 paper says optimisation for direct question-answering "undermines effective pedagogy which requires strategically withholding answers".[58]
- A 2025 benchmark finds LLMs "often fail to provide effective adaptive scaffolding when learners experience confusion".[57]
- This is the empirical basis for the skill's "Advisor drift" pitfall (l.109). It also bears on the user's moment of aporia, where the urge to resolve confusion with content is strongest.

**Sycophancy under challenge.** Sharma et al. find that assistants "frequently wrongly admit mistakes when questioned by the user". After "Are you sure?", models changed their initial answer 32-86% of the time and admitted a mistake 42-98% of the time.[49] In an elenchus, the assistant's refutation steps are exactly the claims a user will push back on.

**Multi-turn degradation.**

- Across six tasks, multi-turn performance drops 39% on average. Models "make assumptions in early turns ... and do not recover".[50]
- Instruction-following drifts measurably "within eight rounds".[51]
- The elenchus is a long, stateful dialogue: the premise ledger, the current definition and the list of shifts all persist across turns.

**Hidden state does not persist uniformly.** Anthropic's docs say newer Claude models "keep prior turns' thinking blocks in context", whereas older ones "stripped them".[54] Whether any private reasoning survives to the next turn therefore depends on model and surface. A "silent" list is only reliable if it can be rebuilt from the visible transcript.

## 4. Fidelity audit

Verdicts: **matches** (the rule restates the source), **loose** (fair adaptation, but simplified or moved to a new domain), **departs** (contrary to the source or adds what it lacks), **unsupported** (cited source does not say it).

| # | Skill rule (file:line) | What the sources say | Verdict |
|---|---|---|---|
| A1 | Ask "What is X?" in one form (l.16, l.51) | Core Socratic question; Aristotle credits Socrates with *ti esti*[2]; Euthyphro 6d[7] | matches |
| A2 | Examples are not definitions; ask what all cases share (l.59; patterns l.7-13) | Euthyphro 6d "the essential aspect, by which all holy acts are holy"[7]; Meno 72c[8] | matches |
| A3 | Find X: the assistant picks the concept the user's *idea* stands on (l.45-51) | The elenchus starts from the partner's statement, "which usually implies a claim to wisdom" about virtue[1]; X arises from the interlocutor's confidence (Euthyphro) | loose: moved from virtue terms with a presumed essence to artefact and product concepts, where definitions are partly stipulative |
| A4 | Premises one short question at a time (l.18, l.35, l.30) | Protagoras 334d-335a on brevity[16][17]; question-and-answer style of the early group[1] | matches. "One ask per message" is stricter than Plato, where Socrates sometimes asks compound or long questions, but it is in the spirit |
| A5 | Only agreed premises; no hidden premise; each step checkable (l.37) | Premises often have "no authority aside from the partner's agreement"[1]; Benson's availability constraint[5]. But Socrates sometimes argues *for* a premise by epagoge[1], and scholars dispute whether he argues fairly[6] | matches the ideal; stricter than Plato's practice |
| A6 | Too broad / too narrow premises (l.69-70) | Laches 190e-191c (too narrow)[10][59][11]; endurance → foolish endurance (too broad)[1] | matches |
| A7 | "Stated goal" premise (l.71) | The typical Socratic premise is "X is always *kalon*/beneficial" (Laches, Charmides)[1]. A user's goal plays that role | loose but well-founded |
| A8 | Consequence and hypothesis premises (l.72; patterns l.21) | Meno 86e: examine "by means of hypothesis ... what the geometricians often do"[23] | matches (Meno is transitional, as the skill says) |
| A9 | Contradiction laid out; "So ① can't stand as it is" (l.82-84) vs "① and ② can't both stand" (patterns l.31) | Logically only the conjunction is refuted; this is the "problem of the elenchus"[5][2] | l.84 departs (Vlastos step 5 overclaim); patterns l.31 and l.86 match the non-constructivist reading |
| A10 | User may withdraw a premise instead (l.86) | Charmides could reject q or r instead of p[5] | matches |
| A11 | User judges; "examine statements, not the person" (l.31, l.111) | Partner judges the outcome[1] (matches). But the elenchus tests "the single human being"[5], the person's life (Laches 187e-188a[34][35]; Apology 38a[37]); Brickhouse & Smith: it tests lives[5] | departs (deliberate; should be labeled) |
| A12 | Sincere assent; re-ask a pleasing answer (l.29) | Crito 49d[14]; Gorgias 495a[15]; Vlastos's "answerer's own belief"[5] | matches |
| A13 | "You don't know" (Apology 21d), no answers or advice (l.27) | Apology 21d is about not *thinking* one knows[13]. The "no reply myself" reproach is Theaetetus 150c[26] and Aristotle's report[2]. But Socrates exhorts (Apology 29d)[36] and holds strong views (SEP)[1] | disavowal matches; "never advise" is loose: a design choice that the midwife image supports better than the Apology |
| A14 | Never offer a definition; "the user writes it" (l.92) | Socrates proposes "part of the right" (Euthyphro 11e-12d)[32][33], model definitions (Laches 192b[12], Meno 75b[24]) and four Hippias Major answers[1] | departs from the early dialogues; matches only the Theaetetus midwife's "sterile" self-description[26] |
| A15 | Irony = only refusing to claim knowledge, never mockery (l.28) | Socrates' irony was notorious (Republic 337a)[60]; IEP lists several senses[2]; Vlastos's complex irony[6] | departs (deliberate; reasonable for an assistant; should be labeled) |
| A16 | Ends in aporia by default; aporia is a gain (l.21, l.98) | Usual ending of the group[1]; Meno 84a-c[20][21][22]; Theaetetus 210b-c[30][31] | matches |
| A17 | Surviving definition is "held so far", never "proven" (l.98) | Gorgias 508e-509a "steel and adamant" yet "I cannot tell how the matter stands"[38] | matches (non-constructivist) |
| A18 | Each revision is an idea the user gives birth to; list of "ideas born" (l.3, l.23, l.92; patterns l.42-50; record l.20-21) | The midwife tests offspring and discards wind-eggs; at Theaetetus 210b all of them are wind-eggs "not worth rearing"[30]. Revisions in the early dialogues are failed attempts at one true definition, not ideas to collect[1] | departs: a brainstorming purpose layered on the method |
| A19 | Not Paul's question types (l.14, l.108) | Paul & Elder's categories (clarification, assumptions, evidence, viewpoints, implications)[55] are distinct from the definition elenchus | matches (the distinction is correct) |
| A20 | Cited loci | Euthyphro 6d-e ✓[7]; Meno 72a-c ✓[8]; Laches 190e-191c ✓ (Scythians at 191a[59]); Crito 49c-d ✓ (the sincerity line is at 49d[14]); Gorgias 495a ✓[15]; Protagoras 334c-335c ✓[16][17]; Apology 21d ✓[13]; Meno 84a-c ✓; Meno 86e-87b ✓[23]; Theaetetus 150b-151d ✓[25][26][27][28]; wind-egg 151e ✓[29]; 210b-c ✓[30][31] | all checked loci exist and say roughly what the skill uses them for. Exception: 210b-c is used for aporia-as-gain, while 210b also undercuts "ideas born" |

## 5. Lineage: what changed from upstream, and what was lost

**Diff against `socratic-elenchus` 1.3.1.** The only changes are:

- the name;
- `metadata.version`, `lineage` and `source`;
- two `socratic-brainstorm` → `dia-brainstorm` pointers (SKILL.md l.53, l.104);
- `agents/openai.yaml` display name and `default_prompt`;
- one record-template line, where "`/sc:brainstorm` or `/sc:design`" became "A later `dia-brainstorm` session" (record l.44).

The two reference files are otherwise byte-identical. This matches spec §5.2 ("Behavior: unchanged from the reference"). Nothing behavioral was lost in the rebuild.

**Design history from the owner's notes:**

- **v1 was not the elenchus** (09 §1). It used "Paul's modern 'Socratic questioning'", Osborn-style diverge/converge, contradictions "waited for, not constructed", and aporia as one verdict among three. The owner caught this, and the core was rebuilt as the elenchus (09 §1-4).
- **The method table** (09 §2) maps each element to a Plato locus "checked against Perseus". Vlastos (1983) is cited for "agreed premises contradict the thesis → revise", but the notes do not record that Vlastos himself was read. That table is the origin of every locus in SKILL.md; §4 above re-checked them.
- **"How it stays a *brainstorm*"** (09 §3): "The ideas come from the revisions." This was written while elenchus *was* the brainstorm skill (socratic-brainstorm 2.0.0).
- **The split** (10 §1-2) moved the brainstorm role back to socratic-brainstorm 3.0.0 (now dia-brainstorm) and kept the elenchus as the strict skill. The "ideas born" layer was not removed in the split, and it survives today in the description (l.3), l.23 ("For brainstorming ..."), patterns l.50 ("the brainstorm's output") and the record's "Ideas born" section. This is the main residue of the one-skill era (Finding 1).
- **Probe-driven fixes** (09 §6):
  - no confirm-only turns;
  - lay out a collision immediately;
  - "the user writes the revised definition, not you", added after Codex wrote revised definitions for the user;
  - exactly three result labels, later four (13 L6).
  - The noted "remaining imperfection" is that the model summarised a premise as if it were the user's definition. It was left unfixed "because one more rule risks making the dialogue stiff" (09 §6).
- **Independent review** (13 §2):
  - L3 corrected the "early dialogues" overclaim and marked Meno/Theaetetus as aids.
  - L4 enforced one "what is X" form.
  - L5 required the restatement to keep the user's key words.
  - The quoted-ending observation became Rule 4.
  - The reviewer flagged the Paul attribution as unsourced. It is now supported by Paul & Elder's own guide.[55]
- **Ambiguous "Socratic" routing** is a coin flip (12 §2), which is why l.53 adds a pointer line. P7 shows elenchus routing 2/2 in Korean and English for both arms (docs/probes.md).
- **Not yet probed for dia:** P2 (Claude mobile) and P5 (ChatGPT mobile). P8 (tool-less) covered only refine and iterate. The elenchus needs no tools except the optional save (l.100), so tool-less risk is low, but a mobile multi-turn run has not been recorded for dia.

## 6. Risks and failure modes

### 6.1 On LLMs generally

1. **Capitulation under pushback.** The "That's a leap" handler (patterns l.37-38) tells the model to withdraw a step "if they're right". Given measured sycophancy rates,[49] the likely failure is withdrawing a *valid* step because the user objected. That silently destroys the contradiction, which is the point of the method. The rule needs an equally explicit "if the step does follow, show it again and keep it".
2. **Advice leakage at aporia.** Tutoring studies show premature and overly direct turns, especially when the learner is confused.[46][47][57] The aporia moment is where a model will most want to "help" with a definition. The skill forbids that (l.92, l.109) but has no specific script for the confused or frustrated user (Meno's torpedo,[44] Theaetetus "ready to bite"[28]).
3. **Writing the definition through the back door.** 09 §6 already records a model turning a premise into a definition. The "name the shift" step (l.92; patterns l.44-48: "from a means to an end", "from a feature to a condition") invites the model to *interpret* the user's revision with its own abstract label. That is a mild form of supplying the idea.
4. **Overclaiming the refutation.** The l.84 sample ("① can't stand as it is") will be copied verbatim. It frames every contradiction as the definition's fault and nudges users away from the premise-withdrawal option the skill itself allows (l.86).
5. **Ledger loss over many turns.** The premise list is "silent" (l.76; patterns l.23), but there is no private memory across turns on many models and surfaces.[54] Multi-turn reliability drops with length.[50][51] The visible transcript is the only durable store. Numbering is invented at contradiction time and may not match what the user remembers agreeing to.
6. **Too many definitions demanded.** The priority-of-definition principle is contested (Geach's "Socratic fallacy").[1] For everyday design concepts, a user may legitimately know cases without a common essence. The skill's refusal handler ("Then how would you tell whether what you're building is X", patterns l.13) is good, but nothing tells the model that "no single common feature" can itself be an honest result.

### 6.2 Tool-less and mobile surfaces

- The skill is tool-free by construction. The only tool mention is conditional ("If a filesystem exists and the user asks", l.100), which satisfies spec §7.1.
- Reference files may not be readable. That was observed in Codex sandboxes (09 §7) and in headless Claude Code without Read permission (probes P8 observations). Everything essential except the record layout and pushback scripts is in SKILL.md, and the record falls back to an improvised one (09 §6). Consider putting the four result labels' criteria in SKILL.md; they are currently only in record l.36-41.
- Phone fit: Rule 2 and the ≤4-line contradiction suit mobile. The final record has eight sections and is long on a phone. That is acceptable because it comes once and at the end, and the template already forbids code blocks.

### 6.3 Cross-surface (Claude / Codex / ChatGPT)

- **Codex/ChatGPT invocation.** `allow_implicit_invocation: false` (openai.yaml l.6) means the skill fires only when called by name. P3 found that the plugin form is `$dia:dia-elenchus`. The `default_prompt` says `$dia-elenchus` (openai.yaml l.4), which resolves only for a copied folder (spec §4; probes P3). That is a packaging issue shared by all seven skills, not specific to this one.
- **Host Socratic modes.** ChatGPT study mode is system-prompt driven and its makers acknowledge "inconsistent behavior".[52] Claude Learning mode uses Paul-style evidence questions.[53] If the user runs the skill inside such a mode, the host instructions may push the dialogue back toward hints and question-type tours. The skill's Pitfall l.108 is the only guard.
- **Model differences already seen.** Codex re-confirmed instead of probing and wrote definitions for the user. Claude invented result labels (09 §6). Both were fixed by text. These are n=1 observations on older model versions and should be re-run for dia.

## 7. Findings and recommendations (proposals only)

**1. The "ideas born" brainstorm layer is presented as part of the elenchus — high.**

- Evidence:
  - description l.3 ("each revision is a new idea the user gives birth to");
  - l.23 ("For brainstorming, the revisions are the ideas");
  - patterns l.50 ("These moves are the brainstorm's output");
  - record "Ideas born" section.
- This layer dates from when elenchus was socratic-brainstorm 2.0.0 (09 §3) and survived the split (10 §1).
- In the source, the midwife discards wind-eggs. At Theaetetus 210b, all offspring are wind-eggs "not worth rearing", and the gain is knowing what one does not know.[30][31] Early-dialogue revisions are failed attempts at one definition.[1]
- There *is* a defensible rationale: for artefact concepts, definitions are partly stipulative, so a revision is a design decision. It is this skill's adaptation, not Plato's.
- Proposal:
  - Replace l.23 with: "**Adaptation, not Plato:** in the dialogues a fallen definition is simply discarded (Theaetetus 210b). Here the concepts are your user's own designs, so each revision also records a choice they made. Keep a list of the shifts, but judge each one as the midwife does: sound, or a wind-egg."
  - In the description, change "each revision is a new idea the user gives birth to" to "each revision is recorded as the user's own refinement".
  - In patterns l.50, change "These moves are the brainstorm's output" to "These moves go in the record."

**2. The l.84 example overstates what a contradiction proves — high.**

- Evidence: l.84 "So ① can't stand as it is" vs patterns l.31 "So ① and ② can't both stand", and l.86, which allows withdrawing a premise.
- This is the "problem of the elenchus": only the conjunction is refuted.[5][2]
- Models copy examples verbatim, so the l.84 line biases every dialogue toward revising the definition.
- Proposal: change l.84 to "> So ① and ② can't both stand. Which would you change?"

**3. No guard against sycophantic withdrawal of valid steps — high.**

- Evidence:
  - patterns l.38 only covers the case where the user is right;
  - SKILL.md l.86 says "check honestly";
  - measured capitulation rates are 32-86% answer changes and 42-98% false admissions after "Are you sure?".[49]
- Proposal: in patterns after l.38, add: "If the step does follow, don't withdraw it to please them. Show it again in one line, quoting their agreed words, and ask which part they reject. Then they may withdraw a premise (that counts as a revision)."

**4. "Never offer a definition" and "no ideas of its own" are labeled Socratic but are stricter than the early dialogues — medium.**

- Evidence:
  - Socrates proposes "part of the right" in the Euthyphro;[32][33]
  - he gives model definitions in Laches 192b[12] and Meno 75b;[24]
  - Hippias Major answers come from Socrates.[1]
  - The "no reply myself" stance is the Theaetetus midwife[26] and Aristotle's report.[2]
- Proposal:
  - Label the rule: at l.92 add "(Stricter than Socrates, who sometimes proposed definitions, e.g. Euthyphro 12d; here the ideas must stay the user's.)"
  - Add the genuinely Socratic, idea-neutral move to patterns "Forcing a definition": "| Still gives examples after one push | Give a one-line definition of an unrelated everyday thing (Laches 192b: quickness = getting much done in little time), then: 'Can you say X in that form?' |"

**5. "Examine statements, not the person" departs from the elenchus — medium.**

- Evidence: Laches 187e-188a;[34][35] Apology 38a;[37] Vlastos's existential dimension; Brickhouse & Smith on testing lives.[5]
- The choice suits an assistant, but it is presented as part of the method.
- Proposal: at l.31, write "**Examine statements, not the person.** (A deliberate departure: Socrates examined how people lived, Laches 187e-188a. You don't.) A contradiction belongs to the statements; the user decides what to give up."

**6. The irony line rewrites Socratic irony — low.**

- Evidence: Republic 337a;[60] IEP's senses of irony;[2] Vlastos's complex irony.[6]
- Proposal: at l.28, write "**Sincere, not ironic.** Plato's Socrates was famous for irony (Republic 337a). You drop it: no feigned admiration, no mockery. Only the plain admission that you don't know what X is."

**7. "Never advise" rests on the wrong citation — low.**

- Evidence: Apology 21d is about not *thinking* one knows.[13] Elsewhere in the Apology, Socrates exhorts (29d).[36] The no-answers stance is Theaetetus 150c.[26]
- Proposal: at l.27, write "**You don't know** (Apology 21d) **and give nothing of your own** (Theaetetus 150c)." Add "Unlike Socrates, who also exhorted (Apology 29d), you never advise."

**8. The "silent numbered list" has no storage on many surfaces — medium.**

- Evidence: l.76; patterns l.23. Thinking-block retention varies by model.[54] Multi-turn degradation is documented.[50][51]
- Proposal: change l.76 to "Keep the agreed premises recoverable from the conversation itself. Before laying out a contradiction, re-read the user's actual answers and number them then. If the dialogue is long, restate the current definition at the start of a premise question."
- Change patterns l.23 to "Number premises when you lay them out, from the user's actual answers."

**9. "Name the shift" invites the model to interpret the revision — medium.**

- Evidence: 09 §6 "remaining imperfection"; patterns l.44-48 give abstract labels ("from a means to an end").
- Proposal: at l.92, write "Name the shift in one line, using the user's own words on both sides ('no deliberating → a choice you don't tire of'). Don't add your own label for the kind of move." Keep the patterns l.44-48 categories as guidance for the *record* only.

**10. No script for the frustrated or numbed user — medium.**

- Evidence: Meno 80a-b;[44][18] Theaetetus 151c;[28] Euthyphro 15e.[41] LLMs handle learner confusion poorly.[57] Signs of aporia (patterns l.52-58) cover "I don't know" but not irritation.
- Proposal: add to patterns "When the user pushes back": "'This is pointless' / irritation → one line naming it (Meno compared Socrates to a numbing sea-fish; feeling stuck is where the examination works), then one choice: keep going, or stop and get the record."

**11. Priority of definition is applied without acknowledging its limit — low.**

- Evidence: SEP on Geach's "Socratic fallacy" and that no text unequivocally commits Socrates to it.[1]
- Proposal: add to Signs of aporia (patterns l.52-58): "If the user shows that the cases share nothing single, record that as the finding ('X may have no one defining feature') rather than forcing a fourth definition."

**12. Scope shift from virtue terms to product concepts is unlabeled — low.**

- Evidence: SEP says the elenchus starts from "a claim to wisdom" about virtue.[1] The skill's examples are a lunch app, retrospectives and a coding class (l.47-49).
- Proposal: at l.14, after "It is not the modern list...", add "Plato applied it to virtues such as piety and courage; this skill applies the same shape to the concept behind a user's idea."

**13. Result-label criteria live only in the reference file — low.**

- Evidence: record l.36-41. Reference files were unreadable in some runs (09 §7; probes P8 observations).
- Proposal: at l.100, add one sentence: "aporia = at least one definition fell and none survives; holding = passed a breadth test and a goal or consequence test; partly tested = passed some test, then stopped; stopped before testing = current definition untested."

**14. Host "Socratic" modes may override the method — low.**

- Evidence: study mode and Learning mode use hint and evidence questions;[52][53] Paul's categories.[55]
- Proposal: at Pitfalls l.108, add "If the app has its own study or learning mode, its hints and evidence questions are not this method; keep to definitions, premises and contradictions."

**15. Cross-surface probes for dia-elenchus are missing — medium.**

- Evidence: 09 §6 probes were run on older model versions; P2 and P5 have not been run (docs/probes.md).
- Proposal: no skill text change. Re-run the two scripted dialogues (lunch, retro) on Claude mobile and ChatGPT, plus one pushback-sycophancy script ("that doesn't follow" against a valid step). Record the results in docs/probes.md.

## 8. Open questions for the owner

1. Should dia-elenchus keep any idea-generation role now that dia-brainstorm exists? Or should "Ideas born" become a neutral "How the definition changed" (already a template section), with the shifts moved there?
2. Do you want strict *early-dialogue* fidelity, which would allow the assistant to propose candidate definitions as Socrates does (Euthyphro 12d)? Or strict *midwife* fidelity (Theaetetus 150c), which forbids it? The skill currently mixes the two and cites both.
3. Should the skill name its interpretive stance explicitly (non-constructivist: a contradiction shows only that the set cannot stand)? This would be one line in the intro.
4. Is "examine statements, not the person" a safety rule you want to keep regardless of fidelity? If so, label it as a departure (Finding 5).
5. Should a sycophancy probe (a valid step plus "that's a leap") be added to the spec's probe list for this skill?
6. The `default_prompt` uses `$dia-elenchus`, but the Codex plugin route resolves `$dia:dia-elenchus` (probes P3). Fix it for all seven skills together?

## Sources

[1] https://plato.stanford.edu/entries/plato-ethics-shorter — SEP: Plato's Shorter Ethical Works (Woodruff)
[2] https://iep.utm.edu/socrates — IEP: Socrates
[3] https://plato.stanford.edu/entries/socrates — SEP: Socrates (Nails)
[4] https://plato.stanford.edu/entries/plato-theaetetus — SEP: Plato on Knowledge in the Theaetetus
[5] https://sites.temple.edu/dwolf/files/2020/06/Socratic-philosophizing.pdf — Wolfsdorf, Socratic Philosophizing (survey of elenchus scholarship)
[6] https://bmcr.brynmawr.edu/1992/1992.03.20 — BMCR review of Vlastos, Socrates: Ironist and Moral Philosopher
[7] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0170:text=Euthyph.:section=6d — Plato, Euthyph. 6d (Perseus, Fowler/Lamb tr.)
[8] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Meno:section=72c — Plato, Meno 72c (Perseus, Fowler/Lamb tr.)
[9] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Meno:section=71b — Plato, Meno 71b (Perseus, Fowler/Lamb tr.)
[10] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0176:text=Lach.:section=190e — Plato, Lach. 190e (Perseus, Fowler/Lamb tr.)
[11] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0176:text=Lach.:section=191c — Plato, Lach. 191c (Perseus, Fowler/Lamb tr.)
[12] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0176:text=Lach.:section=192b — Plato, Lach. 192b (Perseus, Fowler/Lamb tr.)
[13] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0170:text=Apol.:section=21d — Plato, Apol. 21d (Perseus, Fowler/Lamb tr.)
[14] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0170:text=Crito:section=49d — Plato, Crito 49d (Perseus, Fowler/Lamb tr.)
[15] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Gorg.:section=495a — Plato, Gorg. 495a (Perseus, Fowler/Lamb tr.)
[16] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Prot.:section=334d — Plato, Prot. 334d (Perseus, Fowler/Lamb tr.)
[17] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Prot.:section=335a — Plato, Prot. 335a (Perseus, Fowler/Lamb tr.)
[18] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Meno:section=80b — Plato, Meno 80b (Perseus, Fowler/Lamb tr.)
[19] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Meno:section=80c — Plato, Meno 80c (Perseus, Fowler/Lamb tr.)
[20] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Meno:section=84a — Plato, Meno 84a (Perseus, Fowler/Lamb tr.)
[21] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Meno:section=84b — Plato, Meno 84b (Perseus, Fowler/Lamb tr.)
[22] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Meno:section=84c — Plato, Meno 84c (Perseus, Fowler/Lamb tr.)
[23] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Meno:section=86e — Plato, Meno 86e (Perseus, Fowler/Lamb tr.)
[24] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Meno:section=75b — Plato, Meno 75b (Perseus, Fowler/Lamb tr.)
[25] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Theaet.:section=150b — Plato, Theaet. 150b (Perseus, Fowler/Lamb tr.)
[26] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Theaet.:section=150c — Plato, Theaet. 150c (Perseus, Fowler/Lamb tr.)
[27] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Theaet.:section=150d — Plato, Theaet. 150d (Perseus, Fowler/Lamb tr.)
[28] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Theaet.:section=151c — Plato, Theaet. 151c (Perseus, Fowler/Lamb tr.)
[29] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Theaet.:section=151e — Plato, Theaet. 151e (Perseus, Fowler/Lamb tr.)
[30] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Theaet.:section=210b — Plato, Theaet. 210b (Perseus, Fowler/Lamb tr.)
[31] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0172:text=Theaet.:section=210c — Plato, Theaet. 210c (Perseus, Fowler/Lamb tr.)
[32] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0170:text=Euthyph.:section=11e — Plato, Euthyph. 11e (Perseus, Fowler/Lamb tr.)
[33] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0170:text=Euthyph.:section=12d — Plato, Euthyph. 12d (Perseus, Fowler/Lamb tr.)
[34] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0176:text=Lach.:section=187e — Plato, Lach. 187e (Perseus, Fowler/Lamb tr.)
[35] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0176:text=Lach.:section=188a — Plato, Lach. 188a (Perseus, Fowler/Lamb tr.)
[36] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0170:text=Apol.:section=29d — Plato, Apol. 29d (Perseus, Fowler/Lamb tr.)
[37] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0170:text=Apol.:section=38a — Plato, Apol. 38a (Perseus, Fowler/Lamb tr.)
[38] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Gorg.:section=509a — Plato, Gorg. 509a (Perseus, Fowler/Lamb tr.)
[39] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Gorg.:section=458a — Plato, Gorg. 458a (Perseus, Fowler/Lamb tr.)
[40] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0176:text=Charm.:section=166d — Plato, Charm. 166d (Perseus, Fowler/Lamb tr.)
[41] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0170:text=Euthyph.:section=15e — Plato, Euthyph. 15e (Perseus, Fowler/Lamb tr.)
[42] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Gorg.:section=475e — Plato, Gorg. 475e (Perseus, Fowler/Lamb tr.)
[43] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0176:text=Lach.:section=194a — Plato, Lach. 194a (Perseus, Fowler/Lamb tr.)
[44] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0178:text=Meno:section=80a — Plato, Meno 80a (Perseus, Lamb tr.)
[45] https://aclanthology.org/2023.bea-1.57 — Al-Hossami et al. 2023, Socratic Questioning of Novice Debuggers (BEA)
[46] https://arxiv.org/html/2310.03210 — Al-Hossami et al. 2024, Can Language Models Employ the Socratic Method? (SIGCSE)
[47] https://arxiv.org/abs/2305.14536 — Macina et al. 2023, MathDial
[48] https://arxiv.org/abs/2303.08769 — Chang 2023, Prompting LLMs With the Socratic Method
[49] https://arxiv.org/html/2310.13548v4 — Sharma et al., Towards Understanding Sycophancy in Language Models
[50] https://arxiv.org/abs/2505.06120 — Laban et al. 2025, LLMs Get Lost In Multi-Turn Conversation
[51] https://arxiv.org/abs/2402.10962 — Li et al. 2024, Measuring and Controlling Instruction (In)Stability
[52] https://openai.com/index/chatgpt-study-mode — OpenAI, Introducing study mode
[53] https://www.anthropic.com/news/introducing-claude-for-education — Anthropic, Introducing Claude for Education (Learning mode)
[54] https://platform.claude.com/docs/en/build-with-claude/extended-thinking — Anthropic docs, Extended thinking
[55] https://www.criticalthinking.org/TGS_files/SocraticQuestioning2006.pdf — Paul & Elder, The Thinker's Guide to Socratic Questioning (2006)
[56] https://arxiv.org/abs/2412.16429 — LearnLM Team 2024, LearnLM: Improving Gemini for Learning
[57] https://arxiv.org/abs/2508.06583 — GuideEval: Evaluating instructional guidance in Socratic LLMs (2025)
[58] https://arxiv.org/abs/2505.15607 — Dinucu-Jianu, Macina et al. 2025, From Problem-Solving to Teaching Problem-Solving
[59] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0176:text=Lach.:section=191a — Plato, Lach. 191a (Perseus, Lamb tr.)
[60] https://www.perseus.tufts.edu/hopper/text?doc=Perseus:text:1999.01.0168:book=1:section=337a — Plato, Republic 1.337a (Perseus, Shorey tr.)
