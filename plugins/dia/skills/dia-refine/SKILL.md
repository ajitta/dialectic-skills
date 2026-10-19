---
name: dia-refine
description: Review the previous answer or a named draft once, checking in order for factual errors, logical leaps, missing requirements and needless repetition, and return one integrated revision that fixes only defects whose basis was confirmed. Use when the message starts with dia-refine, or when the user asks to review the previous answer as a draft, fix factual errors and logical leaps, recheck or revise the previous answer, treat it as a draft, give only the improved final version, or do a task the dia-refine way, or the same in any language. A passing mention of dia-refine in the middle of a sentence is not an invocation. Repeated verification rounds belong to dia-iterate.
license: MIT
metadata:
  author: ajitta
  version: "1.0.0"
  lineage: "self-refine (installed copy, unversioned)"
  source: "https://github.com/ajitta/dialectic-skills"
---

# dia-refine

Treat the last output as a draft, find its defects, and produce one integrated revision that fixes only the confirmed ones. This is a single-pass procedure. Change is not improvement in itself, and a request for review is not in itself a sign of error. The skill must work in a chat with no tools (mobile apps included), so verify only as far as the available tools allow and leave the rest marked unverified.

## Invocation

- Explicit: the message starts with `dia-refine`. What follows is the review criteria, for example `dia-refine — check the numbers` or `dia-refine for tone`. `/dia:dia-refine`, `$dia:dia-refine`, `$dia-refine` and `@dia-refine` also count.
- Natural language: "review your previous answer as a draft", "fix factual errors and logical leaps", "give me only the improved final version".
- A task with no draft yet: "do this task the dia-refine way" means first write a candidate answer, check it once by the procedure below, and give only the final version. Show the review only if the user asks for it.
- A dia-refine mentioned in passing in the middle of a sentence is not an invocation. Requests for several rounds belong to `dia-iterate`, not to this skill.

## Target

The last output, or another target the user names (a draft, a file, a specific answer). If the target is ambiguous, ask one question and stop before changing anything.

## Procedure

1. **Requirements.** From the latest user instruction, build an internal checklist: deliverable, format, scope, audience, constraints. Do not print it. Deliberate choices in the draft (tone, structure, terminology) are kept unless they conflict with a higher instruction or a confirmed fact.
2. **List every defect candidate.** Use the user's criteria if given; otherwise check factual errors → logical leaps → missing requirements → needless repetition and circumlocution, in that order. Do not filter by severity at this step. Starting out to "find only the important ones" makes you find fewer, so list every candidate and filter in step 4. Point each candidate at its span in the draft. Include the premises the draft rests on as candidates.
3. **Verify.** Re-derive logic and calculations independently; this needs no tools. Check numbers, dates, names, quotations, versions, library APIs, code and recent events if a search, code-execution or file tool is available. Do not skip a search because a name is familiar: the more familiar it feels, the more plausible a stale answer sounds. One check per item is enough; do not add verification rounds for incidental details. Your own recall is not verification: a fact you remember differently from the draft is unverified, however sure you are. Items you have no tool for, or could not check, stay as drafted and are marked unverified; the mark goes in ④, not inside the revision (in "final version only" mode, in the closing line when it bears on the user's conclusion). Never write "verified" for a check you did not run. Do not launch subagents to check your own work.
4. **Choose changes.** Of the candidates, fix only the defects and omissions whose basis was confirmed: by a tool that ran, by the user's instructions or supplied material, or by re-deriving the logic or calculation yourself. A suspected factual error you could not check goes under ④ with the correction you suspect; the revision keeps the draft's wording. Do not change correct facts, quotations, structure or tone without grounds. Do not turn uncertain content into an assertion or hide it; mark its limits. Do not mix style polishing with factual correction. For a concision request, remove only duplication, circumlocution and unneeded examples, without changing the meaning or the level of certainty.
5. **Integrated revision.** Produce one revision, check it against the checklist from step 1, and finish. Iterate further only on new evidence or specific feedback. Rechecking again and again only adds cost; the result does not improve.

## Output

Write the output in the language of the user's latest message, labels included; if that message has no text besides the invocation (the `dia-refine` marker or one of the names under Invocation), use the language of the conversation.

- Default: **defect list, then revision**. The defect list has four parts: ① confirmed errors ② missing requirements ③ correct content kept ④ remaining uncertainty. Tag each ① item with its basis: (tool), (user's instructions or material) or (re-derived). List individually only the items that change the user's conclusion or next action; group incidental fixes such as notation or style into one line. The list is a verdict on the draft, not a record of your thinking.
- On a "final version only" request: give only the revision. Do not show the review or a change log. One closing line may follow, and only if needed, naming what the user would otherwise not see: a single-right-answer result your own re-derivation changed (original and revised value, and the premise), what stayed unverified and bears on the user's conclusion (a suspected error with the correction you suspect, or a group such as "three benchmark figures unverified"), a problem outside the scope (see Safeguards), or, for a file target, the sources of verified items (see below). For "do this task the dia-refine way" there was no draft the user saw, so there is no original value to show.
- If nothing needs fixing, say so and give the reason. Do not make edits just to have something to show.
- When your own re-derivation, not a tool, changes a single-right-answer result (a calculation, the output of a code run), present the original and the revision side by side and state the premise the change rests on. Do not declare the revision better on your own judgment alone. The (re-derived) tag in ① is how the defect list shows this: the basis is your own working, not an outside check.
- For verified items, give the source next to the sentence concerned in the revision; for a file target, give it in your reply instead (the defect list, or the closing line in "final version only" mode), never in the file. Mark a source sentence copied word for word as a quotation; otherwise put it in your own words.
- Apart from added requirements (②) and necessary corrections, the revision has no reason to be longer than the draft. When shortening, drop content that does not affect the next action; do not break sentences into fragments or compress them into arrows and abbreviations.
- If the target is a file, fix only the defective passages instead of rewriting the whole file.

Example defect list:

```
① Confirmed errors
- "released March 2024" → May 2024 per the official release notes (tool; source: link)
- "total 1,240" → 1,420 (re-derived: 620 + 800; the draft added 620 + 620)
② Missing requirements
- The requested list of CSV column names is missing
③ Content kept
- Cost comparison table: figures recomputed and match; kept
④ Remaining uncertainty
- Three benchmark figures: no tool to check them; left as drafted, unverified
Incidental: 2 notation fixes applied
```

## Safeguards

- Being invoked is not a signal of error. It is a request for review, not an error report. Flipping a correct answer under pressure that has no specific grounds is the failure this procedure exists to prevent.
- No over-correction. Do not read the request as "something must change".
- Do not widen the scope during the review. Do not edit files outside the original scope, send anything externally or start new work, and do not invent sources, grounds, calculations or run results. If you find another problem worth fixing, keep it out of the revision and mention it in one line at the end.
- Judge creative work by its purpose, audience, tone and constraints instead of by objective errors.
