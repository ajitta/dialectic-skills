# Surface probes

Results of the probes in `docs/spec.md` §12.2. Each run is n=1 unless stated; any generalization from it is marked as such.

## Setup (2026-10-20)

- Plugin `dia` 0.1.0, built by `tools/package.py`.
- Claude Code 2.1.303, headless `claude -p --plugin-dir plugins/dia --model sonnet` (claude-sonnet-5-5).
  - Every run used its own fresh `CLAUDE_CONFIG_DIR` holding only the OAuth credentials. Without that, Claude Code syncs the account's claude.ai plugins and skills (the old `socratic` plugin and `reductio`, `negative-dialectics`, `self-refine`, `recursive-refine`, `confirm-intent`) into the session within one run, and they compete with `dia`. A first batch was discarded for this reason. In every counted run, the init event listed no `@synced` plugin.
  - `CLAUDE_CODE_SYNC_PLUGINS=0` and `CLAUDE_CODE_SYNC_SKILLS=0` did not stop the sync.
  - The baseline arm `old` is a plugin built from `upstream/` (the seven skills the dia skills were rebuilt from). It runs in the same isolated way.
- Codex CLI 0.162.1 with an isolated `CODEX_HOME`.

## Results

| # | Probe | Result | Status |
|---|---|---|---|
| P1 | claude.ai upload of `dialectic-skills.zip` | not run (owner) | open |
| P2 | Claude mobile, one natural-language prompt per skill | not run (owner) | open |
| P3 | Codex CLI plugin install | pass, with a naming finding (below) | done |
| P4 | ChatGPT desktop (Pro) local plugin install | not run (owner) | open |
| P5 | ChatGPT mobile (Pro) | not run (owner) | open |
| P6 | First-word invocation | pass | done |
| P7 | Routing baseline, n=2 | pass: no drop | done |
| P8 | Tool-less run | pass after a fix to dia-refine | done |
| P9 | `references/ko/` loading | not applicable until O1 adds a ko file | open |

### P3: Codex CLI 0.162.1

- `codex plugin marketplace add <repo path>` read `.claude-plugin/marketplace.json`, and `codex plugin add dia@dialectic-skills` installed version 0.1.0. No root `plugin.json` was needed.
- The model-visible skill list (`codex debug prompt-input`) holds `dia:dia-negative`, `dia:dia-reductio` and `dia:dia-refine` only. The four skills with `allow_implicit_invocation: false` are absent, so the policy holds.
- **Naming:** Codex namespaces plugin skills. `$dia:dia-intent` loaded the skill, and the reply followed its review format. `$dia-intent` did not resolve; the model reported that it could not access the skill. `$dia-<x>` is the name only for a folder copied to `~/.agents/skills/`. Spec §4 and the README now give `$dia:dia-<x>` for the plugin route.
- Adding a portable root `plugins/dia/plugin.json` did not change the names (still `dia:dia-*`). Spec D16 therefore ships no root manifest.
- Not covered: the GitHub `owner/repo` marketplace source (the repository is private), and whether `default_prompt` in `agents/openai.yaml` (`Use $dia-<x> …`) resolves in the Codex app or ChatGPT desktop. Check it in P4.

### P6: first-word invocation (dia arm, tools available)

| Prompt | Skill loaded | Pass |
|---|---|---|
| `dia-refine — check the numbers` + draft | `dia:dia-refine` | yes |
| `dia-iterate --max 2` + draft | `dia:dia-iterate` | yes |
| `please refine this paragraph: …` | none | yes |
| sentence mentioning dia-refine in the middle, then an unrelated question | none; the reply said the mention was not an invocation | yes |

### P7: routing, n=2 per cell

Prompts: reductio («귀류법으로 이 주장을 검토해줘: …» / "Use proof by contradiction on …"); negative («부정의 변증법으로 이 문장을 비판해줘: …» / "Do an immanent critique of …"); elenchus («소크라테스 대화법으로 따져줘. …» / "Socratic dialogue please, make me define it first. …"); brainstorm («소크라테스식 브레인스토밍 해줘. …» / "Socratic brainstorm with me: …").

| Skill | ko, dia | ko, old | en, dia | en, old |
|---|---|---|---|---|
| reductio | 2/2 | 2/2 | 2/2 | 2/2 |
| negative | 2/2 | 2/2 | 2/2 | 2/2 |
| elenchus | 2/2 | 2/2 | 2/2 | 2/2 |
| brainstorm | 2/2 | 2/2 | 2/2 | 2/2 |

Removing the Hangul trigger terms from the dia-reductio and dia-negative descriptions caused no routing drop in Claude Code at n=2 (L7). Every Korean prompt whose reply was visible got a Korean reply: elenchus and brainstorm in the P7 runs, plus one longer run each for reductio and negative.

### P8: tool-less run (`--tools Skill`: no search, fetch, code or file tools)

Draft under test: "The Eiffel Tower was completed in 1889 and is about 330 m tall. Python 3.13 removed the GIL by default. 17 x 23 = 391." The Python sentence is wrong.

- **dia-iterate**, 2 runs: both stopped after round 1 with "verification exhausted". Each changed nothing and listed every claim as unverified, with what would make it checkable. Pass.
- **dia-refine, first build**, 1 run: failed.
  - It filed the Python sentence under "confirmed errors" and rewrote it from recall.
  - The baseline `self-refine` did the same in 2 of 2 runs, so the defect came from the reference skill.
  - The cause was a conflict between two rules. Step 3 said unchecked items stay as drafted. The output rule allowed changing a single-right-answer result without external verification if both versions are shown side by side.
- **dia-refine, fixed**, 3 runs: all three kept the draft's wording and put the suspected correction under ④. Pass.
  - The fix says that recall is not verification.
  - It lists what counts as a confirmed basis: a tool that ran, the user's instructions or supplied material, or your own re-derivation.
  - It sends an unchecked suspected error to ④ with the suspected correction.
  - It limits the side-by-side rule to the case where your own re-derivation changes a result.

Observations (n=1, not acted on):

- In one run with tools available but search permission denied, dia-refine kept the wording and also added an inline "(unverified; …)" note in the revision.
- That same run replied in Korean to an English prompt. The skill says to reply in the language of the user's latest message. The host's Korean locale may be the cause; this is not established.
- In headless mode the Read tool needs approval, so some runs could not open `references/*.md` and worked from the SKILL.md body alone.
