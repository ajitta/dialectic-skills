# Review: docs/research/dia-refine.md

Verdict: SOUND WITH FIXES

The document's citations hold up. I fetched all 17 sources and every quote and number checked is there. Its file:line references are accurate. The fixes needed are in the findings: two severities are too high, the evidence behind some findings is stretched, and three proposals would cause harm if applied as written (F12 contaminates the probe, F13 conflicts with spec §5.6, and F1 shows an "original" the user never saw). The translation audit (§5.1) also missed a real translation loss.

Method: I read SKILL.md (66 lines), agents/openai.yaml, upstream/installed/self-refine/SKILL.md, spec §5–7, probes.md, handoff.md, AGENTS.md and CLAUDE.md. I downloaded all 17 source URLs with curl (all HTTP 200; [14] redirects to platform.claude.com/.../claude-prompting-best-practices#chain-complex-prompts) and grepped the extracted text. The document is 382 lines, so it meets the <= 500 limit. The SKILL.md description is 675 chars and SKILL.md/openai.yaml contain no Hangul (checked with the spec L1 ranges).

## 1. Findings (section 7)

F1 (high): partly.
- The conflict is real. S:40 says "give only the revision. Do not show the review or a change log". S:42 (side-by-side display) and S:32 ("Do not ... hide it; mark its limits") cannot both hold in that mode. It is easy to reach: "give me only the improved final version" is a natural-language trigger (S:19, S:3).
- Severity should be medium. The P8 failure the document cites as the model case (probes.md:66) was a conflict about whether a fact gets changed. This one is about what gets displayed after the user explicitly asked for the revision only.
- Fix 1: the first exception must not apply to the "do this task the dia-refine way" case (S:20). There the "original result" is the model's internal candidate, which the user never saw. Printing it is noise.
- Fix 2: S:65 already requires "mention it in one line at the end" in every mode. That is a precedent for a closing line, and a third rule that collides with S:40. Cite it and merge it with the new line.
- The document correctly leaves the final decision to the owner (§8 Q1).

F2 (high): partly. Lower to medium.
- The real problem: S:32 counts "re-deriving ... yourself" as confirmed, while S:42 says "Do not declare the revision better on your own judgment alone". Yet a re-derived change is filed under "① Confirmed errors". The document does not state this internal tension directly. It should, because the tag proposal resolves it.
- The cited evidence measures different operations:
  - Huang [2]: re-answering after the prompt "Review your previous answer and find problems with your answer".
  - Tyen [5]: locating the first mistake in a CoT trace. The 52.87 is "with direct step-level prompting".
  - Valmeekam [8]: verifying plans.
- None of them tests working a calculation out again from scratch. That is closer to drawing a second sample (self-consistency), which Huang treats as the sound baseline.
- The tag proposal is cheap and correct. The example is arithmetically right (620+800=1,420; 620+620=1,240).

F3 (medium): partly.
- Real: S:31 "marked unverified" does not say where the mark goes.
- But upstream puts annotations inside the revision. U:35 reads "검증한 항목은 수정본의 해당 문장 가까이에 출처를 적는다" ("write the source near the sentence in the revision"). If F3 bans unverified marks from the revision while sources stay inline, the two rules become asymmetric. The owner should decide both together.
- The proposed text points to "the closing line of F1", so it breaks if F1 is not adopted.
- §6.4(a) overstates S:45: a note on the unverified passage is at the candidate passage, not "outside the defective passage".
- Probe evidence is n=1, which the document acknowledges.

F4 (medium): confirmed, and the scope should be wider.
- [17] says: "CLAUDE.md and CLAUDE.local.md files in the directory hierarchy above the working directory are loaded at launch". It also says "Imported files are expanded and loaded into context at launch" and "if two instructions contradict each other, Claude may pick one arbitrarily".
- CLAUDE.md is `@AGENTS.md`. AGENTS.md:21 says "reply in Korean, briefly", and it has said so since b9b9110, before the probes. handoff.md:35 uses the relative `--plugin-dir plugins/dia`.
- Missed: the same confound also primes routing. AGENTS.md describes the seven dia skills, so the P6/P7 routing results (and L7's "no routing drop") are inflated in absolute terms. The old arm ran in the same setting, so the relative comparison survives.
- Add to the proposal: [17] says Claude Code also reads AGENTS.md directly ("every AGENTS.md ... in your working directory and the directories above it") when there is no CLAUDE.md. The empty directory therefore must have no CLAUDE.md or AGENTS.md in any ancestor.

F5 (medium): partly. Lower to low.
- S:31 already says "Re-derive logic and calculations independently".
- CoVe's gain from factoring comes from removing the baseline from the prompt [6]. An instruction to "not follow the draft's working" cannot do that in one turn.
- The in-context variant in CoVe is "joint" (Wikidata precision 0.29), against two-step 0.36 and factored 0.32. So "F5 captures the useful part of a factored check" (line 284) is overstated. The wording itself is harmless and needs no tools.

F6 (medium): partly. Lower to low.
- Spec §5.6 requires keeping "every rule and its reason". It does not require inventing a reason that upstream never had (the document itself says U:25 has none).
- The proposed reason is defensible: Xu [9] and Panickssery [13] support it, and the subagent premise is right. Claude web/desktop/mobile and ChatGPT have no subagents.
- Adding a reason the upstream never had is a content change, not a translation fix. Label it that way.

F7 (medium): partly. Lower to low.
- The tension between S:44 and ② is real, but S:44 is soft wording ("has no reason to be longer").
- The evidence is overstated. Huang's missing-concepts analysis covers one of Self-Refine's seven tasks (CommonGen-Hard, Table 8: 81.8 vs 75.1). "Where much of the Self-Refine gain came from" generalises that to all seven tasks.
- Wording: also allow fixes to ① corrections, which can lengthen the text. For example: "Apart from added requirements (②) and necessary corrections, ...".

F8 (low): partly.
- The S:32 basis "the user's instructions" already covers a stated purpose, audience or tone (S:29 builds the checklist from them), so the gap is smaller than claimed.
- Sending "matters of taste" to ④ changes ④'s meaning from "remaining uncertainty" to suggestions. Use the S:65 closing line instead.

F9 (low): confirmed.
- The gap between S:18 (criteria), S:32 ("user's instructions or supplied material") and S:63 is real.
- The proposed text is minimal and consistent with the other rules.

F10 (low): confirmed.
- The wording is accurate. Its "because" justifies the single pass, matching dia-iterate:14.
- Whether to cite in the body is an owner decision (§8 Q5).
- One historical correction for §2: the upstream self-refine was already single-pass (U:8, "한 번의 점검으로 끝나는 절차다"). The departure from Madaan predates the rebuild; the rebuild only dropped the name.

F11 (low): confirmed.
- 08-implementation.md:57 reads "Brief in a code block (D): scrolls sideways on phones. The template now says to print plain Markdown".
- That evidence comes from one other skill, so low is right.

F12 (low): wrong as proposed.
- The gap is real: no ④ example shows the suspected-correction form.
- But the proposed example is the P8 probe's planted error ("Python 3.13 removed the GIL by default", probes.md:60). Putting it in the skill teaches to the test, and it would invalidate the P8 re-run that F4 recommends.
- Use a neutral item, for example: `- "founded in 1998": I recall 1996; no tool to check; left as drafted`.

F13 (low): partly.
- S:33: softening the reason is fair (Self-Refine Fig. 4 shows multi-round gains with "diminishing returns").
- S:30: "drop or soften the causal clause" conflicts with spec §5.6, which names "candidate listing without a severity filter" among the rules whose reason must be kept. Dropping it needs a spec change.
- The reason is also not unsupported. [12] reports "RL-only CriticGPT is more conservative, producing much higher precision critiques at the cost of recall". That is indirect support for "aiming for only the important ones finds fewer". A8 should say so. Keep the clause.

F14 (low): confirmed.
- probes.md:32 shows `$dia-intent` did not resolve on the Codex plugin route.
- This duplicates handoff item 3. The change also needs the spec §7.3 template (`Use $dia-<x>`) updated.

F15 (nit): confirmed.
- S:39 reads "correct content kept" and S:55 "Content kept"; upstream has the same mismatch (U:31 vs U:47).
- U:34 has "등" ("etc.") and S:42 dropped it.

All proposals keep within the rules: assistant-neutral "you", tool use is never required, no Hangul, and roughly +8 lines (well under 200 lines). The description is untouched.

## 2. Citations

All 17 resolve. Every quote and number the document uses for a high or medium finding or an audit verdict is verbatim in its source, and so are spot checks of the others:

- [1]: 4 iterations, "concrete phrases", 20%, 25.4 → 74.6, 94% "everything looks good", oracle +4.8/+0.7.
- [2]: Table 3, Table 8 (81.8/75.1), the oracle-label, mischange and feedback-prompt passages, debate vs self-consistency.
- [3]: Table 1, AmbigNQ 50.0 / 42.0 / CoT 44.2.
- [4]: all three quotes.
- [5]: 52.87.
- [6]: 17%/70%, precision 0.17 → 0.29–0.36.
- [7]–[9], [13]: the abstract quotes.
- [10]: 98% and "highly confident".
- [11]: 46%, 17%, challenger wording, wrong answers flip more (HTML v2 §5).
- [12]: real vs spurious issues, the model-only frontier.
- [14]–[17]: all vendor quotes, including "Codex shortens skill descriptions first" and "may pick one arbitrarily".

Problems:

- Overstated, §3.1 line 54 and F7: "much of the gain came from catching missing requirements" holds for Constrained Generation only, not for Self-Refine overall.
- Overstated, F2 / A3: the evidence is about prompted self-correction, error localisation and plan verification, not independent re-derivation. A3 "loose" stands, but its stated reasons should be narrowed.
- Overstated, F5 line 284: see F5. CoVe's in-context "joint" variant gains less than factoring.
- Unflagged weakness, A8: "the specific causal claim is unsourced". [12], already cited, gives indirect support (see F13).
- Minor, [1] line 42: "GPT-3 by 4.8%" copies the paper's prose. Table 9's column header is GPT-3.5 (64.06 → 68.9). Faithful to the text but internally inconsistent in the source; nit.
- Link, [14]: the URL redirects to the general best-practices page. Not dead, but the "chain prompts" title is stale. Nit.

No misattributions or dead links.

## 3. Fidelity audit (section 4)

- A1: right that it departs, but the departure is inherited from upstream (U:8), not introduced in the rebuild.
- A2: "matches CRITIC/Kamoi" holds only for two of the three bases (tool, user material). Re-derivation is intrinsic in Kamoi's sense. A3 covers this, but A2 should say "partly".
- A8: should be "loose, with indirect support [12]", not "reason unsourced".
- All other verdicts I agree with. A12 (anti-flip) is strongly supported by [10] and [11] as stated.

## 4. Missed issues

1. Should-fix: translation loss missed by §5.1.
   - §5.1 says "Every rule in U survives in S". But U:35 places sources "near the sentence in the revision" (수정본의 해당 문장), and S:43 says only "near the sentence concerned". The location is lost.
   - This matters for F3: the upstream design does annotate inside the revision.
2. Should-fix: S:32 vs S:42 contradiction.
   - Re-derived changes are "confirmed" (S:32) and so listed under ① "Confirmed errors" (S:39).
   - Yet S:42 forbids declaring the revision better "on your own judgment alone".
   - F2 touches this but never names the contradiction. The fix (basis tag) should cite S:42.
3. Should-fix (procedure, not skill): the F4 confound extends to routing. AGENTS.md names and describes the dia skills, so P6/P7 absolute routing rates were measured with that description loaded as project instructions. See F4.
4. Should-fix: S:65 vs S:40.
   - The "one line at the end" safeguard applies in final-only mode too, which contradicts "give only the revision".
   - That makes three rules in conflict with final-only mode, not two (see F1).
5. Nit: S:37 language rule with an empty message.
   - "language of the user's latest message" is undefined when the message is only `dia-refine` (S:18).
   - Add a fallback such as "or, if it has no text, of the conversation".
6. Nit: Hangul in the document itself (line 360, «확실해?»).
   - AGENTS.md literally says "No Hangul outside skills/<skill>/references/ko/".
   - docs/probes.md:47 has the same, so the rule is applied in practice only to shipped files. Harmless, but the document should be aware of it.

## Summary of changes to make in the document

- F1, F2 severity high → medium. F5, F6, F7 → low.
- F12: replace the example (probe contamination).
- F13: keep the S:30 reason (spec §5.6; [12] gives indirect support).
- F1: exempt S:20 and fold S:65 into the closing line.
- F3: decide together with sources-in-revision (U:35).
- F4: extend to routing and to AGENTS.md in ancestor directories.
- Narrow the evidence claims in F2, F5 and F7.
- Fix §5.1 (U:35 loss) and A2/A8.
