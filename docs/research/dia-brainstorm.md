# Research: dia-brainstorm

| | |
|---|---|
| Skill | `skills/dia-brainstorm` (metadata.version 1.0.0, lineage `socratic-brainstorm 3.3.1`) |
| Upstream | `upstream/superclaude-stable-47f791b/socratic-brainstorm/` and `docs-features/socratic-brainstorm-skill/` |
| Date | 2026-10-20 |
| Status | Research only. Every text change below is a proposal; nothing in `skills/` was edited. |

## 1. Scope and what the skill says now

This document checks dia-brainstorm against the methods it names or borrows from: Richard Paul's "Socratic questioning", Socratic questioning as guided discovery in cognitive therapy, Plato's midwife image, Osborn-style brainstorming, and criteria-based decision making. It also checks the skill against research on how LLMs behave as ideation partners and interviewers.

The skill in brief (file:line refs are to `skills/dia-brainstorm/`):

- **Label.** The description calls it a brainstorming partner that uses "modern Socratic questioning (Paul's six question types, one question at a time)" and sends requests for the strict Platonic dialogue to dia-elenchus (`SKILL.md:3`). The body says it "borrows the Socratic spirit ... but it is not the strict method of Plato's dialogues" (`SKILL.md:16`). The H1 is still "Socratic Brainstorm" (`SKILL.md:12`).
- **Stance.** "You are a questioning partner, not an advisor. The user owns the idea and its answers." (`SKILL.md:14`)
- **Hard rules** (`SKILL.md:18-26`):
  1. one ask per message, chosen from the last answer;
  2. phone-sized turns with numbered choices;
  3. no answers before Step 3;
  4. quotation marks only around the user's exact words;
  5. stop and continue signals honored at once;
  6. never implement;
  7. reply in the user's language.
- **Step 0, Frame** (`SKILL.md:28-39`). Infer the mode (`develop` or `stress`) and the depth (quick ~4, standard ~8-10, deep). Add a pointer to dia-elenchus when the request only says "Socratic". Don't manufacture doubt about an idea that is already precise.
- **Step 1, Thesis** (`SKILL.md:41-43`). Steelman the idea, mark what was assumed versus said, ask "Is that right?", and keep a *working thesis*.
- **Step 2, Probe** (`SKILL.md:45-73`). Six question types (clarification, assumptions, evidence, viewpoints, implications, the question itself) in a usual order. Six tactics: concreteness, counterexample, contradiction surfacing, definition pressure, falsification, necessity. Rhythm rules: switch type after two probes that don't move the thesis, then go to Step 3 after two dry switches; a parking lot; a pacing cue; at most two optional lenses.
- **Step 3, Diverge** (`SKILL.md:75-81`). The user's own options come first, each built on with "yes, and" before any judging. Then edges: cheapest, most extreme, do nothing. Then at most 3 assistant options, labeled "My ideas:".
- **Step 4, Converge** (`SKILL.md:83-91`). Get 2-3 criteria in the user's words. Ask the user to place the options against them, or ask one trade-off question. Give a pick only on explicit request. Tag each decision confirmed or delegated.
- **Step 5, Verdict and brief** (`SKILL.md:93-103`). Verdict: sharpened, open or refuted, each with a strict condition. The brief is built only from the user's answers. A file only if a filesystem exists and the user asks. Then stop.
- **Pitfalls** (`SKILL.md:105-111`): interview drift, advisor drift, leading questions, agreement theater, wall of text.
- **References.** `references/question-bank.md` holds example questions, tactic templates, optional lenses (premortem, six "expert lenses", SCAMPER, edges) and the switch ring. `references/brief-template.md` holds the brief sections and the rules for refuted, risky and delegated.
- **Codex/ChatGPT sidecar.** `agents/openai.yaml` sets `allow_implicit_invocation: false`, with `default_prompt: "Use $dia-brainstorm to question me about this idea: "`.

Spec §5.3 says the behavior is "unchanged from the reference". Section 5 confirms that.

## 2. The methods in their sources

### 2.1 Richard Paul's Socratic questioning (critical-thinking pedagogy)

- **The six types.** The "six types" go back to Paul's 1990 book *Critical Thinking: What Every Person Needs to Survive in a Rapidly Changing World*. A teaching essay that summarizes it lists six categories as "created and reported by Paul": clarification, probing assumptions, probing reasons and evidence, viewpoints or perspectives, probing implications and consequences, and questions about the question.[2] I did not obtain the 1990 book itself, so the attribution rests on secondary sources.[unverified]
- **How later sources count the types.** Course handouts call the same list "Richard W. Paul's six types of Socratic questions".[4] Another handout lists nine "R.W. Paul's Socratic questions": the six plus questions that probe purpose, concepts, and inferences and interpretations.[3] An EACL 2023 dataset paper that cites Paul and Elder (1990; 2019) uses five of the six types plus a catch-all "Others"; it has no "question about the question" type.[5] So "Paul's six types" is a fair label for the 1990 list, but it is not the only form of the taxonomy.
- **The 2006 Thinker's Guide.** Paul and Elder's later guide builds its "Taxonomy of Socratic Questions Based in Critical Thinking Concepts" around elements of thought and intellectual standards. Its checklist asks whether the questioner made the goal clear, pursued relevant information, questioned inferences, focused on key concepts, noted assumptions, questioned implications, called attention to point of view, kept the central question in focus and asked for context. It then adds standards: clarity, precision, accuracy, relevance and depth.[1]
- **What dia-brainstorm's six types leave out.** Compared with the 2006 guide, the six types omit purpose, concepts, inferences, and the standards of accuracy and precision. The skill partly covers concepts with its "Definition pressure" tactic (`SKILL.md:63`).
- **Procedural rules in the 2006 guide**, all relevant here:
  - Socratic questioning is a discussion "led by a person who does nothing but ask questions" that is "systematic and disciplined (it is not a free-for-all)".[1]
  - "You are not allowed to answer any questions, except by asking another question."[1]
  - "Base each of your questions on the answer given by the last student", and "Take seriously every answer that is given".[1]
  - The checklist's model clarification move is "Let me tell you what I understand you to be saying. Is my Interpretation correct?"[1]
