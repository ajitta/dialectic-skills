Verdict: PASS WITH FIXES

Scope: `git diff d135f8e 75d7ac1 -- skills/dia-intent` (one file, SKILL.md, 5 edits) and the dia-intent parts of `docs/spec.md` (D24 row, §5 and §5.1). The skill text passes: nothing load-bearing was lost and nothing contradicts. The two fixes are in the record, not in the skill.

## What was checked, with evidence

Recommended set against the applied diff (check 5). Each of the five edits matches the audit's §4 recommended set exactly. Nothing else changed.
- R1: "Facts you can investigate and choices already delegated are not reasons to propose this." is removed (old SKILL.md:37, new :37).
- R2: "; if they do, it belongs in evidence and assumptions." is removed (old :31, new :31).
- R3a: the Goal bracket "[Intended outcome, scope, and completion criteria.]" is removed (old :70).
- R3b: the Decisions bracket "[Only what remains open, with its effect. Omit if nothing remains.]" is removed (old :76).
- R3c: the Evidence bracket now reads "[As item 2; mark values worked out without a tool as re-derived.]" (new :72), which is the audit's text word for word.
- O1, O2, O3 and the move of the dependent-decisions block were not applied. `agents/openai.yaml` and the frontmatter are unchanged, and `plugins/dia/skills/dia-intent/SKILL.md` is byte-identical to the source.

Behavior loss (check 1). Each removed unit is restated elsewhere in the file.
- R2: item 2 (:29) still says "Points the request, conversation, or materials settle, and choices delegated to you, belong here with their source or the option you will use, not in questions." The example in the item-3 bullet, "(a request to send settles sending without a preview)" (:31), is kept.
- R1: the trigger at :35 fires only for "open decisions". Investigable facts are excluded at :31 ("Investigate available factual questions instead of asking them") and at :24. Delegated choices are excluded at :29 and :31. I tested one open decision with a delegated choice that depends on it: :38 ("delegating the dependent choices … may resolve the dependency instead") and :39 ("settled or delegated") still close it, and one open decision cannot need "more than one round". One caveat: this sentence came from upstream (`upstream/installed/confirm-intent/SKILL.md:20`), so dropping it departs from the reference text. D24's general clause, "restated rules … were cut", covers that.
- R3a: item 1 (:28) has the same label and a fuller version of the bracket's content.
- R3b: "with its effect" is still at :30 ("explain each one's effect"). "Omit if nothing remains" is still covered by :30 ("An empty decision list is normal; do not add items to fill it", the D23 anti-padding rule), by :42 and by :65. The research named the template cue as one of two guards against manufactured decisions (`docs/research/dia-intent.md:157`). The D23 sentence at :30 now does that job, so this is not a loss.
- R3c: the old bracket contained "Decisive findings (marked re-derived …), supported inferences, material assumptions, settled points with their source, and the options you will use for delegated choices". Every part of it is in item 2 (:29). The D19 "re-derived" slot, added after `review/diff/dia-intent.md` finding 3, survives in the shortened bracket.

D19–D23 survival. All of these are still present:
- D19: re-derived (:29, :72); "unverified assumption" (:29).
- D20: sent/spent and recipient (:76).
- D21: no data out on reads and searches (:21); the language rule ignores an invocation prefix (:67).
- D23: short exact constraints are quoted and still checked (:16); an empty decision list is not padded (:30); an analysis deliverable shows only what decides scope (:44); the limit for open-ended work (:76); the follow-up rule (:61).
- The `short_description` is unchanged.

Contradictions and dangling references (check 2). I read the whole file afterwards. "item 2" at :72 resolves to the only numbered list (:28–:33) and matches the existing "as item 2 says" at :16. The template labels match the bold labels in items 1–3. No section was renumbered or removed. The template now has bare labels for Goal and Decisions and a bracket for Evidence and Confirmation. That is uneven, but nothing in it conflicts.

