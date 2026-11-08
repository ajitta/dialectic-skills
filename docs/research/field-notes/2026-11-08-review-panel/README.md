# Field note: dia skills as a blind review panel (2026-11-08)

Status: observation record, not a verified finding. Written by the assistant (Claude Opus 5.5) that ran the session, from its own records; this is a self-observation, not an independent evaluation. Nothing in `skills/` was changed. The proposals below are candidates to verify in this folder before any skill edit (`AGENTS.md`, Probes and evals).

## 1. Setting

The session was a research session in a separate, private repository about writing instructions for models. The skills ran from the installed plugin (`dia` 2.x), not from this repository's `skills/`.

| Skill | Uses | How |
|---|---|---|
| dia-skopos | 1 | Main assistant, at the start of the session, on the owner's request (invoked by name) |
| dia-negative, dia-reductio, dia-warrant, dia-counterplan | 3 each (12) | One subagent per skill, run in parallel, blind to each other, reasoning effort medium, invoked by name inside the subagent. Each review was one shot: the subagent was told not to wait for approval and to return findings |
| dia-adjudicate, dia-router, dia-techne, others | 0 | — |

The three review targets were Markdown documents in the private repository: an options analysis (round R1), an experiment design with a dry-run plan (R2), and an experiment result (R3). The main assistant then judged every finding and recorded a judgement table (finding, which reviewers raised it, severity, verdict, change made).

## 2. Data

From the three judgement tables and the subagent run statistics reported by the host.

| Round | Findings | Raised by 1 reviewer | By all 4 | Verdicts | Subagent tokens (4 reviews) |
|---|---|---|---|---|---|
| R1 options analysis | 24 | 7 | 2 | 23 accepted, 1 partly | ~488k |
| R2 design | 23 | 7 | 9 | 22 accepted, 1 partly | ~488k |
| R3 result | 21 | 9 | 5 | 21 accepted | ~554k |

- 68 findings, 0 rejected.
- 12 review runs used about 1.53M tokens in total. Each run took 146–265 s.
- Findings raised by a single reviewer, by skill: counterplan 9, negative 5, reductio 5 (all in R3), warrant 4.

**Contributions that changed a decision.**
- **dia-counterplan:** its counterplan became the recommended course twice. In R1 a new option it proposed was adopted. In R3 its "close now and fix reopening conditions" plan replaced the main assistant's draft recommendation.
- **dia-negative:** in R3 it alone found a harness defect. The run folder had no `.git`, so every session's environment block said "not a git repository" (verified in 30 of 30 sessions). That kept 8 of 12 runs of one cell family from using the shell.
- **dia-reductio, dia-counterplan, dia-warrant:** in R3 they argued that a behaviour the draft called "not presented" was itself the measured path. A check of the source record confirmed it, and the draft's central claim was reversed.
- **dia-reductio's formal core:** a strict contradiction was found once in three rounds (R2: a document said it followed a rule while counting in a different unit). In R1 and R3 it reported "no contradiction found" plus conditional contradictions. Its other value came from ordinary findings.

## 3. Problems observed

1. **No one-shot review mode in three of the four review skills.**
   - dia-counterplan's first message runs Steps 1–7 and ends with Step 7's question to the user ("which assumption from each pair do they now hold?").
   - dia-negative and dia-reductio end with options, a recommendation, and a record whose decision field belongs to the user.
   - Only dia-warrant has `--mode=audit`: one response, no questions.
   - In a parallel subagent panel there is no user. Each subagent improvised: counterplan said it skipped Step 7, others ended with "the decision is the user's". The main assistant had to put an output format in every prompt, and the outputs still differed in layout (derivation blocks, (a)/(b)/(c) sections, records). That made merging slower.
2. **Overlap between lenses on document targets.**
   - In R2, 9 of 23 findings came from all four reviewers.
   - Generic defects pull every lens: miscounts, wrong citations, missing evidence labels, unjustified numbers.
   - Each reviewer re-read the same sources, at about 110–150k tokens per run.
