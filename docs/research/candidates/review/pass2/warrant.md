Verdict: PASS WITH FIXES

# dia-warrant, second pass (275e1aa; first pass reviewed b30344d)

Scope: `skills/dia-warrant/`, its design note `docs/research/candidates/design/dia-warrant.md` (DN), and the warrant claims in spec D35/§5.8 and probes Part O. The tree was read-only; commands ran in a scratch copy.

Mechanical: `tools/package.py --check` rc=0; unit tests 19 OK (skipped=1); description 1,015 chars (unchanged); body 133 lines by package.py's count (132 at b30344d). `plugins/dia/skills/dia-warrant` is identical to the source and to the `var2` copy Part O ran. I re-tallied every warrant cell in Part O (w-*, i-churn-all, i-last-answer) from `~/work/dia-review/new-skills-2026-10-21/out{,2}/`; all numbers match.

## First-pass findings

1. Fixed. Rule 3, Step 5 and theory.md §4 carry the proposed text verbatim (SKILL.md:41, :76; theory.md:46); the intro (:16) says "adapts". Residual ambiguity: N7.
2. Fixed. The qualifier form is in Rule 7 (:45); Step 6 (:80) reports the qualifier every time and gives the qualifier-only result; Step 7 (:84) and the template have the field and Result lines.
3. Fixed. Rule 5 (:43) says for or against; Step 6 (:80) has the new condition. The template status line is hard to parse (N2).
4. Fixed: Follow-up (:131) and ask mode (:118).
5. Fixed. Rule 4 (:42) states the departure; the rejection follow-up is split by target (:132); ask mode (:119) leaves "none given"; Rule 7 bridges "none given" to "How do you get there?" left open; theory.md quotes all of rule 5. Its rationale undercuts itself (N5).
6. Fixed (theory.md:34).
7. Partly fixed.
   - Done: "7 and 3" corrected; cells 11–14 added; cells 11–13 run in Part O.
   - Not done: the results never came back to DN, where :77 and :89 still say "open".
   - DN:40 conditioned the "fallacy" decline on cell 11. Cell 11 was lost on both engines, and nothing was decided.
   - Cell 14 was not run as written.
   - My first-pass advice ("if 12–14 miss, narrow the description") pointed the wrong way, because those are positive cells, and DN:73 copied it. See S1.
8. Applied as written, but no routing effect. Scope (:35) is read only after dia-warrant has loaded.
   - Cell 12: Claude loads dia-brainstorm 3/3, which steelmans "your argument" and runs its own Step 1 (`cc-var2-w-poke-arg-1.json`).
   - Brainstorm's Step 0 fallback (brainstorm:41) points to dia-counterplan and dia-conjecture, not dia-warrant.
   - Cell 13 loads nothing on Claude (0/3).
   - My fix was insufficient; see S3.
9. Fixed (:45, :80).
10. Fixed. Step 7 (:84) matches the template order.
11. Fixed (:110, :111).
12. Fixed as listed. The same commit added new stale text (S1, N1).

Regressions or contradictions from the fixes: none found. Rule 7 and Step 6 agree on the qualifier-only result. The ask-mode "none given" line (:119) agrees with the early-stop rule (:120), and both agree with the follow-up result (:132).

## Real sessions (out-283-a/b, warrant.json; one audit turn each, no tools)

Both follow the fixed text.
- Target and mode on the first line.
- "will" read as no qualifier.
- Warrants labelled reconstructed; backing and rebuttal "none given".
- Seven tagged questions, all open.
- The qualifier compared "with my reconstructed W2", the new Step 5 sentence.
- The fixed result form.
- A record with the Step 7 fallback fields (the template was not read).
- The truth line, then the ask-mode offer.

