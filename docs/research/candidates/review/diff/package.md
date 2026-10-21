Verdict: PASS WITH FIXES

# Package-side review of `next` (b30344d) against `main` (eb7ab54)

Scope: everything outside `skills/dia-{warrant,conjecture,counterplan}/` and their generated copies: docs/spec.md, the dia-reductio and dia-brainstorm description edits, manifests, packaging/, AGENTS.md, tools/package.py, tests, plugins/dia, releases. I read the three new descriptions and bodies only to check routing and that spec §5.8–5.10 matches them. The frozen tree was not modified; everything that writes ran in a copy (`$TMPDIR/copy-pkg`).

## What I ran (copy of the tree)

- `tools/package.py --check`: `ok` for all ten skills, exit 0. Unit tests: 19 OK (1 skipped without PyYAML; it passes with PyYAML, as in CI, check.yml:24). Regenerating left `git status` empty, so plugins/dia, both zips and plugin-release.json (1.3.0) are current.
- `claude plugin validate --strict` passes for plugins/dia (one advisory that predates the branch: the README has no install line) and for the marketplace. Each zip holds exactly the ten skill folders.
- Descriptions (characters): brainstorm 1014, confirm 447, conjecture 1018, counterplan 1008, elenchus 970, iterate 582, negative 1009, reductio 1001, refine 695, warrant 1015, all ≤ 1024. Bodies are ≤ 131 lines. Frontmatter keys are name/description/license/metadata everywhere. Manifest, marketplace and OpenAI listing fields are within their limits; the plugin README has 358 words.
- Description tokens (o200k, descriptions only): 1,219 for the seven at eb7ab54, 1,922 for the ten at b30344d (+58%).
- EXPECTED_IMPLICIT (tools/package.py:87-92), spec §7.3 and the three new openai.yaml files agree: all `true`. The new skill text names no product, and its tool use is conditional.

Mechanically the package is sound. The findings concern the record, the routing, and the repository text that still says seven.

## Findings

### 1. should-fix: D35 does not record what the sibling edits actually changed, and the probes are missing from its "not done" list

Evidence:
- spec.md D35: "dia-reductio and dia-brainstorm get pointers to the new skills (their `metadata.version` bumps)."
- The diff does more than add pointers:
  - dia-reductio: "follows from its premises" became "follows **strictly** from its premises". D23 recorded the old wording as P7-tested: "the description asks whether a position 'holds together or follows from its premises' (P7 re-run at `6882022`: no drop)".
  - dia-brainstorm: dropped "(sharpened, open, or refuted)" and "short"; "For the strict dialogue of Plato's dialogues" became "For Plato's strict dialogue"; "even one that names an idea" became "even one naming an idea". The last is D34's probed wording, which the owner checked on ChatGPT mobile.
- §12.2 P7 says "No drop allowed; on a drop, fix the English wording (L7)". docs/probes.md has no 1.3.0 run (`grep -c dia-warrant docs/probes.md` returns 0). The design notes list probe tables but no results (design/dia-warrant.md:54, dia-conjecture.md:57, dia-counterplan.md:51).
- candidates/README.md:52 required "routing probes with negative cells against every sibling it borders" for each pick.

The D21/D25/D34 fixes survive in substance:
- brainstorm keeps "when the user asks for Socratic dialogue or the Socratic method without asking to brainstorm or for options and a plan, use dia-elenchus instead" (D21) and the make-or-write exclusion (D34). Step 0 at SKILL.md:30 is unchanged.
- reductio keeps its dia-negative and dia-elenchus pointers.
- D25 concerns dia-negative, which was not touched.

The tested strings did change, though, and the change is not on record.

Replace in D35:
"Routing: each new description carries exclusion sentences toward its bordering siblings; dia-reductio and dia-brainstorm get pointers to the new skills (their `metadata.version` bumps). Not done in this decision: dia-hypothesis, dia-commit, the munāẓara pushback rule (separate batch), the site's skill plates."
with:
"Routing: each new description carries exclusion sentences toward its bordering siblings. Sibling edits (index review F10): dia-reductio 1.1.0 asks whether a position 'holds together or follows strictly from its premises' (D23 had 'follows from') and points to dia-warrant and dia-conjecture; dia-brainstorm 1.2.0 points to dia-counterplan and, to stay within 1,024 characters, drops the verdict names and 'short' and shortens two phrases ('For Plato's strict dialogue', 'even one naming an idea'), with no rule change. The ten descriptions total 1,922 o200k tokens (1,219 for the seven). Not done in this decision: the routing probes in the three design notes and a P7 re-run for dia-reductio and dia-brainstorm (required before `main`); README (four languages) and the site; dia-hypothesis, dia-commit, the munāẓara pushback rule (separate batch)."

