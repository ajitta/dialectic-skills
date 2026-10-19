Verdict: PASS WITH FIXES

Scope: `git diff cae2e4d 7115d2a -- skills/dia-intent` (SKILL.md: 4 hunks; agents/openai.yaml: 1 hunk), plus the dia-intent parts of docs/spec.md (D19, D20, §4, §5, §7.3, §12.2), README.md and tests/test_package.py. Line numbers below refer to the tree at 7115d2a.

Commands run in the tree (read-only):
- `python3 tools/package.py --check`: "ok" for all seven skills, exit 0.
- `python3 -m unittest discover -s tests`: "Ran 13 tests ... OK (skipped=1)", exit 0.
- Other checks: SKILL.md has 65 lines (64 newlines, no trailing newline). The description is unchanged at 271 characters. No Hangul under skills/dia-intent. No product names were added. plugins/dia/skills/dia-intent/SKILL.md is byte-identical to the source. The worktree is clean.

## Intended vs applied

docs/research/README.md:28-44 lists six dia-intent items. Each was checked against the review's corrected form:

| Item | Corrected form (review) | Applied at | Status |
|---|---|---|---|
| Theme 1, default_prompt | `$dia:dia-<x>` | agents/openai.yaml:4; spec §7.3; test_package.py:62 | Applied correctly |
| Theme 2 / F6, corrections | Review §1 F6 text, word for word | SKILL.md:42 | Applied word for word; see finding 2 |
| Theme 3 / F5, recall | Label "re-derived" for tool-less values; reserve "unverified" for recalled facts | SKILL.md:23 | Applied; consistent with dia-refine's "(re-derived: …)" tag at dia-refine/SKILL.md:52 |
| Item 7 / M2, P2 wording | Explicit-only skills are named in the prompt; check that dia-intent does not load without its name | spec §12.2 P2 (spec.md:406); handoff.md:20 | Applied |
| M1, private data and cost | Add "It must also not send the user's private material to outside services or incur cost." to l.18 | SKILL.md:18 | Applied word for word, but under-covers M1's own example; see finding 1 |
| F3, confirmation names what is sent or spent | Template change only; drop "other limited resources"; the l.24 triggers stay (the review moves the data gap to M1) | SKILL.md:65 | Applied in the corrected (narrower) form; wording nit in finding 4 |
| M3, reply language | Explicit reply-language rule | SKILL.md:53 | Applied; nit in finding 5 |

Nothing intended is missing. None of the findings the README lists as "Still open" (F1, F2, F4, F8–F11) leaked into the text.

Check 3 (fidelity): the dia-intent diff adds no method claims or citations, so there is nothing to verify.

Check 6 (spec): D19 says "values worked out without a tool are labelled re-derived; a correction that conflicts with inspected evidence is named once". That matches SKILL.md:23 and :42. D20's "the confirmation names what is sent or spent, an explicit reply language" matches :65 and :53. D20's "no private data out or cost before approval" is broader than the text, which binds only probes (finding 1). The §4 row (spec.md:84) already listed `$dia:dia-intent`.

## Findings

1. should-fix. SKILL.md:18: the M1 rule binds only probes, but M1's main case is a read or search.
   - The new sentence "It must also not send the user's private material to outside services or incur cost." follows "Running the user's code ... counts as a probe" and "It must leave the user's originals ...". Its subject "It" is therefore the safe isolated probe.
   - The review's M1 names "a web search or fetch built from confidential material" as the first case (review/dia-intent.md:121). A model doing a pre-approval web search classes it as a read, not a probe, so the rule does not reach it.
   - Spec D20 (spec.md:65) states the wider rule ("no private data out or cost before approval"), so the spec and the skill disagree.
   - "incur cost" can also be over-read as any compute or time cost, which would block ordinary local probes. The Model Spec item behind M1 is "Direct expenditures".
   - Replace with: "No read, search or probe may send the user's private material to outside services or incur charges."
   - The sentence stays in the same paragraph, so SKILL.md:40 ("the rules for isolated probes still apply" after an "investigate only" approval) still carries it.

