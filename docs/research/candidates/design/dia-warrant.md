# Design note: dia-warrant

New skill for plugin 1.3.0. Sources: `docs/research/candidates/argumentation.md` (§2.1 Toulmin, §2.2 pragma-dialectics, §2.3 Walton, §5.2 sketch) and the independent review (`review/argumentation.md` F6–F9, F13; `review/index.md` F6, F10), the diff review of `b30344d` (`review/diff/warrant.md`; see Diff review below), and the second-pass review of `275e1aa` (`review/pass2/warrant.md`; see Second pass below). Where they differ, the review wins. Files: `skills/dia-warrant/SKILL.md`, `agents/openai.yaml`, `references/theory.md`, `references/output-template.md`.

## Shape

- One-pass audit by default: claim, data, warrant, backing, qualifier, rebuttal, each marked stated or reconstructed; scheme; critical questions tagged [data], [warrant/backing], [rebuttal] or [conclusion], each answered in the argument, answered by the user, answered by a source found (tool and request only) or open; a qualifier check; the weakest link; a record.
- Named `ask` mode: one slot question per message in Toulmin's order, then the open critical questions.
- `--target=user|claude|text|all` with the siblings' inference rule and first-line statement.
- Fixed results: **weakest link: [slot], because [critical question] is left open** (or "is answered against the step"); **weakest link: qualifier, because the claim says "[strength]" where the warrant licenses "[strength]"**; **no weak link found among the questions asked; not a proof**; **stopped**.
- Never: an unlabelled reconstructed warrant; "false" or "invalid" for weak support; a verdict on the claim's truth (Rule 1 says the audit does not decide it, also when the user asks).
- Body 135 lines; the five schemes' questions are inline, so the skill works without opening any reference. The output template is a reference, and Step 7 lists the record fields as a fallback (the dia-reductio pattern).

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
- **F7a applied on this side only.** The description keeps away from "follows from its premises" and points to dia-reductio for a strict contradiction or a deductive step. The review also asks for dia-reductio's description to say "follows strictly from its premises" and to point to dia-warrant. Applied in the same commit (dia-reductio 1.1.0); P7 re-run open.
- **F7b applied.** The exclusion sends counterexamples to an all, always or never claim to dia-conjecture. dia-conjecture's description already sends "how well reasons support a probable or usually-true conclusion" here. Probe cells 7 and 3 cover both directions.
- **F7c not applicable** (dia-counterplan triggers).
- **F7d applied.** Assumptions under a plan or decision go to dia-counterplan (description and Scope); the argument-from-consequences scheme audits only the argument as given. dia-counterplan's description points back.
- **F8 applied.** SKILL.md and theory.md use Toulmin's own "What have you got to go on?" and "How do you get there?", and theory.md says the backing question is Verheij's paraphrase. Page references come from Verheij [4] (1958/2003). The merge is grounded in Verheij's four types of critical questions, not in [6], and every question carries a slot tag. Verheij sorts Walton's 1996 expert-opinion questions and adds a conditions-of-use question; the tags on the 2008 trustworthiness and backup-evidence questions and on the other four schemes are labelled as this skill's application of his mapping.
- **F9 applied.** Rule 3 supplies the least warrant, adapting the pragma-dialectical validity rule to a defeasible step; it is labelled reconstructed, and W1/W2 are given when two are plausible. The critical questions are inline (no reference needed).
- **F13 applied.** Named ask mode, offered in one line after an audit of the user's own argument; it runs directly when the user asks to be questioned or wants to build an argument.
- **Index F6, partly applied.** The price of the pick, warrant reconstruction ("the core danger"), is met by Rules 2–4, the user's power to reject a warrant, and a pitfall that says the layout is the assistant's reading. On the jargon point, the triggers use plain words ("how well reasons support a conclusion", "whether an expert, analogy or causal argument holds up") beside "warrant" and "Toulmin". **Declined:** a "fallacy" trigger. The skill reports open questions, not fallacy labels (pitfall); add the trigger only if probe cell 11 shows that "is this a fallacy" requests are lost. That condition has fired (cell 11 loaded no skill: Claude 0/3, Codex 0/2), so the owner decides; see Second pass, S1.
- **Index F6 dia-refine scope applied.** The pointer says "the previous answer or a draft", not only the assistant's own answer.
- **Index F10, partly applied.** The warrant exclusion sentence is used in the owner's adapted form: a "strictly universal claim (all, always, never)" in place of "a general rule or claim", because a Toulmin warrant is itself a general rule. The sibling edits F10 lists for dia-reductio and dia-brainstorm were applied in the same commit (dia-reductio 1.1.0, dia-brainstorm 1.2.0); the P7 negative cells for every pair are open.

