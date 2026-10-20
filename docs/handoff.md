# Handoff

State of the work and what is left, for the next agent session. Read `AGENTS.md` and `docs/spec.md` first; probe evidence is in `docs/probes.md`.

## State (2026-10-20)

- Plugin `dia` **1.1.0** renames `dia-intent` to `dia-confirm` (spec D30, 2026-10-20). 1.0.0 (`v1.0.0`) was released after acceptance (spec §12.3); the pre-release `v0.1.0` is what the owner probed, and 1.0.0 differs from it only in the version number. Every skill change needs a new plugin `version` and the skill's `metadata.version`. Older docs (probes, research, reviews) use the name `dia-intent`; it is the same skill.
- CI (`.github/workflows/check.yml`) runs on every push to `main` and on pull requests. It runs `tools/package.py --check`, the unit tests, and `claude plugin validate --strict` for the plugin and the marketplace. It is green.
- Skill text reflects spec D19–D29 (research findings, token audit, data-not-instructions rule, dia-refine suspected corrections, several-skills-in-one-prompt rules, `short_description` length). Every batch was diff-reviewed or probed; results are in `docs/probes.md` Parts A–K, `docs/token-cost.md` and `docs/skill-effect.md`.
- Spec §12.3 acceptance:
  - 12.1 passes.
  - P1–P8 pass (P4 and P5 by owner report); P9 is not applicable. The plugin is accepted.

## Remaining work

| # | Item | Who | Notes |
|---|---|---|---|
| 1 | P1: claude.ai upload: passed 2026-10-20 | — | Accepted with seven skills; the synced copy matches `v0.1.0` byte for byte and the old copies are gone (probes P1). |
| 2 | P2: Claude mobile: passed 2026-10-20 | — | The skills load from natural-language prompts; the mobile `/` menu does not list them, which matches the documented mobile route (in words). Probes P2. |
| 3 | P4: ChatGPT desktop (Pro): passed 2026-10-20 (owner report) | — | Route, `@` listing and `default_prompt` resolution were not reported (probes P4/P5). |
| 4 | P5: ChatGPT mobile (Pro): passed 2026-10-20 (owner report) | — | O4 resolved as supported. |
| 5 | O1: resolved 2026-10-20, no `references/ko/` files in 1.0.0 (spec D17) | — | To add one later: L4 header (`Scope:`, `Source:`, `As of:`, `Use when:`), name the file and its read condition in SKILL.md (L5), run P9. `tools/package.py` enforces the header and the mention. |
| 6 | O3: resolved 2026-10-20, MIT for all seven skills (spec D18) | — | — |
| 7 | Pre-release, acceptance and release: done 2026-10-20 | — | `v0.1.0` pre-release, P1/P2/P4/P5 on it, `v1.0.0` released. Next skill change: bump `version` (1.0.x / 1.x) and the skill's `metadata.version`, run `tools/package.py`, push, wait for green CI, tag, `gh release create`. |
| 8 | Codex GitHub marketplace route: resolved 2026-10-20 | — | `codex plugin marketplace add ajitta/dialectic-skills` works with git credentials for the private repository and fails without them (probes P3). If the repository is made public, re-check without credentials. |
| 9 | Research findings in `docs/research/`: closed 2026-10-20 | — | Applied as spec D19–D25 and D29. The owner-deferred items (dia-intent F1, F8; dia-elenchus M4) were dropped after acceptance (owner ruling). Open probe-wording notes stay in `docs/research/README.md` § Still open. |
| 10 | Codex claims a code check it did not run | owner watches in ChatGPT use | Probes Part K: with dia-refine + dia-iterate, Codex labelled the 20% fix "(tool: JavaScript execution)" with no execution event in its log, 3/3. Both skills already forbid this; check whether it recurs in the Codex app or ChatGPT. |
| 11 | dia-refine by plain request on Claude Code: known limit | — | Probes Part J: a request without the name loaded dia-refine 1/9, before and after D27; by name it loads every time. Kept as a known limit (owner rulings 2026-10-20, confirmed after 1.0.0). |
| 12 | Long output when several analysis skills run at once: kept as is | owner reports if it bothers on a phone | Probes Part K: dia-reductio + dia-negative gave 8.6k–9.4k characters on Claude Code. Owner ruling 2026-10-20 after 1.0.0: no length limit now; add one in a 1.0.x if it proves uncomfortable on a phone. |

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
