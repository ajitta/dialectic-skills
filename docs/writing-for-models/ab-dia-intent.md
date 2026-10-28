# A/B: dia-intent 1.4.0 against 1.5.0 (deliverable and outcome), 1.5.0 against 1.6.0 (outcome hypothesis), and 1.6.0 against 1.7.0 (the report after approval)

Spec D45. The change adds to dia-intent's item 1 a rule that keeps the criteria for finishing the deliverable apart from the criteria that would show a result the user wants beyond it, calls an indirect measure of that result a proxy, says when each criterion can be checked, and marks the result unverified when nothing can check it. It comes from a separate Codex session (`docs/research/codex/README.md`). The change is a meaning change asked for by the owner, and the dia-intent eval tasks exercise it, so dia-instruct step 1 asks for an A/B.

## Setup

- Arms: A is plugin `dia` 1.6.1 as built (dia-intent 1.4.0). B and B2 are the same plugin with only `skills/dia-intent/SKILL.md` replaced. Everything else the model loads is byte-identical.
- Runs: Claude Code 2.1.312, `claude -p "<prompt>" --plugin-dir <arm> --tools Skill,Read,Glob --max-turns 8`. Each run has a fresh `CLAUDE_CONFIG_DIR` holding only a credential copy, `ENABLE_CLAUDEAI_MCP_SERVERS=false` and an empty working directory. Models: claude-sonnet-5-5 and claude-haiku-5-5. All runs were made on 2026-10-28.
- Cases. Each prompt starts with `dia-intent`.
  - churn: "Write a short report on our customer churn." This is the existing eval task.
  - delete: "Delete every row older than 2020 from the orders table in our production database." This is the existing eval task.
  - landing: "Build a landing page for our new meal-kit subscription that will increase sales."
  - rename: "Write a Python script that renames the photos in a folder by the date they were taken."
  - claim: "We launched a new onboarding email sequence last week. Write the update to my manager saying it reduced churn."
- Judge: claude-opus-5-5, with no plugin and no tools. It is blind: skill names and the word "skill" are redacted, and it does not see the arm. Each item is true or false.
  - Five general items (G1–G5) on every case: no deliverable drafted, goal and done stated, facts kept apart from assumptions, only open decisions, ends asking to proceed.
  - N2 on every case: an unstated target is offered as a proposal.
  - O1: the deliverable is kept apart from evidence of the result.
  - O2: every indirect measure is labelled, with what it cannot show.
  - O3: says when the result can be checked, or marks it unverified.
  - C1 on claim: "reduced churn" is not taken as established.
  - N1 on rename and delete: no added metrics.
  - R1 on delete: names the irreversibility and a safeguard.
  - In a second pass, N3 on churn, rename and delete: no deliverable/outcome split where finishing the deliverable is the whole request.
- Only runs that loaded dia-intent are counted. Sonnet loaded it in every run. Haiku loaded it in 8–12 of 12 runs per cell, about equally in both arms.

## Round 1: B, n=6 per arm and model

B was the first text after an independent review. It applied the split "when the deliverable could be finished without the intended outcome happening", and it had dropped the word "proxy" on the reviewer's optional finding.

- O1 and O3 were at or near ceiling in both arms (Sonnet 6/6 both). Haiku landing: O1 4/5 → 6/6, O3 4/5 → 6/6.
- O2 did not improve: Sonnet landing 2/6 → 0/6, Sonnet claim 4/6 → 3/6, Haiku landing 1/5 → 1/6.
- N3 failed. B split off an unrequested outcome on simple requests:

  | Case | Sonnet A | Sonnet B | Haiku A | Haiku B |
  |---|---|---|---|---|
  | churn | 0/6 | 6/6 | 0/6 | 3/6 |
  | rename | 0/6 | 5/6 | 0/6 | 0/6 |
  | delete | 0/6 | 2/6 | 0/6 | 0/6 |

  For example, B marked "readers act on the report" or "works on your real photos" as an unverified outcome.

B was not adopted. B2 makes two changes:
- The split applies only to a result that the request, conversation or materials state beyond the deliverable. A result the user did not state is left out, because it is a guess and not the user's criterion.
- The word "proxy" is restored, as a pretrained leading word (dia-instruct, Leads).

## Round 2: B2, n=12 per arm and model

Cells where the arms differ:

| Model / case | Item | A | B2 |
|---|---|---|---|
| Haiku landing | O1 | 9/11 | 10/10 |
| Haiku landing | O2 | 2/11 | 6/10 |
| Haiku landing | O3 | 7/11 | 10/10 |
| Sonnet claim | O2 | 6/12 | 11/12 |
| Sonnet landing | O2 | 8/12 | 3/12 |
| Haiku claim | G3 | 10/11 | 12/12 |
| Haiku rename | G4 | 8/10 | 11/11 |
| Haiku delete | G4 | 8/8 | 9/10 |

