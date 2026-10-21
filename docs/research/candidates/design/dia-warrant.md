# Design note: dia-warrant

New skill for plugin 1.3.0. Sources: `docs/research/candidates/argumentation.md` (§2.1 Toulmin, §2.2 pragma-dialectics, §2.3 Walton, §5.2 sketch) and the independent review (`report-argumentation.md` F6–F9, F13; `report-index.md` F6, F10). Where they differ, the review wins. Files: `skills/dia-warrant/SKILL.md`, `agents/openai.yaml`, `references/theory.md`, `references/output-template.md`.

## Shape

- One-pass audit by default: claim, data, warrant, backing, qualifier, rebuttal, each marked stated or reconstructed; scheme; critical questions tagged [data], [warrant/backing], [rebuttal] or [conclusion], each answered in the argument, answered by the user, answered by a source found (tool and request only) or open; a qualifier check; the weakest link; a record.
- Named `ask` mode: one slot question per message in Toulmin's order, then the open critical questions.
- `--target=user|claude|text|all` with the siblings' inference rule and first-line statement.
- Fixed results: **weakest link: [slot], because [critical question] is left open** (or "is answered against the step"); **no weak link found among the questions asked; not a proof**; **stopped**.
- Never: an unlabelled reconstructed warrant; "false" or "invalid" for weak support; a verdict on the claim's truth (Rule 1 says the audit does not decide it, also when the user asks).
- Body 132 lines; the five schemes' questions are inline, so the skill works without opening any reference. The output template is a reference, and Step 7 lists the record fields as a fallback (the dia-reductio pattern).

## Research-doc proposals

| Proposal | Status | Note |
|---|---|---|
| §5.2 label (Toulmin layout + Walton CQs; not Toulmin's critique of formal logic) | applied | Adds Verheij's four types as the basis for the tags, and labels the pragma-dialectical fold |
| §5.2 steps 1–5 | applied | Step 2 marks stated or reconstructed; Step 3 allows two schemes [12]; Step 4 statuses; Step 6 weakest link. Step 5, the qualifier check, is added and labelled as this skill's |
| §5.2 stop rule ("one question per turn if the user asks") | applied, strengthened | Now the named ask mode (F13) |
| §5.2 never: call a defeasible argument "invalid" | applied | Rule 1 |
| §5.2 never: attribute a warrant the author would disown | replaced | By the least-warrant rule after the validity rule (F9); the original cannot be checked for a third-party text |
| §5.2 never: assert counter-facts instead of asking | applied | Rule 5; facts carry the siblings' evidence classes |
| §2.2 fold the unexpressed-premise, standpoint and usage rules | applied | Rule 4, labelled "this skill's selection"; theory.md §4 quotes the three rules and says which are left out and why |
| §2.3 short table of schemes (practical reasoning, expert opinion, cause to effect, analogy, sign) | applied with one change | Practical reasoning becomes argument from consequences: practical reasoning's questions (goals, alternative means, side effects) examine a plan or decision, which belongs to dia-counterplan (F7d) |
| §2.1 keep "contradiction" and "follows strictly" out of the description | applied | They appear only in the pointer to dia-reductio |
| §2.1 dia-reductio partial overlap | handled by scope | Scope section and description say strict and deductive questions go to dia-reductio |
| Open question 4 (a shipped scheme table) | settled | The questions sit in SKILL.md in this skill's own wording; sources are in theory.md |

## Review findings

- **F6 (argumentation) applied.** Fixed results, a record, the pushback rule ("withdraw only if you can name its defect … insistence is not a defect"), standard target inference, reply language (Rule 8), and the pasted-material sentence (Targets, text).
- **F7a applied on this side only.** The description keeps away from "follows from its premises" and points to dia-reductio for a strict contradiction or a deductive step. The review also asks for dia-reductio's description to say "follows strictly from its premises" and to point to dia-warrant. That edit, its version bump and a P7 re-run are outside this task's paths. **Open for the parent or owner.**
- **F7b applied.** The exclusion sends counterexamples to an all, always or never claim to dia-conjecture. dia-conjecture's description already sends "how well reasons support a probable or usually-true conclusion" here. Probe cells 8 and 3 cover both directions.
- **F7c not applicable** (dia-counterplan triggers).
- **F7d applied.** Assumptions under a plan or decision go to dia-counterplan (description and Scope); the argument-from-consequences scheme audits only the argument as given. dia-counterplan's description points back.
- **F8 applied.** SKILL.md and theory.md use Toulmin's own "What have you got to go on?" and "How do you get there?", and theory.md says the backing question is Verheij's paraphrase. Page references come from Verheij [4] (1958/2003). The merge is grounded in Verheij's four types of critical questions, not in [6], and every question carries a slot tag. The tags on the four schemes other than expert opinion are labelled as this skill's application of Verheij's mapping.
- **F9 applied.** Rule 3 supplies the least warrant, after the pragma-dialectical validity rule; it is labelled reconstructed, and W1/W2 are given when two are plausible. The critical questions are inline (no reference needed).
- **F13 applied.** Named ask mode, offered in one line after an audit of the user's own argument; it runs directly when the user asks to be questioned or wants to build an argument.
- **Index F6, partly applied.** The price of the pick, warrant reconstruction ("the core danger"), is met by Rules 2–4, the user's power to reject a warrant, and a pitfall that says the layout is the assistant's reading. On the jargon point, the triggers use plain words ("how well reasons support a conclusion", "whether an expert, analogy or causal argument holds up") beside "warrant" and "Toulmin". **Declined:** a "fallacy" trigger. The skill reports open questions, not fallacy labels (pitfall); add the trigger only if probes show that "is this a fallacy" requests are lost.
- **Index F6 dia-refine scope applied.** The pointer says "the previous answer or a draft", not only the assistant's own answer.
- **Index F10, partly applied.** The warrant exclusion sentence is used in the owner's adapted form: a "strictly universal claim (all, always, never)" in place of "a general rule or claim", because a Toulmin warrant is itself a general rule. Not done here (outside this task's paths): the sibling edits F10 lists for dia-reductio and dia-brainstorm, and the P7 negative cells for every pair.

