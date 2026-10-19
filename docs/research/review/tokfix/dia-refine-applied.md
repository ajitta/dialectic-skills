# dia-refine — token-audit core set, applied

Worktree: `/home/ubuntu/work/dia-review/tokfix` (branch `tokfix`). Audit: `docs/research/token-audit/dia-refine.md`, §4 core set.
Only file changed: `skills/dia-refine/SKILL.md`. Frontmatter, description, `metadata.version` (1.0.0) and `agents/openai.yaml` are untouched. No commit, no `tools/package.py`.

## Items

| # | Change | Status |
|---|---|---|
| 3+4 | Cut the intro's last sentence ("The skill must work in a chat with no tools (mobile apps included), so verify only as far as the available tools allow and leave the rest marked unverified.") | Applied as proposed. Step 3 still covers the tool-less behavior: re-derivation "needs no tools", tool checks are conditional, and unchecked items "stay as drafted and are marked unverified". |
| 7 | Cut the Invocation bullet listing natural-language triggers | Applied as proposed. The same phrases stay in the description. |
| 8 | Cut "A dia-refine mentioned in passing in the middle of a sentence is not an invocation." Keep the dia-iterate sentence | Applied as proposed. The bullet now reads "- Requests for several rounds belong to `dia-iterate`, not to this skill." |
| 21 | Cut "It is a request for review, not an error report." from the first Safeguards bullet | Applied as proposed. |

All four proposed texts matched the file exactly, so nothing had to be adapted.

Not applied, because they are outside the approved core set: #6 (invocation-form list and the change to the language fallback), #22 ("No over-correction" bullet), #1+#15 (arXiv IDs), and #9+#10 (step-2 reason wording). All D19–D23 labels stay in place: the Self-Refine label, the Huang citation, basis tags, the closing line, the subagent reason and the (re-derived) explanation. The worked example is unchanged.

## Token counts (cl100k_base, tiktoken)

| Part | Before (HEAD) | After | Δ |
|---|---|---|---|
| SKILL.md body (no frontmatter) | 1,929 | 1,836 | −93 (−4.8%) |
| SKILL.md whole file | 2,129 | 2,036 | −93 |
| References | none | none | — |

This matches the audit's predicted core total of −93.

## Checks

- No Hangul. LF line endings (no CR found). The file was written byte-exact, except for the four removals.
- The language fallback ("one of the names under Invocation") still resolves, because the form list was kept.

## Gaps noticed

- Spec §5.6 "Invocation" still lists the natural-language triggers and the passing-mention rule. After this change the body no longer repeats them; only the description carries them. Spec §5 requires these at the skill level, and the description satisfies that, but the spec does not say whether the body must also carry them. A spec note may be wanted when docs are updated.
- The audit's verification cells are not run yet: P8 (tool-less) for #3/#4, P6 (mid-sentence mention) for #8, and the proposed pushback cell for #21. No final-only or pushback probe exists.
- The worktree also contains uncommitted edits to dia-intent and dia-negative from other implementers. They were not touched.