2. should-fix. SKILL.md:42 vs :39: no place to name the evidence when a correction comes with "proceed".
   - :39 says corrections plus a proceed instruction are "approval of the revised task. Apply the corrections without requesting the same approval again."
   - The new :42 says "name that evidence once in the revised review".
   - With correction plus proceed, which is the common case, no revised review exists. The model either drops the conflict notice or writes a revised review and stalls, against :39. Only the "corrections alone" path (:41) has a revised review.
   - Replace :42 with: "* If a correction conflicts with evidence you inspected, name that evidence once: in the revised review, or before acting when the correction came with an instruction to proceed. Follow the correction for preferences, scope and authority."
   - Note: the review's text, kept as is, still says nothing about factual corrections that conflict with evidence. That is acceptable under the review's corrected form, which deliberately limits deference to preferences, scope and authority; not a defect of the diff.

3. nit. SKILL.md:23 vs :59: the template does not name the new label.
   - :23 now uses four labels: inspected fact, inference, unverified assumption, and the new "re-derived".
   - The Evidence template at :59 lists "Decisive findings, supported inferences, material assumptions, …", so the re-derived label has no slot. The rules and the template do not contradict, but the template no longer reflects the rule.
   - Replace :59 with: "[Decisive findings (marked re-derived where worked out without a tool), supported inferences, material assumptions, settled points with their source, and the options you will use for delegated choices.]"

4. nit. SKILL.md:65: wording of the F3 template change.
   - "including what will be sent or spent and to whom" attaches "to whom" to "spent" as well.
   - Unlike the following "any requested step", it has no "any", so a model may add a "nothing will be sent or spent" line. That works against :28 ("Include only material items").
   - Replace that clause with: "including anything that will be sent or spent and its recipient, any requested step that cannot be undone and the safeguard the user can ask for; …" (rest unchanged).

5. nit. SKILL.md:53: the reply-language rule is narrower than in the sibling skills and has a prefix edge case.
   - It covers only "the review". The brief proceed request (:51) and the re-agreement questions (:47) are not reviews, so they are not covered.
   - On Codex and ChatGPT the English `default_prompt` (openai.yaml:4, "Use $dia:dia-intent to confirm …") is prepended to the user's own text. A Korean task then arrives in a mixed-language "latest message". dia-refine/SKILL.md:37 handles the equivalent marker case explicitly.
   - Replace :53 with: "Write the review and any questions in the language of the user's latest message, ignoring an invocation prefix such as the skill name or a prefilled prompt, and translate the labels consistently."

6. nit. docs/spec.md:119: §5.1 contradicts D19 and D20.
   - It still says "Behavior: unchanged from the reference." The §5 intro was changed to "unless this section, D19 or D20 says otherwise" (spec.md:108), but §5.1 itself states the opposite of D19 and D20 for this skill.
   - Replace with: "- Behavior: unchanged from the reference, except as amended by D19 and D20."

7. nit. docs/spec.md:208: L6 is still not true for the reference skills.
   - L6 still reads "Replies follow the user's language, as all reference skills already require." The review's M3 (review/dia-intent.md:132) noted this is untrue for confirm-intent. The diff fixed the skill but not the spec claim.
   - Replace with: "- L6. Replies follow the user's language; every skill states this (dia-intent since D20)."

8. nit (process; outside the dia-intent hunks, not a test failure).
   - Skill files changed under an unchanged plugin `version` 0.1.0. plugin-release.json was re-digested under the same version, so the §12.1 version rule passes by construction.
   - AGENTS.md says "Changing any skill file requires a new plugin `version` … and the skill's `metadata.version`". dia-intent's metadata.version stays "1.0.0" (SKILL.md:7).
   - This is defensible under O5 (0.1.0 until acceptance) and handoff item 7, but it should be stated. Any existing 0.1.0 install will not pick up these changes.
   - Also stale: docs/handoff.md:27 points to "`docs/research/README.md` § Not applied yet", a section renamed to "Still open". Replace that phrase with "§ Still open".

Checks with no defect found:
- No contradictions with the hold rules (:30–:34).
- The new "a fact you only remember is an unverified assumption" sits inside the "facts you will repeat or act on" sentence, so it does not widen labelling to every remembered fact.
- The F3 change correctly leaves the l.24 materiality triggers alone, as the review asked.
- The P2 amendment matches the review's M2.
