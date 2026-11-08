# dia-panel

A Claude Code plugin with one workflow, `review-panel`. It reviews one document with four skills from the `dia` plugin at once and then has `dia-adjudicate` judge their reports:

1. Four agents run in parallel, each with one skill: `dia-negative`, `dia-reductio`, `dia-warrant` and `dia-counterplan`. Each returns its whole report in the skill's own layout.
2. Two agents run `dia-adjudicate` on the whole reports, each with the reports in a different order (the second order reverses the first).
3. A last agent lists the items on which the two judgments differ. Check those against the sources yourself; the workflow does not.

It needs Claude Code with workflows (on some plans workflows must first be turned on in `/config`) and the `dia` plugin from the same marketplace, which installs with it. It contains a JavaScript workflow file, so it is not part of the `dia` package, which stays instructions only. Codex lists it when the marketplace is added, but installing it there adds nothing, since Codex does not run Claude Code workflows. On chat surfaces without workflows, run the skills one by one as the `dia` README describes.

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

A run starts seven agents. In one test it took about 11 minutes and cost about US$4.60 on Opus at effort high. Under `claude -p`, set `CLAUDE_CODE_PRINT_BG_WAIT_CEILING_MS` (for example to `3600000`), or the print run may stop before the workflow ends.
