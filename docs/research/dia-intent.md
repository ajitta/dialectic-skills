# dia-intent: research and fidelity audit

| | |
|---|---|
| Skill | `skills/dia-intent` (SKILL.md 63 lines, 1,307 words; `agents/openai.yaml` 7 lines; no references) |
| Rebuilt from | `upstream/installed/confirm-intent/SKILL.md` (installed copy, unversioned) |
| Date | 2026-10-20 |
| Status | Research only. Every text change below is a proposal; nothing in `skills/` was edited. |

## 1. Scope and summary of what the skill says

dia-intent is a pre-work gate. Once the user invokes it, the assistant does a bounded read-only investigation, then presents a short review (goal, evidence and assumptions, open decisions, confirmation request), and does no substantive work until the user gives a clear instruction to proceed. It names no academic method. Its nearest relatives are requirements elicitation, conversational grounding, selective clarification in NLP, and the scope-of-autonomy and approval-gate patterns in vendor agent guidance. This document checks the skill against those.

What the text says, by location (`skills/dia-intent/SKILL.md`):

- **Trigger and scope** (l.3): explicit invocation only; applies to "that task and its direct follow-ups". `agents/openai.yaml` l.7 sets `allow_implicit_invocation: false`.
- **Meta guard** (l.12): analyzing or editing the skill is not running it.
- **Decompose the request** (l.16): separate the desired outcome, reported observations, causal explanations, proposed means and explicit constraints. Treat explanations and means as hypotheses. Preserve constraints and authority boundaries.
- **Investigate before asking** (l.18): "bounded read-only investigation" with "the smallest decisive read or safe isolated probe". A probe runs on a copy, never on originals or external state, and running the user's code counts as a probe. If isolation cannot be ensured, read only. Stop when the evidence is enough or the remaining uncertainty needs the user. "Do not offer pre-approval investigation as an option."
- **Review content** (l.20–24):
  1. Goal and success conditions, with observable completion criteria. Inferred conditions need their evidence; optional improvements are kept separate.
  2. Evidence and assumptions, labelled as inspected facts, inferences or unverified assumptions. Re-check repeated facts "against a quick computation when one is available (such as a date's weekday or a total)". Points already settled, and choices delegated to the assistant, go here, not into questions.
  3. Decisions needed from the user: only preferences, trade-offs, authority, or facts only the user holds that "could materially change the result". Investigate a factual question instead of asking it. Before listing an item, check that the request does not already settle it. A material, non-delegated choice stays on the list with a recommendation if it "cannot be undone, ... reaches other people, or ... rests on an ambiguous reading". A step the user requested is settled even if it is irreversible: name the irreversibility and offer the safeguard, but do not ask about it.
- **Dependent decisions** (l.26): if answers depend on each other and need more than one round, name the first decision and offer an interview-style approach or "a suitable skill available in this session". Ask the first decision now and defer the dependent ones.
- **Proportionality** (l.28): material items only; omit empty sections; "a few sentences may suffice".
- **Hold** (l.30–34): until approval, no implementation, no substantive draft, no changes to user assets, no publishing, sending, purchasing or commitments. "The original task request does not itself count as approval." Approval fixes the working understanding and authority; it does not make the explanation true.
- **Recognizing approval** (l.36–42): any clear proceed instruction counts. Corrections plus proceed count as approval of the revised task. Partial approval covers that part only. Corrections alone get a revised review. Praise, ambiguous reactions, silence or elapsed time are not approval.
- **After approval** (l.44–46): delegated choices are made and disclosed. Scope, authority or constraint changes are re-agreed for the changed part only. Unaffected work continues, and held steps are named. Routine details do not restart confirmation.
- **Format** (l.48–64): four bold-labelled sections, labels translated, empty sections omitted. For an ambiguous reaction, ask briefly for a proceed instruction instead of repeating the review.

Spec §5.1 describes the purpose as "restate the goal, disclose material assumptions and list only the decisions the user must make. Then wait for approval", with behavior "unchanged from the reference". The text matches that description.

## 2. The method in its primary sources

dia-intent has no single originating text, so this section reconstructs the method from the four traditions it draws on.

### 2.1 Grounding: confirmation as positive evidence of shared understanding

