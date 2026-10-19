Verdict: PASS WITH FIXES

Independent diff review of 75d7ac1 against d135f8e, dia-iterate only (skills/dia-iterate/SKILL.md, skills/dia-iterate/references/verification-sources.md, docs/spec.md D24 and §5 headers). Line numbers are in 75d7ac1 unless prefixed "old:" (= `git show d135f8e:<path>`).

## Summary

The diff contains exactly the audit's recommended set (S1-S11, R1-R4), in the audit's exact wording, and nothing else. I found no lost rule, stop condition, D19-D23 label, fallback or template field. One example class (anecdotes about famous people) dropped out of the skill completely. The audit assumed the Guardrails bullet still covered it, but that bullet never listed it. Two small wording losses are nits. Builds, tests and token counts reproduce.

## Findings

1. should-fix, skills/dia-iterate/SKILL.md:89 (the loss comes from S4 at :21).
   Problem: old:SKILL.md:23 was the only place that listed anecdotes as a set-text class: "for widely copied set texts (fables, proverbs, anecdotes about famous people) that draft will overlap existing documents closely and can trip the host's content filter." The class came from upstream (upstream/installed/recursive-refine/SKILL.md:17). The audit justified S4 with "The set-text half repeats :91, which already covers set texts in every output" (token-audit/dia-iterate.md:43). That is only partly true. :91 (now :89) reads "Widely copied set texts (fables, proverbs, full standard licenses)", which has no anecdotes. So the class is now gone from the skill, even though the skill's own example topic, "the sword of Damocles" (:21), is that kind of anecdote. Step 4's set-text quotation rule (:32, D23) and the restate rule (:89) are now narrower for it than before. The implementer noticed this ("Gaps noticed", tokfix/dia-iterate-applied.md:42) but left it unfixed.
   Replacement for :89 (about +5 tokens; it restores the coverage the audit already assumed, so it does not reopen S4):
   `- Widely copied set texts (fables, proverbs, anecdotes about famous people, full standard licenses) have been reported to block even when reworded. Do not restate such passages; point to their location only.`

2. nit, skills/dia-iterate/SKILL.md:31 (S5).
   Problem: old:SKILL.md:33 said "Long verbatim overlap with an existing document can trigger the host's content filter". The audit kept S5 because the reason "lets the model extend the no-copy rule to sources the step does not list" (audit :44). The shortened sentence drops the object ("with an existing document"), and that object is the generalising cue. As written, "Long verbatim overlap" no longer says what the overlap is with.
   Replacement: `Long verbatim overlap with existing text can trip the host's content filter and lose the round's work.`

3. nit, skills/dia-iterate/SKILL.md:14 (S1, fidelity).
   Problem: the Huang gloss changed from "revising repeatedly on self-judgment alone brings no gain..." (old:14) to "repeated self-judgment brings no gain on reasoning tasks and often makes them worse". Huang et al. test intrinsic self-correction, i.e. revising "without external feedback" (abstract). The new gloss drops "revising" and "alone", so it now sounds like judging alone, not revising on that judgment, does the damage. The parenthetical now also sits on "a loop that feeds on its own judgment amplifies its own errors", a claim the earlier diff review called uncited and only "consistent with" Huang (review/diff/dia-iterate.md:75). The gloss after the colon states what Huang actually found, so this is acceptable, but tighter wording costs 2 tokens.
   Citation checked: arXiv:2310.01798 is Huang et al., "Large Language Models Cannot Self-Correct Reasoning Yet", ICLR 2024 (abs page fetched). "often" is backed by §1 of the v2 PDF: "In most instances, the performance after self-correction even deteriorates" (fetched). arXiv:2305.11738 is Gou et al., CRITIC, ICLR 2024 (fetched). "loosely" remains honest: CRITIC revises after tool feedback and has no confirm-only/lock step.
   Replacement for the parenthetical: `(Huang et al., ICLR 2024, arXiv:2310.01798: revising on self-judgment alone brings no gain on reasoning tasks and often makes them worse)`

