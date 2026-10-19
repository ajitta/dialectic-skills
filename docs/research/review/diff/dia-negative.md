Verdict: PASS WITH FIXES

Scope: `git diff cae2e4d 7115d2a -- skills/dia-negative`, plus the parts of docs/spec.md, README.md and tests/ that concern dia-negative. I read the whole SKILL.md, output-template.md, theory.md and openai.yaml after the change. Sources fetched this session: SEP *Critical Theory* (2023), SEP *Adorno* (2024), Stahl 2013 (SSRN PDF).

Checks run in the tree (read-only; `git status` clean before and after):
- `python3 tools/package.py --check`: "ok" for all seven skills, exit 0.
- `python3 -m unittest discover -s tests`: 13 tests OK, 1 skipped ("PyYAML not installed"). The skipped test is the one that checks the new `default_prompt` prefix. I re-ran it with PyYAML installed under my scratch dir (`PYTHONPATH=$TMPDIR/pyyaml`): 13/13 OK, none skipped.
- Description is 977 chars (limit 1024). SKILL.md is 118 lines. No Hangul and no product names in skills/dia-negative/ (the `claude` target value is allowed by D14).

Applied correctly, in the review's corrected form:
- Theme 1: openai.yaml:4 "Use $dia:dia-negative …".
- F6: SKILL.md:99 and :106 use the exact wording of the proposal.
- Theme 3: SKILL.md:36 and output-template.md:23 add "supplied by the user" and "your own recall is never \"verified\"".
- F11 with the History line the review asked for: SKILL.md:94 matches the template's record fields one for one.
- M3: SKILL.md:16 says "If you cannot open it, follow the order of Steps 1–8".
- F5 template and pitfall: output-template.md:40 and :59, SKILL.md:118. "usually 2–3" was dropped as the review required, and options are kept rather than omitted, which respects Rule 8.
- M1: SKILL.md:3 "infers … what it actually does".

Findings:

1. should-fix: the new label misstates the relation between internal and immanent critique. Fidelity problem.
   Locations: SKILL.md:3 ("Internal critique (the narrow form of immanent critique)"), SKILL.md:16 ("Fuller immanent critique, in Adorno and in later accounts such as Jaeggi's and Stahl's, also reconstructs …"), spec.md:64 (D19), spec.md:155 (§5.5), README.md:11.
   Problem: the sources the text itself names treat internal critique as the alternative that immanent critique is defined against, not as a narrow form of it:
   - SEP *Critical Theory* §2.1: "Immanent critique avoids the dichotomy between an internal critique that refers to standards … already recognized … and an external critique".
   - SEP *Adorno* §7.2: "'internal' critique, which holds norms fixed, vs. genuine 'immanent critique,' which can modify norms, cf. Jaeggi 2018".
   - Stahl 2013: a theory of immanent critique must "constitute a genuine alternative to external and internal critique".
   SKILL.md:16 also leaves out the feature the SEP uses to separate the two, namely that immanent critique can change the norms. Theme 4 was meant to make the label honest, and this wording replaces one inaccurate claim with another.
   Replacements:
   - SKILL.md:3 opening: `Internal critique (narrower than Adorno's immanent critique), adapted from Adorno's negative dialectics, run in one pass.` (981 chars total; "immanent critique" stays as a trigger.)
   - SKILL.md:16, second and third sentences: `It runs internal critique: the standard is what the target itself states. Immanent critique, in Adorno and in later accounts such as Jaeggi's and Stahl's, goes further: it draws on norms a practice implies without stating them, and it can change those norms. This skill does not reconstruct such norms.`
   - spec.md:155, README.md:11 and D19 (spec.md:64): replace "the narrow form of immanent critique" with "narrower than Adorno's immanent critique".
   - Because the description changes, L7 asks for the P7 routing re-check again (probes.md:60 recorded one for the D19 wording).

2. should-fix: theory.md still describes the old label and now contradicts SKILL.md. The research asked for this change and it was not made.
   Locations: theory.md:33 ("**Kept:** immanent standards, …") and theory.md:41 ("The skill does internal critique by default (the stated standard) and becomes immanent when Step 5 exposes the operative function and the options include changing the standard.").
   Problem: SKILL.md:16 now says the skill runs internal critique and does not do the further step. theory.md says the skill keeps immanent standards and sometimes becomes immanent. Research F1 says "Either way, change theory.md:41 to name which one the skill does", and the review did not reverse that. A model sent to theory.md "when … unsure … whether a standard is the target's own" (SKILL.md:16) gets two incompatible accounts of what it is doing.
   Replacements:
   - theory.md:33: `- **Kept:** judging by the target's own standards (internal critique; see §4), determinate (not abstract) negation, attention to the remainder, no forced synthesis, attention to function.`
   - theory.md:41: `- **Internal versus immanent critique (Jaeggi, Stahl).** Internal critique holds the target's norms fixed and checks compliance; immanent critique also draws on norms implicit in a practice and can change the norms themselves (SEP *Adorno* §7.2; SEP *Critical Theory* §2.1; Stahl 2013). This skill does internal critique: its standard is what the target states. Step 5 and the options to change the practice or own the operative purpose point towards immanent critique, but the skill does not reconstruct implicit norms.`

