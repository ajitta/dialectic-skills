# Token cost

Measured 2026-10-20. Two trees: `main` at `1b3f139` (D22 text) and the D23 batch (`6882022`, the remaining low research findings after their diff review), called "D23" below. The old skills (`upstream/`) are the baseline.

## Method

- **Static counts:** tiktoken `cl100k_base` over the shipped files (`plugins/dia/skills/`). This is exact for that tokenizer, not for Claude's. For Codex, `o200k_base` over the model-visible skill list.
- **Claude, measured:** Claude Code 2.1.303, claude-sonnet-5-5, headless, fresh `CLAUDE_CONFIG_DIR` per run, empty working directory, absolute `--plugin-dir`. The always-on cost is the first turn's total input (`input + cache_creation + cache_read`) with the dia plugin minus the same with an empty plugin. The per-invocation cost is the increase in total input from the turn that calls `Skill` to the next turn, minus the first turn's output.
- **Codex, measured:** Codex CLI 0.163.0, isolated `CODEX_HOME`, plugin installed from a local marketplace, `codex debug prompt-input "hi"` (no model call).

### Noise and how it was handled

- The account's claude.ai connectors (11 MCP servers) load into isolated sessions, and how many tools they add varies between runs (27 to 86 tools). That moved the first turn by up to 6k tokens on identical input. All Claude figures below come from runs with `ENABLE_CLAUDEAI_MCP_SERVERS=false`.
- Even then, some runs receive an extra context attachment of roughly 5.9k–10k tokens (it coincides with `commands_changed` events). Per-invocation deltas that include one are not usable. Only two invocation runs were clean. Both give a Claude/cl100k ratio near 1.5: 3,762 tokens for dia-brainstorm's 2,545 cl100k, and 2,425 for confirm-intent's 1,523. The Claude column below is therefore an estimate, **cl100k × 1.5** (n=2 calibration; treat it as ±10%).
- The always-on figure is solid: three dia runs gave 18,637 tokens each and the empty-plugin run with the same events gave 16,888.

## Always-on (every conversation)

| | Claude Code (measured) | Codex (o200k, measured listing) |
|---|---|---|
| dia, 7 skills (measured at `1b3f139`) | **1,749** | **597** (3 skills; the 4 explicit-only skills are not listed) |
| dia 1.2.0, 7 skills (2026-10-21, D33) | not re-measured; the dia-confirm description grew by 38 cl100k tokens (51 → 89) | **1,342** (7 skills; 610 for the 3 listed at 1.1.1) |
| old skills, 7 | 1,690 | — |

The seven descriptions are 1,146 cl100k tokens in total (`main`), 1,149 after D23 (only the dia-reductio description changed, +3). The longest are dia-elenchus (226), dia-negative (216) and dia-brainstorm (203).

## Per invocation (when a skill loads)

The skill's SKILL.md is injected in full. References load only if the model reads them.

| Skill | SKILL.md cl100k, main → D23 | ≈ Claude (×1.5), D23 | References cl100k, D23 | Worst case cl100k (all files), D23 | Old skill SKILL.md cl100k |
|---|---|---|---|---|---|
| dia-intent | 1,762 → 1,896 | 2,840 | 0 | 1,896 | 1,562 |
| dia-refine | 1,920 → 2,129 | 3,190 | 0 | 2,129 | 2,629 (Korean text) |
| dia-iterate | 2,457 → 2,659 | 3,990 | 890 | 3,549 | 2,152 |
| dia-negative | 2,593 → 2,691 | 4,040 | 2,740 | 5,431 | 2,195 |
| dia-brainstorm | 2,788 → 2,963 | 4,440 | 1,190 | 4,153 | 2,437 |
| dia-elenchus | 2,823 → 2,992 | 4,490 | 1,542 | 4,534 | 2,477 |
| dia-reductio | 2,947 → 3,136 | 4,700 | 2,657 | 5,793 | 2,161 |
| **Total** | 17,290 → 18,466 | | 7,870 → 9,019 | | |

What the measured runs actually read (main tree, one turn of each skill): dia-reductio and dia-negative read `output-template.md` (about 1,170 Claude tokens as returned by Read, line numbers included) and not `theory.md`; the other skills read no reference in their first turn. So a typical first turn is SKILL.md plus at most one template, and `theory.md` loads only when the method is asked about or a step is in doubt.

Billed cost of a whole headless run of three or four turns (sonnet; most of it is the ~19k Claude Code base context, cached): $0.05–0.13.

## After the token audit (D24)

SKILL.md files total 17,487 cl100k after D24 (from 18,466 at D23, −979, −5.3%); per skill: dia-iterate −295, dia-elenchus −254, dia-negative −174, dia-refine −93, dia-intent −74, dia-reductio −63 (it gained two rules moved from theory.md), dia-brainstorm −26. References grow from 9,019 to 9,557 because dia-elenchus gains `theory.md` (1,156, read only when the user asks about sources or the method). Descriptions are unchanged. The diff-review fixes that followed add a few tokens. Details: `docs/research/token-audit/`.

## Against the old skills

- Always-on: +59 tokens (+3.5%) for the same seven methods.
- Per invocation, SKILL.md (cl100k, `main`): +13% to +18% for five skills, +36% for dia-reductio (worked example, prove-direction rules), and −27% for dia-refine (its old text was Korean, which costs more cl100k tokens for the same content).
- The D23 batch adds about 1,180 tokens across the seven SKILL.md files (+6.8%) and about 1,150 across the references (+14.6%, mostly dia-reductio's and dia-negative's `theory.md`).

## Not measured

- Multi-turn sessions: SKILL.md stays in context after loading, so a long elenchus or brainstorm dialogue pays it once and then as cached input on every turn.
- claude.ai web/desktop/mobile and ChatGPT: their skill listings and loading are not observable from here.
