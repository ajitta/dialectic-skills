Verdict: PASS WITH FIXES

Scope: `git diff 7115d2a 395098a` for skills/dia-iterate, docs/spec.md, docs/probes.md, README.md, AGENTS.md and docs/handoff.md; the whole of SKILL.md and verification-sources.md as they are now. Runs in the tree: `python3 tools/package.py --check` printed "ok" for all 7 skills (exit 0). `python3 -m unittest discover -s tests` ran 13 tests, OK, 1 skipped (the PyYAML-gated test; openai.yaml:4 checked by hand and unchanged). SKILL.md has 89 lines, the description has 582 characters, there is no Hangul, and the only product name is "Context7" (verification-sources.md:9), which spec §5.7 mandates. Every tool use stays conditional. dia-iterate is not one of the two re-routed descriptions; the dia-refine description (:3, :21) still points multi-round requests to dia-iterate, which is consistent.

| # (pass 1) | Status | Evidence |
|---|---|---|
| 1 description zero-defects | fixed | SKILL.md:3 now reads "zero defects (none named, or all refuted)" and adds `@dia-iterate`; agrees with :47 |
| 2a step 4 vs exception | fixed | :34 "The one exception is the round-1 style, concision and syntax edits under Guardrails." |
| 2b "below" / syntax | fixed | :83 names style and concision (below) and syntax (the reference) separately; verification-sources.md:8 says "In round 1 only" |
| 2c un-run counterexample | fixed | verification-sources.md:14 now says "Unverifiable … not grounds for an edit" |
| 3 spec §5.7 invocation | partly | spec.md:186 fixed. spec.md:272 still says "First word only by design" (new finding 3) |
| 4 D19 wording | fixed | spec.md:64 uses the proposed clause and adds the `@dia-iterate`/by-name note |
| 5 restored defect | fixed | :46 "List any confirmed defect the undone edit had fixed as remaining." (where to list it: new finding 5) |
| 6 :52 split | fixed | :52 matches the proposed text |
| 7 narrowed criteria | fixed | :31 "Unless the user's criteria narrow the review, …" |
| 8 table rendering | fixed | blank line at :68 separates both trailing lines from the table |
| 9 P2 ambiguity | fixed | spec.md:407 and handoff.md:20 say dia-iterate prompts start with `dia-iterate`, and a mid-sentence mention should get the one-line request |

No pass-1 finding was deliberately left open. Low findings F6, F8–F10, F12 and F13 stay listed as open in docs/research/README.md:53, which is acceptable.

New findings

1. should-fix (existed before this diff; I missed it in pass 1, and the new :52 makes it visible): SKILL.md:48, stop rule 3 is ambiguous and, read literally, contradicts the worked example.
   "every remaining defect is unverifiable": once round 1 has fixed its confirmed defects, the only defects left are the unverifiable ones, or none at all, which makes the rule vacuously true. Read that way, rule 3 fires after every round 1, and the loop never reaches round 2. Yet the template (:66-67) runs round 2 after a round with 2 confirmed, 1 refuted and 1 unverifiable. :52 ("named but none could be checked") assumes the narrower reading. Without a second round, the regression rule (:46) can never catch a fix that broke something.
   Replace the first sentence of :48 with: `3. **Verification exhausted**: no defect named this round was confirmed, and at least one was unverifiable (any others were refuted). Stop and hand the unverified list to the user, …` (keep the rest as is). Checks: the example's round 1 continues and round 2 stops; P8 (nothing confirmed) still stops after round 1; :40's "usually stops after round 1" still holds.

2. should-fix: docs/probes.md:23, :25 and :70 say the P6/P8 re-runs came "after D21", but the dia-iterate cells (:78, :80) ran dia at `7115d2a`. D21's dia-iterate edits are in a506214 (`git diff 7115d2a a506214 --stat -- skills/dia-iterate`: 2 files changed). The current SKILL.md text, including :34, :46, :52 and verification-sources.md:8 and :14, has never been probed. The results probably still hold, since nothing in them depends on the changed lines, but the label overstates what was tested.
   :23 → `pass; re-run from a neutral directory at 7115d2a (before D21's skill edits): pass`
   :25 → `pass after a fix to dia-refine; re-run from a neutral directory at 7115d2a (before D21's skill edits): pass`
   :70 → `### Neutral-directory re-run after spec D19–D20, with D21 routing and label cells (2026-10-20)`
   Alternatively, re-run P6/P8 for dia-iterate at the current commit.

3. nit: spec.md:272 still says "First word only by design", which contradicts §5.7 (:186) and SKILL.md:20. This is the remainder of pass-1 finding 3.
   Replace with: `| dia-iterate | false | First word or explicit name only, by design |`

4. nit: spec.md:66 (D21) misdescribes the change. It says "dia-iterate's description, step 4 and verification table state the round-1 exception consistently". The description (:3) does not mention the round-1 exception; what changed there is the zero-defects definition and `@dia-iterate`. D21 also leaves out the :52 split and the table fix.
   Replacement clause: `dia-iterate's description defines zero defects as the stop rule does and lists @dia-iterate; step 4, the Guardrails and the verification table state the round-1 exception consistently; round 1 separates "zero defects" from "verification exhausted"; an undone fix lists the defect it had fixed; narrowed criteria narrow the candidate list; the round-summary template renders as a table`

5. nit: SKILL.md:46 and :50 tell the model to report remaining confirmed defects, but the output template (:58-74) has no place for them, and "## Unverified" is the wrong section, because they are confirmed. A model may leave them out or put them under Unverified.
   After :70 add the template line: `Confirmed but not fixed: (item, or "none")`, and at :46 replace "as remaining" with `under "Confirmed but not fixed"`.

6. nit (my own pass-1 wording, now applied): SKILL.md:83 and verification-sources.md:8 mark syntax fixes "(style, not verified)". A syntax fix is not a style edit, so the label misinforms the user.
   :83: `…, marked "(style, not verified)" or, for syntax, "(not verified)", next to the change.` In verification-sources.md:8, replace the marking with `marked "(not verified)"`.

No other contradictions found. The description, Invocation (:20-22), spec §4 :91, §5.7 :186, README.md:14 and D19 now agree on "first word or explicit name". Step 4, Guardrails :83-84 and verification-sources.md:8, :14 and :15 agree on the round-1 exception. :52 and stop rules 2 and 3 agree, provided rule 3 is read as in finding 1.