Clark and Brennan define the *grounding criterion*: "The contributor and his or her partners mutually believe that the partners have understood what the contributor meant to a criterion sufficient for current purposes."[15] A contribution has a presentation phase and an acceptance phase, and "It takes both phases for a contribution to be complete."[15] They argue that people look for *positive* evidence of understanding. If only negative evidence counted, "we would often accept information we had little justification for accepting."[15] They also say the criterion and technique vary with purpose and medium, and that partners try to minimize the joint effort.[15]

A restated goal is a presentation, and the user's proceed instruction is the acceptance. The skill's refusal to count silence, praise or elapsed time as approval (l.42) is the positive-evidence rule in operational form. "Scale the review to the task" (l.28) matches "sufficient for current purposes".

### 2.2 Requirements engineering: optative vs indicative, and means vs ends

Zave and Jackson separate statements in the "indicative" mood, which describe the environment as it is ("often called 'assumptions' or 'domain knowledge'"), from statements in the "optative" mood, which describe it as we would like it to be ("commonly called 'requirements'").[27] They also name *implementation bias*: "Requirements are supposed to describe what the desired machine does, not how it does it."[27]

The skill's split of outcome, observations, causal explanations, proposed means and constraints (l.16) is a practitioner version of this. Outcome and constraints are optative. Observations and explanations are indicative and can be wrong, so they are "hypotheses". Proposed means are possible implementation bias. The skill does not cite this tradition, and it adds a category the paper does not have (authority boundaries).

### 2.3 Decision theory of asking vs acting

Horvitz's mixed-initiative principles include "Employing dialog to resolve key uncertainties ... considering the costs of potentially bothering a user needlessly" and "Scoping precision of service to match uncertainty": "A preference for 'doing less' but doing it correctly under uncertainty."[14] He models dialog as a third option beside acting and not acting. There are two thresholds on the probability of the user's goal, one between inaction and dialog and one between dialog and action. "Thresholds can be directly assessed by designers or users."[14]

This framing explains an apparent conflict. Most guidance says to ask *selectively*, yet dia-intent asks for confirmation *every time it is invoked*. Explicit invocation is the user setting the dialog/action threshold by hand: for this task, confirmation is worth a round trip. Inside the review, the skill goes back to selective asking: list only material, open, non-investigable decisions. That reading is coherent with Horvitz. The skill does not state it, though.

### 2.4 Vendor guidance on scope, assumptions and approval

- **OpenAI Model Spec** is the closest primary source. It tells the assistant to "weigh the cost of incorrect assumptions against the inconvenience of asking", to "fill information gaps using context or trusted external sources ... resorting to direct user queries only when uncertainty persists", and notes that "Trivial questions ... may be better if stated as an assumption that the user can correct."[20]
  - It separates actions "logically necessary to fulfill the user's request", which the assistant announces without pausing, from actions "beyond what the request clearly implies", which need confirmation.[20]
  - For sensitive or irreversible actions, the confirmation should "clearly outline what information will be sent, who will receive it".[20]
  - Its "scope of autonomy" covers which sub-goals the assistant may pursue, acceptable side effects, and "When the assistant must pause". A good scope should "resolve the most consequential uncertainties" and "prevent unnecessary user interactions". Every scope "must include an ending condition".[20]
  - It warns that confirmations for trivial actions "could habituate the user to automatically confirming all requests".[20]
  - Its worked example ("Before I start booking ... does this sound right?") has almost the same shape as a dia-intent review.[20]
- **Claude's Constitution** lists, as an unhelpful behavior, one that "Checks in or asks clarifying questions more than necessary for simple agentic tasks". It also says "Claude should ask for clarification in cases of genuine ambiguity."[21]
- **Anthropic prompting guidance** offers two opposite system-prompt snippets. `<default_to_action>` says "infer the most useful likely action and proceed, using tools to discover any missing details instead of guessing". `<do_not_act_before_instructions>` says that when intent is ambiguous, "default to providing information, doing research, and providing recommendations rather than taking action".[16] dia-intent is a task-scoped, user-invoked form of the second, with the first's "discover instead of guessing" built in (l.18).
- **Claude Code plan mode** is the product-level version of the same gate. "Plan mode tells Claude to research and propose changes without making them", and "edits stay blocked until you approve the plan".[25]
- **Anthropic, Building effective agents**: agents "pause for human feedback at checkpoints or when encountering blockers" and use stopping conditions "to maintain control".[22]
- **OpenAI GPT-5 prompting guide** shows the opposite pole. Its "more eagerness" prompt says "Do not ask the human to confirm or clarify assumptions ... proceed with it, and document it", and a quoted coding prompt says "you should almost never ask the user whether to proceed with a plan".[19] The same guide recommends per-tool thresholds: checkout and payment tools "should explicitly have a lower uncertainty threshold for requiring user clarification", and "the delete file tool should have a much lower threshold than a grep search tool".[19]

