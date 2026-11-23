# Spec sections retired at 5.0.0 (record)

**This is a record, not instructions.** These are sections of `docs/spec.md` as they stood at plugin `dia` 5.0.0 (2026-11-23), moved here because they restated the skills' behaviour or described one-time steps and acceptance of 1.0.0, and had drifted from the skill files. What each skill does is in its `skills/<skill>/SKILL.md`; the decisions are in `docs/spec.md` §3.

## Former status line

| | |
|---|---|
| Status | Approved by the owner on 2026-10-20; pre-release 0.1.0, accepted (§12.3) and released as 1.0.0 on 2026-10-20; 1.1.0 renames dia-intent to dia-confirm (D30), and 1.6.0 renames it back (D42). 1.5.0 (D39, D40) was built on a branch and never released; its changes ship in 1.6.0 (owner, 2026-10-28). 1.7.0 extends dia-intent's goal step (D45); 1.8.0 adds its outcome hypothesis (D46), resolves the D43 rewrite's open proposals (D47) and closes the dia-adjudicate re-test (D48); 1.9.0 settles the decisions 1.8.0 left (D49); 1.10.2 applies the first stage of the 2026-10-29 audit (D50; 1.10.0 and 1.10.1 were built on the branch and never released). 1.11.0 applies its second stage and dia-instruct 1.1.0 (D51). 1.11.1 settles the dia-conjecture items left in D50 (D52). 1.13.0 adds dia-techne (D55). 2.0.0 makes every skill router-only and renames five (D56); 2.1.0 limits dia-router to numbers, names and description-based requests (D57); 2.2.0 trims nine bodies (D58). 2.3.0 adds dia-regula's Writing step 4 (D59). Probe results: `docs/probes.md` |

## Former §6 L6, L7 and §7.2 description convention

- L6. Replies follow the user's language. Until 2.11.0 every skill stated this (dia-intent since D20). Since 2.12.0 (D71) no SKILL.md states it except dia-reductio 4.0.0 ("Write in the user's language", D118), because current models write in the user's language without being told (probes Part AJ); the bodies keep only the language rules that are not that default: quotations stay in their original language, dia-negative uses plain words, logic labels may stay as they are, dia-regula sets the language of the text it writes or edits, dia-techne writes the rewritten prompt in the source prompt's language, and dia-emend's revision keeps the draft's language. All six output templates (dia-reductio, dia-warrant, dia-counterplan, dia-negative, dia-elenchus, dia-quaestio's brief) keep their one sentence on translating headings and labels, by decision (D71): a template printed in English pulls the headings to English, and without the sentence dia-reductio printed English headings in 3 of 5 runs (probes Part AJ (c)).
- L7. Removing Hangul from descriptions (5.4, 5.5, 5.6) may reduce routing accuracy for Korean prompts. P7 measures this. If routing drops below the baseline, fix the English trigger wording. Do not reintroduce Hangul.
- Description convention (D37): method label (the name a user would type, plus at most one honest qualifier) → what it does, in at most two sentences, only behaviour that separates it from its siblings → "Use when …, or the same in any language." → one "Not for …" sentence naming the sibling for each border. Explicit-only skills: what it does → "Use only when …" → the gate negation → "Not for …". Dates, rule and chapter numbers, lineage, template fields and flags stay in the body. State each border once, on the side probes show over-pulling, unless a probe shows both halves are needed (brainstorm/elenchus, Part B). Target at most 900 characters, so a probe-driven fix still fits. When a description is edited, reread it whole and delete what the new phrase makes redundant; cite the probe cell in the decision row.

## 5. Skills

Since 2.0.0 (D56) every skill below starts only on its name as the first word, an explicit invocation by name, or a choice by dia-router; Invocation lines that mention natural language describe 1.x. Five sections carry their 2.0.0 names.

The seven rebuilt skills (5.1–5.7) keep their reference behavior unless this section or D19–D35 say otherwise. The three skills added in 1.3.0 (5.8–5.10), dia-menu (5.11, 1.4.0), dia-adjudicate (5.12, 1.5.0), dia-instruct (5.13, 1.6.0) and dia-techne (5.14, 1.13.0) have no reference; design notes for 5.8–5.10 are in `docs/research/candidates/design/`, dia-menu's design is D38 and §5.11, dia-adjudicate's research is `docs/research/dia-adjudicate.md`, dia-instruct's record is `docs/writing-for-models/`, and dia-techne's is `docs/research/dia-techne.md`. For every rebuilt skill, the rebuild:

- renames the skill;
- updates cross-references so that each description names the new skill names;
- removes Hangul outside `references/ko/` (§6);
- adds `agents/openai.yaml` (§7.3);
- sets `metadata.version` to `1.0.0` and records `metadata.lineage` as `<old name> <old version>`.

### 5.1 dia-skopos (from confirm-intent; `dia-confirm` from 1.1.0 to 1.4.0, D30, D42; `dia-intent` until 2.0.0, D56)

