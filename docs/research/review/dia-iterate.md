# Review: docs/research/dia-iterate.md

Reviewer: independent (reviewer profile), 2026-10-20. Tree: detached `main` at feea231. Nothing under `tree/` was edited.
Method: I opened every file:line the document cites. I fetched all 27 sources (arXiv PDFs or abstracts, vendor docs, GitHub issues) and grepped them for the quoted passages. I also word-diffed upstream `recursive-refine/SKILL.md` against `dia-iterate/SKILL.md`.

**Verdict: SOUND WITH FIXES.** The two high findings (F1, F2) and F3 point at real defects. Most quotations and numbers check out. Six proposals need changes before anyone edits the skill from them:

- F2 puts product names into skill text, which breaks AGENTS.md.
- F1 keeps an existing conflict with the lock rule.
- F6 contradicts SKILL.md:33.
- F7's "at times" change rests on a misreading of Huang.
- F5 and A2 misstate the lineage.
- F11 conflicts with F12.

Document length: 364 lines (limit 500). No Hangul in the document.

## 1. Per-finding verdicts (section 7)

**F1 (high), regression metric. Confirmed. Fix the proposal (partly).**
- The problem is real. SKILL.md:46 counts regression as "fewer items passed verification than in the previous round". SKILL.md:35 defines "passed verification" per round, and locked items are not re-examined, so later rounds normally have fewer passes.
- The skill's own example breaks this rule. SKILL.md:66-67 shows round 1 with 2 confirmed and 1 refuted, then round 2 with 0 and 0. Under :46 that is a regression, yet :68 reports "verification exhausted". The document missed this evidence, which makes the case stronger.
- Severity high is defensible because the rule defeats multi-round use. The failure is conservative, though: verified fixes are discarded and the stop reason is wrong, but no false content is added.
- Proposal problem: it keeps "a locked item changed" unqualified. SKILL.md:35 explicitly allows changing a locked item "unless new external evidence appears". The current text already conflicts with that (missed issue M2), and the proposal carries the conflict forward.
- Suggested change: write "a locked item changed without new external evidence". Also consider reverting only the offending edit instead of the whole round. "Roll back to the previous round's result" throws away that round's other confirmed fixes.

**F2 (high), invocation on Codex and ChatGPT. Partly: downgrade to medium and rewrite the proposal.**

Evidence that holds:
- P3 (`docs/probes.md:31-32`) shows that false-policy skills are absent from the Codex model-visible list, and that `$dia-intent` did not resolve on the plugin route.
- [26] has a contributor comment stating that `hidden_from_prompt` "only clears `prompt_visible`" and that hidden skills "are still selected by `$name`".
- [25] says: "In ChatGPT, type `@` to select a skill."

Problems:
- The proposed text says "in Claude", "in Codex", "in ChatGPT". AGENTS.md (Rules, 1st bullet) and spec D14 require assistant-neutral skill text with no product names. The current SKILL.md:20 lists invocation forms without naming products, and so does `dia-refine/SKILL.md:18`. Keep it that way: `(/dia:dia-iterate, $dia:dia-iterate, $dia-iterate, @dia-iterate)`.
- The proposal leaves the description unchanged. Description line :3 also lists `$dia-iterate` and should get the same change. The description is currently 549 characters, so there is room under 1024.
- Severity: the main problem (a first-word `dia-iterate` message does nothing on Codex) cannot be fixed in SKILL.md, because the skill is never loaded on that route. The real fix is spec §4 and the README. That part is inferred, not probed: P3 never sent a first-word message. The document should label it [inference].
- An `@` mention is already "an explicit invocation by name" under :20, so the missing `@dia-iterate` is cosmetic.
- The `default_prompt` question is package-wide (spec §7.3 template; research README theme 1). Decide it once for all seven skills, not in this skill.
- The `:22` fallback edit targets text that only Claude surfaces can reach. Make it neutral: "...a message beginning with `dia-iterate`, or an explicit invocation of the skill by name".

**F3 (medium), "zero defects" swallows "verification exhausted". Confirmed.**
- SKILL.md:47 says "nothing was confirmed". That is true whenever every defect is unverifiable, and :47 is checked before :48.
- The example at :66-68 contradicts the order too: round 2 has confirmed=0, yet the stated stop reason is "verification exhausted".
- The proposal is correct. I traced the mixed cases (refuted plus unverifiable, none confirmed) and they now fall through to "exhausted". It also makes the example table consistent.

