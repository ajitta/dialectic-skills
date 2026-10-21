# Design note: dia-conjecture

New skill for plugin 1.3.0. Method: Lakatos's *Proofs and Refutations*, ch. 1 sections 1-6 and Rules 1-4, as a multi-turn counterexample dialogue on a strictly universal claim the user holds. Sources: `docs/research/candidates/modern-dialectic.md` (section 2.3, the Popper fold in 2.4, the sketch in section 4) and the independent reviews `review/modern-dialectic.md` and `review/index.md` (candidates review of 2026-10-21; diff review `review/diff/conjecture.md`). Where the research and the review differ, the review was followed.

Files: `skills/dia-conjecture/SKILL.md` (body 126 lines), `agents/openai.yaml`, `references/theory.md`. No `references/output-template.md`: the record fits in the body, so no fallback is needed.

Description: 1,020 characters after the diff review (Python `len` of the parsed value; limit 1,024; 1,018 in b30344d).

## Research proposals

Applied:

- The name `dia-conjecture` (open question 1).
- Steps 1-6 of the sketch: quote C, proof-analysis with [T]/[A] lemmas, counterexamples with an evidence class, the user's ruling, the repair picked by the user, a record from C to C′.
- Roles: the user owns C and its proof and rules; the assistant raises cases.
- The "Never" list: no unnamed monster-barring, no silent "I meant …", no ruling for the user, no flip without a named defect, no C′ before the user picks (hard rules 4-7).
- The Popper fold: the prior refutation criterion, asked before the first case for a claim that rests on observation.
- Rule 5 left out (open question 7), now labelled as not implemented.
- The round cap of three, and naming the pattern when repairs become a list of exceptions.

Declined or changed:

- "At most three counterexamples" per pass: replaced by one per message (review F11).
- The Step 5 menu (surrender, exception-barring, monster-adjustment, lemma-incorporation, "Rule 2 by default"): replaced by the local/global branch (F1).
- "A 'doesn't count' is named as monster-barring": replaced by four ruling classes (F2).
- "Stop when a pass finds no counterexample": a holding record must list what was tried (F10).
- The research label ("applied to any general claim backed by an argument"): replaced by the owner/F5 label; "general claim" narrowed to strictly universal (F3).
- "Rules, policies, generalizations" as the object: "policies" dropped (F3).
- Reconstructing [A] lemmas as the default for a claim with no argument (open question 2): the argument is asked for first; reconstruction is offered, conditional on the user accepting each lemma.
- Moving "find counterexamples" requests from dia-brainstorm (open question 3): not done. This batch edits dia-brainstorm's description only for the dia-counterplan pointer; a dia-conjecture pointer would push it past 1,024 characters (now 1,014) and needs the owner to choose what to trim. Probes 5 and 11 measure the gap. dia-brainstorm's body gets a fallback line toward dia-counterplan and dia-conjecture instead (package review finding 9).
- The "fit: high" rating and the HCI evidence as support (lines 159-171): not carried into the skill (F6).

## Review findings, review/modern-dialectic.md

- **F1 applied.** Step 3 applies Lakatos's Rules 1 and 3 to every local case; Step 5 branches local only (Rule 4; C unchanged unless the lemma was built into C, then a deeper proof widens C′), global only (name the hidden lemma, add it, then Rule 2), both (lemma-incorporation). Exception-barring and monster-adjustment only on request, labelled as responses Lakatos rejects. The content-increasing direction is the deeper proof (section 6a) for a local case against a built-in lemma, and a weaker lemma (Rule 2's "a suitable lemma") for a global case.
- **F2 applied.** Hard rule 2: each case shows, condition by condition, that it meets C's antecedent and violates its consequent. Step 4: invalid (the user names a failed condition) is withdrawn; monster-barring is accepted only as an explicit definition change with its lost content, labelled as a departure from Rule 2; a bare denial is disputed, neither dropped nor counted.
- **F3 applied.** Strictly universal claims only; Step 0 and the description send "generally / usually" claims to dia-warrant, plans and policies to dia-counterplan, dia-brainstorm or dia-negative, meanings to dia-elenchus, Q and not-Q to dia-reductio. "Contradiction" and "follows from its premises" are not in the description. The overlap with dia-reductio and dia-negative (both narrowings are exception-barring) is stated in theory.md section 7.
- **F4 applied.** Roles: ask for the argument first; a run on reconstructed [A] lemmas needs the user's acceptance of each, and the skill says it is then arguing both sides. The user's incentive to monster-bar is named, and answered by the per-case check and the ruling classes.
- **F5 applied.** Label in the body and in theory.md: ch. 1 sections 1-6 and Rules 1-4; Rule 5 and the concept-stretching analysis of sections 7-9 not implemented; concept-stretching is only classified (a Step 4 class).
- **F6 applied.** theory.md section 6: no study tests this method with users; Danry et al. and Chiang et al. are distant analogues; the Counterexample Game figures are model-rated upper bounds from a model-versus-model setup on definitions. No fit rating appears in the skill.
- **F9 applied.** "Popper's prior refutation criterion; an addition to Lakatos", with Lakatos's denial of Popperian critical tests in theory.md. The surrender voice is cited to SEP "Lakatos".
- **F10 applied.** The holding results require the Tried line: lemmas, kinds of case tried, the most suspect lemma, and "C′ not yet tested" when the last repair was not pressed.
- **F11 applied.** One counterexample per message; the repair menu is its own message.
- **Repo note applied.** A C′ forced by a case resting only on the assistant's recall is conditional (hard rule 3, Step 5, record line).
- F7, F8, F12: not about this skill.

