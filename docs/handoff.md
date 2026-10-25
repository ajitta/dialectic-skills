# Handoff

State of the work and what is left, for the next agent session. Read `AGENTS.md` and `docs/spec.md` first; probe evidence is in `docs/probes.md`.

## State (2026-10-25)

- Plugin `dia` **1.4.0** (2026-10-25, `v1.4.0`) adds `dia-menu` (spec D38): `dia`, `dia <n>`, `dia <prefix>`, `dia <request>`; dia-confirm 1.3.0 and dia-iterate 1.3.0 accept its selector. Built on branch `menu`, merged with the owner's go (PR #1). Two independent review passes (PASS WITH FIXES each), fixes applied; probes Part Q round 2 (Claude Code 84/84, Codex 56/56) and round 3 after the second pass (54/54, 33/36). The three Codex misses (a sibling answering a "N reasons" request directly without its method; no gated skill started) are kept as a case to watch by owner ruling, with no rule added. The owner checked `dia` on the phones (item 21, passed).
- Plugin `dia` **1.3.0** (2026-10-22, `v1.3.0`) adds dia-warrant, dia-conjecture and dia-counterplan (spec D35) and rewrites all ten descriptions to one convention after a clutter audit (spec D37; gate in probes Part P). 1.2.1 (2026-10-21) is meant to keep dia-brainstorm off plain requests to make or write something (spec D34; confirmed on ChatGPT mobile by the owner, item 16). 1.2.0 (2026-10-21) made all seven skills visible to the model on Codex and ChatGPT (`allow_implicit_invocation: true`, spec D33), so a message that starts with a skill's name works there as on Claude: probed on Codex (probes Part M) and confirmed in the ChatGPT mobile app by the owner (probes P5, item 15). 1.1.1 (2026-10-20) added the directory packaging (spec D32); 1.1.0 renamed `dia-intent` to `dia-confirm` (spec D30). 1.0.0 (`v1.0.0`) was released after acceptance (spec §12.3); the pre-release `v0.1.0` is what the owner probed, and 1.0.0 differs from it only in the version number. Every skill change needs a new plugin `version` and the skill's `metadata.version`. Older docs (probes, research, reviews) use the name `dia-intent`; it is the same skill.
- The repository `ajitta/dialectic-skills` is public since 2026-10-20 (owner decision; secrets scan of the full history was clean, and all `upstream/` material is the owner's own work).
- CI (`.github/workflows/check.yml`) runs on every push to `main` and on pull requests. It runs `tools/package.py --check`, the unit tests, and `claude plugin validate --strict` for the plugin and the marketplace. It is green.
- 1.3.0 was built on branch `next` and merged to `main` on 2026-10-22 with the owner's go (the owner's claude.ai syncs `main` automatically, so new skills and behaviour changes stay on a branch until then). The project page shows ten skills, with example sessions folded behind toggles and AVIF/WebP pictures. Branch `docs-skills-cli` (skills CLI install note, `upstream/` move, spec D36) is not merged, by owner decision.
- Releases are by tag: `.github/workflows/release.yml` attaches both zips to the release for a `vX.Y.Z` tag (item 7). The latest release is `v1.4.0`.
- README is in four languages (`README.md`, `.ko`, `.ja`, `.zh-CN`; spec D31). Change all four in one commit; `TestReadmeTranslations` checks their structure. It has the install routes per surface, a skill guide with worked examples (raw runs: `~/work/dia-review/readme-examples/` on the build VM) and troubleshooting.
- Project page: https://ajitta.github.io/dialectic-skills/ (2026-10-20), static `site/` deployed by `.github/workflows/pages.yml` on pushes that touch `site/`. Built with taste-skill, refined with impeccable; design records and the gates to re-run are in `docs/site/README.md`. All four READMEs link it. Independent review 2026-10-20 (reviewer profile; report on the build VM at `~/work/dia-review/site-2026-10-20/report.md`): facts, links, licences, rendering, gates and repository rules verified; its major finding (the immanent-critique gloss) and the minor and most nit findings are fixed. Left: the phone page is long (about 20,500 px); repeated "Copy the prompt"/"Full guide" accessible names; the local-folder install routes are not on the page. Google Search Console: URL-prefix property verified by the `google-site-verification` meta tag in `site/index.html` (keep it); `site/sitemap.xml` lists the page.
- Also listed in the catalog `ajitta/claude-plugins` as `dia@ajitta` (git-subdir `plugins/dia`, unpinned, so no catalog change per release).
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
| 7 | Pre-release, acceptance and release: done 2026-10-20 | — | `v0.1.0` pre-release, P1/P2/P4/P5 on it, `v1.0.0` released. Next skill change: bump `version` (1.0.x / 1.x) and the skill's `metadata.version`, run `tools/package.py`, push, wait for green CI, then push an annotated tag `vX.Y.Z` (its message becomes the release notes). `.github/workflows/release.yml` re-checks the build, checks that the tag matches the version in both zips, and attaches `dialectic-skills.zip` and `dialectic-skills-openai.zip` to the release (`vX.Y.Z-<suffix>` makes a pre-release; an existing release gets its assets replaced). Tested 2026-10-20 with a throwaway pre-release tag (create and re-run paths) and a mismatched tag (fails, no release); both were deleted. |
| 8 | Codex GitHub marketplace route: resolved 2026-10-20 | — | The repository is public since 2026-10-20; the Codex and Claude Code marketplace routes and the release download work without credentials (probes P3). |
| 9 | Research findings in `docs/research/`: closed 2026-10-20 | — | Applied as spec D19–D25 and D29. The owner-deferred items (dia-intent F1, F8; dia-elenchus M4) were dropped after acceptance (owner ruling). Open probe-wording notes stay in `docs/research/README.md` § Still open. |
| 10 | Codex claims a code check it did not run | owner watches in ChatGPT use | Probes Part K: with dia-refine + dia-iterate, Codex labelled the 20% fix "(tool: JavaScript execution)" with no execution event in its log, 3/3. Both skills already forbid this; check whether it recurs in the Codex app or ChatGPT. |
| 11 | dia-refine by plain request on Claude Code: known limit | — | Probes Part J: a request without the name loaded dia-refine 1/9, before and after D27; by name it loads every time. Kept as a known limit (owner rulings 2026-10-20, confirmed after 1.0.0). |
| 12 | Long output when several analysis skills run at once: kept as is | owner reports if it bothers on a phone | Probes Part K: dia-reductio + dia-negative gave 8.6k–9.4k characters on Claude Code. Owner ruling 2026-10-20 after 1.0.0: no length limit now; add one in a 1.0.x if it proves uncomfortable on a phone. |
| 13 | Directory listings (Anthropic, OpenAI) | owner submits later | Package side done in 1.1.1 (spec D32): plugin-folder README, `releases/dialectic-skills-openai.zip` with listing fields and draft logo. Owner steps: `docs/directory-submission.md` § Owner steps. |
| 14 | Owner housekeeping | owner | (a) Done 2026-10-20: claude.ai uses the GitHub marketplace. A marketplace added on claude.ai does not pull new versions by itself: select Check for updates on it, or turn on Sync automatically (claude.com/docs/plugins/overview). On 2026-10-21 the account still held 1.1.0 after 1.2.0 and 1.2.1 were released. Check for updates refreshed the marketplace (`updated_at` 10:16 UTC) but the account's synced plugin list then dropped `dia` instead of moving it to 1.2.1; removing `dia` and installing it again from the marketplace gave 1.2.1 (synced copy at 10:19 UTC, byte-identical to `plugins/dia/` at `v1.2.1`). README Troubleshooting and the site FAQ say so. The owner then turned on Sync automatically for `dialectic-skills` (2026-10-21), so later releases should reach claude.ai without a manual step. (b) Tell the agent the exact name of ChatGPT's plugin zip upload menu; README says "the plugin zip upload". (c) Native read of README.ja.md and README.zh-CN.md wording (structure is test-checked; wording was agent-translated and not read by a native speaker). |
| 15 | ChatGPT mobile check of 1.2.0 (D33): passed 2026-10-21 | — | Owner re-uploaded the 1.2.0 zip on chatgpt.com, saw 1.2.0 in the mobile app, and `dia-brainstorm …` and `dia-iterate --max 1 …` with no `@` both ran. A bare noun phrase («사진 파일을 날짜별로 이름 바꾸는 스크립트») loaded dia-brainstorm there; see probes P5 and item 16. |
| 16 | dia-brainstorm loaded for a bare noun phrase on ChatGPT mobile: fixed in 1.2.1, passed 2026-10-21 | — | Probes Part N and P5; spec D34. After re-uploading the 1.2.1 zip, «사진 파일을 날짜별로 이름 바꾸는 스크립트» on the phone gave the script directly, with no dia-brainstorm (owner). |
| 17 | Candidate methods for new skills: three picks (D35) released in 1.3.0 on 2026-10-22; README and site updated | — | `docs/research/candidates/README.md`: six family documents, cross-family clusters (pick at most one per cluster), folds into existing skills, and the check of the external proposal. Each pick then needs a spec decision row, §4/§5 entries, a full research document, routing probes with negative cells against its siblings, and a minor bump. |
| 18 | Description and body clean-up (spec D37): released in 1.3.0 on 2026-10-22, gated in probes Part P | — | Descriptions follow spec §7.2's convention (at most 900 characters; one "Not for" sentence). Re-run Part P's flagged cells after any description edit. |
| 19 | 1.3.0 on the owner's surfaces: ChatGPT zip re-uploaded, a new skill tried on the phone, and claude.ai showing 1.3.0, 2026-10-22 (owner report; no problem reported) | owner reports a miss if one shows up | The build VM cannot run the ChatGPT or Claude apps' skill choice; per-app results were not reported in detail. |
| 20 | dia-menu (spec D38): released in 1.4.0 on 2026-10-25 | — | Probes Part Q; reviews `~/work/dia-review/menu-2026-10-25/report.md` and `report2.md` on the build VM. Watch: on Codex, "N reasons my plan will fail?" via `dia` can announce a method that the sibling then skips (Part Q round 3). |
| 21 | dia-menu on the phones after the 1.4.0 release: passed 2026-10-25 (owner report) | — | The owner reported the mobile check of `dia`, `dia 4 …` and `dia` + a Korean request as done, on both Claude mobile and ChatGPT mobile (owner confirmed both apps); per-prompt results were not reported. Probes Part Q. |
| 22 | Project page shows `dia` (mobile step, claude.ai check count, FAQ): done 2026-10-25 | — | Text-only edits in `site/index.html`; the og image and skill count (ten skills) are unchanged. Design gates in `docs/site/README.md` were not re-run (no layout change). |