- **Purpose.** In the 1990 framing, Socratic questioning "helps students arrive at a judgment through their own reasoning".[2]

Reading: the skill's Steps 0-2 and Rules 1 and 3 follow Paul closely. Paul's method has no Step 3 or Step 4. The questioner never adds options or picks. The skill's later steps are a deliberate extension, and the description says so ("followed by brainstorming", `SKILL.md:16`).

### 2.2 Socratic questioning as guided discovery (cognitive therapy)

- **Padesky's distinction.** Padesky's 1993 keynote separates Socratic questioning that "changes minds" from questioning that "guides discovery". She says: "In the best cognitive therapy, there is no answer. There are only good questions that guide discovery of a million different individual answers."[6]
- **Her definition.** Socratic questioning asks questions which "a) the client has the knowledge to answer b) draw the client's attention to information which is relevant to the issue being discussed but which may be outside the client's current focus c) generally move from the concrete to the more abstract so that d) the client can, in the end, apply the new information to either reevaluate a previous conclusion or construct a new idea".[6]
- **Four stages.** Informational questions, empathic listening, summarizing, and synthesizing or analytical questions.[6]
- **Summaries.** "One of the most common mistakes I notice therapists making in the Socratic questioning process is that they don't summarize enough", with "a summary every few minutes".[6]
- **Synthesis.** The synthesizing question is the last chance "for the client to discover something unexpected".[6]
- **Listening.** "Listen for idiosyncratic words", and "If you are not truly curious to know the answer, don't ask the question."[6]
- **Status of the account.** A narrative review notes that Padesky's account rests "largely on clinical observation rather than empirical evidence". It has nonetheless become widely espoused and is built into descriptions of CBT competence. The review also finds the components of the Socratic method poorly delineated.[7] The same review reports the view that guided discovery aids engagement, while pushing a patient toward a conclusion the therapist already holds may cause disengagement.[7]
- **One empirical result.** In one study of 55 depressed adults, within-patient Socratic questioning in early sessions predicted session-to-session symptom change. The authors call this "the first empirical support" for that link.[8] It is therapy evidence, not brainstorming evidence. It shows the questioning stance can matter. It does not show that it improves ideas.

Reading: Padesky's account fits dia-brainstorm better than Plato does. It covers the user's own knowledge, concreteness first, no hidden right answer, summaries and a synthesis. The skill takes "concreteness first" (`SKILL.md:60`) and "no leading questions" (`SKILL.md:109`) from this family. It does not take two of Padesky's four stages: repeated summaries and a closing synthesizing question asked of the user (findings F2, F3).

### 2.3 Plato: elenchus and the midwife

- **The elenctic dialogues.** The SEP entry on Socrates names the "elenctic dialogues", "called 'elenctic dialogues' for Socrates's preferred method of questioning": Apology, Charmides, Crito, Euthyphro, Gorgias, Hippias Minor, Ion, Laches, Protagoras and Republic I.[9]
- **The midwife passage.** The image of drawing ideas out of the other person comes from the Theaetetus, which is outside that list. There Socrates says: "I am sterile in point of wisdom ... the god compels me to act as midwife, but has never allowed me to bring forth". His companions progress "not because they have ever learned anything from me, but because they have found in themselves many fair things and have brought them forth".[10] His art is to "test in every way whether the mind of the young man is bringing forth a mere image, an imposture, or a real and genuine offspring".[10]

Reading: two parts of the skill touch the midwife image. "The user owns the idea" (`SKILL.md:14`) and user-first divergence (`SKILL.md:79`) borrow it. The assistant's own labeled options (`SKILL.md:81`) and an on-request pick (`SKILL.md:89`) depart from it: the midwife has no offspring of his own. The skill does not claim the elenchus, and the owner's earlier redesign moved the strict method into a separate skill (`docs-features/.../10-two-skills.md` §2). Line 16 still describes "drawing ideas out of the user" as "the Socratic spirit" without naming its source or saying that Step 3 departs from it (F1).

### 2.4 Brainstorming: Osborn, group productivity, nominal groups, fixation

- **Osborn's rules**, as Diehl and Stroebe summarize them: "the more ideas the better and the wilder the ideas the better, improve or combine ideas already suggested; and do not be critical". Osborn claimed that "the average person can think up twice as many ideas when working with a group than when working alone".[11]
- **Group losses.** Diehl and Stroebe tested free riding, evaluation apprehension and production blocking. They found that "production blocking accounted for most of the productivity loss of real brainstorming groups".[11] A meta-analysis found brainstorming groups "significantly less productive than nominal groups, in terms of both quantity and quality".[12]
- **Nominal group technique.** It runs four stages: silent generation, round robin, clarification and voting (ranking). Silent generation means individuals first "silently reflect or record their individual ideas".[13]
- **Divergent and convergent.** The split is usually traced to Guilford. His structure-of-intellect model lists divergent and convergent production among five operations; the APA dictionary adds that the evidence for that model "is weak".[14] The skill does not cite Guilford, and only the diverge/converge vocabulary depends on him.
- **Fixation.** Design fixation is "a blind adherence to a set of ideas or concepts limiting the output of conceptual design".[16] In brainstorming, "exchanging ideas in a group reduced the number of domains of ideas that were explored", and ideas "conformed to ideas suggested by other participants". Fixation narrowed breadth but did not reduce the number of ideas.[15] Kohn and Smith also note that conformity caused by examples has been shown to be unaffected by instructions to avoid conformity.[15]

Reading: dia-brainstorm is a dyad, so production blocking and evaluation apprehension in groups mostly do not apply. The user-first rule matches NGT's silent generation followed by exposure. "Yes, and ... before judging" (`SKILL.md:79`) matches Osborn's no-criticism and build-on rules. "Three other ways" sets a number where Osborn says "the more the better" (F12). The fixation results predict that the assistant's options will narrow the categories the user goes on to consider, even when they are labeled. The skill limits this by order and by a cap of 3, but it says nothing about which categories its own options come from (F5).