## Review findings, review/index.md

- **F7 applied.** The skill does not claim that the assistant only questions: it raises cases and recommends a repair, and says so in the opening paragraph and hard rule 7 (the Roles section it first cited was cut on 2026-10-21; see Clutter cuts). The Counterexample Game finding is stated in theory.md as the reason for the per-case check and the cap, explicitly "a risk finding, not support for the method".
- **F10 applied in part.** The exclusion sentence is the review's, plus the dia-warrant clause the owner asked for. Negative probe cells below cover every bordering sibling. Not done here: the sibling edits F10 lists (dia-reductio "follows strictly", dia-brainstorm's pointers), which D35 assigns to the batch owner; this implementer may not touch other skills. Note for the batch owner: dia-brainstorm's Step 2 "Counterexample" tactic and its "poke holes" trigger still border this skill; probe 5 checks it.
- Batch owner, same commit (b30344d): dia-reductio 1.1.0 now says "follows strictly from its premises" and points to dia-warrant and dia-conjecture; dia-brainstorm 1.2.0 points to dia-counterplan. dia-brainstorm's description has no pointer to dia-conjecture; its body gets a fallback line toward dia-counterplan and dia-conjecture (package review findings 4 and 9). The P7 re-run is done: probes Part O.

## Open items for the owner

- Cross-reference check: `tools/package.py` requires every `dia-*` name in the text to exist; dia-warrant and dia-counterplan must land in the same batch.
- Always-on listing cost: a 1,020-character description adds to the listing D33 measured.

## Routing probes

Run on Claude and Codex, n=2 per cell, against the 1.2.x baseline, as in P7.

| # | Prompt | Expected |
|---|---|---|
| 1 | "My rule: every pure function can be memoized safely, because its output depends only on its inputs. Find counterexamples, Lakatos style, and let's repair it." | dia-conjecture |
| 2 | "내 규칙은 '테스트가 모두 통과한 커밋은 언제나 배포해도 안전하다'야. 반례를 하나씩 들어서 이 규칙이 정말 모든 경우에 성립하는지 따져 줘." | dia-conjecture |
| 3 | "Most users prefer dark mode, based on our survey. How well do my reasons support that?" | dia-warrant (defeasible claim; negative for dia-conjecture) |
| 4 | "Here is my plan to move the team to a four-day week. Build the strongest opposing case." | dia-counterplan |
| 5 | "Poke holes in my idea for a lunch-menu app before I commit." | dia-brainstorm |
| 6 | "Every promotion here must be fair. But what do I even mean by 'fair'? Make me define it first." | dia-elenchus |
| 7 | "Our policy says all hiring is merit-based. Where does it fail its own standard?" | dia-negative |
| 8 | "I said these three things about our release process. Do they hold together, or is there a contradiction?" | dia-reductio |
| 9 | "대부분의 스타트업은 시리즈 A 이후 5년을 버틴다는 내 주장, 근거가 얼마나 탄탄해?" | dia-warrant |
| 10 | "Write a Python function that checks whether every element of a list is positive." | no skill |
| 11 | "Poke holes in my claim that every microservice should own its own database." | dia-conjecture (universal claim; negative for dia-brainstorm) |
| 12 | "My definition: a game is any activity done for fun. Give me counterexamples." | dia-elenchus (Step 0 sends what a word means there; owner to confirm) |
| 13 | "Our policy says every refund is approved within 24 hours. Find counterexamples." | dia-conjecture acceptable (read as a claim about what happens) |
| 14 | "Here is my proof that every even perfect number ends in 6 or 8. Does it follow?" | dia-reductio (deductive step; negative for dia-conjecture) |
| 15 | "How well does my argument support the claim that all our users churn after a price rise?" | dia-conjecture or dia-warrant, owner to decide; the two descriptions currently both claim it |
| 16 | "Our team rule: never deploy on Fridays. Does it hold in every case?" | not dia-conjecture (a policy to adopt; Step 0 sends it to dia-negative or dia-counterplan) |

