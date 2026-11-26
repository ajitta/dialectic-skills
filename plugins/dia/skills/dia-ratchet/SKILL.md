---
name: dia-ratchet
description: Revise a target in rounds that move only on evidence from outside the model, so that the user knows which claims were checked. Use only when the message starts with dia-ratchet, or when the skill is invoked by name; a request that only sounds like this is not an invocation.
license: MIT
metadata:
  version: "4.0.0"
---

Revise a target in rounds that move only on evidence from outside the model: what a check confirmed is fixed and locked, and the rounds stop when no check can move anything more or when anything slips back. It is for the user to know, for what the target is for, which of the claims it depends on were checked from outside and which were not. Only a defect you name can be checked, and an error you would make yourself is unlikely to be named, so the confirmed defects are a lower bound, and a stop with none is not a clean bill.

## What it works from

The target: a text, code or a computed result, as the text or file the user names or pastes, or your last answer where they name none. With a topic and no target, ask one question, whether to work on your last answer or on a draft they will supply, and write none, because a draft of your own would leave the rounds checking your own guesswork. With it, the criteria the user gives, the round cap (`--max N`, three where none is given), and what the target is for, in the user's words; where they did not say, read it in one line and say the reading is yours, or say that none is stated. A purpose decides which defects are checked first and which unverified items are listed first; one you read in makes nothing a defect and is no basis for an edit.

Evidence is what comes from outside you: a tool that ran here, and what the user supplies. What the user supplies counts by what it is about. Their requirements, and their own system, code, data or circumstances that only they can know, are evidence in themselves, once any conflict with material in the conversation is shown. A primary source they supply (the original document, log or data the claim rests on, not a page that reports it) is evidence. A claim about the world, theirs or in a secondary source they hand you, is one source and is adopted only once a check confirms it; otherwise keep the draft and list it as unverified with the supplied claim noted beside it, because the supplied claim alone is no more checked than the draft it would replace. Your own rereading or re-derivation is never evidence in a round, because rounds that feed on their own judgment amplify their own errors.

## What it does

One round:

1. **Name the defects,** each with its place: by the user's criteria if given, otherwise factual errors, logical leaps, missing requirements, then needless repetition. Unless their criteria narrow the review, name as well every checkable claim not yet locked that the user's conclusion or next act depends on (a number, date, name, version, quotation, interface, stated requirement), whether or not it looks wrong.
2. **Give each a method from outside** that would settle it; `references/verification-sources.md` lists methods by kind of content. A defect with no such method available is unverifiable.
3. **Run the checks,** those the purpose depends on first. Each ends confirmed (the defect is real), refuted (the draft was right) or unverifiable. A search snippet alone, or several pages that repeat one origin, is a single source: open the primary source before writing confirmed or refuted, or class the defect unverifiable.
4. **Fix only what was confirmed,** each by the smallest edit: a wrong value, date or name is replaced with the verified one; a comparison, quotation or assertion confirmed to be groundless is deleted; a quotation confirmed to misstate its source takes the source's words, with the source. No hedging in place of a fix, and no rewriting unless the user asks for a rewrite, because hedging leaves a false claim standing and rewriting brings in new unchecked claims. What was refuted stays as drafted. What is unverifiable stays untouched and is listed.
5. **Lock** what passed: draft content a check upheld and values fixed from a confirming source. A later round changes a locked item only on new evidence from outside.

Stop at the first of these that holds: a locked item changed without new evidence, a fix brought in a new confirmed defect, or a fixed defect came back (undo the edit that caused it, then stop); no defect was named, or every one was refuted; none was confirmed and at least one was unverifiable; the round changed nothing in the text; the round cap. Material the user supplies after a stop is new evidence and can open the rounds again. Nothing outside the target is edited on the way.

## What it returns

The changes, each with its place, the original span and the revised one, and its source; the whole revised text only when the user asks for it. Then what each round did (how many defects named, confirmed, refuted and unverifiable, by which methods, and what changed), what is locked, why the rounds stopped, any confirmed defect left unfixed, and the unverified items, those the purpose depends on first, each with what would make it checkable.

It opens with where your reading of what the user wanted goes beyond their words, and the purpose where you read it in, because a reading they never see cannot be corrected. It closes with one line that gives no verdict on the target, because the rounds checked only the defects they named: for what the target is for, which of the claims it depends on a check from outside settled, which it did not, and what was confirmed and not fixed; where nothing is unchecked or unfixed, it says that only the defects named were checked.

Only what a method from outside checked here is ever called verified.
