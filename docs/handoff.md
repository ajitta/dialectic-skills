# Handoff

State of the work and what is left, for the next agent session. Read `AGENTS.md` and `docs/spec.md` first; probe evidence is in `docs/probes.md`.

## State (2026-10-20)

- Plugin `dia` **0.1.0** is tagged `v0.1.0` and published as a GitHub pre-release (spec O5). The owner installed it on claude.ai on 2026-10-20 (P1 pass), so the no-bump window is closed: every skill change now needs a new plugin `version` and the skill's `metadata.version`.
- CI (`.github/workflows/check.yml`) runs on every push to `main` and on pull requests. It runs `tools/package.py --check`, the unit tests, and `claude plugin validate --strict` for the plugin and the marketplace. It is green.
- Skill text reflects spec D19–D29 (research findings, token audit, data-not-instructions rule, dia-refine suspected corrections, several-skills-in-one-prompt rules, `short_description` length). Every batch was diff-reviewed or probed; results are in `docs/probes.md` Parts A–K, `docs/token-cost.md` and `docs/skill-effect.md`.
- Spec §12.3 acceptance:
  - 12.1 passes.
  - P1, P3, P6, P7 and P8 pass.
  - P2 is still open; it is owner-run.
  - P4 and P5 need recorded results, pass or documented limitation; they are owner-run.

## Remaining work

| # | Item | Who | Notes |
|---|---|---|---|
| 1 | P1: claude.ai upload: passed 2026-10-20 | — | Accepted with seven skills; the synced copy matches `v0.1.0` byte for byte and the old copies are gone (probes P1). |
| 2 | P2: Claude mobile, one natural-language prompt per skill (next) | owner runs, agent records | Pass: the right skill loads and the reply is in the prompt's language. Suggest prompts from `docs/probes.md` P7, plus one each for intent, refine and iterate. For dia-intent the prompt names the skill and for dia-iterate it starts with `dia-iterate`; elenchus and brainstorm use the P7 prompts. For dia-intent also send the same request without the name and check that it does not load (spec §12.2). |
| 3 | P4: ChatGPT desktop (Pro), local plugin install | owner runs, agent records | `default_prompt` now uses `$dia:dia-<x>` (spec D19, from P3). Record whether it resolves in ChatGPT desktop and whether the skills appear under `@`. If it does not resolve there, report it; do not change it back without the owner. |
| 4 | P5: ChatGPT mobile (Pro) after P4 | owner runs, agent records | Pass or a documented plan limitation (O4) |
| 5 | O1: resolved 2026-10-20, no `references/ko/` files in 1.0.0 (spec D17) | — | To add one later: L4 header (`Scope:`, `Source:`, `As of:`, `Use when:`), name the file and its read condition in SKILL.md (L5), run P9. `tools/package.py` enforces the header and the mention. |
| 6 | O3: resolved 2026-10-20, MIT for all seven skills (spec D18) | — | — |
| 7 | Acceptance and 1.0.0 release | agent | The 0.x pre-release is done: `v0.1.0` (GitHub pre-release with `dialectic-skills.zip`). After P2 passes (and P4/P5 are recorded), set `version` to `1.0.0`, bump each changed skill's `metadata.version`, run `tools/package.py`, push, wait for green CI, tag `v1.0.0`, and `gh release create v1.0.0 releases/dialectic-skills.zip`. Update the status lines in `docs/spec.md` and `docs/probes.md`. |
| 8 | Codex GitHub marketplace route: resolved 2026-10-20 | — | `codex plugin marketplace add ajitta/dialectic-skills` works with git credentials for the private repository and fails without them (probes P3). If the repository is made public, re-check without credentials. |
| 9 | Research findings in `docs/research/` | agent | Applied 2026-10-20 (spec D19–D25, D29), still as 0.1.0. What remains is in `docs/research/README.md` § Still open: owner-deferred items (dia-intent F1, F8; dia-elenchus M4) and probe-wording items. |
| 10 | Codex claims a code check it did not run | owner watches in P4/P5 | Probes Part K: with dia-refine + dia-iterate, Codex labelled the 20% fix "(tool: JavaScript execution)" with no execution event in its log, 3/3. Both skills already forbid this; check whether it recurs in the Codex app or ChatGPT. |
| 11 | dia-refine by plain request on Claude Code | owner decides | Probes Part J: a request without the name loaded dia-refine 1/9, before and after D27; by name it loads every time. Left as a known limit (owner ruling: hold). |
| 12 | Long output when several analysis skills run at once | owner judges in P1/P2 | Probes Part K: dia-reductio + dia-negative gave 8.6k–9.4k characters on Claude Code. Owner ruling 2026-10-20: decide on a phone, not now. |