### 2. should-fix: the "recommended pick in each cluster" basis in D35 ignores the index review's high finding

Evidence:
- D35: "the owner took the recommended pick in each cluster".
- review/index.md F7 (high): cluster 2 is "mis-framed"; the correction is "Move dia-conjecture to cluster 4 ('distinct')" and "Make cluster 2 an explicit choice between dia-defend and dia-munazara, or neither".
- candidates/README.md was not changed in this diff. It still frames dia-conjecture inside cluster 2, and :15 still says "The documents have **not** had an independent review yet."

Replace "the owner took the recommended pick in each cluster" with:
"the owner picked dia-warrant (cluster 1) and dia-counterplan (cluster 3), and dia-conjecture, which the index review (F7) moved out of cluster 2 into the distinct candidates; cluster 2 (dia-munazara, dia-defend) was not picked".

In candidates/README.md:15, replace "The documents have **not** had an independent review yet." with:
"Each document was reviewed independently on 2026-10-21 (`review/`, all SOUND WITH FIXES); the corrections were applied in `design/`, not in these documents."

### 3. should-fix: spec sections that D35 did not update

- §5.3 (spec.md:151-153) still says "Behavior: the reference, amended by D19–D34." and "Cross-reference: points to dia-elenchus."
  Replace with "Behavior: the reference, amended by D19–D35." and "Cross-reference: points to dia-elenchus, and to dia-counterplan (D35)."
- §5.4 (spec.md:166): "Cross-references: the description and body point to dia-negative and dia-elenchus." The body was already wrong before this branch: `grep -n "dia-negative\|dia-elenchus" skills/dia-reductio/SKILL.md` matches only line 3, the description. The line now also misses the new pointers.
  Replace with "Cross-references: the description points to dia-negative, dia-elenchus and, since D35, dia-warrant and dia-conjecture; the body has no pointers."
- §8 (spec.md:347): "├── skills/                         source: seven plain skills". Change "seven" to "ten".
- §12.2 P1 (spec.md:449): "Accepted; seven skills listed as `dia:dia-<x>`". Replace with "Accepted; every skill in §4 listed as `dia:dia-<x>`".
- §12.2 P7 (spec.md:455): "Korean and English prompts for reductio, negative dialectics, elenchus and brainstorm." Append: "From 1.3.0 (D35) also the routing tables in `docs/research/candidates/design/dia-*.md`, with negative cells against every bordering sibling."
- §1, G1, D1, §4, §5.8–5.10 and §7.3 match the skills: each border list and each §7.3 reason names the siblings in that skill's exclusion clauses.

### 4. should-fix: the design notes say the sibling edits were not done, but this commit does them

Evidence:
- design/dia-warrant.md:33: "That edit, its version bump and a P7 re-run are outside this task's paths. **Open for the parent or owner.**"
- design/dia-warrant.md:42: "Not done here (outside this task's paths): the sibling edits F10 lists for dia-reductio and dia-brainstorm, and the P7 negative cells for every pair."
- design/dia-conjecture.md:50: "Not done here: the sibling edits F10 lists (dia-reductio 'follows strictly', dia-brainstorm's pointers)".
- design/dia-counterplan.md:38: "Not done here: dia-brainstorm's description should gain a pointer to dia-counterplan".
- All of these edits are in b30344d (skills/dia-reductio/SKILL.md:3, skills/dia-brainstorm/SKILL.md:3).

Add one line under each note's review section:
"Batch owner, same commit: dia-reductio 1.1.0 now says 'follows strictly from its premises' and points to dia-warrant and dia-conjecture; dia-brainstorm 1.2.0 points to dia-counterplan. Still open: the probes below and the P7 re-run."
For dia-conjecture.md:50, also add: "dia-brainstorm has no pointer to dia-conjecture (see the package review, finding 9)."

