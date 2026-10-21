Verdict: PASS WITH FIXES

# Second-pass review: skills/dia-conjecture (next 275e1aa; first pass at b30344d)

Line numbers are from `skills/dia-conjecture/SKILL.md` at 275e1aa unless another file is named.

What I ran, in a scratch `cp -r` copy:
- `package.py --check`: ok. `unittest`: 19 OK (skipped 1).
- The source and `plugins/dia/` copies of dia-conjecture and dia-brainstorm are identical.
- Description 1,020 characters.
- o200k tokens for the descriptions: 1,922 at b30344d, 1,924 now.
- CUP contents re-fetched: §6 is "Return to criticism of the proof by counterexamples which are local but not global", with 6a "Increasing content by deeper proofs".
- Part O transcripts (`~/work/dia-review/new-skills-2026-10-21/out*/`) re-tallied; every dia-conjecture count matches.
- Both example sessions read in full.

## First-pass findings

1. Monster-barring: **fixed** (lines 83-85). theory §4-5 agree. Wording drift: N2.
2. Rule 4 in the Claim line: **fixed** (line 117). Edge case: N1.
3. Deeper proof: **partly fixed, and partly my own error**.
   - The local-only widening (line 93) is correct, and it is §6.
   - The global-case "deeper proof" (line 96) came from my replacement text. It is not from §6, and in practice it collapses into restating B (S1). I withdraw that attribution.
4. Overlapping results: **fixed** (lines 106-112).
5. "policies": **fixed in the text** (description, line 14, theory §5).
   - Routing is only partly fixed: the refund cell still loads dia-conjecture (Claude 2/3, Codex 1/2).
   - Part O's reason is sound: both Claude runs say they read the prompt as a claim about what happens.
   - Design-note row 13 still expects dia-negative (N4).
6. Routing probes and the stale decline: **fixed**. Rows 11-16 were added and run, line 30 was replaced, and a brainstorm body fallback was added. The gap is real (row 11: 0/3 Claude) and is left to the owner, but it is not recorded (S3).
7. Monster-adjustment source: **fixed** (theory:27).
8. Worked example: **fixed**.
9. Two asks after round three: **fixed** (line 104; consistent with line 20).
10. Both-sides paths: **fixed** (lines 53, 61, 94). Session b, turn 6 follows line 94: "Picking option 1 or 2 below accepts L5."
11. Label: **fixed** (line 14). The 6a scope is wrong for the global case (S1).
12. Citations: **fixed**.
13. Case order: **fixed**. Both sessions aim case 1 at the suspect lemma.

Declined: none, as the design note says.

## New findings

### S1. should-fix: the global "deeper proof" is mislabelled §6 and collapses into restating B

Evidence:
- Line 96 and theory:34 attribute "for a global case, a weaker condition …" to 6a. But §6 concerns local-not-global counterexamples. A weaker lemma for a global case is Rule 2's "a suitable lemma".
- Nothing stops the "weaker condition" from simply being B. SEP's warning about an "empty tautology" sits only in theory.md.
- All four repair menus in the sessions offer a near-tautology:
  - a, turn 4, recommended: "comes close to restating what 'saves money' means"
  - b, turn 4, recommended: "nearly restates 'you spend less'"
  - b, turn 6: "whenever the extra charges are smaller than the unit-price savings"
- Line 96 is violated outright in a, turn 6, option 2: "bulk saves money if the bulk price is lower than what I'd otherwise have paid for the amount I actually use". The counting case meets that condition (24 bars at $9.60 against 24 × $0.50 = $12.00), so that C″ is refuted by the very case it answers. No check was shown.

Replace line 96 with:

```
- **Weaker lemma** (Rule 2's "a suitable lemma"), where you can find one: for a global case, a weaker lemma than the one you would build in, one the proof can still use, that the counting case fails and that more of C's other cases meet, so that C′ keeps more of C's content. Show in one line that the counting case fails it. Never offer a condition the counting case meets (that case is an A that is not B), or one that only restates B ("every A that ends up B is B"): that keeps C true by emptying it, the "empty tautology" Lakatos's critics warn of, and is not a repair.
```

In line 117, replace "deeper proof," with "weaker lemma, deeper proof,".

In theory:34, replace the sentence beginning "SKILL.md uses only this deeper-proof move (6a)" with:

```
SKILL.md uses this deeper-proof move (6a) in one place: for a local case against a lemma already built into C, a replacement lemma that widens the revised claim. For a global case it also offers a weaker lemma to build in than the one first named; that is the skill's reading of Rule 2's "a suitable lemma", not section 6.
```

Add to Pitfalls:

```
- **Empty repairs:** a condition that restates B ("saves money when it costs less") keeps C true by emptying it. Do not offer it.
```

### S2. should-fix: Step 0 admits a universally worded policy, and Part O says it doesn't

Evidence:
- Line 44 says "stop unless the user restates it as universal". Probe 16 is already universal ("never deploy on Fridays. Does it hold in every case?"), and it contains the description's trigger "does this hold in every case".
- `out2/cc-var2-c-neg-friday-2.json` loaded the skill and did not stop: "A rule is a policy, not a statement about what is the case. To test it with counterexamples, I'll read it as the strictly universal claim below. C (in my words): every deploy made on a Friday is a mistake." It then went on to Step 1.
- Part O says "Step 0 sends a policy to adopt elsewhere". The one run that tested this contradicts it.

Replace line 44 with:

```
Take only a claim about every member of a class that says what is the case. A rule about what to do ("never deploy on Fridays", "every refund must be approved within a day") is a policy even when worded with all, every or never, or asked as "does it hold in every case". Otherwise say in one line where it fits, and stop unless the user restates it as a claim about what is the case (for example "every Friday deploy fails more often than other deploys"); do not restate it that way yourself:
```

