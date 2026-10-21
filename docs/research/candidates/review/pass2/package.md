Verdict: PASS WITH FIXES

# Package review, second pass: `next` b30344d → 275e1aa

The frozen tree was left untouched. Everything that writes ran in a copy (`$TMPDIR/copy2`).

Mechanics on 275e1aa:
- `package.py --check`: ok for ten skills. Tests: 19 OK (the PyYAML skip passes under `uv run --with pyyaml`). Regenerating leaves `git status` empty. `claude plugin validate --strict` passes for the plugin and the marketplace.
- Descriptions: warrant 1015, conjecture 1020, counterplan 1019, brainstorm 1014 characters. Tokens: 1,924 o200k now; D35's 1,922 is stated "at `b30344d`", so it holds.
- The probe trees base, var and var2 are byte-identical to `plugins/dia` at eb7ab54, b30344d and 283f6fa. var2 is the shipping build (no skill change after 283f6fa). An empty `CODEX_HOME` resolves to `gpt-6.1-sol`, as Part O says.

## Status of first-pass findings

1. D35 record and missing probes: **fixed.** D35 records the sibling edits, the DA sentence and the token count. Part O's reductio and brainstorm sibling cells against `main` cover the P7 re-run in substance. Stale "open" lines remain (new finding 2).
2. "Recommended pick in each cluster": **partly fixed.** D35 and candidates/README.md:16 are fixed. Still wrong: candidates/README.md:33 lists `dia-conjecture` inside cluster 2, with "(rules, policies, generalizations)" (new finding 4).
3. Spec sections: **fixed.** §5.3, §5.4, §8, P1 and P7 all use my text. §5.3 is now one pointer short (new finding 7).
4. Design notes: **fixed** (F7a, F10, I-F8, D-F13 updated; `report-*.md` renamed; counterplan.md:3 keeps the old names with "copies in `review/`", acceptable).
5. Handoff: **fixed, then overtaken** by 275e1aa (new finding 2).
6. "Seven" leftovers: **fixed in all four READMEs** (intro, `/dia` range, invoke lists, Options, tables, guide). The site is **deliberately left**, and soundly: D35 lists it as not done and the handoff tracks it. Layout lines remain (new finding 8).
7. Untested reductio/warrant cell: **fixed.** Cell `r-follow` ran and loaded no skill in any arm on either engine.
8. DA on a plan: **fixed** (D35 and counterplan theory.md §4).
9. Brainstorm Step 0 fallback: **fixed** with my text verbatim (skills/dia-brainstorm/SKILL.md:41).
10. Collisions: **fixed.** The cells ran, and the conjecture description says "(not a policy to adopt)". The hidden-assumptions request was settled in counterplan D-F12, not in D35, which is acceptable.
11. Interface capability line: **fixed.**
12. Test name: **fixed** (`test_skills_match_expected_table`).

## Part O against the JSON files

My own re-tally of all 499 run files (`out`, `out2`; none `@synced`; both var listings show ten skills) **matches every count in both tables**. One parenthesis is wrong (new finding 3), and the reading bullets overstate (new finding 1).

## New findings

### 1. should-fix: Part O's reading overstates coverage, and the fallacy-trigger condition is met but not acted on

- Bullet 1 says "Every positive cell for the three new skills loads its skill on both engines except the Korean startup-survival claim". That is true only for the first table. In the boundary table the cells expected to load a new skill miss on Claude var2:
  - fallacy question: 0/3 (Codex 0/2)
  - "poke holes in my argument": brainstorm 3/3
  - hidden assumptions behind an argument: 0/3
  - "poke holes in my claim that every…": 0/3 (Codex 1/2)
  - all-users churn: 1/3 (Codex 0/2)
- Bullet 3 calls the no-skill answers "pre-existing behaviour". For the fallacy question that is meaningless, since base has no dia-warrant. design/dia-warrant.md (Index F6): "add the trigger only if probe cell 11 shows that 'is this a fallacy' requests are lost". Cell 11 is lost on both engines (0/5); no decision is recorded.
- Bullet 2 says "base and var2 agree on every sibling and no-skill cell". The Codex deductive-check cell went from 0/1 to 2/2.

Replace bullet 1 with:
"- Every positive cell in the first table loads its skill on both engines except the Korean startup-survival claim on Claude (0/3; a bare factual claim with no stated reasons, answered directly; Codex 2/2). The design note did not widen the description for it. Boundary cells that expect a new skill mostly miss on Claude: the fallacy question (0/3; Codex 0/2), \"poke holes in my argument\" (dia-brainstorm 3/3), the hidden assumptions behind an argument (0/3; Codex 2/2), \"poke holes in my claim that every …\" (0/3; Codex 1/2) and the all-users churn argument (1/3; Codex 0/2)."

Replace bullet 2 with:
"- No regression on the siblings: no sibling or no-skill cell does worse in var2 than in base (the Codex deductive-check cell improved, 0/1 to 2/2)."

Replace bullet 3 with:
"- On Claude, the short checks (the proof, the invalid syllogism, \"check your last answer\") load no skill in either arm, so the new descriptions took nothing from a sibling. The fallacy question (dia-warrant design note, cell 11) is lost on both engines (0/5). That meets the condition the design note set for adding a \"fallacy\" trigger. It is not added because the description is 9 characters under the cap; the decision is the owner's."

### 2. should-fix: "open" and "before the merge" lines that 275e1aa has overtaken

- handoff.md:10: "Before the merge: the diff-review fixes and their re-probe (probes Part O), the README in four languages, and the site text." Replace with:
  "Before the merge: the site text and plates, and the owner's call on the routing gaps in probes Part O (the fallacy question; boundary cells Claude answers directly)."