Nit in the same files: dia-warrant.md:3 and dia-conjecture.md:33/:47 cite `report-argumentation.md`, `report-index.md` and `report-modern-dialectic.md`. No such files exist in the repo; the reviews are `review/argumentation.md`, `review/index.md` and `review/modern-dialectic.md`. Only dia-counterplan.md:3 says "copies in `docs/research/candidates/review/`". Replace each `report-<x>.md` with `review/<x>.md`.

### 5. should-fix: docs/handoff.md was not updated

Evidence:
- handoff.md:7 still says "Plugin `dia` **1.2.1**…" and "1.2.0 … made all seven skills visible".
- The "latest release" line still says `v1.2.1`; that is correct for `main`, but the handoff has no word about `next`.
- Item 17: "Candidate methods for new skills: researched 2026-10-21, not reviewed | agent: independent review; owner: picks".

Add a State bullet:
"- Branch `next` holds plugin `dia` **1.3.0** (spec D35): dia-warrant, dia-conjecture and dia-counterplan, plus pointers in dia-reductio 1.1.0 and dia-brainstorm 1.2.0. Not on `main` until the owner approves. Before the merge: the routing probes in the three design notes, a P7 re-run for dia-reductio and dia-brainstorm, the README in four languages and the site."

Replace item 17's status with:
"reviewed 2026-10-21 (`docs/research/candidates/review/`); three picks implemented on `next` (D35); probes pending | agent: probes; owner: approve merge".

### 6. should-fix: places that still say "seven" or list only seven skills (reported, not fixed)

User-facing; update before the merge to `main`:
- README.md: :7 "Seven reasoning-and-review skills"; :9-17 the skill table (7 rows); :66 "Seven entries, `dia:dia-brainstorm` to `dia:dia-refine`". Sorted by name, ten skills end at `dia:dia-warrant`, so the range is wrong too. Also :115 (the "in words" list names four skills), :127 (the implicit-start list), :131-136 (Options lacks warrant's `--target`/`--mode` and counterplan's `--target`), :145-154 (the "Pick a skill" table) and :156-341 (the guide has 7 sections).
- README.ko.md :7, :66; README.ja.md :7, :66; README.zh-CN.md :7, :66; each has the same 7-row tables.
- site/index.html: :8, :9, :15, :23 (title and meta), :54, :57, :89, :97 ("Seven skills"), :100-108 (the 7-item "wants" list), :381 (the same "/dia" range as README :66). D35 defers only the plates.
- docs/site/PRODUCT.md:22, :27-28 (lists the seven names); docs/site/DESIGN.md:3, :215 (the plates, deferred).
- docs/spec.md:347, :449 (finding 3); docs/handoff.md:7 (finding 5).

Dated records, fine as they are: directory-submission.md:46 ("at 1.1.0"; its "longest identity" row is now `dia:dia-counterplan`, 19 characters, still ≤ 64); token-cost.md:21-25 (needs a 1.3.0 row, see finding 1); probes.md, skill-effect.md:53, and spec D18/D33/O3.

### 7. should-fix (routing): "does my conclusion follow from these reasons?" is now claimed by two skills, and that cell is untested

Evidence:
- reductio: "wants to know whether a position holds together or follows strictly from its premises".
- warrant: "Use when the user asks how well reasons support a conclusion … For a strict contradiction or a deductive step use dia-reductio".

The two exclusion clauses agree with each other (deductive goes to reductio, probable to warrant). But ordinary requests rarely say "strictly", and the reductio trigger that P7 tested was changed (finding 1). Concrete requests that fall between them:
- "Does my conclusion follow from what I said?"
- "Check my argument"; reductio's `user` target is "a claim, belief, plan or argument the user states" (reductio SKILL.md:21).

Warrant's probe cell 5 covers only the explicit Korean "연역적으로 엄밀하게" ("deductively, strictly"). Add a plain cell to the P7 re-run: "Does my conclusion follow from my premises? [three premises and a conclusion]", expected dia-reductio, with dia-warrant as a negative cell.

### 8. should-fix (routing and record): devil's advocate goes to dia-counterplan, but the counterplan theory note says the critic role stays with dia-brainstorm

