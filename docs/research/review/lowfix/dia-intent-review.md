Verdict: PASS WITH FIXES

Scope: `git diff 1b3f139 b430a97 -- skills/dia-intent`. SKILL.md has 6 hunks and agents/openai.yaml has 1. The same diff over `docs/spec.md README.md tests/` is empty: this commit changes no docs or tests at all (see finding 1). Line numbers refer to the tree at b430a97.

Commands run in the tree (read-only; the worktree is clean):
- `python3 tools/package.py --check`: "ok" for all seven skills, exit 0.
- `python3 -m unittest discover -s tests`: "Ran 13 tests ... OK (skipped=1)".
- plugins/dia/skills/dia-intent/{SKILL.md, agents/openai.yaml} and the zip entry are byte-identical to the source.
- SKILL.md is 79 lines (limit 200). The description is unchanged at 271 characters. No Hangul under skills/dia-intent. A grep for claude, codex, chatgpt, openai, gpt, anthropic and gemini in SKILL.md finds nothing. Tool use is still conditional (l.24: "if a decisive read or probe is available and permitted").
- F10 was meant to change no wording. I split the old and new SKILL.md into sentences and compared them. The only sentences added or changed are the F2, F4, F11, M4 and M6 edits. Every other sentence is unchanged, so the restructure changed no wording.

## Intended vs applied

Intended for dia-intent: the low items in docs/research/README.md § Still open (F1, F2, F4, F8–F11), in the review's corrected form. The implementer also took review nits M4–M6.

| Item | Review's corrected form | Applied | Verdict |
|---|---|---|---|
| F1 | settle open question 1 first | declined | justified (review/dia-intent.md:21) |
| F2 | "An empty decision list is normal; do not add items to fill it." | SKILL.md:30, word for word | correct |
| F4 | resource limit for open-ended work only; l.28 criteria already cover bounded tasks | template only, SKILL.md:79 | correct and minimal |
| F8 | keep as owner question; it would split Claude from Codex/ChatGPT behaviour | declined | justified (review:63-67) |
| F9 | medium probe, not a low; not a skill change | declined | justified; out of scope |
| F10 | bullets, wording unchanged | l.18-24, l.30-33, l.35-40 | wording unchanged, but one cross-reference got weaker (finding 2) |
| F11 | only short constraints whose exact form matters | l.16 | correctly narrowed; nit (finding 4) |
| M4 | "show only the calculations that decide scope or decisions" | l.44 | slightly narrowed (finding 5) |
| M5 | repo-wide nit | intent only, openai.yaml:3 (81 → 60 chars) | partial (finding 3) |
| M6 | one sentence: follow-ups take the re-agree path | l.61 | correct |

No item meant for this batch is missing. Nothing from F3's dropped "other limited resources" or F8's widened description leaked into the text. Check 3 (fidelity): the diff adds no method claim or citation. I did fetch openai/skills skill-creator/references/openai_yaml.md: it says "Human-facing short UI blurb (25–64 chars)", which confirms M5's basis. Check 4 (logic): the diff adds no logical example. The stop conditions (l.23) and approval rules (l.52-57) are unchanged and still agree with each other.

Checked and found consistent:
- F2 agrees with "omit empty sections" (l.42) and with the template's "Omit if nothing remains" (l.76).
- The F4 limit is part of the work to approve, so it sits in the confirmation and is not a new question. If the limit is a user preference, such as a spending budget, item 3's "material and not delegated" bullet (l.32) still puts it among the decisions with a recommendation.
- M6 agrees with the description's "Apply to that task and its direct follow-ups" (l.3), with "After approval, use the format appropriate to the task" (l.65), and with "asking about the changed portion only" (l.61).
- The nested bullets under item 3 use a 3-space indent, which is correct for a "3. " list marker.

## Findings