## Description

- 1,015 characters, counted with Python (`len()` of the parsed frontmatter value; `tools/package.py validate_skill` reports no errors). There is little headroom: 9 characters under the 1,024 limit.
- Pointers are shortened ("…, dia-refine; …, dia-conjecture; …, dia-counterplan") to fit; the meaning of the owner's exclusion sentence is kept.
- `short_description`: 61 characters.

## Sources added beyond the research ledger

These were fetched on 2026-10-21 for the five question sets: Wikipedia "Argumentation scheme" (expert opinion, Walton, Reed & Macagno 2008 p. 310); Walton 2014 (analogy, p. 315); an IRMCT amicus brief quoting Walton 1995 (cause to effect; single secondary source); Fan 2019 (consequences, p. 102; secondary); Macagno, Walton & Reed 2017 (scheme forms); and Blair 1998 (sign, Walton 1996 p. 48). Verheij [4] was re-read for the page references and the four types.

## Routing probes

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
| 11 | "Is this an appeal to authority fallacy? 'My doctor says it, so it's true.'" | dia-warrant (user, expert opinion) |
| 12 | "Poke holes in my argument that remote work will work for us because it worked at Acme." | dia-warrant, not dia-brainstorm |
| 13 | "What hidden assumptions is my case for the four-day week resting on? It boosts morale, so productivity rises." | dia-warrant, not dia-counterplan |
| 14 | "Does the reasoning in your last answer actually support its conclusion?" | dia-warrant (target claude), not dia-refine |

A miss on 5–10 means the description is pulling too wide. Narrow the triggers first. Do not add another exclusion clause, because the description is 9 characters under the limit. A miss on 11–14 means a request this skill should take went elsewhere or nowhere. Fix it in the sibling that took it (its body fallback) or in this description's triggers, not by narrowing this description.

Cells 11–14 were added by the diff review (finding 7); the close-case tiebreak they test lives in the Scope section, not the description.

Results of the batch owner's run before the diff-review fixes (n=3 Claude, n=2 Codex): every positive cell passed except two. The op-ed cell (3) passed 2/3 on Claude. A Korean cell asking how solid the grounds are for "my claim that most startups survive 5 years after series A" passed 2/2 on Codex and 0/3 on Claude, which answered directly. The description was not widened for it: a bare factual claim with no stated reasons is a defensible non-load, close to cell 10. Cells 11–13 and the post-fix re-probe were run on `283f6fa` (probes Part O). Cell 11 loaded no skill (Claude 0/3, Codex 0/2). Cell 12 went to dia-brainstorm on Claude (3/3) and split on Codex (dia-warrant 1, dia-brainstorm 1). Cell 13 loaded nothing on Claude (0/3) and dia-warrant on Codex (2/2). Cell 14 was not run as written: Part O ran a different "check your last answer" prompt and expected no skill.

## Diff review (2026-10-21)

Source: `review/diff/warrant.md` (PASS WITH FIXES), on `b30344d`. The batch owner made the dia-reductio (1.1.0) and dia-brainstorm (1.2.0) sibling edits in `b30344d`; this note had them as open. All fixes are in SKILL.md, theory.md and the output template; the description is unchanged (1,015 characters) and the body is 133 lines. No version bump: 1.3.0 is unreleased on `next`, so the skill stays at 1.0.0.

