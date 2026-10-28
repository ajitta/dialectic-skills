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

Later: [dia-adjudicate.md](dia-adjudicate.md) (2026-10-28) records the trials behind dia-adjudicate and the rename of dia-iterate to dia-ratchet (spec D39, D40); documents above keep the old name. [codex/README.md](codex/README.md) (2026-10-28) summarizes a separate Codex session on the plugin's framing (output is not outcome), naming and new-skill candidates, with the owner's rulings (no rename; spec D45).

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

## Applied, second batch (spec D20, 2026-10-20)

Items 1–8 of the former "Not applied yet" list, in the reviewed forms: dia-reductio M1, M2, F4, F5, F6; dia-iterate F4 (option b), F5, F11, M3, M4; dia-refine F3, F7, M5; dia-negative F5, F11, M1 (plus the template fallback, M3); dia-elenchus F8, F10, F13; dia-brainstorm M1, F2, F3, F4, F5; dia-intent M1, F3, M3.

## Applied, third batch (spec D21, 2026-10-20)

Every finding of the diff reviews of `7115d2a` (reports in [review/diff/](review/diff/)), including their nits, plus review M4 for dia-brainstorm (Hickey's "incidental complexity").

## Applied, fourth batch (spec D23, 2026-10-20)

The remaining low findings, in the reviewed forms, applied by one implementer per skill and checked by one diff reviewer per skill ([review/lowfix/](review/lowfix/)): dia-reductio F8, F10 (carried check), F11–F15, M5, M7; dia-iterate F6, F8–F10, F12, F13; dia-refine F5, F6, F8–F13, F15; dia-negative F2–F4, F9, F10 (b, d and the Preface citation), F12, M4–M7; dia-elenchus F4 (quickness move), F6, F7, F9, F11, F12, F14, M5, M6; dia-brainstorm F6–F8, F10–F13, M2, M3, M5; dia-intent F2, F4, F10, F11, M4–M6.

## Token audit (2026-10-20)

[token-audit/](token-audit/) classifies each skill's text by kind (instruction, rationale, provenance, example, redundant, meta), counts it in cl100k tokens and proposes keep, move, cut or shorten for everything that is not an instruction. [token-audit/evidence.md](token-audit/evidence.md) gives the cited evidence and decision rules. The recommended set is applied as spec D24 (implementers' accounts and diff reviews in [review/tokfix/](review/tokfix/)); the post-apply probes are in `docs/probes.md`, Part E.

## XML tags (2026-10-20)

[xml-tags/evidence.md](xml-tags/evidence.md) checks the claim that XML tags help separate instructions, material and examples, against vendor docs and format studies, and ends with decision rules. [xml-tags/audit.md](xml-tags/audit.md) goes through the seven skills for places where a delimiter would help or hurt and proposes a probe plan. Baseline probe: `docs/probes.md` Part H. Applied as spec D26 (no XML tags; a plain data-not-instructions rule in five skills), checked in Part I.

## Candidate methods for new skills (2026-10-21)

Research into further dialogue and reasoning methods, weighed by fit for human-AI chat and fidelity, with a claim-by-claim check of an external proposal: [candidates/](candidates/README.md). Proposals only; not yet independently reviewed.

## Still open

1. Probes: P6–P8, intent behavior and pushback were re-run from a neutral directory (`docs/probes.md`). Open: first-pass strictness of dia-negative findings (under a bare objection it now withdraws only named defects, but the withdrawn findings were weak to begin with); multi-turn probes for elenchus and brainstorm.
2. Owner rulings 2026-10-20: dia-reductio keeps its one-line dialetheism note; dia-intent F1 (state why the hold is unconditional) and F8 (explicit invocation in words) and dia-elenchus M4 ("during the dialogue" in the description) were deferred, then dropped after acceptance (owner ruling 2026-10-20: P1–P5 found no problem they would fix). Items that needed a probe first: dia-negative F7 (Codex over-triggering) was confirmed by probes Part F and is fixed by D25 (Part G); dia-brainstorm F15 (multi-turn) is probed in Part F, with two slips noted; and F8 (dropped per the review); dia-brainstorm M6 (routing differs between surfaces) is accepted as designed (owner ruling 2026-10-20: implicit on Claude, explicit-only on Codex, as upstream D2); dia-reductio M6 (probe wording). `short_description`: all seven are now 25–64 characters and `tools/package.py` enforces it (spec D29).