1. should-fix. docs/spec.md:109, :121; docs/research/README.md:50-53. The behaviour changes are not recorded.
   - Problem: spec §5 says the skills "keep their reference behavior unless this section or D19–D22 say otherwise" (spec.md:109), and §5.1 says "Behavior: the reference, amended by D19–D22" (:121). F2, F4, F11, M4 and M6 change behaviour (research open question 5; the implementer's own report says each "may need a D-entry"). No D-entry covers them, so the spec no longer describes SKILL.md. docs/research/README.md:53 also still lists "intent F1, F2, F4, F8–F11" as open, although F2, F4, F10 and F11 are now applied and F1 and F8 are owner questions.
   - Replacement: add a spec row after D22: "| D23 | Remaining low research findings, in the reviewed forms (2026-10-20). dia-intent: short exact constraints (a name, amount or date) are quoted in the user's words; an empty decision list is normal and is not padded; when the deliverable is itself a calculation or analysis, the review shows only the parts that decide its scope or a decision; the confirmation names the limit for open-ended work; a direct follow-up is handled by the re-agreement rule, not by a new full review; the three longest paragraphs are bulleted without wording changes; `short_description` is 60 characters. Left for the owner: F1 (depends on research open question 1) and F8 (question 2). |". Change "D19–D22" to "D19–D23" at spec.md:109 and :121. In research/README.md:53, replace "intent F1, F2, F4, F8–F11" with "intent F1 and F8 (owner questions 1 and 2), F9 (behaviour probe of the current text; the run at probes.md:79 predates D21 and D23)".

2. should-fix. SKILL.md:54. The F10 split weakens the cross-reference that carries the no-data-out rule.
   - Problem: "For an investigation, it lifts the limit on how far to investigate, but the rules for isolated probes still apply." The pass-2 review accepted this only because the no-data-out sentence sat "in the same paragraph" as the probe rules (review/pass2/dia-intent.md, finding 1 status; review/diff finding 1). That sentence is now its own bullet, l.21, and it covers reads and searches, not only probes. "The rules for isolated probes" now reads most naturally as bullet l.20 alone. So after an "investigate only" approval, a model can take web searches built from private material as allowed. This is a behaviour change from a refactor that was meant to change no wording. It also leaves open what D20 meant by "before approval".
   - Replacement for that sentence: "For an investigation, it lifts the limit on how far to investigate, but the isolation rule and the rule against sending private material out or incurring charges still apply."

3. nit. agents/openai.yaml:3 (M5). Applied to one skill only.
   - Problem: the review calls M5 "a repo-wide nit" (review:142). docs/research/README.md:19 says cross-cutting fixes should be "decided once and applied to all of them". The other six short_description values are still 77–94 characters, against the 25–64 guidance. A UI blurb has no runtime effect, so this is cosmetic.
   - Replacement: shorten the other six in the same batch, or add this line under docs/research/README.md § Still open: "3. `short_description` exceeds the 25–64 character guidance in six skills (intent review M5, repo-wide); only dia-intent is shortened (D23)."

4. nit. SKILL.md:16 (F11). The new example overlaps item 2's check rule, and the apostrophes are mixed.
   - Problem: "a date" is the example in both rules. Item 2 (l.29) says to check facts you will repeat against a quick computation "rather than copying them from the materials". The new rule says to quote such a constraint "in the user's words". A model can read the quote as exempt from the check. For example, "Friday 24 October" would be quoted unchanged although 24 October 2026 is a Saturday. The same sentence also mixes "user’s" (U+2019, the only curly apostrophe in any SKILL.md) with "user's".
   - Replacement for l.16's second sentence: "Treat explanations and means as hypotheses when appropriate; preserve the user's constraints and authority boundaries, quoting short exact constraints (such as a name, amount or date) in the user's words and still checking them as item 2 says."

5. nit. SKILL.md:44 (M4). "the open decisions" is narrower than the review's text, and "calculations" does not fit an analysis.
   - Problem: the review proposed "show only the calculations that decide scope or decisions". "the open decisions" leaves out a calculation that settles a point, so that it moves to evidence. Item 2 (l.29) asks for exactly that: "contrary evidence that could change the decision". For a non-numeric analysis there may be no "calculations" at all.
   - Replacement for the clause: "when the deliverable is itself a calculation or analysis, show only the parts of it that decide its scope or a decision in the review."

## Declined items

- F1: the decline is justified. The review says the finding "presupposes the answer to open question 1 … Settle that question first" (review:21). The parts that do not depend on that question already exist: the hold (l.44, l.46) and the short form (l.42). One caveat: F1 is now open only as an owner question, and the docs do not record that (finding 1).
- F8: the decline is justified. With `allow_implicit_invocation: false`, a wider description can never fire on Codex or ChatGPT (review:64-66). It would also change spec §5.1 and §7.3 ("Its description says explicit only", spec.md:267).
- F9: the decline is justified. F9 is medium, not low, and it is a probe, not a text change. An intent behaviour run exists (probes.md:79), but it was made at 7115d2a, before D21 and this batch. Re-run it before acceptance.

## The implementer's report, checked

The per-finding claims, the sizes (79 lines; description 271 characters) and the "wording unchanged" claim for F10 are accurate. Its consistency claim, "'The rules for isolated probes still apply' still points at the investigation block, which still includes the no-data-out bullet", is the weak point (finding 2). Its note that only `test_committed_output_is_current` failed applied to its own worktree before regeneration. In b430a97 the output is current and every check passes.
