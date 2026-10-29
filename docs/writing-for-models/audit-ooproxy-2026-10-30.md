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
