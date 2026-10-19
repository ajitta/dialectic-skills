# Handoff

State of the work and what is left, for the next agent session. Read `AGENTS.md` and `docs/spec.md` first; probe evidence is in `docs/probes.md`.

## State (2026-10-20)

- Plugin `dia` **0.1.0** is built and on `main`. It is not released: there is no tag and no GitHub release, and the owner has installed it nowhere yet. While that holds, a skill change may keep 0.1.0: delete `plugin-release.json`, then run `python3 tools/package.py`. After the first install or release, every skill change needs a version bump.
- CI (`.github/workflows/check.yml`) runs on every push to `main` and on pull requests. It runs `tools/package.py --check`, the unit tests, and `claude plugin validate --strict` for the plugin and the marketplace. It is green.
- Spec §12.3 acceptance:
  - 12.1 passes.
  - P3, P6, P7 and P8 pass.
  - P1 and P2 are still open; they are owner-run.
  - P4 and P5 need recorded results, pass or documented limitation; they are owner-run.

## Remaining work

| # | Item | Who | Notes |
|---|---|---|---|
| 1 | P1: claude.ai upload of `releases/dialectic-skills.zip` (Customize › Plugins › Upload plugin). Pass: accepted; seven skills listed as `dia:dia-<x>` | owner runs, agent records | Before testing, the owner removes the old copies (spec §10): the synced skills `reductio`, `negative-dialectics`, `self-refine`, `recursive-refine`, `confirm-intent`, and the `socratic` plugin. Headless Claude Code showed all of them still active on the account. |
| 2 | P2: Claude mobile, one natural-language prompt per skill | owner runs, agent records | Pass: the right skill loads and the reply is in the prompt's language. Suggest prompts from `docs/probes.md` P7, plus one each for intent, refine and iterate. For the explicit-only skills the prompt names the skill or uses its marker; for dia-intent also send the same request without the name and check that it does not load (spec §12.2). |
| 3 | P4: ChatGPT desktop (Pro), local plugin install | owner runs, agent records | `default_prompt` now uses `$dia:dia-<x>` (spec D19, from P3). Record whether it resolves in ChatGPT desktop and whether the skills appear under `@`. If it does not resolve there, report it; do not change it back without the owner. |
| 4 | P5: ChatGPT mobile (Pro) after P4 | owner runs, agent records | Pass or a documented plan limitation (O4) |
| 5 | O1: resolved 2026-10-20, no `references/ko/` files in 1.0.0 (spec D17) | — | To add one later: L4 header (`Scope:`, `Source:`, `As of:`, `Use when:`), name the file and its read condition in SKILL.md (L5), run P9. `tools/package.py` enforces the header and the mention. |
| 6 | O3: resolved 2026-10-20, MIT for all seven skills (spec D18) | — | — |
| 7 | Acceptance and release | agent, after 1–4 | Set `version` to `1.0.0` in `plugin-manifest.json`, bump each skill's `metadata.version` as needed, run `tools/package.py`, push, wait for green CI. Then `git tag v1.0.0`, push the tag, and `gh release create v1.0.0 releases/dialectic-skills.zip`. Update the status lines in `docs/spec.md` and `docs/probes.md`. |
| 8 | Codex GitHub marketplace route (`codex plugin marketplace add ajitta/dialectic-skills`) | agent, where Codex CLI is installed | P3 covered only a local path. The repository is private, so Codex needs git credentials for it. |
| 9 | Research findings in `docs/research/` | agent | High findings and cross-cutting themes 1–4 applied 2026-10-20 (spec D19), still as 0.1.0. The remaining findings are listed, numbered, in `docs/research/README.md` § Not applied yet; settle them with the owner before P1. |

Observations from P8 that were not acted on (n=1 each; see `docs/probes.md`). Re-test before changing anything:

- In one run, dia-refine added an inline "(unverified; …)" note inside the revision.
- In one run, dia-refine replied in Korean to an English prompt. The host's Korean locale may be the cause.

## How probes were run (for re-runs)

- **Claude Code:** `claude -p "<prompt>" --plugin-dir plugins/dia --model sonnet --output-format stream-json --verbose --no-session-persistence --max-turns N`.
  - Give every run its own fresh `CLAUDE_CONFIG_DIR` that holds only a copy of `.credentials.json`. Otherwise the account's claude.ai plugins and skills sync into the session within one run and compete with `dia`. `CLAUDE_CODE_SYNC_PLUGINS=0` and `CLAUDE_CODE_SYNC_SKILLS=0` do not prevent the sync.
  - Start each run in an empty directory outside the repository and pass an absolute `--plugin-dir`. At the repository root, `CLAUDE.md` imports `AGENTS.md`, which describes the skills and says to reply in Korean, and that confounds routing and language results.
  - Discard any run whose `system/init` event lists a plugin with an `@synced` source.
  - Read which skill loaded from the `Skill` tool_use input.
  - Tool-less runs use `--tools Skill`.
  - Delete the credential copies afterwards.
- **Baseline arm:** a plugin directory with `.claude-plugin/plugin.json` (`{"name": "old", ...}`) and `skills/` copied from `upstream/installed/*` and `upstream/superclaude-stable-47f791b/socratic-*`.
- **Codex CLI:** use an isolated `CODEX_HOME`.
  - `codex plugin marketplace add <path>`, then `codex plugin add dia@dialectic-skills`.
  - `codex debug prompt-input "hi"` shows the model-visible skill list and needs no model call.
  - Explicit invocation needs a real `codex exec` run, which needs a copy of `auth.json`; delete the copy afterwards.

## Environment notes

- Every developer command is stdlib Python: `python3 tools/package.py [--check]`, `python3 -m unittest discover -s tests -v`. PyYAML is optional; the YAML test is skipped without it.
- `claude plugin validate` needs the Claude Code CLI. CI installs it with `npm install -g @anthropic-ai/claude-code`.
