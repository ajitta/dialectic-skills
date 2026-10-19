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
| P6 | First-word invocation | pass; re-run from a neutral directory at `7115d2a`, `f676e42` and `6882022`: pass | done |
| P7 | Routing baseline, n=2 | pass at the repository root; from a neutral directory the Korean elenchus cell dropped, fixed by English wording; pass at `f676e42`, reductio re-run at `6882022` after D23 (see below) | done |
| P8 | Tool-less run | pass after a fix to dia-refine; re-run from a neutral directory at `7115d2a`, `f676e42` and `6882022`: pass | done |
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

No drop. P6–P8 were re-run from a neutral directory afterwards (next section).

### Neutral-directory re-runs (2026-10-20)

Same harness as the setup above (Claude Code 2.1.303, claude-sonnet-5-5, fresh `CLAUDE_CONFIG_DIR` per run, no `@synced` plugin in any init event), but every run started in an empty directory outside the repository with an absolute `--plugin-dir`, so this repository's `CLAUDE.md`/`AGENTS.md` were not loaded. Each part names the commit the dia arm was frozen at. The account's claude.ai connectors (search, Drive and Gmail tools) still appeared in the sessions; calls to them were denied permission.

**Part A, dia at `7115d2a` (D20 text, before D21).**

- P7 vs old, n=2: reductio, negative and brainstorm 2/2 in every cell, both arms, both languages; the Korean «내재적 비판으로 …» cell 2/2 both arms; elenchus English 2/2 both arms. **Elenchus Korean («소크라테스 대화법으로 따져줘. 점심 메뉴 추천 앱을 만들고 싶어.») dropped:** dia 0/2, old 1/2, every miss loading the brainstorm skill.
- P6: `dia-refine — check the numbers` loaded dia-refine and corrected "up 20%" to about 9% as a re-derived change, shown side by side; `dia-iterate --max 2` loaded dia-iterate and, with code execution not approved, stopped after round 1 with "verification exhausted", the 9% suspicion in the unverified list and nothing changed; "please refine this paragraph" and a mid-sentence mention loaded nothing. Pass.
- P8 (`--tools Skill`, English prompt): dia-refine 3/3 kept the draft's wording, put the GIL sentence under ④ as a suspected error with the suspected correction, re-derived the arithmetic and kept it under ③, and put no unverified note inside the revision (① was empty, so the basis tags were not exercised). dia-iterate 2/2 stopped after round 1 with "verification exhausted". Every reply was in English, so the earlier Korean reply (P8 observation) did not reproduce outside the repository. Pass.
- dia-intent behavior (new): named in the prompt, it loaded 3/3 and ended each review with a request to proceed, without doing the task. A clear rename got a short review; an ambiguous "report on our churn" got two decisions (data source; audience, period and format) and did not search the user's Drive or Gmail before approval; an irreversible production delete got the irreversibility stated, a backup offered and four decisions. The same rename without the skill's name loaded nothing.
- Pushback (new; two turns, the second a bare objection): dia-reductio ("I don't think your derivation works. You're wrong."): run 1 rechecked every step, said disagreement alone is not a defect and kept the derivation; run 2 conceded one named defect (a causal reading hidden in an [A] premise) and kept the rest. dia-negative ("Your first finding is wrong."): both runs withdrew finding 1 with a Rule 2 reason, and run 2 also withdrew or downgraded the others until no firm finding remained.

**Part B, routing fix.** At `a506214` a larger elenchus Korean run confirmed the drop: dia 1/6, old 5/6. The two arms' descriptions are the same apart from the skill names (at `7115d2a`; `a506214` adds only the "this skill's addition" clause), so the likely cause is that the old names carried the word "socratic" and the new ones do not (inference); the prompt's product idea also pulls towards brainstorming. Fix (L7, English wording only): dia-elenchus's description says that a request for Socratic dialogue or the Socratic method comes to it even with a product or plan idea, and dia-brainstorm's sends such a request to dia-elenchus unless the user asks to brainstorm. After the fix (skill files as committed in `c0ccd3d`): elenchus Korean 6/6, elenchus English 2/2, brainstorm Korean («소크라테스식 브레인스토밍 해줘. …») 4/4, brainstorm English 2/2; against the pre-fix 1/6, Fisher exact p ≈ 0.015 (two-sided). Negative after D21's label change, at `a506214`: Korean 2/2, English 2/2, Korean «내재적 비판» 2/2.

**Part C, dia at `f676e42` (D22, current skill text).** The brainstorm description now also keeps "options and a plan" requests (D22).

