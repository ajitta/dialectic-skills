# Review: docs/research/dia-intent.md

Verdict: SOUND WITH FIXES

The document's description of the skill is accurate. I re-opened every file:line it cites, and all are correct, including the 195/190/173-word paragraph counts, the diff against upstream and the probe line numbers. Every quoted source passage I fetched exists as quoted. The weaknesses are in the analysis and the proposals. Three severities are inflated (findings 1, 3 and 7). Two proposed texts conflict with existing rules in the skill (findings 2 and 6). One fidelity verdict rests on a misreading of Clark and Brennan (A14). The document also missed one real pre-approval gap: data disclosure and cost during investigation.

Paths below are relative to `tree/`. Fetched source texts are saved in `~/.hermes/profiles/reviewer/cache/scratch/dia-intent/`.

Basic checks:
- Document under review: 271 lines, within the 500-line limit.
- SKILL.md: 63 lines. Description: 271 characters. No Hangul.
- Every proposal, if applied, keeps SKILL.md far under 200 lines and the description under 1024 characters. No proposal adds a product name or an unconditional tool use.

## 1. Findings in section 7

F1. State why the gate is unconditional (medium): PARTLY. Lower to low.
- The gap is real. l.30–32 enforce the hold but never give the reason for it.
- No evidence shows the hold failing. P3's one dia-intent run "followed its review format" (docs/probes.md:32). The predicted failure is speculative.
- The proposed text says "to see the plan". The skill never uses "plan"; use "the review".
- "ask only for a proceed instruction" can be read as overriding l.64, which still requires naming a requested irreversible step and its safeguard. Say "keep the review to a few sentences" and drop "only".
- This finding presupposes the answer to open question 1 (waiving the hold). Settle that question first.

F2. Name the empty decision list as a good outcome (medium): PARTLY. Lower to low, and fix the text.
- Most of the problem is already covered:
  - l.24: settled items go to evidence.
  - l.28: "Include only material items and omit empty sections".
  - l.61: "Only what remains open … Omit if nothing remains".
  - l.64: "the open decisions only".
- The proposed "then write that no decisions are needed", appended to item 3, contradicts l.28, l.50 and l.61. All three say to omit the empty section.
- Minimal version: "An empty decision list is normal; do not add items to fill it."

F3. Widen the materiality triggers (medium): PARTLY. Lower to low.
- The Model Spec passages are real (side-effects list; "clearly outline what information will be sent, who will receive it").
- The gap in l.24 is narrower than claimed. The same paragraph says "Your own default settles an item only when the choice was delegated or is minor". So a costly, non-delegated choice already stays a decision. l.30 also already forbids purchasing before approval.
- "other limited resources" is open-ended. It invites the over-asking that F2 tries to prevent. Drop it.
- The template change at l.64 ("what will be sent or spent and to whom") is the useful part. Keep it.
- The real data-disclosure gap sits in the investigation rule (l.18), not in the decision list. See missed issue M1.

F4. Ask for a limit or ending condition (low): PARTLY.
- The cited sentence exists: "Every scope must include an ending condition … best practice to include a time limit" (Model Spec, scope of autonomy). The Model Spec's own example lists "Total budget authority: $4000" and "Complete all reservations within 24 hours".
- But l.22's "observable completion criteria" already is an ending condition for bounded tasks. The document's own A1 rates it "matches".
- The only gap is a resource limit for open-ended work. The proposal is correctly scoped to that ("for open-ended work"). Fine as a low.

F5. Recall is not verification (medium): PARTLY. Low-to-medium.
- The risk is real. Without a code tool, "a quick computation … such as a date's weekday" is error-prone mental arithmetic.
- "P8 found the same defect class" is overstated. P8's defect was a rule conflict that let dia-refine rewrite a factual claim from recall (docs/probes.md:63–66). l.23 is about computation, not recall.
- The proposal makes the tool-less wording stricter than dia-refine, the skill it claims to align with. dia-refine treats your own re-derivation as a confirmed basis: "Re-derive logic and calculations independently; this needs no tools" (skills/dia-refine/SKILL.md:31; probes.md:69).
- To stay consistent, label a value as "re-derived (no tool)" and reserve "unverified" for recalled facts.
- This is a behavior change under spec §5.1. Open question 5 already flags that.

