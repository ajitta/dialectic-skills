# Token audit: dia-iterate

Scope: `skills/dia-iterate/SKILL.md` body (lines 11–91, frontmatter and description out of scope) and `references/verification-sources.md`. Tokens are tiktoken `cl100k_base`; Claude tokens ≈ ×1.5 (`docs/token-cost.md`). Units are sentences or bullets; a sentence that mixes classes is split where the split is clean (line 14's first sentence: label / rule / reason). Unit sums omit newlines between units (13 tokens in SKILL.md, 9 in the reference). Unit ids are `line.sentence`, 0-based.

Classes: A instruction, B rationale, C provenance/label/citation, D example, E redundant (restates text in the same file or a file loaded with it), F meta (headings, pointers, invocation forms).

## Per-class totals

| Class | SKILL.md body | verification-sources.md |
|---|---|---|
| A instruction | 1,590 | 620 |
| B rationale | 366 | 23 |
| C provenance / label | 105 | 0 |
| D example | 143 | 96 |
| E redundant | 194 | 95 |
| F meta / headings | 56 | 47 |
| Units total | 2,454 | 881 |
| File as counted (with newlines) | **2,467** | **890** |

Notes on the counts:
- A includes some inline examples and short reasons that are not worth splitting out: the "sword of Damocles" prompt (:23), the compact-summary sample line (:77), "(for example Context7)" (reference :9, wording required by spec §5.7), and the hedging/rewrite reason at :34.
- :16 is counted as A because it is the only place in the body that states the default cap (`default 3`); the rest of it repeats :20 and :27.
- Non-A text is 864 tokens (35% of the body). Most of it is load-bearing (below); the recommended cut is 295.

## Evidence used

- D19–D23 (spec §3): D19 adds "own re-derivation is not verification here" and the CRITIC/not-Self-Refine label (research README theme 4, "honest method labels"); D21/D22 require the round-1 exception to be stated consistently in step 4, Guardrails and the reference; D23 adds the quotation rule, the observed-risk wording of the content-filter claims, the lower-bound sentence, the compact summary and the fixed-point listing.
- Spec §5.7 requires the tool-less rule nearly word for word ("This is expected behavior, not a failure"), the content-filter guardrails (change list by default, one retry, then change shape) and the invocation forms including `@dia-iterate`.
- Spec §7.1 and P8: some headless runs could not open `references/*.md`, so anything the skill needs to finish (rules, record format, output template) must stay in SKILL.md.
- P6 (`dia-iterate --max 2` + draft) and P8 (tool-less; `17 x 23` must stay unverified, stop is "verification exhausted") are the probes that touch dia-iterate. No probe covers the content-filter rules or a topic-without-target prompt.
- docs/research/dia-iterate.md §3.6 (filter evidence: one vendor statement, the rest single field reports), review/diff (CRITIC and Huang citations fetched and correct; "loosely" is honest), review/lowfix (lower-bound wording).

## Candidates (SKILL.md)

"LB" = load-bearing. Savings are measured by applying the proposal to a scratch copy.

| # | Line / unit | Class | Tok | LB? Reason | Proposal | Risk (probe) |
|---|---|---|---|---|---|---|
| S1 | :14 whole paragraph (label 14.0a, rule 14.0b, reason 14.0c, CRITIC 14.1, Huang 14.2, "So here a round is…" 14.3, "When verification methods run out…" 14.4, "quality of the signal caps…" 14.5, lower bound 14.6) | C 105, A 23, B 79, E 37 | 244 | Partly. 14.0b is the only body statement that re-derivation is not verification (D19; P8 relies on it for `17 x 23`). CRITIC/Self-Refine is a D19 label. Huang backs 14.0c and the user may ask. 14.6 is D23 and sets how a zero-defects stop is reported. 14.3 repeats steps 2–4 and :85; 14.4 repeats stop 3; 14.5 is a reason no rule needs (stops and the cap already end the loop). | **Shorten** (labels and citations kept in place, so no owner decision is needed): `A multi-round relative of dia-refine with a stricter basis: every round needs a signal from outside the model, and your own re-derivation does not count as one, because a loop that feeds on its own judgment amplifies its own errors (Huang et al., ICLR 2024, arXiv:2310.01798: repeated self-judgment brings no gain on reasoning tasks and often makes them worse). A round, "verify, then fix only what was confirmed", loosely follows CRITIC (Gou et al., arXiv:2305.11738); it is not the Self-Refine loop. Only defects you name can be verified, and an error you would make yourself is unlikely to be named, so the confirmed defects are a lower bound, and a "zero defects" stop is not a clean bill.` Saves **68**. | Low. All rules survive; "often" kept (review C1). Loss of 14.5 could let a run push past a useless round, but stops 3–4 still fire. P8 catches a re-derivation edit. |
| S1b | same, variant | C | — | — | As S1, but cut the Huang finding to `(Huang et al., arXiv:2310.01798)` and move the sentence to a "Method background" section in the reference. Saves 91 here, adds 49 to the reference. | **Not recommended**: the reference has no read condition for "the user asks about the method", so the finding would be unreachable when asked; 23 extra tokens are not worth it. |
| S2 | :16 "A call may carry the target (…), a round cap (`--max N`, default 3), and review criteria." | A/E | 38 | Only for "default 3"; the target list repeats :27, and "may follow it" at :20 repeats the rest. | **Cut** :16; change :20's second sentence to `Target, \`--max N\` (round cap, default 3) and criteria may follow it.` Saves **30**. | Low. Default cap still stated once. P6 (`--max 2`) exercises parsing. |
| S3 | :22 "Running the loop without an explicit request for iteration is overkill." | B | 13 | No; the rule before it is complete. | **Cut**. Saves **13**. | Very low. P6 natural-language cells. |
| S4 | :23 "This is a verification loop, not a writing tool. If the model drafts first, the loop's target becomes the model's own guesswork; and for widely copied set texts (…) that draft will overlap … and can trip the host's content filter." | B | 63 | Partly: the guesswork reason helps the model refuse a user who insists on a draft. The set-text half repeats :91, which already covers set texts in every output. | **Shorten** to `Do not draft one yourself: the loop would then only check your own guesswork.` Saves **46**. | Low–medium: on a fable or proverb topic the model loses one reminder; :91 remains. No probe; suggested probe: `dia-iterate on the sword of Damocles` → one question, no draft. |
| S5 | :33 "Long verbatim overlap with an existing document can trigger the host's content filter, which blocks the whole response, and the round's work is lost with it." | B | 32 | Yes, briefly: it lets the model extend the no-copy rule to sources the step does not list. D23 set the observed-risk wording. | **Shorten** to `Long verbatim overlap can trip the host's content filter and lose the round's work.` (keeps "can", the observed-risk form). Saves **14**. | Very low. No probe covers filters. |
| S6 | :35 "Without this lock, correct content drifts as rounds accumulate." | B | 12 | No; lock rule and regression rule are explicit. | **Cut**. Saves **12**. | Very low. |
| S7 | :52 "If round 1 names no defects, or refutes all of them, say so and end." | E | 20 | Its only new content is "say so" (the lowfix review ties the lower-bound point to this stop). | **Cut**, and change rule 2's "Stop." (:47) to `Say so and stop.` Saves **17**. Keep the rest of :52 (D19/F3: "verification exhausted, not zero defects"). | Low. P8 checks the stop label. |
| S8 | :56 "Edits here change only a few sentences…, so a full reprint is mostly a re-emission… If that original is a third party's text or a widely copied piece, the host's content filter can block the entire response. The change list carries the same information without that risk." | B | 63 | Partly: it justifies refusing an unrequested full reprint. | **Shorten** to `A full reprint mostly re-emits the original, and for a third party's or widely copied text the host's content filter can block the whole response.` Saves **32**. | Low. Change-list default (spec §5.7) unchanged. P6 shows the change-list format. |
| S9 | :79 "Annotating unchanged sentences makes the final version differ from the original, which is itself an edit." | B | 20 | No; the preceding sentence already limits sources to changed sentences. | **Cut**. Saves **20**. | Low: watch for "(verified)" tags on unchanged sentences in P6 output. |
| S10 | :89 "Sporadic blocks clear on retry; if the shape of the output is the cause, no number of retries helps." | B | 24 | No; "at most once" and "then change the shape" are explicit. | **Cut**. Saves **24**. | Very low; no filter probe. |
| S11 | :90 "Once a conversation is tied up in work that reproduces source text, even later unrelated short outputs have been reported to block. More rounds produce nothing in that state." | B | 33 | Partly: it is what the model tells a user surprised by "start a new conversation". | **Shorten** to `Later outputs in such a conversation have been reported to block too.` (observed-risk wording kept). Saves **20**. | Very low. |

Candidates reviewed and **kept**:

| Line / unit | Class | Tok | Why keep |
|---|---|---|---|
| :14 label "relative of dia-refine…", CRITIC, Self-Refine, Huang | C | 105 → ~96 after S1 (the CRITIC sentence now also carries the round definition) | D19 honest-label requirement; cutting needs an owner decision; moving is possible but no read condition reaches it (S1b). |
| :14 lower bound (14.6) | B | 43 | D23; the only text telling the model a zero-defects stop is not a clean bill. |
| :20 invocation forms | F/A | 50 | Spec §5.7 and D19 (`@dia-iterate`); the body must recognise markers when the skill is model-loaded. P6. |
| :22 / :23 first sentences | A | 73 | Spec §5.7 one-line ask; topic-without-target question. |
| :32 pointer to the reference | F | 22 | The only read condition for the reference. |
| :32 "rereading … is not an external method", :85 first sentence | E | 35 | Operative restatements at the two places that decide edits; P8's dia-refine failure came from a rule placed away from the step it governed. |
| :34 "Do not hedge … and do not rewrite: hedging leaves…" | A+B | 28 | The reasons generalise to "softening" variants the rule does not list (reference :34 names one). |
| :40 "This is expected behavior, not a failure." | B | 9 | Required by spec §5.7; stops apologetic forced edits in P8. |
| :46 "Fewer items passing verification … is not a regression" | A+B | 31 | D19 change; its reason (locks are not re-examined) is what prevents a false regression stop. |
| :52 second sentence | E | 22 | D19/F3; P8 pass condition ("verification exhausted"). |
| :58–75 output template | D | 143 | Copied verbatim (P6 shows "Confirmed but not fixed: none"); must stay in SKILL.md for unreadable-reference runs (spec §7.1, P8). |
| :77 compact one-line summary | A (+D) | 56 | D23. Moving it to the reference with a pointer saves only 26 and loses it when references are unreadable. |
| :80 single-right-answer result | E | 32 | Restates step 4, but it is the exact rule whose absence broke dia-refine in P8 (an output-section rule allowed the change). Cheap insurance. |
| :84 "Flipping a correct answer under unspecific pressure is the failure…" | B | 18 | Generalises the rule to pushback forms not listed; pushback is a known failure mode (research §3). |
| :85–:86 round-1 style exception (85.1, 86) | A/E | 97 | D21/D22 require the exception stated consistently in step 4, Guardrails and the reference; merging :85 and :86 would save about 20 but re-opens reviewed text. Not recommended. |
| :88, :91 | A | 73 | Honest "verified" wording (D19); set-text class and its examples, referenced by :34. |

## Candidates (verification-sources.md)

Loaded only when the model reads it; the measured first turns read no reference for this skill (`docs/token-cost.md`). SKILL.md is always in context when it is read, so text that repeats SKILL.md is pure E here (the reverse does not hold: SKILL.md must stand alone).

| # | Line / unit | Class | Tok | LB? | Proposal | Risk |
|---|---|---|---|---|---|---|
| R1 | :3 "The same model judging again from the same grounds is not external verification, and no edit is made on that basis alone." | E | 24 | No; SKILL.md :32 and :85 say it. The criterion sentence before it stays (it generalises to unlisted content types). | **Cut**. Saves **24**. | Very low. |
| R2 | :21 "Cut the draft-side span to a clause or less and do not quote the source's text. What is kept is the method (with URL), the verdict, and one value. Copying source sentences … can trip the host's content filter." | E 36, B 23 | 59 | No; SKILL.md step 3 (:33) states the same limits and reason. | **Shorten** :21 to `One line per defect, within the limits of SKILL.md step 3.` Saves **49**. | Low. The log example below still shows the shape. |
| R3 | :33 "Quoting a whole source paragraph as the grounds for a confirmation. A judgment needs the value and the URL, not the paragraph." | E | 27 | No; repeats SKILL.md :33 and reference :21. | **Cut** the bullet. Saves **27**. | Very low. |
| R4 | :34 "Changing the sentence is an edit too." | E | 8 | No; the bullet already says leave the text as it is. | **Cut**. Saves **8**. | Very low. |

Kept in the reference: the criterion (:3, second sentence), every table row (all A; row 8's self-written-tests note and row 9's Context7 example are D23 / spec §5.7 wording), the log example (D, 96; the format the model copies), and misjudgments 1, 2 and 4 (each names an error pattern the rules do not spell out).

## Recommended set and saving

| Set | Items | cl100k saved | ≈ Claude (×1.5) |
|---|---|---|---|
| SKILL.md, every invocation | S1–S11 (not S1b) | **295** of 2,467 (12.0%) | ≈ 440 |
| Reference, only when read | R1–R4 | **108** of 890 (12.1%) | ≈ 160 |

Measured by applying all edits to scratch copies: body 2,467 → 2,172; reference 890 → 782. This brings dia-iterate's SKILL.md (2,659 with frontmatter) to about 2,364, back near the D22 figure (2,457) while keeping every D19–D23 change.

What the set does **not** touch: any rule (A) except the merge in S2/S7, any D19–D23 label or citation (shortened in place, not cut or moved), the output template, the tool-less section, and anything the skill needs when references cannot be opened.

Risk summary:
- Behaviour-relevant edits are S2 (default cap moves into the invocation bullet) and S7 (rule 2 now says "Say so and stop."); P6 and P8 cover both.
- S4, S5, S8, S10, S11 remove content-filter reasons, not rules. No probe covers filters; if the owner wants coverage, add a probe that iterates on a widely copied text (a famous fable, the MIT licence) and checks: one question when no target, change list by default, no source quotation beyond one sentence.
- The CRITIC/Self-Refine label and the Huang finding stay in SKILL.md (S1), so no owner decision is needed. Moving them (S1b) or cutting them would need one (D19 theme 4).

Suggested re-check after applying: P6 (`dia-iterate --max 2` + draft) and P8 (tool-less), each n≥2, from the neutral directory, compared against the Part D results in `docs/probes.md`.