### 2.5 Convergence by criteria (decision analysis)

- **People miss their own objectives.** In three studies, participants "consistently omitted nearly half of the objectives that they later identified as personally relevant", and the omitted ones were "almost as important" as those they had listed.[28]
- **People miss their own alternatives.** Decision makers "identify less than half of their alternatives", and the overlooked ones are of the same average quality. Using objectives as stimuli "enhances both the number and quality of created alternatives".[29]
- **The UK MCDA manual.** Its "standard feature" is a performance matrix (consequence table): options as rows, criteria as columns.[30] "The number of criteria should be kept as low as is consistent with making a well-founded decision. There is no 'rule'".[30] It says reliable support usually needs numerical weights and scores, with exceptions such as dominance, and that "in practice, dominance is rare".[30] Its case studies score a status quo option alongside the others.[30]
- **Choice overload.** A meta-analysis of 50 experiments found "a mean effect size of virtually zero but considerable variance".[31]
- **Anchoring.** In Tversky and Kahneman's classic numerical studies, arbitrary starting values "had a marked effect on estimates", and payoffs for accuracy did not reduce the effect.[32] That is numerical anchoring. For option sets, the fixation work in §2.4 is the closer evidence.

Reading:

- "Get 2-3 criteria in the user's words" (`SKILL.md:87`) and "place the options against those criteria" (`SKILL.md:88`) are a light, verbal form of the MCDA matrix with no weights. That fits a chat, and the manual sets no number of criteria.
- The research says unprompted users will list only part of what matters to them, so a single "what matters most?" will usually miss criteria (F4).
- Siebert and Keeney suggest criteria also help *generate* options. The skill asks for criteria only after diverging (F6).
- The do-nothing edge (`SKILL.md:80`) matches the status-quo option in MCDA practice.
- The cap of 3 assistant options has no support in choice-overload research. Its real justification is attribution, anchoring and phone length, and the skill should say so if it states a reason at all.

### 2.6 Interviewing: one question at a time

- **Survey design.** Pew: "It is also important to ask only one question at a time." Double-barreled questions "are difficult for respondents to answer and often lead to responses that are difficult to interpret."[34] This supports Rule 1 and its compound-ask clause (`SKILL.md:20`). The owner's probes found that clause necessary: a question-mark-counting rule still produced compound asks in 2 of 3 runs, and the reworded rule gave single asks in 3 of 3 (`08-implementation.md` §2).
- **Acquiescence.** Pew also describes acquiescence bias in agree/disagree formats. It is "even more pronounced when there's an interviewer present", and a better practice is "to offer respondents a choice between alternative statements".[34] The skill's "Is that right?" after the steelman (`SKILL.md:43`) is a yes/no confirmation of the assistant's own statement, which is the format that invites acquiescence (F8). Paul and Elder use the same move ("Is my Interpretation correct?"), so the skill matches its source here. The risk comes from survey research, not from Paul.
- **LM elicitation.** In preregistered experiments, LMs prompted to elicit preferences with open-ended questions got responses "often more informative than user-written prompts or labels". They also surfaced "novel considerations not initially anticipated by users".[39] This supports question-led elicitation in general. It does not test a Socratic protocol.

## 3. How LLMs behave in this role

### 3.1 As idea generators

- **Novel but repetitive.** In a study with 100+ NLP researchers, LLM-generated research ideas were "judged as more novel (p<0.05) than human expert ideas while being judged slightly weaker on feasibility".[18] Of 4,000 generated seed ideas, "there are only 200 non-duplicate unique ideas".[18]
- **Less diverse than human groups.** Idea pools from GPT-4 "with various plausible prompts are less diverse than ideas generated by groups of human subjects". Prompt engineering, and chain-of-thought most of all, substantially improved dispersion.[21]
- **Homogenizing across users.** Writers given generative-AI ideas wrote stories judged more creative, but "more similar to each other than stories by humans alone".[19] ChatGPT users "tended to produce less semantically distinct ideas" than users of another tool, and "felt less responsible for the ideas they generated".[20]
- **Counter-evidence.** In a large dynamic experiment, high AI exposure "did not affect the creativity of individual ideas but did increase the average amount and rate of change of collective idea diversity". The authors sum up: "AI made ideas different, not better", with "no main effects of disclosure", i.e. labeling an idea as AI-made changed little.[22]
- **Where models help.** ChatGPT raised the creativity of ideas compared with no technology or a web search, and "was most effective at generating incrementally (versus radically) new ideas".[27]

Implication: model-added options can help (see also §2.5 [29]), but by default they drift toward the typical. "My ideas:" labeling (`SKILL.md:81`) serves honest attribution in the brief. The disclosure result suggests it does little to prevent anchoring.

### 3.2 Order: human first, model later

- **Fixation from AI images.** Support from an AI image generator during ideation "leads to higher fixation on an initial example". Participants produced "fewer ideas, with less variety and lower originality".[17]
- **Timing.** "Using LLMs from the beginning reduced the number of original ideas and lowered creative self-efficacy and self-credit." The authors propose "delaying the use of LLMs".[25]
- **Later unassisted work.** LLM assistance "can provide short-term boosts in creativity during assisted tasks" but "may inadvertently hinder independent creative performance" when people later work without it.[23]
- **Think first.** A "think first, ChatGPT later" group first generated their own ideas and then improved them with ChatGPT. That group outperformed both other groups in later independent creativity.[24]
- **Who leads.** A model-led mode "substantially improved idea quality but reduced idea diversity and users' perceived idea ownership". A reflective, human-led mode in which the LLM elicits elaboration "through suggestions or questions" improved quality "while preserving diversity and ownership".[26]

Implication: "Ask the user for their own options first" (`SKILL.md:79`) and "no answers before Step 3" (`SKILL.md:22`) are among the best-supported rules in the skill. Of all its rules, they have the strongest modern evidence.

### 3.3 As questioners and dialogue partners

