# dia skills inside an orchestrated review pipeline: usage audit

Session date: 2026-11-09 (Asia/Seoul). Status: research record and unadopted proposals. The owner decides whether any proposal becomes a skill change; nothing here changes a skill. Reviewed in [review.md](review.md), which checks the claims about the skill text and corrects §1 (T2, T4, T6), §2 (C1, C6) and §3; where they differ, the review wins.

This record comes from one Claude Code session in a separate, private research project. That project reviews its own result documents with dia skills run by subagents. After the session, the owner asked for an audit of how the dia skills were used, and for this record so the findings can inform later dia changes. Project content is left out. Only how the skills were invoked, what they returned and where that went wrong is kept.

## Setting

| Item | Value |
|---|---|
| Plugin | `dia` 2.10.0, installed in the Claude Code desktop app (Windows) |
| Skills used | dia-skopos 2.2.0, dia-negative 2.2.0, dia-reductio 2.2.0, dia-warrant 2.3.0, dia-counterplan 2.3.0, dia-adjudicate 2.3.0 |
| Model | `claude-opus-5-5` for the main agent, reviewers and adjudicators (effort high); the Codex relay subagent ran on a Sonnet model with no effort set; Codex itself ran at high effort |
| dia-skopos | Run once by the main agent at the start of an interactive session (a long pasted request after `/dia:dia-skopos`) |
| Review pipeline | Run twice, on two result documents. A workflow script started four reviewers in parallel, without letting them see each other's output: three Claude subagents invoked dia-negative, dia-reductio and dia-warrant; a fourth subagent (the `codex:codex-rescue` agent type) asked Codex to read a copy of dia-counterplan's SKILL.md (byte-identical to the installed 2.3.0) and apply it. A fresh subagent then invoked dia-adjudicate on all reviewers' findings. Every subagent was non-interactive and had to return one structured-output object whose schema the caller fixed |
| Common reviewer schema | `findings[]` of `{title, location, problem, evidence, severity, fix}`, plus `checked_claims` and free-text `notes`; the same schema for all four reviewers |
| Adjudicator schema | `groups[]` of `{members, ruling (accept / partly accept / reject), reason, changes_reading, blocks_next_gate, required_fix}` and a `summary` |

## How the audit was done

- **Auditors:** one auditor per skill read the installed SKILL.md and references, the caller's brief, the subagent transcripts and the returned objects. It reported problems in four layers: the skill text, how the caller invoked it, how the agent executed it, and the fit between the skill's own output format and the caller's schema.
- **Verifiers:** one adversarial verifier per auditor re-checked every finding against the transcripts and marked it upheld, weakened (with a corrected statement) or refuted.
- **Result:** 48 findings: 19 upheld, 28 weakened, 1 refuted.
- **Limits:**
  - One session.
  - The auditors and verifiers are the same model family as the agents they audited.
  - This is a description of failures, not an A/B. No finding shows that a proposed change would help.

## Findings

### 1. Skill-text gaps (candidates for dia changes)