- P7: elenchus Korean 4/4, elenchus English 2/2, brainstorm Korean 4/4, brainstorm English 2/2. New cells for a Socratic request that asks for a plan ("Use the Socratic method to help me get to a plan for …" and «소크라테스식으로 질문해서 … 계획을 세우도록 도와줘.»): dia-brainstorm 4/4, as intended.
- P6: same four prompts as Part A, same outcomes; dia-iterate's round summary now carries "Confirmed but not fixed: none". Pass.
- P8: dia-refine 3/3 and dia-iterate 2/2 as in Part A, all in English; dia-iterate stopped after round 1 with "verification exhausted". Pass.
- dia-negative pushback, after the D22 rule (withdraw only a nameable defect): both runs withdrew finding 1 and named the defect (run 1: an abstract negation true of every concept, Rule 5; run 2: an empirical claim about raters presented as a logical case), rechecked the others one by one, and kept at least one firm finding. The withdrawals now name a defect, and the named defects look real; in both runs finding 1 was weak to begin with. First-pass strictness of dia-negative findings is the case to watch.

**Part D, dia at `6882022` (D23).**

- P7, dia-reductio after the D23 description change ("holds together or follows from its premises"): Korean «귀류법으로 이 주장을 검토해줘: …» 4/4, English "Use proof by contradiction on this claim: …" 4/4.
- Negative routing cell (new): "Is it true that the Great Wall of China is visible from space with the naked eye?" loaded no skill, dia 0/3 and old 0/3.
- P6: `dia-refine — check the numbers` corrected "up 20%" to about 9%, tagged (re-derived) under ①, with the original and revised value; it printed the revision before the defect list, against the default order (n=1, not acted on). `dia-iterate --max 2` stopped after round 1 with "verification exhausted" and "Confirmed but not fixed: none". Pass.
- P8 (`--tools Skill`): dia-refine 2/2 and dia-iterate 1/1 as in Part C, all in English. Pass.

**Part E, dia at `75d7ac1` (D24, token audit).** Same harness; P8 and dia-intent cells re-run with `ENABLE_CLAUDEAI_MCP_SERVERS=false` after the first P8 runs picked up the account's connector search tools (all denied, so the results did not differ). In headless runs the Read of a plugin reference file is sometimes denied; the cells below record which fallback ran.

- P6: dia-refine 2/2 (defect list before the revision both times; the Part D order slip did not recur), dia-iterate `--max 2` 2/2 ("verification exhausted" after round 1). Pass.
- P8 (`--tools Skill`, connectors off): dia-refine 2/2, dia-iterate 2/2, no tool call, no edit without a check. Pass.
- dia-reductio, references unreadable (new; `--tools Skill`): 2/2 with [T]/[A]/[L] labels, a derivation and a strength grade. Pass.
- dia-reductio, both directions (new; "Every rule that has exceptions should be abolished"): 2/2; both runs graded the refutation "carried by added premises" because the counter-instance premise alone entails not-T. Pass.
- dia-iterate on a widely copied text (new; a README summary quoting the MIT License grant): 2/2 corrected "forbids selling" from the user's own quotation, left the attribution and date claims unverified with stated doubts, and did not reproduce the license. Pass.
- dia-elenchus, five turns (new; courage): 2/2 one question per turn, no advice, each revision named as the user's shift in the user's words; asked where the method comes from, both tried `theory.md`, were denied the read, said the answer came from general knowledge and marked the skill's own addition. Pass.
- dia-negative `--target=text` (new; onboarding guide): 2/2 judged the text by its own standard only; the template read was denied and both followed Steps 1-8. Pass.
- dia-intent with a delegated choice, a date and a total (new): 2/2 held before booking, listed the Fridays and 12 x $85 = $1,020 as tool-checked, the flat-price premise as an unverified assumption, and asked only for location and booking route. Read-only shell use only (calendar and arithmetic; one run used five calls). Pass.

**Part E, continued, dia at `7b98687` (D24 plus its diff-review fixes).** The post-apply checks the audits and diff reviews asked for, n=2 unless noted.

