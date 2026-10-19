# dia-brainstorm: token-audit recommended set (applied)

Source audit: `docs/research/token-audit/dia-brainstorm.md`. Worktree: `/home/ubuntu/work/dia-review/tokfix` (branch `tokfix`). Only `skills/dia-brainstorm/SKILL.md` and `skills/dia-brainstorm/references/question-bank.md` changed. Frontmatter, description, `agents/openai.yaml` and `metadata.version` ("1.0.0") are untouched. No commit was made.

## Items

| Item | Status | Change / reason |
|---|---|---|
| S9 | Applied (exact) | Deleted " Required at least once in `stress`." from the Falsification pull tactic (L66). The same rule stays in Rhythm (L72: "In `stress`, do at least one falsification probe."). |
| S17 | Applied (exact) | Deleted the Pitfalls bullet "**Wall of text on a phone**: if a turn needs scrolling, cut it." (L115). Rule 2 still says "A turn fits a phone screen without scrolling." The file still ends with one LF. |
| Q1 | Applied (exact) | Deleted "- **Edges** (Step 3): cheapest version · most extreme version · do nothing." from question-bank.md:57. SKILL.md Step 3.2 still lists the same three edges. |
| S1–S3 (L16 rewording) | Declined | This needs the owner's OK, and the owner did not approve it. L16 is unchanged, so every D19 label, the midwife sentence and the dia-elenchus route are kept word for word. |
| S6, Q2, B1, B2 (optional) | Declined | The audit marks these optional and does not recommend them. |
| All "Keep" items | Untouched | — |

## Token counts (tiktoken cl100k_base)

| File | Before (HEAD) | After | Δ |
|---|---|---|---|
| SKILL.md body (no frontmatter) | 2,695 | 2,669 | −26 |
| SKILL.md whole file | 2,963 | 2,937 | −26 |
| references/brief-template.md | 465 | 465 | 0 |
| references/question-bank.md | 725 | 706 | −19 |

These match the audit's forecast for the safe set: S9 + S17 = −26 per invocation (≈ −39 Claude tokens) and Q1 = −19 when the bank is read. That is about 1.0% of the body.

## Checks

- No CR characters in either file, so line endings are still LF. No Hangul was added, and the text stays assistant-neutral.
- Neither diff touches frontmatter, the routing paragraph (L37) or L16, so P7 routing cannot regress.

## Gaps / notes

- No probe covers multi-turn brainstorming. The audit's suggested checks still apply: a `stress` session should include at least one falsification probe, and every turn should fit a phone screen. These are the S9 and S17 behaviours.
- With S17 gone, the turn-length rule appears only once in the body, in Rule 2.
- `git diff` in the worktree also shows edits to other skills (intent, iterate, negative, refine). Other implementers made those; I did not touch them.
