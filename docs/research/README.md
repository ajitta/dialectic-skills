# Research

One document per skill: the method in its primary sources, relevant LLM research, a fidelity audit of the skill text, its lineage from `upstream/`, risks per surface, and numbered proposals. Written 2026-10-20 against plugin `dia` 0.1.0 (`main` at `cae2e4d`). Nothing here has been applied to `skills/`; every proposal waits for an owner decision.

| Skill | Document | Sources | Findings (high) |
|---|---|---|---|
| dia-intent | [dia-intent.md](dia-intent.md) | 29 | 11 (1) |
| dia-elenchus | [dia-elenchus.md](dia-elenchus.md) | 60 | 15 (3) |
| dia-brainstorm | [dia-brainstorm.md](dia-brainstorm.md) | 41 | 15 (0) |
| dia-reductio | [dia-reductio.md](dia-reductio.md) | 31 | 15 (2) |
| dia-negative | [dia-negative.md](dia-negative.md) | 28 | 13 (1) |
| dia-refine | [dia-refine.md](dia-refine.md) | 17 | 15 (2) |
| dia-iterate | [dia-iterate.md](dia-iterate.md) | 27 | 13 (2) |

Citations were registered as pages were fetched and checked with a citation ledger (every `[n]` resolves to a fetched URL). Claims without a source are marked `[unverified]`. The documents are agent-written and have not yet had an independent review.

## Cross-cutting themes

Several findings recur across skills. A fix for one should be decided once and applied to all of them.

1. **Codex/ChatGPT invocation names.** `default_prompt` in every `agents/openai.yaml` uses `$dia-<x>`, which P3 showed does not resolve on the Codex plugin route (`$dia:dia-<x>` does). For `dia-iterate`, `allow_implicit_invocation: false` also hides the skill from the Codex model, so first-word invocation cannot work there. Raised in intent, brainstorm, refine and iterate; see handoff item 3 (P4).
2. **Yielding under pushback (sycophancy).** No skill says when a step, finding or verdict may be withdrawn after the user disputes it. Published "are you sure?" studies report high flip rates. Raised in elenchus, brainstorm, reductio, negative and intent.
3. **Recall is not verification, everywhere.** The P8 fix to dia-refine (the confirmed basis is a tool that ran, user material or own re-derivation) is not mirrored in dia-intent's quick check or dia-reductio's evidence classes. Also, dia-refine counts its own re-derivation as confirmed while dia-iterate does not.
4. **Honest method labels.** Each skill departs from its named source somewhere: the "ideas born" layer in elenchus, Paul/CBT rather than Plato in brainstorm, internal rather than immanent critique and a Popperian falsifier in negative, CRITIC rather than Self-Refine in iterate. Each document proposes either a text fix or an explicit label.
5. **Fallbacks when references are unreadable.** Headless runs could not always open `references/*.md`. Record formats and result labels that live only in references (elenchus, negative) or a missing worked example (reductio) then go missing.
6. **Probe confound.** The probes ran at the repository root, where `CLAUDE.md` imports `AGENTS.md` ("reply in Korean"). The language evidence in P7 and P8 (one Korean reply to an English prompt) is therefore confounded. Re-run from a neutral directory with an absolute `--plugin-dir` (dia-refine F4).
