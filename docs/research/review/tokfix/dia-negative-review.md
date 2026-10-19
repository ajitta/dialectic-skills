Verdict: PASS WITH FIXES

Scope: `git diff d135f8e 75d7ac1 -- skills/dia-negative` (3 files: SKILL.md, references/output-template.md, references/theory.md; 7 insertions, 11 deletions), and the D24 and §5 edits in docs/spec.md. I compared every hunk with the old text (`git show d135f8e:...`), the audit (docs/research/token-audit/dia-negative.md) and the evidence rules (evidence.md §8).

## Findings

1. should-fix: the no-motive guard for `--target=user` is weaker (K7, "Mind-reading").
   - Removed text (d135f8e SKILL.md:114): "- Mind-reading: asserting a person's hidden motive instead of what the claim does." That pitfall applied to every target.
   - The audit's reason for cutting it (audit:56) says "Rule 6 sentence 2 and Step 5 … say the same". That holds only for two of the three targets. Rule 6 is explicitly scoped: SKILL.md:38 says "For texts and for your own answers, speak about what the claim or text does, not about a person's hidden motives." For the default target, `user`, the only guard left is the parenthesis in Step 5 (SKILL.md:72, "(as a function, not an intention)"). That parenthesis covers the operative-function line, but not findings, options ("replace the stated purpose with the operative one and own it", :83) or follow-ups.
   - This matters for the user target in particular: the description invites "what is this really for" and "the real purpose behind a stated goal", and the research names mind-reading as a main risk (docs/research/dia-negative.md:212). The D23 fix ("function … not an intention") survives, so no D-decision is lost. What is lost is coverage of one target.
   - Fix (SKILL.md:38): this generalizes Rule 6 and also saves tokens, so the cut pitfall's coverage comes back without restoring the line. Replace "For texts and for your own answers, speak about what the claim or text does, not about a person's hidden motives." with:
     `Speak about what the claim or text does, not about anyone's hidden motives.`
   - Alternative, if Rule 6 (text reviewed under D23) should not change: restore the pitfall under Pitfalls, SKILL.md after :111:
     `- Mind-reading: asserting a person's hidden motive instead of what the claim does.`

2. nit: the intro is now a bare universal thesis that reads like the abstract-negation pitfall (K1).
   - New SKILL.md:14: "No concept captures its object without a remainder." Pitfall at SKILL.md:111: "Abstract negation: … \"nothing captures reality\"."
   - The removed bridge sentence (d135f8e SKILL.md:14, "Critique works by pointing out specific contradictions between what a concept or claim says and what it actually delivers, using the claim's own standards, and it does not end in a reconciling synthesis.") was the line that turned the thesis into "a remainder is shown only through a specific gap".
   - Rules 1, 2, 5 and 7 still enforce that, so behavior should not change. But the skill now opens with a sentence that is close to an example it forbids. Evidence rule 9 (contradictions and near-duplicates cost GPT-5-class models) argues for a few tokens of disambiguation.
   - Optional replacement (SKILL.md:14):
     `No concept captures its object without a remainder; this skill shows a remainder only through a strict gap (Rules 2 and 5).`

3. nit: the implementer's account is stale on regeneration.
   - docs/research/review/tokfix/dia-negative-applied.md:46 says "Nothing regenerated: `tools/package.py` was not run, so `plugins/dia/` now lags the source". At 75d7ac1 the generated copies are current: `diff -r skills/dia-negative plugins/dia/skills/dia-negative` shows them identical, the zip entries match the source byte for byte, and `--check` passes.
   - Replacement:
     `- Regenerated in 75d7ac1: plugins/dia/ and releases/dialectic-skills.zip match the source; tools/package.py --check passes.`

4. nit (process, not text): the audit's risk probes were not run.
   - The audit names these probes (audit:110–116):
     - P8 with a "what method is this?" follow-up, for K1 and K2;
     - a `--target=text` run on a mission statement, for K6;
     - P7 negative cells with output review, for K7.
   - Evidence rule 13 says "Validate each class removal with the probes before shipping". Neither D24 nor the account records a run; the account lists them as open (applied.md:44–45).
   - This is acceptable at the pre-release 0.1.0, but it should be done before the first release. Suggested D24 addition:
     `Probe re-runs named in the audits' risk tables are pending before release.`

## Per-item verification (check 1, behavior loss)

- K1 (SKILL.md:14):
  - The removed "To think is to identify" and "never goes into its concept without a remainder" are in theory.md:11 and :13, with SEP and ND 5.
  - Its other parts are each still stated in the body: own standards (Rule 1, :33), specific contradictions (Rule 2, :34; Rule 5, :37), says/delivers (Step 4, :62–63), no synthesis (Rule 7, :39).
  - "Identification" is still defined in place at Step 1 (:48, "the place where something is identified as something").
  - No loss beyond finding 2.
