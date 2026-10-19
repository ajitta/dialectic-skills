# Skill mode: a loop where a skill edits a skill

The procedure when the target is a skill folder. Same principle as output mode, except the verification signal is "the result of actually carrying out a test prompt" and the thing edited is SKILL.md rather than a deliverable. Structurally this matches skill-creator's iterative-improvement procedure; it differs in checking the stopping conditions mechanically each round and in keeping the conditions for editing narrow.

## Setup

1. **Working copy.** Copy the target skill with `cp -r` to `<workspace>/<skill-name>/`, and put the original state once more in `<workspace>/snapshot/`. Do not "copy" by reading the files and retyping them: if the model emits whole files, the content filter may block the response, whereas a tool copy leaves nothing in the output. Install paths (`/mnt/skills/...`, `~/.claude/skills/...`) are read-only or must stay as the rollback baseline, so leave them untouched during the loop.
2. **Test prompts.** Use `evals/evals.json` if present. Otherwise write 2-3 prompts a real user might type. Requests with context attached (a file path, a situation, a constraint) actually trigger the skill; abstract ones ("review this file") often don't. If the user has already ordered the run and did not ask to review the prompts, do not stop: show the prompts verbatim ahead of the results and proceed. If feedback comes back that a prompt was unsuitable, that becomes the external evidence for the next round. Show the prompts and stop only if the user asked to review them, or if the target skill's scope is unclear enough that confirmation is needed before editing.
3. **Round log file.** Record the items below per round in `<workspace>/iterations.md`. Do not paste excerpts of test outputs or of SKILL.md into it. Point to defects by location plus a span of a clause or less.

## One round

1. **Run.** For each test prompt, read the working copy's SKILL.md and carry out the task as it instructs. Where subagents exist (Claude Code, Cowork) run them in parallel; where they don't (Claude.ai) run sequentially and directly. Running directly means the same party used the skill and evaluates it, so the blind spots are shared. Note that limitation in the round log.
2. **Collect defects.** Apply one output-mode round to each result. Only confirmed defects go forward. Unverifiable defects are never grounds for editing the skill.
3. **Sort by cause.** Put each confirmed defect in one of these:
   - (a) the skill has no instruction covering it.
   - (b) the instruction exists but wasn't followed.
   - (c) it is specific to that prompt.
   - (d) it is a model limitation no instruction fixes.
   - (e) a newly added instruction conflicts with an existing one. Editing a skill always means adding lines to existing text, so this conflict can arise with any edit.
4. **Select what to edit.** (a), (b), and (e) are editable. Among those, pick only what recurred across two or more tests, or what appeared in one test but can be explained as generalizing. A sentence added to fit a single case makes that case pass and turns the skill into a tool for that case alone. For (e), when both conflicting lines were written by the skill, fix one or state the precedence. When one side is wording the user specified, do not change it: roll back per the regression rule and report the conflicting existing rule together with alternative wording that does not conflict. If the executor rewrites the user's wording, what gets verified is no longer what the user asked for.
5. **Edit.** For (a), add the instruction along with its reason. For (b), find in the run log why the instruction was ignored — usually it comes too late, conflicts with another instruction, or commands without giving a reason. Fix by supplying the reason rather than by adding more capitalized prohibitions. Confine edits to SKILL.md and `references/`. Create `scripts/` only when several tests each wrote the same helper code themselves.
6. **Rerun and compare.** Run the same tests against the edited copy and compare defect counts. Count newly introduced defects too.
7. **Lock.** Record which defects disappeared in the tests that passed this round; the instruction that removed them is locked. Deleting or weakening that instruction in a later round requires a new run result as evidence.

## Stopping conditions

One more is added to output mode's five.

- **Nothing to edit**: confirmed defects remain but all are (c) or (d), so no skill edit fixes them. Stop and hand those defects to the user.

Regression means "total confirmed defects rose" or "a defect that had disappeared in the previous round came back." On regression, roll back to the previous copy and stop.

## Installation

When the loop ends, show the user the following and get approval.

- `diff -u` against the original. Do not show the revised SKILL.md in full
- Round summary (defect counts per round, what was edited, why it stopped)
- Defects the edits did not fix

After approval:

- **Claude.ai**: build a `.skill` file with skill-creator's packager and hand it over. Keep the original skill name.
  ```bash
  cd /mnt/skills/examples/skill-creator && python -m scripts.package_skill <workspace>/<skill-name> <output-path>
  ```
- **Claude Code**: apply the diff at the original path.

Tuning the `description` field for trigger accuracy is out of scope here. skill-creator's `run_loop.py` does that, and only in environments with `claude -p`.

## What this loop cannot do

- It cannot change the model. Only SKILL.md changes, and when the session ends only the saved files remain.
- Situations the test prompts don't cover don't improve. The test set's coverage is the improvement's coverage.
- When the evaluator is the same model as the executor, errors they share go uncaught. Human review fills that gap.
