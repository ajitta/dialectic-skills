# Design note: dia-counterplan

New skill for plugin 1.3.0. Sources: `docs/research/candidates/argumentation.md` §2.7, §2.9, §3, §5 (sketch 1); its independent review (`report-argumentation.md`, cited **A-Fn**) and the index review (`report-index.md`, cited **I-Fn**), copies in `docs/research/candidates/review/`; `scholastic.md` §2.5 for *teyku* and the kept minority view. Where research and review differ, the review was followed. Owner decisions from the implementation brief were applied as given.

Files: `skills/dia-counterplan/SKILL.md` (body 124 lines after the diff review), `agents/openai.yaml`, `references/theory.md`, `references/output-template.md` (the body's Step 8 lists the record fields as a fallback, as in dia-reductio).

## Description

1,019 characters after the diff review (Python `len`, limit 1,024; 1,008 at b30344d). No `: ` or ` #` in the plain scalar (package.py rule), so the honest label uses a semicolon there; the body keeps the colon form. Order: label, what it does, "Use only when" triggers limited to plans and decisions plus "or the same in any language", the claim-level devil's-advocate exclusion (see Diff review), then the exclusion sentence from the brief. `short_description` is 57 characters.

## Research proposals (argumentation.md sketch 1)

Applied:
- Steps 1, 2, 3, 5 and 7 of the sketch: state the plan, number the assumptions (quoted [T] or reconstructed [A]), keep those that do the work, put both side by side, hand the decision to the user, end with a record.
- Step 6, "name the observation that would favour each side": one line per pair in Step 6.
- Never-list: pick no winner, no carping critic (Rule 1), no invented figures or sources (Rule 4).
- One pass for Steps 1-7; follow-ups re-run only on a changed plan or a rewritten contrary.

Declined or changed:
- "Negate those" (step 4): replaced by chosen, labelled contraries (A-F3).
- The devil's-advocate variant as a mode: not offered (owner decision). theory.md §4 says why the skill is DI.
- The label's "with a devil's-advocate variant": dropped; owner label used verbatim.
- Open question 2 (the assistant's own recommendation as default): declined (A-F5). `claude` only on request.
- "Weaken the counterplan only with a supplied fact": replaced by the ruling rule (A-F12).
- "Fit: high": rated medium in theory.md §5 (A-F1).
- "Do not use 'poke holes' or 'stress-test' in the description": kept in substance. The words appear only in the exclusion sentence that points them to dia-brainstorm.

## Review findings

- **A-F1** applied: fit medium, and "no study tests one model writing both sides" in theory.md §5. Symmetry rule (Rule 3): pairs, same data, same level of detail, and the line that one assistant wrote both sides.
- **A-F2** applied: Schwenk's negative conclusions, the "heard both sides" belief and the DA-solidifies-commitment warning in theory.md §4. The record states what was not tested and "Hearing both sides is not evidence that the plan was tested." The F2 suggestion to make DA the default was declined (owner decision for DI); the evidence is stated in theory.md.
- **A-F3** applied: fidelity "medium-high; procedure from secondary sources"; Churchman lineage in the label; contraries chosen, labelled, checked for coherence and same data (Step 4); Step 7 asks which assumptions the user holds, and that set is the result (Mason's criterion 2). theory.md §1 says the synthesis is not Hegel's (consistent with modern-dialectic.md).
- **A-F4** applied: the SAST test in Step 3, labelled "from SAST (Mason & Mitroff 1981)"; ratings omitted and the omission stated.
- **A-F5** applied: not the default target; the self-examination line; Chiang et al. described as interactive DA against a separate model's advice, in groups, with marginal main effects; Huang et al. on self-correction.
- **A-F7(c)** applied: triggers name a plan or decision; claim-level devil's advocate is excluded in the description and in "When this skill does not fit". A-F7(a), (b), (d) concern dia-warrant and dia-conjecture; (d) is reflected by the dia-warrant pointer.
- **A-F12** applied: Rule 6 and the follow-up turns. A rejected contrary is a ruling to record; a rewrite needs a named defect (it misstates the data or contradicts another contrary). The plan's assumption list follows D19.
- **I-F1** applied: theory.md §5 says the debate gains needed separate debaters, a hidden source text and a quote verifier, and that the user can still act as judge.
- **I-F8** applied: one model writing both sides is stated as a risk, not hidden. The modern-dialectic.md:20 conflict is resolved by having no DA mode (the critic role stays with dia-brainstorm's stress mode). dia-brainstorm's description gained the pointer in this batch (1.2.0).
- **I-F9** applied: *teyku* as the result **undetermined**, and the kept strongest argument for the side set aside (Eduyot 1:5), both labelled as Talmudic borrowings (theory.md §6).
- **I-F10** applied: the exclusion sentence, adapted per the brief (dia-conjecture "universal claim"; dia-warrant added). The dia-brainstorm pointer is made here; a dia-negative pointer is not.

## Choices of this implementation (for the owner to check)

- `--target=user|claude|text`, without `all`: one plan per counterplan keeps the output to one comparison. Several plans: the one being decided, the others listed as not examined.
- At most five key assumptions, to keep Step 6 readable on a phone.
- A datum the decision turns on that is only single source or unverified recall is listed as an assumption, so a contrary may dispute it openly rather than "contradict the data".
- Result values: plan side held, counterplan side held, synthesis, undetermined, no key assumption found, stopped.
- No pick, during or after the inquiry (changed in the diff review, finding 4(a)): a user who asks for the assistant's pick is told the result is their set (or will be, once they rule) and given the observation that would decide each open pair, or the one pair they name as hardest (second pass, N8).
- "What are the hidden assumptions in my plan?" without a request for a counterplan is not in this skill's triggers ("Use only when"). If the skill is loaded for it anyway, it runs Steps 1 to 3 and offers the counterplan in one line (diff review, finding 12). Routing is unprobed for a pure plan prompt; the nearest Part O cell ("my case for the four-day week") was expected and loaded as dia-warrant on Codex (2/2) and loaded no skill on Claude (0/3).

## Routing probes

| # | Prompt | Expected |
|---|---|---|
| 1 | Our plan: move support to a four-day week in Q1, because tickets fell 20% and hiring is frozen. Play devil's advocate on this plan and make the case for the opposite plan. | dia-counterplan (user) |
| 2 | 우리 계획은 내년에 자체 물류센터를 짓는 거야. 핵심 가정들이 틀렸다면 어떤 반대 계획이 나오는지 써 줘. | dia-counterplan (user) |
| 3 | You recommended Postgres over DynamoDB above. What if the key assumptions behind your recommendation are wrong? Write the counterplan. | dia-counterplan (claude, self-examination line) |
| 4 | 신규 채용 대신 외주로 가기로 했어. 이 결정의 반대 입장에서 대안 계획을 세워 줘. | dia-counterplan (user) |
| 5 | Poke holes in my plan to open a second café; ask me one question at a time. | dia-brainstorm (negative cell) |
| 6 | 내 창업 아이디어를 질문으로 하나씩 검증해 줘. | dia-brainstorm (negative cell) |
| 7 | Play devil's advocate: is intermittent fasting actually healthy? | no skill (claim-level, A-F7c) |
| 8 | Every team that adopts microservices ships slower. Find counterexamples to that. | dia-conjecture (negative cell) |
| 9 | How well do the reasons in this op-ed support its conclusion? [pasted op-ed] | dia-warrant (negative cell) |
| 10 | Our promotion policy says it is merit-based. Where does it fail its own standard, and what is it really for? | dia-negative (negative cell) |

A write-something cell ("Write a go-to-market plan for our app") should load no skill; if this skill loads anyway, its "does not fit" section says to do the task without it.

## Diff review (2026-10-21)

Review: `docs/research/candidates/review/diff/counterplan.md` (PASS WITH FIXES, cited **D-Fn**), plus finding 8 of `review/diff/package.md` (**P-F8**). No version bump: 1.0.0 is unreleased.

- **D-F1** applied: Rule 3 asks for the same slots; a figure neither side has is written "not supplied" and listed under not tested, so Rule 4 wins. The template's Counterplan line says the same.
- **D-F2** applied: **stopped** means no pair ruled; stopping after some rulings is **undetermined**. The "always" record lines exclude **no key assumption found**, which gets its own not-tested line (body and template).
- **D-F3** applied: only ruling-only follow-ups must fit a phone screen; rewrites show changed lines; reruns and the record use numbered lines. Pitfall narrowed to match.
- **D-F4** applied, option (a): no pick during or after the inquiry; the pick request gets the user's set and the observation that would decide the hardest pair. The label's "Picks no winner" now holds without exception.
- **D-F5** applied: Mason's procedure restated from Schwenk (plan from the planners, counterplan built separately, debated before managers) in SKILL.md and theory.md §7; theory.md §3 quotes Schwenk's "negation" and lists contraries as a departure.
- **D-F6** applied: *teyku* is "named after … borrowed loosely"; theory.md §6 says an undetermined pair is open only for now, and cites Eduyot 1:6's rival reason (the kept view follows 1:5).
- **D-F7** applied: theory.md §4 describes the study designs (separate subgroups or advocates, or written reports presented as from different sources; none tested a person who knows one author wrote both sides; reworded in the second pass, N2).
- **D-F8** applied: the Rule 2 example marks the merger as a supposition, and Rule 2 says a mechanism in a contrary is never a reported fact.
- **D-F9** applied: a rejected contrary counts as the plan's assumption held unless the user gives their own wording or can't tell; own-words pairs keep the argument for whichever side the wording departs from more; "can't tell" records the pair as open.
- **D-F10** applied, extended: the Procedure intro names the early exits (Step 1 asks, Step 3 finds none, and the assumptions-only request from D-F12), so the intro and "When this skill does not fit" agree.
- **D-F11** applied: the kept minority view is labelled as a Mishnah borrowing in Step 8.
- **D-F12** (a) applied: an assumptions-only or weak-points-only request runs Steps 1 to 3 and offers the counterplan in one line (this settles the earlier open choice; it surfaces assumptions, not flaws, so Rule 1 holds). (b) and (c) remain open (second pass: P-F8 is a theory.md sentence, not routing, and no probe cell was added); dia-refine and dia-negative are outside this skill.
- **D-F13** applied: the I-F8 and I-F10 lines now say the dia-brainstorm pointer was made in this batch. The batch owner made that edit (dia-brainstorm 1.2.0) in b30344d.
- **P-F8** applied: theory.md §4 states that a devil's advocate on a plan is answered with dialectical inquiry (a counterplan), not devil's-advocacy critique; critique by questions stays with dia-brainstorm's stress mode.

Routing probes (Part O; cell 3 was replaced by "Play devil's advocate on our plan to move to a four-day week: what if our key assumptions are wrong?", so the `claude` target is unprobed; cell 9 ran as an unstated-warrant prompt): the four positive cells loaded dia-counterplan 3/3 on Claude and 2/2 on Codex in both var and var2. Cell 7 ("Play devil's advocate: is intermittent fasting actually healthy?") loaded no skill on Claude (0/3, correct) but loaded dia-counterplan on Codex (2/2); the skill then answered normally, but the load is an over-trigger. The description now reads "Use only when asked for a counterplan or a devil's advocate on a plan or decision" and replaces "Not for whether one claim is true" with "Not for a devil's advocate on a claim or question ("is X true?", "is X healthy?"); answer directly." To fit the cap, the trigger example "devil's advocate on this plan" (a duplicate of the trigger), "decision" in "a plan, decision or recommendation" (still in the trigger) and "the user's" in the dia-brainstorm pointer were dropped. On var2, cell 7 loads no skill on Codex (0/2).

## Second pass (2026-10-21)

Review: `docs/research/candidates/review/pass2/counterplan.md` (PASS WITH FIXES, cited **N1**-**N9**). First-pass findings re-verified as fixed except D-F7 (overclaim, now N2) and D-F12 (b), (c) (not covered; restated as open above). No version bump: 1.0.0 is unreleased.

- **N1** applied: Rule 3 says "not supplied" is for a missing fact (a price, a measured quantity); a step, date or condition the counterplan chooses must be named. Template Counterplan line matches.
- **N2** applied: theory.md §4 intro replaced with the reviewer's text (subgroups or advocates; reports presented as from different sources; no test of a known single author). D-F7 line above reworded to match.
- **N3** applied: an added assumption goes through Steps 3 to 7, shows only new lines, is ruled on before the record, and either displaces a named pair or is listed as passed but not paired.
- **N4** applied: Step 1 asks for an exact quote, never reworded inside quotation marks; Step 2 makes any reworded or inferred line [A].
- **N5** applied in this note: the hidden-assumptions choice above replaced with the reviewer's text. The proposed Part O cell ("What are the hidden assumptions in our plan to open a second warehouse?", owner-chosen expectation) is left to the owner; docs/probes.md and the probe scripts are outside this pass.
- **N6** applied: the probe paragraph's first and last sentences replaced (cell 3 replaced, `claude` target unprobed, cell 9 ran as an unstated-warrant prompt; cell 7 on Codex var2 0/2).
- **N7** applied: Step 7 says a leaning counts as held only if the user says so; otherwise the pair is open with the lean noted in one word.
- **N8** applied: the pick follow-up now matches Rule 5 (the result is their set or will be; the observation for each open pair, or the one the user names as hardest). Choices line above updated.
- **N9** applied in part: the assumptions-only line in "When this skill does not fit" now says no record and key assumptions only, not flaws (Rule 1). The spec §5.10 qualifier "(except when no key assumption is found)" is not applied: spec.md is outside this pass; left for the owner.