**F4 (medium), edits without external verification. Partly.**
- The tension between :81 and :82, and with verification-sources.md:14-15, is real. But :82 reads as a deliberate, scoped exception carried over word for word from upstream (`upstream/.../SKILL.md:84-85`). The defect is unstated precedence rather than a contradiction.
- The claimed conflict with :84 is wrong. :84 governs what may be *described as verified*, and nothing makes style edits claim that.
- The evidence is one-sided. [12] covers Game of 24, graph colouring and planning, not style. The abstract of Tyen et al. [10] even opens with "self-correction has shown promise in improving LLM outputs in terms of style and quality".
- Option a adds a "Suggestions (not applied)" section that is not in the output template (:58-72), and it turns the default 4th check ("padding", :31) into a suggestion only.
- Recommend option b (label the exception at :81) as the minimal edit. Severity: low to medium.

**F5 (medium), recall depends on suspicion. Partly.**
- The risk is real, but the lineage claim is wrong. §3.2 says "dia-iterate lost that instruction". `upstream/installed/recursive-refine/SKILL.md:27` is word for word SKILL.md:31: the instruction was never in recursive-refine. It belongs to self-refine/dia-refine.
- Tyen et al. [10] study logical mistakes in chain-of-thought traces (BIG-Bench Mistake). The proposal's sentence "Fluent claims you believe are the ones least likely to be named" is the author's inference, not Tyen's finding.
- "List every checkable claim" changes what the round table counts as "Named". In tool-less runs it also turns every claim into an unverified-list entry.
- Suggested change: scope it to "every checkable claim that bears on the user's conclusion or next action". That mirrors the filter in `dia-refine/SKILL.md:39`.

**F6 (medium), no legal fix for a misquotation. Partly; wrong as written.**
- The gap is narrower than claimed. :34 already allows replacing wrong "values, dates and names", which covers a wrong number or name inside a quotation.
- The no-copy rule is deliberate (the content-filter rationale at :33 and :87).
- The proposal permits copying source text into the final version but leaves :33's "never copied into ... the final version" unchanged. That creates a direct contradiction. It also conflicts with :87 for set texts.
- To proceed, amend :33 in the same edit. Severity: low.

**F7 (medium), label and Huang wording. Partly.**
- Wrong part: the "often" → "at times" change. Huang et al. write in §1: "In most instances, the performance after self-correction even deteriorates" (arXiv:2310.01798v2, p.1). "Often" is faithful, so drop that half of F7. A1's "slightly overstated" goes with it.
- The CRITIC label is acceptable as an honest "in the style of", but §2.2's "almost step for step" overstates the match. In CRITIC's Algorithm 1, line 7 regenerates the output conditioned on free-text critiques. CRITIC has no smallest-edit rule, no locks, no verdict classes, and no tool-less path: its "w/o Tool" ablation is the failure case.
- A2 misjudges the referent. "dia-refine run over several rounds" names the sibling skill, not Madaan's Self-Refine, so judging it against [2] is a category error. The valid point is that dia-refine accepts self re-derivation and dia-iterate does not.

**F8 (medium), content-filter mechanism. Confirmed; severity low.**
- [17] supports the regurgitation premise. "Sentence by sentence" and "even when reworded" are indeed undocumented.
- The proposed rewording of :85 and :33 is fine.
- See citation note C4 on [20] and [22].

**F9 (low), self-written tests. Confirmed.** [3] says: "all tests pass on an incorrect solution", "prematurely report an invalid submission". The proposal is neutral and minimal.

**F10 (low), shared blind spot. Confirmed.** `skill-loop.md:55-56` says what the document claims. The proposal is fine.

**F11 (low), locks invisible. Partly.** The point is valid. But a `Locked` column makes the 7-column table wider, which works against F12. Prefer the "one line under the table" option.

**F12 (low/nit), mobile table. Unverifiable.** The document correctly marks it [unverified]. Fine as a nit.

**F13 (low), fixed point. Confirmed.** The CRITIC quote checks out ("stopping early if the answer remains the same for two consecutive corrections", §4.1). The proposal is a harmless safety net.

## 2. Citation problems

I fetched all 27 sources ([7] and [15] as spot checks). All URLs are live, and every quoted string except those below was found verbatim. The numbers match exactly: Huang Tables 3-4 (including 74.7%), Self-Refine (22.0→28.8, 29.0→49.7, 64.1→64.1, max 4), CRITIC (50.0 vs 42.0 EM, n=3, "2-3 rounds") and FlipFlop (46%, 17%).

Problems:

- C1 (medium; it drives F7). The document says Huang's own wording is "at times" and that "often" is stronger. It missed the §1 sentence "In most instances, the performance after self-correction even deteriorates". This also changes A1.
- C2 (medium; supports A14 and §3.5). The document says "Without external feedback, Huang's round 2 is no better than round 1 and sometimes worse." That is false. In Huang Tables 3-4, round 2 beats round 1 in 4 of 10 cells:
  - GPT-3.5 CSQA 38.1→41.8
  - GPT-4 CSQA 79.5→80.0
  - GPT-4-Turbo GSM8K 88.0→90.0
  - GPT-4-Turbo CSQA 81.5→83.0

  The defensible claim is "round 2 never recovers the no-correction baseline". The cap-of-3 conclusion survives.
- C3 (low; A8). [4] is cited for the lock ("gains surge when only erroneous items are modified"). CRITIC* is an *oracle* setting, "where we only apply correction on the incorrect answers" using ground-truth labels. That is exactly the confound Huang criticises, so it does not support locking. [1] (correct→incorrect flips) and [9] are adequate support on their own.
- C4 (low; F8 and §3.6).
  - [22] is about the `refusal` stop reason, which "Safety classifiers return". The page never mentions content filtering, copyright or regurgitation, so it is not evidence about the copy-block filter.
  - [20] is cited as matching the "start a new conversation" advice. It actually lists that as a *cost* ("starting a new session loses all the context").
- C5 (low; F2). [26] calls the comment "a Codex maintainer-side analysis". The fetched page shows a contributor comment (argszero) with no maintainer marker. Its title is also paraphrased: the real title is "allow_implicit_invocation: false also disables explicit $skill invocation, contradicting docs", and the opener claims the opposite of what the document cites. P3 is better first-hand evidence: `$dia:dia-intent` loaded a false-policy plugin skill.
- C6 (nit). §3.2 and F5 present Tyen et al. as showing that models cannot find *their own* errors in drafts. The paper tests mistake-finding in CoT traces generated by PaLM 2, which is a narrower claim.
- C7 (nit). In §6.3, "`$dia-iterate` does not resolve" generalises from one P3 run on dia-intent (n=1). It should say so.

## 3. Fidelity audit: verdicts I disagree with

- A1 is "matches", without "slightly overstated". See C1.
- A2 is "loose", not "departs". The phrase refers to the sibling skill. The real gap is the re-derivation standard (`dia-refine/SKILL.md:32` versus `verification-sources.md:7`).
- A3 is "loose (CRITIC-like shape)", not a flat "matches". CRITIC Algorithm 1 line 7 regenerates the whole output from critiques. It has no minimal-edit rule, verdict triad or lock, and it is undefined without tools.
- A8 stays "matches", but drop [4] as support (C3).
- A14 stays "matches", but strike the Huang round-2 clause (C2).
- A19 is "loose", not "matches in spirit". `verification-sources.md:11` accepts "bibliographic data in search results" for citations, which conflicts with :31 ("one search snippet ... is not independent confirmation"). See M3.

## 4. Missed issues

- M1 (should-fix). The example round summary contradicts the stop rules. Round 2 at SKILL.md:67 (confirmed 0, refuted 0) triggers both regression (:46) and zero defects (:47) before "verification exhausted" (:68). A model that follows the example and one that follows the rules will disagree. F1 plus F3 fix it, but the document should cite it, and any rewrite of :46-47 must be checked against :66-68.
- M2 (should-fix). The lock exception conflicts with the regression rule. :35 allows changing a locked item on new external evidence; :46 treats any locked-item change as regression and rolls back. Present in upstream too (`recursive-refine/SKILL.md:31,38`). The F1 proposal keeps it.
- M3 (should-fix). Search snippets count for citations but not for facts. `verification-sources.md:11` ("or bibliographic data in search results") against :31 (snippet ≠ confirmation, open the primary source or mark "single source"). Exact titles, authors and numbers are what :11 itself says stay unverified, so the snippet route is weak.
- M4 (nit). The lock relies on a re-check that no step performs. :35 locks "content re-confirmed after a fix", but steps 3-4 have no re-verification after the fix. Either add "re-check the fixed span by the same method" to step 4, or lock the fixed value on the strength of the confirming source.
- M5 (nit). README.md:13 says "first word `dia-iterate` only", which conflicts with SKILL.md:20 and spec §4/§5.7 (explicit names also count). The document raises the Codex side (F2) but not the README wording.

Checked and fine: SKILL.md length (87 lines, proposals add fewer than 15), description length (549 characters), Hangul (none), and tool-free operation (no proposal requires a tool). The §5.1 lineage summary matches my word diff, apart from the F5 claim.