Probe run reported by the batch owner (description of b30344d, before the diff-review edits): all four positive cells 3/3 on Claude and 2/2 on Codex; no sibling cell moved to dia-conjecture. Rows 11-16 were run on 283f6fa: probes Part O, boundary table.

## Diff review (2026-10-21)

Source: `review/diff/conjecture.md` (PASS WITH FIXES), plus `review/diff/package.md` findings 4 and 10. Applied in the review's replacement text unless noted. Description 1,020 characters; body 125 lines. No version bump (1.0.0 is unreleased).

- **1 applied** (monster-barring class): Step 4 anchors invalid, concept-stretching and monster-barring to the reading of C fixed in Step 1; a post-hoc narrowing is monster-barring, never concept-stretching. theory.md sections 4-5 now say the same, so they agree with hard rule 5.
- **2 applied** (Rule 4 in the Claim line): Rule 4 dropped from the reasons for C → C′; lemma replacements go under Proof-analysis.
- **3 applied** (deeper proof): local-only now widens C′ when the replaced lemma was built into C (section 6); the deeper-proof option is a weaker condition the counting case still fails. theory.md section 4 describes both uses of 6a.
- **4 applied** (overlapping results): the result is the first that applies, ordered given up, stopped before testing, open, revised, holding.
- **5 applied** (policies): the description says "Not for plans, policies, decisions or ideas"; "such as" dropped. To fit package finding 10 (below) the description also drops "ch. 1 sections 1-6" from its label (the body keeps the full label), says "splits its argument" and "a repair Lakatos allows", and "checked condition by condition" became "each with its check" (hard rule 2 still requires condition by condition).
- **6 applied** (routing): probe rows 11-15 added; the open-question-3 line replaced, with the dia-brainstorm body fallback added (package finding 9).
- **7 applied** (monster-adjustment source): theory.md section 3 says the grouping is the skill's reading, not a quoted source.
- **8 applied** (worked example): "O(log n) time", and the check separates link walks from comparisons.
- **9 applied** (two asks after round three): the third post-pick message restates C and offers to stop instead of raising a case.
- **10 applied** (both-sides paths): [T] covers C's source (user, pasted text or earlier answer); self-examination says the assistant argues both sides; picking the global-only option accepts the [A, hidden] lemma.
- **11 applied** (label): body line names 6a as the only part of section 6 used, Rule 5 as section 7, concept-stretching as sections 8-9.
- **12 applied** (citations): `report-*.md` → `review/<x>.md` in line 3 and both headers.
- **13 applied** (case order): Step 3 aims first at the lemma marked most suspect.
- **Package 10 applied** (rule vs policy): the description and the body's opening line say "a rule or generalization about what is the case (not a policy to adopt)"; theory.md section 5 matches; probe 16 covers the Friday-deploy request.
- **Package 4 applied**: the batch-owner sibling edits in b30344d are recorded under review/index.md F10.
- Declined: none.

## Second pass (2026-10-21)

Source: `review/pass2/conjecture.md` (PASS WITH FIXES), plus the conjecture item in `review/pass2/package.md` (finding 6). Description 1,020 characters; body 126 lines. No version bump (1.0.0 is unreleased); `plugins/dia/` and the zips are not regenerated here.

