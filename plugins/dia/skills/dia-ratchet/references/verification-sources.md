# Verification method assignment

Which methods count as "external verification" for each type of content. One criterion governs: information or execution results that differ from what the model used while drafting.

| Content type | Accepted external method | When no method exists |
|---|---|---|
| Calculations, figures, totals, unit conversions | Recompute by running code | Unverifiable. Leave as drafted |
| Code | Execution, tests, type checking, linter. Tests you write yourself share your blind spots: prefer existing or user-supplied tests, and say which kind ran | Unverifiable without a run environment |
| Library APIs, versions, config keys | An official-documentation lookup tool, or a fetch of official docs | Unverifiable |
| Facts, dates, a person's current position, recent events | Web search, then fetch a primary source | Unverifiable |
| Quotations, citations, paper titles and authors | Fetch the original, or open a bibliographic record (publisher, DOI or library catalogue page) | Unverifiable. Exact titles and numbers in particular stay unverified however fluently they came to mind |
| Statements about the user's system, code, or situation | Compare against files, logs, and user statements in the conversation | Unverifiable if there is nothing to compare against |
| Missing requirements | Compare against the user's latest instructions | The instructions are themselves external evidence, so almost always possible |
| Logical leaps | Build a counterexample as concrete input and check it by calculation or execution | Unverifiable. A counterexample you cannot run is not grounds for an edit; list the leap among the unverified items with the counterexample |
| Style, concision, tone | Compare against criteria the user supplied | Unverifiable. Leave as drafted |
| Human feedback: requirements, scope, tone, audience, facts about the user's own system, code, or situation | Evidence in itself. If it conflicts with material in the conversation (pasted code, logs, docs), show the conflict before adopting it | - |
| Human feedback: claims about the world ("I remember it was from 3.6") | Single source. Verify by the method for that content type above, then adopt. If a primary source contradicts it, that source settles the draft's claim like any other defect. If the user produces a different primary source, that is new evidence | Unverifiable. Keep the draft and note the user's claim alongside it among the unverified items |
