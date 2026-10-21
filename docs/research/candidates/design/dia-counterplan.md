# Design note: dia-counterplan

New skill for plugin 1.3.0. Sources: `docs/research/candidates/argumentation.md` §2.7, §2.9, §3, §5 (sketch 1); its independent review (`report-argumentation.md`, cited **A-Fn**) and the index review (`report-index.md`, cited **I-Fn**), copies in `docs/research/candidates/review/`; `scholastic.md` §2.5 for *teyku* and the kept minority view. Where research and review differ, the review was followed. Owner decisions from the implementation brief were applied as given.

Files: `skills/dia-counterplan/SKILL.md` (body 122 lines), `agents/openai.yaml`, `references/theory.md`, `references/output-template.md` (the body's Step 8 lists the record fields as a fallback, as in dia-reductio).

## Description

1,008 characters (Python `len`, limit 1,024). No `: ` or ` #` in the plain scalar (package.py rule), so the honest label uses a semicolon there; the body keeps the colon form. Order: label, what it does, "Use when" triggers limited to plans and decisions plus "or the same in any language", "Not for whether one claim is true", then the exclusion sentence from the brief. `short_description` is 57 characters.

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
- **I-F8** applied: one model writing both sides is stated as a risk, not hidden. The modern-dialectic.md:20 conflict is resolved by having no DA mode (the critic role stays with dia-brainstorm's stress mode). Not done here: dia-brainstorm's description should gain a pointer to dia-counterplan (sibling edit, outside this batch).
- **I-F9** applied: *teyku* as the result **undetermined**, and the kept strongest argument for the side set aside (Eduyot 1:5), both labelled as Talmudic borrowings (theory.md §6).
- **I-F10** applied: the exclusion sentence, adapted per the brief (dia-conjecture "universal claim"; dia-warrant added). Sibling pointers back to dia-counterplan (dia-brainstorm, possibly dia-negative) are not made here.

## Choices of this implementation (for the owner to check)

- `--target=user|claude|text`, without `all`: one plan per counterplan keeps the output to one comparison. Several plans: the one being decided, the others listed as not examined.
- At most five key assumptions, to keep Step 6 readable on a phone.
- A datum the decision turns on that is only single source or unverified recall is listed as an assumption, so a contrary may dispute it openly rather than "contradict the data".
- Result values: plan side held, counterplan side held, synthesis, undetermined, no key assumption found, stopped.
- After the record, a user who still wants the assistant's own pick gets it labelled as the assistant's view, with the note that it wrote both sides (modelled on dia-elenchus's "after the dialogue"). The skill itself never gives a verdict. Drop this line if the owner wants no pick at all.
- Open: "What are the hidden assumptions in my plan?" without a request for a counterplan routes here under A-F7(d), but the skill always builds the counterplan. A Steps-1-to-3-only answer would amount to a DA-style critique, which the owner did not take.

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
