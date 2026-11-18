# dia-panel

A Claude Code plugin with two workflows. `review-panel` reviews one document with four skills from the `dia` plugin at once and then has `dia-adjudicate` judge their reports:

1. Four agents run in parallel, each with one skill: `dia-negative`, `dia-reductio`, `dia-warrant` and `dia-counterplan`. Each returns its whole report in the skill's own layout.
2. Two agents run `dia-adjudicate` on the whole reports, each with the reports in a different order (the second order reverses the first).
3. A last agent lists the items on which the two judgments differ, and gives each judgment's line on what its verdicts leave of the claim, saying whether the two agree. Check the differing items against the sources yourself; the workflow does not.

`judge` is steps 2 and 3 alone, for reports that already exist: review agents you started yourself, another assistant, or people. `dia-adjudicate` asks whoever calls it to make a second, separate run and to compare the two; a judge that runs inside an agent cannot start that run, and a caller that writes its own orchestration tends to leave it out. This workflow makes both runs and the comparison.

It needs Claude Code with workflows (on some plans workflows must first be turned on in `/config`) and the `dia` plugin from the same marketplace, which installs with it. It contains JavaScript workflow files, so it is not part of the `dia` package, which stays instructions only. Codex lists it when the marketplace is added, but installing it there adds nothing, since Codex does not run Claude Code workflows. On chat surfaces without workflows, run the skills one by one as the `dia` README describes.

## Install

```
claude plugin marketplace add ajitta/dialectic-skills
claude plugin install dia-panel@dialectic-skills
```

Start a new session afterwards.

## Use

Ask in a Claude Code session, naming the document:

```
Run /dia-panel:review-panel on docs/design.md
```

To name the central claim the lenses should examine, add it: `... with the claim "the pilot needs 30 runs"`.

To judge reports that are already written, name the document and the report files:

```
Run /dia-panel:judge on docs/design.md with the reports reviews/a.md, reviews/b.md and reviews/c.md
```

An agent that calls the workflow passes `{target, reports, claim}`: `reports` is a list of file paths, with `{text: "..."}` in place of a path for a report the caller holds in memory. The judges see the paths, so give report files names that do not say who wrote them or in what role (`report-1.md`, not `critic.md`). With several documents, pass `targets` and a `claim`, the conclusion the reports are judged against. Do not prescribe an output format for the judges; each returns `dia-adjudicate`'s own sections, and the result holds both runs, the items on which they differ and the list to check by hand.

A `review-panel` run starts seven agents. In one test it took about 11 minutes and cost about US$4.60 on Opus at effort high. A `judge` run starts three. Under `claude -p`, set `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS` (for example to `3600000`), or the print run may stop before the workflow ends.