- **Premature solutions.** In multi-turn settings, LLMs "often make assumptions in early turns and prematurely attempt to generate final solutions, on which they overly rely". Performance dropped 39% on average compared with single-turn.[37] This supports confirming the restatement before probing (`SKILL.md:43`) and Rule 3. It also argues for re-stating the working thesis now and then in long sessions, which the skill tracks but never shows (F2).
- **Telling too early.** As tutors, LLMs "fail at tutoring because they generate factually incorrect feedback or are prone to revealing solutions to students too early".[38] This is the "advisor drift" the skill names (`SKILL.md:108`).
- **Sycophancy.** Five state-of-the-art assistants "consistently exhibit sycophancy", and both humans and preference models sometimes prefer "convincingly-written sycophantic responses over correct ones".[35] In multi-turn tests, "alignment tuning amplifies sycophantic behavior", measured by how quickly and how often models flip under sustained user pressure.[36] For this skill the exposure is the verdict: "agreement theater" (`SKILL.md:110`) on the way in, and a flip from "open" to "sharpened" when the user pushes back (F9).
- **Machine-generated Socratic questions.** A Socratic question-generation dataset of 110K (question, context) pairs, labeled with Paul and Elder's types, shows that models can produce type-conditioned questions. Crowdworkers sometimes preferred the generated questions to the reference ones.[5] Type labels are therefore usable by models, but nothing shows that type rotation alone moves a thesis.

## 4. Fidelity audit

Verdicts: **matches** (the source says this); **loose** (in the spirit of the source, but changed or simplified); **departs** (contrary to the named source, deliberately or not); **unsupported** (no external source found; a design heuristic).

| # | Skill rule (location) | What the source says | Verdict |
|---|---|---|---|
| A1 | "Paul's six question types" (`SKILL.md:3,16,49-56`) | Paul 1990 lists six categories [2]. Later Paul and Elder material uses an elements-of-thought taxonomy plus standards [1]. Handouts and datasets give 9 or 5 types [3][5] | matches the 1990 list; label should date it (F1) |
| A2 | One ask per message, chosen from the last answer (`:20`, `:107`) | "Base each of your questions on the answer given by the last student" [1]. Survey design: one question at a time, no double-barreling [34] | matches |
| A3 | No answers before Step 3; "what would you do?" gets a question (`:22`) | "not allowed to answer any questions, except by asking another question" [1] | matches (stricter in the source, which has no Step 3) |
| A4 | Steelman, mark assumed vs said, "Is that right?" (`:43`) | Paul and Elder: "Let me tell you what I understand you to be saying. Is my Interpretation correct?" [1]. A steelman strengthens rather than restates, and yes/no confirmation invites acquiescence [34] | loose (F8) |
| A5 | Usual order: clarify, then assumptions/evidence, then viewpoints/implications (`:47`) | Padesky: move "from the concrete to the more abstract" [6]. Paul gives no fixed order [1] | loose; reasonable |
| A6 | Concreteness pull (`:60`) | Padesky (c), concrete first [6] | matches |
| A7 | Counterexample, contradiction surfacing, definition pressure (`:61-63`) | Elenctic moves [9]. The skill waits for collisions rather than building them, as the owner's own redesign note says (`09-elenchus-redesign.md` §1) | loose; honestly disclaimed (`:16`) |
| A8 | Falsification pull, required once in stress (`:64,70`) | Fits Paul's evidence category ("anything which might change the student's mind") [2]. The Popper lineage is not cited [unverified] | loose |
| A9 | Necessity check (`:65`) | From the upstream requirements-analyst agent (`02-research.md` §1). No external source | unsupported (harmless) |
| A10 | Switch type after two non-moving probes; stop after two dry switches (`:69`) | From community skills (`02-research.md` §2). No research source | unsupported heuristic |
| A11 | Working thesis kept and updated (`:43`) | Padesky: summarize "every few minutes" and share the summary [6] | loose: kept but not shown (F2) |
| A12 | User's options first (`:79`) | NGT silent generation [13]; LLM timing and order studies [24][25][26] | matches, well supported |
| A13 | "Yes, and" before judging; wild ones welcome (`:79`) | Osborn: build on ideas, do not be critical, wilder is better [11] | matches |
| A14 | "Three other ways" (`:79`) | Osborn: "the more ideas the better" [11] | loose (F12) |
| A15 | Edges: cheapest, most extreme, do nothing (`:80`) | Osborn wild ideas [11]; MCDA scores a status quo option [30] | loose; reasonable |
| A16 | At most 3 assistant options, labeled, one line each (`:81`) | Paul: the questioner only asks [1]. Midwife: no offspring of his own [10]. External stimuli improve alternatives [29][27]. LLM options homogenize [18][19][20][21]. Disclosure has little effect [22]. Choice overload does not justify the cap [31] | departs from Paul/Plato by design; loose against ideation research (F5) |
| A17 | 2-3 criteria in the user's words (`:87`) | People omit nearly half of their objectives [28]. Keep criteria few; no rule [30] | loose (F4) |
| A18 | Place options against criteria, or one trade-off question (`:88`) | MCDA performance matrix [30] | loose (verbal, unweighted); fits chat |
| A19 | Pick only on explicit request, then ask what would change it (`:89`) | Paul: no answers [1]; Padesky: "there is no answer" [6] | departs, intentionally and labeled |
| A20 | Confirmed vs delegated decisions (`:91`) | From upstream `/sc:brainstorm`. Indirect support from acquiescence research: a bare "ok" is weak evidence [34] | unsupported but sound |
| A21 | Verdicts sharpened / open / refuted with strict conditions (`:97-99`) | Theaetetus: the art tests whether the offspring is real or "a mere image" [10]. "Open" stands in for aporia | loose; well guarded |
| A22 | Brief built only from the user's answers (`:101`) | Padesky ends with a synthesizing *question* to the client, not a therapist-written conclusion [6]; Paul: the student reaches the judgment [2] | loose: "Thesis after" is assistant-written (F3) |
| A23 | Never implement (`:25,103`) | Consistent with the questioner-only stance [1][10] | matches |
| A24 | Premortem lens (`question-bank.md:50`) | Klein: assume the project "has just failed", then generate plausible reasons [33] | matches |
| A25 | Expert lenses: Drucker ... Beck (`question-bank.md:51-57`) | No source checked. The lines are paraphrases in quotation marks; "Beck" is ambiguous next to Aaron Beck of CBT [unverified] | unsupported (F11) |
| A26 | Advisor drift: "have you considered X?" is a disguised suggestion (`:108`) | Padesky's changing-minds vs guiding-discovery distinction [6]. But Padesky (b) allows drawing attention to information outside the user's focus [6] | matches, but the boundary is unclear (F10) |
| A27 | Evidence probes such as "How many cases is that?" (`question-bank.md:20`) | Padesky (a): ask only what the client "has the knowledge to answer" [6] | partly; no explicit answerability rule (F7) |

