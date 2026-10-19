Verdict: PASS WITH FIXES

Scope: `git diff 1b3f139 b430a97 -- skills/dia-negative` (SKILL.md: 3 hunks; references/theory.md: 6 hunks). The same diff has no changes to docs/spec.md, README.md or tests/. I read all of SKILL.md, theory.md, output-template.md and openai.yaml after the change, and checked every changed citation against its source. Sources fetched this session: SEP *Adorno* (2024 revision); *Positivist Dispute* PDF (Heinemann 1976); *Minima Moralia* PDF (Jephcott); Ashton's ND Introduction (Columbia reader); Ashton's ND Preface (search-result copies); Stahl 2013 (SSRN PDF).

Checks run in the tree (read-only; `git status` clean before and after):
- `python3 tools/package.py --check`: "ok" for all 7 skills, exit 0.
- `python3 -m unittest discover -s tests`: 13 tests, OK, 1 skipped (PyYAML). With PyYAML on PYTHONPATH: 13/13 OK.
- `plugins/dia/skills/dia-negative` is identical to the source. SKILL.md has 118 lines. The description is 981 chars and unchanged, so no L7/P7 re-run is needed. No Hangul and no product names.

Verified correct in the review's corrected form:
- M7. SKILL.md:40 "do not decide for the user". This agrees with Step 7 (:90) and with Step 8 and the record.
- F12. SKILL.md:72 "whose interests the pattern favors (as a function, not an intention)". This agrees with Rule 6 (:38) and the Mind-reading pitfall (:114).
- F2. SKILL.md:72 uses the review's narrowed wording ("A restatement of the stated purpose is not such an observation"). theory.md:36 uses the review's "a figure Adorno disputed" and not "borrowed from Popper". "Not all theorems are hypotheses" is on p. 112, confirmed.
- F4. SKILL.md:80 has the Option A note only. Leaving out the Step 7 half follows the review ("non-problem").
- F9. theory.md:35 is right. Ashton's Preface says "Part Three elaborates models of negative dialectics. They are not examples; they do not simply elucidate general reflections."
- F10(b). Correct: Stopford has "not a system…", and the SEP has "not expoundable" and "concise summary". F10(d): the Kwon line is gone, it was cited nowhere in the body, and nothing else refers to it.
- M4. Stahl 2013 p. 6 does say "a mere demand for consistency seems to only enable a very weak form of critique". But see finding 6.
- M5. Ashton p. 5 reads "objects do not go into their concepts without leaving a remainder", "Contradiction is nonidentity under the aspect of identity" and "Dialectics is the consistent sense of nonidentity". All three now match theory.md:13 and :17, and theory.md:3 is accurate.
- M6. "1969 text" is safe. SEP 1969a is "Spätkapitalismus oder Industriegesellschaft?", and the quote is "ibid." to it.
- F3 sources. p. 115 has "the critique of ideology was under obligation to provide concrete proof … the mere mistrust of ideology … was not sufficient". MM §82 has "an element of exaggeration" and "tries with a thousand subtle arguments to prove its literal correctness, it founders". The translators and imprints in Sources are correct.
- Declines that are justified:
  - F7: the review says "Probe first, then change text", and the description is untouched.
  - F8: the review calls the finding wrong. Dropping the parenthesis was optional ("At most").
  - F10(a) and (c): the review says to drop them.

Findings

1. should-fix: theory.md:34 cites the wrong SEP section, overstates its sources, and drops the review's stringency point.
   - Problem, part 1: the sentence says Adorno's texts work "by rhetorical means and constellation instead of stepwise argument (SEP §3, …; SEP §5)".
     - The SEP's ND 41 quote ("In dialectics … the rhetorical element is on the side of content") is in SEP §2 *Early Writings*, not §5. The review's "SEP *Adorno* §5 quotes ND 41" is itself wrong; I searched the whole entry, and "rhetoric" occurs only in §2 and §3.
     - SEP §5 says the opposite of "instead of stepwise argument": "logical stringency and expressive flexibility interact (ibid., 18–19, 52–53)". Ashton p. 18 agrees: "expression and stringency are not two dichotomous possibilities. They need each other".
   - Problem, part 2: the review asked to keep the research's "stringency in presentation (ND pp. 18–19, as cited in the SEP)" ("checks out"). It was left out.
   - Replacement for theory.md:34:
     `- **Changed:** "contradiction" is narrowed to a checkable gap between what a claim says and what it delivers, and a finding must be strict. Adorno did ask ideology critique for concrete proof, not mere mistrust (Positivist Dispute, p. 115), and held that expression and stringency "need each other" (ND 18). But he also held that thought has "an element of exaggeration" and founders when it tries to prove its literal correctness (*Minima Moralia* §82); he placed the rhetorical element of dialectics on the side of content (ND 41, cited in SEP §2), and Honneth reads *Dialectic of Enlightenment* as using rhetorical means such as exaggeration (SEP §3). The strictness rule keeps the demand for proof and drops the exaggeration, a choice made for this skill so that its findings can be checked and disputed.`
   - Also change theory.md:51 "sections 3, 5 and 7.2" to "sections 2, 3, 5 and 7.2".

