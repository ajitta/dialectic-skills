# dia-intent: low-severity findings

Worktree: /home/ubuntu/work/dia-review/lowfix. Files changed: `skills/dia-intent/SKILL.md` and `skills/dia-intent/agents/openai.yaml`. The description, metadata and frontmatter are unchanged.

## Per finding

- **F1, state why the gate is unconditional: declined (owner question 1).** The rationale ("the user invoked this skill to see the review before any work") settles open question 1, whether a user can waive the hold in the invoking message. The parts that do not depend on that question are already in the skill: the hold is at "Until approval, present only this review…" plus "The original task request does not itself count as approval", and the short form is at "Scale the review to the task; a few sentences may suffice."
- **F2, empty decision list: applied** (SKILL.md item 3), using the review's minimal text: "…explain each one's effect." -> "…explain each one's effect. An empty decision list is normal; do not add items to fill it."
- **F4, limit for open-ended work: applied** (SKILL.md, Confirmation template only): "…sent or spent and its recipient, any requested step…" -> "…sent or spent and its recipient, the limit for open-ended work (such as a budget, count or stopping point), any requested step…". For bounded tasks, the completion criteria in item 1 already give the ending condition (review F4), so no body rule was added.
- **F8, description wording for explicit invocation: declined (owner question 2).** The review found that widening the description would trigger on Claude but not on Codex or ChatGPT, where `allow_implicit_invocation: false` hides the skill. That breaks the requirement to run unchanged on every surface. It would also change spec §5.1/§7.3.
- **F9, behavioral probe: declined.** It calls for a probe in docs/probes.md, not a skill change, and the probe is outside this task (no CLI runs here).
- **F10, split long paragraphs: applied** (SKILL.md), wording unchanged:
  - Investigation paragraph -> a lead sentence plus 5 bullets (probe definition and isolation; no data out or charges; probe result; when to stop; do not offer investigation as an option). "If that isolation cannot be ensured…" moved up to sit with the isolation definition it refers to.
  - Item 3 -> a lead sentence plus 3 sub-bullets (do not ask what is settled; when to keep a choice; requested irreversible steps).
  - Dependent-decisions paragraph -> a lead sentence plus 4 bullets.
- **F11, quote constraints verbatim: applied in the review's narrowed form** (SKILL.md, first paragraph of Before Starting): "…preserve the user's constraints and authority boundaries." -> "…boundaries, quoting short exact constraints (such as a name, amount or date) in the user's words." The rule is limited to short constraints whose exact form matters, not a general rule to present things verbatim.
- **M4, calculations vs a preliminary deliverable: applied** (SKILL.md, hold paragraph): "Do not include a preliminary deliverable in the review." -> "…in the review; when the deliverable is itself a calculation or analysis, show only the calculations that decide its scope or the open decisions."
- **M5, short_description length: applied for this skill only** (agents/openai.yaml): "Restate the goal, disclose assumptions and list open decisions before work starts" (81 chars) -> "Confirm the goal, assumptions and open decisions before work" (60 chars). No test or tool checks this field. The other six dia skills still exceed 64 characters, so the repo is now inconsistent until they are shortened as well (repo-wide nit).
- **M6, direct follow-ups: applied** (SKILL.md, end of the "Update the working interpretation" paragraph): appended "Handle a direct follow-up to the approved task under this paragraph, not with a new full review." A follow-up that widens scope or authority is re-agreed for the changed portion only, and routine details proceed. This matches the description's "Apply to that task and its direct follow-ups".

## Consistency check

I reread the whole SKILL.md after the edits and found no contradictions:
- "The rules for isolated probes still apply" still points at the investigation block, which still includes the no-data-out bullet.
- The F4 limit is part of the work to approve, not a question.
- F2 and M4 agree with "omit empty sections", item 2 and the template.
- No Hangul, no product names, and tool use is still conditional.

Notes for the parent:
- F2, F4, F11, M4 and M6 may each need a D-entry line under spec §5. I did not edit docs/.
- The only failing test is `test_committed_output_is_current`, because plugins/dia has not been regenerated yet.

## Size

SKILL.md: 79 lines (limit 200). Description: 271 characters, unchanged.
