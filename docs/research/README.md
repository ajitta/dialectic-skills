# Research

One document per skill: the method in its primary sources, relevant LLM research, a fidelity audit of the skill text, its lineage from `upstream/`, risks per surface, and numbered proposals. Written 2026-10-20 against plugin `dia` 0.1.0 (`main` at `cae2e4d`), so line references point at that tree. Each document was then checked by an independent reviewer (all seven verdicts: sound with fixes); the reports are in [review/](review/). Where a review corrects a document, the review wins.

| Skill | Document | Sources | Findings (high) |
|---|---|---|---|
| dia-intent | [dia-intent.md](dia-intent.md) | 29 | 11 (1) |
| dia-elenchus | [dia-elenchus.md](dia-elenchus.md) | 60 | 15 (3) |
| dia-brainstorm | [dia-brainstorm.md](dia-brainstorm.md) | 41 | 15 (0) |
| dia-reductio | [dia-reductio.md](dia-reductio.md) | 31 | 15 (2) |
| dia-negative | [dia-negative.md](dia-negative.md) | 28 | 13 (1) |
| dia-refine | [dia-refine.md](dia-refine.md) | 17 | 15 (2) |
| dia-iterate | [dia-iterate.md](dia-iterate.md) | 27 | 13 (2) |

Citations were registered as pages were fetched and checked with a citation ledger (every `[n]` resolves to a fetched URL). Claims without a source are marked `[unverified]`. The documents are agent-written; see [review/](review/) for the independent check.

## Cross-cutting themes

Several findings recur across skills. A fix for one should be decided once and applied to all of them.

1. **Codex/ChatGPT invocation names.** `default_prompt` in every `agents/openai.yaml` uses `$dia-<x>`, which P3 showed does not resolve on the Codex plugin route (`$dia:dia-<x>` does). For `dia-iterate`, `allow_implicit_invocation: false` also hides the skill from the Codex model, so first-word invocation cannot work there. Raised in intent, brainstorm, refine and iterate; see handoff item 3 (P4).
2. **Yielding under pushback (sycophancy).** No skill says when a step, finding or verdict may be withdrawn after the user disputes it. Published "are you sure?" studies report high flip rates. Raised in elenchus, brainstorm, reductio, negative and intent.
3. **Recall is not verification, everywhere.** The P8 fix to dia-refine (the confirmed basis is a tool that ran, user material or own re-derivation) is not mirrored in dia-intent's quick check or dia-reductio's evidence classes. Also, dia-refine counts its own re-derivation as confirmed while dia-iterate does not.
4. **Honest method labels.** Each skill departs from its named source somewhere: the "ideas born" layer in elenchus, Paul/CBT rather than Plato in brainstorm, internal rather than immanent critique and a Popperian falsifier in negative, CRITIC rather than Self-Refine in iterate. Each document proposes either a text fix or an explicit label.
5. **Fallbacks when references are unreadable.** Headless runs could not always open `references/*.md`. Record formats and result labels that live only in references (elenchus, negative) or a missing worked example (reductio) then go missing.
6. **Probe confound.** The probes ran at the repository root, where `CLAUDE.md` imports `AGENTS.md` ("reply in Korean"). The language evidence in P7 and P8 (one Korean reply to an English prompt) is therefore confounded. Re-run from a neutral directory with an absolute `--plugin-dir` (dia-refine F4).

## Applied (spec D19, 2026-10-20)

The high findings and themes 1–4, in the form the reviews corrected:

- Theme 1: `default_prompt` is `Use $dia:dia-<x> …` in all seven skills; dia-iterate lists `@dia-iterate` and the neutral fallback wording; spec §4, §5.7, §7.3 and P3's pass condition updated.
- Theme 2: a step, finding or verdict is withdrawn only when its defect can be named (elenchus, reductio, negative) or the user adds substance (brainstorm); dia-intent names a correction that conflicts with inspected evidence.
- Theme 3: "supplied by the user" added to the evidence classes, and recall is never "verified" (reductio, negative); dia-intent labels tool-less values as re-derived; dia-refine tags each confirmed error (tool / user's material / re-derived); dia-iterate says why re-derivation does not count there.
- Theme 4: labels in elenchus ("ideas born", user-worded revision, statements not persons), brainstorm (midwife), negative (internal critique), iterate (CRITIC-like, not Self-Refine).
- dia-elenchus F2: the contradiction is the definition and premises together, with one script ("Which would you change, and how?") in all three places.
- dia-reductio F1, F2: "no contradiction found" instead of consistency or independence; [L] is logic or mathematics only, an unstated definition is [A]; theory.md credits Duhem–Quine.
- dia-refine F1, F2: one closing line allowed in "final version only" mode; basis tags with a re-derived example.
- dia-iterate F1, F3: regression is a changed lock without new evidence, a new confirmed defect from a fix, or a returning defect; zero defects is none named or all refuted. The example round summary now agrees with the rules.
- dia-intent 7: no text change; the P2 wording for explicit-only skills is fixed in spec §12.2.

## Not applied yet

Numbered for decisions. Each follows the review's corrected form.

1. dia-reductio: strength grades and the "carried" test are written for the refute direction only; the prove direction mis-grades (review M1). The "both" direction has no rule for recording two contradictions (M2).
2. dia-reductio: contraries need the premise that rules out both being true (F4, corrected); keep the rule list open-ended and add arithmetic (F5); add the corrected ~12-line worked example (F6).
3. dia-iterate: label the round-1 style exception (F4 option b); scope candidates to claims that bear on the conclusion (F5); search snippets vs citations (M3); re-check a fixed span before locking it (M4); a locks line under the round table (F11).
4. dia-refine: where the "unverified" mark and sources go, decided together with upstream's sources-in-revision rule (F3); exempt added requirements from the length rule (F7); language fallback for a bare `dia-refine` message (M5).
5. dia-negative: list only the options that fit, plus a no-findings variant (F5, with Rule 8 and Step 7); record fallback including History (F11); the description promises a "real purpose" the body treats as an inference (M1).
6. dia-elenchus: frustration script without the anecdote (F10); copy the result-label criteria into SKILL.md verbatim (F13); number premises from the visible transcript (F8).
7. dia-brainstorm: SCAMPER only in Step 3, stated in SKILL.md (M1); one summary cadence (F2); a synthesizing question before the verdict (F3, keep the risky-assumption clause); criteria prompt as examples (F4); options differ in kind (F5).
8. dia-intent: pre-approval investigation must not send private material out or incur cost (M1); the confirmation says what is sent or spent and to whom (F3); explicit reply-language rule (M3).
9. Probes: re-run P6–P8 from a neutral directory, since the original runs loaded this repository's `AGENTS.md` (theme 6; the dia-negative P7 cells and the Korean "immanent critique" cell were re-run that way after D19, see `docs/probes.md`); behavior probes for intent and for pushback.
