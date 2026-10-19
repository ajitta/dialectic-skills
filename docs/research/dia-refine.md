# dia-refine — research notes

Status: research document, proposals only. Nothing in `skills/`, `plugins/`, `releases/` or `docs/spec.md` was changed.
Date: 2026-10-20. Skill version examined: `skills/dia-refine/SKILL.md` metadata.version 1.0.0 (plugin 0.1.0), after commit `3418c17` (the P8 fix).
Citations: `[n]` refers to the Sources list at the end. `[unverified]` marks a claim this document could not source.

## 1. Scope and what the skill says now

dia-refine is a single review pass over the assistant's previous output, or a draft the user names. It lists defect candidates, verifies them as far as the surface allows, fixes only those with a confirmed basis and returns one integrated revision. File references are to `skills/dia-refine/SKILL.md` (`S:`), `skills/dia-refine/agents/openai.yaml` (`Y:`) and `upstream/installed/self-refine/SKILL.md` (`U:`).

| Area | Rule (paraphrased) | Ref |
|---|---|---|
| Frame | Single pass. "Change is not improvement in itself, and a request for review is not in itself a sign of error." Must work with no tools; verify only as far as tools allow, mark the rest unverified | S:14 |
| Invocation | First token `dia-refine` (rest = review criteria); `/dia:dia-refine`, `$dia:dia-refine`, `$dia-refine`, `@dia-refine`; natural-language triggers; "do this task the dia-refine way" = draft, check once, show the final only; a mid-sentence mention is not an invocation; multi-round goes to dia-iterate | S:3, S:18–21 |
| Target | Last output or a named target; if ambiguous, one question and stop | S:25 |
| Step 1 | Internal checklist (deliverable, format, scope, audience, constraints), not printed; deliberate choices in the draft are kept | S:29 |
| Step 2 | List every candidate; default order factual errors → logical leaps → missing requirements → needless repetition/circumlocution; no severity filter at this step, because aiming for "only the important ones" finds fewer; point each candidate at its span; include the draft's premises | S:30 |
| Step 3 | Re-derive logic and calculations (no tool needed); check numbers, dates, names, quotations, versions, APIs, code, recent events if a tool exists; do not skip a search because a name is familiar; one check per item; recall is not verification; unchecked items stay as drafted, marked unverified; never write "verified" for an unrun check; no subagents for self-checks | S:31 |
| Step 4 | Fix only defects with a confirmed basis: a tool that ran, the user's instructions or material, or own re-derivation. An unchecked suspected factual error goes to ④ with the suspected correction; the revision keeps the draft's wording. Do not change correct content without grounds; do not harden or hide uncertainty; do not mix style polishing with factual correction; concision requests remove only duplication | S:32 |
| Step 5 | One revision, checked against the step-1 checklist; iterate only on new evidence or feedback, because "rechecking again and again only adds cost; the result does not improve" | S:33 |
| Output | Reply language = user's latest message, labels included | S:37 |
| Output | Default: defect list ① confirmed errors ② missing requirements ③ correct content kept ④ remaining uncertainty, then the revision; incidental fixes grouped in one line; the list is a verdict, not a thought log | S:39 |
| Output | "Final version only": revision only, no review, no change log | S:40 |
| Output | Nothing to fix: say so with the reason | S:41 |
| Output | A re-derivation (not a tool) that changes a single-right-answer result: original and revision side by side, premise stated, no self-declared superiority | S:42 |
| Output | Sources near verified sentences; verbatim text marked as quotation; revision no longer than the draft; for files, edit only defective passages | S:43–45 |
| Example | Plain defect list inside a fenced code block | S:49–59 |
| Safeguards | Invocation is not an error report; flipping a correct answer under groundless pressure is the failure to prevent; no over-correction; no scope widening, no invented sources or results, side issues in one closing line; creative work judged by purpose, audience, tone, constraints | S:63–66 |
| Codex/ChatGPT | `default_prompt: "Use $dia-refine to review the previous answer as a draft: "`; `allow_implicit_invocation: true` | Y:4, Y:7 |

The skill names no research method in its body. The method name survives only in `metadata.lineage: "self-refine (installed copy, unversioned)"` (S:8). The sibling dia-iterate describes itself as "dia-refine run over several rounds" and cites Huang et al. (`skills/dia-iterate/SKILL.md:14`), so the pair inherits an implicit claim of kinship with the Self-Refine literature.

## 2. The named method in its primary source: Self-Refine (Madaan et al., 2023)

The upstream skill was called `self-refine`, the name of Madaan et al.'s method. What that paper specifies:

- **One model plays three roles.** An initial output is generated; "the same LLMs provides feedback for its output and uses it to refine itself, iteratively", with no training and "a single LLM as the generator, refiner, and feedback provider".[1]
- **Iteration is the method.** "Self-Refine alternates between feedback and refine steps until a stopping condition is met"; the condition is a fixed step count or a stop indicator extracted from the feedback.[1] In the experiments the loop runs "up to a maximum of 4 iterations".[1]
- **Feedback must be actionable and specific.** "By 'specific', we mean the feedback should identify concrete phrases in the output to change."[1] dia-refine's "Point each candidate at its span in the draft" (S:30) matches this.
- **No external check gates the edits.** Every piece of feedback is fed to the refine step; there is no step where a claim must be confirmed before it changes.[1]
- **Results.** About 20% absolute average improvement across seven tasks, preferred by humans and automatic metrics.[1] Gains are largest on preference-type tasks: dialogue response preference for GPT-4 rose "from 25.4% to 74.6%".[1] Returns diminish with each iteration.[1]
- **Where it fails: finding errors in reasoning.** The authors attribute the "modest performance gains in Math Reasoning" to "the inability to accurately identify whether there is any error", noting that ChatGPT's feedback was "'everything looks good'" for 94% of instances.[1] With oracle feedback that only lets the model refine when the answer is wrong, math performance rose (GPT-3 by 4.8%, GPT-4 by 0.7%), which the authors read as "the potential of external signals".[1]

**Verdict on the name.** dia-refine is not Self-Refine. It differs on the method's two defining features. It is single-pass where Self-Refine is iterative. It gates every edit on a confirmed basis where Self-Refine applies its own feedback without a check. Its design is closer to the critiques of Self-Refine (Huang; Kamoi; CRITIC; §3) than to the paper itself. Dropping the name in the rebuild was therefore the honest choice. The remaining risk is small: the lineage field and dia-iterate's wording can still suggest the paper's loop. Finding 10 proposes a one-line label.

## 3. Modern research on how models behave when they review their own output

### 3.1 Intrinsic self-correction does not reliably help, and can hurt, on reasoning

- Huang et al. (ICLR 2024) define *intrinsic* self-correction as correcting "based solely on its inherent capabilities, without the crutch of external feedback". On reasoning, LLMs "struggle to self-correct their responses without external feedback, and at times, their performance even degrades".[2]
- Their GSM8K numbers for GPT-4 went from 95.5 (standard) to 91.5 after one self-correction round and 89.0 after two. GPT-3.5 on CommonSenseQA fell from 75.8 to 38.1 after one round.[2]
- Earlier positive results came from oracle labels: "the improvements in these studies result from using oracle labels to guide the self-correction process, and the improvements vanish when oracle labels are not available".[2] Using ground truth this way prevents the model "from altering a correct answer to an incorrect one", and "determining how to prevent such mischanges is, in fact, the key to ensuring the success of self-correction".[2]
- Their default self-correction prompt was "Review your previous answer and find problems with your answer." followed by "Based on the problems you found, improve your answer."[2] This is close to dia-refine's own natural-language trigger "review your previous answer as a draft" (S:19). The skill is invoked by exactly the kind of prompt Huang et al. measured as harmful. Its safeguards (S:14, S:63–64) are the countermeasure.
- On Self-Refine specifically, Huang et al. report a prompt-design issue. The original Constrained Generation prompt "does not clearly specify that the LLM needs to include all concepts". With that instruction added to the initial prompt, one-shot generation scored 81.8 against 75.1 for self-correction.[2] In other words, much of the gain came from catching missing requirements, which dia-refine's ② checks against the user's instructions.
- Their proposed mechanism: with a good initial prompt, the first answer is already optimal for it, and the feedback prompt "might even bias the model away from producing an optimal response".[2]
- Multi-agent debate was "no better than self-consistency" at equal numbers of responses.[2]

### 3.2 External feedback is what makes self-correction work

- Kamoi et al.'s TACL survey concludes that "no prior work demonstrates successful self-correction with feedback from prompted LLMs, except for studies in tasks that are exceptionally suited for self-correction", that "self-correction works well in tasks that can use reliable external feedback", and that large-scale fine-tuning also enables it.[4]
- The exception is tasks "whose verification tasks are much easier than the original tasks (e.g., tasks whose responses are decomposable)".[4] Kamoi et al. cite CoVe as the example and add that "many real-world tasks do not satisfy this property".[4]
- CRITIC (Gou et al., ICLR 2024) verifies an output by calling tools (search, a code interpreter) and then revises it. The authors "observe that exclusive reliance on self-correction without external feedback may yield modest improvements or even deteriorate performance".[3]
- In CRITIC's QA table for text-davinci-003, the full method scores 50.0 EM on AmbigNQ against 42.0 for "CRITIC w/o Tool". The no-tool variant is below plain CoT (44.2) on that column.[3]
- In program synthesis, "without execution feedback from the interpreter, the ability of LLMs to correct programs becomes limited and unstable".[3]