## 3. Modern research on clarification in LLMs

**Models under-ask by default.**

- Kuhn et al. found that "current language models rarely ask users to clarify ambiguous questions and instead provide incorrect answers". Their CLAM framework prompts the model to detect ambiguity, ask, and then answer.[1]
- In tool use, Wang et al. found that LLMs "tend to arbitrarily generate the missed argument, which may lead to hallucinations and risks". They propose Ask-when-Needed.[11]
- Laban et al. measured an average 39% drop from single-turn to multi-turn underspecified conversations. "LLMs often make assumptions in early turns and prematurely attempt to generate final solutions, on which they overly rely."[12]

These findings are the strongest support for a pre-work gate that makes assumptions visible before they set.

**Ambiguity is common, and asking pays when it is targeted.**

- AmbigQA found "over half of the questions in NQ-open are ambiguous".[3]
- Aliannejadi et al. report that "asking only one good question leads to over 170% retrieval performance improvement in terms of P@1".[5]
- On Ambig-SWE, interaction improved underspecified-task performance by up to 74%. However, "models struggle to distinguish between well-specified and underspecified instructions".[6]

**Selectivity is the hard part.**

- Zhang and Choi split the problem into when to ask, what to ask, and how to use the answer. Their intent-entropy method, "When only allowed to ask for clarification on 10% of examples", doubles the gain of random selection.[2]
- Edwards and Schuster found that a prompted "Interactive Baseline achieves its high resolve rate at the cost of overclarification, asking questions in nearly every instance regardless of necessity". A scaffold with a separate intent-detection agent asked less often and matched it.[9]
- HiL-Bench scores asking with Ask-F1, "the harmonic mean of question precision and blocker recall", to capture "the tension between over-asking and silent guessing". It finds "a large universal judgment gap".[7]
- HiL-Bench's blockers "surface only through progressive exploration, not upfront inspection".[7] An up-front review cannot catch every blocker; re-agreement during execution (l.46) is needed.

**Timing matters.** Gulati et al. found that "goal clarification loses nearly all value after 10% of execution ... while input clarification retains value through roughly 50%". Deferring any clarification "past mid-trajectory degrades performance below never asking at all". In unscripted sessions they observed strategies "ranging from over-asking (52% of sessions) to never asking at all".[8] This supports confirming the *goal* before work and leaving routine *input* details to the execution phase, which is what l.44–46 do.

**Investigate, then ask, but do not keep searching.** On DiscoBench, SearchThenAsk reached 93.4% mean pass rate, against 56.5% for DirectGuess and 51.9% for SearchHeavyGuess. "SearchHeavyGuess even underperforms DirectGuess despite performing more retrieval steps."[10] This supports both halves of l.18: investigate first, and stop when the remaining uncertainty needs the user.

**Question quality and user cost.**

- In a user study with 89 participants, "low-quality CQs do disturb users", and showing only high-quality clarifying questions "receives better gains with less effort".[28]
- GATE and STaR-GATE show that elicitation quality can be improved by prompting or training. STaR-GATE's questioner produced responses preferred "on 72% of tasks".[13][4]
- A Claude Code user report describes "pseudo-check-ins" that "ask questions whose answers are already in context", each costing "a context-switch, a moment of attention". This is single-user evidence, not a measurement.[26]

**Approval and sycophancy.** Sharma et al. found that assistants "consistently exhibit sycophancy" and that responses matching the user's views are preferred.[29] This bears on two parts of the skill. The rule that approval "does not establish that the explanation is true" (l.34) guards against it. Corrections that contradict inspected evidence are not covered (finding 6).

## 4. Fidelity audit

The skill names no method, so the audit asks whether each rule is supported by the traditions in §2–3. Verdicts: **matches**, **loose** (same idea, looser or partial), **departs** (deliberately different), **unsupported** (no source either way).

