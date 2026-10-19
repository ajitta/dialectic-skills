# Token audit: dia-intent

| | |
|---|---|
| Files | `skills/dia-intent/SKILL.md` (79 lines; byte-identical to `plugins/dia/skills/dia-intent/SKILL.md`). No `references/` (spec §5.1: "References: none at present"). `agents/openai.yaml` and the frontmatter are out of scope. |
| Tokenizer | tiktoken `cl100k_base`. Claude ≈ cl100k × 1.5 (`docs/token-cost.md`, n=2, ±10%). |
| Counted text | The body after the closing `---` (what Claude Code injects on invocation): **1,782 cl100k** (whole file 1,896). |
| Status | Audit only. No skill, spec or doc file was edited. |

## 1. Method

- The body was split into 94 units: one per sentence or bullet, with parenthetical examples and restating clauses split off as their own units. Every unit was located in the body in order; the only text between units is list markers and whitespace.
- Each unit was tokenized on its own. The units sum to 1,779; the remaining 3 tokens are list markers and line breaks.
- Classes: **A** instruction (changes behavior), **B** rationale, **C** provenance or fidelity label or citation, **D** example, **E** redundant (restates something in the same file), **F** meta (headings, invocation guard).
- Evidence used: `docs/research/dia-intent.md` (research, R), `docs/research/review/dia-intent.md` (review, Rv), `review/diff/`, `review/pass2/`, `review/lowfix/dia-intent-{applied,review}.md`, `docs/probes.md`, spec D19–D23 and §5.1, §7.1.

## 2. Per-class totals (SKILL.md body)

| Class | Units | cl100k | Share |
|---|---|---|---|
| A instruction | 64 | 1,395 | 78.3% |
| B rationale | 4 | 60 | 3.4% |
| C provenance / citation | 0 | 0 | 0% |
| D example | 10 | 109 | 6.1% |
| E redundant | 12 | 186 | 10.4% |
| F meta / headings | 4 | 29 | 1.6% |
| list markers, line breaks | – | 3 | 0.2% |
| **Body** | 94 + markup | **1,782** | 100% |

References: none, so no per-reference table. Worst-case cost per invocation = the body.

**Headline.** The owner's concern (history, citations, scholarly attributions, method lineage) does not apply to this skill: the body has **no class-C text at all**. The research found no academic method behind it, so it needs no label (R §4: "Since it claims no named method, no relabelling is needed"). The diff reviews confirm that "the diff adds no method claims or citations" (`review/diff/dia-intent.md`, `review/lowfix/dia-intent-review.md`). Lineage lives only in `metadata.lineage` in the frontmatter, which is out of scope and is not injected by Claude Code. The D19–D23 "labels" for this skill (re-derived values; unverified assumptions) are output labels that the model must write, so they are class A, not provenance. The only reducible text is restatement (E) and a few example or rationale fragments, so the saving is small.

## 3. Candidate list (every non-A unit)

Line numbers refer to the current SKILL.md. LB = load-bearing.