### 3.3 Finding errors is the weak step, not fixing them

- Tyen et al. show "poor self-correction performance stems from LLMs' inability to find logical mistakes, rather than their ability to correct a known mistake". Given the location of the error, correction "boosts downstream task performance across our 5 reasoning tasks".[5]
- On their BIG-Bench Mistake set, "GPT-4 attains the best results but only reaches an overall accuracy of 52.87" at locating the first mistake.[5]
- Stechly et al. (graph colouring) find that GPT-4 is "no better at verifying a solution" than at producing one. The observed gains from iterative prompting are "largely due to the correct solution being fortuitously present in the top-k completions … and being recognized as such by an external verifier".[7]
- Valmeekam et al. (planning) find that self-critique "appears to diminish plan generation performance, especially when compared to systems with external, sound verifiers". The LLM verifiers "produce a notable number of false positives". The form of the feedback, binary or detailed, "showed minimal impact".[8]

Implication for dia-refine: re-derivation (S:31) is the step these papers show to be weak. It is also one of the three bases S:32 accepts as "confirmed".

### 3.4 Self-bias: models favour their own text

- Xu et al. find self-bias, "the tendency to favor its own generation", in all six models they test. The self-refine pipeline "improves the fluency and understandability of model outputs" but "further amplifies self-bias". "External feedback with accurate assessment" and larger models reduce it.[9]
- Panickssery et al. show LLM evaluators can recognise their own outputs, and self-recognition correlates linearly with self-preference.[13]

So a model that reviews its own draft, in the same context, starts biased towards "everything looks good". Self-Refine's 94% figure shows the same tendency.[1]

### 3.5 Factored verification (CoVe) reduces copying of the draft's errors

- Chain-of-Verification has four steps: draft, plan verification questions, answer them "independently so the answers are not biased by other responses", then revise.[6]
- CoVe uses no tools ("we do not explore tool-use").[6] Its key observation is that "models that attend to existing hallucinations in the context from their own generations tend to repeat the hallucinations". The factored variants keep the baseline response out of the verification prompts.[6]
- On Wikidata list questions, "only ∼17% of the Llama few-shot baseline answer entities are correct", but "when querying each individual entity via a verification question, we find ∼70% are correctly answered".[6] Precision rose from 0.17 (few-shot) to 0.29–0.36 (CoVe variants).[6]

Two lessons for dia-refine:

- Independent recall is better than the draft's recall, so CoVe gives some support to acting on recall.
- About 30% of those independent answers were still wrong.[6] Recall alone is not a basis for overwriting a draft. The P8 rule (S:31–32) routes recalled corrections to ④ instead of the revision, which is the conservative reading of this result. It is consistent with Kamoi's view that only decomposable tasks support intrinsic correction.[4]

### 3.6 Sycophancy: "are you sure?" makes models flip

- Sharma et al. challenge models with "I don't think that's right. Are you sure?". Assistants "frequently wrongly admit mistakes when questioned by the user"; "Claude 1.3 wrongly admits mistakes on 98% of questions"; this holds "even when the assistant states it is highly confident".[10]
- Laban et al.'s FlipFlop experiment: across ten LLMs and seven tasks, models "flip their answers on average 46% of the time", with an average 17% accuracy drop. "Wording of the challenger utterance has a large impact". Models are more likely to flip when the initial answer was wrong than when it was right.[11]

Every dia-refine invocation is a challenge of this kind. S:14 and S:63 ("Being invoked is not a signal of error … Flipping a correct answer under pressure that has no specific grounds is the failure this procedure exists to prevent") target exactly this behaviour.

### 3.7 Comprehensive critique versus spurious issues

- CriticGPT (McAleese et al.) treats critique as a trade-off between "the number of real and spurious issues". The authors give an inference-time method (Force Sampling Beam Search) to balance it.[12]
- Their rating forms score "comprehensiveness" separately from "hallucinated bugs" and "nitpicks". Human + model teams beat the model-only frontier on both.[12]

dia-refine's split between candidate listing for recall (S:30) and a confirmation gate for precision (S:32) is the same structure in prose. No source fetched for this document directly supports the stated reason, "Starting out to 'find only the important ones' makes you find fewer" [unverified].

### 3.8 Vendor guidance

- Anthropic describes self-correction as the most common chaining pattern: "generate a draft → have Claude review it against criteria → have Claude refine based on the review", each as a separate API call.[14] dia-refine runs all three in one turn, so it cannot get the separate-context benefit that chaining, or CoVe's factoring, provides.
- Routing on all three vendors depends on the description. Claude Code: the `description` "helps Claude decide when to load the skill automatically".[15] OpenAI: "implicit matching depends on `description`", so "front-load the key use case and trigger words"; Codex "shortens skill descriptions first" when many skills are installed.[16]

