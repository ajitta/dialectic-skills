# Token fix report: dia-intent

File edited: `skills/dia-intent/SKILL.md` only (no `references/` exist). Frontmatter, description, `agents/openai.yaml` and `metadata.version` (1.0.0) untouched. LF endings kept; no Hangul.

## Items

| Id | Change | Status |
|---|---|---|
| R1 | Cut "Facts you can investigate and choices already delegated are not reasons to propose this." (dependent-decisions bullet 1) | Applied as proposed |
| R2 | Cut "; if they do, it belongs in evidence and assumptions." (item 3, bullet 1); sentence now ends after the parenthesis | Applied as proposed |
| R3a | Cut template bracket "[Intended outcome, scope, and completion criteria.]"; bold label kept | Applied as proposed |
| R3b | Cut template bracket "[Only what remains open, with its effect. Omit if nothing remains.]"; bold label kept | Applied as proposed |
| R3c | Template bracket shortened to "[As item 2; mark values worked out without a tool as re-derived.]" | Applied as proposed (exact text) |
| O1, O2 | Optional cuts | Declined (owner decision: recommended set only) |
| O3 | Not recommended | Declined |
| Dependent-decisions move to a reference | Not recommended / owner decision | Declined; block stays in SKILL.md |

All proposed texts matched the file exactly; no adaptation needed.

## Token counts (cl100k_base, tiktoken)

| Text | Before (HEAD) | After | Delta |
|---|---|---|---|
| SKILL.md body (after closing `---`) | 1,782 | 1,708 | −74 (4.2%) |
| SKILL.md whole file | 1,896 | 1,822 | −74 |
| References | none | none | – |

Matches the audit's predicted 74 cl100k (≈110 Claude tokens per invocation).

## Labels and safety checks

- D19 "re-derived" label kept in item 2 and in the shortened Evidence template bracket; "unverified assumption" wording, D20 sent/spent and recipient, D23 open-ended limit untouched.
- Meta guard, all examples, all rationale units, l.54 partial-approval restatements and the Confirmation bracket kept.
- Nothing moved to a reference, so the skill still works when references cannot be opened.

## Gaps / notes

- The Goal and Decisions template slots are now bare bold labels followed by a blank line. That reads fine as a section skeleton, but the template no longer carries a cue for those two sections; the model relies on items 1 and 3 above.
- Follow-up outside this task's scope (per the audit): regenerate `plugins/dia/` and the zip; consider a spec D-row noting "template brackets reduced to non-redundant cues; no rule change"; re-run the probes Part A dia-intent cells, adding a delegated-choice + date/total cell (R3c) and a dependent-decisions cell (R1).
- `git diff --stat` in the worktree also shows dia-negative and dia-refine changes; those are from other implementers, not this task.
