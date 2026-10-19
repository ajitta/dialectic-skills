Verdict: PASS WITH FIXES

Scope: the 7115d2a..395098a diff for brainstorm and the docs. I re-read all of the current SKILL.md, brief-template.md and openai.yaml, plus dia-elenchus's description and Step 0.

Mechanical checks, run in the tree:
- `python3 tools/package.py --check`: "ok" for all 7 skills, exit 0.
- `python3 -m unittest discover -s tests`: 13 run, OK, skipped=1 (no PyYAML); with /usr/bin/python3 (PyYAML 6.0.1): 13 OK, 0 skipped.
- SKILL.md 113 lines; descriptions 873 (brainstorm) and 970 (elenchus) chars. No Hangul, no product names, no new tool use.
- Skill files are identical at c0ccd3d and 395098a.

## Per-finding status

| # | First-pass finding | Status | Evidence |
|---|---|---|---|
| 1 | No fallback for "thesis after" | fixed | brief-template.md:12 and SKILL.md:95 match my wording, including the recorded-as-is path |
| 2 | §5.3 says "unchanged" | fixed | spec.md:135 "the reference, amended by D19–D21" (§5.1 :120 and §5.2 :127 too); §5 intro :109 |
| 3 | Two cadences in `deep` | fixed, but my wording caused new finding 1 | SKILL.md:33 |
| 4 | Pacing cue has no line at `quick` | fixed | SKILL.md:72 |
| 5 | Pointer antecedent / "may give a pick" | fixed | SKILL.md:16, verbatim |
| 6 | "the other verdict" | fixed | SKILL.md:101 "a different verdict" |
| 7 | "scale" counted as a difference in kind | fixed | SKILL.md:81 |
| 8 | handoff item 9 stale | fixed (different words, accurate) | handoff.md:27; docs/research/README.md:50 "Still open" exists |
| 9 | M2–M6 untracked; Hickey term wrong | fixed | question-bank.md:54 "incidental complexity" (Hickey, "Simple Made Easy"); README.md:46 third batch notes M4; :53 lists M2, M3, M5, M6 |
| 10 | Version not bumped | deliberately left; acceptable | AGENTS.md:26 and handoff.md:7 now document the pre-release exception. Correction to my first pass: `metadata.version` 1.0.0 is dia-brainstorm's own first version (lineage 3.3.1 is separate) and was never released, so item 7 does not need a brainstorm-specific bump. |

## Routing and description check

- The two descriptions (brainstorm SKILL.md:3, elenchus SKILL.md:3) agree with each other and with D21 (spec.md:66): Socratic dialogue or method goes to dia-elenchus unless the user asks to brainstorm.
- probes.md:74 "same apart from the skill names" holds for brainstorm (upstream vs 7115d2a).
- Fisher exact, 6/6 vs 1/6: two-sided p = 0.01515, so "p ≈ 0.015" holds. I could not re-run the routing counts (no CLI allowed).
- D21's brainstorm clause is true of the files. P2 (spec.md:407, handoff.md:20) matches the P7 prompts (probes.md:47).

## New findings

1. should-fix: SKILL.md:33 now bundles two asks, which breaks Hard rule 1 (SKILL.md:20).
   This comes from the replacement text I proposed in the first pass. In `deep`, the checkpoint offer is pinned "after the 'So far' line". That line opens the message that also carries the next probe, so the message holds two asks ("keep going or wrap up?" plus the probe). The reference never defined "checkpoint" either.
   Replace `deep` (no budget; every ~4 probes, after the "So far" line, offer a checkpoint) with:
   `` `deep` (no budget; every ~4 probes, send the "So far" line with one ask, whether to keep going or wrap up, in place of that turn's probe) ``

2. should-fix: SKILL.md:37 contradicts the new description (SKILL.md:3).
   The description now sends a general "Socratic method" request that does not ask to brainstorm to dia-elenchus. Step 0 still treats exactly that case ("socratic method", "does not ask for brainstorming or options") as normal brainstorm work and continues. The sibling dia-elenchus also claims that case (elenchus SKILL.md:53), so both bodies now treat it as their own. The line can only fire once this skill is already loaded, through a misroute (the P7 failure mode) or an invocation by name, so it should say so.
   Replace "If the request only says "Socratic" in general ("do it Socratically", "question me like Socrates", "socratic method") and does not ask for brainstorming or options, add one line to that same message:" with:
   `If the request only says "Socratic" in general ("do it Socratically", "question me like Socrates", "socratic method") and does not ask for brainstorming or options, it normally belongs to dia-elenchus; if this skill was chosen anyway (for example by name), add one line to that same message:`

3. nit: SKILL.md:95 and brief-template.md:12. The "working thesis" may not exist.
   "Working thesis" is defined only in Step 1 (SKILL.md:43). On the recorded-as-is path (SKILL.md:39), or after a stop signal before the first steelman is confirmed, there is none, so "otherwise the working thesis" points at nothing.
   In SKILL.md:95 replace "(otherwise the working thesis)" with:
   `(otherwise the working thesis, or the user's own statement if none was formed)`
   In brief-template.md:12 replace "or the working thesis if none was asked" with:
   `or else the working thesis (the user's own statement if none was formed)`

4. nit: spec.md:66 (D21) leaves out two brainstorm behavior changes.
   The narrowed kind rule (scale no longer counts, SKILL.md:81) and the standalone pacing cue (SKILL.md:72) are not listed. Spec §5 (:109) says behavior is the reference "unless … D19–D21 say otherwise".
   After "and Hickey's own term", insert:
   `; a bigger or smaller version does not count as differing in kind, and the pacing cue may stand on its own line`

5. nit: probes.md:76 does not name the commit for the "After the fix" counts.
   probes.md:72 says the dia arm "was frozen at the commit named in each part". This part names none for its elenchus and brainstorm counts.
   Prepend `**After the fix, dia at <commit>:**`, using the commit actually run. If it was c0ccd3d, note that its skill files equal 395098a's.

6. nit (untested edge, no text change now): "use the Socratic method to poke holes in my plan" now routes to dia-elenchus, though it matches brainstorm's own "poke holes" trigger. The user would get aporia, not a stress test. This is probably the owner's intent (the P7 elenchus prompt «따져줘» is similar). Confirm it with the owner, or add a P7 cell.