4. should-fix before release (process, no text change), docs/research/review/tokfix/dia-iterate-applied.md:43.
   Problem: the audit's re-check (P6 `dia-iterate --max 2` + draft, and P8 tool-less, n>=2, audit :102) and evidence.md rule 13 ("Validate each class removal with the probes before shipping") were not run. The behaviour-relevant merges, S2 (default cap now only inside the invocation bullet, :18) and S7 (rule 2 "Say so and stop.", :45), are textually equivalent to the old text, but no probe has exercised them.
   Fix: run P6 and P8 against 75d7ac1 before the 0.x pre-release and record the results in docs/probes.md.

## Check results

Check 1, behaviour loss (each unit compared with old text):
- S1: D19 labels (re-derivation does not count, CRITIC "loosely", not Self-Refine, Huang "often") and D23's lower-bound sentence (verbatim) are kept. Old "not 'reread and rewrite'" is covered by :30 and :83, and "When verification methods run out, the loop ends" by stop 3 (:46). "Quality of the signal caps improvement" was a reason with no rule attached.
- S2: "default 3" is still stated once (:18) and matches spec §5.7. The target list is still at :25.
- S3, S6, S9, S10: pure rationale. The rules they supported (:20, :33, :77, :87) are intact.
- S4: the refusal to draft is kept, with a reason (:21). The lost anecdote class is finding 1.
- S7: old "If round 1 names no defects, or refutes all of them, say so and end" is fully covered by rule 2 "Say so and stop." (:45), which applies in any round. The D19/F3 sentence is kept (:50).
- S8: the change-list default and the full-text-on-request rule are intact (:54, :76). Dropping "The change list carries the same information without that risk" removes no rule.
- S11: the abandon / new-conversation rule is intact. The observed-risk wording ("have been reported") survives (D23).
- R1: covered by SKILL.md :30 and :83 (no edits on reread-only grounds). The reference's criterion sentence is kept (:3).
- R2: "SKILL.md step 3" resolves; step 3 (:31) carries every limit the old line gave (no source text in either log, URL + verdict + one value, a draft span of a clause or less). The log example (:24-26) shows the method field.
- R3 restated step 3. R4's remaining bullet (:33) still says to leave the text as it is.
- D21/D22: the round-1 exception still agrees across step 4 (:32), Guardrails (:83-84) and reference rows 8 and 15. "Confirmed but not fixed" is still listed for regression, fixed point and the template (:44, :47, :69).

Check 2, contradictions or dangling references: none. Both files were read in full. All in-file pointers resolve, no step or section was renumbered, and the template (:56-73) is unchanged and agrees with :75-78.

Check 3, moved text: nothing moved into a reference. R2 adds a reference -> SKILL.md dependency, which is safe because SKILL.md is always loaded first. SKILL.md still completes with no tools and with references unreadable: the tool-less section (:38), stops, template and compact summary are all in the body.

Check 4, fidelity: see finding 3. Citations are correct.

Check 5, set conformance: all 15 recommended items were applied, with wording identical to the audit's proposals. S1b was not applied, which is correct. The dia-iterate diff contains nothing outside the set, and agents/openai.yaml is unchanged. Spec: D24 (spec.md:69) describes the dia-iterate edits accurately ("labels were shortened in place and kept"; templates and no-reference fallbacks kept). §5 now says "D19-D24", and §5.7 needs no change because its required wording ("This is expected behavior, not a failure", default 3, @dia-iterate, change-list default, one retry then change of shape) is all still present.

Check 6, commands, run in the tree (git status clean afterwards):
- `python3 tools/package.py --check`: "ok" for all seven skills, exit 0.
- `python3 -m unittest discover -s tests`: 13 tests OK, 1 skipped (PyYAML missing). Re-run in a scratch venv with PyYAML: 13 tests OK, 0 skipped.
- plugins/dia/skills/dia-iterate matches the source byte for byte. No Hangul. LF line endings. SKILL.md is 89 lines (limit 200).
- Token counts (tiktoken cl100k_base, my own run): SKILL.md 2,659 -> 2,364 whole file, body 2,467 -> 2,172 (-295). Reference 890 -> 782 (-108). These match the implementer's and the audit's figures.
