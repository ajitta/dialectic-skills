# Codex session record, summarized (2026-10-28)

English summary of a session the owner ran in Codex on 2026-10-28, separate from this repository's agent sessions. The original handoff (Korean, about 50 KB) is not kept in the repository (D11); it is filed with the A/B harness outside the repository (`C:/Users/ajitta/work/dia-probes/intent-outcome-ab/source/` on the owner's Windows PC). It was written against `main` at `0583ae9` (plugin 1.4.0, 2026-10-25), before D39–D44, so it uses the names `dia-confirm` and `dia-iterate` and counts ten skills plus dia-menu. The review notes and owner rulings below are from 2026-10-28, against plugin 1.6.1.

## What the session was about

The owner wanted the plugin to carry a critical view of AI: skills that teach how to talk to an AI, not a list of prompt tips. The working principles that came out of it:

- An agent that acts is not the party that sets the goal and answers for it ("Agent is not Agency"): the user keeps the goal, constraints, criteria and approval; the assistant shows its assumptions, evidence, uncertainty and what it actually ran.
- A delivered artifact is not the change the user wanted ("Output is not Outcome"). Example: for "build a landing page that raises sales", the page is the output, more sales is the outcome, click or conversion rates are proxies, and only the first can be checked before launch.

These are design principles for the skills, not claims about AI consciousness or legal responsibility. The session dropped a personifying framing ("AI is a sociopath") at the owner's objection.

## Naming (track A)

The owner asked for several rounds of plugin names and prefixes around "agent not agency", "AI not agency" and "output is not outcome", aimed at renaming the repository. The exact lists the model proposed then were not recoverable. The record added five new drafts (agent-not-agency `ana-`, output-not-outcome `ono-`, human-agency `ha-`, outcome-first `of-`, agency-boundary `ab-`), with no uniqueness or search check, and recommended holding any rename.

Review (2026-10-28):

- D42 settled the skill name `dia-intent` on the same day, for the same reason the session gave (the name should say what the review is about).
- The proposed brands describe dia-intent, and at most dia-ratchet and dia-adjudicate; most of the plugin (dia-reductio, dia-elenchus, dia-conjecture, dia-warrant and others) consists of dialectical methods, which those names would misdescribe.
- A rename now also touches the public repository, the `dia@ajitta` catalog entry, the project page and its Search Console property, the pending directory listings (handoff item 13) and the uploaded ChatGPT zip.
- Two-letter prefixes (`ab-`, `ha-`, `of-`) break dia-menu's three-letter prefix rule, and `of` is a common word, the same failure class as `dia 1 thing …`.

**Owner ruling (2026-10-28): no rename.** The principles may be used later as a positioning line (for example in the README), not as a name.

## New skill candidates (track B)

Not implemented; none approved.

| Candidate | Idea | Review (2026-10-28) |
|---|---|---|
| dia-eval | After the work, judge the output (done / not done) and the outcome (supported / not met / cannot tell) from outside evidence only | Its boundary must now be drawn against dia-ratchet (only outside checks count) and dia-adjudicate (verdicts with an evidence class; not found is not false), not dia-iterate. Its distinct part is judging the user's outcome. In a chat, outside evidence is usually missing, so most verdicts would be "cannot tell". Hold. |
| dia-diagnose | The output exists but the outcome did not happen: rival explanations, the observation that would separate them, no cause asserted without evidence | Later than dia-eval; the main risk is a plausible after-the-fact story. |
| dia-control | A table of what the user decides, what the assistant does, what evidence is needed, and where re-approval is needed | Overlaps dia-intent's authority and approval rules; not a separate skill. |
| dia-dialogue | Teach the user the questions to ask an AI | A guide, not a skill; as a skill it would intrude on ordinary chats. |
| dia-compare | Compare competing outputs by outcome criteria | Covered in part by dia-counterplan and dia-brainstorm; wait for a distinct use. |
| dia-consistency | A maintenance check for new skills (routing, authority, evidence claims, tool-less path) | Already covered by dia-instruct, the new-skill procedure in `docs/research/candidates/README.md` and `tools/package.py`. Drop. |

The record's summary of the 2026-10-21 candidate research (`docs/research/candidates/`) is accurate, including dia-commit and dia-hypothesis as the open distinct candidates and the methods not recommended (pre-mortem, debate, Double Crux, learning by teaching).

## dia-confirm draft (track C)

The session drafted a dia-confirm 1.4.2 (plugin 1.5.2, never committed) on top of dia-confirm 1.3.0. It added an Output / Outcome / Proxy split to the goal step, check timing (now, after the output, only by later or outside observation), an "Evaluation basis" for a later evaluation, an extended description, and restored four rules after a diff against the original.

Review (2026-10-28):

- The draft cannot replace the file: it predates D42 (name) and D43 (body rewrite), and its version numbers collide with history.
- The four restored rules are all present in dia-intent 1.4.0 (dependent decisions, facts only the user can supply, investigate-only approval, a new requirement that conflicts with a constraint).
- dia-intent 1.4.0 already separates the outcome from proposed means and asks for observable completion criteria; the new content is only the output/outcome/proxy split and check timing.
- The Evaluation basis serves a skill that does not exist and adds a trigger ("when asked for a handoff"); dropped. The description change would reopen the routing gates that D43 kept fixed; dropped.

**Owner ruling (2026-10-28):** add the split to dia-intent's item 1 as one sentence, description unchanged, and test it by A/B on cases drawn from the record's test table (landing page and sales; a simple rename script that must not get metrics; a request to claim a result with no data), next to the two existing dia-intent eval tasks. Applied as spec D45 (dia-intent 1.5.0). The A/B changed the text: the first version split off unrequested outcomes on simple requests, so the adopted one applies the split only to a result the user or the materials state (`docs/writing-for-models/ab-dia-intent.md`).