F6. Flag corrections that conflict with evidence (low): PARTLY.
- The gap is real. l.39 and l.41 apply corrections with no conflict check.
- "apply it as the user's decision" fits preferences and authority, not facts. l.24 says to investigate factual questions rather than settle them by asking.
- Suggested text: "If a correction conflicts with evidence you inspected, name that evidence once in the revised review; follow the correction for preferences, scope and authority."

F7. Make the explicit-only claim testable (high): PARTLY. Lower to medium.
- The core claim is confirmed by code.claude.com/docs/en/skills: "Plugin skills are not affected by `skillOverrides`. Manage those through `/plugin` instead". The same page shows the upload "fails with a hard error" on fields the spec does not allow.
- The severity is inflated. Implicit firing produces an unwanted review and hold. It is visible and recoverable, with no loss of data or authority.
- "No probe covers dia-intent routing" is partly wrong. Handoff item 2 (docs/handoff.md:20) already plans a P2 prompt for intent, but P2's pass condition is "the right skill loads" from a natural-language prompt. For an explicit-only skill that is ambiguous. Proposal (a) should amend P2 rather than only add a new probe.
- (b) repeats handoff item 3 (handoff.md:21) almost word for word. It is not a new finding.
- (c) is valid and new.

F8. Clarify explicit invocation in words (low): PARTLY.
- Widening the description has no effect on Codex or ChatGPT. With `allow_implicit_invocation: false` the skill is absent from the model-visible list (probes.md:31), so a description clause for implicit triggering can never fire there.
- Result: Claude would trigger on "confirm the plan before you start" and Codex would not. That breaks "run unchanged on every surface".
- It also changes spec §5.1 and §7.3 ("Its description says explicit only").
- Keep it as an owner question, with this divergence stated.

F9. Behavioral probe (medium): CONFIRMED.
- The gap is real: nothing in docs/probes.md tests the hold or approval recognition.
- `claude plugin eval` exists: the skills page says it "runs each prompt in an isolated session with and without the plugin".
- The expected outcomes for prompts (i)–(iv) match l.24, l.28, l.42 and l.50.
- Caveat: there is no documented tool-less Codex mode, so "tools off" may be Claude-only.

F10. Split the long paragraphs into bullets (low): CONFIRMED. Optional. Word counts verified.

F11. Quote constraints verbatim (low): PARTLY.
- Clark and Brennan's "verbatim displays" are a specialized technique for content where the exact form matters: "names, addresses … dollar amounts".
- That supports quoting short, exact constraints. It does not support "grounding works best" with verbatim presentation in general.
- The 00-intent.md precedent is a written record, not a chat review.
- Acceptable as an optional low.

## 2. Fidelity audit verdicts I disagree with

A14 (silence, praise, ambiguity are not approval: "matches" via [15]): WRONG basis.
- In Clark and Brennan, praise-like acknowledgments are positive evidence. "First, acknowledgments are the most obvious form of positive evidence … These include continuers such as uh huh, yeah". "Initiating the relevant next turn is ordinarily an excellent piece of positive evidence."
- So under grounding theory, "looks good!" does ground understanding. The skill rejects it because approval is authorization, which grounding theory does not cover. The skill's own l.34 separates the two: "Approval agrees the working understanding and authority".
- Only "silence ≠ evidence" follows from [15]. Re-source the praise/ambiguity half to the Model Spec ("seek confirmation before proceeding"; confirmation "helps the user provide informed consent"). The verdict becomes loose.
- The same error appears in §2.1 ("the positive-evidence rule in operational form").

A13 (unconditional hold: "departs"): overstated.
- The Model Spec's scope-of-autonomy section models exactly this gate for multi-step real-world tasks. Its example stops before any action: "Before I start booking … does this sound right? … Should I go ahead and start making the reservations".
- The hold departs only for simple tasks. The Constitution text cited is limited to "simple agentic tasks".
- Better verdict: matches for consequential agentic tasks, departs for trivial ones. That also weakens F1's rationale.