Evidence:
- brainstorm (new): "For a counterplan or devil's advocate on a plan, use dia-counterplan."
- counterplan: "Use when the user asks for a counterplan or a devil's advocate on a plan or decision". Its Rule 1 says "do not carp … it is not a list of the plan's flaws".
- counterplan theory.md:34: "the critic's role is already played by dia-brainstorm's stress mode".
- design/dia-counterplan.md:38: "resolved by having no DA mode (the critic role stays with dia-brainstorm's stress mode)".

The two descriptions point the same way, so they do not collide. The record, however, says the critic role stays with brainstorm, while every "devil's advocate on my plan" request now reaches a skill that refuses to critique and writes a full counterplan instead. theory.md:28 records that the evidence favours DA over DI on performance. The routing is defensible, since A-F7(c) limited the trigger to plans, but it should be stated where it is decided.

Add to D35 (or to theory.md:34, which belongs to the new-skill review):
"A request for a devil's advocate on a plan is answered with dialectical inquiry (a counterplan), not with devil's-advocacy critique; critique by questions stays with dia-brainstorm's stress mode."

### 9. nit (routing): dia-brainstorm's body has no fallback toward dia-counterplan or dia-conjecture

Evidence:
- brainstorm Step 0 has misroute fallbacks for make-or-write requests (:30) and for general "Socratic" requests (:39), but none for the new borders. Its stress mode "hunt[s] for counterexamples" (:34).
- Example requests: "Play devil's advocate on my café plan" if brainstorm is chosen anyway; "Poke holes in my rule that every pure function can be memoized". Conjecture's description sends "poke holes" to brainstorm, but brainstorm then runs Paul-style probes on a universal claim with no hint that dia-conjecture exists.
- dia-counterplan does have the reverse fallback (counterplan SKILL.md:34).
- The description has 10 characters left, so the body is the place. 1.2.0 is unreleased, so no extra bump is needed.

Insert after brainstorm SKILL.md:39:
"If the request asks for the opposing plan, a counterplan or a devil's advocate on a plan, it belongs to dia-counterplan; if it asks for counterexamples to a claim about every case (all, always, never), it belongs to dia-conjecture. If this skill was chosen anyway, add one line to that same message naming that skill, then continue."

### 10. nit (routing): collisions with no probe cell

- "Check the reasoning in your last answer": dia-refine ("recheck … the previous answer", "logical leaps"), dia-warrant ("an earlier answer") and dia-reductio (`--target=claude`) all claim it. Refine points to neither of the others. Add this as a P7 cell.
- "Our team rule: never deploy on Fridays. Does it hold in every case?": conjecture's description takes "a rule" with "never", but its Step 0 (:47) excludes "a plan, policy, decision". Suggested description wording (new-skill scope; it needs a matching cut): "a rule or generalization about what is the case (not a policy to adopt)".
- "What are the hidden assumptions in my plan?": goes to counterplan, which always writes the full counterplan. design/dia-counterplan.md:49 lists this as open; carry it into D35.
- "Assume every prime is odd and show where it breaks": reductio's own trigger, used on an all-claim. Either answer is defensible; add the cell so the outcome is known.

### 11. nit: OpenAI capability line gives the repair to the assistant

packaging/openai/interface.json: "Test a universal claim by counterexamples and repair it (Lakatos)". The skill says "The user … picks every repair" (conjecture SKILL.md:24), and the longDescription in the same file says "repairs it with you".
Replace with: "Test a universal claim by counterexamples; you pick the repair (Lakatos)".

### 12. nit: the test name promises a spec check

tests/test_package.py:38 `test_skills_match_spec_names` compares the folders with `pkg.EXPECTED_IMPLICIT`, not with spec §4; I checked the spec tables by hand and they agree. Rename it to `test_skills_match_expected_table`, or parse the names in spec §4's table.

## Checks outside this scope, or with nothing found

- Checks 1 and 3 (applied findings, fidelity) belong to the new-skill reviews. Spec §5.8–5.10 and the packaging summaries match the bodies, apart from finding 11.
- Check 4 at package level: the packaging text keeps the no-verdict and user-decides framing and overstates nothing.
- Check 6: no Hangul in skills/; limits pass. warrant and counterplan read their templates only "if you can open it" and keep the record fields in the body (warrant :84, counterplan :91). The packaging is assistant-neutral, and AGENTS.md says "ten". The manifests are identical (1.3.0). The bumps (plugin 1.3.0, reductio 1.1.0, brainstorm 1.2.0, new skills 1.0.0) pass the digest rule.
