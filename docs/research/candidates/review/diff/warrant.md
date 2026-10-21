Verdict: PASS WITH FIXES

# dia-warrant diff review (next b30344d vs main eb7ab54)

Scope: `skills/dia-warrant/` (all four files), checked against design note `docs/research/candidates/design/dia-warrant.md` (DN), `review/argumentation.md` (RA) and `review/index.md` (RI). The tree was read-only; commands ran in a scratch copy.

## Mechanical checks (all pass)

- `python3 tools/package.py --check`: `ok dia-warrant`, rc=0. `python3 -m unittest discover -s tests`: `Ran 19 tests ... OK (skipped=1)`.
- Size limits: description 1,015 chars (limit 1,024); body 132 lines by package.py's count (limit 200); `short_description` 61 chars.
- Frontmatter keys are in the §7.2 whitelist.
- No Hangul in `skills/dia-warrant`.
- Wording is assistant-neutral: `claude` appears only as the target value, which SKILL.md:25 explains.
- Tool use is conditional (:43).
- References are read conditionally and have a body fallback (:16, :84); the scheme questions are inline (:88–99).

## Applied findings: verified in the text

- RA F6: results, record, the D19 pushback rule, target inference, reply language and the D26 sentence are at :45, :82–84, :129, :29, :46 and :124.
- RA F7b/F7d: the exclusions are at :3 and :35, and consequences replaces practical reasoning (theory.md:30).
- RA F8: Toulmin's own questions are at :58–59 and the paraphrase is flagged at theory.md:16. The merge is grounded in Verheij's four types and every question is tagged (but see finding 6).
- RA F9: least warrant and inline CQs are present (but see finding 1).
- RA F13: ask mode is present (:31, :113–119).
- RI F6: the reconstruction risk is covered by Rules 2–4 and the pitfall at :140, and the dia-refine scope is fixed. Declining a "fallacy" trigger is reasonable, but its condition cannot fire (finding 7).
- RI F10: the exclusion is present.

Sources fetched: all support the text except as noted in findings 5 and 6.
- Verheij 2009: page references and the four types.
- Wikipedia "Pragma-dialectics": rules 3/5/7/8/10.
- Wikipedia "Argumentation scheme": expert opinion, WRM p. 310.
- Walton 2014: analogy, p. 315.
- IRMCT amicus para. 12: cause to effect.
- Fan 2019: consequences, p. 102.
- Blair 1998: sign, Walton 1996 p. 48.
- Calvo Figueras & Agerri 2024.

## Findings

### 1. should-fix: Rule 3 contradicts the worked example and Step 5, and the validity rule as cited contradicts Rule 1

Rule 3 (:41) says: supply the least rule that "licenses the step to the claim **at its stated strength** (after the pragma-dialectical validity rule: ... would make it valid)".

The example (:103–110) breaks it:
- The claim is "will", unqualified.
- But W1 = "...will **generally** work for us".
- Then: "W1 licenses 'probably'; the claim says 'will', so it is overstated."

So the assistant weakened the warrant below the stated strength and then charged the arguer with overstatement. Followed literally, Rule 3 makes Step 5 unable to ever find an overstatement on a reconstructed warrant. Making a "will" step *valid* would also need a strict warrant, which clashes with Rule 1 (:39): "it does not claim deductive validity".

Replace Rule 3 with:

> 3. **The least warrant.** The warrant is usually unstated. Supply the least general rule that, with the data, takes the step to the claim: keep the arguer's terms and add no content the step does not need. Give it the strength the target's own words give the link; if they give none, write it as holding "generally" (Toulmin's usual warrant), never "all" or "always" unless the target says so. This adapts the pragma-dialectical validity rule (an argument may be used if making its unexpressed premise explicit would make it valid) to a defeasible step: supply the premise the step needs, not one that makes it deductively valid. Label it reconstructed. If two warrants are plausible, write both (W1, W2), test the one the arguer more plausibly relies on, and say whether the other changes the result.

Append to Step 5 (:76):

> If the warrant is reconstructed, say in the same line that the comparison is with your reconstruction.

In theory.md:46, replace "takes its form from the **validity rule (8)**:" with:

> adapts the **validity rule (8)** to defeasible steps (it supplies the premise the step needs, not one that makes it deductively valid):

### 2. should-fix: the qualifier check never reaches the result or the record

Rule 7 (:45) and the Step 6 tie order (:80) list "qualifier" as a possible weakest-link slot. But every result form is "because [critical question] is left open/answered against", and no question is tagged [qualifier] (:44). The record (:84; template :44–54) has no qualifier field.

So an "overstated" finding is lost. When every question is answered, Step 6 returns "no weak link found" beside an overstated claim.

Fix:
- Rule 7: after "...with the quote);" insert:

  > **weakest link: qualifier, because the claim says "[strength]" where the warrant licenses "[strength]"**;

- Step 6: append:

  > Report the Step 5 result beside the weakest link in every case. If no question is open or answered against the step but the qualifier is overstated, the result is **weakest link: qualifier**.

- Step 7 fields: after "result;" insert "qualifier check (matches or overstated);".
- Template: add `- Qualifier check: matches | overstated ("…" vs "…")`, and add the qualifier form to the Result line (:50).

### 3. should-fix: the "no weak link" condition ignores answers against the step and answers from a source

Step 6 (:80): "If every question asked is answered in the argument or by the user, the result is **no weak link found**".

- A question answered *against* the step by the user meets this condition, which contradicts the same step's first sentence.
- "Answered by a source you found" is missing, so an audit where every question is answered by a source has no result.
- Rule 5's statuses (:43) carry no direction, but Rule 7 needs one.

Replace that sentence with:

> If no question asked is open or answered against the step (each is answered for it in the argument, by the user or by a source you found) and the qualifier matches, the result is **no weak link found among the questions asked; not a proof**:

Append to Rule 5:

> An answered question is answered for or against the step; say which.

### 4. should-fix (yielding): bare assertions close open questions

- Follow-up (:130): the user's answer is marked "answered by the user", then Steps 5–7 are redone.
- Ask mode (:117): "Each answer fills its slot as stated by the user."

Nothing requires the answer to supply what was asked. Repeating "yes, they do" to each open question reaches "no weak link found", which is the yielding path D19 targets. The siblings guard this:
- brainstorm:107 ("only if they add a substantive answer");
- conjecture:86 ("a bare 'no', or insistence ... disputed").

Append to :130:

> An answer counts only if it supplies what the question asks for (a measure, a named similarity, a reason, a source); a bare "yes", "it does" or "trust me" leaves the question open: say so in one line and keep its status.

Append to :117:

> A bare yes or no to a critical question fills nothing; ask once for the content, then mark it open.

### 5. should-fix (fidelity, yielding): "if the user disowns it, it goes" ignores the target, inverts the cited rule, and leaves no result

**Fidelity.** Rule 4 (:42) is labelled "from pragma-dialectics", but the cited rule 5 (fetched) reads: "A party may not **deny premise that he or she has left implicit** or falsely present something as a premise that has been left unexpressed". The skill keeps the second half and reverses the first, with no label.

**Target.** Follow-up :131 removes a rejected warrant for any target. For `text` or `claude` the user is not the arguer: "ask ... which rule they rely on" has no addressee, and the rejection is really a dispute, which :129 requires a named defect for. dia-counterplan:119 draws this distinction ("For target `user`...").

**Result.** After a removal with no replacement, there is no defined result outside ask mode's stop rule. Any weak link at the warrant slot can be made to vanish.

Replace the Rule 4 "Unexpressed premise" sentence with:

> *Unexpressed premise:* never present a reconstructed warrant or premise as the target's own. When the user is the arguer and disowns it, it goes, but the step still needs a rule (Follow-up turns); this departs from the rule's other half, under which an arguer may not deny a premise left implicit.

Replace :131 with:

> - **The user rejects a reconstructed warrant:** for target `user`, remove it, test W2 if there was one, otherwise ask in one line which rule they rely on; if they name none, the warrant reads "none given" and the result is **weakest link: warrant, because "How do you get there?" is left open**. For `claude` or `text` the user is not the arguer: treat the rejection as a dispute (withdraw only on a named defect), and if the user proposes another rule, add it as W2 and say whether it changes the result. Then redo Steps 4 to 7.

At :118, after "a 'no' removes it", append:

> ; if the user names no other rule, the warrant stays "none given" (at the end: **weakest link: warrant**, or **stopped** on an early stop).

Add the departure sentence to theory.md §4 after :43.

### 6. nit (fidelity): theory.md overstates what Verheij sorted

theory.md:34 says "Verheij sorts the expert-opinion questions this way". What Verheij actually sorts (§2.5, fetched) is Walton's **1996 five** questions, plus a conditions-of-use question of his own.

SKILL.md:95 uses the **2008 six**. Two of its tags have no basis in Verheij:
- trustworthiness, tagged [rebuttal];
- backup evidence, tagged [warrant/backing], which is not Verheij's conditions-of-use question.

Replace the sentence with:

> Verheij sorts Walton's 1996 expert-opinion questions this way and adds a conditions-of-use question of his own; the tags on the 2008 trustworthiness and backup-evidence questions, and on the other four schemes, are this skill's application of the same mapping.

### 7. should-fix (routing unverified): the probe table has no results, and one condition cannot fire

- DN:54–69 has only an "Expected" column; neither `docs/probes.md` nor `docs/handoff.md` mentions "warrant".
- DN:34 says "Probe cells 8 and 3 cover both directions"; the conjecture cell is 7, not 8.
- DN:40 makes the "fallacy" decline conditional on probes, but no cell tests a fallacy request.

Fix: run the table (Claude and Codex, n=2) before merging to main and record the results; change "8 and 3" to "7 and 3". Add four cells:
- (11) "Is this an appeal to authority fallacy? 'My doctor says it, so it's true.'" → dia-warrant.
- (12) "Poke holes in my argument that remote work will work for us because it worked at Acme." → dia-warrant, not dia-brainstorm.
- (13) "What hidden assumptions is my case for the four-day week resting on? It boosts morale, so productivity rises." → dia-warrant, not dia-counterplan.
- (14) "Does the reasoning in your last answer actually support its conclusion?" → dia-warrant (target claude), not dia-refine.

### 8. should-fix (routing): three collisions have no tiebreak

All ten descriptions were read. The new pointers agree with each other: reductio, conjecture and counterplan all send "how well reasons support a probable conclusion" to dia-warrant, and dia-warrant's exclusions point back.

Requests still claimed twice:
- (a) "Poke holes in / question me about my argument". dia-brainstorm claims "poke holes in it" and "question me about this idea" (brainstorm:3). dia-warrant's ask mode "questions the user slot by slot". Neither points to the other.
- (b) "What does my case for X rest on?", where an argument is given for a decision. dia-warrant claims the warrant, and its Scope lists consequences arguments (:35). Its own exclusion sends "assumptions under a plan or decision" to dia-counterplan, which builds a full counterplan (counterplan:3) the user did not ask for.
- (c) A universal claim argued from cases. Scope sends only *counterexamples* to dia-conjecture, while dia-conjecture's description takes any "strictly universal claim the user holds".

The description has only 9 characters of headroom, so add the tiebreak to Scope (:35):

> Close cases: "poke holes in" or "question me about" an idea or plan goes to dia-brainstorm, but the same for an argument (reasons given for a conclusion) stays here; the assumptions a plan rests on go to dia-counterplan, but the unstated rule that takes given reasons to a conclusion stays here; a universal claim argued from cases stays here when the user asks how well the reasons support it, and goes to dia-conjecture when they ask for counterexamples or whether it holds in every case.

If probes 12–14 miss, narrow the description triggers as DN:69 says.

### 9. nit: the mapping from tag to slot is unstated

The tags [warrant/backing] and [conclusion] (:44) do not match the slots "warrant", "backing" and "conclusion" (:45). The layout calls the last one "Claim" (:57).

Append to Rule 7:

> A [warrant/backing] question names warrant, or backing if it doubts a stated backing; a [conclusion] question names the claim.

Also replace "conclusion" with "claim" in Rule 7's slot list and in Step 6's tie order.

### 10. nit: two lines each claim to be the last

Parameters (:31) end with the ask-mode offer. Step 7 (:84) ends with the truth line. The template (:56–57) puts the offer last.

Replace the Step 7 sentence with:

> End with one line: whether the claim is true is not decided by this audit (then, if Parameters call for it, the one-line ask-mode offer).

### 11. nit: the example skips mandatory questions

Step 4 (:72) says "Ask the four general questions and those of the scheme", but the example (:107–109) omits both [conclusion] questions. Either add:

> `- [conclusion] Is there a similar company where remote work failed? open`

or label the example "(excerpt)".

### 12. nit: the design note is stale against its own commit

- DN:33 calls the F7a dia-reductio edit "**Open for the parent or owner.**" But `git diff eb7ab54 b30344d -- skills/dia-reductio` shows the "follows strictly" wording, the dia-warrant pointer and the bump to 1.1.0.
- DN:42 says the same about the RI F10 sibling edits, but both landed (dia-brainstorm is now 1.2.0).
- DN:3 cites `report-argumentation.md` and `report-index.md`; the files are `review/argumentation.md` and `review/index.md`.

Fix: change DN:33 to "Applied in the same commit (dia-reductio 1.1.0); P7 re-run open". Change DN:42 to match, and fix the two file names.

## AI-chat risks vs the design note

- **Invented premises:** handled by Rules 2–4 and the pitfall at :140; the disown path needs finding 5.
- **Invented sources:** handled by Rule 5's evidence classes, "own recall is never verified", and source answers only with a tool and on request.
- **Yielding:** the D19 rule is present (:129), but there are two bypasses (findings 4 and 5).
- **Over-reliance:** handled by Rule 1, the closing truth line, "not a proof", ask mode, and "what would strengthen it" being stated as a kind of answer rather than a fact.
- **One model on both sides:** the self-examination line is present (:123).
- **Tool-less chat:** every step runs without tools.
- **Phone screens:** ask-mode turns fit one screen (:115). The one-pass audit scrolls, as dia-reductio's does; the template's "lines, not wide tables" is the right mitigation.

## Summary

No blockers: the applied findings are in the text, the sources support it, and the package rules pass. Before merging to main, fix:
- the internal logic: findings 1–3;
- the yielding bypasses: findings 4–5;
- routing: findings 7–8.

These are SKILL.md edits. While 1.3.0 is unreleased on `next`, AGENTS.md lets dia-warrant stay at 1.0.0.