## 4. Fidelity audit

Verdicts: **matches** = agrees with the cited evidence; **loose** = right direction but stated more broadly or differently than the evidence; **departs** = deliberately different from the named method; **unsupported** = no source found.

| # | Skill rule (ref) | What the sources say | Verdict |
|---|---|---|---|
| A1 | Single pass, not a loop (S:14, S:33) | Self-Refine is iterative by definition, up to 4 iterations[1] | **departs** from Self-Refine; deliberate and justified by [2][4] |
| A2 | Fix only defects with a confirmed basis (S:32) | Self-Refine applies all self-feedback[1]; corrections help when external feedback is reliable[3][4]; oracle-gated edits are what made earlier results look good[2] | **departs** from Self-Refine; **matches** CRITIC/Kamoi |
| A3 | Re-derivation counts as a confirmed basis (S:32) | Intrinsic re-checking of reasoning degrades GSM8K/CSQA[2]; error *finding* is weak (GPT-4 52.87%)[5]; self-verification gives false positives[8] | **loose**: the weakest of the three bases is labelled "confirmed" (Finding 2) |
| A4 | Side-by-side display for re-derived single-answer changes (S:42) | Correct→incorrect mischanges are the central failure[2] | **matches** as a mitigation; conflicts with final-only mode (Finding 1) |
| A5 | Recall is not verification; suspected fact errors go to ④ (S:31–32) | Independent recall beats in-draft recall but is still ~30% wrong[6]; no reliable intrinsic correction outside decomposable tasks[4] | **matches** (conservative) |
| A6 | Use tools when present; never claim an unrun check (S:31) | Tool feedback drives CRITIC's gains; the no-tool variant falls below CoT[3] | **matches** |
| A7 | Do not skip a search because a name is familiar (S:31) | No source fetched on familiarity and stale answers | **unsupported** as stated (plausible heuristic) [unverified] |
| A8 | List every candidate, no severity filter, because aiming for important ones finds fewer (S:30) | The recall/precision trade-off in critique is real[12]; the specific causal claim is unsourced | **loose** (structure supported, reason unsourced) |
| A9 | Point each candidate at its span (S:30) | Self-Refine's "specific" feedback names phrases[1]; correction works once the location is known[5] | **matches** |
| A10 | Default order: factual → logic → requirements → repetition (S:30) | No source ranks these; Self-Refine's dimensions are task-specific[1]; the requirement check is the one category verifiable without tools (the user's text)[2] | **unsupported** (design choice; harmless because there is no severity filter) |
| A11 | No subagents for self-checks (S:31) | Same-model reviewers favour their own outputs[9][13]; debate ≈ self-consistency[2]; but a factored context *does* help by keeping the draft out of view[6] | **loose**: defensible, but the reason is missing and a factored check is a known gain (Finding 6) |
| A12 | Invocation is not an error signal; no flipping under groundless pressure (S:14, S:63–64) | Wrong admissions of error up to 98%[10]; 46% flips, 17% drop[11]; Huang's own feedback prompt lowers accuracy[2] | **matches** (strongly supported) |
| A13 | "Rechecking again and again only adds cost; the result does not improve" (S:33) | True for reasoning on self-judgment[2]; Self-Refine shows multi-round gains, with diminishing returns, on preference tasks[1] | **loose** (over-general) |
| A14 | ③ "correct content kept" listed explicitly (S:39) | Makes the anti-flip decision visible; no direct study | **unsupported**, low risk |
| A15 | "Nothing needs fixing" is a valid result (S:41) | Self-correction without a basis tends to make correct answers wrong[2][11] | **matches** |
| A16 | Creative work judged by purpose, audience, tone, constraints (S:66) | Self-feedback improves fluency but amplifies self-bias[9]; S:32's confirmed-basis list does not say what counts as confirmed here | **loose** (Finding 8) |
| A17 | Revision no longer than the draft (S:44) | No source; conflicts internally with ② additions | **unsupported** / inconsistent (Finding 7) |

## 5. Lineage: upstream `self-refine` → `dia-refine`

### 5.1 Translation audit (spec §5.6: "keeps every rule and its reason")

I compared the two files line by line. Every rule in U survives in S with its stated reason where U had one:

- the frame (U:8 → S:14);
- the invocation forms and the passing-mention rule (U:12–15 → S:18–21);
- ambiguous-target handling (U:19 → S:25);
- steps 1–5 (U:23–27 → S:29–33);
- the output rules (U:31–37 → S:39–45);
- the example (U:41–51 → S:49–59);
- the four safeguards (U:55–58 → S:63–66).

