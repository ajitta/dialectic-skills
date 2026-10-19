Verdict: PASS WITH FIXES

Scope: `git diff d135f8e 75d7ac1 -- skills/dia-refine docs/spec.md` (dia-refine parts), checked against the audit (`docs/research/token-audit/dia-refine.md` §4), `evidence.md` §8, the upstream source (`upstream/installed/self-refine/SKILL.md`) and spec §5.6/§6/§7. I re-ran everything myself and did not rely on `docs/research/review/tokfix/dia-refine-applied.md`.

What changed (verified): four deletions in `skills/dia-refine/SKILL.md`; frontmatter, description, `metadata.version` and `agents/openai.yaml` are unchanged. Spec: a new D24 row (spec.md:69), "D19–D24" in §5, and a §5.6 note (spec.md:179).

## Checks run (real output)

- `python3 -B tools/package.py --check`: "ok" for all seven skills, exit 0.
- `python3 -B -m unittest discover -s tests`: 13 tests, OK (1 skipped: PyYAML missing). With PyYAML in a scratch venv: 13 tests, OK, none skipped.
- `git status --porcelain` is empty before and after, so nothing was written to the tree.
- `plugins/dia/skills/dia-refine/SKILL.md` is identical to the source.
- No Hangul in `skills/dia-refine/`. LF line endings. SKILL.md is 69 lines (limit 200).
- Token counts (tiktoken cl100k_base): body 1,929 → 1,836 and whole file 2,129 → 2,036, a cut of 93. This matches the implementer's account and the audit.

## Check-by-check

1. Behavior loss. The four core items are:
   - #3+#4: the intro's "The skill must work in a chat with no tools (mobile apps included), so verify only as far as the available tools allow and leave the rest marked unverified."
   - #7: the natural-language trigger bullet.
   - #8: "A dia-refine mentioned in passing in the middle of a sentence is not an invocation."
   - #21: "It is a request for review, not an error report."

   The operative behavior of each still exists elsewhere:
   - Tool-less handling is in SKILL.md:30: "this needs no tools", "if a search, code-execution or file tool is available", "Items you have no tool for, or could not check, stay as drafted and are marked unverified".
   - Anti-flip is at SKILL.md:14 ("a request for review is not in itself a sign of error") and SKILL.md:66.
   - Final-only mode is defined on its own terms at SKILL.md:39.

   All D19–D23 text survives unchanged: the Self-Refine label and arXiv ID (:14), the Huang citation (:32), the basis tags (:38), the closing line (:39), the subagent reason (:30), the bare-claim rule (:31), the (re-derived) explanation (:41), the creative-work basis (:69), the language fallback (:36) and the full example with the ④ suspected correction (:46–62). Removing #3+#4 also resolves the pass-2 nit about "leave the rest marked unverified" versus the closing-line rule. Two residual gaps (findings 1 and 2).
2. Contradictions and dangling references: none. The language fallback (:36, "one of the names under Invocation") still resolves, because the form list at :18 was kept. "See Safeguards" and "see below" (:39) still resolve. The template and the rules still agree. One D24/§5.6 wording mismatch (finding 3).
3. Moved text: nothing was moved. dia-refine still has no references, so the fallback when references cannot be opened is unaffected.
4. Fidelity: no citation was changed or moved. I checked both anyway:
   - arXiv:2303.17651 is "Self-Refine: Iterative Refinement with Self-Feedback", Madaan et al., 2023.
   - arXiv:2310.01798 is "Large Language Models Cannot Self-Correct Reasoning Yet", Huang et al. (ICLR 2024).
