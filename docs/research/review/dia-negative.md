# Review: docs/research/dia-negative.md

Verdict: SOUND WITH FIXES

The quotes and page numbers mostly check out. I fetched all 28 sources and confirmed Hegel §79/§84, Positivist Dispute pp. 112–115, and Minima Moralia §29/§82/§89. F1, the core finding, is right. But two of the document's own citation findings are wrong, and acting on them would delete correct citations from theory.md:

- The SEP *Adorno* entry does contain the internal/immanent distinction (A20, F10a).
- The SEP *Adorno* entry does mention rhetorical exaggeration (A19, F3).

Several proposals also need changes before they are applied (F1b, F4, F5, F8, F11).

The document is 365 lines (limit 500) and contains no Hangul.

## 1. Section 7 findings

**F1 (high), internal vs immanent critique: confirmed; proposal partly right.**
- The problem is real:
  - SKILL.md:33 says "Never bring in an outside value the target does not hold".
  - SEP *Critical Theory* §2.1 defines internal critique as one that "refers to standards and standpoints that are already recognized by those criticized".
  - Stahl 2013 says immanent norms "go beyond both the regularities of empirical behavior and the individual or collective beliefs".
  - theory.md:41 admits "internal critique by default".
- High severity is fair, given the owner's fidelity rule.
- Option (a) contradicts spec §5.5 ("Purpose: immanent critique adapted from Adorno") and openai.yaml:3 ("Immanent critique: …"). The document does not mention either.
- Option (b), a "reconstructed standard", conflicts with three rules in the same skill unless they are amended together:
  - Rule 1 (SKILL.md:33: "Quote where it commits to each standard"; "Never bring in an outside value");
  - the pitfall "External critique" (SKILL.md:110);
  - the follow-up "standard is not theirs: remove every finding that used it" (SKILL.md:105).
- Either option also needs a version bump (AGENTS.md; spec §12.1).

**F2 (medium), the falsifier is Popper's device: partly right; severity should be low.**
- The quotes are accurate (Positivist Dispute p. 112: "Viewed from without, everything and nothing is refutable … Not all theorems are hypotheses").
- That passage objects to treating all theory as hypotheses. Asking for one disconfirming observation for one function-inference does not do that.
- The same essay demands ideology critique give "concrete proof of the falsehood" (p. 115). So the right verdict is "added, not from Adorno", not "departs".
- The proposed theory.md text says the falsifier "is borrowed from Popper". That is an unsupported claim about design origin; the document itself notes in §5 that upstream has no design notes. Suggested replacement: "a falsifiability check in Popper's sense, a figure Adorno disputed".
- In the SKILL.md:72 rewrite, "a statement of intent is not such an observation" over-restricts. For `--target=text`, an internal design memo is real evidence. Narrow it to "a restatement of the stated purpose is not such an observation".

**F3 (medium), the strictness rule: partly right; the attribution half is wrong.**
- The substance holds:
  - MM §82: thought that "tries with a thousand subtle arguments to prove its literal correctness … founders";
  - p. 115: "concrete proof".
- "The SEP does not say that" is false:
  - SEP *Adorno* §3: Honneth reads the text as "a disclosive critique that uses rhetorical means (narration, myth, chiasmus, exaggeration, etc.)".
  - SEP *Adorno* §5 quotes ND 41: "in dialectics … the rhetorical element is on the side of content".
- The real defect is narrower. The SEP's exaggeration point is Honneth's reading of the co-authored *Dialectic of Enlightenment*, not of "Adorno's own writing" generally.
- The proposed rewrite's "ND pp. 18–19, as cited in the SEP" checks out: "logical stringency and expressive flexibility interact (ibid., 18-19, 52-53)". Keep the SEP citation and add MM §82.

**F4 (medium), Option A and "keep it open": partly right; severity low.**
- The note on Option A is good. Positivist Dispute p. 115: "not logical contradictions which could be eliminated by means of more sophisticated definitions".
- The second half addresses a non-problem. Step 7 (SKILL.md:88) already allows recommending "keep the tension open" (SKILL.md:84), and Rule 4 (SKILL.md:36) already governs recommendations that rest only on conditional findings.
- The letters "Option A/E" exist only in output-template.md:40-44. SKILL.md:80-84 is unlettered.
- MM §89 ("Those who cannot help ought also not advise") is a social diagnosis in context ("in an order where every mousehole has been plugged …"), not a rule of method.