2. should-fix: the new falsifier wording has no referent when the target states no purpose.
   - Location: SKILL.md:72, "that would show the stated purpose explains the pattern as well".
   - Problem: Step 2 and output-template.md:17 allow "Stated purpose: … (or: none stated)", while Rule 6 (SKILL.md:38) still requires a falsifier. When no purpose is stated, the only kind of falsifier the new text allows cannot exist. A model will then either invent a stated purpose or name no falsifier at all. This gap comes from the research's own F2 text, and the review did not catch it.
   - Replacement for the sentence:
     `…and name the observation that would falsify it: one the user could actually make (a document, a practice, a case) that would show the stated purpose (or, with none stated, another cause you name) explains the pattern as well. A restatement of the stated purpose is not such an observation.`

3. should-fix: the batch is not recorded in the spec or in the research index.
   - Problem: spec §5 (spec.md:110) says "All seven skills keep their reference behavior unless this section or D19–D22 say otherwise". This commit changes dia-negative behavior (the falsifier test, the narrowing note, the function-not-intention wording, Rule 8) and changes spec.md not at all. docs/research/README.md:53 still lists "negative F2–F4, F7–F10, F12" as open. This applies to the whole batch, not only to this skill.
   - Replacement for spec.md: add a decision row, for example
     `| D23 | Low research findings (lowfix, 2026-10-20) amend §5. … dia-negative: the operative-function falsifier must be an observation the user can make that would show the stated purpose explains the pattern as well (a restatement of the purpose does not count); narrowing C notes when the gap is in the practice and narrowing only moves it; the function is stated as whose interests the pattern favors, not an intention; Rule 8 says the recommendation does not decide for the user; theory.md labels the falsifier as Popperian and corrects its attributions. F7 waits for a Codex probe; F8 is dropped per the review. |`
     Then change spec.md:110, 121, 128 and 136 from "D19–D22" to "D19–D23".
   - Replacement for research/README.md:53: remove "negative F2–F4, F7–F10, F12" and add "negative F7 (Codex over-triggering probe)".

4. nit: the F10 Wikipedia replacement was declined without a valid reason.
   - Location: theory.md:7 "(Wikipedia, quoting the preface)" and theory.md:54.
   - Problem: the review says "Replacing Wikipedia is fine, but cite Ashton's Preface". It drops only F10(a) and (c). The implementer limited F10 to "(b) and (d) only", and the review does not support that. theory.md:3 now ties ND to Ashton, and theory.md:35 already cites the Preface directly. Ashton's Preface opens: "As early as Plato, dialectics meant to achieve something positive by means of negation; the thought figure of a 'negation of negation' later became the succinct term. This book seeks to free dialectics from such affirmative traits without reducing its determinacy." That is exactly what theory.md:7 paraphrases.
   - Replacement:
     - theory.md:7 `(Wikipedia, quoting the preface)` → `(ND, Preface)`.
     - theory.md:54 → `- "Negative Dialectics", Wikipedia (secondary).` It is still cited at :21.

5. nit: theory.md:13 gives Ashton's wording verbatim without quotation marks, although theory.md:3 says "Everything is paraphrased from them unless quoted".
   - Replacement: `**The nonidentical.** "Objects do not go into their concepts without leaving a remainder" (ND 5).`

6. nit: theory.md:41 joins Stahl to the Habermas point as if Stahl supported it.
   - Problem: Stahl's point is the transformative weakness of internal critique (it "seems to run danger of claiming too little", p. 6). That is a different objection from Habermas's missing normative foundation. The "and" makes Stahl read as support for "It does not remove it".
   - Replacement for the second half:
     `It does not remove it: the demand that a finding be strict (rule 2) is the skill's own norm. That demand also has a cost: Stahl writes that "a mere demand for consistency seems to only enable a very weak form of critique" (Stahl 2013).`

Logic and contradictions:
- With the new note, Step 6 (SKILL.md:80) is consistent. A narrowed C′ holds by construction, so the old gap moves into C′'s remainder, which is exactly the template's "remainder" slot (output-template.md:41).
- Rule 8, Step 7, Step 8 and the template's "The decision is yours." agree.
- Rule 6, Step 5 and the template's "Would be falsified by:" agree, apart from finding 2.
- theory.md's "rule 6, Step 5" and "rule 2" point to the right places.
- No worked examples exist to contradict.

Implementer's report: accurate on what changed, the counts and the declines, with three exceptions:
- It describes F10 as "(b) and (d) only", which the review does not support (finding 4).
- It does not say that the review's ND 18–19 stringency point was left out (finding 1).
- It did not run the checks. I ran them, and they pass.

Version: unchanged at 0.1.0 / 1.0.0, under the documented pre-release exception (AGENTS.md; handoff.md, State). Acceptable.
