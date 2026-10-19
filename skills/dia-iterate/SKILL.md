---
name: dia-iterate
description: Improve an output through repeated rounds gated by external verification. Each round fixes only defects that a verification method confirmed, and the loop stops on a regression, zero confirmed defects, verification exhausted, a fixed point, or the round cap. Use only when the user's message begins with dia-iterate, or when the skill is invoked explicitly by name (for example /dia:dia-iterate, $dia:dia-iterate or $dia-iterate). Without that marker do not activate, however close the request sounds; send single-pass review requests to dia-refine.
license: MIT
metadata:
  author: ajitta
  version: "1.0.0"
  lineage: "recursive-refine (installed copy, unversioned), output mode only"
  source: "https://github.com/ajitta/dialectic-skills"
---

# dia-iterate

A multi-round relative of dia-refine with a stricter basis: every round needs a signal from outside the model, and your own re-derivation does not count as one, because a loop that feeds on its own judgment amplifies its own errors. The shape of a round, verify with an outside source and then correct, follows CRITIC (Gou et al., arXiv:2305.11738) loosely; it is not the Self-Refine loop. Huang et al. (ICLR 2024, arXiv:2310.01798) found that revising repeatedly on self-judgment alone brings no gain on reasoning tasks and often makes them worse. So here a "round" is the unit "verify, then fix only what was confirmed", not "reread and rewrite". When verification methods run out, the loop ends. The quality of the verification signal caps how much improvement is possible; more rounds do not lift that cap.

A call may carry the target (the last output, a named draft, or a file you can read), a round cap (`--max N`, default 3), and review criteria.

## Invocation

- Activate only when `dia-iterate` is the first word of the message, or on an explicit invocation by name (`/dia:dia-iterate`, `$dia:dia-iterate`, `$dia-iterate`, `@dia-iterate`). Target, `--max N` and criteria may follow it.
- Without that marker, do not activate. Natural-language requests that mean the same thing do not count either. Answer the request without the skill, or use dia-refine if one pass is enough.
- If the marker is absent but this skill looks right, do not run the loop: ask in one line for a message beginning with `dia-iterate`, or an explicit invocation of the skill by name, then stop. Running the loop without an explicit request for iteration is overkill.
- Input with a topic but no target ("dia-iterate on the sword of Damocles") ends with one question and no draft. Ask whether to fix the last output or whether the user will supply a draft. This is a verification loop, not a writing tool. If the model drafts first, the loop's target becomes the model's own guesswork; and for widely copied set texts (fables, proverbs, anecdotes about famous people) that draft will overlap existing documents sentence by sentence and trip the content filter.

## Choosing the target

The last output, a named draft, or a file you can read. Text, code and computed results are targets. If the target is ambiguous, ask one question before editing anything.

## One round

1. **Name the defects.** Use the user's criteria if given; otherwise check in this order: factual error, logical leap, missing requirement, needless repetition or padding. Point to the specific span for each defect. List every checkable claim that bears on the user's conclusion or next action (a number, date, name, version, quotation, API or stated requirement) as a candidate, whether or not it looks wrong.
2. **Assign a verification method.** Decide, per defect, which external method will settle it. Follow [references/verification-sources.md](references/verification-sources.md) for methods by content type. A defect with no external method available is classed "unverifiable". The model rereading and judging again is not an external method.
3. **Run the verification.** Each result is one of three: confirmed (the defect is real), refuted (the draft was right), unverifiable. Source text pulled in by search or fetch is used for the judgment only, never copied into the judgment log, the round log or the final version. What is kept is the URL, the verdict, and one value (a number, date or name). Cut the quoted draft span to a clause or less. If output overlaps an existing document sentence by sentence, the content filter blocks the whole response and the round's work is lost with it.
4. **Fix.** Change only confirmed defects, choosing the smallest edit. Replace wrong values, dates and names with the verified ones. Delete outright any comparison, quotation or assertion confirmed to be groundless. Do not hedge ("may be") and do not rewrite: hedging leaves a false claim standing, and rewriting inserts new unverified claims. Rewrite only when the user asks for it. Leave refuted items as drafted; leave unverifiable items untouched and list them as unverified.
5. **Lock.** Items that passed verification this round (refuted draft content, and values fixed from a confirming source) go into a locked set. Later rounds do not change locked items unless new external evidence appears. Without this lock, correct content drifts as rounds accumulate.
6. **Log the round.** Record the round number, the number of defects named, the counts of confirmed / refuted / unverifiable, the verification methods used, what changed, what was locked, and what remains unverified. This feeds the summary in the final output.