**F5 (medium), template pressure: problem confirmed; proposal incomplete.**
- output-template.md:39-44 and :58 ("A–E offered") do contradict SKILL.md:78 ("Offer the responses that fit").
- output-template.md:30 already has a no-findings line. What is missing is only what happens to Options and Recommendation.
- "Options and Recommendation are omitted" contradicts Rule 8 (SKILL.md:40) and Step 7, which are unconditional. SKILL.md must change as well.
- "usually 2–3" is unsupported.
- Sharma et al. measured users who dislike a passage. "Negative sycophancy under a critique request" is the author's inference, not their finding.

**F6 (medium), capitulation guard: confirmed.**
- Sharma's "frequently wrongly admit mistakes when questioned by the user" checks out. Both edits are minimal and consistent with Rule 2.

**F7 (medium), Codex over-triggering: plausible but unevidenced; low until probed.**
- The facts check out (openai.yaml:7; probes.md:31).
- Probe first, then change text.
- The proposed description measures about 995 characters, up from 917. It is under the 1024 limit, but with little margin.

**F8 (low), "(the nonidentical remainder)": wrong.**
- The document's own source (SEP §5) says determinate negation gives the misidentified aspects "an indirect, conceptual articulation". That is exactly what the "What escapes" line does.
- The proposed caveat adds philosophy-lecture text to a field label, against Rule 9 and the Jargon pitfall (SKILL.md:41, 114).
- At most, drop the parenthesis.

**F9 (low), models vs counterexamples: confirmed.**
- The Prologue says: "They are not examples; they do not simply illuminate general considerations."

**F10 (low), theory.md attributions: partly right.**
- (a) is wrong. SEP *Adorno* §7.2 says: "on 'internal' critique, which holds norms fixed, vs. genuine 'immanent critique,' which can modify norms, cf. Jaeggi 2018". That nearly matches theory.md:41. The only defect is that theory.md:49 cites "sections 3 and 5"; add §7.2.
- (b) is correct. The SEP has no "not a system / standpoint / set of principles"; Stopford's abstract does.
- (c) is not a misattribution. The SEP carries both quotes ("philosophy is not expoundable (referierbar)" and "no philosophical thinking of quality allows of concise summary").
- (d) is correct. The official English title is on the dCollection page, and the thesis is unused in the body.
- Replacing Wikipedia is fine, but cite Ashton's Preface, not [6] (Redmond). theory.md:3 fixes Ashton pagination, and the Wikipedia quote is Ashton's wording.

**F11 (low), record fallback: confirmed; the proposal drops a line.**
- The fallback omits "History" (output-template.md:61), which SKILL.md:103 uses. Add it.

**F12 (low), "whose aim": confirmed (nit).**
- SEP CT §3.3 says ideology "plays a functional role … cannot be explained with reference to the individual psyche".

**F13 (low), Korean "immanent critique" routing: confirmed.**
- probes.md:47 shows that only the Korean "negative dialectics" phrasing was probed.

## 2. Citation problems

All links resolved, including theory.md's own Stopford URL. Every quote behind F1–F6 and section 4 was found. These spot checks passed:

- Horkheimer: both quotes.
- Marx 1843: all three quotes.
- Stahl: the human-rights example; O'Connor and the "promise of autonomous subjectivity".
- Jaeggi 2005: Walzer and "overburdening".
- Jaeggi 2015.
- NDPR: "murky matter".
- Essay as Form: "emphatic concept".
- The Prologue.
- The arXiv and Springer abstracts.

Problems:

1. A19/F3: "SEP does not say this" is false (see F3).
2. A20/F10(a): the claim is in the SEP *Adorno* entry §7.2 (see F10).
3. A5: "polarities and ambiguity [1]". The SEP says "polarities or dialectical pairs" and never uses "ambiguity". Aesthetic polarities are also irrelevant to a rule about fixing one reading.
4. A10: "The need to let suffering speak" does not support "describe what the text does, not motives". Better support is [8] ("the truth that each text intends even in spite of itself") and SEP CT §3.3.
5. A14/F4: MM §89 and Horkheimer's "suspicious of … better, useful" are read as rules about critique method. In context both diagnose the social order. They are fair to cite as tension, but they are not Adorno forbidding recommendations.
6. §3.3/§6.1: "the research predicts pressure towards manufactured findings" is unlabelled inference; mark it [unverified] as the last bullet of §3.3 does.
7. §5: the lineage section omits the heading change at theory.md:43 ("Relation to reductio (dia-reductio)").

## 3. Fidelity table: disagreements

- **A9** should be "added, not from Adorno", not "departs" (reasons under F2).
- **A8** should be "matches the SEP's account": naming what C misses is the indirect conceptual articulation that determinate negation yields.
- **A19 and A20** are wrong (citation problems 1 and 2).
- **A16** should be "matches, with one closing status": "holding against the tested particulars" is a closing status that Geuss's "no natural stopping point" does not cover.

I agree with the other verdicts.

## 4. Missed issues

1. **Should-fix: the description over-promises.** SKILL.md:3 says the skill "names … what purpose it actually serves" and triggers on "wants the real purpose behind a stated goal exposed". The body makes purpose an inference that may come up empty (SKILL.md:72, "say so") and bans mind-reading (SKILL.md:38, 112). The description invites the requests the body refuses. Suggested: "infers what the claim actually does, as a checkable inference".
2. **Should-fix (cross-surface): `default_prompt` uses the wrong invocation form.** openai.yaml:4 has "Use $dia-negative …", but P3 found that `$dia-<x>` does not resolve for plugin installs; only `$dia:dia-<x>` does (probes.md:32; still open at probes.md:34). This is repo-wide (spec §7.3), and the document's §6.3 missed it.
3. **Nit: the template read has no fallback.** SKILL.md:16 says to read the template "before writing the first output" without a fallback (spec §7.1 requires completion with no tools). F11 covers only the record. A one-line fallback ("if you cannot open it, follow the order of Steps 1–8") would cover the whole layout.
4. **Nit: the answer to Habermas over-claims.** theory.md:39 says rule 1 means the skill "does not need a foundation of its own". But Rule 2 ("cannot both hold") and the decision to value consistency are the skill's own norms. Stahl names the "mere demand for consistency" as internal critique's weakness. The document audited the Rosen answer (A17) but not this one.
5. **Nit: theory.md mixes translations and sources.**
   - theory.md:17 quotes "the nonidentical under the aspect of identity", which is the SEP's modified translation (Ashton: "nonidentity under the aspect of identity").
   - It then quotes Ashton's "consistent sense" where the SEP has "consistent consciousness", although theory.md:3 says all page references are to Ashton.
   - theory.md:13 credits the remainder line to "(SEP)", but the SEP never uses "remainder"; the wording is ND p. 5.
6. **Nit: theory.md:19 date.** It says "1969 lecture" for SEP 1969a ("Spätkapitalismus oder Industriegesellschaft?"). From memory, unverified: it was given in 1968 and published in 1969. "1969 text" is safer.
7. **Nit: Rule 8 vs Step 8.** Rule 8 says "Recommend one option and stop there" (SKILL.md:40), but Step 8's record follows the recommendation. Reword to "and do not decide for the user".
8. **Nit: no version bump.** No proposal mentions the version bump that AGENTS.md and spec §12.1 require for any skill-file change.

## 5. Use of the document

- Apply as written, or with the noted fixes: F1 (resolve option (b)'s rule conflicts, or update spec §5.5 and openai.yaml for (a)), F5 (plus SKILL.md Step 6/7 edits), F6, F9, F11 (add History), F12, F13.
- Apply only with the corrections above, at low severity: F2 and F4.
- Drop: F8, F10(a), F10(c), and the "SEP does not say" claims in F3, A19 and A20. Otherwise correct citations would be removed from theory.md.