Departures:
- Rule 5, session a: recall used to settle an open question, with no evidence class and no "Facts added" line. Quote: "[data] Is the friend a genuine expert in the relevant field? Open. A personal trainer knows exercise practice. Orthopedics and sports medicine are a different field". Session b asks the same question and asserts nothing.
- Rule 3, both sessions: W1/W2 used for a chain. Rule 3's W1/W2 are rival warrants for one step; both sessions use them for two steps in series (trainer says X; X, so I will get knee problems). Session a says "W2 is the one tested for the qualifier", calls the W2 step "the biggest jump", and then names a W1 question as the weakest link, against Step 6's least-support rule. The skill has no rule for an intermediate claim (S2).
- Step 6, session b: "Report the Step 5 result beside the weakest link in every case" is not followed. The Result paragraph omits the qualifier, which appears only earlier and in the record.
- Step 7, both sessions: the truth line names the data, not C. Quote: "This audit does not decide whether running harms knees." C is "I will get knee problems" (N4).
- Both sessions: every reconstructed warrant is defeasible, so any unqualified "will" comes out "overstated". This follows from Rule 3 as fixed, and my own wording is part of the cause (N7).

## Claims in DN, D35/§5.8 and Part O

True:
- DN:4–6 and DN:83–94 (each applied fix checked against the text).
- DN:34.
- The 1,015-character count.
- Spec §5.8 purpose, and spec line 313.
- Part O's warrant numbers.
- "var2 = the build that ships", byte-identical for dia-warrant.

False or stale:
- DN:12 and DN:81 say "132 lines"; it is 133.
- DN:77 and DN:89 say the re-probe is open; it ran.
- DN:73 is wrong for cells 11–14.
- DN:40's condition fired: cell 11 loaded no skill (Claude 0/3, Codex 0/2).
- DN cell 14 (→ dia-warrant) was never run. Part O substituted a different "Check the reasoning in your last answer: …" prompt, expected "informative", and gave no note.
- Part O reading 1 ("Every positive cell for the three new skills loads its skill on both engines except the Korean startup-survival claim on Claude") is false once the boundary cells are counted:
  - fallacy: 0/3 and 0/2;
  - poke-arg: Claude 0/3, Codex 1/2;
  - hidden assumptions: Claude 0/3;
  - churn-all: Claude 1/3, Codex 0/2.
- Part O reading 3 calls the fallacy cell "pre-existing behaviour, not caused by the new descriptions". Base has no dia-warrant to load, so for these cells it is a miss of the new description, and Codex misses it too.
- D35 says "each new description carries exclusion sentences toward its bordering siblings". Cell 12 shows dia-brainstorm is a bordering sibling, but dia-warrant's description and §5.8 Borders do not name it (N6).

Not verified: D35's 1,922 o200k token total (tiktoken is not installed; it spans all ten skills).

## New findings

### S1. should-fix: Part O results not folded back; Part O misreads the warrant cells

DN:77, replace the last sentence with:
> Cells 11–13 and the post-fix re-probe were run on `283f6fa` (probes Part O). Cell 11 loaded no skill (Claude 0/3, Codex 0/2). Cell 12 went to dia-brainstorm on Claude (3/3) and split on Codex (dia-warrant 1, dia-brainstorm 1). Cell 13 loaded nothing on Claude (0/3) and dia-warrant on Codex (2/2). Cell 14 was not run as written: Part O ran a different "check your last answer" prompt and expected no skill.

DN:89, replace "Running 11–14 and the post-fix re-probe is open." with:
> Cells 11–13 and the re-probe ran (probes Part O; results above); cell 14 as written is open.

DN:73, replace with:
> A miss on 5–10 means the description is pulling too wide. Narrow the triggers first. Do not add another exclusion clause, because the description is 9 characters under the limit. A miss on 11–14 means a request this skill should take went elsewhere or nowhere. Fix it in the sibling that took it (its body fallback) or in this description's triggers, not by narrowing this description.

DN:40: the condition has fired, so the owner decides.
- (a) Recommended: add the trigger. Drop "Ends with a record. " (the record is body content, not a routing cue). Then replace "or whether an expert, analogy or causal argument holds up," with "or whether an expert, analogy or causal argument holds up or is a fallacy,". That gives 1,011 characters. Re-run cell 11.
- (b) Decline again, and record: "Cell 11 loads no skill on either engine. Declined: Claude answers it directly at base too, and the headroom is kept."

