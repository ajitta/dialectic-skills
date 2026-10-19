Verdict: PASS WITH FIXES

Scope: second pass on dia-refine at 395098a against my first-pass report (docs/research/review/diff/dia-refine.md, at 7115d2a). The only dia-refine change is in a506214 (spec D21): SKILL.md lines 37, 39, 40, 42 and 43. Line numbers are for 395098a.

Commands run in the tree:
- `python3 tools/package.py --check`: "ok" for all seven skills, exit 0.
- `python3 -m unittest discover -s tests`: "Ran 13 tests ... OK (skipped=1)", exit 0.
- Own checks, all pass: 67 lines; description 675 chars, unchanged; no Hangul; no product names; tool use conditional and the skill works with no tools (:14, :31); the plugins/dia/ and zip copies are byte-identical to the source.
- Routing: dia-refine's description did not change. The new dia-elenchus and dia-brainstorm descriptions use none of its triggers (review, draft, fix, refine).

## Pass-1 findings

| # | Status | Evidence |
|---|---|---|
| 1 closing-line scope | fixed | SKILL.md:40 now uses the replacement text word for word. A residual tension with :31 is new finding 3. |
| 2 file-target sources in final-only mode | partly | SKILL.md:43 sends them to "the closing line in "final version only" mode", but the list at :40 of what that line names does not include sources (new finding 2). |
| 3 "changed" vs "concerned" sentence | fixed | SKILL.md:43 now reads "next to the sentence concerned". |
| 4 (re-derived) tag linked to the caution | fixed | SKILL.md:42, last sentence. |
| 5 language fallback | fixed | SKILL.md:37 now covers "one of the names under Invocation", which matches :18. |
| 6 tag set | fixed | SKILL.md:39: "(user's instructions or material)". |
| 7 spec D20 | partly | D21 (spec.md:66) records the closing line and file-target sources. D20 (spec.md:65) still says "sources sit next to changed sentences", which contradicts SKILL.md:43. No D row records the "necessary corrections" lengthening, the tag set or the language fallback (new finding 4). |
| 8 spec §5.6 forms | fixed | spec.md:173 now lists `$dia:dia-refine` and `$dia-refine` (copied folder only). |
| 9 handoff stale | partly | Item 9 (handoff.md:27) is fixed, and the bullet at :31 is updated. The heading at :29 still says "not acted on", and :32 contradicts probes.md:80 (new finding 5). |
| 10 version exception | fixed | AGENTS.md:26 appends the pre-release exception. |

## Probe claims vs the files

The transcripts in /home/ubuntu/work/dia-review/probes-7115d2a/out/ (p6-refine-first, p8-refine-1 to -3) show what probes.md:78 and :80 describe. But they ran the 7115d2a text, and probes-a506214/out/ holds only P7 files. So the D21 text has never been probed, and the "final version only" mode never at all (finding 1).

## New findings

1. should-fix: docs/probes.md:23 and :25 overstate when the probes ran.
   - Both rows say "re-run from a neutral directory after D21: pass". The runs were "dia at `7115d2a`" (probes.md:78, :80), which is before D21 (a506214). D21 changed SKILL.md:37, :40, :42 and :43.
   - The heading at probes.md:70 ("after spec D19–D21") has the same problem for P6 and P8.
   - Replacement for the result cell at :23: `pass; re-run from a neutral directory at 7115d2a (D20 text, before D21): pass`
   - Replacement for the result cell at :25: `pass after a fix to dia-refine; re-run from a neutral directory at 7115d2a (D20 text, before D21, default mode only): pass`

2. should-fix: the closing-line list at SKILL.md:40 leaves out the sources that SKILL.md:43 sends to that line.
   - :40 lists what the one closing line names and says it is used "only if needed". :43 says that for a file target, sources go in "the closing line in "final version only" mode".
   - D21 (spec.md:66) says the closing line "covers ... file-target sources", but :40 does not.
   - Replacement for SKILL.md:40, from "or a problem outside the scope (see Safeguards)." to the end of that clause: `a problem outside the scope (see Safeguards), or, for a file target, the sources of verified items (see below).`

3. nit: in final-only mode, SKILL.md:31 and :40 now scope the unverified mark differently.
   - :31 sends the mark for every unchecked item to the closing line.
   - :40 (my own pass-1 wording) names only what "bears on the user's conclusion". So an incidental unverified item gets no mark at all, against :14 ("leave the rest marked unverified").
   - The filtering in :40 is reasonable. Align :31 with it. Replacement for the parenthesis in :31: `(in "final version only" mode, in the closing line when it bears on the user's conclusion)`

4. nit: spec D20 is stale and D21 is incomplete for dia-refine (spec.md:65–66).
   - Replace D20's dia-refine clause with: `dia-refine: unverified marks go in ④, sources sit next to the sentence concerned in the revision, added requirements and necessary corrections may lengthen the revision.`
   - Append to D21's dia-refine clause: `; the ① basis tags include the user's instructions, the (re-derived) tag is tied to the no-self-judgment rule, and the language fallback covers every invocation name`

5. nit: docs/handoff.md:29 and :32 contradict the probe record.
   - The heading at :29, "not acted on ... Re-test before changing anything", sits over a bullet (:31) that says the observation was addressed.
   - :32 still blames the host's Korean locale, although probes.md:80 says the Korean reply did not reproduce outside the repository.
   - Replacement for :29: `Observations from P8 (n=1 each; see docs/probes.md):`
   - Replacement for :32: `- In one run, dia-refine replied in Korean to an English prompt. It did not reproduce from a neutral directory (3/3 English), so the repository's AGENTS.md ("reply in Korean") was the likely cause.`

6. nit: docs/probes.md:68 is stale.
   - It says "The other P6–P8 cells have not been re-run from a neutral directory yet", directly above the section that re-runs them.
   - Replacement: `No drop. P6–P8 were re-run from a neutral directory below.`

7. nit: probes.md:80 says dia-refine "tagged the arithmetic (re-derived)".
   - In all three transcripts, ① was empty and the arithmetic sat under ③ with a re-derivation. So P8 did not exercise the ① basis-tag rule (SKILL.md:39).
   - Replacement: `re-derived the arithmetic and kept it under ③ (① was empty, so the basis tags were not exercised)`

No blockers. The SKILL.md body has no other new contradictions. The example (:49–60) still matches the tag set, the ④ placement and :42. The Safeguards line :66 matches the closing line at :40.
