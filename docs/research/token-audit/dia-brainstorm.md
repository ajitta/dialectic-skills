# Token audit: dia-brainstorm

Counted at `d5e9efa` (D23 skill text) with tiktoken `cl100k_base`. Claude tokens ≈ 1.5 × cl100k (`docs/token-cost.md`, n=2 calibration, ±10%). Read-only audit: no skill file was changed.

## Method

- **What each figure covers.** Claude Code injects the SKILL.md body without frontmatter on every invocation: 2,695 cl100k (the file is 2,963, and the frontmatter's 269 are out of scope). References load only when the model reads them. In the measured runs no brainstorm reference was read in the first turn (`docs/token-cost.md`). `brief-template.md` is needed at the end of a full session. `question-bank.md` is optional during probing.
- **Units.** Each sentence or bullet is one unit, and table rows are units too. A unit that mixes classes was split at the clause boundary (e.g. L66 tactic + rationale). Unit sums differ from the file totals by the newlines between units (SKILL.md body: 2,688 vs 2,695).
- **Classes.**
  - A: instruction.
  - B: rationale.
  - C: provenance or fidelity label, citation.
  - D: example.
  - E: redundant, either within the file or with a file loaded at the same time. A reference is always read while SKILL.md is in context, so text a reference repeats from the body is E.
  - F: meta. Here F includes headings, list numbers and table markup (structure), plus pointers.
- **Evidence used.**
  - `docs/spec.md` §5.3, §7.1 and D19–D23.
  - `docs/probes.md`: P7 routing, and P8's note that in headless runs references were sometimes unreadable.
  - `docs/research/dia-brainstorm.md` and its reviews: `review/`, `review/diff/`, `review/pass2/`, `review/lowfix/`.
  - Upstream `10-two-skills.md` §2 ("Honest labels") and the upstream SKILL.md.

## 1. Per-class totals (cl100k)

| File | A instr. | B rationale | C label/cit. | D example | E redundant | F meta | Sum of units | File |
|---|---|---|---|---|---|---|---|---|
| SKILL.md body (every invocation) | 2,209 (82%) | 46 | 113 | 59 | 139 | 122 (101 structure, 21 pointers) | 2,688 | 2,695 (body) |
| references/brief-template.md (on read) | 331 | 17 | 0 | 16 | 54 | 36 (structure) | 454 | 465 |
| references/question-bank.md (on read) | 127 | 0 | 36 | 412 | 105 | 42 (structure) | 722 | 725 |

Reading: the body is about 82% instruction. Its non-A text is 479 tokens. Of these, 101 are headings and markup, and 21 are the two reference pointers; both are needed. The labels (113) are all in L16 and are owner-required. Most of the E text either sits in the Pitfalls list (83) or is the brief's section list, which is load-bearing (43). So the purely informational text that could go is small. `question-bank.md` is mostly D by design ("Shapes, not scripts"), and the model adapts those shapes.

## 2. Candidates: SKILL.md (non-A units)

Tok = cl100k of the unit. "LB" = load-bearing.

| # | Unit (line) | Class | Tok | LB? Reason | Proposal | Risk / what would catch it |
|---|---|---|---|---|---|---|
| S1 | L16.0 "What this is: modern Socratic questioning (Richard Paul's six question types, from critical-thinking teaching) followed by brainstorming (diverge, then converge)." | C (+E) | 34 | Partly. The Paul label is the owner's honest label (upstream `10-two-skills.md` §2), and a user may ask "is this the Socratic method?". "From critical-thinking teaching" adds provenance only. "(diverge, then converge)" restates Steps 3–4. | **Shorten** (with S2, S3; text in §4). | Low. Every claim stays. Needs a light owner OK, because it rewords the owner's label text. |
| S2 | L16.1 "It borrows the Socratic spirit, which is asking rather than telling and drawing ideas out of the user, but it is not the strict method…" | C (+E) | 35 | The label "borrows the spirit, not the strict method" is load-bearing: it is the owner's label and the basis of the elenchus hand-off. The gloss "asking rather than telling…" restates L14 ("questioning partner, not an advisor"), Rule 3 and Step 3.1 (user-first). | **Shorten**: keep the label, drop the gloss. | Low. The stance is still stated at L14 and Rule 3. Removing the gloss loses the explicit "drawing ideas out" link to the midwife sentence that follows. The midwife sentence stands on its own. |
| S3 | L16.2 "If the user wants that strict method (…), switch to the `dia-elenchus` skill." | A (part E with the description and L37) | 40 | Yes. This is the only mid-session route to dia-elenchus; L37 covers only the opening request. | Keep; merge into the shortened S2 sentence. | None if the wording is kept. |
| S4 | L16.3 "Unlike the midwife of Plato's Theaetetus, who offers no ideas of his own, this skill adds its own labeled options in Step 3 and, if asked, gives a pick in Step 4." | C (behavior part E with Step 3.3, 4.3) | 44 | Yes. D19 requires the label (theme 4), and pass-2 review finding 5 fixed this exact wording ("if asked"). | **Keep verbatim.** Moving it would need a new reference file, which spec §5.3 does not list. Cutting it needs an owner decision under D19. | — |
| S5 | L20.2 "Two asks joined into one sentence still count as two: "where do they buy coffee now, and how do you know?" is bundling even with one question mark." | D (+A) | 34 | Yes. It defines bundling for the commonest violation. Pass-2 finding 1 was exactly a hidden second ask. | Keep. | — |
| S6 | L25.2 "Building is a separate request the user makes after the brief." | B | 12 | Yes, weakly. It tells the model that a later "now build it" is allowed. Without it, "Never implement" could turn into refusing all later work. | Keep. Optional cut: −12. | If cut, the model might refuse a build request made after the brief. Untested. |
| S7 | L30.1 "Options can arrive in any wording… (`--mode stress`, "go hard", "quick", "keep it light"); no parser exists, so infer them." | D + A | 33 | Yes. The no-harness rule (§7.1) means flags are just text, and the examples show natural-language forms. | Keep. | — |
| S8 | L66 "A belief nothing could disconfirm is a finding, not a strength." | B | 14 | Yes. It tells the model to record unfalsifiability as a finding, which feeds the open questions and the verdict. No rule lists that case. | Keep. | — |
| S9 | L66.1 "Required at least once in `stress`." | E (same rule at L72.1 "In `stress`, do at least one falsification probe.") | 8 | No. It is an exact duplicate in the same file. | **Cut** (keep the Rhythm copy, next to the question-the-question minimum). | None expected. The rule stays in Rhythm. |
| S10 | L71.2 "Repeating yourself in new words is not progress." | B | 10 | Yes. It defines what "move the thesis" excludes, which the switch rule depends on. | Keep. | — |
| S11 | L100.2 "It counts as a result, not a failure." | B | 10 | Yes. It makes "open" acceptable and counters agreement theater (research F9, sycophancy). | Keep. | — |
| S12 | L105 ": thesis before and after, decisions (confirmed or delegated), assumptions (…), open questions, options…, next step." | E (with brief-template.md) | 43 | Yes. It is the brief's fallback when references can't be read (P8 note; research README theme 5). | Keep. | — |
| S13 | L107.1 "Don't start building." | E (Rule 6) | 5 | Marginal. It sits at the end-of-answer rule. | Keep (too small to matter). | — |
| S14 | L111 Interview drift ("asking a fixed list ("users? budget? timeline?") regardless of answers. Each question must come from the last answer.") | E (Rule 1: "based on the last answer") | 30 | Yes. The named failure and its example show the shape to avoid, and that shape is the main failure mode of an LLM interviewer. It is a different angle from Rule 1, which is about one ask per message. | Keep. | — |
| S15 | L112.1 "Before Step 3, ask about the user's reasoning, not your alternative." | E (Rule 3) | 16 | Yes. It extends Rule 3 to suggestions phrased as questions. The D23 test-versus-replace sentence that follows relies on it (review F10). | Keep. | — |
| S16 | L114 Agreement theater | E (Sharpened condition) | 19 (+8 A) | Yes. It names the sycophancy failure (research F9). | Keep. | — |
| S17 | L115 "**Wall of text on a phone**: if a turn needs scrolling, cut it." | E (Rule 2: "A turn fits a phone screen without scrolling.") | 18 | No. The same rule is in the same file. | **Cut.** | Low. It drops one end-of-body reminder. No probe covers turn length: multi-turn brainstorm probes are open (research README "Still open" 1) and P2 (mobile) is owner-run. |
| S18 | L49.3, L75.1 pointers to question-bank and brief-template (21 tok) | F | 21 | Yes. They are the only read triggers. | Keep. | — |
| S19 | Headings, list numbers, table markup | F | 101 | Yes. The steps are referred to by number ("go to Step 5", "Step 4's questions"). | Keep. | — |

Not candidates even though they look informational:
- The SCAMPER parenthetical at L75 ("SCAMPER only in Step 3") is A. It was added for review M1 because references can be unreadable.
- The L37 routing paragraph (111) is A. It is the P7 / D21 / D22 fix.
- The Step 4 criteria examples at L89 ("cost, time, risk…") are A+D. The research found that recognition from a list recovers missed criteria (Bond et al., review F4).

## 3. Candidates: references (savings only when the file is read)

| # | Unit (file:line) | Class | Tok | LB? Reason | Proposal | Risk |
|---|---|---|---|---|---|---|
| Q1 | question-bank:57 "- **Edges** (Step 3): cheapest version · most extreme version · do nothing." | E (SKILL.md Step 3.2) | 19 | No. Step 3.2 in SKILL.md gives the same three edges, and the body is always in context when the bank is read. | **Cut.** | None expected. |
| Q2 | question-bank:39 "Concreteness: "Walk me through the first time, step by step."" and :44 "Necessity: "What breaks if we leave this out?"" | E (SKILL.md L62, L67 quote nearly the same lines) | 31 | Weak. The other four templates add a shape the body lacks; these two do not. | Optional cut. Not recommended: a gap in the tactic list may read as "these tactics have no template". | Low. |
| Q3 | question-bank:41 "(verbatim quotes only)" | E (Rule 4, L64) | 5 | Yes. It reminds the model at the moment it fills a template with quotation marks. | Keep. | — |
| Q4 | question-bank:46 heading "(pick at most two, only when the idea calls for one)" | E (L75) | 12 of 17 | Marginal. It is a local reminder. | Keep. | — |
| Q5 | question-bank:50–55 expert names (Peter Drucker … Kent Beck) | C | 36 | Yes. "Asked as a question in that person's spirit" needs the person. D23 chose full names (Kent Beck, not Aaron T. Beck), and D21 corrected Hickey's term. A user may ask whose lens a question is. | Keep. | — |
| Q6 | question-bank:61 "After two dry switches, say "I think we've hit the edge…" and move to Step 3." | E (L71.1) + D | 29 | Yes, in part. The quoted line is a phrasing the model copies. Review M2 aligned the target step with the body. | Keep. | — |
| Q7 | question-bank:8–35, :40–43 question and tactic shapes | D | 412 | Yes. They are the purpose of the file. | Keep. | — |
| B1 | brief-template:12 "After: <the user's restatement from Step 5, or else the working thesis (the user's own statement if none was formed); any tightening marked as yours; …>" | E (SKILL.md L97) | 36 of 59 | Partly. Two reviews put this fallback here on purpose (diff-review finding 1, pass-2 finding 3), to guard "invent nothing" at the point where the line is written. | Optional shorten to `- After: <the thesis after, as Step 5 sets it; any live risky assumption written in as a condition, e.g. "…, piloted for one month first">` (−21). Not recommended. | Medium-low. It reopens a reviewed fix, and the model would have to look back to Step 5 for the fallback. |
| B2 | brief-template:3 "(code blocks scroll sideways on phones)" | B | 7 | Yes, weakly. It explains why the rule is limited to "in chat", which keeps saved files free. | Keep. | — |
| B3 | brief-template:3 "so the reader still sees they were considered" | B | 9 | Yes. It explains why "none" lines are kept instead of trimmed. | Keep. | — |
| B4 | brief-template:3 "Fill every section from the user's answers only," and :41 "Without that, it is `open`." | E | 18 | Yes. They are local reminders of the two output rules most at risk (invent nothing; refuted). | Keep. | — |
| B5 | brief-template:33 "e.g. "no counterexample pressure", "no outside viewpoint"" | D | 16 | Yes. The model copies these for "Not tested". | Keep. | — |

## 4. Recommended set

Exact new text for **S1–S3** (replaces all of SKILL.md L16):

```text
What this is: **modern Socratic questioning** (Richard Paul's six question types) followed by brainstorming. It borrows the Socratic spirit, not the strict method of Plato's dialogues: if the user wants that strict method ("what is X?", contradictions built from their own agreed premises, aporia, no advice at all), switch to the `dia-elenchus` skill. Unlike the midwife of Plato's Theaetetus, who offers no ideas of his own, this skill adds its own labeled options in Step 3 and, if asked, gives a pick in Step 4.
```

What this keeps and drops:
- Kept: every label (Paul's six types, "modern Socratic questioning", "borrows the spirit, not the strict method", the D19 midwife sentence, verbatim) and the elenchus route.
- Dropped: "from critical-thinking teaching", "(diverge, then converge)", and the "asking rather than telling…" gloss.
- If the owner wants "from critical-thinking teaching" kept, the saving drops to 23.

| Item | Change | cl100k saved | ≈ Claude | When |
|---|---|---|---|---|
| S1–S3 | L16 shortened as above | 28 | 42 | every invocation |
| S9 | delete " Required at least once in `stress`." (L66) | 8 | 12 | every invocation |
| S17 | delete the "Wall of text on a phone" pitfall (L115) | 18 | 27 | every invocation |
| **SKILL.md total** | | **54** (2.0% of the 2,695 body) | **≈ 81** | every invocation |
| Q1 | delete the Edges bullet (question-bank:57) | 19 | 28 | only when the bank is read |

- If the owner declines the L16 rewording, the safe remainder (S9 + S17) is 26 cl100k (≈ 39 Claude) per invocation.
- Optional items add up to 71 cl100k: S6 (−12), Q2 (−31), B1 (−21), B2 (−7). I do not recommend them, for the reasons in the tables.
- In a multi-turn session the body stays in context, so the saving recurs on each turn as cached input, which is cheaper than the first write.
- Any of these edits is a skill-file change. AGENTS.md and spec §12.1 call for a version bump, or the pre-release exception noted in the handoff.

## 5. What to keep and why

- **All of L16's labels and the midwife sentence.** These are owner-required honest labels: upstream "Honest labels" and D19 theme 4. The skill has no `theory.md`-style reference to move them to, and adding one changes spec §5.3's reference list. For about 40 tokens, keeping them in the body is cheaper than a new file plus a read condition.
- **Everything that serves as the no-reference fallback (spec §7.1, P8).**
  - The brief's section list (L105).
  - "SCAMPER only in Step 3" (L75).
  - The six-type table.
  - The tactic one-liners. They carry the shapes when question-bank.md can't be opened.
- **The rationales S8, S10 and S11.** Each tells the model how to treat a case no rule lists: an unfalsifiable belief, a reworded repeat, an open verdict.
- **Pitfalls S14–S16.** Each names a failure mode the research tied to evidence: interviewer drift, advisor drift as F10, sycophancy as F9. Each also adds something its rule lacks.
- **The question-bank D text and expert names.** That is the file's job. The names were corrected in D21 and D23.
- **Pointers and step headings.** Other rules refer to steps by number. The pointers are the only read triggers.

## 6. Risk and verification

- **Coverage.** No current probe exercises a brainstorm dialogue. P7 checks only which skill loads; the edits touch neither the description nor the routing paragraph L37, so P7 cannot regress. P8 was run for refine and iterate, not brainstorm. Multi-turn brainstorm probes are listed as open.
- **Suggested checks if the set is applied.** Run both arms from a neutral directory, n≥3 each:
  1. A `stress` session of 5+ turns. Check that at least one falsification probe happens (S9) and that every turn fits one phone screen (S17).
  2. A by-name invocation with "do it Socratically" and no request for options. The first message should carry the dia-elenchus line (L37). A mid-session "make me define it, no advice" should switch to dia-elenchus (S3).
  3. A user who asks "what method is this?". The answer should name Paul's six types, say it is not Plato's strict method, and mention that the skill adds its own options (S1, S2, S4).
- **Overall.** Expected behavior change: none for S9 and Q1; low for S17 and S1–S3. The saving is small (about 2% of the body). This skill's body is already almost all instruction, and most of its non-instruction text is load-bearing.