| # | Skill rule (line) | What the sources say | Verdict |
|---|---|---|---|
| A1 | Restate goal with observable completion criteria (l.22) | Grounding needs a presentation the partner can accept[15]. A scope defines sub-goals and an ending condition[20] | matches. No explicit ending or limit field (finding 4) |
| A2 | Separate outcome / observations / explanations / means / constraints; explanations and means are hypotheses (l.16) | Optative vs indicative; implementation bias[27] | loose, and a sound practitioner adaptation |
| A3 | Investigate before asking; smallest decisive read; do not offer investigation as an option (l.18) | Fill gaps from context and tools; ask "only when uncertainty persists"[20]. "use tools to discover any missing details instead of guessing"[16]. SearchThenAsk best[10] | matches |
| A4 | Bounded; stop when remaining uncertainty needs the user; not exhaustive (l.18) | SearchHeavyGuess < DirectGuess[10]. Plan mode explores but does not edit[25] | matches |
| A5 | Probes only on isolated copies; running user code counts as a probe (l.18) | Minimize side effects; GET requests with sensitive data count as side effects[20]. Plan mode allows exploratory shell commands under a classifier[25] | stricter than the sources (by design) |
| A6 | Label facts / inferences / unverified assumptions (l.23) | "articulating and/or confirming any assumptions"[20]. Early hidden assumptions derail models[12] | matches |
| A7 | Re-check repeated facts "against a quick computation when one is available" (l.23) | No source found on this exact practice. On tool-less surfaces the "computation" is the model's own re-derivation | unsupported; risky as worded (finding 5) |
| A8 | List only decisions that are open, non-investigable and material (l.24) | Trivial questions → state as assumption[20]. Over-asking is unhelpful[21]. Ask-F1 precision[7]. Overclarification under prompting[9]. Low-quality questions disturb users[28]. Selective asking[2] | matches, well founded |
| A9 | Materiality triggers: cannot be undone, reaches other people, ambiguous reading (l.24) | Model Spec side-effect list adds expenditures, deleting files, modifying external documents, sending sensitive data; it asks for "what information will be sent, who will receive it"[20]. Per-tool thresholds for payment and delete[19] | loose: money and data disclosure are not named (finding 3) |
| A10 | A requested step is settled even if irreversible; mention it, do not ask (l.24) | "logically necessary" actions are announced without pausing[20] | matches |
| A11 | Recommendation with each kept decision (l.24) | Model Spec example states its own default ("I'll assume you prefer non-stop")[20]. Horvitz: users refine the agent's guesses[14] | matches |
| A12 | Dependent decisions: name the first, defer the rest, offer an interview (l.26) | Prior work selects each next question given the earlier answers[5]. No source found on batching dependent questions | loose; sound |
| A13 | Always hold for approval once invoked; the request is not approval (l.30–32) | Default guidance is selective or concurrent: "take a stab", ask and act "concurrently"[20]; "almost never ask ... whether to proceed"[19]. Thresholds may be set by users[14] | departs by design: the user opted in. Justified, but not stated in the text (finding 1) |
| A14 | Silence, praise, ambiguity ≠ approval (l.42) | Positive evidence of understanding is required[15] | matches |
| A15 | Corrections + proceed = approval of revised task; corrections alone → revise and wait (l.39, 41) | Grounding repair sequences[15] | matches |
| A16 | Partial approval covers only that part (l.40) | Scope must be "mutually understood"; out-of-scope needs approval[20] | matches |
| A17 | Approval does not make the explanation true (l.34) | Sycophancy: models drift toward the user's views[29] | matches (guard) |
| A18 | Re-agree changed scope or authority only; continue unaffected work; name held steps (l.46) | "If a task cannot be completed within the existing scope ... notify the user and seek approval"[20]. Blockers surface mid-task[7] | matches |
| A19 | Omit empty sections; a few sentences may suffice (l.28) | Scope should "prevent unnecessary user interactions"[20]. Habituation risk[20] | matches. Padding risk remains (finding 2) |
| A20 | Explicit invocation only (l.3, openai.yaml l.7) | Codex: `false` stops implicit use; `$skill` still works[17]. Claude: no portable equivalent (§6) | holds on Codex; on Claude it rests on wording only (finding 7) |

Overall: dia-intent is a faithful, conservative implementation of the "scope of autonomy + state assumptions + selective clarification" consensus. It departs in one deliberate way: an unconditional hold once invoked. Since it claims no named method, no relabelling is needed. The sources do suggest saying *why* it always holds, and widening its materiality triggers.

## 5. Lineage: what changed from upstream

