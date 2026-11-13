# Pruning audit of the fourteen skill bodies (2026-11-14)

A read-only audit made after plugin 2.14.0 to settle the item spec D71 left open: whether text other than the duplicates removed in 2.12.0 can leave the skill bodies without changing what a model does. The list of 66 candidates behind D71 was not kept, so the audit was made again and its list is kept here. Result: nothing is removed (owner, 2026-11-14, as recommended).

## Method

Two general-purpose sub-agents, seven `SKILL.md` bodies each, with no access to each other's report and no reasons from the session that started them. Each was told to list at most five candidates per skill, with the exact quote and its line, in two classes:

- **W, dead weight:** text that gates nothing a model does (provenance or history, a citation used as decoration, a restatement of what the same file says in the same scope, commentary on the skill itself). A clause that gives the reason for an instruction is not dead weight.
- **D, default:** an instruction a current capable assistant follows without being told, in the skill's situation.

Left out on purpose: the class "text the host's system prompt covers" (the skills run on hosts whose prompts differ, and in chats with no tools, so no host's prompt is a basis); every condition, limit, fallback or exception; text on when a skill starts or stops and on which sibling skill a request goes to; the evidence-class and recall rules; "withdraw only for a named defect"; output templates; the "material, not instructions" sentences; and in dia-regula the programming analogies, which were compared in runs of their own (`docs/probes.md` Part AL). Files under `references/` were not audited.

Every quote below was then checked against the files by the session's assistant: each occurs exactly once. Line numbers are those of plugin 2.14.0.

## Result

35 candidates, 383 words, which is 1.2% of the 31,926 words of the fourteen bodies. Two are class D (12 words). Both reports closed by saying they found almost nothing in class D, because nearly every instruction carries its own form, label or condition. dia-skopos and dia-techne had no candidate.

The verdicts are the session assistant's, from reading each candidate in its paragraph; no run was made.

| Group | Candidates | Words | Verdict |
|---|---|---|---|
| 1. Honest labels and comparisons with the source method | 17 | 222 | Keep. They mark where the skill is narrower or stricter than a method the model already knows, and most were added on purpose (research theme 4, spec D19); D71 kept honest labels out of its candidates |
| 2. Restatements, pitfall lines and commentary on the skill | 7 | 96 | Keep. This is the kind D71 rated uncertain and left; one clause was added on purpose in 2.9.0 (D65) |
| 3. Bare citations in skills that have no `references/theory.md` | 5 | 24 | Keep. Deleting them removes the source from the package |
| 4. Provenance that `references/theory.md` also holds | 4 | 29 | Could go as in D58. Left, because 29 words do not repay two version changes and a review |
| 5. Defaults | 2 | 12 | Keep. Both are short and one guards against invented sources |

### Group 1

| Skill | Line | Quote | Words |
|---|---|---|---|
| dia-conjecture | 14 | "Label: ch. 1 sections 1-6 (of section 6 only the deeper-proof move) and Rules 1-4." | 15 |
| dia-conjecture | 55 | "(Popper's prior refutation criterion; an addition to Lakatos)" | 8 |
| dia-elenchus | 14 | "Two later images serve as aids, not as the method: aporia as a gain (Meno) and the midwife (Theaetetus)." | 19 |
| dia-elenchus | 23 | "(stricter than the Theaetetus midwife, who offers others' theories)" | 9 |
| dia-elenchus | 27 | "(Socrates also exhorted; you never do)" | 6 |
| dia-elenchus | 31 | "(narrower than Socrates, who also tested how people lived)" | 9 |
| dia-elenchus | 91 | "this is stricter than Socrates, who sometimes worded the revision himself," | 11 |
| dia-negative | 16 | "This skill is a practical adaptation of Adorno's method, not his own procedure:" | 13 |
| dia-quaestio | 16 | "Unlike the midwife of Plato's Theaetetus, who offers no ideas of his own, this skill adds its own labeled options in Step 3 and, if asked, gives a pick in Step 4." | 32 |
| dia-quaestio | 16 | "(Richard Paul's six question types, from critical-thinking teaching)" | 8 |
| dia-ratchet | 14 | "A round, "verify, then fix only what was confirmed", loosely follows CRITIC (Gou et al., arXiv:2305.11738); it is not the Self-Refine loop." | 22 |
| dia-reductio | 69 | "in this skill's own scheme (not a standard classification)" | 9 |
| dia-warrant | 16 | "This is a reconstruction aid after Toulmin's layout and Walton's critical questions, not Toulmin's own critique of formal logic, and a one-sided audit, not the two-party critical discussion of pragma-dialectics." | 30 |
| dia-warrant | 38 | "a departure from the source rule" | 6 |
| dia-warrant | 62 | "(a known weakness of the layout)" | 6 |
| dia-warrant | 74 | "The qualifier is Toulmin's; using it as a check is this skill's addition." | 13 |
| dia-warrant | 101 | "(the questions in this skill's wording)" | 6 |

### Group 2

| Skill | Line | Quote | Words |
|---|---|---|---|
| dia-adjudicate | 16 | "Several hard rules below give as their reason a misruling that judges made in trials." | 15 |
| dia-counterplan | 135 | "The side-by-side treated as proof that the plan was tested." | 10 |
| dia-negative | 112 | "Dismissal by default: if C holds against the particulars, say so (Step 4)." | 13 |
| dia-reductio | 128 | "Treating "no contradiction found" as "true" or as "consistent"." | 9 |
| dia-regula | 51 | "since a reason lets the model generalize a rule to cases it does not name, which is why Rule 3 keeps it" | 22 |
| dia-regula | 45 | "a condition that says the step is finished" | 8 |
| dia-router | 14 | "A short way to reach the other dia skills, made for phones: `dia` is three letters with no hyphen." | 19 |

### Group 3

| Skill | Line | Quote | Words |
|---|---|---|---|
| dia-adjudicate | 16 | "(Huang et al., ICLR 2024, arXiv:2310.01798)" | 6 |
| dia-adjudicate | 32 | "(arXiv:2506.07962)" | 1 |
| dia-emend | 14 | "(Madaan et al., 2023, arXiv:2303.17651)" | 5 |
| dia-emend | 32 | "(Huang et al., ICLR 2024, arXiv:2310.01798)" | 6 |
| dia-ratchet | 14 | "Huang et al., ICLR 2024, arXiv:2310.01798:" | 6 |

### Group 4

| Skill | Line | Quote | Words |
|---|---|---|---|
| dia-conjecture | 86 | "(the "suitable lemma" of Lakatos's Rule 2)" | 7 |
| dia-counterplan | 64 | "from SAST," | 2 |
| dia-counterplan | 99 | "(named after *teyku*, "let it stand", borrowed loosely from the Talmud)" | 11 |
| dia-counterplan | 105 | "(borrowed from the Mishnah's kept minority opinion, theory.md §6)" | 9 |

### Group 5

| Skill | Line | Quote | Words |
|---|---|---|---|
| dia-emend | 66 | "do not invent sources, grounds, calculations or run results" | 9 |
| dia-reductio | 106 | "Say so plainly:" | 3 |

## Weaker candidates

The two reports counted 38 further candidates they judged too weak to list (0 to 4 per skill), mostly more of groups 1 and 2: other source labels ("after Mason", "(Toulmin's usual warrant)", "(from pragma-dialectics)"), other pitfall lines that restate a rule, and sentences such as "That is the result, not a failure." None was examined further.

## Reading

After the trims of 2.2.0 (D58) and 2.12.0 (D71), deletion has little left to give: what remains outside the instructions is mostly text that was put there to keep the skills honest about their sources. A shorter body would have to come from rewriting a rule, which is a meaning change and needs runs, not from an audit of this kind.