- Handoff item 17 status: replace "agent: fixes, re-probe; owner: approve merge" with:
  "diff-reviewed and re-probed (probes Part O), README updated | agent: site; owner: Part O gaps, approve merge".
- design/dia-warrant.md: "Cells 11–14 and the re-probe after the fixes (probes Part O) are open." and "Running 11–14 and the post-fix re-probe is open." Cells 11–13 ran. **Cell 14 did not**: Part O's "Check the reasoning in your last answer: …" is my F10 cell, marked "informative", not cell 14 ("Does the reasoning in your last answer actually support its conclusion?", expected dia-warrant). Cell 6 (the natural-language dia-refine negative) also did not run. Part O's refine cell is the first-word `dia-refine — check the numbers`. Replace both sentences with:
  "Cells 11–13 and the post-fix re-probe ran in probes Part O; cells 6 and 14 (the dia-refine border in plain words, and target claude) have not been run."
- design/dia-conjecture.md: "Rows 11-16 were added after that run and are not yet run." and ":50 Still open: the P7 re-run." Rows 11–16 ran in Part O. Replace with:
  "Rows 11-16 ran in probes Part O (var2); rows 12 and 15 remain owner decisions (Codex loads dia-conjecture for row 12, 2/2)."
- design/dia-counterplan.md last line: "Cell 7 on Codex needs a re-probe." Replace with:
  "Re-probed in probes Part O: cell 7 loads no skill on Codex var2 (0/2)."
- spec P7 says the routing tables run "with negative cells against every bordering sibling (probes Part O)". The dia-warrant/dia-refine border has no natural-language cell. Either run warrant cells 6 and 14, or append to P7: "(the dia-warrant/dia-refine border is covered only by a first-word cell)".

### 3. nit: wrong parenthesis in the Part O counterplan row

"Codex var: 8/8 (one run also read dia-brainstorm)" is wrong. Every Codex var counterplan run read only dia-counterplan. The dia-brainstorm read was the **Codex base** run of `p-assume` (`out/cx-base-p-assume-1.json`).
Replace the two cells with: Codex base "0/4 (one run read dia-brainstorm)", Codex var "8/8".

### 4. should-fix: candidates/README.md:33 still contradicts D35 and the conjecture description

Cluster 2 lists `dia-conjecture` and gives its object as "(rules, policies, generalizations)". The skill now says "not a policy to adopt". Append to item 2:
"(The index review, F7, moved `dia-conjecture` out of this cluster into the distinct candidates, where D35 picked it; its object is a rule or generalization about what is the case, not a policy.)"

### 5. should-fix: a README counterplan tip promises behaviour the skill does not define

README.md (and the three translations), dia-counterplan Tips: "If you only lean one way, say so. The record keeps it as a leaning (\"counterplan held (leaning)\"), not as a settled view."

Step 7 allows plan's / counterplan's / own words / "can't tell"; there is no "leaning". The two real runs disagree:
- out-283-a: "K2/C2 commute: counterplan held (leaning)."
- out-283-b: "Commute (K2/C2): Open, leaning counterplan."

Replace with:
"- If you only lean one way, say so. The skill has no separate \"leaning\" ruling, so the record may count it as held with a note or as open with the lean noted; say \"can't tell\" if you want the pair kept open."

### 6. Session fidelity (real runs on 283f6fa)

The README excerpts quote run a faithfully (every quoted line checked against `turns[].text`). Departures from the skill text:

- **should-fix (skill, conjecture):** out-283-a turn 6, option 2: "C″ would be 'bulk saves money if the bulk price is lower than what I'd otherwise have paid for the amount I actually use'". The counting case meets this condition: 24 bars cost $9.60 against $12.00 at the small-box price, yet the user lost $6.60. That breaks Step 5: "Never offer a C′ whose condition the counting case meets." The README elides this option, so the README is unaffected. Route it to the conjecture owner.
- **nit (counterplan):** out-283-a has "A5 [T]: Good reviews mean the school is good for your kids", which the user never stated, and A1 [T] is not a quote. Step 2: "[T] stated by the target (quote it)". Both runs put a paraphrase in quotation marks as the Step 1 quote.
- **nit (counterplan):** out-283-a turn 1 adds K6, making six key assumptions (Step 3 caps at five). It also records "K6/C6 space: plan held" although C6 was never put to the user. The README excerpt shows this line.
- **nit (warrant):** out-283-a: "A personal trainer knows exercise practice. Orthopedics and sports medicine are a different field" carries no evidence class (Rule 5). The README quotes it; run b avoids it.

### 7. nit: spec details behind the fixes

- §5.3: replace "points to dia-elenchus, and to dia-counterplan (D35)" with
  "points to dia-elenchus, to dia-counterplan (description and Step 0) and to dia-conjecture (Step 0 only) (D35)".
- §5.9 Borders: replace "plans and decisions go to dia-counterplan or dia-brainstorm" with
  "plans, policies, decisions and ideas go to dia-counterplan, dia-brainstorm or dia-negative (C is a rule or generalization about what is the case, not a policy to adopt)".
- §5.9 Purpose: after "lemma-incorporation" add ", and the deeper-proof move of section 6a".

### 8. nit: README leftovers (all four languages)

- dia-conjecture Tips: "\"open\" means a case counted and no repair was picked". Replace with:
  "\"open\" means a case is disputed, or a case counted and no repair was picked" (skill Step 6).
- Repository layout: change "material the skills were rebuilt from" to "material the seven original skills were rebuilt from".
- Repository layout: change "measured token cost per skill" to "measured token cost (the seven 1.2.x skills)".
- Repository layout: change "each skill against no skill, blind-judged" to "the seven 1.2.x skills against no skill, blind-judged".

No regressions in packaging, manifests, zips or tests. The brainstorm fallback contradicts neither its description nor the sibling exclusions.