`diff upstream/installed/confirm-intent/SKILL.md skills/dia-intent/SKILL.md` shows changes only in the frontmatter:

- `name` changed from `"confirm-intent"` to `dia-intent`, and the quotes around `name` and `description` were dropped.
- Added `license: MIT` and `metadata` (`author`, `version: "1.0.0"`, `lineage`, `source`).
- The body (upstream l.6–57 = dia l.12–63) is byte-identical.
- `agents/openai.yaml` is new: display name "Dia: Confirm Intent", `default_prompt: "Use $dia-intent to ..."`, and `allow_implicit_invocation: false`.

This satisfies spec §5.1 ("Behavior: unchanged from the reference"). No Hangul and no cross-references needed removing.

**What the upstream design notes say.** `upstream/superclaude-stable-47f791b/docs-features/` has no design or research notes for confirm-intent; its origin is undocumented in this repository. Two related upstream practices survive in altered form:

- `portable-skills-single-plugin/00-intent.md` is an earlier intent record by the owner. It has sections Problem / Proposed outcome / Affected users and systems / Constraints / Open questions, and it quotes the requester verbatim ("Existing installs must not break"). dia-intent keeps the structure (goal, constraints, open decisions) but has no verbatim-quote rule and no "affected users and systems" slot. The "reaches other people" trigger (l.24) only partly covers the latter.
- `socratic-brainstorm-skill/02-research.md` l.20 records that `/sc:brainstorm` tagged decisions as `confirmed` vs `delegated`. dia-intent's "choices delegated to you ... with ... the option you will use" (l.23) carries that distinction.

**Explicit-only lineage.** `socratic-brainstorm-skill/04-design.md` D2 chose "explicit-only by wording + Codex `allow_implicit_invocation: false`" over `disable-model-invocation: true`, because the latter "makes the claude.ai upload fail". dia-intent inherits that decision (spec §7.3). The upstream Codex probe N1 (`08-implementation.md`) confirmed that, with the flag set, a plain-words prompt did not load the skill. P3 here confirmed that the flag hides dia-intent from Codex's model-visible list and that `$dia:dia-intent` loads it (`docs/probes.md` l.31–32).

**Nothing was lost in the rebuild.** The one gap is evidential, not textual. No probe in `docs/probes.md` exercises dia-intent's *behavior* (review shape, hold, approval recognition), and P7 routing did not include it. Spec §5.1 relies on "unchanged" text; nothing has shown the text behaves as intended on the target models.

## 6. Risks and failure modes

### 6.1 On LLMs generally

1. **Manufactured decisions.** Prompted to ask, models over-ask[9], and they struggle to tell well-specified from underspecified tasks[6]. A model under dia-intent may fill "Decisions needed" with items the request already settles, the "pseudo-check-in" pattern[26]. The skill's settled-check (l.24) and "Omit if nothing remains" (l.61) address this. Neither says outright that an empty decision list is a normal, good outcome.
2. **Approval habituation.** If every review carries questions, users learn to type "go". The Model Spec warns of exactly this[20].
3. **Hidden early assumptions.** This is the failure the skill exists to prevent[12]. It is only as good as the model's assumption detection; HiL-Bench reports "overconfident wrong beliefs with no gap detection" as a common pattern[7].
4. **Fake verification.** l.23's "quick computation" invites a model on a tool-less surface to state a weekday or total as checked when it only recalled it. P8 found the same class of defect in dia-refine; it was fixed there by saying "recall is not verification" (`docs/probes.md` l.67–71).
5. **Sycophantic corrections.** A user correction that contradicts inspected evidence may be adopted silently[29]. l.39/41 say to apply corrections but not to flag a conflict with evidence.
6. **Rule density.** l.18, l.24 and l.26 are single paragraphs of 195, 190 and 173 words with nested exceptions. Long, conditional prose is where instruction-following drops rules. This is a general concern, not measured for this skill [unverified].

### 6.2 Tool-less and mobile surfaces