- **1 applied (should-fix).** Rule 3 now gives the warrant the strength the target's words give the link, or "generally", and adapts the validity rule to defeasible steps instead of requiring validity, so it no longer clashes with Rule 1 or the worked example. Step 5 says when the comparison is with a reconstruction; theory.md §4 and the SKILL.md intro say "adapts".
- **2 applied (should-fix).** Rule 7 gains the **weakest link: qualifier** form; Step 6 reports the qualifier check in every case and uses that form when no question is open or against; Step 7 and the template record have a qualifier-check field, and the template's Result lines carry the new form.
- **3 applied (should-fix).** "No weak link found" now needs no question open or answered against the step (sources count as answers) and a matching qualifier; Rule 5 says an answer is for or against the step, and the template's status line shows it.
- **4 applied (should-fix).** A bare "yes" or "trust me" leaves a question open (Follow-up turns); in ask mode a bare yes or no fills nothing.
- **5 applied (should-fix).** Rule 4 states the departure from the rule's first half; the rejection follow-up is split by target (user: remove, then "none given" makes the warrant the weakest link; claude or text: a dispute, withdrawn only on a named defect); ask mode's "no" leaves "none given". Rule 7 says a "none given" warrant leaves "How do you get there?" open, so the follow-up's result matches the fixed form. theory.md §4 quotes the whole rule 5 and states the departure.
- **6 applied (nit).** theory.md §3 says Verheij sorts Walton's 1996 questions plus his own conditions-of-use question; the 2008 trustworthiness and backup-evidence tags are this skill's.
- **7 applied in part (should-fix).** "8 and 3" is now "7 and 3"; cells 11–14 are added; the owner's pre-fix run is recorded above. Cells 11–13 and the re-probe ran (probes Part O; results above); cell 14 as written is open.
- **8 applied (should-fix).** The review's close-case tiebreak (brainstorm, counterplan, conjecture) is in Scope; the description is not touched, so the 1,024 cap is not at issue. The Scope tiebreak acts only after this skill loads; the reverse case is in dia-brainstorm's Step 0 fallback.
- **9 applied (nit).** Rule 7 maps [warrant/backing] to warrant or backing and [conclusion] to the claim; "conclusion" is "claim" in the slot list and the tie order.
- **10 applied (nit).** Step 7 ends with the truth line, then the ask-mode offer when Parameters call for it, as the template does.
- **11 applied (nit).** The worked example gains the [conclusion] question (the analogy's counter-case, merged with the general one) and says its qualifier comparison is with the reconstructed W1.
- **12 applied (nit).** F7a and Index F10 now say the sibling edits landed in `b30344d`; the `report-*.md` citations are now `review/<x>.md`.

## Second pass (2026-10-21)

Source: `review/pass2/warrant.md` (PASS WITH FIXES), on `275e1aa`. Fixes are in SKILL.md, the output template, theory.md and this note; the description is unchanged (1,015 characters); the body is 135 lines. No version bump (1.3.0 unreleased on `next`).

- **S1 applied in this note; probes.md left to its owner.** Lines on cells 11–13 and the re-probe now carry the Part O results; cell 14 as written is open; the miss rule is split (5–10 too wide; 11–14 fix the sibling or the triggers); the F6 fallacy condition is marked fired. Open for the probes.md owner: replace Part O readings 1 and 3 with the review's text.
- **S1 fallacy trigger: open, owner decides.** (a) recommended: drop "Ends with a record. " and add "or is a fallacy" after "holds up" (1,011 characters), then re-run cell 11; (b) decline again: "Cell 11 loads no skill on either engine. Declined: Claude answers it directly at base too, and the headroom is kept." The description is not changed here.
- **S2 applied.** Step 1 gains the chained-step rule (C1; Wa and Wb by step; W1/W2 stay rivals; questions within the cap; qualifier on the step reaching C; the result names the step); the template has a step-warrants line; Step 7's fallback warrant field adds Wa and Wb.
- **S3 not applied here (sibling file).** For the batch owner: insert in `skills/dia-brainstorm/SKILL.md` Step 0 fallback, after "…it belongs to dia-conjecture;": "if it asks how well the reasons given support a conclusion (an argument rather than an idea or plan), it belongs to dia-warrant;", then re-run cell 12. The DN:90 sentence is applied (Diff review, 8).
- **N1 applied.** "132 lines" is 133 in the Diff review section; Shape gives the current 135.
- **N2 applied.** The template's critical-question status line uses the review's form.
- **N3 applied.** Step 5 says a "none given" warrant gives "no warrant to compare"; the template record's Warrant line adds "none given"; to keep them consistent, the template's qualifier-check lines and Step 7's fallback field add "no warrant to compare".
- **N4 applied.** Step 7's last line names C; the template's closing line quotes C to match.
- **N5 applied.** theory.md §4 grounds the departure in the assistant not knowing whether its reconstruction is the implicit premise, with the user's word the only evidence.
- **N6 not applied (spec.md out of scope).** For the batch owner: append to spec §5.8 Borders "; poking holes in an idea or plan to dia-brainstorm (an argument's support stays here)."
- **N7 applied.** Rule 3 takes the strength from the rule itself, not the claim's qualifier; Step 5 says when an overstatement follows from the "generally" default; the worked example and the template's qualifier check say it too.
