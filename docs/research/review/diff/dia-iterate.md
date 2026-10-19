Verdict: PASS WITH FIXES

Scope: `git diff cae2e4d 7115d2a -- skills/dia-iterate`, plus the dia-iterate parts of docs/spec.md (D19, D20, §4, §5.7, §7.3, §12.2), README.md and tests/. Read against docs/research/dia-iterate.md, its review (which wins on conflicts) and docs/research/README.md ("Applied", "Applied, second batch").

Runs in the tree (read-only):
- `python3 tools/package.py --check`: "ok" for all 7 skills, exit 0.
- `python3 -m unittest discover -s tests`: 13 tests, OK, 1 skipped (the PyYAML-gated frontmatter test, `tests/test_package.py:52`; PyYAML is not installed here, so the new `default_prompt` assertion at :62 was not exercised by the test run. I checked by hand that `skills/dia-iterate/agents/openai.yaml:4` reads `Use $dia:dia-iterate to …`).
- SKILL.md is 88 lines and the description is 549 characters. No Hangul and no product names were added. No hunk depends on a tool.

Hunks that check out (each matches the review's corrected form):
- :14. CRITIC is cited as "loosely" (as the review's A3 says), "not the Self-Refine loop", "relative of dia-refine" (A2), and the reason re-derivation does not count (theme 3). "often" is kept, as C1 says it should be. I fetched arXiv:2305.11738 (Gou et al., CRITIC, ICLR 2024) and arXiv:2310.01798 (Huang et al., ICLR 2024); both are correct.
- :20 and :22. `@dia-iterate` is added, and the fallback uses the neutral wording the review gave word for word.
- :31 (F5). The new text is limited to claims that "bear on the user's conclusion or next action". The "do not filter by severity" and "fluent claims" sentences the review objected to were dropped.
- :35 (M4) locks a fixed value on the strength of its confirming source. :36 and :68 (F11) use the one-line option the review preferred.
- :46 (F1+M2) has "without new external evidence", undoes only the offending edit, and drops the old pass-count metric. :47 (F3) is word for word.
- Worked example :64-69, traced by hand. Round 1 named 4: 2 confirmed, 1 refuted, 1 unverifiable. Locked = 1 refuted + 2 fixed = 3, which matches "Locked: 3 items". Round 2 named 1 and it was unverifiable. Stop rule 1 does not fire. Rule 2 does not fire (the defect was not refuted). Rule 3 fires, so "verification exhausted" is right. The example now agrees with the rules.
- verification-sources.md:11 (M3) now agrees with :31.
- openai.yaml:4, tests/test_package.py:62 and spec §7.3 match theme 1. README.md:13 matches M5. Spec §4 (:90) carries the "(inferred from P3)" label the review asked for.

Findings

1. should-fix: SKILL.md:3 (description) still states the old zero-defects rule.
   Problem: the description says the loop stops on "zero confirmed defects". That is the definition F3 removed. :47 now reads "no defect was named, or every named defect was refuted". Under the description's wording, a run whose defects are all unverifiable stops as "zero defects", not "verification exhausted". This is exactly the misreport F3 was meant to prevent, and the description is the text every surface sees first. The same description still lists invocation forms without `@dia-iterate`, although review F2 asks for "the same change" there. (This half is cosmetic, because the list says "for example".)
   Replacement for :3:
   `description: Improve an output through repeated rounds gated by external verification. Each round fixes only defects that a verification method confirmed, and the loop stops on a regression, zero defects (none named, or all refuted), verification exhausted, a fixed point, or the round cap. Use only when the user's message begins with dia-iterate, or when the skill is invoked explicitly by name (for example /dia:dia-iterate, $dia:dia-iterate, $dia-iterate or @dia-iterate). Without that marker do not activate, however close the request sounds; send single-pass review requests to dia-refine.`
   (About 590 characters. Regenerate afterwards, because the description is mirrored in generated output.)

2. should-fix: the round-1 exception (option b, F4) is stated in one place only, so three other rules still conflict with it.
   a) SKILL.md:82 allows round-1 "style, concision and syntax edits below", but step 4 (:34) still says "Change only confirmed defects … leave unverifiable items untouched". Style and padding are "Not verifiable" (verification-sources.md:15). The step that actually governs edits therefore still forbids what :82 allows. This is the "unstated precedence" defect the review describes, now half-stated.
   b) "below" refers to :83, which covers style and concision only. Syntax appears only in verification-sources.md:8, which is not limited to round 1.
   c) verification-sources.md:14 still lets an un-run counterexample "Apply once, in round 1". That counterexample is the model's own reasoning. It contradicts the new sentence at :14 ("your own re-derivation does not count as one"), spec D19 ("own re-derivation is not verification here"), and :82, which does not list it as an exception.
   Replacements:
   - :34, in place of the last sentence: `Leave refuted items as drafted; leave unverifiable items untouched and list them as unverified. The one exception is the round-1 style, concision and syntax edits under Guardrails.`
   - :82: `- If the only verification method is "on rereading it seems", that round has no verification. Do not make edits in such a round, except round-1 style and concision edits (below) and syntax errors settled without running (references/verification-sources.md), each marked "(style, not verified)" next to the change.`
   - verification-sources.md:8, third cell: `Unverifiable without a run environment. In round 1 only, fix what is settled without running, such as syntax errors, marked "(style, not verified)"`
   - verification-sources.md:14, third cell: `Unverifiable. A counterexample you cannot run is not grounds for an edit; list the leap under Unverified with the counterexample`
   ("next to the change" in place of "the change list marks" also covers the `## Final version` mode, which has no change list; see :75-76.)