| # | Skill | Gap | Evidence in this session | Verifier |
|---|---|---|---|---|
| T1 | dia-negative, dia-reductio, dia-warrant, dia-counterplan | No rule for a run where another agent calls the skill and fixes the output schema. The text assumes a user who reads the full output and replies, for example: "state the inferred target in the first line so the user can correct it", "Recommend one option and do not decide for the user", and phone-friendly layout. Each agent decided for itself what to keep, and mandatory parts were lost together with optional ones | dia-negative returned no claim C, no own-standard quote and no firm/conditional split. dia-reductio returned no numbered derivations and no Result. dia-warrant returned no warrant record or question list. dia-counterplan returned no assumption list A1…An and no SAST judgements | upheld (dia-negative); weakened to "the text does not cover callers or schemas; harm not shown in every case" (others) |
| T2 | dia-reductio | The output-language rule is ambiguous when the brief is in English and says "Write in Korean" | One run wrote its notes in English | weakened (consistent with, not proven by, the rule) |
| T3 | dia-counterplan | Nothing says what to do when one request asks for both a defect list and a counterplan, or for a fixed machine schema. Rule 1 excludes defect lists, but the skill does not say which instruction wins | Codex put a defect list first and the counterplan after it, in both runs | weakened (the caller's brief is the main cause) |
| T4 | dia-adjudicate | Several safeguards are steps the adjudicator performs on itself: shuffled labels R1…Rn with authors removed, "run it once more" when the result feeds a decision, and the must-check list. In a pipeline the caller controls the input and the number of runs, and the skill gives the caller no checklist. In this session the caller passed reviewer names and severities in a fixed order, ran one adjudicator, and its schema had no must-check field | Round 1 had no must-check list. Round 2's list was incomplete ("no reports rejected", while one group says "the part not accepted: …"). One overturned item was justified by "already accepted at the design gate" | upheld |
| T5 | dia-adjudicate | "Rule, don't rewrite" sits uneasily with callers who ask for a fix. The adjudicator wrote replacement sentences, and they went into the target unchanged, so it became a co-author of the revision it will later judge | The caller's schema made `required_fix` a required field | upheld (as an invocation problem; the skill could name an allowed form such as an acceptance condition) |
| T6 | dia-skopos | The split-omission condition ("when the finished deliverable cannot fail to bring a stated outcome about") can be met by restating the outcome as the deliverable, for example "the document gives the basis for the next decision". Here the materials already said that the outcome could fail | The review omitted the split. The deliverable was done, but one of its purposes, a sensitivity check, stayed unverified | weakened (mainly an execution error; one observation) |
| T7 | dia-skopos | Confirmation asks for a proceed request in the body. The host UI (Claude Code desktop `wrap_up` box) tells the agent not to repeat a question the box shows, so the proceed request lived only in the box | Exported transcripts show the review without any request to proceed | weakened (no harm this time) |

### 2. Caller-side pitfalls (not skill defects; worth documenting for users who orchestrate dia skills)

| # | Pitfall | What happened | Effect |
|---|---|---|---|
| C1 | One generic finding schema for every lens | Each skill's own output (dia-negative's claim and own-standard quote; dia-reductio's premises, derivation, strength and options; dia-warrant's Toulmin record and weakest link; dia-counterplan's assumptions and SAST) had no field. Agents put it in `notes` or dropped it. None of the three Claude reviewers read `references/output-template.md` in at least one run | The lenses converged on plain source-checking. At most 4 of 16 dia-reductio items had the form of a strict contradiction; most dia-warrant items overlapped with other reviewers (9/10, 7/8) |
| C2 | `notes` not forwarded | The caller sent the adjudicator only the `findings`. In round 1 dia-reductio's options and recommendation, dia-warrant's reconstructed warrant and Codex's counterplan never reached the ruling | The parts that made each lens different never reached the decision |
| C3 | Same brief for every lens | Every reviewer was asked to check sources and report how many claims it verified | The four lenses overlapped heavily. Overlap gave some confirmation but lost the separate views |
| C4 | `severity` and `fix` fields for every reviewer | dia-warrant, whose rule is to give only the kind of answer that would strengthen a reason, wrote replacement text and an alternative recommendation | A skill rule was broken because the schema required it |
| C5 | Codex through a relay agent | The relay rewrote the Codex prompt differently in each round. In round 1 it added category hints ("numbers that do not match their sources, claims stronger than the evidence…") that the other reviewers did not get. In round 2 it packaged the counterplan as an extra "finding" with a severity it invented. It also ran on a weaker model than required | The two rounds cannot be compared. The Codex finding count was overstated by one |
| C6 | One adjudicator, identities visible, untraceable ids | See T4. The saved review files also lacked reviewer keys, so ruling ids could not be traced back from the saved files alone | The adjudicator's own errors had no second run to expose them, and later audits needed the transcripts |

### 3. Execution observations

- **dia-reductio:** in one run it graded "conditional" a refutation that rested on one verified fact, so the grading did not match the skill's definition. Another run left an empirical extrapolation in the derivation without tagging it as a premise.
- **dia-warrant:** it did not record whether it weighed a second warrant (W2), so Rules 3–4 cannot be checked.
- **dia-counterplan (Codex):** it read the template but omitted the A1…An list, per-assumption SAST judgements, evidence classes and the Record's "kept for the side set aside".
- **dia-adjudicate:**
  - Round 1 accepted one item on a quote it had not opened; the quote was correct.
  - Round 1 used `Write` (a scratch helper file in the session scratchpad), `TaskStop` (its own timed-out background command) and PowerShell (reads). It changed no project file.
  - Round 2 used `WebFetch` to check a cited public page.
  - The brief had no write ban, so only the skill's guardrails limited it.
- **dia-skopos (main agent):**
  - It omitted the outcome split (T6).
  - It kept a material scope choice as its own default and did not list the strongest existing evidence as an alternative.
  - Later, after a coder warned that a text revision changed what the main contrast measures, it judged the warning itself and ran on. The question reached the owner only through the later review. Recognizing Approval asks for approval of such a changed portion before dependent work.
  - It listed an external send (to Codex) and still said "no step cannot be undone".

### 4. What worked

- **dia-skopos:** before approval the main agent only read. It asked material decisions with a recommendation and the strongest alternative. Its text, still in context, did not capture later unrelated requests.
- **Reviewers:** three of four found the most consequential error in round 1 on their own, by reading raw traces. The error was a false statement that thinking content was absent.
- **dia-adjudicate:**
  - Both runs re-derived key numbers from raw data instead of trusting reports.
  - Round 2 asked for human checks on the one count its main ruling rested on, and that count held when re-run.
  - Its rulings changed the authoring agent's recommendation twice; each change rested on data the adjudicator re-derived.

## Candidate changes (unadopted)

| # | Skill(s) | Proposal | Basis | Limits |
|---|---|---|---|---|
| P1 | dia-negative, dia-reductio, dia-warrant, dia-counterplan | Add a short "Called by another agent" paragraph. When a caller fixes the output schema or there is no user, write the skill's full output in the template layout into one text field (or the caller's equivalent), and never drop the mandatory parts (for example firm/conditional and evidence classes, derivation and strength, warrant record, assumption list). Put options and the record in compressed form there, not in the caller's finding fields | T1, C1, C2 | One session. The caller's schema was the main cause. Behaviour under the new text is untested |
| P2 | dia-adjudicate | Add a caller checklist: shuffled anonymous labels with authors and severities removed; a must-check field in the output; two independent runs whenever the result feeds a decision, with the disagreements going to the must-check list; prior approvals are not evidence. Define "acceptance condition (what must be true after the fix)" as the allowed form when a caller asks for a fix | T4, T5, C6 | Same |
| P3 | dia-counterplan | State the order when a request also asks for a defect list or a fixed schema: give the counterplan in full first; put defects in a separate labelled list, never inside the counterplan | T3, C5 | Same |
| P4 | dia-reductio | Settle the output language when the brief's language and an explicit instruction differ (the explicit instruction wins) | T2 | One observation |
| P5 | dia-skopos | Add a check to the split-omission condition: do not omit the split when the request or materials say the deliverable might not bring the outcome about, or when a completion criterion can be met just by recording that something is unverified. Note that a host box may carry the proceed request, but the body still states what approval is asked for | T6, T7 | One observation, and mostly an execution error |
| P6 | README or docs (no skill change) | A short usage note for orchestrated use: give each lens its own output field; forward the full skill output to the adjudicator; do not give every lens the same brief; pass a Codex prompt verbatim; record the relay model | C1–C6 | — |

## Caller-side fix applied in the research project

The research project rewrote its review script (version 2). The changes:
- Each reviewer returns its full skill output, read from the template, and the adjudicator receives it.
- Each lens gets its own brief.
- dia-reductio puts non-reductio comments in a separate list.
- dia-warrant gives "strengthen" (the kind of answer that would help) instead of fix text.
- The Codex relay runs at high effort and passes a fixed prompt verbatim, with the counterplan in its own field.
- Reports are shuffled under neutral ids, without reviewer names or severities.
- Two independent adjudicators run, and their disagreements are listed.
- The adjudicators give acceptance conditions instead of replacement sentences and must fill a must-check list.
- The saved result keeps the id map.

This version has not yet been run.