5. Recommended set versus applied: exactly the core set (#3+#4, #7, #8, #21). None of the extended items (#6, #22, #1+#15, #9+#10) was applied, and D24 says so ("Not applied … dia-refine's extended set"). No over- or under-application.

## Findings

1. should-fix — spec.md:174 versus the removal at SKILL.md:14 (old text).
   Spec §5.6 says: "The translation keeps every rule and its reason: candidate listing without a severity filter, verification limited to what tools allow, …". In the upstream file, the reason for "verification limited to what tools allow" is exactly the removed sentence ("도구가 없는 채팅(모바일 앱 포함)에서도 동작해야 하므로", from `upstream/installed/self-refine/SKILL.md`, intro). Old text (`git show d135f8e:skills/dia-refine/SKILL.md`, line 14): "The skill must work in a chat with no tools (mobile apps included), so verify only as far as the available tools allow and leave the rest marked unverified."
   The rule survives in step 3, but its reason no longer appears anywhere in the body. D24's dia-refine sentence does not record this departure from §5.6. The audit itself sent a similar §5.6-protected item (#22, "the safeguards") to the owner, but treated this one as core, which is inconsistent. The owner approved the cut, so fix the record rather than the skill. In spec.md:69 (D24), replace "dia-refine's natural-language triggers live in the description only." with:
   "dia-refine's natural-language triggers and passing-mention rule live in the description only, and its intro sentence on chats with no tools is cut: step 3's conditional wording ("this needs no tools", "if a … tool is available", unchecked items "stay as drafted and are marked unverified") carries the §5.6 rule "verification limited to what tools allow" without the upstream reason."
   Alternative, if the owner prefers to keep the reason in the body (about +9 tokens): at SKILL.md:30, change "Items you have no tool for, or could not check, stay as drafted and are marked unverified;" to "The skill must complete with no tools: items you have no tool for, or could not check, stay as drafted and are marked unverified;".

2. nit — SKILL.md:20 (cut #8). The audit's premise is that the description "says the same thing … on every surface". That does not hold on Codex. The Codex skills page (developers.openai.com/codex/skills, fetched today) says: "If many skills are installed, Codex shortens skill descriptions first." The passing-mention sentence starts at character 542 of the 675-character description (SKILL.md:3), so it is among the first text to be cut. dia-refine also has `allow_implicit_invocation: true` (`agents/openai.yaml`). So on a Codex install with a crowded skill list, a mid-sentence "dia-refine" can load the skill, and the body no longer tells the model to back out. The explicit rule at :18 ("the message starts with `dia-refine`") partly covers this. The risk is low and the owner approved the cut, so no change is required. If the owner wants the guard back for 12 tokens, change SKILL.md:20 to:
   "- A mid-sentence mention of dia-refine is not an invocation. Requests for several rounds belong to `dia-iterate`, not to this skill."

3. nit — spec.md:69 versus spec.md:179. D24 records only "dia-refine's natural-language triggers live in the description only", while §5.6 (:179) says "the natural-language triggers and the passing-mention rule live in the description only". Fix with the D24 replacement text in finding 1 (it adds "and passing-mention rule"). If finding 1's text is not taken, change the D24 sentence to: "dia-refine's natural-language triggers and passing-mention rule live in the description only."

4. should-fix (process, not text) — no file in the diff. The audit §6 ("Verification needed after any cut") and evidence.md rule 13 ("Validate each class removal with the probes before shipping … High") call for re-running P8 (covers #3/#4), P6 (covers #7/#8) and a new pushback cell (covers #21). The implementer's account says none were run, and neither `docs/handoff.md` nor `docs/probes.md` records them as due. I could not run them, because the claude and codex CLIs were out of scope. Add a row to `docs/handoff.md` (item 9, or a new row before item 7):
   "| 10 | D24 probe re-run | agent | Before the 0.x pre-release: re-run P6 and P8 (dia-refine and the other D24-changed skills) from a neutral directory, plus the two new cells from `docs/research/token-audit/dia-refine.md` §6 (final-only request; pushback on a correct draft), n≥2. Record the results in `docs/probes.md`. |"

No blockers. The skill text change is correct, minimal and exactly the approved set. The fixes are about the spec and the record, plus one optional re-hardening.