- K2 (:16): the label "practical adaptation of Adorno's method, not Adorno's own procedure" is kept. The reason clause is in theory.md:31 ("Adorno resisted summary … (SEP) … (Stopford 2012)"). This is a label shortened, not lost (D19). OK.
- K4 (:35): the rule itself, "count a finding only where the gap is strict *within* a single reading", is unchanged, and the template repeats "Ambiguity alone is not a finding." (output-template.md:11). OK.
- K5 (:56): Rule 4 (:36), "Take D from the target's own material first", is unchanged. OK.
- K6a (Targets): `user` is still defined in the Parameters table (:24), and the `all` order "user, claude, text" (:100) still resolves. OK.
- K6b (:99), "Treat the text's purpose statements as its standard": covered by Rule 1 "stated goals" (:33) and Step 2 "what it says it is for … **stated purpose**" (:52).
- K6b, "not what its author intended": covered for texts by Rule 6 (:38) and Step 5 (:72). OK.
- K7, External critique: Rule 1 (:33) includes the same example.
- K7, Closure: Rule 7 (:39), "must state its own remainder".
- K7, Mind-reading: see finding 1.
- K9 (template :3): each dropped clause is in Rule 9 (SKILL.md:41), which is always loaded with the template:
  - "language of the user's latest message";
  - "Quote the target in its original language";
  - "Use plain words; put Adorno's terms in parentheses at most".
  The pointer "(Rule 9)" resolves to the language rule. OK.
- K10 (theory.md:3): the read condition still stands at SKILL.md:16 and :107. The ND translation note is kept. OK.
- D19–D23 survival, confirmed present:
  - description label "narrower than Adorno's immanent critique" (:3) and the theory §4 statement (theory.md:43);
  - internal-critique label and "does not reconstruct such norms" (:16);
  - evidence classes with "your own recall is never \"verified\"" and the rule that user-supplied facts are not conditional (:36);
  - no-findings path through Step 7 (:68, :86, :90);
  - dispute rule, "Withdraw it only if you can name what fails" (:105);
  - falsifier as an observation the user can make (:72);
  - "narrowing moves the gap" (:80);
  - Rule 8 (:40);
  - theory.md Popperian label (theory.md:36);
  - template fallback (:16) and record fallback (:94);
  - "Filling the template" pitfall (:114).

## Checks 2–6

- 2, contradictions and dangling references:
  - Rule and step numbers are unchanged; theory.md's references to "rule 1/2/6" and "Step 5" still resolve.
  - The template and SKILL.md agree on statuses, the no-findings lines and the conditional definition.
  - Nothing else is dangling. One near-conflict: finding 2.
- 3, moved text: nothing was moved. Every cut unit already existed in theory.md (K1, K2) or elsewhere in the body (the rest). Nothing a first turn needs depends on a reference, and the no-reference fallbacks are intact.
- 4, fidelity: no citation was moved or changed in dia-negative. The new SKILL.md:14 is an unattributed paraphrase of ND 5 ("Objects do not go into their concepts without leaving a remainder", quoted at theory.md:13). It reverses the subject without changing the meaning. No fetch was needed.
- 5, scope: the diff contains exactly K1, K2, K4, K5, K6a, K6b, K7, K9 and K10 (audit:90–101), and each text matches the audit's proposal verbatim. K8 (Jaeggi/Stahl, owner decision) was not applied, and D24 says so. Frontmatter, description, agents/openai.yaml and metadata.version are untouched. Nothing was added outside the set.
- Spec:
  - The D24 row and the "D19–D24" substitutions are consistent. §5.5 has no "Behavior" line, before or after, so there is nothing stale there.
  - D24's claims about dia-negative ("labels were shortened in place and kept … no-reference fallbacks were kept"; "Not applied … dia-negative's Jaeggi/Stahl shortening") are accurate.
- Repo rules:
  - SKILL.md is 114 lines (<= 200).
  - No Hangul in skills/dia-negative.
  - LF endings.
  - The text stays assistant-neutral, with no new tool use.
- 6, commands run in the tree (read-only):
  - `python3 tools/package.py --check`: "ok" for all 7 skills, exit 0.
  - `python3 -m unittest discover -s tests`: Ran 13 tests, OK (skipped=1). The skip is test_frontmatter_and_openai_yaml_parse, "PyYAML not installed". The frontmatter and openai.yaml are unchanged in this diff.
  - Generated copies: plugins/dia/skills/dia-negative is identical to the source, and the three .md entries in releases/dialectic-skills.zip match the source byte for byte.
  - Token counts were not re-measured, because tiktoken is not installed here. The 174/31/30 figures are the implementer's.