Observations from P8 (n=1 each; see `docs/probes.md`):

- In one run, dia-refine added an inline "(unverified; …)" note inside the revision. Addressed by spec D20 (marks go in ④ or the closing line); see the neutral-directory P8 re-run in `docs/probes.md`.
- In one run, dia-refine replied in Korean to an English prompt. It did not reproduce from a neutral directory (3/3 English), so the repository's `AGENTS.md` ("reply in Korean") was the likely cause.

## How probes were run (for re-runs)

- **Claude Code:** `claude -p "<prompt>" --plugin-dir plugins/dia --model sonnet --output-format stream-json --verbose --no-session-persistence --max-turns N`.
  - Give every run its own fresh `CLAUDE_CONFIG_DIR` that holds only a copy of `.credentials.json`. Otherwise the account's claude.ai plugins and skills sync into the session within one run and compete with `dia`. `CLAUDE_CODE_SYNC_PLUGINS=0` and `CLAUDE_CODE_SYNC_SKILLS=0` do not prevent the sync.
  - Start each run in an empty directory outside the repository and pass an absolute `--plugin-dir`. At the repository root, `CLAUDE.md` imports `AGENTS.md`, which describes the skills and says to reply in Korean, and that confounds routing and language results.
  - Discard any run whose `system/init` event lists a plugin with an `@synced` source.
  - Read which skill loaded from the `Skill` tool_use input.
  - Tool-less runs use `--tools Skill`.
  - Set `ENABLE_CLAUDEAI_MCP_SERVERS=false`: the account's claude.ai connectors otherwise load into isolated sessions, add a varying number of tools, and even appear in `--tools Skill` runs.
  - Action-holding cells need `--max-turns` 12 or more; hitting the cap returns an empty result.
  - Delete the credential copies afterwards.
- **Baseline arm:** a plugin directory with `.claude-plugin/plugin.json` (`{"name": "old", ...}`) and `skills/` copied from `upstream/installed/*` and `upstream/superclaude-stable-47f791b/socratic-*`.
- **Codex CLI:** use an isolated `CODEX_HOME`.
  - `codex plugin marketplace add <path>`, then `codex plugin add dia@dialectic-skills`.
  - `codex debug prompt-input "hi"` shows the model-visible skill list and needs no model call.
  - Explicit invocation needs a real `codex exec` run, which needs a copy of `auth.json`; delete the copy afterwards.
  - `$dia:dia-<x>` must be followed by a space, not a colon; `$dia:dia-intent:` does not resolve.
  - On the OCI build VM the Codex sandbox (bwrap) cannot start, so no shell command runs under `-s read-only` or `workspace-write`; cells that need file access ran with `--dangerously-bypass-approvals-and-sandbox` in a scratch directory.
  - Log every `item.*` event type: Codex's web search arrives as `web_search` items, not `command_execution`.
- **Skill-effect eval:** harnesses and raw runs are on the build VM under `~/work/dia-review/eval/` and `eval2/` (`run.py`, `sim.py` for the adaptive respondent, `judge.py`); the method is in `docs/skill-effect.md`.

## Environment notes

- Every developer command is stdlib Python: `python3 tools/package.py [--check]`, `python3 -m unittest discover -s tests -v`. PyYAML is optional; the YAML test is skipped without it.
- `claude plugin validate` needs the Claude Code CLI. CI installs it with `npm install -g @anthropic-ai/claude-code`.
