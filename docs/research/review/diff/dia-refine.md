Verdict: PASS WITH FIXES

Scope: `git diff cae2e4d 7115d2a -- skills/dia-refine` (SKILL.md: 6 hunks; agents/openai.yaml: 1 line), plus the dia-refine parts of docs/spec.md (D19, D20, §4, §5, §7.3, §12.2), README.md and tests/test_package.py. Line numbers are for SKILL.md at 7115d2a unless stated.

## Commands run (in the tree, read-only)

- `python3 tools/package.py --check`: "ok dia-refine" for all seven skills, exit 0.
- `python3 -m unittest discover -s tests`: "Ran 13 tests ... OK (skipped=1)", exit 0.
- Own checks: SKILL.md is 67 lines (limit 200). The description is 675 chars and unchanged. No Hangul in the skill. A grep for Claude|ChatGPT|Codex|GPT in skills/dia-refine/ found no matches. plugins/dia/skills/dia-refine/SKILL.md is byte-identical to the source.

## Hunk-by-hunk (check 1)

Applied as intended, in the review's corrected form:

- F14 / theme 1: openai.yaml:4 now reads `Use $dia:dia-refine to review the previous answer as a draft: `. This matches §7.3 and test_package.py:62.
- F2: SKILL.md:39 tags each ① item "(tool), (user's material) or (re-derived)". SKILL.md:52 adds the re-derived example. Arithmetic checked: 620 + 800 = 1,420 and 620 + 620 = 1,240. The severity was lowered as the review asked, and the review's F2 example was used.
- F1: SKILL.md:40 allows one closing line. It includes both review fixes: the "do this task the dia-refine way" exemption ("there is no original value to show"), and the S:65 out-of-scope line, merged in as "a problem outside the scope (see Safeguards)".
- F3: SKILL.md:31 says "the mark goes in ④, not inside the revision (in "final version only" mode, in the closing line)". As the review required, this was decided together with source placement (SKILL.md:43).
- F7: SKILL.md:44 uses the review's exact wording, "Apart from added requirements (②) and necessary corrections".
- M5: SKILL.md:37 adds the language fallback for a bare marker.
- F12 (probe contamination): correctly not applied. The GIL sentence from the P8 probe was not added to the example.

Every hunk is minimal. No hunk introduced a product name or an unconditional tool use, and the skill still completes with no tools.

## Fidelity and logic (checks 3, 4)

The diff adds or changes no method citations in dia-refine or in its parts of D19/D20, so there was nothing to fetch. The only logical content is the arithmetic example, and it is correct.

## Findings

