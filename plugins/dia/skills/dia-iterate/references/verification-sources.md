# Verification method assignment

Which methods count as "external verification" for each type of content. One criterion governs: information or execution results that differ from what the model used while drafting. The same model judging again from the same grounds is not external verification, and no edit is made on that basis alone.

| Content type | Accepted external method | When no method exists |
|---|---|---|
| Calculations, figures, totals, unit conversions | Recompute by running code | Unverifiable. Leave as drafted |
| Code | Execution, tests, type checking, linter | Unverifiable without a run environment. Fix only what is settled without running, such as syntax errors |
| Library APIs, versions, config keys | An official-documentation lookup tool (for example Context7), or a fetch of official docs | Unverifiable |
| Facts, dates, a person's current position, recent events | Web search, then fetch a primary source | Unverifiable |
| Quotations, citations, paper titles and authors | Fetch the original, or bibliographic data in search results | Unverifiable. Exact titles and numbers in particular stay unverified however fluently they came to mind |
| Statements about the user's system, code, or situation | Compare against files, logs, and user statements in the conversation | Unverifiable if there is nothing to compare against |
| Missing requirements | Compare against the user's latest instructions | The instructions are themselves external evidence, so almost always possible |
| Logical leaps | Build a counterexample as concrete input and check it by calculation or execution | A counterexample that cannot be run is weak verification. Apply once, in round 1, and never as grounds in a later round |
| Style, concision, tone | Compare against criteria the user supplied | Not verifiable. Apply once, in round 1 |
| Human feedback: requirements, scope, tone, audience, facts about the user's own system, code, or situation | Evidence in itself. If it conflicts with material in the conversation (pasted code, logs, docs), show the conflict before adopting it | - |
| Human feedback: claims about the world ("I remember it was from 3.6") | Single source. Verify by the method for that content type above, then adopt. If it conflicts with a primary source, show the source and keep the draft. If the user produces a different primary source, that is new evidence | Unverifiable. Keep the draft and note the user's claim alongside it in the unverified list |

## Judgment log format

One line per defect. Cut the draft-side span to a clause or less and do not quote the source's text. What is kept is the method (with URL), the verdict, and one value. Copying source sentences turns the log itself into a reproduction of an existing document and trips the content filter.

```
[defect 3] "total 1,240" - method: code execution - result: confirmed (actual 1,280) - action: fixed
[defect 4] "announced March 2024" - method: web search - result: refuted (draft was right) - action: locked
[defect 5] "this approach is faster" - method: none - result: unverifiable - action: unverified list
```

## Common misjudgments

- Writing "confirmed" on the strength of one search snippet. Secondary coverage repeating a single origin is not independent confirmation. Open the primary source, or mark it "single source" if only the snippet was seen.
- Editing because a different value came to mind than the draft's. When two recollections conflict, both are unverified.
- Quoting a whole source paragraph as the grounds for a confirmation. A judgment needs the value and the URL, not the paragraph.
- Softening a sentence by appending "needs checking" to an unverifiable item. Leave the text as it is and record it in the unverified list only. Changing the sentence is an edit too.