3. should-fix: spec.md:185 (§5.7) does not match the skill, although README "Applied" says §5.7 was updated.
   Problem: §5.7 still says "Invocation: first word only" and the fallback "ask in one line for a message starting with `dia-iterate` and stop". SKILL.md:22 now adds "or an explicit invocation of the skill by name", and neither D19 nor D20 records that change. Since §5 is the authority, the skill now departs from it without a recorded decision. "first word only … also count" also contradicts itself, which is the same issue M5 fixed in the README.
   Replacement for the start of :185: `- Invocation: first word or explicit name only. Activate only when the message starts with \`dia-iterate\` or the skill is invoked explicitly by name. If the marker is absent but the skill looks right, ask in one line for a message starting with \`dia-iterate\`, or an explicit invocation of the skill by name, and stop.` (Keep the rest of the bullet.)

4. nit: spec.md:64 (D19) words the stop-rule change imprecisely.
   Problem: "normal progress and unverifiable defects no longer stop the loop wrongly". All-unverifiable rounds still stop the loop; what changed is the stop reason (rule 3 instead of rule 2). D19 also leaves out the new behaviour of undoing only the offending edit.
   Replacement for that clause: `dia-iterate: fewer passes than the previous round is no longer a regression, and a regression undoes only the offending edit; rounds whose defects are all unverifiable stop as "verification exhausted", not "zero defects"; own re-derivation is not verification here.`
   D20 (:65) matches the diff, except that "round-1 style edits are marked unverified" also covers syntax edits (:82).

5. nit: SKILL.md:46. After an undo, the restored defect is not reported.
   Problem: if a fix "introduced a new confirmed defect", undoing it brings back the defect it had fixed. That defect was confirmed and is now in the text again, but only rule 5 (:50) says "say so if confirmed defects remain". Worked through: round n fixes X; round n+1 finds that the fix broke Y; the undo restores X; the loop stops, and the user is never told about X.
   Replacement, after "and stop.": `List any confirmed defect the undone edit had fixed as remaining.`

6. nit: SKILL.md:52. Half of F3 was not applied.
   Problem: the review accepted F3 as a whole, including the :52 sentence that separates "zero defects" from "verification exhausted". The stop order now does this on its own, so nothing is broken. The sentence would still help tool-less runs, where every claim in step 1 now ends unverifiable.
   Replacement for :52: `If round 1 names no defects, or refutes all of them, say so and end. If defects were named but none could be checked, the stop is "verification exhausted", not "zero defects". Do not invent defects to fill rounds.`

7. nit: SKILL.md:31. The new candidate sentence ignores narrowed criteria.
   Problem: it follows "Use the user's criteria if given" with no condition. So `dia-iterate for tone` now also enumerates every number and date. Without tools, each of those then becomes an entry in the unverified list. This widens the scope beyond what the user asked, against :84 ("Do not widen scope").
   Replacement: `Unless the user's criteria narrow the review, list every checkable claim that bears on the user's conclusion or next action (…) as a candidate, whether or not it looks wrong.`

8. nit: SKILL.md:68. Rendering.
   Problem: in GFM, a line placed directly under a table becomes a table row. I checked with markdown-it (commonmark plus the table extension): "Locked: 3 items …" rendered as `<tr><td>Locked: 3 items (total)</td><td></td></tr>`. The "Stopped because" line at :69 already had this problem; the new line repeats it. A model that copies the template will produce a broken table in chat UIs.
   Replacement: put one blank line between :67 and :68.

9. nit: spec.md:406 (P2). The probe is ambiguous for dia-iterate.
   Problem: "the prompt names the skill or uses its marker". dia-iterate activates only on the first word or an explicit invocation form (SKILL.md:20-21). A natural-language prompt that names the skill mid-sentence should get the one-line fallback, by analogy with P6 for dia-refine, so P2 could be scored as either pass or fail.
   Replacement, appended: `; for dia-iterate the prompt begins with \`dia-iterate\`, and a mid-sentence mention should produce the one-line request, not the loop.`

Intended but not applied, or applied only in part (check 5):
- Review F2, description half: finding 1.
- F3, :52 half: finding 6.
- F4 option b, carried into step 4 and the reference: finding 2.
- README "Applied" claims for §5.7: finding 3.
Nothing outside the intended set was changed. The low-severity findings F6, F8–F10, F12 and F13 are correctly left open.

Fidelity (check 3): no Stephanus numbers, Adorno or Duhem–Quine claims touch dia-iterate. The CRITIC and Huang citations are correct (fetched), and "loosely" is honest given that CRITIC regenerates the output from critiques, with no locks or verdict classes. The new rationale "a loop that feeds on its own judgment amplifies its own errors" is uncited. It is consistent with Huang's results and with Xu et al. on self-bias amplification, and it is acceptable as a design statement.