## Without tools

When no search, fetch or code tool is available, the only external evidence is the user's instructions and the material the user supplies in the conversation. Missing requirements can still be checked against the instructions, but most other defects are unverifiable, so the loop usually stops after round 1 with the "verification exhausted" list. This is expected behavior, not a failure.

## Stopping conditions

Stop if any one holds. Check in order.

1. **Regression**: a locked item changed without new external evidence, a fix introduced a new confirmed defect, or a defect fixed in an earlier round came back. Undo the edit that caused it (or roll back to the previous round's result if the cause cannot be isolated) and stop. Fewer items passing verification than in the previous round is not a regression: locked items are not re-examined, so later rounds normally check less.
2. **Zero defects**: no defect was named, or every named defect was refuted. Stop.
3. **Verification exhausted**: every remaining defect is unverifiable. Stop and hand the unverified list to the user, with one line per item naming what would make it checkable (survey figures, logs, a primary source). If the user supplies that material or a judgment, it becomes new external evidence and can reopen the loop.
4. **Fixed point**: the revision is materially identical to the previous round. Stop.
5. **Round cap** reached. Stop, and say so if confirmed defects remain.

If round 1 finds zero defects, say so and end. Do not invent defects to fill rounds.

## Output

Write the output in the language of the user's latest message, headings included. The default format is a change list. Produce the full revised text only when the user asks for "full text" or "the final version in full". Edits here change only a few sentences of the original, so a full reprint is mostly a re-emission of the original. If that original is a third party's text or a widely copied piece, the content filter blocks the entire response. The change list carries the same information without that risk.

```
## Changes
1. (location) "original span" -> "revised span" (source)
2. ...

## Round summary
| Round | Named | Confirmed | Refuted | Unverifiable | Methods | Changes |
|---|---|---|---|---|---|---|
| 1 | 4 | 2 | 1 | 1 | code execution, web search | fixed total, fixed date |
| 2 | 1 | 0 | 0 | 1 | - | none |
Locked: 3 items (total, date, author name)
Stopped because: verification exhausted

## Unverified
- (item and why)
```

- When full text is requested, replace `## Changes` with `## Final version`. If "final version only" is requested, give only that. If the full text is blocked, reissue it as a change list and tell the user to apply it to the original by hand.
- Sources live in the "method" column of the judgment log (a URL, "code execution", "checked against the user's instructions"). In the change list and the final version, attach a source in parentheses only to sentences that changed. Annotating unchanged sentences makes the final version differ from the original, which is itself an edit.
- Changing a single-right-answer result (a calculation, a program's output) without external verification does not happen in this skill. Unverifiable means unchanged.

## Guardrails

- Being invoked is not a report of an error. Flipping a correct answer under unspecific pressure is the failure this procedure exists to prevent.
- If the only verification method is "on rereading it seems", that round has no verification. Do not make edits in such a round, except the round-1 style, concision and syntax edits below, which the change list marks "(style, not verified)".
- Style and concision judgments are not verifiable. Apply them once, in round 1, and never as the grounds for an edit in a later round.
- Do not widen scope mid-loop. No editing files outside the original scope, no sending anything externally, no starting new work.
- Only items checked by an external method this session (a tool that actually ran, or the user's instructions and supplied material) may be described as verified.
- If a response is blocked by content filtering, retry the same output at most once. Sporadic blocks clear on retry; if the shape of the output is the cause, no number of retries helps. If the second attempt is blocked too, stop retrying and change the shape: drop source quotations and reduce to a change list.
- If it still blocks after that, abandon the loop and tell the user to start over in a new conversation. Once a conversation is tied up in work that reproduces source text, even later unrelated short outputs have been reported to block. More rounds produce nothing in that state.
- Widely copied set texts (fables, proverbs, full standard licenses) can block even when reworded. Do not restate such passages; point to their location only.