Overall: the questioning half (Steps 0-2) is a faithful, compressed version of Paul's Socratic questioning plus parts of Padesky's guided discovery. The idea half (Steps 3-4) is Osborn plus light decision analysis, and it departs on purpose from both Paul and the midwife image. The skill's labels admit this in substance (`SKILL.md:16`). The weaknesses are mostly omissions relative to the sources (summaries, a synthesizing question, missed criteria, option diversity), not misattributions.

## 5. Lineage

### 5.1 What changed from upstream 3.3.1

A file-by-file diff of `upstream/superclaude-stable-47f791b/socratic-brainstorm/` against `skills/dia-brainstorm/`:

- `SKILL.md`:
  - frontmatter `name`, `metadata.version` (3.3.1 → 1.0.0), `metadata.lineage` and `metadata.source`;
  - the cross-reference `socratic-elenchus` → `dia-elenchus` in the description (`:3`), the intro (`:16`) and Step 0 (`:37`).
  - No behavioral line changed.
- `references/brief-template.md`: removed the final rule "In a repository that uses superclaude, a suitable next step is `/sc:design` or `/sc:review` on the brief. Suggest it; don't run it." (upstream line 44). This follows spec D14 (no other projects named).
- `references/question-bank.md`: identical.
- `agents/openai.yaml`: `display_name` "Socratic Brainstorm" → "Dia: Brainstorm"; `default_prompt` `$socratic-brainstorm` → `$dia-brainstorm`. Policy unchanged.

So spec §5.3 ("Behavior: unchanged from the reference") holds. The only content lost is the superclaude handoff suggestion. The brief's "Next step" now has no default follow-on, which is the intended outcome of D14.

### 5.2 Why the skill looks the way it does (owner's design notes)

- **v1 (1.0.0)** combined elenchus and maieutics, with headings "Probe (elenchus)" and "Diverge (maieutics)". The requirements R1-R19 trace each rule to community skills and SuperClaude assets (`03-analysis.md` §2).
- **2.0.0** rebuilt it as Plato's elenchus. The owner had noticed that the six types are "Richard Paul's modern 'Socratic questioning'" and that diverge/converge "is Osborn's brainstorming, which defers judgment. The elenchus judges at every step" (`09-elenchus-redesign.md` §1).
- **3.0.0** restored the v1 body under an "honest description" and moved the elenchus to its own skill (`10-two-skills.md` §2).
- **3.1.0** added the one-line pointer for generic "Socratic" wording. In the ambiguous-routing probe (3 runs per prompt), "socratic method on my idea" loaded dia-elenchus's predecessor in 2 of 3 runs, and two Korean wordings loaded brainstorm in 3 of 3 (`12-followups.md` §2).
- **3.2.0** renamed the remaining "(elenchus)/(maieutics)/(aporia)" headings (`13-review.md` M3).
- **3.3.x** removed Korean from the skill text (`docs-features/portable-skills-single-plugin/05-plan.md`). The Korean stop-signal examples from R11 are gone. Rule 5 now relies on "or the same in the user's language" (`SKILL.md:24`).

Not carried into dia, and not recorded anywhere in this repo:

- **Stale summary.** The feature README in `docs-features/socratic-brainstorm-skill/` still says 3.2.1. The 3.3.x changes appear only in the single-plugin plan. This does not affect dia; the lineage field is correct.
- **Old reviewer concern.** The owner's independent review listed "the Paul attribution" as unsupported by its source pack and kept it as "standard" (`13-review.md` §2). §2.1 above finds secondary support for Paul (1990) as the origin of the six categories. The 1990 primary text was not checked.
- **Dropped design notes.** Two of the owner's explicit reasons are no longer visible in the skill text: chips anchor answers, so numbered text options are used (`04-design.md` §3), and the brief was kept as a fixed section order rather than a validated schema. Both are sound; nothing needs restoring.

## 6. Risks and failure modes

### 6.1 On LLMs generally

| Risk | Evidence | Current guard | Gap |
|---|---|---|---|
| Advisor drift and early solutions | [37][38] | Rule 3; pitfall `:108` | The line between a test case and an alternative is unclear (F10) |
| Compound asks | owner probes, `08-implementation.md` §2 | Rule 1 wording (3/3 after the fix) | none known |
| Homogeneous, typical model options | [18][19][20][21] | cap of 3, labels | no diversity instruction (F5) |
| User fixates on the model's options | [15][17][25] | user first; options come last | none known |
| Verdict inflation; flips under pushback | [35][36] | strict verdict conditions; "say which tests did not happen" | no rule for pushback on the verdict (F9) |
| Drift over long or `deep` sessions | [37] | working thesis; checkpoint every ~5 probes in deep | the thesis is not shown to the user (F2) |
| Invented quotes | owner probes, `13-review.md` obs | Rule 4 | none known |
| Asking for facts nobody in the chat has | Padesky (a) [6] | none | F7 |
| Missing criteria at convergence | [28] | none | F4 |

### 6.2 Tool-less and mobile surfaces