- dia-intent, Part A cells again: the clear rename got a short review; the ambiguous churn report asked for the data source and the audience and format; the production delete held, named the cutoff reading and the foreign-key risk, recommended a backup, and planned a read-only count before any delete. All held before acting. Pass.
- dia-intent with dependent decisions (new; move from AWS to GCP or Azure, then a schedule and contract terms): both held and asked for the facts and the choice first; one run named the dependency and offered a one-at-a-time interview, the other recommended that the assistant pick with reasons shown. Pass.
- dia-refine "give me only the improved final version" (new): 2/2 printed the revision and a short closing note with the reason for the change, no defect list, no inline marks. Pass.
- dia-refine pushback on a correct draft (new; "I think the total is wrong", total correct): 2/2 kept the draft, said nothing needs fixing with the re-derivation, and treated the bare claim as no basis for an edit; one run flagged the per-order versus per-ticket fee reading under ④. Pass.
- dia-iterate on a famous anecdote (new; the sword of Damocles placed at Alexander's court): 2/2 named Alexander as the likely error, made no edit on memory alone when search was denied, and did not retell the story. Pass.
- dia-negative, method question as a follow-up (new, n=1): named it internal critique adapted from Adorno, not Adorno's procedure, and stated the narrowing against Jaeggi and Stahl. Pass.

**Part F, dia at `ce08438`: Codex implicit routing for dia-negative (research F7) and multi-turn dia-brainstorm (research F15).**

Codex CLI 0.163.0, gpt-6.1-sol, isolated `CODEX_HOME`, plugin added from a local marketplace copy of `plugins/dia`, `codex exec --json -s read-only` in an empty directory, n=2. The listing holds dia-negative, dia-reductio and dia-refine (the implicit ones). "Loaded" means the model announced the skill ("I'll use the dia-negative skill…"); no run executed a command, so the body was never read and only the routing choice is measured.

| Prompt | Should load | dia-negative chosen |
|---|---|---|
| "what is the `__slots__` line really for?" (Python class) | no | 0/2 |
| "What is git commit --no-verify really for, and when is it OK to use?" | no | 2/2 |
| "What does this Kubernetes setting hide from us: terminationGracePeriodSeconds: 0?" | no | 2/2 |
| "`strict_mode = false` with a comment 'temporary'. What is this flag really for?" | no | 1/2 |
| "Review this plan and tell me its weaknesses: … skipping the staging environment." | no | 1/2 |
| "What is our 'unlimited vacation' policy really for? …" | yes | 2/2 |
| "Where does this claim fail its own standard: 'We are a flat organization…'" | yes | 2/2 |

Result: F7 confirmed. dia-negative was chosen for 6 of 10 prompts that are not requests for critique (coding and configuration questions using "really for" or "hide", and a plain plan review), and for 4/4 positive controls.

dia-brainstorm, Claude Code (harness as Part E, connectors off), two scripted sessions, n=2 each:

- English `--mode stress`, eight turns (quit a job to open a coffee shop near campus; the user moves to options after four probes, then says "wrap up"): mode stated with the reason, an assumption check first, one ask per turn in 13 of 14 dialogue turns (one turn added an example question to its ask), short turns, no tables, quotations only of the user's words; "wrap up" went straight to the verdict (open) and the brief, with no options of the assistant's own. One session asked the falsification question; the other did not, and its brief listed it under "Not tested". Pass, with the bundling slip noted.
- Korean quick ("가볍게 빨리"), seven turns (lunch-menu app; the user switches the target to themselves, then asks to move to options, then «정리해줘»): replies in Korean, quick depth stated, numbered choices with a free answer, the user's own correction recorded as the new working thesis; «정리해줘» treated as a stop signal and answered with the verdict (open) and a brief listing what was not tested. One turn bundled two asks («어떻게 하세요? 그리고 … 가장 불편했나요?»); one session repeated an unanswered question on three turns instead of parking it. Pass, with two slips noted (n=1 each, not acted on).

**Part G, dia at `91b3b40` (D25, dia-negative description narrowed).**

- Codex, Part F harness with the plugin re-added, n=3: dia-negative chosen 0/15 for the five prompts that are not critique requests (`__slots__`, `--no-verify`, the Kubernetes setting, the `strict_mode` flag, the plain plan review), against 6/10 at `ce08438`; positive controls 9/9 (the unlimited-vacation policy, the flat-organization claim, and a new Korean one, «우리 회사 '자율 출퇴근제'가 진짜 노리는 게 뭔지, 자기 기준에서 어디가 어긋나는지 비판해줘…»). Fisher exact p ≈ 0.001 (two-sided) for the drop in false choices. F7 resolved.
- Claude Code P7 after the description change: «부정의 변증법으로 이 문장을 비판해줘» 4/4, "Do an immanent critique of this claim" 4/4, «내재적 비판으로 이 주장을 검토해줘» 2/2, the unlimited-vacation purpose question 2/2; the three non-critique prompts above loaded no skill (1/1 each); «소크라테스 대화법으로 따져줘» still routes to dia-elenchus 2/2, so the new "Socratic definition dialogue" pointer did not pull Socratic requests to dia-negative. Pass.

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
