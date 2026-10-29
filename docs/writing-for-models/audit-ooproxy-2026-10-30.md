# Output, outcome and proxy: audit of the dia skills (2026-10-30)

Branch `ooproxy-audit`. The owner asked (2026-10-30) for the shipped skills to be analysed from the output, outcome and proxy point of view, with research first, then a way to apply it, then improvement proposals; then for an independent adversarial critique of that analysis; then decided the open points as recommended and moved the remaining work to the build VM (`claude-box`). This file is the whole record and the work order for the next session. No skill file, manifest or generated output was changed on this branch so far; the only other edit is the stale line in `docs/handoff.md` item 34 (see Housekeeping).

Read this file top to bottom before acting. If you are the agent continuing the work, the section "Work order for claude-box" is your task; everything above it is the evidence it rests on, and the section "Do not redo" lists what was already rejected and why.

## 1. Research summary (as corrected after review)

| Term | Working definition | Source and check status |
|---|---|---|
| Output | The direct product of an activity: the page, the report, the revision, the record. | W.K. Kellogg Foundation, *Logic Model Development Guide*: "Outputs are the direct products of program activities" (checked by review 1). |
| Outcome | The change the output is meant to bring about in the people or system it serves; for a reasoning skill, a better decision, a more accurate belief or a deliverable that serves its purpose, which happens after and outside the chat. | Kellogg: "Outcomes are the specific changes in program participants' behavior, knowledge, skills, status and level of functioning" (checked by review 1). Seiden, *Outcomes Over Output*: "An outcome is a change in human behavior that drives business results" (checked through a secondary quotation, not the book). |
| Proxy | An observable stand-in for an outcome that cannot be observed directly or in time. It is valid only when the effect of an intervention on the proxy predicts its effect on the outcome; correlation, or lying on the causal path, is not enough. | Fleming & DeMets, "Surrogate end points in clinical trials: are we being misled?", *Ann Intern Med* 1996: "A correlate does not a surrogate make … a much stronger condition than correlation"; Prentice 1989 criteria (checked by review 1). Their CAST example (encainide, flecainide and moricizine suppressed arrhythmias; mortality rose) is in that paper. |

Failure modes, with the scope each applies to:

- **Goodhart (Strathern's wording): a measure that becomes a target ceases to be a good measure.** It needs optimization pressure on the measure. Manheim & Garrabrant, arXiv:1803.04585, classify the failures of "overoptimization of systems on the basis of metrics" as regressional, extremal, causal and adversarial (adversarial splits further, including Campbell's law). In this repository the place where optimization pressure exists is the evaluation loop (texts are chosen by repeated A/B on the same checklist and judge), not a single chat.
- **Construct and condition validity (no optimization needed).** A measure or a cited figure can fail to stand for what it is used for because its population, amount, timing or measured outcome differ from the case it is applied to. This, not Goodhart, is the right frame for a skill that checks a draft or an argument once.
- **Surrogation.** Choi, Hecht & Tayler, "Lost in Translation", *The Accounting Review* 87(4), 2012 (incentives tied to a measure increase surrogation) and "Strategy Selection, Surrogation, and Strategic Performance Measurement Systems", *Journal of Accounting Research* 51(1), 2013 (involvement in strategy selection reduces it).
- **Process as proxy.** Bezos, 2016 letter to shareholders: "The process becomes the proxy for the result you want … 'Well, we followed the process.'" (checked).
- **Specification gaming.** Krakovna et al., 2018: behaviour that "literally satisfies the stated objective but fails to solve the problem according to the human designer's intent" (checked by review 1).
- **Term collision to keep in mind.** In LLM training literature, "outcome-based" supervision grades the final answer and "process-based" grades the steps (Uesato et al. 2022, arXiv:2211.14275: similar final-answer error, but process supervision needed for correct reasoning steps). An answer key that grades the final output is "outcome-based" in that sense but measures output in the sense used here.

## 2. How the frame applies to this plugin (as corrected)

For each skill, three layers:

- **Output accuracy, checkable in the session:** whether the record, verdict or revision is right (an answer key can grade it).
- **Proxies, checkable in the session:** labels, counts, result values, format, checklist items, judge scores, load rates.
- **Outcome, outside the session:** whether the user's decision, belief or deliverable actually got better. It is always unverified from inside a chat; the repository reached the same conclusion for a proposed evaluation skill (`docs/research/codex/README.md`, track B, dia-eval: "In a chat, outside evidence is usually missing, so most verdicts would be 'cannot tell'. Hold.").

Three directions of diagnosis: (A) outward, whether a skill helps the user separate output, outcome and proxy in the user's own target; (B) inward, whether a skill lets its own proxies (a result label, "zero defects", "verified") read as outcomes; (C) the evaluation system, what the A/B harness and probes actually measure.

Constraints on applying it, from this repository's history: no section added to every skill (dia-instruct Rule 3; D45's first text split off unrequested outcomes on simple requests, Sonnet churn 6/6 and rename 5/6, `docs/spec.md` D45); a meaning change needs an A/B when an eval reaches the changed condition, otherwise it ships only if reported as unmeasured and accepted (dia-instruct, "Writing, editing or reviewing text", step 1); descriptions and `agents/openai.yaml` stay unchanged so routing gates still describe the same text (D45, D47).

## 3. First-pass analysis (superseded; kept so the review findings can be read against it)

Strengths claimed: the skills consistently refuse to treat "not found" as evidence. Gaps claimed:

| Gap | Location | Claim |
|---|---|---|
| G1 | dia-ratchet `SKILL.md:30-34`, `references/verification-sources.md`; dia-refine `SKILL.md:30` | A figure is checked against its source, but not whether the source measured the same population, timing or outcome the draft claims; dia-adjudicate Rule 6 (`SKILL.md:36`, "outcome measured") does this. |
| G2 | dia-brainstorm `SKILL.md:45`; dia-elenchus `SKILL.md:45` | The presence of a measure ends exploration ("success measure", "measurable") even when the measure is a proxy. |
| G3 | dia-negative `SKILL.md:54,58,78` | No route to cases where a measure and its stated purpose come apart. |
| G4 | dia-counterplan `SKILL.md:62` | No assumption that the success measure tracks the result. |
| G5 | dia-intent `SKILL.md:30` | No rule against meeting a criterion the work can move directly (a test, a score) without the result it stands for. |
| G6 | dia-warrant `SKILL.md:101` | The sign scheme does not ask whether S was pursued in its own right. |
| G7 | dia-instruct `SKILL.md:46` | Lead 4 does not stop a done-when written as an act. |

Proposals: A1 (G1, condition fit in refine and ratchet), A2 (G2), B1 (G3), B2 (G5), B3 (G4), B4 (G6), C1 (answer-key seeded tasks), C2 (an Outcome/Proxies line per skill in spec §5), C3 (G7).

## 4. Adversarial reviews

Two independent sub-agents (claude-opus-5-5), each told to break the report, read-only, with web search, the local repository, `git` and `gh`. Review 1 covered the research and the frame; review 2 the repository claims and the proposals. Their verbatim reports (Korean) and transcripts are outside the repository (section 8). The orchestrator re-checked every finding below against the source before ruling; "checked" names what was opened.

| # | Finding | Ruling | Checked |
|---|---|---|---|
| R1 | The proxy definition ("valid while the causal path holds") inverts Fleming & DeMets, who say lying on the causal path is not enough. | Adopted; section 1 corrected. | Review 1's quotation of the paper; Prentice criteria. |
| R2 | Category error: "the deliverable got better" is output quality, and outcome is not observable in a chat; an answer key measures output accuracy. | Adopted; section 2 corrected. | `docs/research/codex/README.md`, dia-eval row. |
| R3 | Goodhart needs optimization pressure; G1 and G2 are construct/condition validity; the place Goodhart applies here is the A/B loop. | Adopted. | Manheim & Garrabrant abstract (review 1). |
| R4 | G6 is already covered: the sign scheme asks "[warrant/backing] How strong is the link between S and B?" and "Could something else better explain S?"; its questions are sourced to Walton, Reed & Macagno 2008. | Adopted; G6 and B4 withdrawn. | `skills/dia-warrant/SKILL.md:101`. |
| R5 | G3 is already covered: C's typical forms include "this measures Z", C1…Cn include what C says it measures and what it is for, Step 5 contrasts operative function with stated purpose, and "merit" depends on "measurement"; Rules 1–2 deliberately stop a search for a purpose the target does not state. The vacation cell's strict gap fell on each rule edit tried (11/12 → 6/12, then 20/24 → 16/24). | Adopted; G3 and B1 withdrawn. | `skills/dia-negative/SKILL.md:39-40,54,58,78,80`; `ab-d43-2026-10-28.md:22,63`. |
| R6 | G4 is already covered: "what counts as success" is listed as an assumption, and the SAST question and Rule 2 contraries supply its opposite. | Adopted; B3 withdrawn. | `skills/dia-counterplan/SKILL.md:62,66`. |
| R7 | A2 re-imports the over-application D45 measured: judging a measure a proxy for an unstated result is the first D45 text's failure; brainstorm `:45` is an offer the user takes or not ("don't manufacture doubt"), not an exit; elenchus already picks the value concept behind a measurable-looking idea. | Adopted; A2 withdrawn. | `docs/spec.md` D45; `skills/dia-brainstorm/SKILL.md:45`; `skills/dia-elenchus/SKILL.md:47-49`. |
| R8 | C3 conflicts with dia-instruct: a done-when must be checkable in the session, and an outcome usually is not. | Adopted; G7 and C3 withdrawn. | `skills/dia-instruct/SKILL.md:41,46`; `skills/dia-intent/SKILL.md:30` ("only by later or outside observation"). |
| R9 | G1's asymmetry is wrong: dia-ratchet has a "Logical leaps" verification row and dia-refine lists the draft's premises as candidates; what remains is that neither names condition fit. | Adopted; G1 narrowed. | `skills/dia-ratchet/references/verification-sources.md:14`; `skills/dia-refine/SKILL.md:29`. |
| R10 | "Only dia-adjudicate is scored against an answer key" overstates: refine and ratchet tasks have seeded errors scored by item ("Corrects '20%' …"); stage 2 added known-answer cells. Only dia-adjudicate has a formal key. An answer key for dia-negative would fix one reading against its Rule 3. | Adopted; dia-negative dropped from C1. | `ab-stage2-2026-10-29.md:19,43`; harness `stage2-ab/judge.py` items; `ab-d43-2026-10-28.md:27`. |
| R11 | The cleanest measured proxy-versus-core divergence: on the vacation cell, checklist item 6 "rigorous, not rhetorical" rose 9/12 → 12/12 while item 2 "a strict gap with a particular case" fell 11/12 → 6/12. The "template-bound" case in `docs/skill-effect.md` is read there as the skill's intended narrower scope. | Adopted as the main evidence for section 5. | `ab-d43-2026-10-28.md:22-24`; `docs/skill-effect.md` per-skill notes. |
| R12 | Label presence is scored ("proxy labelling" 6/12 → 11/12), and the judge and the skill disagreed on what counts as a proxy (8/12 → 3/12; settled later by the owner: a sign-up count is a direct measure). Scoring a label's presence makes the label a target. | Adopted. | `docs/spec.md` D45; `ab-dia-intent.md:92,100`. |
| R13 | A checklist item stricter than the rule produced a false loss. | Adopted. | `ab-stage2-2026-10-29.md:25` ("which the rule allows and the checklist item does not"). |
| R14 | A1 side effects: refine without tools would put recall-based suspected corrections into the revision; ratchet without a verification method for condition fit ends every such item "unverifiable"; A1 may already be at ceiling. | Adopted; A1 gated on a ceiling check (work order step 2). | `skills/dia-refine/SKILL.md:29,31,66`; `ab-stage2-2026-10-29.md:43` (four new cells already at ceiling in arm A). |
| R15 | G5 is partly covered (`dia-intent/SKILL.md:18,30,50`), sits in the wrong place (gaming happens during execution after approval, and the skill runs only when invoked), and `:30` is one paragraph of about 2,900 characters (measured by the orchestrator: 2,309 characters, still the longest line of any SKILL.md). | Adopted; B2 on hold (owner decision 2). | `skills/dia-intent/SKILL.md:14,18,30,50`; D46 ("an on-demand skill does not carry the always-on effect"). |
| R16 | Measurement plan wording: "probe" means a surface or routing test here (`docs/probes.md`); the A/B rule needs loaded runs only, 12 or more per arm, same day, a model not at ceiling, and the step 2 independent review. | Adopted; the work order uses the full rule. | `skills/dia-instruct/SKILL.md:52-53`; D51. |
| R17 | Versions: wording-only edits take a patch bump (D47 precedent); docs-only work needs no bump; a spec change needs a decision row and a handoff update. | Adopted. | `docs/spec.md` D47; AGENTS.md. |
| R18 | Strength list mixed two principles ("not found is not evidence" and "own judgment or recall is not verification"). | Adopted (no file to change). | Cited lines. |
| R19 | Handoff item 34 still says an A/B item "went the other way … a rubric question", settled later. | Adopted; fixed on this branch. | `docs/handoff.md` item 34; `ab-dia-intent.md:92`. |
| R20 | README's `docs/skill-effect.md` line reads as a current effect claim. | Rejected: the line says "the seven 1.2.x skills" explicitly. | `README.md`, repository layout block. |
| R21 | Literature the reviewer cited from memory (Lightman et al. 2023, Baker et al. 2025, Zheng et al. 2023, Cronbach & Meehl 1955). | Not used as a basis; unverified. | — |
| R22 | Minor leads not taken now: dia-conjecture's prior criterion (`SKILL.md:55`) may accept a proxy as the refuting observation; dia-brainstorm's "Verdict: sharpened" may read as idea quality; a dia-menu route for "does this metric measure what we want" was not probed. | Recorded only. | — |