- **No tools needed.** The skill uses no tool. Files are conditional (`SKILL.md:101`), and the brief's section list is repeated inline in `SKILL.md:101`, so the skill can finish when `references/` cannot be read. The probes observed exactly that: some headless runs "worked from the SKILL.md body alone" (`docs/probes.md`, P8 observations).
- **What is lost without `references/`.** The lenses and the switch ring live only in the question bank. Without it, a model told that lenses exist (`SKILL.md:73`) may improvise "expert" questions and attribute them to named people (F11).
- **No fact-checking.** Tool-less sessions cannot check facts. Evidence probes therefore have to be answerable from the user's own knowledge, or parked as open questions (F7).
- **Skills on claude.ai.** Skills need code execution enabled ("This feature requires code execution to be enabled").[40] A claude.ai chat with that setting off never loads the skill, which is a separate failure from a tool-less run.
- **Phone length.** Turns are phone-sized and options numbered (`SKILL.md:21`). The two long messages are the options list (allowed to run long, `:81`) and the brief. The brief keeps every empty section with "none" (`brief-template.md:3`). With ten sections, an early-stopped session prints a long, mostly empty brief on a phone (F13).
- **Untested.** P8 (tool-less) covered dia-refine and dia-iterate only. P2 (Claude mobile) is still open. No dia-brainstorm run has been recorded on a tool-less or mobile surface (F15).

### 6.3 Across surfaces

- **Claude.** `allow_implicit_invocation` affects only Codex and ChatGPT.[41] On Claude, the description alone governs routing, and it includes "poke holes in this plan" (`SKILL.md:3`). Claude can therefore load the skill implicitly where Codex cannot. P7 found brainstorm routing intact at n=2 (`docs/probes.md`).
- **Generic "Socratic" wording** remains ambiguous between dia-brainstorm and dia-elenchus. The pointer line handles a misroute rather than preventing it (`SKILL.md:37`; `12-followups.md` §2).
- **Codex.** P3 found that plugin skills are named `$dia:dia-<x>` and that `$dia-<x>` "did not resolve" (`docs/probes.md` P3). The sidecar's `default_prompt` uses `$dia-brainstorm`, which is the copied-folder name. Whether `default_prompt` resolves in the Codex app or ChatGPT desktop is listed as not covered (P3) (F14).
- **ChatGPT.** Skills are invoked with `@` or implicitly by description.[41] Explicit-only means `@dia-brainstorm`. Plan availability on Pro is unconfirmed (spec §9).
- **Reply language.** One dia-refine run answered in Korean to an English prompt, possibly because of the host locale (`docs/probes.md` P8). Rule 7 carries the same risk here; it was not tested for this skill.

## 7. Findings and recommendations (proposals only)

**F1 (medium): make the label exact about what comes from where.**

- *Evidence.* §2.1 and §2.3. The six types are Paul's 1990 list [2]. Later Paul and Elder versions differ [1][3][5]. "Drawing ideas out of the user" is the Theaetetus midwife [10], who contributes nothing of his own, unlike Step 3.
- *Proposal.* Replace `SKILL.md:16` with: "What this is: **modern Socratic questioning**, after Richard Paul's six types of Socratic questions (Paul, 1990) and guided discovery as used in cognitive therapy, followed by brainstorming (diverge, then converge). From Socrates it borrows only the stance of asking rather than telling and the image of drawing ideas out of the user (Plato's *Theaetetus*). Unlike Socrates, you add a few options of your own in Step 3 and may give a pick when asked. It is not the strict method of Plato's dialogues. If the user wants that (...), switch to the `dia-elenchus` skill."
- Optionally retitle the H1 (`SKILL.md:12`) to "Brainstorm by Socratic questioning".

**F2 (medium): show the working thesis periodically.**

- *Evidence.* Padesky: the most common mistake is not summarizing enough; summarize "every few minutes" [6]. LLMs lose track over multiple turns [37].
- *Proposal.* Add to the Step 2 Rhythm list (`SKILL.md:67-73`): "When an answer changes the working thesis, or every ~4 probes, open your next message with the current working thesis in one line ("So far: …"), then ask the next question. This counts toward the turn length; keep it to one line."

**F3 (medium): let the user draw the conclusion before the verdict.**

- *Evidence.* Padesky's fourth stage is a synthesizing question to the client [6]. Paul: the student reaches "a judgment through their own reasoning" [2]. Today "Thesis after" is assistant-written (`brief-template.md:12`).
- *Proposal.* Insert at the start of Step 5 (`SKILL.md:95`): "Unless the user sent a stop signal, first ask one synthesizing question: "Putting it all together, how would you now state the idea?" Use their answer as the thesis after; if you must tighten it, show both." Then in `brief-template.md:12`: "After: <the user's restatement; your tightening, if any, marked as yours>".

**F4 (medium): prompt once for missed criteria.**

- *Evidence.* People omit nearly half of their own objectives, and the omitted ones are nearly as important [28]. Keep the criteria few [30].
- *Proposal.* After `SKILL.md:87` add: "Then ask once whether anything is missing, offering common kinds as a numbered list (cost, time, risk, reversibility, people affected, fun). Keep at most three criteria; if more come up, ask which three matter most."

**F5 (medium): make the assistant's options differ in kind.**

- *Evidence.* LLM ideas cluster [18][21]. They also homogenize across users [19][20]. Examples narrow the domains people explore [15]. Labeling ideas as AI-made had no main effect [22].
- *Proposal.* Replace `SKILL.md:81` with: "Only then add **at most 3** options of your own, labeled as yours ("My ideas:"), each a single line. Each must use a different approach from every option already listed and from each other (a different mechanism, owner or scale, not a variant). If you can't find a genuinely different one, add fewer. Number every option so far; this one message may run past the line limit, so keep each option to one short line."

**F6 (low): use criteria as a generation prompt (optional).**

- *Evidence.* Objectives used as stimuli increase the number and quality of alternatives [29].
- *Proposal.* After the edges in `SKILL.md:80` add: "If the user named what matters during probing, add one prompt: "What option would win on <their criterion>, even if it loses elsewhere?""
- This does not reorder the steps. See open question Q2.

**F7 (medium): ask only what the user can answer.**

