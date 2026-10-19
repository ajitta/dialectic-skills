# dia-negative: low-severity findings (lowfix)

Files changed: `skills/dia-negative/SKILL.md`, `skills/dia-negative/references/theory.md`. Not touched: the description, `output-template.md`, `agents/openai.yaml`.

## Findings

- **F2 (falsifier), applied in the review's corrected form.**
  - SKILL.md Step 5: "name the observation that would falsify it." -> "name the observation that would falsify it: one the user could actually make (a document, a practice, a case) that would show the stated purpose explains the pattern as well. A restatement of the stated purpose is not such an observation."
  - theory.md §3: new "Changed" bullet: the falsifier "is a falsifiability check in Popper's sense, a figure Adorno disputed ("Not all theorems are hypotheses", Positivist Dispute, p. 112). It is not Adorno's device; it is kept because an inference about what a claim does needs a check the user can run." The research's "borrowed from Popper" wording is not used.
  - Rule 6 and the template's "Would be falsified by" line are unchanged and still agree.
- **F3 (strictness attribution), applied.**
  - theory.md §3, the "Changed" bullet: "Adorno's own writing often works by rhetorical exaggeration … (SEP)" -> concrete proof (Positivist Dispute p. 115), then *Minima Moralia* §82 ("an element of exaggeration"; founders when it tries to prove its literal correctness).
  - The SEP citation is kept and narrowed to "SEP §3, on Honneth's reading of *Dialectic of Enlightenment*; SEP §5".
  - "The skill keeps the demand for proof and drops the exaggeration."
  - Sources: added Adorno's "On the Logic of the Social Sciences" (*Positivist Dispute*, Heinemann 1976, the research's URL) and *Minima Moralia* (Jephcott, NLB 1974).
- **F4 (narrow-C option), applied, note only.**
  - SKILL.md Step 6: "(state C′ exactly)" -> "(state C′ exactly; if the gap comes from how the practice works rather than from how C is worded, say that narrowing moves the gap rather than closing it)".
  - Not applied: the Step 7 half. The review calls it a non-problem.
- **F7 (Codex over-triggering), declined.** The review says to probe before changing the text, and the description is not to be changed.
- **F8 ("(the nonidentical remainder)"), declined.** The review calls the finding wrong: the "What escapes" line is the indirect, conceptual articulation the SEP describes. The parenthesis also follows Rule 9 and the template ("Adorno's terms in parentheses at most"), so I kept it.
- **F9 (models vs counterexamples), applied.** theory.md §3 has a new "Changed" bullet: "particulars are used as test cases (counterexamples). The models in ND's third part are extended interpretations of one subject matter, and the Preface says they are not examples; this skill does not attempt them." It paraphrases rather than quotes, because the Ashton and Redmond wordings differ.
- **F10 (b and d only), applied.**
  - (b) theory.md §3: "…cannot be given in a digest, and later scholars argue … (SEP; Stopford 2012)" -> "…cannot be given in a digest (SEP), and later scholars argue … (Stopford 2012)".
  - (d) The Kwon/Sogang thesis line is removed from Sources. It was cited nowhere in the body.
  - Not done: (a) and (c), which the review calls wrong; §7.2 was already in the SEP Sources line.
  - Owner/parent question: the separate F10 proposal to replace the Wikipedia citation with Ashton's Preface is outside "b and d", so I left it. Wikipedia is also cited at theory.md §2 "No final synthesis".
- **F12 ("whose aim"), applied.** SKILL.md Step 5: "and whose aim or what process it serves" -> "and what process it serves, or whose interests the pattern favors (as a function, not an intention)".
- **M4 (Habermas over-claim), applied.** theory.md §4: "…so it does not need a foundation of its own" -> "The skill's rule 1 narrows this in practice … It does not remove it: the demand that a finding be strict (rule 2) is the skill's own norm, and Stahl counts a bare demand for consistency as the weak point of internal critique (Stahl 2013)."
- **M5 (translation and source mix), applied.**
  - theory.md §2: "No object goes into its concept without a remainder … (SEP)" -> "Objects do not go into their concepts without leaving a remainder (ND 5) …". The SEP is kept for "no direct access".
  - "the nonidentical under the aspect of identity" -> Ashton's "nonidentity under the aspect of identity" (ND 5). Both wordings are taken from the research's Ashton quotes; I did not open Ashton myself.
  - Line 3: "Ashton translation as cited by the SEP" -> "Ashton translation, and ND quotations use its wording".
  - Sources: the ND entry now reads "(primary)" instead of "(primary; page numbers as cited by the SEP)".
- **M6 ("1969 lecture"), applied.** theory.md §2: "his 1969 lecture on late capitalism" -> "his 1969 text on late capitalism".
- **M7 (Rule 8 vs Step 8), applied.** SKILL.md Rule 8: "Recommend one option and stop there." -> "Recommend one option and do not decide for the user."

## Consistency check

I reread SKILL.md, theory.md and output-template.md after the edits:
- Rule 6 and Step 5 agree on the falsifier, and so does the template line "Would be falsified by".
- Rule 8 now agrees with Step 8's record.
- The Step 6 note fits the template's "remainder" slot.
- theory.md's "rule 6, Step 5" and "rule 2" references point to the right places.
- There are no worked examples to contradict.

## Counts

- SKILL.md: 118 lines (unchanged).
- Description: 981 characters (unchanged).
- No Hangul and no product names in skills/dia-negative/.
- Versions not bumped (pre-release exception, AGENTS.md). I did not run package.py or the tests.
