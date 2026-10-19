# dia-refine — token audit

Status: audit only; no skill, spec or probe file was changed. Tree: `d5e9efa`. File: `skills/dia-refine/SKILL.md` (70 lines). Line refs `:N` are to that file.
Counts: tiktoken `cl100k_base`. Claude tokens ≈ cl100k × 1.5 (`docs/token-cost.md`, n=2 calibration, ±10%).

## 1. What loads

- On invocation Claude Code injects the SKILL.md body without frontmatter: **1,929 cl100k** (the whole file is 2,129; the 200-token frontmatter, including the description, is out of scope).
- **dia-refine has no reference files** (`skills/dia-refine/` holds only SKILL.md and `agents/openai.yaml`; spec §5.6 "References: none at present"). So the body is the whole per-invocation cost and also the worst case. Nothing can be "moved to a reference" without creating a new file.
- The description is in the always-on skill listing on every surface, so body text that repeats it is paid twice when the skill loads.

## 2. Per-class totals (SKILL.md body)

The body was split into 60 units (a sentence, a clause carrying a separate function, a bullet, a heading or the example block). Units were tokenized one by one; they sum to 1,922, and the other 7 tokens are newline joins.

| Class | Meaning | Units | cl100k | Share |
|---|---|---|---|---|
| A | instruction | 30 | 1,335 | 69.5% |
| B | rationale | 7 | 147 | 7.6% |
| C | provenance / citation | 2 | 52 | 2.7% |
| D | example | 2 | 175 | 9.1% |
| E | redundant | 8 | 124 | 6.5% |
| F | meta (headings, invocation forms, pointers) | 11 | 89 | 4.6% |
| | joins | | 7 | 0.4% |
| **Total** | | 60 | **1,929** | |

References: none, so 0 tokens in every class.

The body is mostly instruction. Purely informational text (C plus non-load-bearing E/F) is about 150 tokens. The rest of the B and D text is load-bearing (§3).

## 3. Every non-A unit

"LB" = load-bearing. Tokens are for the unit alone.

