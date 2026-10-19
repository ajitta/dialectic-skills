Verdict: PASS WITH FIXES

Scope: `git diff cae2e4d 7115d2a -- skills/dia-brainstorm` (SKILL.md, agents/openai.yaml, references/brief-template.md) plus the brainstorm parts of docs/spec.md (D19, D20, §4, §5, §7.3, §12.2), README.md and tests/test_package.py. Intended items for this skill, from docs/research/README.md: theme 1 (F14), theme 2 (F9), theme 4 (F1 in the review's form), then D20 M1, F2, F3, F4, F5.

Mechanical results (run in the tree, read-only):
- `python3 tools/package.py --check`: "ok" for all seven skills, exit 0.
- `python3 -m unittest discover -s tests`: 13 run, OK, skipped=1. The skipped test is `test_frontmatter_and_openai_yaml_parse` ("PyYAML not installed"), which is the test this diff changed (tests/test_package.py:62). Re-run with /usr/bin/python3 (PyYAML 6.0.1): 13 run, OK, 0 skipped, so the new `startswith(f"Use $dia:{s.name} ")` assertion passes. CI installs pyyaml (.github/workflows/check.yml), so CI covers it too.
- SKILL.md is 113 lines (limit 200). Description is 776 chars (limit 1024). No Hangul under skills/dia-brainstorm. No product names. No tool use added.

Coverage: all eight intended items are applied. Hunk by hunk:
- Midwife label (SKILL.md:16) follows the review's form. Padesky and the "(Paul, 1990)" date are dropped, as the review asked. I checked the Theaetetus against Fowler's translation at Perseus, 150c: "I question others but make no reply myself about anything, because I have no wisdom in me … the god compels me to act as midwife, but has never allowed me to bring forth". So "who offers no ideas of his own" is faithful.
- Pushback rule (SKILL.md:101) is the F9 text verbatim, which the review confirmed.
- default_prompt `$dia:dia-brainstorm` matches spec §4 and §7.3, and the test was updated as the review's F14 note required.
- M1 (SKILL.md:73) is the review's exact wording.
- F3 keeps the "risky assumption as a condition" clause and exempts `quick`, as the review asked.
- F4 frames the list as examples, offers "name your own" and drops "fun".
- F5 adds the differ-in-kind rule and keeps the line-limit clause.
- Spec D19 and D20 describe the brainstorm changes accurately.

No blockers. Findings:

1. should-fix — skills/dia-brainstorm/references/brief-template.md:12, and SKILL.md:95. New contradiction: no fallback for "thesis after".
   SKILL.md:95 skips the synthesizing question after a stop signal or at `quick` depth. But the template now always demands "<the user's restatement, …>". On those two paths no restatement exists, so the model must either invent one, which breaks "invent nothing" (SKILL.md:103), or ignore the template. Before the diff the field was "<refined thesis>", which the working thesis filled. A third path is also not covered: an idea "recorded as-is" from Step 0 (SKILL.md:39). There the question "how would you now state the idea?" makes no sense.
   Replace brief-template.md:12 with:
   `- After: <the user's restatement from Step 5, or the working thesis if none was asked; any tightening marked as yours; any live risky assumption written in as a condition, e.g. "…, piloted for one month first">`
   In SKILL.md:95, replace "Unless the user sent a stop signal or the depth is `quick`, first ask one synthesizing question: "Putting it all together, how would you now state the idea?" Use their answer as the thesis after; if you tighten it, mark the tightening as yours." with:
   `Unless the user sent a stop signal, the depth is `quick`, or the idea was recorded as-is, first ask one synthesizing question: "Putting it all together, how would you now state the idea?" Use their answer as the thesis after (otherwise the working thesis); if you tighten it, mark the tightening as yours.`

2. should-fix — docs/spec.md:134 (§5.3). The spec contradicts itself.
   §5.3 still says "Behavior: unchanged from the reference." D19 and D20 now change brainstorm behavior, and the §5 intro was widened to "unless this section, D19 or D20 says otherwise". An explicit "unchanged" in the section still contradicts D19 and D20. Lines 119 and 126 (§5.1, §5.2) have the same problem; those are outside this review.
   Replace with: `- Behavior: the reference, amended by D19 and D20.`

3. should-fix (partial application of F2) — SKILL.md:33 vs :72. Two cadences remain.
   The review (F2) objected to three cadences and asked for a single trigger. The diff merged the pacing cue into the "So far" line but left the `deep` checkpoint at "every ~5 probes" (:33). In `deep` the model now runs a ~4 and a ~5 rhythm side by side.
   Replace SKILL.md:33 "`deep` (no budget; offer a checkpoint every ~5 probes)" with:
   `` `deep` (no budget; every ~4 probes, after the "So far" line, offer a checkpoint) ``

4. nit — SKILL.md:72. The pacing cue has no line to join at `quick` depth.
   At `quick` (~4 probes), half the budget is about probe 2, before any "So far" line is due. "add the pacing cue to that line" then has nothing to attach to, and the cue may be dropped or a "So far" line forced early.
   Replace the second sentence with: `Around half the budget, add the pacing cue to that line, or give it on its own line if no summary is due ("almost there, two or three more").`

5. nit — SKILL.md:16. The pointer's antecedent shifted.
   The new midwife sentence sits between "not the strict method of Plato's dialogues" and "If the user wants that (…)". "That" now grammatically points at the midwife sentence, not at the strict method. Also, "may give a pick in Step 4" drops the condition at :89 ("If the user explicitly asks").
   Replace the last two sentences of :16 with:
   `If the user wants that strict method ("what is X?", contradictions built from their own agreed premises, aporia, no advice at all), switch to the `dia-elenchus` skill. Unlike the midwife of Plato's Theaetetus, who offers no ideas of his own, this skill adds its own labeled options in Step 3 and, if asked, gives a pick in Step 4.`

6. nit (logic) — SKILL.md:101. "the other verdict" assumes there are only two.
   There are three verdicts (sharpened, open, refuted), so "the other verdict" is ill-defined.
   Replace "meets the condition for the other verdict" with `meets the condition for a different verdict`.

7. nit (logic) — SKILL.md:81. "Scale" is a difference of degree, not kind.
   "Each must differ in kind … (a different mechanism, owner or scale, not a variant)". A bigger or smaller version of the same mechanism is a variant, and Step 3.2 has just produced the cheapest and most extreme versions. Listing "scale" as a kind-difference invites exactly the variants the rule forbids. This came from research F5 and the review did not catch it.
   Replace the parenthesis with: `(a different mechanism or owner, not a bigger, smaller or tweaked version)`

8. nit — docs/handoff.md:27. Stale after D20.
   Item 9 still says "High findings and cross-cutting themes 1–4 applied … (spec D19)" and points to "`docs/research/README.md` § Not applied yet". That section no longer exists; it became "Applied, second batch" and "Still open".
   Replace the Notes cell with: `D19 (high findings, themes 1–4) and D20 (second batch) applied 2026-10-20, still as 0.1.0. What remains is in docs/research/README.md § Still open; settle it with the owner before P1.`

9. nit (tracking, fidelity) — docs/research/README.md:49 and references/question-bank.md:54.
   Review misses M2–M6 for brainstorm are neither applied nor listed under "Still open". Item 2 names only "brainstorm F6–F15". M4 is a known misattribution that still ships: question-bank.md:54 has "Hickey: … the accidental complexity". "Accidental complexity" is Brooks's term (No Silver Bullet, 1986); Hickey's is "incidental complexity". Not in scope for this diff, but it should be tracked.
   In README.md:49, change "brainstorm F6–F15" to `brainstorm F6–F15 and M2–M6 (M4 is a fidelity error)`.

10. nit (process) — SKILL.md:7 and plugin-manifest.json.
    Skill files changed, yet `metadata.version` stays "1.0.0" and the plugin stays 0.1.0. The digest in plugin-release.json was re-recorded instead. AGENTS.md ("Changing any skill file requires a new plugin `version` … and the skill's `metadata.version`") and spec §12.1 say otherwise. tools/package.py:19-20 allows re-recording before first release, and there are no tags, so the build is consistent and this is an owner-directed exception ("still 0.1.0"). Handoff item 7 must still bump `metadata.version` at 1.0.0, because brainstorm behavior now differs from its 1.0.0 lineage text. No text change needed now.

Checked and found consistent:
- The "So far" line has no quotation marks (Rule 4) and is a statement, not a second ask (Rule 1).
- The Step 4 criteria prompt is one ask with offered answers, which Rule 1 allows ("is it A or B?").
- "Keep at most three" agrees with "2-3 criteria" and with the template's Criteria line.
- SCAMPER now lives in Step 3 in both SKILL.md:73 and question-bank.md:56.
- The pushback rule agrees with the verdict conditions at :97-99, including "A stop signal is not that answer".
- The synthesizing question respects Rule 5. The brief's section list at :103 is unchanged.
- The description still matches the body. The README row is unchanged and still accurate.
- Spec §12.2's new P3 condition matches docs/probes.md. The P2 explicit-only wording is a conservative test for brainstorm; natural-language routing for it is covered by P7.