| # | Unit (line) | Cl. | Tok | LB? Reason | Proposal | Risk |
|---|---|---|---|---|---|---|
| 1 | "A request to analyze, review, or edit this skill is not a request to run it." (l.12) | F | 19 | Yes. It is the only guard against the hold firing when a user edits or reviews the loaded skill (R §1 "Meta guard"); it is unique to this skill among the seven. | keep | – |
| 2 | Headings `## Before Starting`, `## Recognizing Approval`, `## Response Format` (l.14, 50, 63) | F | 10 | Yes. They give structure; "Use the sections below" (l.65) refers to the format section. | keep | – |
| 3 | "(such as a name, amount or date)" (l.16) | D | 10 | Yes. It sets the scope of "short exact constraints". The review narrowed F11 to exactly these content types (Rv F11, Clark & Brennan's "names, addresses … dollar amounts"). Without it the quote rule would read as general verbatim restating. | keep | – |
| 4 | "such as a copy of the relevant files," (l.20) | D | 9 | Yes. It gives the concrete form of "separate temporary location", which is what the model does on a coding surface. | keep | – |
| 5 | "including their workspace, accounts, and shared systems." (l.20) | D | 10 | Yes. It defines "external state". Without it, accounts and shared systems (the churn report's Drive and Gmail, probes Part A) are easy to read as outside scope. | keep | – |
| 6 | "A probe's result is evidence for the review, not a draft deliverable:" (l.22) | B | 16 | Yes. This rationale lets the model apply "report what it showed, not the change it used" to cases that are not listed (a probe that produced a working fix). pass2 rewrote it on purpose to fix the pronoun chain. | keep | – |
| 7 | "Do not investigate exhaustively." (l.23) | E | 6 | Weak. It restates "bounded" (l.18) and the stop rule just before it. | optional cut (O2, −6) | Over-investigation before approval. Low; the stop rule remains. Probe: dia-intent behavior run, churn prompt. |
| 8 | "(such as a date's weekday or a total)" (l.29) | D | 11 | Yes. It is the concrete trigger for the quick-computation check, and the lowfix review's F11 finding turns on exactly the weekday case (24 October 2026 is a Saturday). | keep | – |
| 9 | "(ones no available source holds, such as what their team handles or a booking they made)" (l.30) | D | 19 | Yes. It defines "facts only the user can supply" as distinct from investigable facts, which is the core of selective asking (R A8). The model copies the pattern. | keep | – |
| 10 | "An empty decision list is normal;" (l.30) | B | 7 | Yes. It is the D23 anti-padding rule in the review's minimal form (Rv F2); R §6.1 item 1 names manufactured decisions as the main failure mode. | keep | – |
| 11 | "(a request to send settles sending without a preview)" (l.31) | D | 11 | Yes. It is the only worked case of "the request settles it", the pseudo-check-in failure (R [26]). | keep | – |
| 12 | "; if they do, it belongs in evidence and assumptions." (l.31) | E | 12 | No. Item 2 already says (l.29): "Points the request, conversation, or materials settle … belong here … not in questions." | **cut (R2, −11)**; new text: "…do not already settle it (a request to send settles sending without a preview). Your own default…" | A settled point is dropped instead of being moved to evidence. Low: l.29 states where it goes. Probe: Part A irreversible-delete prompt (the request settles the delete). |
| 13 | "(such as a backup)" (l.33) | D | 6 | Yes. Probes Part A: the production-delete run "offered a backup", which is the behavior this example models. | keep | – |
| 14 | "Facts you can investigate and choices already delegated are not reasons to propose this." (l.37) | E | 16 | No. The dependency rule applies only to *open decisions*, and item 3 already excludes investigable facts ("Investigate available factual questions instead of asking them") and delegated choices ("Your own default settles an item only when the choice was delegated…"). Such items can never trigger l.35. | **cut (R1, −15)** | An interview is offered for investigable dependencies. Low, and only on a rare path. No probe covers dependent decisions; add one to the dia-intent behavior probe (R F9). |
| 15 | "delegating the dependent choices or narrowing the scope may resolve the dependency instead." (l.38) | B | 15 | Yes. It names two alternatives the model can offer instead of switching. Without it the only exits are "switch" or "ask the first decision". | keep | – |
| 16 | " and omit empty sections." (l.42) | E | 5 | No. It also appears as "omitting empty sections" (l.65) and "Omit if nothing remains" (l.76). | optional cut (O1, −4); new text "Include only material items." | None expected; l.65 keeps the rule. |
| 17 | "Do not include a preliminary deliverable in the review;" (l.44) | E | 11 | Partly. It overlaps "substantively draft its deliverable" in the same paragraph, but the D23/M4 clause after the semicolon needs it as its anchor. | keep | – |
| 18 | "Approval agrees the working understanding and authority; it does not establish that the explanation is true or the requirements complete." (l.48) | B | 22 | Yes. It is the anti-sycophancy guard (R A17, [29]), and l.56 (a correction that conflicts with evidence) and l.61 (update when evidence changes) rely on it. | keep | – |
| 19 | "(for example, \"investigate only\")" (l.54) | D | 9 | Yes. It is the phrase the model matches a partial approval against, and the next sentence ("For an investigation…") refers back to it. | keep | – |
| 20 | "For an investigation, it lifts the limit … but the isolation rule and the rule against sending private material out or incurring charges still apply." (l.54) | E | 33 | Yes. It restates l.20–21, but the lowfix review (finding 2) required this explicit wording after the bullet split weakened the earlier pointer. It is the only text that keeps the no-data-out rule (D20/D21) in force after an "investigate only" approval. | keep | – |
| 21 | "It does not authorize changing user assets, publishing, deploying, or other remaining actions." (l.54) | E | 17 | Weak in logic: "approval of that part alone" plus the hold list (l.44) already imply it. Strong in consequence: the failure it prevents is an unapproved write or deploy. | keep (O3, −17, not recommended) | If cut: action after a partial approval. High cost, and no probe covers partial approval. |
| 22 | "(for example, a backup made only for the pending change)" (l.61) | D | 13 | Yes. "work whose result or purpose depends on it" is abstract, and this is the only worked case. | keep | – |
| 23 | " omitting empty sections." (l.65) | E | 5 | Yes, as the single home of the rule if O1 is taken. | keep | – |
| 24 | Template "[Intended outcome, scope, and completion criteria.]" (l.70) | E | 10 | No. It is a shorter restatement of item 1 (l.28) under the identical heading. | **cut (R3a, −10)**; keep the bold label | The model writes item 1 from the template alone and drops the inferred-conditions rule. Very low: the bracket did not carry that rule anyway. |
| 25 | Template "[Decisive findings (marked re-derived …), supported inferences, material assumptions, settled points with their source, and the options you will use for delegated choices.]" (l.73) | E | 39 | Partly. Everything restates item 2 (l.29) except the slot cue for "re-derived", the D19 output label, which the diff review asked to show in the template (`review/diff/dia-intent.md` finding 3). | **shorten (R3c, −22)** to "[As item 2; mark values worked out without a tool as re-derived.]" | Settled points or delegated-choice options drop out of the Evidence section. Low–medium. Probe: dia-intent behavior run, adding a prompt that delegates one choice and contains a date or total; check for "re-derived" and for "the option you will use". |
| 26 | Template "[Only what remains open, with its effect. Omit if nothing remains.]" (l.76) | E | 16 | No. It restates item 3 ("explain each one's effect"), l.30 ("An empty decision list is normal"), l.42 and l.65 (omit empty sections). | **cut (R3b, −16)**; keep the bold label | Padding of the decision list. Low: three other rules cover it. Probe: Part A rename prompt (expect no decisions). |
| 27 | "(such as a budget, count or stopping point)" (l.79) | D | 11 | Yes. It is the D23 limit for open-ended work; without the examples "limit" is vague (Rv F4). | keep | – |
| 28 | ", any requested step that cannot be undone and the safeguard the user can ask for" (l.79) | E | 16 | Yes. It restates l.33, but l.33 says "say in the confirmation", and this is that slot. Probes Part A observed the behavior (irreversibility stated, backup offered). | keep | – |

### Instruction blocks considered for a move (class A, outside the informational brief)

| Block | Tok | Proposal | Why |
|---|---|---|---|
| Probe-isolation bullets, l.20–24 | 230 | **keep in SKILL.md** | Only tool surfaces use them, and those are exactly where `Read` may need approval and `references/` may be unreadable (`docs/probes.md` l.117). R §6.2: "They are still worth keeping in the body: P8 showed headless runs sometimes cannot open `references/`." A missed read would let a probe touch the user's originals or send data out (D20/D21). |
| Dependent decisions, l.35–40 | 198 | not recommended; owner decision if wanted | Could move to `references/dependent-decisions.md` with a 63-token body stub that keeps the safety-relevant part (ask the first decision now, defer the dependent ones, no proceed request for work that depends on them) and a read condition ("If open decisions depend on each other…"). Net −135 per invocation. Against it: spec §5.1 says no references (a spec change); the interview offer, the skill offer and the return-to-review rule would be lost when the reference is unreadable (P8 condition); and the rare path would then cost more (body stub + read ≈ 260+). |

## 4. Recommended set

| Id | Change | cl100k saved |
|---|---|---|
| R1 | Cut l.37 "Facts you can investigate and choices already delegated are not reasons to propose this." | 15 |
| R2 | Cut l.31 "; if they do, it belongs in evidence and assumptions." (end the sentence after the parenthesis) | 11 |
| R3a | Cut the template bracket l.70 | 10 |
| R3b | Cut the template bracket l.76 | 16 |
| R3c | Shorten the template bracket l.73 to "[As item 2; mark values worked out without a tool as re-derived.]" | 22 |
| **Total** | measured by re-tokenizing the edited body | **74 cl100k (4.2% of the body) ≈ 110 Claude tokens per invocation** |

Optional, with little gain: O1 (−4) and O2 (−6) bring the total to **84 cl100k (4.7%)**. Not recommended: O3 (−17, safety emphasis on an unprobed path) and the dependent-decisions move (−135 net; spec change, P8 risk).

Context: the D23 batch added 134 cl100k to this body (1,762 → 1,896 file; `docs/token-cost.md`), and the recommended set takes back about half of that without removing any rule or label. In a multi-turn session the body is paid once and then stays as cached input, so the per-turn effect is smaller still.

**Constraints checked**
- No D19–D23 label is removed. The "re-derived" output label stays in item 2 (l.29) and in the shortened template (R3c). The "unverified assumption" wording, D20's sent/spent and recipient, and D23's limit for open-ended work are untouched.
- Nothing moves to a reference, so the skill keeps working when references cannot be opened (spec §7.1, P8).
- Changes to the frontmatter or description: none.
- Process (AGENTS.md, spec §12.1): even a no-behavior-change edit to SKILL.md is a skill-file change. Before the first release it may keep 0.1.0 / 1.0.0 (`docs/handoff.md`, State). Regenerate `plugins/dia/` and the zip. R3 alters the response template, so a D-row noting "template brackets reduced to non-redundant cues; no rule change" keeps spec §5.1 accurate.

**Verification after applying**
- Re-run the probes Part A dia-intent cells (rename, "report on our churn", irreversible production delete; skill named, n=3). Expect the same review shapes, a hold, no Drive/Gmail search before approval, and the irreversibility plus safeguard in the Confirmation.
- Add one cell with a delegated choice and a date or total (checks R3c) and one with dependent decisions (checks R1).
- That run would also close R F9 for the current text: the existing run is at `7115d2a`, before D21 and D23 (`review/lowfix/dia-intent-review.md`).

## 5. What to keep, and why

- **All class-A text (1,395 tokens, 78%).** This is the review procedure, the hold, approval recognition and re-agreement. Each sentence was added or kept for a reviewed reason (R §4 A1–A20; D19–D23), and the skill has no references to fall back on.
- **All examples (D, 109 tokens).** Each parenthetical sets the scope of an abstract rule (short exact constraints, external state, facts only the user holds, settled-by-request, safeguard, dependent purpose, open-ended limit). Several match behavior seen in probes Part A: the backup offer, and the data-source decision with no pre-approval Drive search.
- **The four rationale units (B, 60 tokens).** Each one lets the model handle cases the rules do not list: probe output is not a deliverable; an empty decision list is normal; delegating or narrowing can dissolve a dependency; approval is not truth. The owner deferred adding the one rationale the research asked for (F1, why the hold is unconditional; `docs/research/README.md` § Still open, item 2), so the skill already carries only rationale that does work.
- **The l.54 restatements (50 tokens).** The no-data-out and no-action-after-partial-approval wording is deliberate redundancy: a reviewer required it, and it guards the costliest failures.
- **The meta guard (l.12) and the headings.**