A4 (bounded investigation: "matches" via DiscoBench): loose.
- DiscoBench's DG/SHG/STA are behavioral profiles assigned after the fact ("Pass rate by behavioral profile on the common subset (N=146)"), not interventions.
- The paper explains SearchHeavyGuess as "failing to escalate retrieval uncertainty into clarification". That supports "ask when ambiguity remains". It is not evidence that bounding investigation helps.
- Plan mode does not bound investigation either.

Other verdicts I checked against their sources and accept: A2, A3, A5, A8, A9, A10, A16, A18 and A20.

## 3. Citations

Fetched and confirmed as quoted, numbers included: [1]–[4], [6]–[16], [19]–[24], [26]–[29]. That covers every quote, statistic and attribution in sections 2–4 and 7 apart from the problems below.

Dead links: none. All 29 URLs resolved.

Problems:
- [15] for A14 and §2.1: misapplied. See section 2.
- [5] Aliannejadi: "over 170%" is from "experiments on an oracle model". The qualifier is dropped, so the figure reads as an achievable gain.
- [17] Build skills: §6.3 says ChatGPT implicit use is "governed by the same yaml". The page names only Codex for the flag: "When `false`, Codex won't implicitly invoke the skill". It says only generically that openai.yaml sets "invocation policy". The ChatGPT claim is unconfirmed; mark it [unverified] for P4.
- [18] codex #40600: the issue itself is about `debug prompt-input`. The picker-casing evidence is a comment, filed separately as #43727 ("TUI skill picker uses display_name casing"). Cite #43727.
- [25] Permission modes: "edits stay blocked until you approve the plan" drops the leading qualifier, "Except in interactive terminal sessions with bypass permissions available". Minor.
- [10] DiscoBench: observational profiles are presented as if they were compared strategies (§3, A4). Minor overstatement.

## 4. Missed issues

M1. should-fix: pre-approval investigation can still disclose data or spend money.
- l.18 defines a safe probe as leaving "the user's originals and external state unchanged".
- It does not cover requests that carry the user's private content off-device (a web search or fetch built from confidential material). The Model Spec lists "Making tool requests (including web GET requests) that contain sensitive user data" and "Direct expenditures" as side effects.
- It also does not cover running the user's code "against the copy" when that code calls paid or authenticated external APIs. Such a call can change nothing and still send data or incur cost.
- l.30 ("Judge inspection by its actual effects") helps only implicitly.
- This is where F3's concern actually belongs. Suggested addition to l.18: "It must also not send the user's private material to outside services or incur cost."

M2. should-fix (document): F7's probe gap is misstated, and the probe plan carries an ambiguity.
- Handoff item 2 (docs/handoff.md:20) already schedules an intent prompt in P2.
- P2's pass condition, "the right skill loads" from a natural-language prompt (spec §12.2), conflicts with explicit-only unless the prompt names the skill. F7(a) should fix P2's wording for dia-intent.

M3. nit: no explicit reply-language rule.
- dia-intent is the only one of the seven skills without one. The others say, for example, "Reply in the user's language" (dia-elenchus/SKILL.md:41) or "language of the user's latest message" (dia-refine/SKILL.md:37). dia-intent has only "Translate the labels consistently" (l.52), with no target language.
- Spec L6 says replies follow the user's language "as all reference skills already require"; for confirm-intent that is not literally true.
- In practice models follow the user's language anyway, hence nit.

M4. nit: possible tension for analysis tasks.
- l.23 asks the review to "State decisive observations, including calculations".
- l.30 says "Do not include a preliminary deliverable in the review".
- When the deliverable is itself a calculation or analysis, the line between the two is unclear. One clause would settle it: show only the calculations that decide scope or decisions.

M5. nit: `short_description` is 81 characters.
- OpenAI's skill-creator reference gives "Human-facing short UI blurb (25–64 chars)" (github.com/openai/skills, skill-creator/references/openai_yaml.md). Its generator rejects longer values.
- This is guidance, not a documented runtime limit. Every dia skill exceeds it (79–96 characters), so it is a repo-wide nit.

M6. nit: "direct follow-ups" is undefined.
- The description (l.3) extends the skill to direct follow-ups. The body never says whether a follow-up gets a full review and hold, or only the l.46 "re-agree the changed portion" path.
- The latter is probably intended. One sentence would make it explicit.