| # | Unit (line) | Cls | Tok | LB? Reason | Proposal | Risk / probe |
|---|---|---|---|---|---|---|
| 1 | :14 ", not the iterative Self-Refine loop (Madaan et al., 2023, arXiv:2303.17651)." | C | 30 | Partly. An honest-method label recorded in D23 ("the body labels the skill as not the iterative Self-Refine loop"). It also backs up "single-pass" against the "refine → loop" association. A user may ask what the method is. | Keep the label. Optional (owner): drop the arXiv ID → "(Madaan et al., 2023)". | Cutting the label needs an owner decision (D23). If the ID is dropped and a user asks for the paper, the model may supply an ID from memory (a fabrication risk). No probe covers this. |
| 2 | :14 "and a request for review is not in itself a sign of error." | E | 14 | Yes, as the first anti-flip statement, read before the procedure. Same point as :67 (twice). The anti-flip rule is the best-supported rule in the skill (research A12: Sharma; Laban FlipFlop). | Keep. Cut the in-bullet duplicate at :67 instead (#21). | — |
| 3 | :14 "The skill must work in a chat with no tools (mobile apps included)," | B | 15 | Weak. It explains why verification is conditional. Step 3 already encodes the whole behavior: "this needs no tools", "if a search … tool is available", unchecked items "stay as drafted and are marked unverified". | **Cut** together with #4. | Medium-low. A tool-less model might stop or ask for tools instead of completing. **P8** (`--tools Skill`) catches this. |
| 4 | :14 "so verify only as far as the available tools allow and leave the rest marked unverified." | E | 18 | No. It restates :31. It also caused the tension recorded in pass-2 nit 3 ("leave the rest marked unverified" vs the final-only closing line, which marks only items that bear on the conclusion). | **Cut** (with #3). | Same as #3. It also removes a recorded inconsistency. |
| 5 | :18 "for example `dia-refine — check the numbers` or `dia-refine for tone`" | D | 19 | Some. It shows that the text after the marker is criteria, in two shapes (dash and prose). | Keep. Dropping "or `dia-refine for tone`" saves 8, which is not worth the churn. | — |
| 6 | :18 "`/dia:dia-refine`, `$dia:dia-refine`, `$dia-refine` and `@dia-refine` also count." | F | 29 | Partly. :37's language fallback refers to "one of the names under Invocation" (D22: "the language fallback covers every invocation name"). Spec §5.6 lists these forms as required. Routing does not read the body. | Extended set (owner): cut it and change :37's parenthesis to "(the skill's name in any form)". Net −36. | Low. On a bare `$dia:dia-refine` message the model must still recognise the name as an invocation, which the new wording covers. Needs a spec §5.6 note. **P6** (first-word) and a P3-style `$dia:dia-refine` run would catch a change. |
| 7 | :19 Natural-language trigger phrases | F | 30 | No. They are routing triggers. After loading they change nothing, and the description carries the same phrases on every surface. "Final version only" mode is defined at :40 on its own terms. | **Cut** the bullet. | Low. Routing is description-only, so **P6/P7** are unaffected. If a "give me only the final version" request were no longer recognised as final-only mode, a final-only probe would show it; none exists (pass-2 review: "the 'final version only' mode never [probed] at all"). |
| 8 | :21 "A dia-refine mentioned in passing in the middle of a sentence is not an invocation." | E | 19 | No. The description says the same thing almost word for word, which is what prevents loading (P6 cell 4: no skill loaded). | **Cut**. Keep :21's dia-iterate sentence. | Low. If the skill is ever loaded on a passing mention, the body no longer tells the model to back out. **P6** cell 4 catches this. |
| 9 | :30 "Starting out to "find only the important ones" makes you find fewer," | B | 15 | Yes. Spec §5.6 requires this reason to be kept, and review F13 refused to drop it. It also extends to criteria-led reviews ("check the numbers" still means list every number). | Keep. | — |
| 10 | :30 "so list every candidate and filter in step 4." | E | 11 | Partly. "List every candidate" repeats the step title. "Filter in step 4" names where filtering happens. | Extended set: rewrite #9+#10 as `Aiming to "find only the important ones" finds fewer; filtering is step 4's job.` (−5). | Negligible. The reason stays. |
| 11 | :31 "the more familiar it feels, the more plausible a stale answer sounds." | B | 14 | Yes. It extends "familiar name" to versions, dates and APIs. It is one of the four upstream reasons that spec §5.6 keeps (research §5.1). | Keep. | — |
| 12 | :31 "(in "final version only" mode, in the closing line when it bears on the user's conclusion)" | E | 22 | Yes. It repeats :40, but it sits where the mark-placement decision is made. P8 observation (a), an inline "(unverified; …)" note, was this exact failure, and final-only mode has never been probed. | Keep. | Cutting it (−21) would re-open P8 (a) in an unprobed mode. |
| 13 | :31 "a subagent is normally the same model, so it adds calls without giving a stronger basis than your own re-derivation." | B | 26 | Yes. It tells a subagent-capable host (Claude Code, Codex) why a "second opinion" tool or worker does not count, which covers cases the rule does not list. D23 records it as an owner-accepted addition. | Keep. | — |
| 14 | :33 "Rechecking again and again on your own judgment alone adds cost and tends not to improve correctness; on reasoning it can make it worse" | B | 26 | Yes. It scopes "iterate only on new evidence" and keeps step 3's single re-derivation legitimate. The wording was set by the lowfix diff review (finding 2). | Keep. | — |
| 15 | :33 "(Huang et al., ICLR 2024, arXiv:2310.01798)." | C | 22 | Partly. D23 records the body citation, and dia-iterate cites the same way. It does not change behavior. | Keep. Optional (owner): drop the arXiv ID (with #1, −20 total). | As #1. |
| 16 | :40 "(see Safeguards)", "(see below)" | F | 10 | Some. In a 160-token sentence they point to where "matter of taste" and file-target sources are defined. | Keep. | — |
| 17 | :41 "Do not make edits just to have something to show." | E | 11 | Yes. It is the concrete form of the no-over-correction safeguard, placed at the "nothing to fix" decision. | Keep. It is the one to keep if #22 is cut. | — |
| 18 | :42 "The (re-derived) tag in ① is how the defect list shows this: the basis is your own working, not an outside check." | B | 30 | Yes. It resolves the contradiction the diff review raised (M2) between "do not declare the revision better on your own judgment" and listing a re-derived change under "① Confirmed errors". D22 records it. | Keep. | — |
| 19 | :47 "Example defect list:" | F | 4 | Yes, as the label for #20. | Keep. | — |
| 20 | :49–63 example defect list | D | 156 | **Yes, strongly.** The model copies it: the basis tags "(tool; source: link)" and "(re-derived: …)", the ④ suspected-correction form (F12, D23), the grouped "Three benchmark figures" form that :40 quotes, and the "Incidental" line. It was de-fenced on purpose (F11). In the P6 run at `6882022` the output carried "(re-derived)" under ① as shown. With no reference file, and P8 runs that cannot open references, it must stay in SKILL.md. | Keep in full. | Removing any line weakens a specific format rule. P6 (① tag), P8 (④ form). |
| 21 | :67 "It is a request for review, not an error report." | E | 12 | No. It restates the sentence just before it in the same bullet, and :14. | **Cut**. | Low. Anti-flip is still stated at :14 and :67 ("Being invoked is not a signal of error" plus the flip sentence). No dia-refine pushback probe exists; one would catch it (see §6). |
| 22 | :68 "No over-correction. Do not read the request as "something must change"." | E | 17 | Weak. The same rule is at :14 ("Change is not improvement in itself") and :41. But spec §5.6 names "the safeguards" among what the translation keeps. | Extended set (owner): cut. | Low behaviorally. It needs the owner's assent, because it removes a whole upstream safeguard bullet. |
| 23 | :67 "Flipping a correct answer under pressure that has no specific grounds is the failure this procedure exists to prevent." | B | 21 | Yes. It is the upstream anti-flip reason (spec §5.6). It defines what "grounds" means for pushback cases the rules do not list, and it ties to :32's "bare statement … is review criteria". | Keep. | — |
| 24 | Headings (`#`, six `##`) | F | 16 | Yes. :37 and :40 refer to "Invocation" and "Safeguards" by name. | Keep. | — |

## 4. Recommended set

Core set (no owner decision needed; each removal repeats text that stays in the body or the description):

| # | Change | cl100k saved |
|---|---|---|
| 3+4 | Cut :14's last sentence ("The skill must work in a chat with no tools … marked unverified.") | 33 |
| 7 | Cut :19 (natural-language triggers) | 30 |
| 8 | Cut :21's first sentence (passing mention); keep "Requests for several rounds belong to `dia-iterate`, not to this skill." | 18 |
| 21 | Cut :67's "It is a request for review, not an error report." | 12 |
| | **Core total** (measured on the edited body) | **93** (1,929 → 1,836, −4.8%; ≈140 Claude tokens) |

Extended set (each item needs an owner decision, because it touches text that spec §5.6 or D22/D23 names):

| # | Change | cl100k saved | Why owner |
|---|---|---|---|
| 6 | Cut :18's form list; :37 → "(the skill's name in any form)" | 36 | Spec §5.6 lists the forms; D22 records the fallback over every name |
| 22 | Cut :68 | 17 | A whole upstream safeguard bullet (spec §5.6 "the safeguards") |
| 1+15 | Drop both arXiv IDs, keep authors and years | 20 | D23-recorded citations; fabrication risk if a user asks for the paper |
| 9+10 | Shorten the step-2 reason | 5 | Reason kept, wording changed |
| | **Core + extended** | **171** (1,929 → 1,758, −8.9%; ≈255 Claude tokens) |

Not recommended:
- Cutting the two method citations outright (−50). That removes an honest label D23 placed in the body; it needs an owner ruling.
- Moving them to a new `references/sources.md`. That adds a file plus a read-condition pointer (~15 tokens), so the net is about −35. It also fails wherever references cannot be opened (P8 headless note), and it adds packaging for a 50-token saving.

Version note (AGENTS.md): any edit keeps plugin 0.1.0 and `metadata.version` 1.0.0 before the first release, then `python tools/package.py` regenerates `plugins/dia/`.

## 5. What to keep and why

- **All A text (1,335).** Each sentence is a rule a probe or review traced to behavior:
  - the P8 fix: recall is not verification, the three confirmed bases, ④ with the suspected correction, side-by-side only for re-derivation;
  - D19–D23 additions: basis tags, the closing line and its contents, file-target sources, the bare-claim rule, the creative-work basis, the language fallback;
  - the upstream steps and safeguards that spec §5.6 requires.
- **The example (156).** It is the cheapest way the format rules reach the model, and it is the only format template, since there is no `output-template.md`.
- **Rationales #9, #11, #13, #14, #18, #23 (141).**
  - Spec §5.6 requires the upstream reasons (#9, #11, #14, #23).
  - D23 records #13 as an accepted addition. D22 records #18 as the fix for a contradiction.
  - Each tells the model how to treat a case the bare rule does not list: criteria-led reviews, familiar versions and APIs, subagent-capable hosts, repeated user-requested rechecks, re-derived ① items, bare pushback.
- **The Self-Refine label and Huang citation (52).** They are honest-label text the owner placed in the body (D23). Only the arXiv IDs are optional.
- **The :31 final-only parenthesis (22).** It is redundant on paper, but it guards the P8 (a) inline-mark failure in a mode that has never been probed.

## 6. Verification needed after any cut

- **P8** (`--tools Skill`, the Eiffel/GIL/17×23 draft), 3 runs: the run completes, the GIL sentence goes to ④ with the suspected correction, the revision keeps the draft's wording and carries no inline mark. This covers #3/#4.
- **P6** four prompts: `dia-refine — check the numbers` still tags (re-derived) under ① and shows original and revised values; a mid-sentence mention loads nothing. This covers #7/#8, and #6 if taken.
- **Gaps that no current probe covers.** Proposed new cells, n≥2:
  - a "give me only the improved final version" request: revision only, at most one closing line, no inline marks;
  - pushback on a correct draft (`dia-refine — I think the total is wrong`, with the total correct): the draft is kept, with "nothing needs fixing" and a reason. This covers #21/#22.
- Cross-skill note: the Invocation-section cuts (#6–#8) apply equally to the other six skills, if they repeat their description the same way. Decide them once for all seven, so that spec §5's invocation lists stay consistent.
