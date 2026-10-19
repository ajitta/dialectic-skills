# Token-audit application: dia-reductio

Worktree `/home/ubuntu/work/dia-review/tokfix` (branch `tokfix`). Audit: `docs/research/token-audit/dia-reductio.md`. Only files under `skills/dia-reductio/` were edited (SKILL.md, references/output-template.md, references/theory.md). Frontmatter, description, `agents/openai.yaml` and `metadata.version` (1.0.0) are unchanged. No commits, no packaging run.

## Items

### SKILL.md

| # | Status | What changed |
|---|---|---|
| S1 | applied | L14 second sentence ("Then show the user which members … let the user decide.") cut. |
| S2 + S8 | applied | L16 rewritten to the audit's text: plain code paths instead of markdown links, "Theory, history and …" (comma dropped as proposed), "(then answer briefly)" folded in. The follow-up bullet "**The user asks about the method:** answer from the theory reference, briefly." cut. |
| S3 | applied | R5 "Refuting a weaker reading is a strawman." cut. Pitfall "A strawman from testing the weak reading." kept (S9: keep one of the two). |
| S4 | applied | R6 "A contradiction shows only that the thesis and the premises cannot all be true together." cut; the bold title and the operative sentences stay. |
| S5 | applied | Step 5: the `e.g. "Lines 4 and 7: …"` replaced by "; mark each [A] member." |
| S6 | applied | "This is the strongest result." cut from the `internal` grade. |
| S7 | applied | Targets "- **user:** follow the procedure as written." cut. |
| S9–S17 | kept (audit: keep) | Own-scheme label (D22), L57 independence non-claim, L59 intuitionistic note (D23), worked example, pitfalls, Rule 1 example and parenthetical, Step 8 field list, Step 4 "Checked by" clause all untouched. |

### Owner-approved moves from theory.md (audit §5 gap)

| Source | Status | Text added to SKILL.md |
|---|---|---|
| theory.md §4 L43 (rule or practice) | applied | Step 3, before "Keep the list …": "For a rule or practice, list its stated aim or another stated rule as a premise; its generalized application must contradict that." (25 tokens) |
| theory.md §6 L51 (per impossibile) | applied | End of Step 1: "If the user only explores consequences, call it *per impossibile* reasoning and claim no refutation." (21 tokens) |

Together 46 cl100k, above the ~30 estimate. Shorter variants (19–22 tokens each) were tried; they saved 3–5 tokens but read worse ("is a premise its generalized application must contradict"), so the clearer forms were kept. theory.md §4 and §6 are unchanged (explanatory text kept, including the original sentences).

### output-template.md

| # | Status | What changed |
|---|---|---|
| O1 | applied | L3 now "Translate headings and labels per Rule 8. Use numbered lines, not wide tables, so it reads on a phone." (The dropped "Keep the target's quotes in their original language" is covered by Rule 8's "Quote the target in its original language".) |
| O2 | applied | `(Direction "both": one Contradiction and Strength line per direction.)` cut. |
| O3–O5 | kept (audit: keep) | — |

### theory.md

| # | Status | What changed |
|---|---|---|
| T1 | applied | §8 "Failure modes to watch" cut; §9 "Hard cases" renumbered §8. No file in the skill refers to either number (checked by grep). |
| T2 | applied | L17 now "**This skill allows only the first** (SKILL.md Rule 1 says how a falsehood or implausibility is made strict)." |
| T3–T6 | kept (audit: keep) | Sources, history, hard cases, §1–§6 untouched. |

No item was adapted or declined; all proposed texts matched the files.

## Token counts (tiktoken cl100k_base)

| File | Before (HEAD) | After | Delta |
|---|---|---|---|
| SKILL.md body (no frontmatter) | 2,882 | 2,819 | −63 |
| SKILL.md whole file | 3,136 | 3,073 | −63 |
| references/output-template.md | 623 | 593 | −30 |
| references/theory.md | 2,034 | 1,877 | −157 |
| Typical invocation (body + template) | 3,505 | 3,412 | −93 |

The recommended set alone matches the audit (body 2,882 → 2,773, −109; template −30; theory −157). The two owner-approved additions put back 46, so the net body saving is 63. Lines: SKILL.md 135 → 133, template 54 → 53, theory 84 → 75. LF endings and no Hangul confirmed.

## Lines shared with dia-negative

- S7: the Targets bullet "- **user:** follow the procedure as written." (byte-identical in dia-negative) is **cut** here. The parallel dia-negative change in the worktree also cuts it, so the two still match.
- S8: the follow-up bullet "- **The user asks about the method:** answer from the theory reference, briefly." is **cut** here, with "briefly" moved into the L16 pointer sentence. In the current worktree, dia-negative **keeps** it (L107), and its L16 still uses markdown links without "briefly". So the two skills now differ on this line. Whoever reconciles them should decide whether dia-negative applies the same S2+S8 pair.

## Gaps noticed

- Audit §5 still applies: no probe runs dia-reductio without references, so S5 (the [A] marks in the depends-on line) and O1/O2 are not covered by any probe. The suggested cell (`--tools Skill`, plus a "both" run) is still missing.
- The two new SKILL.md lines (rule or practice, per impossibile) have no probe either.
- Version: kept at 1.0.0 under the pre-release exception in AGENTS.md. A release still needs the version rule applied.