3. **No path from reviews to adjudication.**
   - dia-adjudicate exists for exactly this step, but nothing pointed to it (dia-router has no panel flow). The main assistant adjudicated by hand.
   - 0 of 68 findings were rejected. That suggests the judging step may not have been strict.
   - The judgement tables recorded how many reviewers raised each item. dia-adjudicate's Rule 2 says agreement is not evidence.
   - There was no table of reviewer errors. Reviewers disagreed on facts: three recounts of the same stored judge-call total gave 1,227, 751 and 633, and only 633 deduplicated correctly.
4. **Text-only checking of designs that will run.**
   - In R2 all four reviewers checked the design against its own text and the repository's records.
   - None asked what the run environment would show the model: the missing `.git`, or whether a key account was visible in tool output.
   - Both mattered and surfaced only in R3, with run data. The skills have no step that lists execution-environment assumptions and checks them.
5. **Evidence class is not marked in lens outputs.**
   - One reviewer cited a tool description it saw in its own session as evidence about a different runtime (`claude -p`), without flagging the environment difference.
   - dia-adjudicate requires an evidence class on every verdict (Rule 8). The four lenses do not.
6. **Same-model independence.** All reviewers and the adjudicating assistant were the same model. dia-counterplan and dia-adjudicate state this limit, but the plugin offers no route to a different engine for a panel member.
7. **dia-skopos: no problem observed.**
   - It presented the review, waited, and correctly treated "correction + proceed" as approval of the revised task: the owner changed the reviewers' effort and said proceed.
   - Minor: the owner's prompt asked for a three-line summary before the review. The template has no slot for it, so it was added outside the sections.

## 4. Improvement candidates (to verify here)

| # | Candidate | Touches | How to check (per `AGENTS.md`, Probes and evals) |
|---|---|---|---|
| I1 | A one-shot mode for dia-negative, dia-reductio, dia-counterplan, modelled on dia-warrant's `--mode=audit`: no user question, ends with a fixed findings table (location, problem, evidence with evidence class, severity, suggested fix) | the three SKILL.md files and output templates | Same target, old vs new text, 2 runs per skill: does the run end without a question, and does the table parse the same way across skills? |
| I2 | A review-panel recipe: N lenses in parallel, then dia-adjudicate. A shared claim inventory is built once and given to every lens. Adjudication produces merged issues, a reviewer-error table and a must-check list | dia-router (menu or selection rule), dia-adjudicate inputs | One panel run on a document with known planted defects: are duplicates merged, planted defects kept, and reviewer errors listed? |
| I3 | Sharper lens charters for document targets. reductio skips with one line when the target has no premises usable in a strict derivation. Counting and citation checks go to adjudication (or one lens) | four SKILL.md files | Count findings raised by 3 or more lenses before and after, on the same target |
| I4 | An environment-assumption step for designs that will be executed. List what the run environment will show (repository state, exposed tools, visible state) and check each with a read-only probe or a dry-run log; or hand off to dia-techne | dia-negative or dia-counterplan (design targets), dia-router | Replay the R2 design with the new text: does a reviewer flag the missing `.git` or the account-visibility gap? |
| I5 | Evidence class on every lens finding (tool-checked this session / read in the target / inferred / remembered), with a flag for observations from a different environment | four SKILL.md files | Inspect outputs from I1 runs |
| I6 | A shared context pack for parallel lenses (the claim inventory from I2) to cut repeated reading | I2 recipe | Compare tokens per lens with and without the pack |

Open items for the owner: whether I1 should be a new flag on each skill or a single panel skill; whether a cross-engine panel member (§3, item 6) is in scope given the plugin's "instructions only" package rule (`AGENTS.md`, Rules).

## 5. Limits of this note

- One session, one owner, three targets from one research domain, one engine.
- The main assistant was both the panel's client and its judge, and it wrote this note.
- Token counts and durations are as the host reported them. Finding counts come from the judgement tables. The 0-rejection figure may reflect the judge more than the reviewers.
- The private repository's documents and data are not reproduced here.