- *Evidence.* Padesky (a) [6]. On tool-less surfaces neither side can look anything up (§6.2).
- *Proposal.* Add to Rule 1 (`SKILL.md:20`) or the start of Step 2: "Ask only what the user can answer from their own experience or knowledge. If the idea turns on a fact neither of you can check here, don't ask them to guess it; record it under open questions as something to find out."

**F8 (low): phrase confirmation so correction is easy.**

- *Evidence.* Acquiescence bias in yes/no, agree/disagree formats [34]. LLM early assumptions persist [37]. The source move itself matches Paul and Elder [1].
- *Proposal.* In `SKILL.md:43` replace "and ask "Is that right?"" with "and ask what you got wrong or left out (for example "What did I get wrong?"), not a bare yes/no". Also add: "Restate first in their words; strengthen only by making explicit what they implied, never by adding parts they did not say."

**F9 (medium): add a guard against verdict flips under pushback.**

- *Evidence.* Sycophancy is common and grows under sustained multi-turn pressure [35][36].
- *Proposal.* Add after `SKILL.md:99`: "If the user objects to the verdict, change it only if they add a substantive answer that meets the condition for the other verdict. Disappointment or insistence is not that answer; say so kindly and keep the verdict."

**F10 (low): say where advisor drift begins.**

- *Evidence.* Padesky allows drawing attention to relevant information outside the user's focus [6]. Telling solutions early is the documented failure [38]. The counterexample tactic (`SKILL.md:61`) requires the assistant to supply a case.
- *Proposal.* Extend `SKILL.md:108`: "...Before Step 3, ask about the user's reasoning, not your alternative. Offering a concrete case to *test* their idea is fine; offering a different plan to *replace* it is not."

**F11 (low): fix the expert-lens attributions.**

- *Evidence.* The lines in `question-bank.md:51-57` are paraphrases inside quotation marks after surnames. They were not checked against sources [unverified]. "Beck" collides with Aaron T. Beck, the CBT figure behind Socratic questioning in therapy (§2.2).
- *Proposal.* Change the intro line to "**Expert-style lens**, a question in the spirit of (not a quote from):". Use full names (Peter Drucker, Clayton Christensen, Nassim Taleb, Michael Nygard, Rich Hickey, Kent Beck). Drop the quotation marks, or add "(paraphrase)".

**F12 (low): treat three as a floor, not a ceiling.**

- *Evidence.* Osborn: "the more ideas the better" [11].
- *Proposal.* After the first sentence at `SKILL.md:79` add: "When they stop, ask once "Any more, even odd ones?" before moving on."

**F13 (low): shorten an early-stopped brief on a phone.**

- *Evidence.* `brief-template.md:3` keeps every empty section, and spec §1 targets mobile apps.
- *Proposal.* In `brief-template.md:3` replace the last sentence with: "If several sections are empty, list them on one line ("None: parking lot, criteria, options") so the reader still sees they were considered."

**F14 (medium): resolve the Codex `default_prompt` name.**

- *Evidence.* P3: `$dia-<x>` did not resolve for the plugin route; `$dia:dia-<x>` did. `default_prompt` resolution is untested (`docs/probes.md`).
- *Proposal.* This is a spec decision (§7.3 fixes the format), so it is not a skill-text change. Run P4 with this sidecar. If `$dia-brainstorm` fails there, change the spec template to `Use $dia:dia-brainstorm to …`, or to a natural-language prompt.

**F15 (low): add brainstorm-specific probes.**

- *Evidence.* P8 had no brainstorm run, and P2 is open (§6.2).
- *Proposal.* Add three probes to `docs/probes.md`:
  - a three-turn tool-less run (pass: no fact asked of the user that they cannot know; the brief is built from user answers; no tool attempted);
  - a stop-signal run in Korean (pass: Step 5 immediately);
  - a verdict-pushback run (pass: the verdict holds unless new substance arrives).

## 8. Open questions for the owner

- **Q1. Title.** Keep "Socratic Brainstorm" as the H1 (`SKILL.md:12`), or move "Socratic" into a subtitle so that the only claim is "modern Socratic questioning"? (F1)
- **Q2. Order of criteria and options.** Siebert and Keeney [29] favor eliciting criteria before generating options; Osborn [11] favors deferring evaluation. Should the skill ask "what matters most?" at the end of Step 2 and reuse the answer in Steps 3 and 4, or keep the current order and adopt only F6?
- **Q3. The cap.** Is the cap of 3 assistant options meant as an attribution and anchoring limit, or a phone-length limit? If the user says "more", should the cap lift (as Rule 5 lifts the probe budget), or hold?
- **Q4. Weights in stress mode.** When `stress` mode concerns money or an irreversible choice, should Step 4 offer an optional weighted pass (scores 1-5 against weighted criteria [30]), or stay verbal on purpose?
- **Q5. Versioning.** Do F2-F9 change "behavior" in the sense of spec §5.3? If so, they need a skill `metadata.version` bump (1.1.0) and a plugin version bump (spec §12.1), and P7 should be re-run against the `old` arm.
- **Q6. Primary text.** Should someone check Paul (1990) directly, so that `metadata` or a reference note can cite the six categories from the primary text rather than from course handouts and essays [2][4]?

## Sources