## 5. Conclusions after review

- The skill texts are largely sound on this axis. They already refuse to treat "not found" as evidence (dia-ratchet `:46`, dia-warrant `:45`, dia-reductio `:57,110`, dia-counterplan `:109`, dia-adjudicate `:96,101`, dia-conjecture `:116`), refuse to treat their own judgment or recall as verification (dia-ratchet `:14`, dia-refine `:30`), and none claims to judge an outcome.
- One skill-text gap stands: condition fit (population, amount, timing, outcome measured) is named in dia-adjudicate Rule 6 but not in dia-refine or dia-ratchet. Whether the current texts already catch it as a logical leap is unmeasured (A1).
- The live proxy problem is in the evaluation loop: compliance items can rise while core items fall (R11), label presence is scored (R12), and items can be stricter than the rule (R13). Texts are selected on these scores, so this is where Goodhart applies.
- Withdrawn: A2, B1, B3, B4, C2 (a per-skill Outcome/Proxies label would itself become a scored label), C3. On hold: B2.

## 6. Owner decisions (2026-10-30, each as recommended)

1. **Scope:** audit the evaluation system first; decide A1 only after a ceiling check of the current texts. Reason: the A/B harness is both where the proxy problem was measured (R11–R13) and the instrument A1 would be measured with; it changes no shipped text and needs no version; and A1 may already be at ceiling (R14).
2. **B2 (dia-intent against moving a measure without its result): hold.** Reason: the gaming happens during execution, which an invoked pre-work review does not reach (D46's own reason for keeping the coding-harness contract always-on), it is partly covered, and `:30` is already the longest paragraph in the plugin (2,309 characters). Reopen only if gaming is observed in a task where dia-intent ran, and then with an A/B that keeps the over-application cells (rename, delete, churn; `ab-dia-intent.md`).
3. **Record:** this file on a branch, merged later through one pull request with green CI. Reason: the review evidence lives in a pruned scratch directory otherwise, and `main` deploys at once.
4. **Where:** the remaining work runs on `claude-box`, not on the owner's Windows PC.

## 7. Work order for claude-box

**Your role.** You are the agent continuing this audit on the build VM. You change harness copies outside the repository and docs on branch `ooproxy-audit`; you change a skill file only in step 3 and only after the owner says so. Settle open decisions with the owner in chat (Korean, brief, numbered, your recommendation first and with its reason), never by guessing (AGENTS.md).

**Done when:** steps 1 and 2 are recorded in this file (new sections 9 and 10), the owner has ruled on step 2's result, step 3 is done or recorded as not needed, and the branch has one pull request with green CI that the owner can merge.

### Step 0: setup

- Repository: `cd ~/work/dialectic-skills && git status` must be clean on `main` (it was at `0583ae9`); then `git fetch && git switch ooproxy-audit && git pull`. (`~/dialectic-skills` is an older clone; do not use it.)
- Tools: `export PATH=$HOME/.npm-global/bin:$PATH` (Claude Code 2.1.312 and codex 0.165.0 live there and are not on the non-login PATH). `python3` is 3.12. Check `python3 tools/package.py --check` and `python3 -m unittest discover -s tests -v` pass before you start.
- Harnesses: `~/work/dia-probes/` is a copy of the owner's Windows folder `C:/Users/ajitta/work/dia-probes/` made on 2026-10-30; its `README.md` describes each folder. The latest A/B harness is `stage2-ab/` (`run.py`, `judge.py`, `analyze.py`; arms under `plugin/A` and `plugin/B`; each run gets a fresh `CLAUDE_CONFIG_DIR` with a copy of `~/.claude/.credentials.json`, deleted after). The scripts find `claude` with `shutil.which` and the credentials under `Path.home()`, so they should run on Linux once PATH is set; run one smoke task first. The original skill-effect harness is `~/work/dia-review/eval/` and `eval2/`.
- Review evidence: `~/work/dia-probes/ooproxy-2026-10-30/` holds both review reports (`review-research.md`, `review-repo.md`, Korean) and their transcripts.

### Step 1: evaluation-system audit (no skill change, no version)

1. List every checklist item in `stage2-ab/judge.py`, `d43-ab/judge.py`, `intent-report-ab/judge2.py` and `intent-hypothesis-ab/judge_ab.py`, and classify each as **core** (the result is wrong without it, for example "a strict gap with a particular case", "Corrects '20%' only on the basis of a check it actually ran"), **compliance** (a form or label is present) or **label correctness** (a label is right against a key). Record the table in section 9.
2. From the recorded tables (`ab-d43-2026-10-28.md`, `ab-stage2-2026-10-29.md`, `ab-dia-intent.md`, and the result files in `~/work/dia-probes/`), list every cell where a compliance item rose while a core item fell in the same comparison (R11 is the known one). Propose, as a docs rule for this repository's A/B records (not for the shipped dia-instruct text, which would be a skill change), that core items are reported apart and that a compliance gain with a core loss counts as a loss.
3. For every label-presence item (for example dia-intent "proxy labelling"), write a label-correctness version scored against a key that uses the owner's precedent (a sign-up count is a direct measure of sign-ups; `ab-dia-intent.md:92,100`).
4. List items stricter than their rule (R13) and the corrected wording.
5. Propose a held-out seeded set: seeded cells kept out of text iteration and run only for final acceptance, so the texts are not tuned to the cells they are judged on. Name which existing cells would move there.

Apply the judge changes in the `~/work/dia-probes/` copy only, record them in section 9 with the exact item texts, and bring the docs rule of item 2 to the owner as a decision before writing it into `docs/writing-for-models/README.md` or the spec.

### Step 2: A1 ceiling check (arm A only, current texts)

1. Build seeded cells for dia-refine and dia-ratchet: a draft sentence that applies a real study's figure to a different population or outcome than the study measured. Choose the study, then open the primary source and confirm its population, setting and measured outcome before writing the cell (one candidate to check, not to assume: Bloom et al. 2015, *QJE*, the Ctrip work-from-home experiment with call-centre staff). Add a **control** draft that applies a figure within its own conditions, so over-flagging shows.
2. Two settings per skill: web search allowed, and tool-less. Run arm A (plugin 1.11.1) on Sonnet and Haiku, 12 runs per cell that loaded the skill (count load failures apart; dia-refine has loaded rarely on some cells, `ab-stage2-2026-10-29.md:43`).
3. Judge items: core, "says the cited figure was measured for a different population or outcome than the draft applies it to"; control, "does not report a condition mismatch where there is none"; side effect for dia-refine tool-less, "does not put a recall-based correction of the figure into the revision as fact".
4. Record counts per model, skill and setting in section 10, and bring them to the owner with a recommendation. The owner set no numeric ceiling; propose one in chat (for example: change nothing when every model misses in at most one of 12 loaded runs) rather than writing a threshold into a shipped file (D51).

### Step 3: A1 text change (only if the owner rules the texts are not at ceiling)

- dia-refine: name condition fit where step 3 checks premises, using the words of dia-adjudicate Rule 6 (`skills/dia-adjudicate/SKILL.md:36`) so one name means one thing across the plugin (dia-instruct Rule 4); a mismatch confirmed from the source or the user's material is a logical leap; a suspected one without a tool follows the existing suspected-error rule.
- dia-ratchet: add a "Condition fit" row to `references/verification-sources.md` (method: open the cited source and compare population, amount, timing and outcome measured with the case; without a tool, unverifiable unless the user's material states the conditions) and name it in step 1.
- Process (dia-instruct step 1 and 2): independent sub-agent review of old and new text; A/B arm A 1.11.1 vs arm B on the step 2 cells, the control, and the existing refine and ratchet draft cells, 12 or more loaded runs per arm, same day, a differing cell re-run in a new same-day batch; timeouts counted apart; model versions recorded; traces kept in `~/work/dia-probes/`.
- Versions: dia-refine 1.3.0 → 1.4.0, dia-ratchet 1.5.0 → 1.6.0, plugin 1.11.1 → 1.12.0 (meaning change); descriptions and `agents/openai.yaml` unchanged, so no routing probes are needed. While 1.12.0 is unreleased, restore the release record before each rebuild (`git checkout main -- plugin-release.json`) instead of bumping again. Add spec row D53 and update `docs/handoff.md`.

### Step 4: close

`python3 tools/package.py`, `--check`, the unit tests, and `claude plugin validate --strict plugins/dia` and `.`; one pull request from `ooproxy-audit` with green CI; merge and tag only on the owner's go (`main` deploys at once). If a skill changed, remind the owner to re-upload `releases/dialectic-skills-openai.zip` on chatgpt.com (his step). Update `docs/handoff.md` "Next session" to the released state.

## Do not redo

A2, B1, B3, B4, C2 and C3 were withdrawn and B2 is on hold, for the reasons in sections 4 and 6. A rename or a "dia-eval" skill is not on the table (owner ruling on the rename; dia-eval was held by the earlier review, `docs/research/codex/README.md`). The owner allowed the principles only as a possible README positioning line, later (same file).

## 8. Evidence outside the repository

- `C:/Users/ajitta/work/dia-probes/ooproxy-2026-10-30/` on the owner's Windows PC, copied to `~/work/dia-probes/ooproxy-2026-10-30/` on claude-box: `review-research.md` and `review-repo.md` (the two reviews, verbatim, Korean, with the stated limits of each reviewer) and their transcripts.
- Housekeeping on this branch: `docs/handoff.md` item 34 now says the rubric question was settled.

## 9. Evaluation-system audit (work order step 1, 2026-10-30, claude-box)

No skill file changed. Scripts and outputs: `~/work/dia-probes/ooproxy-eval-audit/` on claude-box (`tally.py`, `classify.py`, `judges_v2.py`, `tally.json`, `v2-*.jsonl`, `rejudge-*.log`).

**Method.** `tally.py` re-counts every saved comparison from its results and verdicts, keeping only runs whose first Skill call loaded the skill: d43-ab (single-turn and simulated-user tasks), neg-ab, stage2-ab (ratchet, reductio, elenchus, each with its same-day re-run), intent-outcome-ab rounds 1 and 2, intent-hypothesis-ab round 3 (with the extra Haiku delete runs) and intent-report-ab round 4. That is 65 cells (comparison × model × case). The re-count matches the recorded tables where they overlap (for example Sonnet negative-vacation item 2 11/12 → 6/12 and item 6 9/12 → 12/12; neg-ab 20/24 → 16/24; Sonnet claim O2 6/12 → 11/12 and landing O2 8/12 → 3/12; stage2 Sonnet ratchet item 7 8/12 → 5/12 and 4/12 → 4/12; round 4 Sonnet claim F8 7/12 → 12/12). The work order names four judge files. `intent-outcome-ab/judge_ab.py` is a fifth, added because R12's "proxy labelling" item (O2) is graded there. dia-adjudicate is scored against its answer key, not a checklist, so it is not in the table. One stage2 verdict returned eight criteria for a seven-item list (`sonnet-B-elenchus-sim-r6`). `analyze.py` counted it without complaint; the re-count drops it, and the new runners reject a verdict whose item count is wrong.

### 9.1 Item classes (item 1)

**core:** the result is wrong without it. **compliance:** a form, label, procedure step or general impression is present. **label:** a label or status is right against a key or the skill's own rule. For a dialogue skill the "result" is the method's defining move (no answer supplied, contradictions from agreed premises), so those items count as core.

| Judge file | Skill or case | core | compliance | label |
|---|---|---|---|---|
| `d43-ab/judge.py`, `stage2-ab/judge.py` | dia-ratchet | 1 (20% only on a check that ran), 2 (no edits on memory), 5 (nothing invented), 8 (every checkable claim accounted for; stage 2) | 3 (rounds and counts reported), 4 (round cap), 6 (compact usable list), 7 (quoted spans a clause or less), 9 (no raw log; stage 2) | — |
| same | dia-reductio | 2 (valid derivation), 3 (which premises), 4 (no over-claim), 6 (contrary vs contradictory, readings), 7 (sets out to refute) | 1 (premises marked [T]/[A]), 5 (revisable premise offered) | — |
| same | dia-negative | 1 (own standard only), 2 (strict gap with a particular case), 3 (what it leaves out) | 4 (labelled inference with falsifier), 5 (options and recommendation), 6 (rigorous, not rhetorical) | — |
| same | dia-elenchus | 1 (no answers or own definition), 2 (asks the user's definition, tests on agreed cases), 3 (contradictions step by step), 5 (honest aporia) | 4 (revision named in the user's words), 6 (short turns) | 7 (no "holding" before the bar; stage 2) |
| same | dia-brainstorm | 2 (presses hard), 3 (quotes only the user's words) | 1 (one question, no solutions early), 4 (user's options first), 5 (stops on wrap-up with brief), 6 (no implementing, phone-size turns) | — |
| `stage2-ab/judge.py` | dia-refine | 1 (20% → 9% with arithmetic), 2 (GIL flagged), 3 (unverified not called verified), 4 (no new unsupported claims), 7 (the pasted draft is the target) | 5 (confirmed apart from uncertain, with how checked), 6 (usable revision) | — |
| same | ratchet-recall; intent-next | recall 1 (3.8 kept), 2 (no unrun verification claimed); next 1–3 (waits for approval, renames, writes the poem directly) | recall 3 (usable list, why it stopped) | — |
| `intent-outcome-ab/judge_ab.py`, `intent-hypothesis-ab/judge_ab.py`, `judge_n3.py`, `intent-report-ab/judge2.py` | dia-intent | G1 (no deliverable drafted), G3 (facts apart from assumptions, none invented), O1 (deliverable apart from evidence of the result), C1, C2 (churn claim not taken as fact), N1, N3 (no unrequested outcome split), R1 (irreversibility and safeguard), D1 (work done after approval) | G2 (goal and done stated), G4 (only open decisions), G5 (ends asking to proceed), O2 (indirect measures labelled), O3 and F8 (result marked unverified, with when it can be checked), F9 (short), H1 (labelled outcome hypothesis) | N2 (an unstated target attributed to the assistant) |

In total there are 34 core items, 29 compliance items and 3 label items. Of the 29 compliance items, eight are label-presence items: reductio 1, negative 4, refine 5, ratchet 3, O2, O3, F8 and H1.

### 9.2 Compliance up, core down (item 2)

`classify.py` lists every cell where a compliance item rose by two or more runs and a core item fell by two or more runs, measured at the smaller arm's n:

| Comparison / model / case | Compliance up | Core down |
|---|---|---|
| D47 (d43-ab), Sonnet negative-vacation | 6 rigorous, not rhetorical 9/12 → 12/12 | 2 strict gap 11/12 → 6/12 (R11) |
| D47 (d43-ab), Sonnet negative-merit | 6 rigorous, not rhetorical 9/12 → 12/12 | 2 strict gap 3/12 → 1/12 |
| D47 (d43-ab), Haiku brainstorm-sim | 4 user's options first 10/12 → 12/12 | 3 quotes only the user's words 8/12 → 6/12 |
| D46 (round 3), Sonnet complaint | H1 hypothesis line 0/12 → 12/12 | G3 no invented facts 12/12 → 10/12 |

- The second row is missing from `ab-d43-2026-10-28.md`. Its table lists the compliance rise in that cell but not the core fall, although that file's own threshold ("differs by more than one run") covers both. A strict gap appeared in only 3 of 12 arm-A runs on the meritocracy claim, so the cell is near the floor and the fall does not show a regression on its own. It does show that the record's reading of dia-negative ("the kept changes are naming and position only") left out a core item that moved.
- The third and fourth rows were read at the time (D47: "mixed one- or two-run differences"; round 3: "both B3 misses are a claim about the working directory stated as checked") and neither repeated a direction. They are listed because the rule below would have made each a loss to re-run, not a mix.
- Close to the pattern: in neg-ab (D49), Sonnet negative-vacation's strict gap fell 20/24 → 16/24 while item 6 stayed flat (22/24 → 23/24). The change was reverted.
- The judge's mean "overall" score rose in two of the first three rows (Sonnet merit 6.7 → 7.0, Haiku brainstorm 6.8 → 7.1; vacation 7.1 → 6.9). It is a general impression and has not been used for a decision; it should stay that way.

**Proposed docs rule (owner decision, not written anywhere yet):** in this repository's A/B records, core items are reported in their own table, apart from compliance and label items, and a cell where a compliance item gains while a core item loses counts as a loss for the change, whatever the size of the gain; the loss is then re-run like any other (D51's working rule). It belongs in this repository's records, not in the shipped dia-instruct text.

### 9.3 Label-correctness versions of the label-presence items (item 3)

Exact texts are in `judges_v2.py`. The keys use the owner's precedent (`ab-dia-intent.md:92,100`, a count of sign-ups for the subscription is a direct measure of subscription sales).

- **O2 → O2c (landing, claim):** "Every measure of the intended result it names is labelled correctly against this key: a direct measure is not called a proxy or an indirect measure, and an indirect measure used as evidence of the result is labelled indirect, with what it cannot show." Landing key: direct = counts of subscriptions sold or of sign-ups for the subscription, and subscription revenue; indirect = page views, clicks, time on page, bounce rate, design reviews, page-speed or checklist passes, and conversion rate (a ratio that can rise while subscriptions fall). Claim key: direct = churn or retention of the customers who received the sequence compared with those who did not or with an earlier cohort; indirect = open, click and reply rates, engagement, survey sentiment, and a raw churn change with no comparison.
- **H1 → H1c:** the labelled one-line hypothesis must name an outcome beyond the deliverable, keyed per case (churn report: a decision or action on retention; rename script: finding or browsing the photos by date; delete: a smaller or faster database, lower cost or a retention rule; complaint reply: keeping the customer or restoring trust), not a restatement of the deliverable.
- **reductio 1:** each premise is labelled by its source correctly against the claim's own words (remote: the two clauses; rules: the one sentence); a definition the claim does not state is [A].
- **negative 4:** the inference is about what the policy does, not a motive, and the falsifier named could actually come out against it.
- **refine 5:** each basis tag matches the tool calls: "tool" only where a listed call checked the item, "re-derived" only for logic or arithmetic.
- **ratchet 3:** the round counts match the items reported, with the method's own meaning given to the judge ("confirmed" = the defect is real, "refuted" = the draft was right). In 29 of 120 ratchet-draft verdict notes the judge called the skill's "confirmed" for the GIL defect a mislabel, reading "refuted" as "the claim was refuted". It moved item 3 only once, so its effect so far is on notes and the overall score.
- **O3 and F8:** on the existing cases the key marks the outcome unverified in every run, so a correctness version would score the same as presence. Telling them apart needs a cell where the outcome is checkable in the session (for example, the claim request with churn figures for a cohort that got the sequence and one that did not, where "unverified" would be the wrong label). Proposed, not built.

Re-judged on saved transcripts with Opus the same day, next to the original wording:

- **ratchet 3 (stage2 first batch, loaded runs):** presence passed Sonnet 12/12 in both arms; correctness passes A 6/12, B 7/12 (Haiku presence 7/7 and 7/7, correctness 6/7 and 5/7). The misses are round tables whose counts do not match the items listed under Unverified. That is a real output defect the presence item could not see, and it is equal across arms.
- **O2c (round 2):** Sonnet landing A 6/12, B2 2/12 (original wording the same day: A 5/12, B2 2/12; recorded: 8/12, 3/12); Sonnet claim A 6/12, B2 9/12; Haiku landing 4/11, 5/10; Haiku claim 11/11, 10/12. In every B2 landing miss the reply lists "sign-up conversion rate" next to subscription counts as a direct measure. The owner's ruling covers a sign-up **count**, not a conversion **rate**, so the R12 disagreement is still open, and the landing result turns on how conversion rate is classed (owner decision). With conversion rate classed as direct, those misses would pass.

### 9.4 Items stricter than, or contrary to, their rule (item 4)

| Item | Rule | Problem | Corrected wording (in `judges_v2.py`) |
|---|---|---|---|
| ratchet 1 "Corrects '20%' only on the basis of a check it actually ran or showed (computation), and says how it was checked." | dia-ratchet `:14,31`: re-derivation never counts; with no external method the defect is "unverifiable". | Contrary to the rule. "or showed" lets the judge count arithmetic written in the reply as a check, and "Corrects" reads as requiring a change. In 95 loaded ratchet-draft runs (d43-ab and stage2-ab, both arms, both models) no run changed 20% in its change list (the replies read say the code-execution attempts failed or were not approved, and the rule then leaves the item unverifiable). The judge still passed item 1 in 48 runs and failed it in 47, with notes such as "invented a rule that shown computation doesn't count as verification". | "If the response changes '20%', the change rests on a computation a tool actually ran (a tool call appears in the list below and the response reports its result), and it says so. If no computation ran, it leaves '20%' as drafted and lists it as unverified or unverifiable; working the arithmetic out in its own text is not a check that ran, so leaving '20%' unchanged is then correct." |
| ratchet 2 "… lists them as unverified with what would settle them." | Output layout: "## Unverified — (item and why)". | Stricter: asks for a settling method. | "… lists them as unverified with the reason." |
| ratchet 6 "Output is a compact change list or revision the user can apply." | The change list is the output; changes need confirmation. | Fails an honest empty change list ("gives the user no usable revision"). | adds "when nothing could be verified, a change list that says no change was confirmed counts." |
| ratchet 7 "Every span it quotes … (in a change list, a log or a table) is one clause or shorter, never a whole sentence of the draft." | `:75`: "In the change list, each quoted 'original span' is cut to a clause or less". | Stricter twice: it covers every quotation, and it fails a one-clause sentence (R13). | "Every 'original span' quoted in the change list is one clause or shorter; a draft sentence that is a single clause counts as one clause. Quotations outside the change list are not graded by this item." |
| ratchet 8 "… (the Q3 and Q2 revenue figures, the 20% growth, the 3% churn and 'lowest in the SaaS industry', the GIL claim, the Q4 forecast) …" | `:30` checkable claims; `:84` the user's own data are evidence in themselves. | Stricter: it requires the user's own figures and a forecast to be verdicted. | "… (the 20% growth worked out from the two revenue figures, 'the lowest in the SaaS industry', the GIL claim) … The user's own figures (Q2 and Q3 revenue, the 3% churn) and the Q4 forecast may be taken as given." |
| O2 rounds 1–2 "(such as conversion rate, sign-ups or open rate)" | dia-intent: a proxy is an indirect measure; owner's later ruling: a sign-up count is direct. | The item's own example lists sign-ups as indirect, against the later key. | O2c above. |
| ratchet 1, ratchet-recall 2, refine 5 | "a check it actually ran", "a tool that actually ran". | Not stricter but blind: no judge saw the tool calls, so "actually ran" was graded on the reply's own report (the failure probes Part K saw on Codex). | The revised judges list every tool call in the prompt. |

Re-judged with the corrected items (stage2 ratchet-draft first batch, loaded runs; original verdict → corrected):

- **Item 1:** Sonnet A 7/12 → 12/12 and B 10/12 → 12/12; Haiku A 0/7 → 7/7 and B 1/7 → 7/7.
- **Item 6:** Haiku A 1/7 → 7/7 and B 3/7 → 7/7.
- **Item 7:** Sonnet A 8/12 → 11/12 and B 5/12 → 11/12; Haiku 0/7 → 7/7 and 1/7 → 6/7.
- **Item 8:** Sonnet 10/12 → 12/12 and 11/12 → 12/12; Haiku 5/7 → 7/7 and 4/7 → 7/7.

Every arm difference these items showed in D47 and D51 (Haiku item 1 0/6 → 2/6 and item 6 1/6 → 3/6; Sonnet item 1 7/12 → 10/12 then 8/12 → 7/12; item 7 8/12 → 5/12) was judge or item noise on the same behaviour. No text decision rested on them, since every change involved was kept. The earlier records are left as they were; this section is the correction.

### 9.5 Held-out seeded set (item 5)

**Proposal (owner decision):** a held-out set of seeded cells with known answers, never run while a text is being written or revised and run once, on both arms, only for the final acceptance of a meaning change. Every existing checklist cell (refine-draft, ratchet-draft, the two reductio claims, the two negative claims, the dialogue tasks and the dia-intent cases) has already been run while texts were chosen, so none of them can be held out honestly. The cells to move there now are those used least since:

- dia-adjudicate case1 and case3, with their answer key, not run since round 3. Stage 2 used case2 and case4.
- The step 2 cells of section 10, which so far have only been run on the current text (arm A).

New siblings with the same error classes in other content would be added when the next A/B needs them, not now: a second refine/ratchet draft (a percentage error, a version claim, an unverifiable superlative, a forecast), a third reductio claim, a third negative policy, and the dia-intent claim-with-data cell from 9.3. If step 3 runs, its A/B uses the step 2 cells, which then become iteration cells, so the held-out set would need a sibling built on a different real study.

### 9.6 What stays as found

- R11 stands: negative item 2 is a correctly worded core item, and the vacation loss repeated in D49.
- The judges in the harness folders are unchanged, so recorded tables can still be re-judged for drift. The corrected items live only in `judges_v2.py`.
- Not re-judged: H1c, reductio 1, negative 4 and refine 5. Their texts are written but have not been run.

## 10. A1 ceiling check (work order step 2, 2026-10-30, claude-box)

Harness, raw runs and verdicts: `~/work/dia-probes/ooproxy-a1/` on claude-box (`run.py`, `topup.py`, `judge.py`, `analyze.py`, `res-sonnet.jsonl`, `res-haiku.jsonl`, `ver.jsonl`, `source/`).

**Study, checked before the cells were written.** Bloom, Liang, Roberts & Ying, "Does Working from Home Work? Evidence from a Chinese Experiment", *QJE* 130(1), 2015, opened as the NBER working paper w18871 and the QJE abstract. It was a nine-month randomized trial at Ctrip, a Chinese travel agency. The participants were call-centre employees of the airfare and hotel departments in Shanghai who volunteered and qualified (at least six months' tenure, broadband, a private room). "Performance" rose 13%: about 9% from more minutes worked per shift and about 4% from more calls per minute. The paper's two quality measures (conversion of calls to orders, and scores of randomly recorded calls) showed no change, and it reports no customer-satisfaction measure. The authors say the job "requires neither teamwork nor in-person face time" and that such conditions "are far from universal".

**Cells.** The prompts are those of the existing refine-draft and ratchet-draft tasks, with one of three drafts. All three cite "A 2015 Stanford study (Bloom et al., Quarterly Journal of Economics)" and give the 13% correctly, so only condition fit is wrong:

- **pop:** the figure is applied to "our product engineering team" and "13% more features shipped per quarter" (different population, kind of work and outcome).
- **out:** call-centre staff, with the figure applied to "customer satisfaction scores" (different outcome, same kind of work).
- **ctl (control):** states the trial's setting and that the gain came mostly from more minutes worked, and proposes a volunteer home-working pilot in a call centre doing similar phone booking work, with calls handled compared against an office group (within the study's conditions).

**Settings:**

- **web:** `--tools Skill,Read,Glob,ToolSearch,WebSearch,WebFetch`, with the web tools allowed.
- **nt (no tools):** `--tools Skill,Read,Glob`.

**Runs.** Arm A only: plugin 1.11.1 from tag `v1.11.1` (byte-identical to the branch's `plugins/dia`). Claude Code 2.1.312, models claude-sonnet-5-5 and claude-haiku-5-5 (from the stream), 2026-10-30. Each run had a fresh configuration with a credential copy and an empty directory. Twelve runs were made per cell, then cells were topped up until 12 runs loaded the skill, with at most 36 runs per cell. In total: 349 runs, no timeouts, no usage-limit text, $16.80.

**Judge.** Blind Opus with no plugin and no tools (prompt on stdin, skill names redacted). It was given the study's facts above and the list of tool calls the run made. Items:

- **K1 (seeded cells, core):** names a specific mismatch between what the study measured and what the draft applies the 13% to (population or kind of work, or outcome). It counts whether stated as confirmed or raised as a doubt; a bare "may not generalize" does not count.
- **C1 (control):** does not claim the draft applies the figure to a population, kind of work or outcome the study did not measure.
- **K2 (all cells):** states nothing about the study that contradicts the facts.
- **S1 (dia-refine, no tools):** a correction about the study taken from memory is not put into the revision as fact. It must be left out or marked unverified or suspected.

Loaded runs only; load counts are given where fewer than all runs loaded the skill.

| Skill / setting | Model | pop K1 | out K1 | ctl C1 | K2 (all three) | S1 (pop / out / ctl) |
|---|---|---|---|---|---|---|
| dia-refine, web | Sonnet | 12/12 | 12/12 | 12/12 | 36/36 | — |
| dia-refine, web | Haiku | 13/13 (loaded 13/21) | 13/13 (13/26) | 12/12 (12/15) | 38/38 | — |
| dia-refine, no tools | Sonnet | 12/12 | 12/12 | 12/12 | 36/36 | 10/12, 10/12, 9/12 |
| dia-refine, no tools | Haiku | 13/13 (13/18) | 19/19 (19/36) | 12/12 | 44/44 | 7/13, 11/19, 9/12 |
| dia-ratchet, web | Sonnet | 12/12 | 12/12 | 12/12 | 34/36 | — |
| dia-ratchet, web | Haiku | 12/12 (12/13) | 12/12 | 12/12 (12/13) | 34/36 | — |
| dia-ratchet, no tools | Sonnet | 12/12 | 12/12 | 12/12 | 36/36 | — |
| dia-ratchet, no tools | Haiku | 12/12 (12/14) | 12/12 | 12/12 (12/13) | 36/36 | — |

**Reading:**

- **Core item at ceiling.** K1 passes in every loaded run of all 16 seeded cells, on both models and in both settings, and the control raised no false mismatch in any loaded run. In the no-tool settings the mismatch is named as a logical leap or as an unverified doubt. In the web settings nearly every run searched (refine Haiku out: 11 of 13 loaded runs).
- **Not loading the skill did not change this.** Haiku runs that did not load the skill also named the mismatch on every seeded cell (refine pop 13 of 13, out 30 of 30, ratchet 3 of 3). So these drafts measure the model rather than the skill text, and they would not show a gain from A1. Without the skill, the web control drew a false mismatch in 2 of 3 runs, against 0 of 12 loaded. That is too few runs to read.
- **K2 misses:**
  - Two Sonnet ratchet-web runs said the paper reported no call-quality result. It did report two quality measures, so these are real errors.
  - Two Haiku ratchet-web misses are a judge misreading. The runs list the journal and year as "Refuted", which in dia-ratchet means the draft was right; the judge read it as "false". This is the same label-semantics problem as in section 9.3.
- **S1, a pre-existing gap in the current text, not caused by A1.** With no tools, dia-refine often wrote study details it recalled into the revision as plain fact (the study was of call-centre staff or volunteers at one Chinese company, it measured calls rather than customer satisfaction). In those runs the doubt appeared only under ④ "Remaining uncertainty". Misses: Sonnet 2–3 of 12 per cell, Haiku 6 of 13 (pop), 8 of 19 (out) and 3 of 12 (ctl). dia-refine step 4 already asks for exactly this: a suspected correction from recall goes into the revision followed by "(suspected, unverified)". So this is the existing rule not being followed on this kind of correction. It is the side effect R14 expected from A1, and it is already present without A1.
- **Limits:**
  - The study is well known, and the mismatches are phrased plainly ("features shipped", "customer satisfaction scores"). A subtler draft, or a less familiar source, might not be at ceiling.
  - There is one judge, and it comes from the generators' model family.
  - The figures are for loaded runs. Haiku loaded dia-refine in 58 of 101 seeded-cell runs.

**Recommendation to the owner.** Proposed ceiling: change nothing when every model misses K1 in at most one of 12 loaded runs. Every cell missed in none, so A1 is not needed, and step 3 is recorded as not needed unless the owner rules otherwise. The S1 gap is not a reason for A1. Adding A1's wording would add more recall-based corrections of this kind. The rule that S1 tests is already in the text, and changing how it is written would be a separate meaning change outside A1. It is recorded as a case to watch, with these cells as its measure.
