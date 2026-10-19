# Token-audit fixes: dia-iterate

Source audit: `docs/research/token-audit/dia-iterate.md`, recommended set (S1–S11, R1–R4). Not applied: S1b (marked not recommended / owner decision) and every item in the audit's "kept" lists. Frontmatter, description, `agents/openai.yaml` and `metadata.version` (1.0.0) are unchanged.

## Items

| Item | Status | Note |
|---|---|---|
| S1 | Applied | :14 paragraph replaced with the audit's exact text. D19 labels kept in place: "own re-derivation does not count", CRITIC (Gou et al., arXiv:2305.11738) "loosely", "not the Self-Refine loop", Huang et al. (ICLR 2024, arXiv:2310.01798) with "often". D23 lower-bound sentence kept verbatim. |
| S2 | Applied | :16 cut; Invocation bullet now reads "Target, `--max N` (round cap, default 3) and criteria may follow it." The default cap is stated once. |
| S3 | Applied | "Running the loop without an explicit request for iteration is overkill." cut. |
| S4 | Applied | Replaced with "Do not draft one yourself: the loop would then only check your own guesswork." It reads correctly after "...or whether the user will supply a draft." |
| S5 | Applied | "Long verbatim overlap can trip the host's content filter and lose the round's work." The observed-risk "can" is kept. |
| S6 | Applied | Lock rationale sentence cut. |
| S7 | Applied | Stop rule 2 now ends "Say so and stop."; "If round 1 names no defects, or refutes all of them, say so and end." cut. The D19/F3 sentence ("verification exhausted", not "zero defects") and "Do not invent defects" are kept. |
| S8 | Applied | "A full reprint mostly re-emits the original, and for a third party's or widely copied text the host's content filter can block the whole response." The change-list default is unchanged. |
| S9 | Applied | The annotating-unchanged-sentences rationale is cut. |
| S10 | Applied | The sporadic-blocks rationale is cut. "At most once" and "change the shape" are kept. |
| S11 | Applied | "Later outputs in such a conversation have been reported to block too." The observed-risk wording is kept. |
| R1 | Applied | Reference :3 second sentence cut; the criterion sentence is kept. |
| R2 | Applied | Reference :21 is now "One line per defect, within the limits of SKILL.md step 3." The log example is kept. |
| R3 | Applied | The "Quoting a whole source paragraph" misjudgment bullet is cut. |
| R4 | Applied | "Changing the sentence is an edit too." cut. |

None of the items needed adapting. Every proposed text matched the file and read correctly in context.

Spec §5.7 wording checks: the tool-less section still reads "This is expected behavior, not a failure." The invocation forms including `@dia-iterate`, the change-list default, the one-retry rule and the change-of-shape rule are all present. The output template, the compact summary, the single-right-answer rule and the round-1 style exception (step 4, Guardrails, reference row) are untouched.

## Token counts (cl100k_base, tiktoken)

| File | Before | After | Saved |
|---|---|---|---|
| SKILL.md body (after frontmatter) | 2,467 | 2,172 | 295 (12.0%) |
| SKILL.md whole file | 2,659 | 2,364 | 295 |
| references/verification-sources.md | 890 | 782 | 108 (12.1%) |

These match the audit's scratch-copy figures exactly. Before = `git show HEAD:<path>`. Both files are LF and contain no Hangul.

## Gaps noticed

- R2 makes the reference depend on SKILL.md step 3 for the log limits (clause-length draft span, no source text, URL + verdict + one value). That is safe because SKILL.md is always in context when the reference is read. The reverse dependency does not exist.
- After S4, the topic-without-target bullet no longer mentions set texts (fables, proverbs, anecdotes). Only the last Guardrails bullet covers them now, and it does not list "anecdotes about famous people". No probe covers this (the audit suggests a `dia-iterate on the sword of Damocles` probe).
- Re-check suggested by the audit: P6 and P8, n≥2, against the Part D results in `docs/probes.md`. These were not run here (CLIs were out of scope).
- `git diff --stat` also shows changes under dia-intent, dia-negative and dia-refine. Those came from other implementers, not this task.