- **S1 applied** (global "deeper proof" mislabelled): Step 5's option is now **Weaker lemma** (Rule 2's "a suitable lemma"), with a one-line check that the counting case fails it and a ban on conditions the case meets or that restate B; the Claim line adds "weaker lemma"; theory.md section 4 uses the reviewer's sentence; Pitfalls gains **Empty repairs**. Changed from the reviewer's text: "the 'empty tautology' Lakatos's critics warn of" became "SEP's account of Lakatos warns of" (the phrase is SEP's exposition, not a critic's); theory.md section 3 quotes SEP's example and points to Step 5; the Exception-lists pitfall says "or a weaker lemma" (deeper proof is now local only).
- **Package 6 applied** (out-283-a turn 6, option 2, met by the counting case): covered by S1's check line and ban.
- **S2 applied** (Step 0 admits a universally worded policy): Step 0 uses the reviewer's text. Part O's "Step 0 sends a policy to adopt elsewhere" is false: in the one Friday run that loaded dia-conjecture (`out2/cc-var2-c-neg-friday-2.json`), Step 0 did not stop; the assistant recast the rule as "every deploy made on a Friday is a mistake" and continued. Step 0 is tightened for this. probes.md is left to its owner.
- **S3 applied in this note** (boundary results): "not yet run" replaced; the F1 line updated. For probes.md's owner: Part O's "Every positive cell for the three new skills …" holds only for the first table; in the boundary table row 11 ("Poke holes in my claim that every microservice …") goes to dia-brainstorm or no skill on Claude (0/3) and splits on Codex (1/2); dia-brainstorm's description has no pointer to dia-conjecture (owner decision).
- **N1 applied:** the Claim line adds ", unless it widens C′ (then the reason is deeper proof)".
- **N2 applied:** hard rule 2 reads "under the reading of C fixed in Step 1".
- **N3 declined here** (dia-brainstorm:41 is another skill's file): route to the batch owner.
- **N4 applied:** row 13 expects "dia-conjecture acceptable (read as a claim about what happens)".
- **N5 applied:** the diff-review "5 applied" line records "each with its check".
- **N6 applied** (recorded): row 12 now expects dia-elenchus, as Step 0 already decides, for the owner to confirm. Part O's "dia-conjecture 2/2" for row 12 on Codex var2 counts reads: both runs ignored the skill (one bulleted list of four counterexamples, no Step 1).
- **N7 declined here** (spec D35 is another file): route to the spec owner ("1,219 for the seven at eb7ab54").
- **N8 declined here** (spec §5.9 and §5.3 are another file): route to the spec owner.
- **Session violations** (b turn 6 "$38" figure, b turn 5 bare "Yes", a turn 1 L3 reason): no text change; hard rule 2, Step 2 and S1's one-line check already cover them.
- Also fixed: the stale "Still open: the P7 re-run" under review/index.md F10 (package pass2 finding 2).

## Clutter cuts (2026-10-21)

Source: the owner-approved body clutter audit (section 4, dia-conjecture: C1-C7). C9 declined by the owner. Frontmatter unchanged. SKILL.md 3,925 → 3,370 cl100k tokens (body 3,680 → 3,125; −555), 136 → 119 lines.

- **C1:** the five-step "shape" list after the opening paragraph cut (the steps and the Step 6 cap say the same).
- **C2:** the Roles section cut. The reconstruction offer moved to Step 1; the both-sides disclosure to Step 2's [A]-lemma bullet. Ownership and the user's rulings stay in the opening line and hard rules 4 and 7. Dropped with it: the sentence naming the owner's incentive to monster-bar (F4); the per-case check and the ruling classes that answer it remain. F7 above now cites the opening paragraph and hard rule 7.
- **C3:** Step 5's conditional-C′ sentence cut; hard rule 3 and the record's Conditional-on line keep it.
- **C4:** Step 4's Invalid, Concept-stretching and Monster-barring bullets shortened to the audit's text. The explicit "ask whether the user now reads the term more narrowly" is gone; a narrowing reply is classified as it comes. theory.md section 5 still says "whether or not the user calls it a change" (not edited here).
- **C5:** the record's Claim-line tail simplified to "a lemma replacement that leaves C unchanged goes under Proof-analysis"; a widening replacement keeps "deeper proof" in the reason list.
- **C6:** Pitfalls cut to Exception lists and Unnamed monster-barring (the other five restated rules; Step 5 keeps the empty-repair ban).
- **C7:** Step 5's Weaker-lemma bullet reworded to the audit's text (same check line and ban).
- **Audit 3.2 (Step 0 misreading):** the sample restatement of the Friday policy as a claim removed, so the model has nothing to echo; "do not restate it that way yourself" stays.
- **Drift D4:** no change here. Hard rule 11 translates labels, as dia-warrant does; the odd one out is dia-counterplan.
- Not re-run: the audit's section 5 A/B re-runs (C2, C4, C7 and the record) are still open.