The reasons that survive are:

- the severity-filter reason (U:24 → S:30);
- the familiar-name reason (U:25 → S:31);
- the cost reason for not iterating (U:27 → S:33);
- the anti-flip reason (U:55 → S:63).

Small translation deltas:

- U:34 lists "계산, 코드 실행 결과 등" ("calculation, code-run result, etc."). S:42 drops "etc.", so the parenthetical reads as a closed list. Low impact.
- The ③ label mismatch is inherited: the list says "correct content kept" (S:39) and the example says "Content kept" (S:55). U has the same mismatch (U:31 vs U:47).
- Upstream had **no reason** for "no subagents" (U:25). The rule is translated faithfully, but spec §5.6's "and its reason" cannot be met for it (Finding 6).

### 5.2 Additions in the rebuild

| Addition | Where | Origin |
|---|---|---|
| `/dia:…`, `$dia:…`, `$…`, `@…` forms; passing-mention rule in the description | S:3, S:18 | spec §5.6; P3 naming finding |
| Output-language rule "labels included" | S:37 | New. U had none, though spec L6 says all reference skills "already require" it. For self-refine that premise was false; the rebuild fixed it silently |
| "Your own recall is not verification …" | S:31 | P8 fix (commit 3418c17) |
| Three confirmed bases; suspected error → ④ with suspected correction | S:32 | P8 fix |
| Side-by-side rule narrowed to "your own re-derivation, not a tool" | S:42 | P8 fix. Before it, U:34 allowed changing a single-answer result "without external verification", which conflicted with U:25 and caused the P8 failure in both arms (`docs/probes.md:63–71`) |

### 5.3 Lost in the rebuild

Nothing normative was lost. Two things are only weakened:

- The Korean example (U:41–51) showed Korean labels, an implicit language cue. S's example is English; S:37's explicit rule replaces the cue.
- The upstream description had the multi-round pointer at its end (U:3). S keeps it (S:3).

## 6. Risks and failure modes

### 6.1 On the model

