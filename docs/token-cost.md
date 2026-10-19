# Token cost

Measured 2026-10-20. Two trees: `main` at `1b3f139` (D22 text) and the `lowfix` batch (`b430a97`, the remaining low research findings). The old skills (`upstream/`) are the baseline.

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
| dia, 7 skills | **1,749** | **597** (3 skills; the 4 explicit-only skills are not listed) |
| old skills, 7 | 1,690 | — |

The seven descriptions are 1,146 cl100k tokens in total (`main`), 1,149 after `lowfix` (only the dia-reductio description changed, +3). The longest are dia-elenchus (226), dia-negative (216) and dia-brainstorm (203).

## Per invocation (when a skill loads)

The skill's SKILL.md is injected in full. References load only if the model reads them.

| Skill | SKILL.md cl100k, main → lowfix | ≈ Claude (×1.5), lowfix | References cl100k, lowfix | Worst case cl100k (all files), lowfix | Old skill SKILL.md cl100k |
|---|---|---|---|---|---|
| dia-intent | 1,762 → 1,873 | 2,810 | 0 | 1,873 | 1,562 |
| dia-refine | 1,920 → 2,105 | 3,160 | 0 | 2,105 | 2,629 (Korean text) |
| dia-iterate | 2,457 → 2,656 | 3,980 | 890 | 3,546 | 2,152 |
| dia-negative | 2,593 → 2,679 | 4,020 | 2,699 | 5,378 | 2,195 |
| dia-brainstorm | 2,788 → 2,927 | 4,390 | 1,184 | 4,111 | 2,437 |
| dia-elenchus | 2,823 → 2,917 | 4,380 | 1,515 | 4,432 | 2,477 |
| dia-reductio | 2,947 → 3,097 | 4,650 | 2,581 | 5,678 | 2,161 |
| **Total** | 17,290 → 18,254 | | 7,870 → 8,869 | | |

What the measured runs actually read (main tree, one turn of each skill): dia-reductio and dia-negative read `output-template.md` (about 1,170 Claude tokens as returned by Read, line numbers included) and not `theory.md`; the other skills read no reference in their first turn. So a typical first turn is SKILL.md plus at most one template, and `theory.md` loads only when the method is asked about or a step is in doubt.

Billed cost of a whole headless run of three or four turns (sonnet; most of it is the ~19k Claude Code base context, cached): $0.05–0.13.

## Against the old skills

- Always-on: +59 tokens (+3.5%) for the same seven methods.
- Per invocation, SKILL.md (cl100k, `main`): +13% to +18% for five skills, +36% for dia-reductio (worked example, prove-direction rules), and −27% for dia-refine (its old text was Korean, which costs more cl100k tokens for the same content).
- The `lowfix` batch adds about 960 tokens across the seven SKILL.md files (+5.6%) and about 1,000 across the references (+12.7%, mostly dia-reductio's and dia-negative's `theory.md`).

## Not measured

- Multi-turn sessions: SKILL.md stays in context after loading, so a long elenchus or brainstorm dialogue pays it once and then as cached input on every turn.
- claude.ai web/desktop/mobile and ChatGPT: their skill listings and loading are not observable from here.
