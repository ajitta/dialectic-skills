Verdict: PASS WITH FIXES

Scope: dia-elenchus at 395098a, checked against my first pass on 7115d2a. Line numbers refer to 395098a.

## Checks run

- `python3 tools/package.py --check`: exit 0, all seven "ok". The generated copy of dia-elenchus is identical to the source (`diff -r` against plugins/dia/skills/dia-elenchus).
- `python3 -m unittest discover -s tests`: 13 tests OK, 1 skipped (no PyYAML). With `PYTHONPATH=$TMPDIR/pyyaml`: 13 OK, 0 skipped.
- SKILL.md is 113 lines. The description is 970 chars, under the 1024 limit with 54 to spare (dia-brainstorm's is 873). No Hangul, and no product names outside agents/openai.yaml. Tool use is conditional (l.100).
- `grep "and how?"` over skills/, plugins/, spec and README: no hits.
- The Fisher p at probes.md:76 recomputes as 0.0152, which matches. The run counts were not re-run, because the CLIs are off-limits for this review.

## Per-finding status

| # | Status | Evidence |
|---|---|---|
| 1 one ask | fixed | SKILL.md:84, :92 and patterns:31 carry my replacement text verbatim. The follow-up step keeps Rule 1 (l.35). |
| 2 stable numbering | fixed, with a residue (new 2) | SKILL.md:76 and patterns:23 match my replacement verbatim. |
| 3 "brainstorm's output" | fixed | patterns:51 now points to "Ideas born", which matches record-template.md:20. |
| 4 P2 wording | fixed | spec.md:407 and handoff.md:20 agree with each other. |
| 5 Protagoras 333c | fixed | SKILL.md:31 matches my replacement. |
| 6 description label | fixed | SKILL.md:3 has "(this skill's addition)". |
| 7 label criteria | partly | The tie-breakers are at SKILL.md:100. record-template.md:38-41, which the skill reads at that step, lacks them (new 3). |
| 8 D19 | fixed | spec.md:64 now has the "narrower than Socrates' practice" label. |

## Spec and probes claims

- D21 (spec.md:66), dia-elenchus clauses (one ask, stable numbers, the description label): all hold at SKILL.md:3, :76, :84, :92 and patterns:23, :31.
- D21 routing sentence: it holds as worded. New finding 1 covers a precedence gap it leaves.
- probes.md:76 describes the committed text accurately. Between c0ccd3d and 395098a only probes.md changed, so the tested descriptions are the shipped ones.
- probes.md:74, "same descriptions apart from the names": I confirmed this against upstream by script. It is true at 7115d2a and false at a506214 (new 4).

## New findings

1. should-fix: brainstorm SKILL.md:3 against elenchus SKILL.md:3 (and spec.md:66). The two descriptions send one request in opposite directions.
   - The request: "Use the Socratic method to help me get to a plan for my app."
   - dia-elenchus says: "For questioning that ends in options and a plan … use dia-brainstorm."
   - dia-brainstorm says: "Socratic method without asking to brainstorm, use dia-elenchus."
   - dia-brainstorm's own body (l.37) already uses the wider exception, "brainstorming or options".
   - Replacement in the brainstorm description: `or when the user asks for Socratic dialogue or the Socratic method without asking to brainstorm or for options and a plan, use dia-elenchus instead.` That brings it to about 900 chars.
   - spec.md:66: replace `unless the user asks to brainstorm` with `unless the user asks to brainstorm or for options and a plan`.
   - Then re-run the P7 elenchus and brainstorm cells (L7) and add a cell for this case.

2. nit: SKILL.md:76 and patterns:23 and :31. The rules do not say what ① is or how later premises are numbered.
   - ① is always the current definition (SKILL.md:82), so every revision reuses ①.
   - The shape "① and ② (or ①–③)" hard-codes ② and ③. A second contradiction with stable numbers would use ④ and up, so copying the shape invites renumbering.
   - Append to patterns:23: `① is always the current definition. Agreed premises start at ② and continue across contradictions (a later one may be ① + ④ + ⑤).`
   - Replace patterns:31 with: `So ① and the premises above can't all stand together. Which would you change?`

3. nit: record-template.md:38-41 lacks the tie-breakers. After l.41, add:
   - `- If no definition was ever given, use stopped before testing.`
   - `- If aporia and another label both fit, use aporia.`

4. nit: probes.md:74 and :76 misstate what was tested.
   - The "same descriptions" sentence follows the a506214 run, but at a506214 the elenchus description already carried "(this skill's addition)". Replace it with `At 7115d2a the descriptions are the same apart from the skill names (a506214 adds only the "this skill's addition" clause)`.
   - The results after the fix name no commit, although l.72 says each part does. Write `After the fix (dia at c0ccd3d)`.

5. nit: AGENTS.md:26 and handoff.md:7 say a change "may keep 0.1.0".
   - Every skill's metadata.version is "1.0.0" (SKILL.md:7). Only plugin-manifest.json:4 is 0.1.0. This is repo-wide, not a dia-elenchus defect.
   - Replacement: `Before the first install or release, a change may keep the plugin at 0.1.0 and each skill's metadata.version at 1.0.0 (docs/handoff.md, State).`

No blockers. Apart from finding 1, the routing change introduces no new contradiction in the body. elenchus Step 1 (l.53) still tells a general "Socratic" request that this is the strict method and points to dia-brainstorm, which fits the new description.
