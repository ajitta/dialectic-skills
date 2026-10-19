Verdict: PASS WITH FIXES

Scope: `git diff 1b3f139 b430a97 -- skills/dia-refine`, which is 9 hunks, all in SKILL.md. agents/openai.yaml did not change. The same diff over `docs/spec.md README.md tests/` is empty: this commit changes no spec, README, test or research-index text. Line numbers below are for SKILL.md at b430a97 unless stated.

Commands run in the tree (read-only):
- `python3 tools/package.py --check`: "ok dia-refine" and ok for all seven skills, exit 0.
- `python3 -m unittest discover -s tests`: "Ran 13 tests ... OK (skipped=1)".
- My own checks:
  - SKILL.md is 70 lines. The description is 675 chars and unchanged.
  - No Hangul (spec L1 ranges).
  - No Claude, ChatGPT, Codex, GPT, OpenAI or Anthropic in skills/dia-refine/.
  - plugins/dia/skills/dia-refine/SKILL.md is byte-identical to the source.
  - OLD_NAMES_RE (tools/package.py:62-63) has no IGNORECASE flag, so "Self-Refine" at :14 does not trip it. The implementer's claim holds.

## Hunk check (1) and the implementer's account

Read against review/dia-refine.md, which takes precedence:

- F5, :31 "from the question or the user's data rather than by following the draft's working". The review lowered this to low and called the wording harmless. It does not claim a CoVe factored gain. Minimal, and correct.
- F6, :31 "a copy of the same model is not an outside check". Partly applied. See findings 1 and 3.
- F8, :70 and :40. Applied in the review's corrected form: taste goes to the closing line, not to ④. :40 was extended to match, which is consistent. Wording nit in finding 4.
- F9, :32. The review confirmed this item. The proposal's second half was dropped, and the drop is justified: step 4 already lists "supplied material" as a basis. This agrees with Invocation :18 ("What follows is the review criteria") and with Safeguards :67.
- F10, :14. The wording is accurate. Spec §5 left body citations as an owner question (research §8 Q5). No decision is recorded, so see finding 1. dia-iterate:14 already cites the same way, so a precedent exists.
- F11, :47-63. The fence was removed, with blank lines between parts. The review confirmed the proposal, which was an instruction: "(print it as plain Markdown, not in a code block)". The implementer instead removed the cause. That is acceptable, but it is a different form (finding 5).
- F12, :61. The neutral item matches the review's text plus ", unverified" (as :60 has). It contains no P8 probe content. It agrees with :31 (recall is not verification) and :32 (④ with the suspected correction).
- F13, :33. The review said softening was fair, and the softening is fair. But the edit also dropped "again and again", and that widened the scope (finding 2). S:30 was kept, which is correct under spec §5.6 (spec.md:172).
- F15, :56 and :42. Both applied. "③ Correct content kept" now matches :39, and "such as" restores upstream's 등.
- F7 and F14 were applied in earlier batches (:44; openai.yaml:4). Nothing was missing.

The implementer's report is accurate except on two points:
- It says only "most surfaces have none" was dropped from F6. The proposal's "it costs extra calls" was dropped too.
- It does not mention the "again and again" loss in F13.

## Fidelity (3)

I fetched both arXiv abstract pages:
- arXiv:2303.17651 is "Self-Refine: Iterative Refinement with Self-Feedback", Madaan et al., 2023. Its abstract says "iterative feedback and refinement". So "not the iterative Self-Refine loop" is accurate. Upstream U:8 was already single-pass ("한 번의 점검으로 끝나는 절차다"), so the line is a label, not a behavior change, as the review said.
- arXiv:2310.01798 is "Large Language Models Cannot Self-Correct Reasoning Yet", Huang et al., with the comment "ICLR 2024". Its abstract says "LLMs struggle to self-correct ... without external feedback, and at times, their performance even degrades". That supports "tends not to improve correctness; on reasoning it can make it worse".

## Logic (4)

- The arithmetic example is unchanged: 620+800=1,420 and 620+620=1,240.
- The ④ example "I recall 1996" states a suspected correction without asserting it, which is consistent with :31 and :32.
- No stop condition changed.

## Findings