[1] https://www.criticalthinking.org/TGS_files/SocraticQuestioning2006.pdf — Paul & Elder (2006), The Thinker's Guide to the Art of Socratic Questioning (excerpt)
[2] https://podnetwork.org/content/uploads/V10-N3-Thoms.pdf — Thoms, Critical Thinking Requires Critical Questioning (POD Essays on Teaching Excellence; reports Paul 1990 taxonomy)
[3] https://public.websites.umich.edu/~scps/html/probsolv/strategy/cthinking.htm — U. Michigan, 9 types of Socratic Questions (after R.W. Paul)
[4] https://www.eoas.ubc.ca/courses/atsc201/A201Home/Critical_thinking_and_Socratic_Questions.pdf — UBC ATSC 201, Critical thinking and Socratic Questions (Paul's six types)
[5] https://aclanthology.org/2023.eacl-main.12.pdf — Ang, Gollapalli & Ng (2023), Socratic Question Generation, EACL
[6] https://padesky.com/wp-content/uploads/2012/11/socquest.pdf — Padesky (1993), Socratic Questioning: Changing Minds or Guiding Discovery?
[7] https://www.tccparatodos.com/_files/ugd/2dfb33_39bdbfaccf2743f58e1800a45a10dbda.pdf — Clark & Egan (2015), The Socratic Method in CBT: A Narrative Review
[8] https://pmc.ncbi.nlm.nih.gov/articles/PMC4449800 — Braun, Strunk, Sasso & Cooper (2015), Therapist Use of Socratic Questioning Predicts Symptom Change
[9] https://plato.stanford.edu/entries/socrates — Stanford Encyclopedia of Philosophy, Socrates
[10] http://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.01.0172%3Atext%3DTheaet.%3Apage%3D150 — Plato, Theaetetus 150 (Fowler tr., Perseus)
[11] https://www.uni-muenster.de/imperia/md/content/psyifp/aeechterhoff/wintersemester2011-12/seminarthemenfelderdersozialpsychologie/08_diehl_stoebe_productivityloss-brainstorming_jpsp1987.pdf — Diehl & Stroebe (1987), Productivity Loss in Brainstorming Groups, JPSP
[12] https://www.tandfonline.com/doi/abs/10.1207/s15324834basp1201_1 — Mullen, Johnson & Salas (1991), Productivity Loss in Brainstorming Groups: A Meta-Analytic Integration
[13] https://pmc.ncbi.nlm.nih.gov/articles/PMC4909789 — McMillan, King & Tully (2016), How to use the nominal group and Delphi techniques
[14] https://dictionary.apa.org/structure-of-intellect-model — APA Dictionary of Psychology, structure-of-intellect model (Guilford)
[15] https://onlinelibrary.wiley.com/doi/10.1002/acp.1699 — Kohn & Smith (2011), Collaborative fixation: Effects of others' ideas on brainstorming
[16] https://cecas.clemson.edu/cedar/wp-content/uploads/2016/07/9-JanssonAndSmith1991.pdf — Jansson & Smith (1991), Design fixation, Design Studies
[17] https://arxiv.org/abs/2403.11164 — Wadinambiarachchi et al. (2024), The Effects of Generative AI on Design Fixation and Divergent Thinking, CHI
[18] https://arxiv.org/html/2409.04109 — Si, Yang & Hashimoto (2024), Can LLMs Generate Novel Research Ideas?
[19] https://pmc.ncbi.nlm.nih.gov/articles/PMC11244532 — Doshi & Hauser (2024), Generative AI enhances individual creativity but reduces collective diversity, Science Advances
[20] https://arxiv.org/abs/2402.01536 — Anderson, Shah & Kreminski (2024), Homogenization Effects of LLMs on Human Creative Ideation
[21] https://arxiv.org/abs/2402.01727 — Meincke, Mollick & Terwiesch (2024), Prompting Diverse Ideas: Increasing AI Idea Variance
[22] https://arxiv.org/abs/2401.13481 — Ashkinaze et al. (2024/2025), How AI Ideas Affect the Creativity, Diversity, and Evolution of Human Ideas
[23] https://arxiv.org/abs/2410.03703 — Kumar et al. (2025), Human Creativity in the Age of LLMs, CHI
[24] https://link.springer.com/article/10.1007/s10648-026-10118-7 — Think First, ChatGPT Later (Educational Psychology Review)
[25] https://arxiv.org/abs/2502.06197 — Timing Matters: How Using LLMs at Different Timings Influences Ideation (2025)
[26] http://arxiv.org/abs/2510.23324 — Maier, Schneider & Feuerriegel (2025), Human-Led and Model-Led Interaction in Human-AI Co-Creation
[27] https://www.nature.com/articles/s41562-024-01953-1 — Lee & Chung (2024), An empirical investigation of the impact of ChatGPT on creativity, Nature Human Behaviour
[28] https://www.scheller.gatech.edu/directory/research/marketing/bond/pdf/bond_carlson_keeney-man-sci-2008.pdf — Bond, Carlson & Keeney (2008), Generating Objectives, Management Science
[29] https://pubsonline.informs.org/doi/abs/10.1287/opre.2015.1411 — Siebert & Keeney (2015), Creating More and Better Alternatives for Decisions Using Objectives, Operations Research
[30] https://assets.publishing.service.gov.uk/media/5a790545e5274a2acd18b975/1132618.pdf — DCLG (2009), Multi-criteria analysis: a manual
[31] https://scheibehenne.com/ScheibehenneGreifenederTodd2010.pdf — Scheibehenne, Greifeneder & Todd (2010), Can There Ever Be Too Many Options? (choice overload meta-analysis)
[32] https://pages.ucsd.edu/~mckenzie/TverskyKahneman1974Science.pdf — Tversky & Kahneman (1974), Judgment under Uncertainty: Heuristics and Biases
[33] https://hbr.org/2007/09/performing-a-project-premortem — Klein (2007), Performing a Project Premortem, HBR
[34] https://www.pewresearch.org/writing-survey-questions — Pew Research Center, Writing Survey Questions
[35] https://arxiv.org/abs/2310.13548 — Sharma et al. (2023), Towards Understanding Sycophancy in Language Models
[36] https://arxiv.org/abs/2505.23840 — Hong et al. (2025), Measuring Sycophancy of Language Models in Multi-turn Dialogues (SYCON Bench)
[37] https://arxiv.org/abs/2505.06120 — Laban et al. (2025), LLMs Get Lost In Multi-Turn Conversation
[38] https://arxiv.org/abs/2305.14536 — Macina et al. (2023), MathDial
[39] https://arxiv.org/html/2310.11589 — Li, Tamkin, Goodman & Andreas (2023/2025), Eliciting Human Preferences with Language Models (GATE)
[40] https://support.claude.com/en/articles/12512180 — Claude Help Center, Use Skills in Claude
[41] https://learn.chatgpt.com/docs/build-skills — ChatGPT Learn, Build skills
