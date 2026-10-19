Verdict: PASS WITH FIXES

Scope: dia-reductio at 395098a, checked against my first-pass report on 7115d2a. I re-read SKILL.md, output-template.md and theory.md in full, plus spec D19–D21, docs/probes.md, docs/research/README.md and handoff item 9. Line numbers refer to 395098a.

Checks:
- `python3 tools/package.py --check`: "ok" for all seven skills, exit 0.
- `python3 -m unittest discover -s tests`: 13 tests, OK (skipped=1), exit 0.
- SKILL.md is 134 lines. The description is 824 characters and unchanged.
- No Hangul and no product names in any dia-reductio file; `claude` appears only as the D14 target value.
- `diff -r` against plugins/dia/skills/dia-reductio: identical.
- New Sources URLs: both return 200. The SEP page discusses Duhem, and the ditext page has Quine's §VI.
- dia-reductio is not one of the skills whose descriptions changed for routing. Its pointer to dia-elenchus (SKILL.md:3) still fits the new dia-elenchus and dia-brainstorm descriptions, and neither of those claims contradiction or proof requests.

Per-finding status

| # | Status | Evidence |
|---|---|---|
| 1 options for "premise set inconsistent" | fixed | SKILL.md:79 matches the proposed text and SKILL.md:100 excludes T; recorded in spec.md:66 (D21). Logic: S_A entails not-T and S_B entails T, so the inconsistent set is S_A ∪ S_B. Correct. |
| 2 key-term meanings had no label | fixed (nit 3) | SKILL.md:63 and template:18 now label them. |
| 3 existence premise passed as [L] | fixed | SKILL.md:33 |
| 4 template and text were refute-only (M1) | partly | Fixed: template:20, :21, :27, :30 and SKILL.md:38, :112. Still refute-only: Step 6 (SKILL.md:100) and the template's Options block (template:36, :38). See finding 1. |
| 5 Duhem–Quine sources missing | fixed | theory.md:71-72 |
| 6 "verified this session" undefined | fixed | SKILL.md:34, template:17 |
| 7 "consistent" pitfall missing | fixed | SKILL.md:133 |
| 8 doc drift | partly | (b) fixed at spec.md:64. (d) fixed at handoff.md:27; "§ Still open" exists at research/README.md:50. (a) not fixed: spec.md:65-66 still omit the Step 4 letter-substitution reread (SKILL.md:67) and the own-scheme label (SKILL.md:81). (c) not fixed: research/README.md:53 still lists reductio F10 as open although it is applied at SKILL.md:81, and review F8 and M5–M7 are still listed nowhere. These do not count as deliberately left, because research/README.md:48 says every diff-review finding was applied "including their nits". |

D21 and probes claims vs the files
- D21's dia-reductio clause (spec.md:66):
  - "premise set inconsistent" options: holds (SKILL.md:79, :100).
  - Labels on key terms and existence premises: holds (SKILL.md:33, :63; template:18).
  - Duhem–Quine sources: holds (theory.md:71-72).
  - "grades and the template work when proving": partly. The grades (SKILL.md:73-77) and the template's Derivation and Contradiction blocks now work when proving. The Options block does not (finding 1).
- probes.md:74 reports reductio routing at 2/2 in every cell at 7115d2a. The description has not changed since then, so the result still stands. I did not re-run it, because the claude CLI is out of scope.
- probes.md:84 pushback: the reported behaviour matches SKILL.md:124. The paragraph names no commit (finding 4).

New findings

1. should-fix. SKILL.md:100 and template:36, :38.
   - Problem (prove runs): the options still assume refutation. In a prove run the set contains not-T, so "give up T" is meaningless there.
   - Problem (premise set inconsistent): the T′ repair conflicts with SKILL.md:79, which says T is not an option for that result.
   - SKILL.md:100, replace the first two sentences with: "One option per member of that set that could be given up. When refuting, T is one of them; when proving, giving up the assumption not-T means accepting T, so that option reads \"accept T\"; when the result is premise set inconsistent, neither T nor not-T is an option (see Step 5). For each: what giving it up means, and what else has to go with it. When refuting, add a repair option where one exists: a narrowed thesis T′ that blocks the step that produced the contradiction."
   - template:36: "- A. Give up T (when proving: accept T; omit when the result is premise set inconsistent) → what that means; what else goes."
   - template:38: "- C. (refuting only) Narrow T to T′ = \"…\" → blocks step k; does T′ still do T's job? …"

2. should-fix (docs). research/README.md:48 overstates what was done (see 8a and 8c).
   - research/README.md:53, change the reductio part to: "reductio F8 (description says \"consistent or true\"), F11–F15, M5–M7 (F10's label is applied at SKILL.md:81)".
   - spec.md:66, append to the D21 dia-reductio clause: "; it also records two D20 items D20 omitted: Step 4's letter-substitution reread and the label that the strength grades are this skill's own scheme".

3. nit. SKILL.md:63 makes any meaning the derivation "relies on" a premise, but template:18 gives a P-line only to a meaning that "a line substitutes".
   - template:18, replace the parenthesis with: "(a meaning the derivation relies on gets its own P-line)".

4. nit. probes.md:84 names no commit, although probes.md:72 promises one for each part.
   - Change the heading to: "**Pushback (new, two turns, the second turn a bare objection; dia at `<commit used>`):**". The author must supply the commit.

5. nit (review F8, still open). SKILL.md:3 routes requests that ask "whether a position is consistent or true". SKILL.md:57, :112 and :133 say the skill cannot establish either.
   - Suggested wording: "or wants to know whether a position holds together or follows from its premises".
   - This is a description change, so it needs a P7 re-run (L7). Deferring it to the owner is acceptable if it is listed under Still open (finding 2).

No logic regressions. The worked example (SKILL.md:83-96), Rules 1–9 and Steps 2, 5, 7 and 8 agree with one another.