1. should-fix: the record was not updated for this batch.
   - Locations: docs/spec.md:64-67 and docs/research/README.md:53.
   - The decision log ends at D22. research/README.md:53 still lists "refine F5, F6, F8–F15" under "Still open". F14 is listed there too, although D19 applied it (openai.yaml:4).
   - The review explicitly asked to label F6 as a content change ("Adding a reason the upstream never had is a content change, not a translation fix. Label it that way."). Spec §5.6 (spec.md:172) promises a translation that "keeps every rule and its reason". F6 adds a reason that upstream U:25 never gave, F13 changes upstream U:27's reason, and the F10/F13 body citations settle research Q5. Nothing in the repository records any of this.
   - Add after spec.md:67:
     `| D23 | Remaining low research findings (2026-10-20). dia-refine: re-derivation starts from the question or the user's data; the no-subagent rule gains a reason upstream did not give (a copy of the same model is not an outside check; an addition, not a translation); a bare user statement that something is wrong is review criteria; creative work: a conflict with a stated purpose, audience, tone or constraint is a confirmed basis, and a matter of taste goes to the closing line; the body labels the skill as not the iterative Self-Refine loop and cites Huang et al. for the softened step-5 reason (owner question Q5 answered: citations allowed); the ④ example shows a suspected correction; the ③ label and "such as" restored. |`
   - In research/README.md:53, delete "refine F5, F6, F8–F15, " and add a line under a new "Applied, fourth batch (spec D23)" heading: `dia-refine F5, F6, F8–F13, F15 (F14 was applied in D19).`

2. should-fix: F13 widened the step-5 reason beyond repeated rounds (SKILL.md:33).
   - Upstream U:27 reads "재확인을 거듭하면 비용만 늘고" ("repeated rechecking only adds cost"). The old text kept that as "again and again". The new text, "Rechecking on your own judgment alone adds cost and tends not to improve correctness; on reasoning it can make it worse", drops "repeated".
   - It now reads as a claim about any self-check, including this skill's own step 3/4. Step 3 makes tool-less re-derivation the normal path, and step 4 counts it as a confirmed basis. So the new sentence undercuts both.
   - The review endorsed softening "does not improve". It did not endorse widening the scope. The review's F2 note also says Huang tests prompted re-answering, not re-derivation from scratch.
   - Replacement: `Rechecking again and again on your own judgment alone adds cost and tends not to improve correctness; on reasoning it can make it worse (Huang et al., ICLR 2024, arXiv:2310.01798).`

3. nit: the F6 reason alone does not explain the ban (SKILL.md:31), and its omission is unreported.
   - Own re-derivation is not an outside check either (:42 says so), yet step 4 accepts it with a tag. So "a copy of the same model is not an outside check" does not by itself say why a subagent is banned while self re-derivation is allowed. The dropped cost clause was what connected the reason to the ban.
   - "copy of the same model" is also not always literally true, because some harnesses run subagents on another model.
   - Replacement: `Do not launch subagents to check your own work: a subagent is normally the same model, so it adds calls without giving a stronger basis than your own re-derivation.`

4. nit: an ambiguous antecedent in the F8 sentence (SKILL.md:70).
   - In "A conflict with one the user stated", the nearest noun is "objective errors". On a skimming or translated reading, "one" can attach to the wrong noun.
   - Replacement for the second sentence: `A conflict with a purpose, audience, tone or constraint the user stated is a confirmed basis (the user's instructions); a matter of taste is not a defect: keep the draft's choice and, if it is worth raising, mention it in the one line at the end.`

5. nit: F11 is applied in a different form than the reviewed proposal (SKILL.md:47).
   - Removing the fence removes the cue, which is arguably the better fix. The report calls it "applied" with "No extra instruction".
   - The precedent the finding cites (08-implementation.md:57) was an explicit "print plain Markdown" instruction. If the owner wants the reviewed form, the replacement for :47 is: `Example defect list (print yours as plain Markdown, not in a code block):`
   - Otherwise, record the deviation in D23.

## Contradiction sweep (2)

I re-read all 70 lines.

- The new hunks agree with each other. The taste line (:70) matches the closing-line list (:40) and the out-of-scope line (:69).
- F9 matches :18 and :67.
- F5 matches the ① and ③ examples (:51, :57).
- The ④ example matches :31 and :32. The ③ label matches :39.
- The description (:3) still matches the body.
- The only new conflict is finding 2.
- One pre-existing tension, not introduced by this diff: in final-only mode, :31 and :40 drop marks for incidental unverified items, while :14 says "leave the rest marked unverified" (pass-2 nit 3).

## Not applied (5) and declines (6)

- Every refine low finding (F5, F6, F8-F15) is accounted for. Partial: F6 (finding 3), F11 (finding 5), and the F6 labelling (finding 1).
- These declines are justified:
  - F13 S:30, required by spec §5.6, with [12] as indirect support.
  - F6 "most surfaces have none".
  - F9's second half.
  - F12's GIL sentence (probe contamination).
- One decline is not justified: dropping F6's "costs extra calls" (finding 3).
