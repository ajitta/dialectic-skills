Verdict: PASS WITH FIXES

Scope: second pass on dia-intent at 395098a against my first-pass report (docs/research/review/diff/dia-intent.md, written at 7115d2a). Diff read: `git diff 7115d2a 395098a -- skills/dia-intent docs/spec.md docs/probes.md README.md AGENTS.md docs/handoff.md`. I also re-read the whole of skills/dia-intent/SKILL.md (64 lines) and agents/openai.yaml. dia-intent has no references/ directory. Line numbers below refer to 395098a.

Commands run in the tree (read-only):
- `python3 tools/package.py --check`: "ok" for all seven skills, exit 0.
- `python3 -m unittest discover -s tests`: "Ran 13 tests ... OK (skipped=1)", exit 0.
- SKILL.md: 64 lines (limit 200). Description: 271 characters, unchanged. No Hangul. No product names (grep for claude/codex/chatgpt/openai/gpt/anthropic/gemini/copilot found nothing). plugins/dia/skills/dia-intent/ and the zip copy are byte-identical to the source. The worktree is clean.

## Per-finding status

| # | Finding (first pass) | Status | Evidence |
|---|---|---|---|
| 1 | M1 rule bound only probes | Fixed | SKILL.md:18 now reads "No read, search or probe may send the user's private material to outside services or incur charges.", word for word as proposed. "incur charges" replaces "incur cost". It is still in the same paragraph, so :40 ("the rules for isolated probes still apply") carries it. It now matches D20 (spec.md:65) and D21 (spec.md:66). See new finding 2 for a pronoun side effect. |
| 2 | No place to name evidence on correction + proceed | Fixed | SKILL.md:42 is the proposed text, word for word. It does not conflict with :39: you name the evidence and then act, and no new approval is requested. |
| 3 | Template lacked the re-derived label | Fixed | SKILL.md:59 is the proposed text, word for word. |
| 4 | Confirmation clause wording | Fixed | SKILL.md:65 now says "anything that will be sent or spent and its recipient". |
| 5 | Reply-language rule too narrow; prefix edge case | Fixed | SKILL.md:53 is the proposed text, word for word. It fits openai.yaml:4, whose `default_prompt` is an English prefix. It is consistent with dia-refine/SKILL.md:37. |
| 6 | spec §5.1 "unchanged from the reference" | Fixed (different wording, acceptable) | spec.md:120 now reads "Behavior: the reference, amended by D19–D21." The §5 intro (spec.md:109) and §5.2/§5.3 (:127, :135) were aligned the same way. |
| 7 | L6 untrue for the reference skills | Fixed | spec.md:209 now says "every skill states this (dia-intent since D20)". Grep confirms each of the seven SKILL.md files states a reply-language rule: brainstorm:26, elenchus:41, intent:53, iterate:56, negative:41, reductio:40, refine:37. |
| 8 | Version unchanged; stale handoff pointer | Pointer fixed; version deliberately left (acceptable) | handoff.md:27 now points to "§ Still open", which exists at research/README.md:50. AGENTS.md:26 adds the pre-release exception, and handoff.md:7 states it ("While that holds, a skill change may keep 0.1.0"). Plugin version 0.1.0 is the same in plugin-manifest.json, plugin-release.json and plugins/dia/.claude-plugin/plugin.json. metadata.version stays "1.0.0" (SKILL.md:7). Handoff item 7 bumps it at release, so leaving it is consistent with the documented rule. |

## Spec D21 and probes.md claims

- D21 (spec.md:66) on dia-intent: "no-data-out rule covers reads and searches, and its language rule ignores an invocation prefix". Both hold (SKILL.md:18, :53). D21 does not mention the :42, :59 and :65 edits. Those clarify D19/D20 behavior that is already stated, so the omission is acceptable.
- dia-intent is not one of the two routing descriptions that changed. Neither the new dia-elenchus description (970 characters) nor the new dia-brainstorm description (873 characters) mentions dia-intent or overlaps its trigger. Its trigger is explicit-only (openai.yaml:7, and the description's "Use only when explicitly selected or invoked"), so the P7 change cannot pull requests into it.
- probes.md:82: the dia-intent behavior run is recorded as "dia at `7115d2a`", which is before the D21 edits to SKILL.md:18, :42, :53, :59 and :65. The entry is honestly dated, but it is not evidence for the current text. I could not re-run it (the claude CLI is not allowed here), so its contents are unverified by me. The heading over it overstates the coverage; see new finding 1.
- The Fisher figure at probes.md:76 (6/6 vs 1/6, two-sided) recomputes to 14/924 ≈ 0.0152. Correct.

## New findings

1. should-fix. docs/probes.md:23, :25, :70: "after D21" mislabels runs made before D21.
   - The P6, P8 and dia-intent runs are all stated as "dia at `7115d2a`" (probes.md:78, :80, :82).
   - D21 is commit a506214, which comes after 7115d2a (git log: 7115d2a → a506214 → c0ccd3d → 395098a). D21 changed dia-refine, dia-iterate and dia-intent text that these probes exercise.
   - Replace in :23 and :25 "re-run from a neutral directory after D21: pass" with "re-run from a neutral directory at 7115d2a (before D21): pass".
   - Replace the :70 heading with "### Neutral-directory re-run after spec D19–D20, with the routing fix after D21 (2026-10-20)".

2. nit. SKILL.md:18: the inserted sentence breaks the pronoun chain.
   - "Its result is evidence for the review …" and "Remove or report what it created." used to follow sentences whose subject was the probe. They now follow "No read, search or probe may …", so "it" is ambiguous, and a read creates nothing.
   - Replace "Its result is evidence for the review, not a draft deliverable: report what it showed, not the change it used. Remove or report what it created." with "A probe's result is evidence for the review, not a draft deliverable: report what it showed, not the change it used. Remove or report what the probe created."

3. nit. docs/probes.md:68 is now stale.
   - "The other P6–P8 cells have not been re-run from a neutral directory yet." is contradicted by the section that follows it.
   - Replace with: "The other P6–P8 cells were re-run from a neutral directory below."

No regressions found in dia-intent itself. The approval rules (:38–:43), the hold rules (:47) and the review template (:55–:65) are mutually consistent. The tool use is still conditional ("if a decisive read or probe is available and permitted", :18), and the skill still works with no tools: re-derived values are labelled at :23 and :59.