In Part O, replace "Step 0 sends a policy to adopt elsewhere." with:

```
In the one Friday run that loaded dia-conjecture, Step 0 did not stop: the assistant recast the rule as 'every deploy made on a Friday is a mistake' and continued; Step 0 is tightened for this.
```

### S3. should-fix (docs): Part O and the design note misstate the dia-conjecture boundary results

- Part O, Reading: "Every positive cell for the three new skills loads its skill on both engines except the Korean startup-survival claim". This is false for the boundary table: the dia-conjecture cell "Poke holes in my claim that every microservice …" gets 0/3 on Claude and 1/2 on Codex, and two warrant cells also miss on Claude.
  - Change the opening to "Every positive cell in the first table …".
  - Add: "In the boundary table, dia-conjecture's own cell ('Poke holes in my claim that every microservice …') goes to dia-brainstorm or no skill on Claude (0/3) and splits on Codex (1/2); dia-brainstorm's description has no pointer to dia-conjecture (owner decision)."
- Design note: "Rows 11-16 were added after that run and are not yet run." This is stale. Replace with "Rows 11-16 were run on 283f6fa: probes Part O, boundary table."
- Design note, F1 line: "local only (Rule 4, C unchanged)". This is stale. Replace with "local only (Rule 4; C unchanged unless the lemma was built into C, then a deeper proof widens C′)".

### Nits

N1. Line 117, "a Rule 4 lemma replacement goes under Proof-analysis, not here": replacing a built-in lemma does change C′ (line 93). Append ", unless it widens C′ (then the reason is deeper proof)".

N2. Hard rule 2 (line 31) still says "in C's stated terms", while Step 4 anchors on "the reading of C fixed in Step 1". Replace "(it is an A, in C's stated terms)" with "(it is an A, under the reading of C fixed in Step 1)".

N3. dia-brainstorm:41 sends "counterexamples to a claim about every case (all, always, never)" to dia-conjecture, so a Friday-style policy would bounce back and forth. Replace that phrase with "counterexamples to a claim about what is the case for every member of a class (all, always, never; not a policy)".

N4. Design-note row 13 expects "dia-negative (policy; negative for dia-conjecture)". Part O calls dia-conjecture defensible, and dia-negative loads in no arm. Change the expected value to "dia-conjecture acceptable (read as a claim about what happens)".

N5. The design note's diff-review list omits one description edit: "checked condition by condition" became "each with its check". Add it to the "5 applied" line. Hard rule 2 still requires condition by condition.

N6. Row 12 ("game" definition) is still "owner to decide". Step 0's "what a word means: dia-elenchus" already decides it de facto.
- Codex var2 read dia-conjecture in 2/2 runs, but both runs ignored the skill: one bulleted list of four counterexamples, against hard rule 1, with no Step 1.
- Part O's "dia-conjecture 2/2" therefore counts reads, not runs that followed the skill. Say so, or record the decision.

N7. Spec D35, "(1,219 for the seven)": the seven total 1,249 at b30344d; 1,219 is their total at main eb7ab54. Write "(1,219 for the seven at eb7ab54)".

N8. Spec §5.9 is stale against the fixed skill:
- Its "At most three rounds" contradicts line 104, which continues on request. Write "up to three rounds, then an offer to stop; continues on request".
- Add "and the deeper-proof move of section 6a" to the repairs.
- The borders should read "plans, policies and decisions go to dia-counterplan, dia-brainstorm or dia-negative".
- §5.3 should add "and, in the body, dia-conjecture".

## Example sessions vs the skill text

Followed:
- Whose claim is stated in the first line, and Step 1 restates C "in my words" and asks one thing.
- Lemmas are tagged [T]/[A], the suspect lemma is marked, and the user is asked to correct.
- The prior criterion gets its own message.
- One case per message, with a check and "rests on" (b separates invented numbers from recall).
- Every repair menu is numbered and ends with one ask.
- Definition changes are recorded with old, new and what was lost. Session b, turn 5, handles an "I meant" correctly: "what I really meant in the first place" → "I'm marking it as one rather than as a clarification".
- Neither run reaches the record, so Step 6 is untested.

Violations:
- a, turn 6, option 2 is met by the counting case (S1, line 96).
- b, turn 6: "Your fee case still fails this condition ($60 against $38 saved)". The unit-price saving was $222 − $200 = $22; $38 is the net loss. The conclusion still holds, but the check's figure is wrong. This is a model error, which S1's one-line check would expose.
- b, turn 5: "Is it a bulk purchase at a lower price per unit? Yes." This asserts the antecedent without giving a reason (hard rule 2). Minor.
- a, turn 1, L3 [A]: the reason given, "because your argument needs it", is not a one-line reason (Step 2). Minor.

## Claims checked

True:
- Description 1,020 characters.
- Body 125 lines (same counting as at b30344d).
- Items 1-13 and package findings 4 and 10 are applied as described.
- dia-brainstorm description at 1,014; no version bump, with the reason given.
- D35: the brainstorm Step 0 fallback (line 41) and the reductio pointer exist; the 1,922 total holds.
- Part O: all dia-conjecture counts; "within 10 characters of the cap" (1,015 / 1,020 / 1,019).

False or stale:
- Part O: the positive-cell bullet and the Step 0 bullet (S2, S3).
- Design note: "not yet run" and the F1 line (S3), row 13 (N4), the missing edit (N5).
- D35: the 1,219 figure (N7).
- Spec §5.9 and §5.3 (N8).