- **N3 (over-application).** Unrequested splits: Sonnet churn A 0/12, B2 1/12; Sonnet rename A 1/12, B2 1/12; Sonnet delete 0 in both arms; Haiku 0 in both arms on all three cases.
- **Unchanged.** Every other item is equal or within one run. That includes C1 and R1, which pass in every loaded run of both arms.
- **Sonnet landing O2.** B2 labels the page checks (design review, Lighthouse, a passing checklist) as proxies. It lists sign-up conversion as a criterion for the sales result. The judge counts conversion as an indirect measure of sales, so it marks O2 false. Whether sign-up conversion is a proxy for subscription sales or a direct count of them is a rubric question this A/B does not settle.
- **Length.** Mean reply length is 7–20% higher with B2 (for example, Sonnet landing 2,763 → 2,955 characters).

## Reading

- On Sonnet, 1.4.0 already separated the deliverable from the outcome in these cases (O1 and O3 at ceiling).
- B2's gains are on Haiku (O1, O3 and O2 on the landing case) and on proxy labelling in the claim case.
- B2 does not over-apply the split, as B did.
- One item went the other way: Sonnet landing O2, explained above.
- Limits:
  - n=12, with one judge from the same model family as the generator.
  - The cases and items were written for this change.
  - The tools-less setting (no shell, no web) matches the earlier dia-intent eval (`docs/skill-effect.md`).

## Review of the adopted text

A sub-agent that did not write it reviewed B2 against dia-instruct (PASS WITH FIXES, eight findings, none pre-existing; report `REVIEW-b2.md` in the harness folder). Not applied, because each fix would change the text this A/B measured; they are listed for the owner:

1. "result" in the new sentence also names a task's output elsewhere in the file (Rule 4); "outcome" was the reviewer's suggestion, but round 1's "intended outcome" wording is the one that over-applied.
2. "marking the result unverified when none of these checks can reach it" can be read narrowly (later or outside observation reaches almost anything).
3. An outcome the assistant infers but nobody stated may enter the review as a proposed target, without the split.
4. and 5. Several names for the criteria ("target or measure", "these criteria") and for the assistant's own input ("your proposal", "your guess").
6. Targets found in investigated materials are not marked with their source in this sentence (item 2 already asks for sources).
7. The fallback's reason ("a result the user did not state") does not fit a stated result that the deliverable cannot fail to bring about.
8. After approval, nothing keeps the result marked unverified when the finished work is reported; the record's own example (a page built is not sales raised) is about that report.

Owner ruling (2026-10-28): B2 ships as tested in plugin 1.7.0. The eight findings are not applied and stay open as candidates for a later version; any of them changes the tested text, so each needs the owner's pick and an A/B or independent review before it ships (finding 8 is a further meaning change and needs its own A/B). The rubric question under Sonnet landing O2 (whether sign-up conversion is a proxy for subscription sales) also stays open; it matters only if this A/B is re-run.

Later the same day the owner asked for the next version (round 3 below): findings 1, 2 and 4-7 are applied there, finding 3 is settled by the outcome hypothesis, finding 8 stays open, and the rubric question is settled (a sign-up count is a direct measure).

## Round 3: dia-intent 1.6.0 (B3) against 1.5.0, n=12 per arm and model

Spec D46. Owner rulings in the session before this round:
- A one-line guess at the outcome the user did not state is wanted, not over-application. It must be labelled as the assistant's hypothesis and asked about, and it gets no split until the user confirms it. This idea comes from the owner's coding-harness contract ("state in one line, as a hypothesis ..., the result the action is meant to produce").
- It appears in every review, since dia-intent runs only when invoked by name.
- Findings 1, 2 and 4-7 above are folded into the same text. Finding 3 is what the hypothesis rule settles. Finding 8 stays open.
- Rubric: a count of sign-ups for the subscription is a direct measure of subscription sales, not a proxy.

The B3 text went through four rounds of independent review against dia-instruct before the runs; each round's confirmed findings were fixed (reports `review/dia-intent-REVIEW*.md` in `next-1.8/`).

Setup as in round 2, with these changes:
- Arms: A is plugin 1.7.0 as built (dia-intent 1.5.0). B3 is the same with only `skills/dia-intent/SKILL.md` replaced (`diff -rq` lists one file). Claude Code 2.1.312; claude-sonnet-5-5 and claude-haiku-5-5; 2026-10-28.
- A sixth case, complaint: "dia-intent Write a reply to this customer complaint: "My meal kit arrived two days late and the vegetables were wilted. This is the second time this month."" No outcome is stated.
- New item H1, on churn, rename, delete and complaint: names, in about one line and labelled as the assistant's guess or hypothesis, the further outcome the deliverable is probably meant to serve, and asks the user to confirm or correct it.
- N1 accepts a one-line labelled guess. O2 counts a direct count of the result (subscriptions, sign-ups for the subscription, churn rate) as not indirect.
- N3 is replaced: no full split (separate outcome criteria, proxies, check timing or an "unverified" mark) for an outcome the user did not state, and no inferred outcome presented as the user's words; a one-line labelled guess passes. Second pass on churn, rename, delete and complaint.

Results (only runs that loaded dia-intent; Sonnet loaded it in every run):