## Description

- 1,015 characters, counted with Python (`len()` of the parsed frontmatter value; `tools/package.py validate_skill` reports no errors). There is little headroom: 9 characters under the 1,024 limit.
- Pointers are shortened ("…, dia-refine; …, dia-conjecture; …, dia-counterplan") to fit; the meaning of the owner's exclusion sentence is kept.
- `short_description`: 61 characters.

## Sources added beyond the research ledger

These were fetched on 2026-10-21 for the five question sets: Wikipedia "Argumentation scheme" (expert opinion, Walton, Reed & Macagno 2008 p. 310); Walton 2014 (analogy, p. 315); an IRMCT amicus brief quoting Walton 1995 (cause to effect; single secondary source); Fan 2019 (consequences, p. 102; secondary); Macagno, Walton & Reed 2017 (scheme forms); and Blair 1998 (sign, Walton 1996 p. 48). Verheij [4] was re-read for the page references and the four types.

## Routing probes (n=2 each, against the 1.3.0 package)

| # | Prompt | Expected |
|---|---|---|
| 1 | "Our churn dropped after we added onboarding emails, so the emails cut churn. How well do my reasons support that?" | dia-warrant (user, audit; cause to effect or sign) |
| 2 | "전문가가 그렇다고 했으니까 맞는 거잖아. 이 근거가 결론을 얼마나 잘 뒷받침하는지 봐줘." | dia-warrant (user, expert opinion) |
| 3 | "What is the unstated warrant in this op-ed paragraph? [pasted paragraph arguing that cities with more bike lanes will usually see fewer accidents]" | dia-warrant (text); not dia-conjecture, because the claim is "usually" |
| 4 | "툴민 모형으로 내 논증을 하나씩 질문하면서 같이 세워줘." | dia-warrant, ask mode |
| 5 | "이 결론이 전제에서 연역적으로 엄밀하게 따라 나오는지 확인해줘." | dia-reductio, not dia-warrant |
| 6 | "Review your previous answer as a draft and fix the logical leaps." | dia-refine, not dia-warrant |
| 7 | "'모든 정규화 기법은 테스트 성능을 올린다'는 내 주장에 반례를 찾아줘." | dia-conjecture, not dia-warrant |
| 8 | "Play devil's advocate on our plan to move to a four-day week: what if our key assumptions are wrong?" | dia-counterplan, not dia-warrant |
| 9 | "Poke holes in my startup idea before I commit to it." | dia-brainstorm, not dia-warrant |
| 10 | "Is it true that intermittent fasting improves memory?" | no skill (a factual question; dia-warrant must not load) |

A miss on 5–10 means the description is pulling too wide. Narrow the triggers first; do not add another exclusion clause, because the description is 9 characters under the limit.