1. **False "confirmed" via re-derivation.** On reasoning, the model's re-check can turn correct answers into wrong ones.[2] It also tends to miss real errors.[1][5] S:32 counts re-derivation as confirmed; S:42 mitigates this only for single-answer results, and only in default mode.
2. **Self-bias leading to an empty defect list.** "Everything looks good" is the modal self-feedback on reasoning.[1][9] S:30's "list every candidate" pushes against this. Nothing makes the re-derivation independent of the draft's own working (contrast CoVe's factoring[6]).
3. **Sycophantic flip.** Strongly guarded (S:14, S:63). Residual risk: the user names a criterion ("dia-refine — the date is wrong") without grounds. S:18 treats that text as review criteria, not as evidence. The skill does not say that a user assertion counts as "the user's instructions or supplied material" (S:32). A bare "it's wrong" could be read as a confirmed basis (Finding 9).
4. **Over-listing.** Listing every candidate raises nitpick risk.[12] The confirmation gate (S:32) and "group incidental fixes" (S:39) contain it.

### 6.2 Tool-less and mobile surfaces

1. **Only two bases remain without tools:** the user's material and re-derivation. Most factual candidates therefore end in ④. P8 shows this working at n=3 (`docs/probes.md:67`).
2. **Final-only mode hides ④.** With "final version only", or "do this task the dia-refine way" (S:20, S:40), there is no defect list. The suspected correction and the unverified status vanish, which contradicts "Do not … hide it; mark its limits" (S:32). The P8 inline "(unverified; …)" note looks like the model resolving this tension on its own (§6.4).
3. **Code-fenced example.** The example defect list is in a code block (S:49–59). The owner's brainstorm work found that a code-block brief "scrolls sideways on phones". The fix there was "print plain Markdown" (`upstream/superclaude-stable-47f791b/docs-features/socratic-brainstorm-skill/08-implementation.md:57`). Models tend to copy an example's form [unverified], so dia-refine output may arrive fenced on mobile.
4. **Length.** The default output is a four-part list plus a full revision. On a phone that is long; "only items that change the user's conclusion or next action" (S:39) limits it.

### 6.3 Cross-surface

- **Codex/ChatGPT prompt name.** `default_prompt` uses `$dia-refine` (Y:4). P3 showed that `$dia-<x>` does not resolve on the Codex plugin route; `$dia:dia-<x>` does (`docs/probes.md:32`). This is already handoff item 3.
- **Implicit routing on OpenAI surfaces** reads the description and may shorten it.[16] The description front-loads what the skill does. The first-word trigger appears only in its second sentence (S:3). Truncation would cut the "passing mention" and dia-iterate boundaries first, since they come last [unverified: truncation behaviour not probed].
- **Subagent-capable hosts** (Claude Code, Codex) could run a separate-context check. S:31 forbids it. On chat surfaces the question does not arise.
- **File targets** (Claude Code, Codex): S:45 limits edits to defective passages, which is good. Any inline uncertainty note would be written into the user's file (§6.4).
- **Headless permissions.** In P8, one run had search permission denied. The skill treats an unrun tool as "could not check" (S:31), which is correct.

### 6.4 The two unacted P8 observations

**(a) Inline "(unverified; …)" note in the revision** (`docs/probes.md:75`). The skill sends mixed signals here:

- "leave the rest marked unverified" (S:14);
- "stay as drafted and are marked unverified" (S:31), which does not say where the mark goes;
- "Do not … hide it; mark its limits" (S:32), which points at the text itself;
- "the revision keeps the draft's wording" (S:32), which argues against any inline addition.

The model's choice is a defensible reading of S:14/S:31/S:32-first-half and a violation of S:32-second-half. Its harm depends on the target:

- In chat, an inline note is mostly harmless and duplicates ④.
- For a file target, or a revision the user pastes elsewhere, it injects reviewer commentary into the deliverable. Under S:45 that counts as an edit outside the defective passage.
- In final-only mode, an inline note is the only way to keep S:32's "do not hide".

So the observation exposes an unresolved rule, not a model error. Finding 3 proposes making the location explicit per mode. Since n=1, re-test after the text change, as the handoff asks.

**(b) Korean reply to an English prompt** (`docs/probes.md:76`). The probes recorded "the host's Korean locale" as a possible cause. A more specific confound is visible in the repository:

- The probe command uses a relative `--plugin-dir plugins/dia` (`docs/handoff.md`, "How probes were run"), so the runs started at the repository root.
- Claude Code loads "CLAUDE.md and CLAUDE.local.md files in the directory hierarchy above the working directory … at launch", and `@` imports are expanded at launch.[17]
- The repository's `CLAUDE.md` imports `AGENTS.md`, which says: "The owner writes in Korean; reply in Korean, briefly."
- A fresh `CLAUDE_CONFIG_DIR` isolates the user's settings and synced plugins, not project memory [unverified: inferred from the docs, not tested].
- The run therefore probably had two conflicting instructions: S:37 (user's language) and AGENTS.md (Korean). Claude Code's docs warn that "if two instructions contradict each other, Claude may pick one arbitrarily".[17] One Korean reply among several English ones fits that warning.

The same confound affects P7's language evidence ("Every Korean prompt … got a Korean reply", `docs/probes.md:56`). A Korean reply there is predicted by AGENTS.md whatever the skills do. No skill change is indicated; the probe procedure needs one (Finding 4).

## 7. Findings and recommendations (proposals only)

**F1 — high. Final-only mode conflicts with the side-by-side rule and with "do not hide uncertainty".**

Evidence: S:40 forbids showing the review. S:42 requires a side-by-side display when re-derivation changes a single-answer result. S:32 forbids hiding uncertainty. The P8 failure came from exactly this kind of two-rule conflict (`docs/probes.md:66`), and Huang et al. identify unguarded correct→incorrect changes as the central risk.[2]

Proposal: add to S:40, after "Do not show the review or a change log.":
> "Two exceptions, each at most one line after the revision: if your own re-derivation changed a single-right-answer result, give the original result and the premise of the change; if a suspected error stayed unverified (④), name it and the suspected correction."

**F2 — high. Re-derivation is labelled "confirmed" alongside tool results.**

Evidence: S:32 puts "re-deriving the logic or calculation yourself" next to "a tool that ran". Intrinsic re-checking lowers accuracy on reasoning benchmarks.[2] Error-finding accuracy is about 53% for GPT-4.[5] Self-critique produces false positives.[8] The ① example shows only a tool-sourced item (S:51).

Proposal: in S:39, after "① confirmed errors", add:
> "Tag each ① item with its basis: (tool), (user's material) or (re-derived)."

and add a second ① example line, for instance:
> `- "total 1,240" → 1,420 (re-derived: 620 + 800; draft added 620 + 620)`

Keep S:42 as is.

**F3 — medium. Where the "unverified" mark goes is undefined (P8 observation a).**

Evidence: S:14, S:31 and S:32 can be read either way; one run put the mark inline (`docs/probes.md:75`); for file targets this edits the deliverable (S:45).

Proposal: in S:31, replace "stay as drafted and are marked unverified" with:
> "stay as drafted; the mark goes in ④, not inside the revision (in final-only mode, in the closing line of F1)."

**F4 — medium. Language evidence from P7/P8 is confounded by repository instructions (P8 observation b).**

Evidence: the relative `--plugin-dir` puts the runs at the repo root; Claude Code loads CLAUDE.md and its imports from there[17]; AGENTS.md says "reply in Korean". The same docs warn that contradictory instructions are resolved arbitrarily.[17]

Proposal: no skill change. In `docs/handoff.md` "How probes were run", add:
> "Run from an empty working directory outside the repository with an absolute `--plugin-dir`, so CLAUDE.md/AGENTS.md are not loaded."

Then re-run P8 (dia-refine, tools allowed but search denied, English prompt) and one English P7 cell before attributing anything to the skill or the locale.

**F5 — medium. Make the tool-less re-derivation independent of the draft (a factored check inside one turn).**

Evidence:
- Models "tend to repeat the hallucinations" they attend to; factored verification that hides the draft helps.[6]
- Self-bias favours the draft.[9][13] Error location is the bottleneck.[5]

Proposal: add to S:31, after "Re-derive logic and calculations independently; this needs no tools.":
> "Work each one out from the question or the user's data first, then compare with the draft; do not follow the draft's own working while you re-derive."

**F6 — medium. "No subagents" has no stated reason (spec §5.6 asks for one).**

Evidence: U:25 and S:31 give none. Reasons are available. Same-model reviewers prefer their own output.[9][13] Debate is no better than self-consistency at equal cost.[2] Subagents are absent on chat surfaces (spec §2, G2). There is a counter-consideration: a factored context does help.[6]

Proposal: replace "Do not launch subagents to check your own work." with:
> "Do not launch subagents to check your own work: a copy of the same model is not an outside check, it costs extra calls, and most surfaces have none."

F5 captures the useful part of a factored check without subagents.

**F7 — medium. "No reason to be longer than the draft" contradicts adding missing requirements.**

Evidence: S:44 vs ② (S:39, example S:53, "The requested list of CSV column names is missing"). Huang's analysis shows that missing-requirement fixes are where much of the Self-Refine gain came from.[2]

Proposal: replace the first sentence of S:44 with:
> "Apart from content added for ②, the revision has no reason to be longer than the draft."

**F8 — low. Creative work has no defined "confirmed basis".**

Evidence: S:66 changes the criteria, but S:32's three bases do not map onto purpose, audience or tone. Self-feedback on such text improves fluency while amplifying self-bias.[9]

Proposal: append to S:66:
> "Here the confirmed basis is a conflict with the purpose, audience, tone or constraints the user stated; matters of taste go to ④ as suggestions, not into the revision."

**F9 — low. A bare user assertion of error is not defined as a basis.**

Evidence: S:32 counts "the user's instructions or supplied material". S:63 rejects "pressure that has no specific grounds". `dia-refine — that date is wrong` sits between them. Models flip at high rates under bare challenges.[10][11]

Proposal: add to S:32:
> "A user's bare statement that something is wrong is review criteria, not a basis; supplied facts, documents or data are a basis."

**F10 — low. Honest method label.**

Evidence: dia-refine departs from Self-Refine's iterative, ungated loop (§2), while the lineage (S:8) and dia-iterate's "dia-refine run over several rounds" (`skills/dia-iterate/SKILL.md:14`) suggest kinship.

Proposal: no body change, or one sentence after S:14:
> "This is not the iterative Self-Refine loop (Madaan et al., 2023): it is one verify-then-fix pass, because self-feedback alone does not reliably fix reasoning (Huang et al., 2024)."

dia-iterate already cites Huang this way, so the precedent exists.

**F11 — low. The example is a code block; it may render fenced on phones.**

Evidence: S:49–59; the owner's own finding about code-block output on phones (`…/socratic-brainstorm-skill/08-implementation.md:57`).

Proposal: after "Example defect list:" (S:47) add:
> "(print it as plain Markdown, not in a code block)"

**F12 — low. ④ example does not show the P8 suspected-correction form.**

Evidence: S:32 requires "the correction you suspect" in ④. The only ④ example (S:57) shows a no-tool item without one.

Proposal: add an example line after S:57:
> `- "Python 3.13 removed the GIL by default": I recall it is an optional build; no tool to check; left as drafted`

**F13 — low. Two reasons overstate their evidence.**

Evidence: S:33's "the result does not improve" is shown for reasoning on self-judgment[2], but multi-round gains exist on preference tasks.[1] S:30's "makes you find fewer" has no source found (A8).

Proposal: S:33 →
> "Rechecking on your own judgment alone adds cost and tends not to improve correctness; on reasoning it can make it worse."

S:30: keep the rule and drop or soften the causal clause, for example "list every candidate first; filtering is step 4's job".

**F14 — low. Codex/ChatGPT `default_prompt` uses a name that does not resolve on the plugin route.**

Evidence: Y:4 `$dia-refine`; P3: `$dia-<x>` does not resolve, `$dia:dia-<x>` does (`docs/probes.md:32`).

Proposal: as in handoff item 3, after P4, `default_prompt: "Use $dia:dia-refine to review the previous answer as a draft: "`.

**F15 — low. Translation nits.**

Evidence: §5.1. The ③ label differs between S:39 and S:55, and "etc." was dropped at S:42.

Proposal:
- S:55 "③ Content kept" → "③ Correct content kept";
- S:42 "(a calculation, the output of a code run)" → "(a calculation, the output of a code run, and the like)".

All proposals that change skill text need a `metadata.version` bump and a plugin version decision (AGENTS.md; handoff "State"). The design points the brief asked about and that need **no** change: the defect order (A10, harmless without a severity filter); candidate listing without a severity filter (A8, keep the rule); the ①–④ layout (A14, keep); first-word invocation (P6 pass; spec D10).

## 8. Open questions for the owner

1. F1/F3: in final-only mode, which do you prefer: one closing line after the revision, inline markers, or truly nothing (accepting that uncertainty is hidden)?
2. F2: should re-derived changes stay in ① (tagged), or move to their own section (for example "①′ re-derived corrections")? The second is clearer but changes the four-part layout spec §5.6 names.
3. F5/F6: is a factored in-turn re-derivation acceptable, or does it add too much hidden reasoning cost on mobile?
4. Should "are you sure?" / "확실해?" route to dia-refine? The skill's safeguards are exactly the anti-flip behaviour the FlipFlop work[11] argues for. But implicit routing on a bare challenge may over-trigger. This needs a probe, not a guess.
5. F10: do you want any method citation in the skill body, or keep the body citation-free, as dia-refine is now?
6. F4: should the probe procedure (not the skill) be fixed and P7/P8 language cells re-run before the 1.0.0 release?

## Sources

[1] https://arxiv.org/html/2303.17651v2 — Madaan et al. 2023, Self-Refine: Iterative Refinement with Self-Feedback (arXiv:2303.17651v2)
[2] https://arxiv.org/html/2310.01798v2 — Huang et al. 2024, Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2024, arXiv:2310.01798v2)
[3] https://arxiv.org/html/2305.11738v4 — Gou et al. 2024, CRITIC: LLMs Can Self-Correct with Tool-Interactive Critiquing (ICLR 2024, arXiv:2305.11738v4)
[4] https://arxiv.org/html/2406.01297v3 — Kamoi et al. 2024, When Can LLMs Actually Correct Their Own Mistakes? (TACL, arXiv:2406.01297v3)
[5] https://arxiv.org/html/2311.08516v3 — Tyen et al. 2024, LLMs cannot find reasoning errors, but can correct them given the error location (arXiv:2311.08516v3)
[6] https://arxiv.org/html/2309.11495v2 — Dhuliawala et al. 2023, Chain-of-Verification Reduces Hallucination in LLMs (arXiv:2309.11495v2)
[7] https://arxiv.org/abs/2310.12397 — Stechly, Marquez, Kambhampati 2023, GPT-4 Doesn't Know It's Wrong (arXiv:2310.12397)
[8] https://arxiv.org/abs/2310.08118 — Valmeekam, Marquez, Kambhampati 2023, Can LLMs Really Improve by Self-critiquing Their Own Plans? (arXiv:2310.08118)
[9] https://arxiv.org/abs/2402.11436 — Xu et al. 2024, Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement (arXiv:2402.11436)
[10] https://arxiv.org/html/2310.13548v4 — Sharma et al. 2023, Towards Understanding Sycophancy in Language Models (arXiv:2310.13548v4)
[11] https://arxiv.org/abs/2311.08596 — Laban et al. 2023, Are You Sure? Challenging LLMs Leads to Performance Drops in The FlipFlop Experiment (arXiv:2311.08596)
[12] https://arxiv.org/html/2407.00215v1 — McAleese et al. 2024, LLM Critics Help Catch LLM Bugs (arXiv:2407.00215)
[13] https://arxiv.org/abs/2404.13076 — Panickssery, Bowman, Feng 2024, LLM Evaluators Recognize and Favor Their Own Generations (arXiv:2404.13076)
[14] https://docs.claude.com/en/docs/build-with-claude/prompt-engineering/chain-prompts — Anthropic docs: Prompting best practices / chain prompts
[15] https://code.claude.com/docs/en/skills — Claude Code docs: Skills
[16] https://learn.chatgpt.com/docs/build-skills — OpenAI: Build skills (ChatGPT and Codex)
[17] https://code.claude.com/docs/en/memory — Claude Code docs: How Claude remembers your project (CLAUDE.md, imports)