- Purpose: before work starts, show the user what they asked for as the assistant reads it and the result it is for, and let them choose which of the two is the request: the thing asked for, or the result. Then wait for their word.
- Behavior (dia-skopos 4.0.0, D114): the body is written from that purpose, about 740 words. The review quotes the request and says what the reading adds to, narrows or leaves out of it; reads a result in when none is stated, because one read too low is approved unnoticed (a result is what should come out differently in the user's work, outside the thing made, and a decision reached, a thing the user can trust and a thing the user is now able to do count as things made); keeps what was found apart from what is assumed; lists what only the user can decide, each with the answer the assistant would give; and ends on the choice between two requests, "as asked" (the thing named, made as its best practitioner would make it) and "for the result" (the result written as one sentence the user could have sent, with a line or two on what of the thing asked for it would keep, change or drop, and not designed further). It asks for the result in the user's own sentence, because a result they state carries what the assistant cannot know; a bare proceed takes the review's sentence, and "as asked" keeps to the thing named. Nothing of the task is done before a clear proceed, and a proceed with corrections approves the request so corrected. On a proceed the approved request goes to dia-techne where that skill is available, with what the user said in their own words and without the answers the review only suggested; nothing about how the work is done is in this body (owner, 2026-11-19). When the work is done, one line says which request it was done for and what has shown the result so far.
- Since 4.2.0 (D116): the review does not print the request back; it says what it would make and what its reading adds to, narrows or leaves out, quoting only the words a reading turns on, and names a result the user stated as theirs with what the reading adds to or narrows in it.
- Since 4.1.0 (D115): for "as asked" the review says only what would be sent or spent and any step that cannot be undone, and no longer what stays when the work is done; for "for the result" it says that the thing asked for becomes one way to the result among others and may be changed or replaced, and neither designs that work nor says what form it will take; the line that closes finished work is dia-techne's.
- No longer in the body (D114, each approved by the owner): the four labelled lines of D72 and D80; the four forms of the outcome and the first effect of D88; the split of D45 between the deliverable's criteria and those of a stated outcome; the ordered cases of D84 for a candidate decision; the paragraph on decisions that depend on each other; the cases for a correction that conflicts with inspected evidence; and the detail of a safe isolated probe, which is now one sentence.
- Invocation: first word or explicit name. The description says "Use only when the message starts with dia-skopos, when the skill is invoked by name, or when dia-router selects it". `allow_implicit_invocation: true` since 1.2.0 (D33), so the first word works on Codex (probed, Part M). The body has no Invocation section; the description gates the skill.
- References: none at present. `references/ko/` is optional (§6).

### 5.2 dia-elenchus (from socratic-elenchus 1.3.1)

- Purpose: Plato's elenchus. Ask "what is X?", collect agreed premises one question at a time, show contradictions, and treat each revision as the user's new idea. It usually ends in aporia and never gives advice.
- Behavior: the reference, amended by D19–D34.
- Cross-reference: "use socratic-brainstorm" becomes "use dia-brainstorm".
- Invocation: natural language or name, as on Claude. `allow_implicit_invocation: true` since 1.2.0 (D33; the reference had false).
- References carried over: `elenchus-patterns.md` and `record-template.md`; `theory.md` added (D24) for the dialogue loci and sources, read only when the user asks about the sources or the method.
- Template folded in (dia-elenchus 3.1.0, D110): there is no record template; Step 6 names the record's lead line, its heading "Dialogue record:", its Result line and its eight sections with what each holds.

### 5.3 dia-quaestio (from socratic-brainstorm 3.3.1; `dia-brainstorm` until 2.0.0, D56)

- Purpose: modern Socratic questioning, one question at a time. The user lists options, the skill adds up to three labeled ones, and the user converges by criteria. It ends with a verdict and a brief, and never implements anything.
- Behavior: the reference, amended by D19–D35.
- Cross-reference: points to dia-elenchus, to dia-counterplan (description and Step 0) and to dia-conjecture and dia-warrant (Step 0 only) (D35).
- Invocation: natural language or name, as on Claude. `allow_implicit_invocation: true` since 1.2.0 (D33; the reference had false).
- References carried over: `question-bank.md` and `brief-template.md`.
- Template folded in (dia-quaestio 3.1.0, D110): there is no brief template; Step 5 names the brief's lead line, its heading "Brief:", its Verdict line and its sections, each under its own header.

### 5.4 dia-reductio (from reductio)

- Purpose: reductio ad absurdum: hold a position against its own commitments and see whether all of them can be true together, for what that brings to the surface (a commitment nobody had stated, commitments that cannot stand together, what each way out would cost what the position is for); then the assistant gives its own judgment.
- Behavior (dia-reductio 4.0.0, plugin 5.0.0, D118): the body is written from that purpose, about 1,240 words against 2,830. The first line names the target (the user's position, a text by someone else, or the assistant's own earlier answer when the user points at it), and one line the thesis as read and what it is for; the strongest reasonable reading is tested. Each commitment carries its source (the target, quoted; logic or arithmetic; or the assistant); an added premise the position's own argument needs is the centre of the work, and a contradiction through any other added premise holds only as far as that premise does. The search starts with what the purpose leans on most, as since D93. A contradiction stays strict (a statement and its exact denial, each step licensed by logic, a stated definition or a computation, one sense per term) and is settled by a tool where one is available; none found shows neither consistency nor truth. The reply leads with the judgment, asks what only the user holds all at once with what each answer decides, then gives the contradiction, the numbered chain with each step's ground and what came to the surface, every fact with how it is known. A named defect is given way to as far as it reaches; repetition moves nothing; a dropped premise or a term now meant otherwise is a changed position, tested again.
- Changed in plugin 5.0.0 (D118): each way out (a commitment given up, or the position narrowed just far enough) is tested by the same means, and the assistant says what each costs the purpose and which it would take and why, handing back only what is the user's alone; until then it recommended one option and left the decision to the user (Rule 7). The ways out wait for answers only the user holds, where Rule 9 had the whole chain in one response.
- No longer in the body (D118): the `--target=user|claude|text|all` parameter (the target is read and named in the first line, and there is no `all`); the numbered hard rules; the labels [T], [L] and [A] and a named rule on each line; the graded strength of the contradiction and the fixed result values; the headings of D109; the two Thesis lines of D82 and the What T is for line of D93, now one line; the record.
- Cross-references: none. Since D56 the description names only how the skill is invoked (by its name or through dia-router), so its earlier pointers (dia-negative; since D35 dia-warrant and dia-conjecture; dia-elenchus until D37) and its Hangul trigger terms are gone. The body has no pointers.
- Invocation: implicit allowed, which is the Codex default; the reference had no `openai.yaml`.
- References carried over: `theory.md`; `output-template.md` until dia-reductio 3.1.0 (D109).
- Caller-fixed output format (D68, changed in 5.0.0, D118): when another agent or a script fixes the format and no user will reply, each contradiction goes in the caller's items with its chain as evidence, and the judgment and what came to the surface in a last item labelled as the method's result, which says at its start where the format forces a value the method does not give; there is no record.

### 5.5 dia-negative (from negative-dialectics)

- Purpose: internal critique (narrower than Adorno's immanent critique), adapted from Adorno, in one pass. The skill:
  - finds the target's own standard;
  - reports strict gaps with particular cases and "what escapes";
  - infers the operative purpose with a falsifier;
  - gives options without a forced synthesis, recommends one, and ends with a record.
- Parameter: `--target=user|claude|text|all`, unchanged.
- Required change: Hangul in the description (one line) and in `references/theory.md` (one line) is removed or moved to `references/ko/`. The Korean routing probe applies here too (P7).
- Cross-references: point to dia-reductio and dia-elenchus.
- Invocation: implicit allowed.
- References carried over: `theory.md` and `output-template.md`.
- Caller-fixed output format (D68): when another agent or a script fixes the format and no user will reply, each strict gap goes in the caller's items with its proof as evidence, a closing item labelled as the method's result holds the record, and severity and fix fields say the method gives none.
- Template folded in and the result up front (dia-negative 3.1.0, D110): there is no output template; the body names the headings (a Target line, then Claim, Result, Its own standard, Findings, Function and purpose, Options, Recommendation and Record). Result stands right after Claim: the status with the number of firm and conditional findings, then each firm finding in a few words, the conditional ones when none is firm, or the particulars C held against when there is no finding.
- Status (dia-negative 3.1.1, D111): open when at least one finding, firm or conditional, is listed; holding against the tested particulars when none is.

### 5.6 dia-emend (from self-refine; `dia-refine` until 2.0.0, D56)

- Purpose: a single review pass over the previous output or a named draft. It checks in this order: factual errors, logical leaps, missing requirements, needless repetition. It fixes only defects whose basis was confirmed and returns one integrated revision.
- Required changes:
  - Translate the whole skill to English. The reference is written in Korean (38 lines contain Hangul). The translation keeps every rule and its reason: candidate listing without a severity filter, verification limited to what tools allow, no subagent self-checks, the output layout ①–④, the "final only" mode, and the safeguards.
  - Invocation:
    - Explicit: a message whose first token is `dia-refine`. Text after it is the review criteria, for example `dia-refine — check the numbers`. `/dia:dia-refine`, `$dia:dia-refine`, `$dia-refine` (copied folder only) and `@dia-refine` also work.
    - Natural language, in English triggers plus "or the same in any language": for example "review your previous answer as a draft", "fix factual errors and logical leaps", "give me only the improved final version".
    - A passing mention of dia-refine in the middle of a sentence is not an invocation.
    - Since D24 the natural-language triggers and the passing-mention rule live in the description only; the body keeps the explicit forms.
    - Multi-round requests belong to dia-ratchet (dia-iterate until 1.4.0, D39).
  - The pointer to recursive-refine becomes a pointer to dia-ratchet.
  - Since D39 the description leads with its evidence basis: a tool, the user's material or its own re-derivation of the logic or a calculation.
- Requirements line (dia-emend 2.4.0, D80): step 1's checklist is no longer kept unprinted. The defect list always opens with a **Requirements, as read** line, naming each point where the reading goes beyond what the user's words and the draft itself settle and that changes what is fixed or kept, or "same as stated"; a "final version only" reply ends with that line only when it names a point.
- Core edition (dia-emend 3.0.0, D90, D91): the body is rewritten from what the user and the situation require, the method, the limits no model outgrows and the aim, 1,121 words against 1,798. The aim: step 1 states what the draft is for (given when the user stated or approved it, read in otherwise and then never a basis for a change), step 2 starts with what that purpose depends on most and examines the passages that look right as well, a stated purpose's gap that only the user can fill gets a placeholder, and a closing line says whether the revision can now do what it is for and what still stands in the way. The sentences guarding a model's habits, the citations and the worked example are gone; the order of the four checks, the bases, the four-part list and the two output forms are as before.
- A gap that only a read-in purpose shows (dia-emend 3.0.1, D106): an audience or a tone the user gave is their instruction, and a passage that does not meet it is changed on that basis; what the draft lacks only by the purpose the assistant read in gets no placeholder, and is named under ② as resting on that purpose and in the closing line, or in the one line of a "final version only" reply.
- Tool-less surfaces: the behavior is already specified. Unchecked items are marked unverified and left as drafted.
- References: none at present.

### 5.7 dia-ratchet (from recursive-refine, output mode; `dia-iterate` until 1.4.0, D39)

- Purpose: repeated review rounds, each gated by external verification. Each round names defects, assigns an external verification method, verifies, fixes only confirmed defects, locks verified items and logs the round. The loop stops on regression, zero defects, verification exhausted, fixed point, or the round cap (`--max N`, default 3).
- Required changes:
  - Remove skill mode entirely: the "Skill mode" sections, `references/skill-loop.md`, and every mention of `cp -r`, `diff -u`, subagents, `evals/` and `package_skill`. Targets are the last output, a named draft, or a file the surface can read.
  - Invocation: first word or explicit name only. Activate only when the message starts with `dia-ratchet` or the skill is invoked explicitly by name. If the marker is absent but the skill looks right, ask in one line for a message starting with `dia-ratchet`, or an explicit invocation of the skill by name, and stop. Explicit `/dia:dia-ratchet`, `$dia:dia-ratchet`, `$dia-ratchet` and `@dia-ratchet` also count. Until 1.1.1 `allow_implicit_invocation: false` hid it from the model on Codex and ChatGPT, so the first word could not work there; since 1.2.0 it is `true` (D33) and the description and the body's marker rule do the gating.
  - Generalize tool names in `verification-sources.md`. "Context7 doc lookup" becomes "an official-documentation lookup tool (for example Context7) or a fetch of official docs".
  - Add an explicit tool-less rule: when no search, fetch or code tool is available, the only external evidence is the user's instructions and material the user supplies. Most defects are therefore unverifiable, and the loop usually stops after round 1 with the "verification exhausted" list. This is expected behavior, not a failure.
  - Keep the content-filter guardrails: a change-list output by default, no source quotations except a misquotation corrected in one sentence (D23), one retry, then change the output shape.
- Pointers: single-pass requests go to dia-refine.
- Requirements line and layout (dia-ratchet 2.6.0, D82): the output opens with a **Requirements, as read** line, as in dia-emend 2.4.0 (each point the reading goes beyond the user's words and the target, or "same as stated"; in a "final version only" output it goes at the end, only when it names a point). Step 4, the forms of output and the guardrail on what the user tells you are written in the layout of dia-regula 2.7.0, and any request about form other than full text or final version only gets the change list.
- References carried over: `verification-sources.md`.

### 5.8 dia-warrant (new in 1.3.0, D35)

- Purpose: hold a conclusion that is only probable against the step that carries it: find the rule, usually unsaid, that takes the reasons to the conclusion, ask whether this is a case where it holds, and judge how far the conclusion can be relied on for what it has to carry. Toulmin's warrant and qualifier and Walton's critical questions stay, in plain words.
- Behavior (dia-warrant 4.0.0, plugin 5.0.0, D118): the body is written from that purpose, about 1,580 words against 2,860; the target, the reply and the exchange are as in 5.4. One line gives the conclusion at its stated strength and what it is for. Each step is taken apart, the one the purpose leans on most first; its rule is quoted, or supplied as the least general rule in the arguer's terms and marked as the assistant's reading. The questions are those the kind of step is open to; each is answered by the argument's words, the material, the user or a cited source, or stays open, and the assistant's recall closes nothing. The conclusion's strength is set beside its rule. An arguer who disowns a supplied rule removes it.
- Changed in plugin 5.0.0 (D118): the assistant judges. It keeps "these reasons do not carry it" apart from "the evidence goes against it" and says the second when evidence does, names the weakest step and why it matters (or that none gave way, which is support and not proof), says whether it would act on the conclusion, gives an answer the user's figures or the material hold, and makes the thing to act on. Until then the audit did not say whether the conclusion was true and gave only the kind of answer that would strengthen a link (Rules 1 and 4). A user who asks to be questioned is still asked one thing a message.
- No longer in the body (D118): the six Toulmin slots as a layout with stated and reconstructed marks, the second warrant W2, and slot tags and statuses on the questions; the numbered hard rules; the fixed results (weakest link by slot, no weak link found, stopped); the reply's five numbered parts and its last line; ask mode by name (`--mode=ask`) and its endings.
- Borders (changed in 5.0.0, D118): until then each border named its sibling (dia-reductio, dia-refine, dia-conjecture, dia-counterplan, dia-brainstorm; D35); now a request for a strict contradiction, or for counterexamples to a claim about every case, is said in a line to be another method's work, and the body names no other skill.
- Invocation: natural language or name. `allow_implicit_invocation: true`.
- Design note: `docs/research/candidates/design/dia-warrant.md`.
- Caller-fixed output format (D68, changed in 5.0.0, D118): with no user to reply, each question the assistant would have asked goes in as open, with what its answer would decide; a caller's fixed format takes the same content, the judgment and what came to the surface in a last item labelled as the method's result, which says at its start where the format forces a value the method does not give.
- First rewritten from its purpose in dia-warrant 3.1.0 (D108), without an output template.

### 5.9 dia-conjecture (new in 1.3.0, D35)

- Purpose: Lakatos's proofs and refutations on a claim about every case: find the argument for it, bring the cases that press it hardest, and where one counts, build the condition it reveals into the claim instead of dropping the claim or listing an exception; then the assistant judges whether "every" stands, what can be asserted in its place, and what becomes of what rested on it.
- Behavior (dia-conjecture 4.0.0, plugin 5.0.0, D118): the body is written from that purpose, about 1,440 words against 3,790; the target, the reply and the exchange are as in 5.4. The claim is stated as "every A is B" in its source's key words, with what it is for; wording of the assistant's that the user corrects back to their own is no change of it (D85's restoring correction, in prose). The argument is set out in numbered steps, supplied ones marked; for a claim about the world the assistant says before the cases what would count against it (Popper's criterion, no longer asked of the user). Cases come most likely first, from the source's own material, each with its check condition by condition and what it breaks: the claim, a step, or what is built on it. A counting case makes the claim as it stands fall; the repair builds the broken or hidden step into the claim as the weakest condition that shuts the case out, says what it no longer covers, and is tested again; an exception listed or a term redefined is named as no repair. The moves of Rules 1–4 stay, without their numbers; section 6a's deeper proof is not used (a case that breaks only a step calls for a better step).
- Changed in plugin 5.0.0 (D118): the assistant says whether a case counts wherever its check settles it, chooses the repair, and judges whether the claim stands, with what was tried and not and what becomes of what it was for; until then the user ruled on each case and picked the repair (Rules 4 and 7). Several cases may come in one reply, where Rule 1 had one case a message, and there is no three-round offer to stop. The description's "user-directed repairs" became "repairs".
- No longer in the body (D118): the classification of the user's ruling (invalid, concept-stretching, monster-barring, disputed); the numbered hard rules and Steps 0–6; the record with its result values, its rounds and the Claim, as stated and Claim, as read lines of D85.
- Borders (changed in 5.0.0, D118): until then the body sent plans, policies, decisions and ideas, the meaning of a word, Q and not-Q, probable claims and a claim against its own standard to named siblings (D35); now a claim put as "usually" or "most" is said in a line to be another method's work, and the body names no other skill.
- Invocation: natural language or name. `allow_implicit_invocation: true`.
- Design note: `docs/research/candidates/design/dia-conjecture.md`.

### 5.10 dia-counterplan (new in 1.3.0, D35)

- Purpose: dialectical inquiry after Mason (1969) on a plan, decision or recommendation: find the assumptions the decision turns on, give each a contrary that could well be true, build the course of action those contraries call for on the same facts, and then the assistant judges which course it would take as things stand and what would change it.
- Behavior (dia-counterplan 4.0.0, plugin 5.0.0, D118): the body is written from that purpose, about 1,610 words against 3,150; the target, the reply and the exchange are as in 5.4. The assumptions, quoted or marked as supplied, are kept when their opposite would make a different course right (SAST test), seldom more than five. Each contrary is a specific state of affairs, the assistant's choice, coherent with the others and with the shared facts. Each pair gets the observation that would show which is true, and is settled where the material or the user settles it, with the plan's own figures worked under the contrary. The counterplan is built from the contraries still standing, as a competent advocate would, at the plan's level of detail; where they no longer call for another course none is built. The reply says one assistant wrote both sides and that this is no independent test.
- Changed in plugin 5.0.0 (D118): the assistant gives a verdict: pair by pair which assumption the evidence supports or that the pair is open, which course it would take (the plan, the counterplan, or one built from the assumptions surviving on each side) and why, and what would have to be seen, and by when, for the other course to be right. Until then it gave none and the result was the set of assumptions the user held (Rule 5, Step 7). With no user to reply, in place of D64's one-response run, every pair the material does not settle is open and the counterplan is built from all of them and given whole.
- No longer in the body (D118): the `--target` parameter; the numbered hard rules; Steps 1–8, the headings of D109 and Step 7's question; the record and its result values.
- Borders (changed in 5.0.0, D118): until then questioning the user's idea went to dia-brainstorm, counterexamples to a universal claim to dia-conjecture, an argument's support to dia-warrant and a plan against its own standard to dia-negative; now a question whether one claim is true, with no course of action in it, is said in a line not to be this method's work, and the body names no other skill.
- Invocation: natural language or name. `allow_implicit_invocation: true`.
- Design note: `docs/research/candidates/design/dia-counterplan.md`.
- Caller-fixed output format (D68, changed in 5.0.0, D118): when a caller fixes a format of findings and no user will reply, the whole output goes in one item labelled as the method's result and not as a finding, which says at its start where the format forces a value the method does not give; there is no record.

### 5.11 dia-router (new in 1.4.0, D38; `dia-menu` until 2.0.0, D56)

- Purpose: a short entry point. `dia` alone shows a fixed numbered menu of the skills (ten in 1.4.0; eleven from 1.5.0, with dia-adjudicate as 11, D40; twelve from 1.6.0, with dia-instruct as 12, D41; thirteen from 1.13.0, with dia-techne as 13, D55). Since 2.1.0 (D57) `dia <n>` or `dia <name>` (the full skill name, with or without `dia-`, in any letter case) runs that skill, unless the number or word plainly belongs to the request's sentence (`3 reasons …`, `dia 1 thing …`, `negative feedback …`); anything else after `dia` (a plain request, a shortened name, a former name) is a request: the router picks the skill whose description fits, with two border sentences the descriptions do not settle (Socratic dialogue goes to dia-elenchus even on a plan; a deductive argument's validity or missing step goes to dia-reductio), names it in one line and runs it, asks when two fit about equally, and answers without a dia skill when none fits. A request for several dia skills, or for reviewers that use dia skills, gets one of the four review skills per reviewer, each started by its skill name, with each result passed on unchanged (D67). The 1.4.0–2.0.0 forms (prefixes, then three-letter codes, and borders written out in the router per skill, D38–D56) are in the git history of this section.
- Since 2.13.0 (D72): the menu is not numbered, only a skill's full name (with or without `dia-`) picks a skill, and a number after `dia` is read as a request.
- Gates: dia-skopos, dia-ratchet, dia-adjudicate and dia-techne are never picked from a request; the router replies with the form to send. A pick by number or name is an explicit invocation by name for every skill, and those four run only on such a pick or their own name (D66).
- Hand-off: the chosen skill is loaded the way the host loads skills and followed in full; the menu table is not a substitute. If it cannot be loaded, the menu says so and gives `dia-<x> <request>`.
- Invocation: first word `dia` on its own, or the name. `allow_implicit_invocation: true`.

### 5.12 dia-adjudicate (new in 1.5.0, D40)

- Purpose: hold reports that others (people or models) wrote about a target against the source and against each other: rule on each point by the evidence, check what the target claims whether or not a report raised it, and then judge what the rulings leave of the target's conclusion and what has to be true of it once corrected. The assistant writes no report of its own, and one it wrote earlier is marked as that.
- Behavior (dia-adjudicate 4.0.0, plugin 5.0.0, D118): the body is written from that purpose, about 1,430 words against 3,360; the target, the reply and the exchange are as in 5.4. The target's checkable claims are listed before the reports are read closely. Each point is ruled on once, however many reports make it: it holds, holds in part, is overstated, is wrong, or cannot be verified; reports that disagree may each be right by their own measure, and the ruling says which measure the target's words commit it to. The order of checks stays (calculations, quotations and attributions, facts, a study's fit to the case, inference), and so do D85's three cases, in prose: overturning needs the source's own words read this session and quoted, or the recomputation shown; absence from the opened sources or from a tool's summary contradicts nothing; a claim about what a person or body holds is looked for in their other statements. Each point is weighed by its effect on the conclusion. The list for the user to check holds every overturn, every "cannot be verified" the conclusion depends on, and every ruling on a summary or on recall.
- Changed in plugin 5.0.0 (D118): the judgment says what the rulings leave of the conclusion, which report was right on which point and what none raised, and what the changed target must satisfy; where the user needs the wording itself the assistant writes it, marked as its own and unjudged, so the description no longer says "without rewriting the target". A second run is made only when a report is overturned on the assistant's reading of a source and a separate agent can be started; D86's four cases, among them asking the user for a second run in a separate chat, are gone, and the reply says whether one run or two was made.
- No longer in the body (D118): the Invocation section and its marker rule; the numbered hard rules and Steps 1–10; the Inputs section and its shuffled order; the named severities and the tables; errors in the reports, the consistency check and the decisive issue as steps; the T, as read line of D85 and the Output sections; any rule for a caller's fixed format (D68's least-claiming verdict, and Rule 1's fix stated as a condition since 2.11.0).
- Borders (changed in 5.0.0, D118): until then reviewing and fixing a draft yourself went to dia-refine, fixing through verified rounds to dia-ratchet, and an argument's support to dia-warrant; now the body names no other skill.
- Invocation: first word or explicit name only, as dia-ratchet; dia-menu selector 11. `allow_implicit_invocation: true`; the description gates it (the body's marker rule did as well until 5.0.0).
- Tool-less surfaces: only what the user supplies can be read as a source; a recomputation shown, worked by hand and said to be, can overturn; a ruling on recall overturns nothing, so most factual items stay "cannot be verified", with where the assistant looked and what would settle them.
- Research and trials: `docs/research/dia-adjudicate.md`.

### 5.13 dia-regula (new in 1.6.0, D41; `dia-instruct` until 2.0.0, D56)

- Purpose: check or write text a model reads and follows against four rules (each paragraph one expression holding its condition, limit and fallback; a scope word kept as narrow as meant; fewer instructions, each with its reason; one name per thing) and the structure they imply. A breach of a rule or structure item is a finding; a lead is advice, never a finding. A review-only request yields a report of breaches with location, quote and rule, and no change until the user picks.
- Borders: an answer or a draft for people, checked for factual errors and logical leaps, goes to dia-refine; ruling on reviews others wrote goes to dia-adjudicate.
- Invocation: natural language and by name; dia-menu row 12, and the menu may choose it for a request. `allow_implicit_invocation: true`.
- Tool-less surfaces: without a sub-agent, kept text is self-checked and the check is called not independent; without an eval, a meaning change stays only if it is reported as unmeasured and the user accepts it.
- Owner rulings after the pre-merge review (2026-10-28): replies to the user are in the user's language (the body stated this until 2.11.0; since 2.12.0, D71, it states only the next half), while text written or edited keeps its language or the one its rules set; a fix for a confirmed review finding is self-checked, with another sub-agent round only when the fix changes meaning; an edit that only adds or updates a fact or command in kept text (a path, a test command) is self-checked like single-use text; "a general-purpose sub-agent" and the CLAUDE.md trigger stay.
- Handoff (2.3.0, D59): a prompt the request asks for is returned in the reply; the model it is for starts only when the request also asks for that.
- Added reasons (dia-regula 2.3.0, D65): Writing step 1 counts a reason added to existing text as a meaning change, since a reason generalizes a rule to cases it does not name (Rule 3's basis).
- Sentence length (dia-regula 2.5.0, D73): Rule 1 no longer says that a sentence runs long rather than splitting; it asks for the condition, limit and fallback inside the paragraph of the result they gate, and a sentence or paragraph is never a breach merely for being long.
- A/B conditions and lists (dia-regula 2.5.0, D73): Writing step 1 says when a meaning change needs an A/B and points to Checking a change in `references/evidence.md` for the conditions that A/B must meet; the lead on numbered short sentences is gone, and the lead on numbering covers bullet items as well.
- Analogies (dia-regula 2.6.0, D75): the body no longer explains its rules by functional-programming analogies (total function, `if` without braces, type signature, alias, separate function, standard-library call); the rules themselves are unchanged.
- Many cases (dia-regula 2.7.0, D80): a Structure item writes a rule that sorts its input into more than two cases, or carries an exception inside an exception, as a lead sentence with a labelled sub-item per case, counted as one paragraph under Rule 1; Writing steps 1 to 3 are written that way.
- Readings in the output (dia-regula 2.8.0, D83): a By kind of text item has an instruction that tells the model to work out, beyond a person's words, what the work should achieve or meet, and whose output the person approves or acts on, show that reading every time on two labelled lines (as stated and as read), kept apart from text meant to be sent on, with a stated value when there is nothing to read in; a short form leaves them out only by a sentence of its own. Carrying out a request as worded is not such a reading.
- Its own readings (dia-regula 2.9.0, D84): Writing step 5 has a reply that carries text written or edited, step 3's revised version included, open with **Requirements, as stated** and **Requirements, as read**, kept apart from the text; a review alone has neither, and a request for the text alone leaves them out. The labels in the readings item are named for what is read.
- A file counts (dia-regula 2.10.0, D86): Writing step 5's two Requirements lines also open a reply that reports that text you wrote or edited went into a file, not only one that carries the text.
- Research: `docs/writing-for-models/` (session record, A/B on dia-adjudicate) and `docs/research/karpathy-regula-2026-11-08/` (a public coding skill rewritten under the rules, Codex A/B, review); evidence per part in `skills/dia-regula/references/evidence.md`.

### 5.14 dia-techne (new in 1.13.0, D55)

- Purpose: take a request to the outcome it serves: do it as the best practitioners of its field would, make what that outcome needs, and have the result checked by something other than the assistant.
- Behavior (dia-techne 4.0.0, D114): the body is written from that purpose, about 930 words. The outcome is read in when none is stated (not the deliverable, and not the deliverable done correctly), and an outcome the user stated or approved is taken as given; approved is what the user said or answered, and what a review only suggested stays open. The thing asked for is one way of reaching the outcome: it is set beside at least one other way, the ways are compared by the outcome's own measure (what each would yield, how soon, at what risk), the one that comes out best is taken, and the reply says what the comparison showed and what became of the thing asked for. With `--aim=request`, or after the user approved the thing "as asked", the thing asked for is the way, made as well as the outcome needs. The work asks what a top practitioner would do that the request does not ask for, what rawest material they would start from, which methods and tools they would use, and which technique from another field or which opposing view would change the result. It finishes the work instead of describing or offering it: where the answer turns on something only the user knows it is carried as far as it holds whatever they would answer, a choice that is the user's gets a recommendation with its condition, and what could be made now is made now. Acting: only what could be undone from what the session holds; a copy before a user's file is changed or deleted; a stop before sending, publishing, pushing, spending, or deleting or changing what is held elsewhere; nothing of the user's private material into a search; work inside the folder given, with whatever was put elsewhere removed before the report; nothing installed or reconfigured without the user's word; and a process ended only if the run started it, by its id and never by its name. The check, where the tools exist: what was built is run on input of the user's kind and on cases chosen to break it, every figure is recomputed from the final values, a source is read before it is given as the basis of a claim, and a claim that rests on recall says so. The reply opens with the user's words for what they asked and the outcome as read, then gives the result, leading with what the user should do or decide.
- Since 4.2.0 (D116): the reply opens with the outcome worked to and whose it is, the user's or the assistant's reading, and no longer with the user's words for what they asked.
- Since 4.1.0 (D115): the reply ends with one line that says which request the work was done for and what has shown the outcome so far, or that it is not yet shown, with how and when it can be checked.
- No longer in the body (D114, each approved by the owner): the four labelled lines of D81; the rewritten-prompt block for a run made in the session (a named executor still gets a prompt in place of a run); the case rulings of Running (a commit as the backup, D63; content that must not survive a deletion; the exception for a push); the marks by evidence class and the rule on a source's finding; the case of a creative task; and the line that names a sibling.
- Invocation: first word or explicit name, a choice in dia-router, or an approved request handed over by dia-skopos. `allow_implicit_invocation: true`; the description and the body's first rule gate it.
- Tool-less surfaces: the check and any search are conditional; without tools the reply says what the user should check and how, and a fact from recall is said to be recall.
- Research and pilots: `docs/research/dia-techne.md`; sources of the method and the name in `skills/dia-techne/references/theory.md`; the pilot behind 4.0.0 in probes Part BW.

## 9. Distribution and invocation by surface

Each route has a status:

- **documented**: a vendor document supports it.
- **owner-probed**: the owner's earlier probe of the `socratic` plugin supports it. This is a single source and must be repeated for `dia`.
- **untested**.

| Surface | Install route | Invocation | Status |
|---|---|---|---|
| claude.ai web / Claude desktop | Customize › Plugins › Upload plugin with `dialectic-skills.zip`. Not Customize › Skills, which rejects a zip that carries a plugin manifest. | `/dia:dia-<x>` or natural language | owner-probed for `dia` (P1) |
| Claude mobile (iOS/Android) | Install once via web or desktop; it reaches the mobile app through the account. The upload screen is not in the mobile app. | Natural language; the mobile `/` menu does not list plugin skills (P2) | owner-probed for `dia` (P2) |
| claude.ai marketplace | Customize › Plugins › Add marketplace `ajitta/dialectic-skills`, then add `dia` from Discover | as above | owner-probed (1.1.0, 2026-10-20; the synced copy on the build VM comes from marketplace `dialectic-skills` and matches 1.1.0) |
| Claude Code | `/plugin marketplace add ajitta/dialectic-skills`, then `/plugin install dia@dialectic-skills`; or account sync after a claude.ai upload | `/dia:dia-<x>`, natural language, first word for refine, ratchet and adjudicate; `dia` for the menu | documented (namespacing) / owner-probed (sync) |
| Codex CLI / IDE | `codex plugin marketplace add <path or owner/repo>`, then `codex plugin add dia@dialectic-skills`; fallback: copy `skills/dia-<x>` to `~/.agents/skills/` | `$dia:dia-<x>` (plugin) or `$dia-<x>` (copied folder), `/skills`, implicit per §7.3 | local-path plugin route probed (P3); GitHub route untested |
| ChatGPT desktop | Upload `dialectic-skills-openai.zip` in the desktop app (saved to the account, reaches web and mobile); or add the GitHub marketplace through Codex in the desktop app (local to that computer only) | `@dia-<x>`, implicit | owner-probed (P4/P5, 2026-10-20; upload vs marketplace observed 1.1.1) |
| ChatGPT mobile | A plugin uploaded as a zip on desktop reaches mobile through the account; a marketplace added on desktop does not | `@dia-<x>`, natural language, first word (1.2.0, D33; owner-probed 2026-10-21) | owner-probed (P4/P5, 2026-10-20; upload vs marketplace observed 1.1.1) |

Sources for the ChatGPT rows: [Build skills](https://learn.chatgpt.com/docs/build-skills), [OpenAI Help — Plugins](https://help-lb.openai.com/en/articles/20001256), [OpenAI Help — Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

Runs started by another agent (a sub-agent, `claude -p`, `codex exec`) are a usage context on these surfaces, not a surface of their own, and often no reply comes in them. Until plugin 5.0.0 dia-counterplan then ended with its record when the first message asked for the whole result in one response without questions or said no answer would come (D64); since 5.0.0 (D118) dia-warrant, dia-counterplan, dia-conjecture and dia-adjudicate judge on what there is when no user will reply and put what they would have asked in as open, and dia-reductio says so only for a caller that fixes the format. When such a caller fixes the output format, the four review lenses fit their result into it (D68); dia-adjudicate 4.0.0 has no rule of its own for that. By their text, the skills that wait for the user (dia-skopos, dia-quaestio, dia-elenchus, the dia-router menu, dia-techne at a stop) end with their question and stop; this was not probed. Probed on Claude Code, and dia-counterplan's one-response run also on Codex, where the record came without the question line (0/4) (probes Part AE and its addendum); the README's review-panel item describes the use.

## 10. Migration (owner's installs)

There are no other users, so there is no automatic migration. Before testing `dia`, remove the old copies on each surface; keeping them loads each method twice under two names.

- claude.ai: Customize › Skills — remove the standalone `reductio`, `negative-dialectics`, `self-refine`, `recursive-refine` and `confirm-intent`. Customize › Plugins — remove `socratic`.
- Claude Code: `/plugin uninstall socratic@ajitta-socratic` if installed, and remove copies under `~/.claude/skills/`.
- Codex / ChatGPT desktop: remove any old copies under `~/.agents/skills/`.

The `superclaude` repository and its `socratic` plugin are left as they are.

## 11. Bootstrap: importing upstream material (first task)

The first commit of the new repository imports the material the skills are rebuilt from. It lives under `upstream/`, is excluded from packaging, and is read-only by convention. Rebuild work reads it; nothing edits it.

`upstream/` (repository root) is unrelated to `skills/<skill>/references/`. The latter holds the documents a skill reads at run time, such as theory notes, output templates and `ko/`, and it is shipped with the plugin (§7.1).

```
upstream/
├── README.md                       provenance table (below)
├── installed/                      from the snapshot zip
│   ├── confirm-intent/
│   ├── reductio/
│   ├── negative-dialectics/
│   ├── self-refine/
│   └── recursive-refine/
└── superclaude-stable-47f791b/     from ajitta/superclaude, branch stable, commit 47f791b
    ├── socratic-brainstorm/
    ├── socratic-elenchus/
    ├── package.py
    ├── README.md                   install matrix and invocation notes
    └── docs-features/              portable-skills-single-plugin/, socratic-brainstorm-skill/
```

Steps:

1. Unpack `dialectic-skills-upstream.zip` into `upstream/installed/`. This is the snapshot produced after spec approval (D12), taken from the copies installed in the owner's claude.ai account on 2026-10-20.
2. Copy the listed paths from `ajitta/superclaude` at `stable` commit `47f791b` into `upstream/superclaude-stable-47f791b/`, using `git archive` or a shallow clone. The snapshot zip will also include them, so step 2 is only a cross-check.
3. Write `upstream/README.md` with one row per item: name, origin, version or commit, date taken, SHA-256 of the folder contents.
4. Add `upstream/` to the packaging exclude list, and add a test that fails if any shipped file path starts with `upstream/`.

Note: the installed copies of reductio, negative-dialectics, self-refine, recursive-refine and confirm-intent carry no `license` or version field. Their provenance row records "installed copy, unversioned". All `upstream/` material is the owner's own work (ajitta): the installed copies were written by the owner on their claude.ai account, and the superclaude items come from the owner's MIT repository (owner statement, 2026-10-20).

### 12.2 Surface probes

Each probe is run once (n=1) unless stated otherwise, and the result is recorded in `docs/probes.md` with the date and the client version. Any generalization from n=1 is stated as such.

| # | Probe | Pass condition |
|---|---|---|
| P1 | claude.ai upload of `dialectic-skills.zip` | Accepted; every skill in §4 listed as `dia:dia-<x>` |
| P2 | Claude mobile app (redefined in 2.0.0, D56; 2.1.0, D57; 2.13.0, D72) | `dia` shows the menu; one `dia <name> <request>` per skill loads the right skill; `dia <request>` loads the fitting skill; the reply is in the prompt's language |
| P3 | Codex CLI plugin install, with only `.claude-plugin/plugin.json` | Plugin loads; `$dia:dia-<x>` resolves (the first run showed that plugin skills are namespaced; `$dia-<x>` applies only to a copied folder); `allow_implicit_invocation: false` holds for the four explicit-only skills. If this fails, add the root `plugin.json` (§7.4), re-run, and confirm that Claude Code still loads with both manifests present |
| P4 | ChatGPT desktop (Pro), local plugin install | Skills appear under `@`; one prompt per skill routes correctly |
| P5 | ChatGPT mobile (Pro) after P4 | Skills are usable; if not, record the plan limitation and test the Codex-cloud fallback |
| P6 | First-word invocation (redefined in 2.0.0, D56) | `dia-emend — check numbers` runs one pass; `dia-ratchet` runs the loop; "please refine this paragraph" and "review this draft" start neither; a sentence mentioning dia-emend in the middle does not start it |
| P7 | Routing (redefined in 2.0.0, D56) | (a) natural requests without `dia` or a skill name load no dia skill, with the 1.x routing prompts as cells, 12 runs each; (b) since 2.1.0 (D57), `dia <request>` cells pick the skill whose description fits (probes Part AA), the two border cells go to dia-elenchus and dia-reductio, and a three-letter code, a former name, a counting number or a sentence word after `dia` is read as a request; (c) each number and each name selects its skill. The 1.x definitions are in the git history of this file |
| P8 | Tool-less run | On a surface or session with no tools, `dia-ratchet` (`dia-iterate` before 1.5.0) stops after round 1 with a "verification exhausted" list, and `dia-refine` marks unchecked items unverified instead of changing them |
| P9 | `references/ko/` loading, once O1 is filled | A Korean-law prompt makes the skill read the ko file and state its `As of` date; an unrelated prompt does not read it |

### 12.3 Acceptance

The plugin is accepted when:

- 12.1 passes;
- P1, P2, P3, P6, P7 and P8 pass;
- P4 and P5 have recorded results, pass or documented limitation.

## 13. Open items

| # | Item | Needed by |
|---|---|---|
| O1 | Resolved: no `references/ko/` files in 1.0.0 (D17) | — |
| O2 | Resolved by P3: no portable root `plugin.json` (D16) | — |
| O3 | Resolved: MIT for all seven skills (D18) | — |
| O4 | Resolved by P5: ChatGPT mobile works on Pro (owner, 2026-10-20) | — |
| O5 | Plugin `version`: `0.1.0` during development; first a 0.x pre-release (tag and GitHub pre-release), then P1 and P2 on that release, then `1.0.0` at acceptance (owner, 2026-10-20). Done: `v0.1.0` pre-release, P1/P2/P4/P5 on it, `v1.0.0` released 2026-10-20 | — |
