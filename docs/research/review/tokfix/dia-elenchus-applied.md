# Token-audit fixes: dia-elenchus

Worktree `tokfix`. Audit: `docs/research/token-audit/dia-elenchus.md`. Owner decision 2026-10-20: apply the recommended set. The owner also approved creating `references/theory.md` and moving the citations there (audit owner decision 1, including the D23 "cited to Aristotle" citation; its label stays in SKILL.md). O1–O3 were not applied. The frontmatter, description, `agents/openai.yaml` and `metadata.version` 1.0.0 are unchanged.

## Items

| Item | Status | Note |
|---|---|---|
| E1 intro, l.14 | adapted | Used the audit text, but changed the read condition from "read it only if the user asks about them" to "read it only if the user asks about the sources or the method", following the owner's instruction (+3 tokens). The pointer is a Markdown link. The D23 scope label survives as "instead of a virtue", the L3 "aids, not the method" label and the anti-"question types" line are kept. |
| E2 addition/midwife, l.23 | applied | Exact text. The D19 "adds one thing the dialogues do not have" label and the D23 midwife departure ("stricter than the Theaetetus midwife") are kept. |
| E3 "You don't know", l.27 | applied | Exact text. The exhortation departure is kept as a label. Apology 21d, the Aristotle *Soph. El.* 183b citation and Apology 29d moved to theory.md §2 (owner-approved). |
| E4 irony, l.28 | applied | "Drop Socrates' irony:" (the drop label is kept). Republic 337a moved. |
| E5 sincere assent | applied | Crito 49c-d and Gorgias 495a moved. |
| E6 brevity | applied | Protagoras 334c-335c moved. Dropped ", which also suits a phone" (a repeat of Rule 2). |
| E7 statements, not the person | applied | Exact text. The D19 label is kept as "(narrower than Socrates, who also tested how people lived)". Charmides 166e and Laches 187e-188a moved. |
| E8 Step 2 | applied | Euthyphro 6d-e and Meno 72a-c moved. |
| E9 Step 3 | applied | The Laches Scythians example moved to theory.md §1. |
| E10 Step 5 | applied | "stricter than Socrates … here the user's own wording is the point" is kept. Euthyphro 9d and Laches 192d moved. |
| E11 Step 6 | applied | Meno 84a-c and Theaetetus 210b-c moved. The instruction stays. |
| P1–P6 patterns | applied | Exact texts. P2: Meno 86e-87b moved to theory.md. P4: the template is now a quote block and the code-block warning is gone. The D22 numbering (① definition, premises from ②) and the Laches 192b tag are kept. |
| R1–R3 record | applied | Exact texts. R2 points to SKILL.md Step 6, which still holds the full label criteria (the P8 fallback). The template's two "name …" clauses are kept. |
| O1–O3 | declined | Owner decision: held until a multi-turn probe exists. |
| New `references/theory.md` | created | §1 method and scope, §2 stance and departures, §3 this skill's additions, then Sources. It holds every moved locus with the label it supports. |

The audit marks the P and R items as needing no owner decision, so they count as part of the recommended set.

## theory.md Sources

Every URL is copied from `docs/research/dia-elenchus.md`: the Perseus Fowler/Lamb section pages (Shorey for the Republic), one per work, and IEP "Socrates" for Aristotle's report. Charmides 166e, Euthyphro 9d, Laches 192d and Theaetetus 157c-d have no URL of their own in the repo; the reviews in `docs/research/review/` checked them on Perseus. The section therefore says that other loci are other sections of the same Perseus text, and no URL was made up for them.

## Token counts (cl100k_base)

| File | Before (HEAD) | After | Δ |
|---|---|---|---|
| SKILL.md body | 2,698 | 2,444 | −254 (audit predicted −258; +3 from the E1 read condition, +1 from how the body is split) |
| SKILL.md with frontmatter | 2,992 | 2,738 | −254 |
| references/elenchus-patterns.md | 1,010 | 905 | −105 (matches the audit) |
| references/record-template.md | 532 | 394 | −138 (matches the audit) |
| references/theory.md | — | 1,156 | new |

Per invocation the saving is 254 cl100k (≈ 380 Claude tokens), and a session that reads the patterns and the record saves about 500.

## Gaps and notes

- **The worst case rises.** theory.md is 1,156 tokens, not the audit's ~488 draft, because the Sources section carries 11 Perseus/IEP URLs (about 600 tokens). When every file is read, the total goes from 4,240 to 4,899 (+659), where the audit had projected no rise. theory.md is read only when the user asks about sources or the method. If the worst case matters, dropping the URLs and keeping the editions alone would bring it near 500.
- The link `[references/theory.md](references/theory.md)` resolves to the new file. `tools/package.py` was not run, as instructed.
- No Hangul. LF line endings. The trailing newlines are preserved.
- Spec §5.2 still says "References carried over: `elenchus-patterns.md` and `record-template.md`". It needs a theory.md line and a D-row (audit owner decision 1). Both are outside my scope (docs/).
- No probe has validated the shortened labels yet (audit Risks: the multi-turn lunch/retro run, and a "where does the no-advice rule come from?" turn that should open theory.md).
