# A/B: dia-adjudicate with and without writing-for-models

The question: does rewriting `dia-adjudicate` by the writing-for-models rules change how
a model judges? Arm A is the skill as it stands; arm B is the rewrite. Everything else the
judge loads is the same. Results and the reading of them are in `../README.md`.

## Arms

- `A/SKILL.md`: `skills/dia-adjudicate/SKILL.md` from branch `adjudicate-ratchet` at
  `26d8c4e`, byte for byte.
- `B/SKILL.md`: the rewrite. Diff it against A to see every change. In short:
  - The opening "Why the rules below exist" paragraph no longer lists the misrulings
    seen in trials; each one, and the correlated-errors citation, now sits as the reason
    inside the rule that targets it (Rules 2, 3, 4, 5, 10), and the paragraph says so.
  - Old Rules 3 and 4 (overturning needs the source's words; not found is not false) and
    the summary cap from old Rule 9 are one rule, Rule 3, so the condition sits with the
    action it gates (writing-for-models Rule 1). The rules run 1–12 instead of 1–13, and
    every cross-reference was renumbered.
  - Wording only elsewhere: invocation bullets merged; a repeated guardrail merged into
    Follow-up turns; "you" as the one name for the judge; Step 3 says "items" for what
    reports raise and "issues" for the merged points (writing-for-models Rule 4).
  - An independent meaning check (prompt in `prompts/checkers.md`) found three meaning
    changes in the first draft of B; they were reverted before any run.
- `skills/skill-k3/SKILL.md` is B and `skills/skill-m7/SKILL.md` is A: the judges were
  given only these blinded paths. `key/mapping.json` holds the mapping.

## Cases

Four fictional cases, each a target text (`target.md`, sentences labelled S1…), three
review reports (`reports/`, items labelled by report) and sources. The answer key is in
`key/`: `key.json` for case1–case2, `key-r3.json` for case3–case4. Each key gives the true
verdict of every report item, the errors in the target (including ones no report raised),
and the traps.

- case1 (retirement withdrawal rate) and case2 (road building and congestion): sources
  are local raw files in `cases/<case>/sources/`.
- case3 (street trees and heat) and case4 (pair programming): sources are reachable only
  through `tools/fetch.py`, which imitates a summarizing fetch tool. A bare fetch prints
  `fetchdata/summary/<page>.md`, a summary written to omit the sentences that support
  some correct report items (the "summary traps" in `key-r3.json`). A question returns
  the two raw sentences in `fetchdata/raw/<page>.md` with the most content words in
  common with the question, or "The page does not appear to address this."
  Every call is logged to `fetchdata/log/<run>.log` (time, page, `Q` or `FETCH`,
  question). The log appends, so use new run ids or clear the folder before a re-run.

## Runs

| Round | Model | Sources | Runs | Plan | Outputs |
|---|---|---|---|---|---|
| r1 | Opus (`claude-opus-5-5`) | local | 2 per arm per case, 8 | `key/plan.json` | `out/` |
| r2 | Haiku (`claude-haiku-5-5`) | local | 2 per arm per case, 8 | `key/plan-haiku.json` | `out-haiku/` |
| r3 | Haiku (`claude-haiku-5-5`) | summarizing fetch | 3 per arm per case, 12 | `key/plan-r3.json` | `out-r3/` |
| r4 | Haiku (`claude-haiku-5-5`) | summarizing fetch, case4 only | 12 per arm, 24 | `key/plan-r4.json` | `out-r4/` |

Each run was one fresh Claude Code general-purpose sub-agent with the model set per
round, launched in parallel batches from one session on 2026-10-28; prompts are in
`prompts/`. The JSON block at the end of each reply was saved as `<run>.json`, with a
`note` added by hand for what the reply itself said (reports not shuffled, an extra
tool call). `usage.csv` has no header: run, total tokens, tool calls, seconds, as reported
by the sub-agent result. r1 has no `usage.csv`; its means are in `../README.md`. Full
replies and traces were not kept.

Round 4 (2026-10-28, the re-test of r3's one unresolved count, `docs/handoff.md` item 28) was
run differently, to close the harness gaps r3 left: `tools/run_r4.py` runs each judge as a
headless `claude -p` session on Haiku (Claude Code 2.1.312) with a fresh configuration, an
empty working directory, the tools Read, Glob and Bash only, and Bash allowed by the CLI only
for the fetch command and `cd`, so no other tool or command can run. B is the shipped 1.1.0
text (`skills/skill-q5/`, which differs from `skill-k3` in two wording fixes made after r3;
`key/mapping-r4.json`); A is `skill-m7` as before. Full session streams (replies, tool calls,
usage) are kept outside the repository, in `C:/Users/ajitta/work/dia-probes/adjudicate-r4/streams/`
on the owner's Windows PC. Four runs (r4-03, r4-11, r4-12, r4-20) were first made before `cd`
and a quoted fetch path were allowed; every fetch in them was denied, so they were discarded
and re-run. In nine runs, two of them among the re-runs, two to four fetch calls were denied
before the judge retried in an allowed form.

## Scoring

```bash
python3 -I tools/score.py r3     # r1, r2 or r3; scipy for the tests
```

Prints one JSON row per run and the per-arm tests (Fisher exact on runs with any
occurrence, Mann-Whitney on tokens, time, tool calls and fetch calls). Target errors are
matched to inventory claims by regular expression (round 3 only), so check a surprising
row by hand.
