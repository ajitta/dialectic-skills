# dia-refine: low-severity findings

All edits are in `skills/dia-refine/SKILL.md`. `agents/openai.yaml` and the description are unchanged.

- **F5 (applied, kept short).** Step 3: "Re-derive logic and calculations independently; this needs no tools." -> "Re-derive logic and calculations independently, from the question or the user's data rather than by following the draft's working; this needs no tools." Per the review, the line does not claim a CoVe-style factored gain. A single turn cannot take the draft out of context. The change only says where the re-derivation starts.
- **F6 (applied; labelled as an added reason).** Step 3: "Do not launch subagents to check your own work." -> "... check your own work: a copy of the same model is not an outside check." This reason is new. Upstream U:25 gave none, so this is a content change, not a translation fix. It rests on Xu [9] and Panickssery [13]. If the spec or decision log records it, it should be labelled as added. I left out the proposal's "most surfaces have none", because that is not a reason to avoid subagents where a surface does have them.
- **F8 (applied with the review's correction).** Safeguards, creative line: appended "A conflict with one the user stated is a confirmed basis (the user's instructions); a matter of taste is not a defect: keep the draft's choice and, if it is worth raising, mention it in the one line at the end." Taste goes to the closing line, not to ④, so ④ keeps its meaning. To keep "final version only" mode consistent, the closing-line list in Output was changed: "a problem outside the scope (see Safeguards)" -> "a problem outside the scope or a matter of taste (see Safeguards)".
- **F9 (applied).** Step 4, after the three bases: added "A user's bare statement that something is wrong is review criteria, not supplied material." The proposal's second half ("supplied facts ... are a basis") was dropped because step 4 already lists supplied material as a basis.
- **F10 (applied, one line).** Intro: "This is a single-pass procedure." -> "This is a single-pass procedure, not the iterative Self-Refine loop (Madaan et al., 2023, arXiv:2303.17651)." Huang is cited once, in step 5, as the reason (see F13), so the label line does not repeat the reason. Per the review's §2 correction, upstream was already single-pass, so the line is a label, not a behavior change. The research §8 Q5 left body citations to the owner. I applied the line as the brief directs, following dia-iterate's precedent. Revert it if the owner wants a citation-free body. The text "Self-Refine" does not trip OLD_NAMES_RE, which is case-sensitive and matches `self-refine`. A crossref check on the file returned no errors.
- **F11 (applied).** The example defect list is no longer in a ```` ``` ```` block. It is plain Markdown, with a blank line between parts so that the ②–④ headings and the "Incidental" line do not get folded into the list item above them. No extra instruction was added.
- **F12 (applied, neutral item only).** Added to ④ in the example: `- "founded in 1998": I recall 1996; no tool to check; left as drafted, unverified`. The P8 GIL sentence was not used. The item matches step 3 (recall is not verification) and step 4 (④ with the suspected correction).
- **F13 (S:33 softened; S:30 kept).** Step 5: "Rechecking again and again only adds cost; the result does not improve." -> "Rechecking on your own judgment alone adds cost and tends not to improve correctness; on reasoning it can make it worse (Huang et al., ICLR 2024, arXiv:2310.01798)." The step-2 severity-filter reason is unchanged. Spec §5.6 requires it, and CriticGPT [12] gives it indirect support, as the review says.
- **F15 (applied).** In the example, "③ Content kept" -> "③ Correct content kept", matching the label in the Output list. In Output, "(a calculation, the output of a code run)" -> "(such as a calculation or the output of a code run)". This restores upstream's "등" so the list reads as open.
- **F14:** already done before this pass; nothing changed.

Contradiction sweep: I reread the whole SKILL.md after the edits.
- The ④ example still matches step 3, step 4 and the ① tag rule.
- The ③ label now matches the Output list.
- The taste mention fits Safeguards "one line at the end" and the closing-line list in final-only mode.
- F9 agrees with Invocation ("What follows is the review criteria") and the anti-flip safeguard.
- F13's "on your own judgment alone" agrees with "Iterate further only on new evidence or specific feedback."

Not done, as instructed: tools/package.py, version bumps, spec or decision-log entries. Because of F6, a D-row entry should mark the subagent reason as added, not translated.

SKILL.md: 70 lines (limit 200). Description: 675 characters, unchanged. No Hangul in the file.