Moved text and fidelity (checks 3–4). Nothing was moved, and the skill still has no `references/` (spec §5.1 is unchanged: "References: none at present"). It has no citations, so nothing to re-fetch.

Repo rules. SKILL.md is 76 lines (limit 200). A grep for Hangul in the file found nothing. Line endings are LF. Tool use is still conditional (:24). The text is still assistant-neutral. Versions stay at 0.1.0 and 1.0.0, which AGENTS.md allows before the first release.

Token claim. I measured this myself with tiktoken cl100k_base in a scratch venv. dia-intent's body went from 1,782 to 1,708 tokens (−74) and the whole file from 1,896 to 1,822. The implementer's account (`tokfix/dia-intent-applied.md:24-25`) is correct. Across all seven bodies the drop is 16,866 → 15,887 (−979), which fits D24's "about 1,000".

Runs (check 6), in the tree:
- `python3 tools/package.py --check`: "ok" for all 7 skills, exit 0.
- `python3 -m unittest discover -s tests`: 13 tests, OK, exit 0. One test was skipped: `test_frontmatter_and_openai_yaml_parse`, "PyYAML not installed". So YAML parsing of the frontmatter was not exercised in this environment. The frontmatter did not change in this diff.


## Findings

1. should-fix — docs/spec.md:69 (D24). The row does not record the dia-intent change, and its general claim is wrong for this skill. It says "worked examples, templates and no-reference fallbacks were kept", but dia-intent's response template lost two brackets and had a third shortened. Spec §5 (:113) says every skill keeps its reference behavior "unless this section or D19–D24 say otherwise". The upstream template brackets (`upstream/installed/confirm-intent/SKILL.md`, Response Format) now differ, and nothing in the record explains why. The audit asked for exactly this note (`token-audit/dia-intent.md:95`: "a D-row noting 'template brackets reduced to non-redundant cues; no rule change' keeps spec §5.1 accurate"). The applied account deferred it (`tokfix/dia-intent-applied.md:39`), and D24 does not include it.
   Replace "worked examples, templates and no-reference fallbacks were kept." with:
   "worked examples, template fields and no-reference fallbacks were kept."
   After "dia-refine's natural-language triggers live in the description only." insert:
   "dia-intent's response template keeps its four section labels, the re-derived cue and the Confirmation contents; bracket text that restated items 1–3 is cut, and two sentences restating where settled points go and what may trigger the dependent-decisions path are cut (no rule change)."

2. should-fix — docs/research/README.md, § Still open (the last lines of the file). Nothing records that the cuts still need probe verification. The audit's "Verification after applying" (`token-audit/dia-intent.md:97-100`) asks for three things:
   - re-run the Part A dia-intent cells;
   - add a cell with a delegated choice and a date or total, for R3c;
   - add a dependent-decisions cell, for R1.

   Decision rule 13 says "Validate each class removal with the probes before shipping … High" (`evidence.md:95`). The applied account calls this out of scope (`tokfix/dia-intent-applied.md:39`), and neither the README's Still open list nor `docs/handoff.md` picks it up. As a result, the existing intent behavior run, made before D24, now looks like it covers the shipped text. I could not run it myself because I was told not to use the claude or codex CLIs. I expect it to pass, since every cut is a restatement.
   Append to § Still open:
   "3. D24 (token audit) is not yet probed. dia-intent: re-run the probes Part A cells (rename, churn report, irreversible delete; n=3) and add one cell with a delegated choice plus a date or total (expects \"re-derived\" and the option used, R3c) and one with dependent decisions (R1). The other skills' audit files list their own post-apply checks."

3. nit — skills/dia-intent/SKILL.md:69-75. The template is uneven: Goal and Decisions are bare labels, while Evidence has "[As item 2; …]" (also noted at `dia-intent-applied.md:38`). It contradicts nothing. No change recommended; listed so the next reviewer does not raise it again.

No blockers. No D19–D23 label or fix is missing or weaker.