- **Investigation collapses to reading the chat.** On a tool-less surface, l.18's probe machinery (copies, caches, test output) does not apply. The fallback "inspect by reading only and report the remaining uncertainty" is correct. About 150 words of probe rules are then dead weight in context. They are still worth keeping in the body: P8 showed headless runs sometimes cannot open `references/` (`docs/probes.md` l.77).
- **Review length on phones.** Four bold sections render fine in plain Markdown, and l.28 allows "a few sentences". The risk is a full four-section review for a trivial task.
- **Hold vs harness.** In non-interactive runs (`claude -p`, `codex exec`) the run ends with the review and no work done. That is correct for the skill but surprising for scripted use. Claude Code's auto mode "nudges Claude to keep working without stopping for clarifying questions, though Claude still asks when your prompt or a skill explicitly relies on it"[25], so the hold should survive auto mode. Codex harness prompts may contain persistence instructions like the GPT-5 guide's "Never stop or hand back to the user when you encounter uncertainty"[19]. Whether the current Codex system prompt does is [unverified]. The interaction should be probed.

### 6.3 Cross-surface invocation (explicit-only policy)

| Surface | Mechanism for "explicit only" | Consequence |
|---|---|---|
| Codex CLI / IDE (plugin) | `allow_implicit_invocation: false` hides the skill from the model's list; explicit `$skill` still works[17]. P3: `$dia:dia-intent` loads it; `$dia-intent` does not | Holds. `default_prompt` uses `$dia-intent`, which likely fails on the plugin route (handoff item 3). An issue thread reports the TUI `$` picker inserting the *display name* casing (e.g. `$Wayfinder`) so explicit-only skills fail to resolve[18]. The display name here is "Dia: Confirm Intent", so the picker route should be probed |
| ChatGPT desktop / mobile | `@` selection; implicit use governed by the same yaml[17] | Untested (P4/P5). Plan availability on Pro is unconfirmed (spec §9) |
| claude.ai web / desktop / mobile | No portable flag. `disable-model-invocation` is a Claude Code extension, and upload "fails with a hard error" on non-spec keys[23]. Claude "determines when each skill is needed based on your request"[24] | Explicit-only rests on the description sentence alone. Implicit firing would impose an unrequested gate, which is the over-asking failure. On mobile the user must name the skill in prose; whether naming it in a sentence counts as "explicitly ... invoked" is left to the model |
| Claude Code (plugin) | `skillOverrides` "user-invocable-only" exists, but "Plugin skills are not affected by `skillOverrides`"[23] | Same as claude.ai: wording only. No user-side switch to enforce it |

## 7. Findings and recommendations (proposals only)

**1. State why the gate is unconditional once invoked. (medium)**
- Evidence: A13 departs from the selective/concurrent default in vendor guidance[20][19][21]. Horvitz's user-set threshold explains why that is legitimate[14], but the text never says so. Without that framing, a model trained toward "take a stab" may treat the hold as optional on easy tasks.
- Proposed text, after l.32: "The user invoked this skill to see the plan before any work. Hold even when the task looks clear; in that case keep the review to a few sentences and ask only for a proceed instruction."

**2. Name the empty decision list as a good outcome and forbid padding. (medium)**
- Evidence: prompted agents over-clarify[9], and models misjudge well-specified tasks[6]. Pseudo-check-ins cost attention[26]. Confirmations habituate users[20], and Ask-F1 penalizes imprecise questions[7].
- Proposed text, append to item 3 (l.24): "Often nothing remains open; then write that no decisions are needed. Do not add questions to fill the section, and do not ask for confirmation of points the review already states as settled."

**3. Widen the materiality triggers to spending and data disclosure, and name recipients. (medium)**
- Evidence: A9. The Model Spec lists direct expenditures and sending sensitive data as side effects. It asks confirmations to say "what information will be sent, who will receive it"[20]. Payment and delete tools warrant low thresholds[19]. The skill's triggers (cannot be undone, reaches other people, ambiguous reading) do not cover a reversible but costly purchase, or a GET request that leaks data.
- Proposed text, l.24: "... it cannot be undone, it spends money or other limited resources, it discloses the user's data or reaches other people, or it rests on an ambiguous reading of the request." Template l.64: "... including what will be sent or spent and to whom, any requested step that cannot be undone ..."

**4. Ask for a limit or ending condition when the work is open-ended. (low)**
- Evidence: "Every scope must include an ending condition"[20]; stopping conditions keep control[22]. "Concrete work and authority to approve" (l.64) does not prompt for limits such as a budget, item count or time.
- Proposed text, template l.64: "... Concrete work, authority and, for open-ended work, its limit (budget, count or stopping point) ..."