Part O reading 1, replace with:
> - Every positive cell in the first table loads its skill on both engines except the Korean startup-survival claim on Claude (0/3; a bare factual claim with no stated reasons, answered directly; Codex 2/2). The boundary cells that expect dia-warrant mostly miss: the fallacy question loads no skill (Claude 0/3, Codex 0/2); "Poke holes in my argument …" goes to dia-brainstorm on Claude 3/3 and to dia-warrant on Codex 1/2; hidden assumptions loads dia-warrant on Claude 0/3 and Codex 2/2; the all-users churn argument loads it on Claude 1/3 and Codex 0/2.

Part O reading 3, replace with:
> - The boundary cells that expect dia-reductio or no skill show Claude answering a short check directly in both arms (the proofs, the invalid syllogism, "check your last answer"); that is pre-existing behaviour. The dia-warrant boundary misses have no base to compare with: they are misses of the new description.

### S2. should-fix: no rule for chained steps (both real sessions improvised)

Append to Step 1 (:53):
> If the reasons reach C through an intermediate claim (data, then C1, then C), name C1 in one line. Give each step its own warrant, labelled by step (Wa: data to C1; Wb: C1 to C). W1 and W2 remain rival warrants for one step. Ask the questions of both steps within the eight-question cap, check the qualifier on the step that reaches C, and say in the result which step the weakest link is on.

Template, Layout: after the W2 line, add:
> - Step warrants (only for a chain): Wa data → C1 "…"; Wb C1 → C — reconstructed

### S3. should-fix (sibling file, required for finding 8 to work): dia-brainstorm has no pointer to dia-warrant

`skills/dia-brainstorm/SKILL.md:41`: after "…it belongs to dia-conjecture;", insert:
> if it asks how well the reasons given support a conclusion (an argument rather than an idea or plan), it belongs to dia-warrant;

Append to DN:90:
> The Scope tiebreak acts only after this skill loads; the reverse case is in dia-brainstorm's Step 0 fallback.

Then re-run cell 12. The skill stays unreleased on `next`.

### Nits

- N1. DN:12 and DN:81: change "132 lines" to "133 lines".
- N2. Template, critical-question line 1: replace with
  > 1. [data] …? — answered (in the argument "…" | by the user | by a source you found, evidence class) for | against the step; or open
- N3. When the warrant reads "none given", Step 5 has nothing to compare. Append to Step 5:
  > If the warrant reads "none given", the qualifier check reads "no warrant to compare".

  In the template record, the Warrant line becomes:
  > - Warrant: stated | reconstructed (W1; W2 if any) | none given
- N4. Step 7, last sentence: replace with
  > End with one line naming C: whether "C" is true is not decided by this audit (then, if Parameters call for it, the one-line ask-mode offer).
- N5. theory.md §4 grounds the departure in "because the reconstruction is the assistant's and not a premise the user left implicit". If that were true there would be nothing to depart from. Replace the clause with:
  > because the assistant cannot tell whether its reconstruction is the premise the user left implicit, and the user's word is the only evidence of it
- N6. Spec §5.8 Borders: append
  > ; poking holes in an idea or plan to dia-brainstorm (an argument's support stays here).
- N7. Rule 3 says "the strength the target's own words give the link". That can be read as including the claim's qualifier, and then Step 5 can never fire. The intended reading means every unqualified claim on a reconstructed warrant is "overstated", so "no weak link found" can never be reached for it. In Rule 3, replace "Give it the strength the target's own words give the link;" with:
  > Give it the strength the target's own words give the rule itself (the claim's qualifier does not count);

  Append to Step 5:
  > When the claim is unqualified and the warrant is your "generally" reconstruction, say that the overstatement follows from that default, so the user can say whether "certainly" was meant.

## Summary

No blockers. All twelve first-pass findings were acted on; 1–6 and 9–12 are fully fixed. Finding 7 is only partly closed, and finding 8 is applied but does not change routing. The real sessions follow the fixed rules, with one Rule 5 lapse, one Step 6 lapse and one systematic gap (S2).

Before the merge to main:
- S1: fold the probe results back into DN and fix the two Part O readings.
- Owner: choose (a) or (b) on the fallacy trigger.
- S2: add the chained-step rule.
- S3: add the dia-brainstorm pointer, then re-run cell 12.
