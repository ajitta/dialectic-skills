# Token-audit fixes: dia-negative

Worktree `/home/ubuntu/work/dia-review/tokfix` (branch `tokfix`). Audit: `docs/research/token-audit/dia-negative.md` (tree `d5e9efa`; the skill files at HEAD matched it). Scope: the audit's recommended set only (owner decision 2026-10-20). Frontmatter, description, `agents/openai.yaml` and `metadata.version` (1.0.0) unchanged. No commits.

## Items

| ID | File | Status | Change |
|---|---|---|---|
| K1 | SKILL.md L14 | applied | Intro paragraph replaced by `No concept captures its object without a remainder.` (the "To think is to identify…" sentence and the "Critique works by…" sentence are gone; both are in theory.md §2). |
| K2 | SKILL.md L16 | applied | Dropped "; he held that his philosophy could not be reduced to a set of steps". The label "practical adaptation of Adorno's method, not Adorno's own procedure." stays. |
| K4 | SKILL.md L35 (Rule 3) | applied | "That C can be read two ways is not a finding by itself, because under one of the readings there may be no gap at all." → `Ambiguity alone is not a finding.` |
| K5 | SKILL.md L56 (Step 3) | applied | Dropped ", from the target's material first" (Rule 4 says it). |
| K6a | SKILL.md L98 (Targets) | applied | Removed the `user` bullet. |
| K6b | SKILL.md L100 (Targets) | applied | `text` bullet is now `- **text:** quote with location.` |
| K7 | SKILL.md Pitfalls | applied | Removed External critique, Mind-reading, Closure. Kept Abstract negation, Jargon, Dismissal by default, Filling the template. |
| K9 | output-template.md L3 | applied | → `Translate every heading and label into the user's language (Rule 9). Use numbered items and short lines so it reads on a phone.` |
| K10 | theory.md L3 | applied | Dropped the read-condition sentence ("Read this when the user asks about the method, …"); the translation/page-reference note stays. |
| K8 | SKILL.md L16 (Jaeggi/Stahl) | declined | Owner decision; not in the recommended set. Text unchanged. |

All proposed texts matched the file exactly; no adaptation was needed. Every D19–D23 label is intact: "practical adaptation … not Adorno's own procedure", "internal critique", the immanent-critique boundary and "does not reconstruct such norms", evidence classes, the falsifier, the self-examination guard, the dispute rule, and the template and record fallbacks. The audit's "not recommended" items were left alone. Files are LF-only and contain no Hangul.

## Token counts (cl100k, tiktoken)

| File | Before (HEAD) | After | Saved |
|---|---|---|---|
| SKILL.md body (after frontmatter) | 2,412 | 2,238 | 174 |
| SKILL.md whole file | 2,691 | 2,517 | 174 |
| references/output-template.md | 624 | 593 | 31 |
| references/theory.md | 2,116 | 2,086 | 30 |

The SKILL.md result matches the audit's measured 2,412 → 2,238. The audit put K10 at 31 tokens; the measured whole-file saving is 30 because of tokenization at the join.

## Lines shared with dia-reductio

These lines are byte-identical in dia-negative and dia-reductio at HEAD (dia-negative line numbers):

- L20 `` `--target=user|claude|text|all` sets what is examined. `` (unchanged)
- L22, L25, L27: Parameters table header and the `claude` and `all` rows (unchanged)
- L98 `- **user:** follow the procedure as written.`: **cut here (K6a)**. The dia-reductio audit cuts the same line (S7), so the two skills stay aligned if that item is applied too.
- L108 `- **The user asks about the method:** answer from the theory reference, briefly.`: **kept here**, because my audit marks it load-bearing. The dia-reductio audit cuts it (S8) and folds "briefly" into its L16. If the other agent applies S8, the two skills will differ on this line. That needs an owner decision on whether to align them; I did not touch it, since cutting it is not in the dia-negative recommended set.

## Gaps and notes

- K6b and K7 remove the only `--target=text` specific guidance on author intent, and three pitfalls. The audit's risk table says no current probe covers `--target=text`, and K7 is rated medium-low risk. The P7 negative cells and a `--target=text` mission-statement run would check these (audit "Risks").
- K1 and K2 leave a method question asked while theory.md is unreadable with only the L16 labels to answer from. Audit check: P8 with a "what method is this?" follow-up.
- Nothing regenerated: `tools/package.py` was not run, so `plugins/dia/` now lags the source until it is regenerated.
