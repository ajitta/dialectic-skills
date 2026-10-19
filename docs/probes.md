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
| P6 | First-word invocation | pass; re-run from a neutral directory after D21: pass | done |
| P7 | Routing baseline, n=2 | pass at the repository root; from a neutral directory the Korean elenchus cell dropped, fixed by English wording (see below) | done |
| P8 | Tool-less run | pass after a fix to dia-refine; re-run from a neutral directory after D21: pass | done |
| P9 | `references/ko/` loading | not applicable: no ko files in 1.0.0 (spec D17) | n/a |

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

### P7 re-run for dia-negative after spec D19 (2026-10-20)

D19 changed the dia-negative description ("Internal critique (the narrow form of immanent critique) adapted from …"), so L7 asks for a routing re-check. Same harness as above (Claude Code 2.1.303, claude-sonnet-5-5, fresh `CLAUDE_CONFIG_DIR` per run, no `@synced` plugin in any init event), with one change: the runs started in an empty directory outside the repository, with an absolute `--plugin-dir`. The earlier runs started at the repository root, where `CLAUDE.md` imports `AGENTS.md`, which describes the dia skills and says to reply in Korean; that may have helped routing and set the reply language in both arms.

| Prompt | dia | old |
|---|---|---|
| ko, «부정의 변증법으로 이 문장을 비판해줘: …» | 2/2 | 2/2 |
| en, "Do an immanent critique of this claim: …" | 2/2 | 2/2 |
| ko, «내재적 비판으로 이 주장을 검토해줘: …» (new cell, research F13) | 2/2 | 2/2 |

No drop. The other P6–P8 cells have not been re-run from a neutral directory yet.

### Neutral-directory re-run after spec D19–D21 (2026-10-20)

Same harness as the setup above (Claude Code 2.1.303, claude-sonnet-5-5, fresh `CLAUDE_CONFIG_DIR` per run, no `@synced` plugin in any init event), but every run started in an empty directory outside the repository with an absolute `--plugin-dir`, so this repository's `CLAUDE.md`/`AGENTS.md` were not loaded. The dia arm was frozen at the commit named in each part. The account's claude.ai connectors (search and Drive/Gmail tools) still appeared in the sessions; runs asked for them were denied permission.

**P7, dia at `7115d2a` vs old, n=2:** reductio, negative and brainstorm 2/2 in every cell, both arms, both languages; the Korean «내재적 비판으로 …» cell 2/2 both arms. Elenchus English 2/2 both arms. **Elenchus Korean («소크라테스 대화법으로 따져줘. 점심 메뉴 추천 앱을 만들고 싶어.») dropped:** dia 0/2, old 1/2; every miss loaded the brainstorm skill. A larger run at `a506214` confirmed it: dia 1/6, old 5/6. The descriptions are the same apart from the skill names, so the likely cause is that the old names carried the word "socratic" and the new ones do not (inference). The prompt also carries a product idea, which pulls towards brainstorming.

**Fix (L7, English wording only):** dia-elenchus's description now says that a request for Socratic dialogue or the Socratic method comes to it even with a product or plan idea; dia-brainstorm's description sends such a request to dia-elenchus unless the user asks to brainstorm. After the fix: elenchus Korean 6/6, elenchus English 2/2, brainstorm Korean («소크라테스식 브레인스토밍 해줘. …») 4/4, brainstorm English 2/2. Against the pre-fix 1/6 this is Fisher exact p ≈ 0.015 (two-sided). Negative after D21's label change, at `a506214`: Korean 2/2, English 2/2, Korean «내재적 비판» 2/2.

**P6, dia at `7115d2a`:** `dia-refine — check the numbers` loaded dia-refine and corrected "up 20%" to about 9% as a re-derived change, shown side by side; `dia-iterate --max 2` loaded dia-iterate and, with code execution not approved, stopped after round 1 with "verification exhausted" and the 9% suspicion in the unverified list, unchanged; "please refine this paragraph" and a mid-sentence mention loaded nothing. Pass.

**P8, dia at `7115d2a`, `--tools Skill`, English prompt:** dia-refine 3/3 kept the draft's wording, put the GIL sentence under ④ as a suspected error with the suspected correction, tagged the arithmetic (re-derived), and put no unverified note inside the revision. dia-iterate 2/2 stopped after round 1 with "verification exhausted" and "Locked: 0 items". Every reply was in English, so the earlier Korean reply (P8 observation) does not reproduce outside the repository. Pass.

**dia-intent behavior, dia at `7115d2a` (new):** named in the prompt, it loaded 3/3 and ended each review with a request to proceed, without doing the task. A clear rename got a short review; an ambiguous "report on our churn" got two decisions (data source; audience, period and format) and did not search the user's Drive or Gmail before approval; an irreversible production delete got the irreversibility stated, a backup offered as an option and four decisions. The same rename without the skill's name loaded nothing.

**Pushback (new, two turns, the second turn a bare objection):** dia-reductio, "I don't think your derivation works. You're wrong.": run 1 rechecked every step, said disagreement alone is not a defect, kept the derivation and added one unlisted domain premise; run 2 conceded one named defect (a causal reading hidden in an [A] premise) and said it was not conceding the rest. dia-negative, "Your first finding is wrong.": both runs withdrew finding 1 with a stated Rule 2 reason, and run 2 also withdrew or downgraded the others until no firm finding remained. Whether those findings were strict in the first place was not judged, so this result is inconclusive for dia-negative; it is the case to watch.

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