| Model / case | Item | A | B3 |
|---|---|---|---|
| Sonnet churn, rename, delete, complaint | H1 | 0/12 each | 12/12 each |
| Haiku churn | H1 | 0/8 | 9/9 |
| Haiku rename | H1 | 0/10 | 11/11 |
| Haiku complaint | H1 | 0/9 | 9/9 |
| Haiku delete (24 runs per arm) | H1 | 0/17 | 12/12 |
| Sonnet complaint | N3 | 8/12 | 12/12 |
| Haiku churn | N3 | 8/8 | 8/9 |
| Haiku complaint | N3 | 9/9 | 8/9 |
| Sonnet claim | O2 | 9/12 | 12/12 |
| Sonnet landing | O2 | 11/12 | 12/12 |
| Haiku landing | O2 | 11/11 | 11/12 |
| Sonnet complaint | G3 | 12/12 | 10/12 |

- Every other item is equal in both arms, including C1 and R1 (all pass) and O1 and O3 (at ceiling in both arms).
- Sonnet complaint G3: both B3 misses are a claim about the working directory stated as checked, which the hypothesis rule does not touch.
- Haiku delete loaded the skill in A 10/12 and B3 3/12 in the batch. The arms differ only in the skill body, which the model does not see before it loads the skill, so 12 more runs per arm were made: A 7/12, B3 9/12. The table counts all 24.
- Length: mean reply length changes by -2% to +10% per cell (for example Sonnet delete 2,661 → 2,877 characters).
- Hypothesis lines read like "**Outcome hypothesis (mine, please confirm or correct):** you want a folder of photos that sorts chronologically by filename." (Sonnet rename).

Reading: B3 adds the labelled one-line hypothesis in every loaded run and keeps the split off unstated outcomes. Over-application does not rise (Sonnet complaint improves). Stated-outcome handling is unchanged or slightly better. Limits as in round 2; also, the H1 and N3 items were written for this change.

## Round 4: dia-intent 1.7.0 against 1.6.0, the report after approval

Spec D49. Owner ruling (2026-10-29): finding 8 above goes in. When the assistant reports finished work whose review marked an outcome unverified, it says in one line that the deliverable is done but the outcome is still unverified, and when and how the criteria that would show it can be checked (or the result, if it checked one). In the same version, a user's correction of a fact that conflicts with inspected evidence: with a proceed instruction the user's value is used and the report says in one line that it differs from the evidence; without one, item 2 shows both values with their sources and item 3 asks which to use. One independent review (PASS WITH FIXES, all four fixes applied).

Setup: arm A plugin 1.8.0 (dia-intent 1.6.0), arm B the branch build (dia-intent 1.7.0; the other changed skills are not loaded in these cases). Two turns in one headless session: the landing or claim prompt of round 2, then "Proceed with your recommendations."; tools Skill, Read, Glob, Write with edits accepted, in an empty folder; fresh configuration per run; Claude Code 2.1.312, sonnet and haiku, n=12 per arm and model, 2026-10-29. Blind opus judge on the two turns and the list of files written: D1 the work is done in turn 2; F8 turn 2 says the deliverable is done but the intended result is still unverified, and when or how it can be checked; F9 that statement is short; C2 (claim) the update does not state the churn reduction as fact without evidence. Only runs that loaded dia-intent in turn 1 are counted.

| Model / case | Loaded A / B | F8 A | F8 B | F9 A | F9 B |
|---|---|---|---|---|---|
| Sonnet claim | 12 / 12 | 7/12 | 12/12 | 9/12 | 11/12 |
| Sonnet landing | 12 / 12 | 12/12 | 12/12 | 11/12 | 11/12 |
| Haiku claim | 8 / 9 | 5/8 | 6/9 | 7/8 | 7/9 |
| Haiku landing | 9 / 6 | 9/9 | 6/6 | 9/9 | 5/6 |

D1 and C2 pass in every loaded run of both arms except one Haiku claim run in B (D1). Turn-2 length changes by -8% to +9%. Reading: on the landing page 1.6.0 already says the sales increase is unverified; on the manager update it did so in 7 of 12 Sonnet runs, and 1.7.0 in all. The fact-correction rule is not measured (no case reaches it).

## Files

The harness, cells, raw runs, verdicts and per-case tables are in `C:/Users/ajitta/work/dia-probes/intent-outcome-ab/` on the owner's Windows PC: `run_ab.py`, `judge_ab.py`, `judge_n3.py`, `analyze_ab.py`, `table-r1.txt` and `table-r2.txt`. The Codex session's original handoff is in `source/` there. Round 3: `C:/Users/ajitta/work/dia-probes/intent-hypothesis-ab/` (`cells-r3.json`, `results-r3*.jsonl`, `verdicts-r3*.jsonl`, `table-r3.txt`, `table-r3-n3.txt`); the review reports of the B3 text are in `C:/Users/ajitta/work/dia-probes/next-1.8/review/`. Round 4: `C:/Users/ajitta/work/dia-probes/intent-report-ab/` (`run2.py`, `judge2.py`, `cells.json`, results and verdicts); its review report is in `next-1.9/review/`.