3. should-fix: the no-findings path is only partly carried through. The Recommendation step and its template line still assume that a finding exists.
   Locations: SKILL.md:90 ("the evidence class of the weakest finding it rests on") and output-template.md:49 ("Rests on: finding n (evidence class).").
   Problem: SKILL.md:86 and template:40 now require options and a recommendation when there is no strict gap, but neither Step 7 nor the template says what "rests on" means in that case. That is exactly the template pressure F5 targets, and the empty slot invites a made-up finding. The review's §5 says "F5 (plus SKILL.md Step 6/7 edits)", and only Step 6 was edited.
   Replacements:
   - SKILL.md:90: `Pick one option and give: the reason; the evidence class of the weakest finding it rests on (with no strict finding: "no strict finding; rests on the tested particulars"); the observation that would change the recommendation. End with a sentence that the decision is the user's.`
   - output-template.md:49: `Rests on: finding n (evidence class). (With no strict finding: the tested particulars.)`

4. should-fix: spec D19 understates what changed for dia-negative.
   Location: spec.md:64, which says only "dia-negative: labelled internal critique (…); disputed findings are checked against Rule 2."
   Problem: the diff also adds the evidence class "supplied by the user" with "recall is never verified" (SKILL.md:36, template:23) and the self-examination guard (SKILL.md:99). D19 lists the evidence-class change for dia-reductio but not for dia-negative, even though docs/research/README.md:34 lists both. The spec is the authority, and D19 says it states how behavior changes.
   Replacement: `dia-negative: labelled internal critique (narrower than Adorno's immanent critique); the evidence classes add "supplied by the user" and own recall is never "verified"; a self-examination neither defends the answer nor concedes a gap that fails Rule 2; disputed findings are checked against Rule 2, and a finding that survives is kept with a one-line reason.`
   D20 (spec.md:65) matches the D20 hunks: only fitting options, a no-findings options path, template and record fallbacks, and the purpose described as an inference.

5. nit: SKILL.md:16 now names Jaeggi and Stahl, but theory.md's source list has neither of them, nor the SEP *Critical Theory* entry.
   Location: theory.md:49–54.
   Problem: SKILL.md:16 says "Theory, sources … are in references/theory.md", so the new attribution has no source a reader can follow.
   Replacement, three lines added to Sources:
   - `- Titus Stahl, "What is Immanent Critique?", SSRN working paper, 2013. https://pure.rug.nl/ws/portalfiles/portal/35734818/SSRN_id2357957.pdf`
   - `- James Bohman et al., "Critical Theory (Frankfurt School)", *Stanford Encyclopedia of Philosophy* (2023), section 2.1. https://plato.stanford.edu/entries/critical-theory/`
   - In the SEP *Adorno* line: `sections 3, 5 and 7.2`

6. nit: the description is redundant at SKILL.md:3 ("infers, as a checkable inference, what it actually does").
   Replacement (the review's M1 wording): `infers what it actually does, as a checkable inference;`

7. nit: Rule 4 lists four evidence classes but does not say which of them make a finding conditional.
   Location: SKILL.md:36 ("A finding that rests on an unverified fact … is **conditional**").
   Problem: with "supplied by the user" added, it is unclear whether a user-supplied fact gives a firm finding or a conditional one. The template (:28) repeats the same wording.
   Replacement: `A finding that rests on a fact that is single source or unverified recall, on one contested reading, or on one branch of a case split is **conditional**; a fact supplied by the user counts as the user's material, labelled as such.` The owner may decide the other way; either way, say it explicitly.

8. nit: the dispute rule now checks only Rule 2.
   Location: SKILL.md:106 ("check it against Rule 2").
   Problem: this is the intended F6 wording, and the review endorsed it. But a dispute about which reading of C the target means is a Rule 3 matter, and a narrow model could reject it as "not a Rule 2 defect".
   Replacement: `check it against Rules 2–4 (a clarified reading of C is the target's own terms).`

9. nit (information only): versions.
   Problem: AGENTS.md requires a version bump for any skill-file change, but plugin `0.1.0` and `metadata.version: "1.0.0"` are unchanged, and plugin-release.json was re-recorded. This matches the pre-release exception in tools/package.py:19–20 ("Before a version is first released, delete the record and rebuild") and the commit message. No change is needed if 0.1.0 has never been released.

Not applied, and correctly so, because they are not in the "Applied" lists: F2–F4, F7–F10, F12, M4–M8. Items intended but missing: the theory.md:41 part of F1 (finding 2) and the Step 7 part of F5 (finding 3).

Logic: the no-findings options ("keep C as it is" or "examine the most likely gap next") agree with Rule 8, the status "holding against the tested particulars" and the new pitfall. The only gap is the "Rests on" slot in finding 3. Options are now lettered by position ("in the order given") in template:40, and that agrees with the Recommendation ("Option X") and the Record ("A, B, … offered"). No worked examples exist in this skill to contradict the rules.
