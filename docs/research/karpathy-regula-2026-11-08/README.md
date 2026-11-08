# Karpathy Guidelines rewrite: outcomes, process, and implications for dia-regula

Session date: 2026-11-08 (Asia/Seoul). Status: research record and unadopted proposals. Reviewed in [review.md](review.md), which corrects the cause of the observed effect, the findings that recurred, and proposals P1 to P4, and records the decisions (spec D65); where they differ, the review wins.

This folder records a session that applied installed dia-regula 2.2.0 to the public Karpathy Guidelines skill, revised the draft while preserving its intent, reviewed it in separate agent contexts, ran a small behavioral comparison, and then re-examined the execution process. The owner's eventual interest was instruction following and the assistant's visible choices during execution, rather than whether the final code was correct.

## Findings to carry forward

- The original and revised text preserved the same core coding requirements in static review. An initial Rule 2 finding was withdrawn because it was not established by that rule. The corresponding exception added to the draft was removed.
- In 36 completed pilot runs, both versions met the functional and scope checks. This did not make their processes identical.
- Among the 15 editing runs per arm, the original produced a specific intermediate policy message after inspecting the files and before changing source in 4 runs; the revision did so in 12. Generic opening announcements and final reports were excluded.
- In the mean-denominator task, the revision's three pilot runs all stated the nonempty-input condition and the intended change/checks before acting. All three checked the current wrong value before writing the fix, even though none first ran a failing assertion against the correct expected value.
- The revision's extra explanations are observable. Better internal judgment, stronger literal compliance, and the causal effect of paragraph layout or reasons are not established.
- The follow-up was incomplete: 24 attempts yielded 11 completed runs and 13 account-usage-limit interruptions. There were no timeouts. It did not meet the requirement of at least 12 valid runs per arm.
- Proposed additions concern mandatory procedure versus discretion, selective disclosure of consequential choices, process-aware evaluation, and auditing reasons for semantic changes. None was installed or adopted as a new dia-regula rule.

## Contents

| File | Purpose |
|---|---|
| [review-and-adjudication.md](review-and-adjudication.md) | Source, drafting, correction history, and separate-context review/judging |
| [behavioral-evaluation.md](behavioral-evaluation.md) | Preregistered pilot criteria, follow-up selection, outcomes, and interruptions |
| [process-analysis.md](process-analysis.md) | Public explanations, actual command order, and method choices |
| [proposals.md](proposals.md) | Candidate changes for dia-regula, with evidence and limits |
| [trace-excerpts.md](trace-excerpts.md) | Selected public messages and executed commands supporting the process reading |
| [inputs/original-SKILL.md](inputs/original-SKILL.md) | Original public skill snapshot |
| [inputs/revised-SKILL.md](inputs/revised-SKILL.md) | Final revision used in the behavioral runs |
| [inputs/dia-regula-2.2.0.md](inputs/dia-regula-2.2.0.md) | Installed review standard used in this session |
| [data/run-results.csv](data/run-results.csv) | All 60 attempted runs; invalid attempts are not task failures |
| [data/phase-summary.json](data/phase-summary.json) | Pilot and follow-up kept separate |
| [data/process-observations.csv](data/process-observations.csv) | Post-hoc process observations for the 47 completed runs |
| [data/process-observations.json](data/process-observations.json) | Public intermediate messages and process categories, without local command paths |
| [data/cases.json](data/cases.json) | Exact common prompt, task prompts, initial fixtures, and independent functional checks |
| [data/provenance.json](data/provenance.json) | Versions, input hashes, archive hash, and data-retention limits |

## Source and versions

The original was fetched from [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills/blob/2c606141936f1eeef17fa3043a72095b4765b9c2/skills/karpathy-guidelines/SKILL.md), commit `2c606141936f1eeef17fa3043a72095b4765b9c2`, blob `6a62d0441753157ca6ca50479e490c2948033adb`. At the initial inspection, the public main response and that pinned content were identical. Its frontmatter declares MIT. The upstream file was not changed.

The installed dia plugin directory was version 2.7.0. The individual review skills used here were dia-regula 2.2.0, dia-negative 2.2.0, dia-warrant 2.3.0, dia-emend 2.0.0, and dia-adjudicate 2.2.0. The plugin directory version is not the skill's internal version.

The behavioral harness requested `gpt-6.1-sol`, effort `high`, through Codex CLI 0.167.0. The backend build identifier was not exposed. The revision's SHA-256 was `D99D3B1BD4D04BD866ACA10479B24ECAF4864053F08DB44F1D0715AB3275346D` throughout the runs.

## Evidence boundaries

This is an English research synthesis of a Korean conversation, not a verbatim transcript. The input snapshots and numeric data retain the recorded content. Four review agents and two judging agents used separate contexts of the same inherited model; they were not different-model or human checks. Their agreement is not independent empirical evidence of an instruction's effect.

The behavioral data contain actual task execution, not just model opinions about the prompts. Nevertheless, most tasks were small and easy, the follow-up was incomplete, and the process categories were selected after the outcome analysis. Paragraph layout and added reasons changed together. There was no no-skill arm and no component ablation.

The full local execution archive was retained during the session and is identified by hash in provenance. This public folder contains summaries, inputs, task fixtures, public messages, and selected trace excerpts; it does not publish the full native event archive, private local paths, account timing messages, or credentials. Do not treat these notes as providing independently reproducible access to every original event.

No shipped skill, manifest, generated plugin, or release artifact was changed by this research record. New model evaluations were not run while saving it to the repository.