**5. Do not present recalled or mentally computed facts as checked. (medium)**
- Evidence: A7 is unsupported. P8 found the same defect class in dia-refine and fixed it there with "recall is not verification" (`docs/probes.md` l.67–71). Keeping the two skills consistent is cheap.
- Proposed text, l.23: "Check facts you will repeat or act on with a tool computation when one is available (such as a date's weekday or a total). Without a tool, label the value as re-derived or unverified; recall is not verification."

**6. Flag corrections that conflict with inspected evidence. (low)**
- Evidence: sycophancy[29]; l.39/41 adopt corrections unconditionally, while l.34 already separates approval from truth.
- Proposed text, append to l.41: "If a correction conflicts with evidence you inspected, apply it as the user's decision but name the conflicting evidence once in the revised review."

**7. Make the explicit-only claim testable on Claude, and close the Codex prompt gap. (high: it is the policy's only enforcement on Claude, and it has never been measured)**
- Evidence: §6.3. On claude.ai and Claude Code plugins, nothing but the description enforces explicit-only[23][24]. No probe covers dia-intent routing (P7 excluded it). `default_prompt` uses `$dia-intent`, which did not resolve on the plugin route in P3. Picker casing may break explicit-only invocation[18].
- Proposals, no skill-text change needed yet:
  - (a) Add a probe pair to spec §12.2 for Claude Code and claude.ai. A plain task ("fix the off-by-one in this function") must not load dia-intent. "dia-intent: fix ..." and "confirm the plan with dia-intent before you start" must load it.
  - (b) Settle handoff item 3 for this skill: `default_prompt: "Use $dia:dia-intent to ..."` if P4 confirms the plugin form.
  - (c) In P4, test the `$` picker route as well as typed names.

**8. Clarify what counts as explicit invocation in words. (low)**
- Evidence: on mobile, prose is the only route (README l.30). "explicitly selected or invoked" (l.3) leaves "please confirm the plan before you start" ambiguous.
- Proposed description text: "Use only when the user selects or names this skill, or explicitly asks to confirm the goal and open decisions before any work starts." Note that this widens triggering slightly; owner decision (Q2).

**9. Run a small behavioral probe of the review itself. (medium)**
- Evidence: §5. "Unchanged" text has no behavioral evidence on current models. The research shows exactly these behaviors vary by model[6][7][8].
- Proposal: n=2 per cell, Claude Code and Codex, tools on and off. Four prompts:
  - (i) a fully specified task: expect a short review, no decisions, a hold;
  - (ii) an ambiguous one: expect one or two decisions with recommendations;
  - (iii) an irreversible requested step: expect it settled, irreversibility named, the safeguard offered;
  - (iv) "looks good!": expect no execution and a brief proceed request.
- Record the results in `docs/probes.md`. `claude plugin eval` can run each prompt with and without the plugin[23].

**10. Restructure the three longest paragraphs into bullets without changing rules. (low)**
- Evidence: l.18/24/26 are 173–195 words each, with nested exceptions (§6.1 item 6) [unverified as a cause of failures here].
- Proposal: split l.18 into "what to investigate / how to probe safely / when to stop" and l.24 into "what qualifies / what to exclude / when to keep a choice with a recommendation". Keep the wording; behavior stays unchanged under spec §5.1.

**11. Optionally record the request's own words for constraints. (low)**
- Evidence: the owner's earlier intent record quoted the requester verbatim (`00-intent.md`). Grounding works best when the presentation lets the partner check the exact content[15]. Paraphrased constraints can drift.
- Proposed text, l.22: "Quote explicit constraints in the user's words when they are short."

## 8. Open questions for the owner

1. Should a user be able to waive the hold in the invoking message (e.g. "dia-intent, and just proceed if nothing is open")? The current text (l.32) says no. Model Spec practice would allow it[20].
2. Should "please confirm the plan before you start", with no skill name, count as explicit invocation (finding 8)? This trades mobile usability against the explicit-only promise.
3. l.26 offers "a suitable skill available in this session" for dependent decisions. Should it name `dia-brainstorm`? That skill ends in a verdict and a brief and never implements (spec §5.3), so it fits exploration better than settling execution choices.
4. Is the strict copy-only probe rule (A5) intended to stay stricter than Claude Code plan mode, which runs exploratory shell commands under a classifier[25]? On large repositories, copying may be impractical, which pushes the model to read-only inspection.
5. Should findings 3–6 count as "behavior changes" under spec §5.1 ("unchanged from the reference")? If so, they need a spec amendment and a version bump (AGENTS.md l.26).

## Sources

[1] https://arxiv.org/abs/2212.07769 — Kuhn, Gal, Farquhar — CLAM: Selective Clarification for Ambiguous Questions with Generative Language Models (2022)
[2] https://arxiv.org/abs/2311.09469 — Zhang & Choi — Clarify When Necessary: Resolving Ambiguity Through Interaction with LMs (2023)
[3] https://arxiv.org/abs/2004.10645 — Min et al. — AmbigQA: Answering Ambiguous Open-domain Questions (EMNLP 2020)
[4] https://arxiv.org/abs/2403.19154 — Andukuri et al. — STaR-GATE: Teaching Language Models to Ask Clarifying Questions (2024)
[5] https://arxiv.org/abs/1907.06554 — Aliannejadi et al. — Asking Clarifying Questions in Open-Domain Information-Seeking Conversations (SIGIR 2019)
[6] https://arxiv.org/abs/2502.13069 — Vijayvargiya et al. — Ambig-SWE: Interactive Agents to Overcome Underspecificity in Software Engineering (2025)
[7] https://arxiv.org/abs/2604.09408 — Trinh, Elfeki et al. — HiL-Bench: Do Agents Know When to Ask for Help? (2026)
[8] https://arxiv.org/abs/2605.07937 — Gulati et al. — Ask Early, Ask Late, Ask Right: When Does Clarification Timing Matter for Long-Horizon Agents? (2026)
[9] https://arxiv.org/html/2603.26233v2 — Edwards & Schuster — Ask or Assume? Uncertainty-Aware Clarification-Seeking in Coding Agents (2026)
[10] https://arxiv.org/abs/2606.27669 — Tao et al. — When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search (2026)
[11] https://arxiv.org/abs/2409.00557 — Wang et al. — Learning to Ask: When LLM Agents Meet Unclear Instruction (2024)
[12] https://arxiv.org/abs/2505.06120 — Laban et al. — LLMs Get Lost In Multi-Turn Conversation (2025)
[13] https://arxiv.org/abs/2310.11589 — Li, Tamkin, Goodman, Andreas — Eliciting Human Preferences with Language Models (GATE, 2023)
[14] https://erichorvitz.com/chi99horvitz.pdf — Horvitz — Principles of Mixed-Initiative User Interfaces (CHI 1999)
[15] https://web.stanford.edu/~clark/1990s/Clark,%20H.H.%20_%20Brennan,%20S.E.%20_Grounding%20in%20communication_%201991.pdf — Clark & Brennan — Grounding in Communication (1991)
[16] https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices — Anthropic — Prompting best practices (Claude docs)
[17] https://learn.chatgpt.com/docs/build-skills — OpenAI — Build skills (ChatGPT / Codex)
[18] https://github.com/openai/codex/issues/40600 — openai/codex issue #40600 — allow_implicit_invocation: false and explicit $skill invocation
[19] https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide — OpenAI — GPT-5 prompting guide (agentic eagerness)
[20] https://model-spec.openai.com/2026-08-18.html — OpenAI — Model Spec (2026-08-18)
[21] https://www.anthropic.com/constitution — Anthropic — Claude's Constitution
[22] https://www.anthropic.com/engineering/building-effective-agents — Anthropic — Building effective agents (2024)
[23] https://code.claude.com/docs/en/skills — Claude Code docs — Extend Claude with skills
[24] https://support.claude.com/en/articles/12512180-use-skills-in-claude — Claude Help Center — Use skills in Claude
[25] https://code.claude.com/docs/en/permission-modes — Claude Code docs — Choose a permission mode (plan mode, auto mode)
[26] https://github.com/anthropics/claude-code/issues/59555 — anthropics/claude-code issue #59555 — Pseudo-check-ins ask questions whose answers are already in context
[27] http://www.pamelazave.com/4dc.pdf — Zave & Jackson — Four Dark Corners of Requirements Engineering (TOSEM 1997)
[28] https://irlab.science.uva.nl/wp-content/papercite-data/pdf/zou2022asking.pdf — Zou, Sun, Long, Aliannejadi, Kanoulas — Asking Clarifying Questions: To Benefit or to Disturb Users in Web Search? (IP&M 2023)
[29] https://arxiv.org/abs/2310.13548 — Sharma et al. — Towards Understanding Sycophancy in Language Models (2023)