Observations from P8 (n=1 each; see `docs/probes.md`):

- In one run, dia-refine added an inline "(unverified; …)" note inside the revision. Addressed by spec D20 (marks go in ④ or the closing line); see the neutral-directory P8 re-run in `docs/probes.md`.
- In one run, dia-refine replied in Korean to an English prompt. It did not reproduce from a neutral directory (3/3 English), so the repository's `AGENTS.md` ("reply in Korean") was the likely cause.

## Install surfaces: what the owner observed (2026-10-20)

Where an install is made decides where `dia` shows up. README § Install says this; raw notes are in `docs/probes.md` P2, P4/P5.

- **Web installs are saved to the account** and reach that account's web and mobile apps: claude.ai (Add marketplace or zip upload) and chatgpt.com (zip upload; chatgpt.com has no marketplace menu).
- **Desktop installs stay on that computer:** Claude desktop (Customize › Plugins) and Codex in the ChatGPT desktop app (GitHub repository, Git URL or local folder). A plugin added in Claude desktop did not reach Claude mobile, and one added on claude.ai did not appear in Claude desktop.
- **Owner's working setup:** both desktop apps from the GitHub marketplace; claude.ai and chatgpt.com with an uploaded zip. Everything works.
- **Uploaded zips do not update.** Re-upload on each release; recommended to the owner: switch claude.ai to Add marketplace (account-wide; updates on Check for updates, or by itself with Sync automatically turned on). chatgpt.com stays on `dialectic-skills-openai.zip` until the OpenAI directory listing (item 13).
- **Claude mobile invocation:** the `/` menu does not list plugin skills, but `/dia-brainstorm`, `/dia:dia-brainstorm` and a message starting with `dia-brainstorm` all start the skill.
- The owner's personal Claude organization is the one the build VM's Claude Code syncs (`~/.claude/plugins/synced/`); its manifest shows which `dia` the account holds.

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