1. should-fix: final-only mode has two different scopes for the unverified mark, at SKILL.md:31 and SKILL.md:40.
   - SKILL.md:31 sends the mark for every "Item[] you have no tool for, or could not check" to the closing line in final-only mode.
   - SKILL.md:40 lists only "a suspected error left as drafted and unverified".
   - An unsuspected unchecked item (the example's "Three benchmark figures", SKILL.md:58) goes to the closing line under :31 and has no place under :40.
   - SKILL.md:14 promises "leave the rest marked unverified", so narrowing :31 would break :14. Widen :40 instead.
   - SKILL.md:40 also drops the suspected correction that SKILL.md:32 requires for ④ ("goes under ④ with the correction you suspect"). The review's F1 text included it ("name it and the suspected correction").
   - Replacement for SKILL.md:40, from "a suspected error left as drafted and unverified" to the end of that clause: `what stayed unverified and bears on the user's conclusion (a suspected error with the correction you suspect, or a group such as "three benchmark figures unverified")`

2. should-fix: a file target in final-only mode loses its sources (SKILL.md:43).
   - SKILL.md:43 reads "for a file target, give it in the defect list instead".
   - In "final version only" mode, and in "do this task the dia-refine way" mode (SKILL.md:20, :40), there is no defect list. So for a file target in those modes, sources for verified changes have no location.
   - Replacement for SKILL.md:43, first sentence: `For verified items, give the source next to the sentence concerned in the revision; for a file target, give it in your reply instead (the defect list, or the closing line in "final version only" mode), never in the file.`

3. nit: the source rule is narrower than upstream (SKILL.md:43).
   - The diff says "next to the changed sentence". Upstream U:35 says 검증한 항목은 수정본의 해당 문장 가까이에 ("for verified items, near the sentence concerned in the revision"). That covers items verified and kept (③), not only changed ones.
   - Review M1 asked to restore the lost location ("in the revision"), not to restrict it to changed sentences. Under the new text, a tool-verified fact that was kept has no defined source location.
   - The replacement in finding 2 ("the sentence concerned") fixes this as well. If the narrowing was a deliberate owner choice, D20 already records it ("sources sit next to changed sentences"), and only this note applies.

4. nit: the tension the review named in M2 is only partly closed (SKILL.md:32, :42).
   - Review M2 said the basis tag "should cite S:42". SKILL.md:42 still says "Do not declare the revision better on your own judgment alone", while a re-derived change is filed under "① Confirmed errors" (SKILL.md:39, :52).
   - No text links the tag to that caution.
   - Append to SKILL.md:42: `The (re-derived) tag in ① is how the defect list shows this: the basis is your own working, not an outside check.`

5. nit: the language fallback covers only one invocation form (SKILL.md:37).
   - SKILL.md:37 says "if that message is only the `dia-refine` marker". SKILL.md:18 also counts `/dia:dia-refine`, `$dia:dia-refine`, `$dia-refine` and `@dia-refine`, which can arrive with no text.
   - Replacement: `; if that message has no text besides the invocation (the dia-refine marker or one of the names under Invocation), use the language of the conversation.`

6. nit: the basis tags omit one of the confirmed bases (SKILL.md:39 vs :32).
   - SKILL.md:32 names "the user's instructions or supplied material" as a basis. The tag set has only "(user's material)".
   - An error confirmed against the user's instruction has no exact tag.
   - Replacement for SKILL.md:39: `(tool), (user's instructions or material) or (re-derived)`

7. nit: spec D20 does not describe the whole diff (docs/spec.md:65).
   - D20 says only "added requirements may lengthen the revision". The diff also allows "necessary corrections" (SKILL.md:44).
   - D20 also omits two behavior changes: the file-target exception for sources (SKILL.md:43) and the M5 language fallback (SKILL.md:37).
   - D19 (spec.md:64) matches the diff.
   - Replacement for the D20 dia-refine clause: `dia-refine: unverified marks go in ④ (in "final version only" mode, in the closing line); sources sit next to the sentence in the revision, or in the reply for a file target; added requirements and necessary corrections may lengthen the revision; a message with only the marker is answered in the conversation's language.`

8. nit: spec §5.6 was not updated for theme 1 (docs/spec.md:172).
   - Theme 1 updated §4 (spec.md:89) and §5.7 but not §5.6. Its explicit-forms list still reads "`/dia:dia-refine`, `$dia-refine` and `@dia-refine` also work". It omits `$dia:dia-refine`, the only `$` form that resolves on the Codex plugin route (probes.md:32), and the one SKILL.md:18 and openai.yaml:4 now use.
   - Replacement: ``/dia:dia-refine`, `$dia:dia-refine`, `$dia-refine` (copied folder only) and `@dia-refine` also work.`

9. nit: handoff.md is stale after D20 (docs/handoff.md:27, :29–32).
   - Item 9 still says "High findings and cross-cutting themes 1–4 applied ... (spec D19)" and points to "`docs/research/README.md` § Not applied yet". That section is now "Applied, second batch" and "Still open".
   - The P8 note is still headed "Observations from P8 that were not acted on ... Re-test before changing anything". Observation (a), the inline "(unverified; …)" note, has now been acted on by F3 (SKILL.md:31) without a re-test.
   - Replacement for item 9's notes: `Applied 2026-10-20 in two batches (spec D19, D20), still as 0.1.0. What remains is in docs/research/README.md § Still open.`
   - Replacement for the first P8 bullet: `In one run, dia-refine added an inline "(unverified; …)" note inside the revision. Addressed by spec D20 (marks go in ④ or the closing line); re-run P8 from a neutral directory to confirm.`

10. nit: process note on versions (AGENTS.md:26 vs docs/handoff.md:7).
    - AGENTS.md:26 requires a new plugin `version` and a new `metadata.version` for any skill change. SKILL.md:7 is still `version: "1.0.0"` and the plugin is still 0.1.0.
    - This is allowed by the pre-release exception in handoff.md:7, and `--check` passes because plugin-release.json was regenerated. It is not a defect in the diff.
    - AGENTS.md:26 should mention the exception so the two files agree. Suggested append: ` Before the first install or release, a change may keep 0.1.0 (docs/handoff.md, State).`

## Intended items not applied (check 5)

For dia-refine, research/README.md lists F1 and F2 (D19), theme 1, and F3, F7 and M5 (D20). All are applied. The only gaps are partial ones: review M2's cross-reference to S:42 (finding 4), and the closing line's suspected correction (finding 1). F5, F6, F8–F13 and F15 are listed as still open, so their absence is correct.

## Spec consistency (check 6)

- D19 matches the diff.
- D20 understates the diff (finding 7).
- §4 (spec.md:89), §7.3 and the P3 pass condition in §12.2 are consistent with openai.yaml and the test. The P2 change does not affect dia-refine, which is implicit-allowed.
- §5.6 lags (finding 8).

## Contradiction sweep (check 2)

The whole SKILL.md was re-read after the change. The only rule conflicts found are findings 1, 2 and 4.

- Description (SKILL.md:3): agrees with the body.
- ①–④ example (SKILL.md:49–60): agrees with the tag rule, the ④ placement and SKILL.md:42. The re-derived line shows the original, the revision and the premise.
- Safeguards line SKILL.md:66 ("mention it in one line at the end"): now consistent with the final-only closing line.
