# dia-iterate: research notes and fidelity audit

| | |
|---|---|
| Skill | `skills/dia-iterate` (SKILL.md 1.0.0, `references/verification-sources.md`, `agents/openai.yaml`) |
| Upstream | `upstream/installed/recursive-refine` (installed copy, unversioned) |
| Spec | `docs/spec.md` §5.7, §7.3; probes P3, P6, P8 in `docs/probes.md` |
| Date | 2026-10-20 |
| Status | Research only. Every text change below is a proposal; nothing in `skills/` was edited. |

## 1. Scope and summary of what the skill says

dia-iterate is a multi-round review loop. A round is "verify, then fix only what was confirmed", not "reread and rewrite" (`SKILL.md:14`). Its parts:

- **Invocation** (`SKILL.md:3`, `:18-23`; `agents/openai.yaml:7`). Activates only when `dia-iterate` is the first word, or on an explicit call (`/dia:dia-iterate`, `$dia:dia-iterate`, `$dia-iterate`). Natural-language equivalents do not count. If the skill looks right but the marker is absent, it asks in one line for a `dia-iterate` message and stops. A topic with no target gets one question and no draft. `allow_implicit_invocation: false`.
- **Target** (`:25-27`). The last output, a named draft, or a readable file. Text, code and computed results.
- **One round** (`:29-36`):
  1. Name defects: the user's criteria, else factual error → logical leap → missing requirement → padding.
  2. Assign an external verification method per defect, from `references/verification-sources.md`. Rereading is not external.
  3. Verify. Each defect ends confirmed, refuted or unverifiable. Keep the URL, the verdict and one value; never copy source text.
  4. Fix confirmed defects only, with the smallest edit. No hedging, no rewriting.
  5. Lock what passed verification.
  6. Log the round.
- **Without tools** (`:38-40`). The only external evidence is the user's instructions and the material they supply. The loop usually stops after round 1 with "verification exhausted". This was added in the rebuild (spec §5.7).
- **Stopping conditions, checked in order** (`:42-52`): regression (roll back), zero defects, verification exhausted, fixed point, round cap (`--max N`, default 3, `:16`). Rounds are never invented.
- **Output** (`:54-76`). A change list by default, a round-summary table, then the unverified list. Full text only on request. A single-right-answer result never changes without external verification.
- **Guardrails** (`:78-87`):
  - Being invoked is not an error report.
  - A round whose only check is rereading makes no edits.
  - Style judgments are applied once, in round 1.
  - No scope widening.
  - "Verified" means checked by an external method this session.
  - Four content-filter rules: retry once, then change the output shape (drop quotations, reduce to a change list), then abandon and start a new conversation; never restate widely copied set texts.
- **Reference table** (`references/verification-sources.md:5-17`). An accepted method per content type, a judgment-log format (`:19-27`) and common misjudgments (`:29-34`). Recompute calculations by running code. Check code by execution or tests, facts by search plus a primary source, missing requirements against the instructions. A user's claim about the world is a single source.

The probe evidence for this skill is P6 (first-word invocation passes in Claude Code) and P8 (tool-less runs: 2 of 2 stopped after round 1 with "verification exhausted" and changed nothing). Both ran in headless Claude Code on Sonnet. P8 was n=2 (`docs/probes.md`).

## 2. The method in its primary sources

The skill names one source, Huang et al., in its opening paragraph (`SKILL.md:14`). Its upstream lineage line says "Self-refine run over several rounds", which the dia text renders as "dia-refine run over several rounds". The procedure itself, though, is closest to a third method it never names: CRITIC.

### 2.1 Self-Refine (Madaan et al., 2023)

- **The loop.** One LLM generates an output, gives feedback on it, and refines the output using that feedback, iteratively. It uses no training data and no external signal [2].
- **Stopping.** The loop "alternates between FEEDBACK and REFINE steps until a stopping condition is met". The condition is either a fixed timestep or a stop indicator that the model itself extracts from its feedback. In the experiments, iterations ran "up to a maximum of 4 iterations" [2].
- **Iteration effect.** Quality rose over three iterations: Code Optimization 22.0 → 28.8, Constrained Generation 29.0 → 49.7. "The marginal improvement naturally decreases with more iterations", and performance "may not always monotonically increase", for example in multi-aspect tasks [2].
- **Where it gained least.** On Math Reasoning, Self-Refine gained 0 to 0.2 points (GPT-3.5 64.1 → 64.1; GPT-4 92.9 → 93.1). The large gains were on preference-judged tasks such as dialogue, sentiment reversal and readability [2].
- **Ablation.** Generic feedback or no feedback lowered scores. Feedback quality, not merely iterating, drives the gain [2].

The feedback in Self-Refine is self-feedback. dia-iterate forbids exactly that as grounds for an edit (`SKILL.md:32`, `:81`; `verification-sources.md:3`). The two share a loop shape and nothing else.

### 2.2 CRITIC (Gou et al., ICLR 2024)

- **Algorithm.** Generate an initial output. Then, for up to n iterations: verify the output by interacting with external tools to obtain critiques; return it if the critiques indicate it is correct; otherwise correct it. Tools include search and a code interpreter [4].
- **Stopping criteria.** "Satisfying critiques from verification, reaching the maximum iterations n, or receiving environmental feedback". In the QA experiments the loop corrected "up to n = 3 rounds, stopping early if the answer remains the same for two consecutive corrections" [4].
- **Iteration effect.** "The marginal benefits of multiple corrections diminish, and typically, 2-3 rounds of corrections yield most of the benefits". Correction surges "when only modifying erroneous samples (oracle setting)" [4].
- **Without tools.** "The model's own critiques contribute marginally to the improvement … and even fall short compared to the initial output". For example, with Text-Davinci-003 on AmbigNQ, CRITIC scores 50.0 EM and CRITIC without tools 42.0 [4].

dia-iterate's round (assign an external method, verify, fix, stop when nothing is confirmed, cap at 3, stop on no change) is CRITIC's algorithm almost step for step. It adds explicit verdict classes, locking and a regression rule.

### 2.3 The negative result the skill cites: Huang et al. (ICLR 2024)

- **Definition.** "Intrinsic self-correction": correcting "based solely on its inherent capabilities, without the crutch of external feedback" [1].
- **Finding.** "LLMs struggle to self-correct their responses without external feedback, and at times, their performance even degrades after self-correction" [1].
- **Earlier positive results.** Huang et al. attribute earlier positive results to oracle labels: "the improvements vanish when oracle labels are not available" [1].
- **Multi-round numbers.** GPT-3.5 on CommonSenseQA falls from 75.8 (standard prompting) to 38.1 (round 1) and 41.8 (round 2). GPT-4 on HotpotQA goes 49.0 → 49.0 → 43.0. Llama-2 on GSM8K goes 62.0 → 43.5 → 36.5 [1].
- **Flips.** On GSM8K, GPT-3.5 kept its answer 74.7% of the time; among the changes, it "is more likely to modify a correct answer to an incorrect one than to revise an incorrect answer to a correct one" [1].

The skill's paraphrase, "brings no gain on reasoning tasks and often makes them worse" (`SKILL.md:14`), is substantively right. "Often" is stronger than the authors' "at times", but most cells in their Tables 3-4 do drop.

### 2.4 Reflexion (Shinn et al., 2023)

- **Mechanism.** Reflexion agents "verbally reflect on task feedback signals" and keep the reflections in episodic memory for the next trial. The loop runs until the Evaluator passes the trajectory or a maximum trial count is reached. The memory is bounded to Ω experiences, "usually set to 1-3" [3].
- **Feedback.** Feedback may be scalar or free text, external or "internally simulated" [3].
- **Limitation for code.** The model writes its own tests. A flaky self-written suite can let "all tests pass on an incorrect solution", a false positive, and then "the agent will prematurely report an invalid submission" [3].

This matters for `verification-sources.md:8`, which accepts "execution, tests" for code without asking who wrote the tests.

## 3. Relevant modern research

### 3.1 When self-correction works

- **Kamoi et al. (TACL 2024)** survey the field.
  - "No prior work demonstrates successful self-correction with feedback from prompted LLMs, except for studies in tasks that are exceptionally suited for self-correction".
  - "Self-correction works well in tasks that can use reliable external feedback".
  - "Large-scale fine-tuning enables self-correction" [5].
  - The exception class is tasks whose verification is much easier than generation, for example responses that decompose into separately checkable items [5].
- **Stechly et al.** studied GPT-4 on Game of 24, graph colouring and STRIPS planning. They found "significant performance collapse with self-critique and significant performance gains with sound external verification", and "merely re-prompting with a sound verifier maintains most of the benefits of more involved setups" [12]. The verifier's soundness matters more than the elaborateness of the critique.
- **Olausson et al. (ICLR 2024)** studied code self-repair. They found it "bottlenecked by the model's ability to provide feedback on its own code"; stronger feedback produced "substantially larger performance gains" [11].
- **Kumar et al. (SCoRe)** open with "self-correction … has consistently been found to be largely ineffective in modern LLMs". They obtain it only through multi-turn reinforcement learning [7]. A prompt-only skill cannot rely on a trained self-correction ability that the host model may or may not have.

Implication: the skill's central bet, that external verification is the gate, is the consensus position. What the skill can control is how sound its verifiers are and how many claims reach them.

### 3.2 Finding errors is the bottleneck, not fixing them

- **Tyen et al.** report that "poor self-correction performance stems from LLMs' inability to find logical mistakes, rather than their ability to correct a known mistake". Given the error location, correction works [10].
- **Chain-of-Verification (Dhuliawala et al.)** drafts, plans verification questions, answers them independently, then revises. Models "that attend to existing hallucinations in the context from their own generations tend to repeat the hallucinations". The "factored" variant answers each question without the draft in context [8].

dia-iterate's step 1 asks the model to "name the defects" (`SKILL.md:31`). That is the step Tyen et al. show to be weakest: a claim the model does not suspect never reaches a verifier. dia-refine, by contrast, says "List every defect candidate … Do not filter by severity … Include the premises the draft rests on" (`skills/dia-refine/SKILL.md:30`). dia-iterate lost that instruction (finding 5).

### 3.3 Iteration amplifies bias and drift

- **Xu et al. ("Pride and Prejudice").** Self-bias, the tendency to favour one's own generation, is "prevalent in all examined LLMs". The self-refine pipeline "improves the fluency and understandability of model outputs" but "further amplifies self-bias". Larger models and "external feedback with accurate assessment" reduce it [6].
- **Mohamed et al. ("Broken Telephone").** Under repeated LLM processing, "distortion accumulates over time"; it can be reduced by prompting but not avoided [14].

These support two rules: the smallest edit with no rewrite (`SKILL.md:34`), and the lock (`:35`). Every pass that regenerates text is a chance for drift. They also explain why the style rule (`:82`) is risky: fluency and style are exactly where self-judgment improves the surface while bias grows.

### 3.4 Pressure to change: sycophancy and FlipFlop

- **Laban et al.** challenged models with "Are you sure?". Models "flip their answers on average 46% of the time", and accuracy dropped by 17% on average [9].
- **Sharma et al.** find sycophancy "a general behavior of state-of-the-art AI assistants", likely driven in part by human preference judgments [13].

The guardrail "Being invoked is not a report of an error" (`SKILL.md:80`) targets this directly. So does the reference rule that a user's claim about the world is a single source to verify, not adopt (`verification-sources.md:17`). Calling a review loop is itself a mild "are you sure?".

### 3.5 Verifiers, search and stopping in iterative algorithms

- **Verifier-guided selection (Cobbe et al.).** Generate many candidates and "select the one ranked highest by the verifier" [15]. This is the alternative architecture to edit loops. It does not fit dia-iterate's job, which is editing an existing draft the user cares about, so its absence is fine.
- **Regression stop with rollback.** This is the early-stopping pattern from training. Prechelt's rule, as quoted on Wikipedia, is to "stop training as soon as the error on the validation set is higher than it was the last time it was checked" and use the previous weights [16]. The pattern needs a metric that measures quality. dia-iterate's metric does not (finding 1).
- **Fixed point.** CRITIC's "answer remains the same for two consecutive corrections" [4] is a fixed-point test.
- **Default cap of 3.** The evidence supports it:
  - CRITIC uses n = 3, with most of the benefit in 2-3 rounds [4].
  - Self-Refine caps at 4 and shows diminishing returns [2].
  - Without external feedback, Huang's round 2 is no better than round 1 and sometimes worse [1].

### 3.6 Vendor output filters behind the content-filter guardrails

- **Anthropic.** The help centre says "Output blocked by content filtering policy" errors "generally arise from Anthropic's efforts to prevent Claude from being used to replicate or regurgitate pre-existing materials" [17]. The Messages API also has a `refusal` stop reason, which the client handles: "Read `stop_details` and retry on a fallback model" [22].
- **Field reports on GitHub** (single reports each, not vendor statements):
  - Writing a standard MIT LICENSE was followed by blocked responses. A later Read of the same file "was also blocked" [18].
  - Generating LICENSE, CODE_OF_CONDUCT and similar files was blocked, then "successfully created the files on retry" [19].
  - Blocks mid-session lost work, and "starting a new session loses all the context" [20].
  - In one thread, a user found that starting a fresh session instead of `--resume` "appears to have fixed the problem" [21].
- **Google Gemini / Vertex AI** has an explicit `RECITATION` finish reason: generation "stopped because the content potentially contains copyright violations" [23].
- **Azure OpenAI** has a "protected material" filter that flags output "that closely matches copyrighted text or code", such as "song lyrics, articles, recipes, and selected web content" [24].
- **ChatGPT.** I found no equivalent documentation for the ChatGPT consumer surface. This is [unverified] either way.

Conclusion: the guardrails' premise, that verbatim reproduction of existing text can block a whole response on Claude, is documented [17]. The specific advice (one retry, then change shape, then start a new conversation; license texts are high risk) matches the observed failure pattern in [18]-[21]. Two finer claims are not documented by any vendor I found and should be labelled as observation: that overlap "sentence by sentence" is the trigger (`SKILL.md:33`), and that set texts "can block even when reworded" (`:87`) [unverified].

### 3.7 Invocation controls on each surface

- **Codex / ChatGPT.** `allow_implicit_invocation` defaults to true. When false, "Codex won't implicitly invoke the skill based on user prompt; explicit `$skill` invocation still works". In ChatGPT the explicit route is `@` [25].
- **What false actually does in Codex.** A Codex maintainer-side analysis traced it: false removes the skill from the model-visible catalog (`hidden_from_prompt`), while `$name` mentions still select it [26]. P3 confirmed the hiding: the three skills with implicit invocation allowed appear in the model-visible list, and dia-iterate does not.
- **The Codex picker.** A later comment on the same issue reports that the `$` picker submits the display name (for example `$Wayfinder`), which fails a case-sensitive lookup; typing the lowercase name works [26]. dia-iterate's display name is "Dia: Iterate" (`agents/openai.yaml:2`). This is a single report.
- **Claude Code** offers `disable-model-invocation: true` to stop the model invoking a skill on its own [27]. Spec §7.2 bars that key because claude.ai upload rejects it, so on Claude surfaces the description text is the only guard. P6 shows that it works.

## 4. Fidelity audit

Verdicts:

- **matches**: the rule agrees with the source.
- **loose**: in the spirit of the source, with gaps.
- **departs**: contradicts the named source.
- **unsupported**: no source found; a design choice.

| # | Skill rule (file:line) | What the source says | Verdict |
|---|---|---|---|
| A1 | Huang: repeated self-judgment "brings no gain on reasoning tasks and often makes them worse" (`SKILL.md:14`) | "struggle … at times … even degrades"; most Table 3-4 cells drop [1] | matches (slightly overstated; scope is reasoning tasks) |
| A2 | "dia-refine run over several rounds" (`SKILL.md:14`); upstream "Self-refine run over several rounds" | Self-Refine's feedback is the same model's [2]. dia-refine also accepts your own re-derivation as a basis (`dia-refine/SKILL.md:32`); dia-iterate does not (`verification-sources.md:7`) | departs (as a label) |
| A3 | Round = assign external method → verify → fix only confirmed (`SKILL.md:29-34`) | CRITIC: verify with tools → stop if correct → correct [4]; success needs reliable external feedback [5] | matches CRITIC (unnamed) |
| A4 | Rereading is not an external method (`SKILL.md:32`, `:81`) | Intrinsic self-correction unreliable [1][5]; collapse under self-critique [12]; CRITIC without tools ≈ no gain [4] | matches |
| A5 | Name defects from a fixed checklist (`SKILL.md:31`) | Finding errors is the weak step [10]; CoVe enumerates verification questions per claim [8] | loose (relies on suspicion, not claim enumeration) |
| A6 | Three verdicts: confirmed / refuted / unverifiable (`SKILL.md:33`) | No source uses this exact triad; CRITIC critiques are free text [4] | unsupported (sound design) |
| A7 | Smallest edit; no hedging, no rewriting (`SKILL.md:34`) | Iterative regeneration distorts [14]; self-refine fluency gains co-occur with bias amplification [6] | loose support |
| A8 | Lock verified items (`SKILL.md:35`) | Correct → incorrect flips [1]; 46% flips under challenge [9]; gains surge when only erroneous items are modified [4] | matches |
| A9 | Tool-less: usually stop after round 1 (`SKILL.md:38-40`) | Intrinsic correction unreliable except for decomposable verification [5]; CoVe gains without tools on list-style facts [8] | matches, conservatively (forgoes CoVe-type gains) |
| A10 | Regression → roll back and stop (`SKILL.md:46`) | Early stopping: stop when the held-out error rises; keep previous weights [16]; Self-Refine non-monotonic [2] | matches in shape; metric departs (§7, F1) |
| A11 | Zero defects → stop (`SKILL.md:47`) | CRITIC returns when critiques indicate correct [4] | matches; overlaps A12 (F3) |
| A12 | Verification exhausted → stop, hand over list (`SKILL.md:48`) | No direct source; follows from [1][5] | unsupported (reasonable) |
| A13 | Fixed point → stop (`SKILL.md:49`) | CRITIC stops if the answer is unchanged over two corrections [4] | matches |
| A14 | Round cap, default 3 (`SKILL.md:16`, `:50`) | CRITIC n = 3, 2-3 rounds give most benefit [4]; Self-Refine max 4, diminishing [2]; round 2 no better without feedback [1] | matches |
| A15 | Invocation is not an error report (`SKILL.md:80`) | FlipFlop [9]; sycophancy [13] | matches |
| A16 | User's claims about the world are a single source (`verification-sources.md:17`) | Sycophancy toward user beliefs [13] | matches |
| A17 | Style applied once, in round 1, without external check (`SKILL.md:82`; `verification-sources.md:15`) | Self-refine improves fluency while amplifying self-bias [6] | loose; conflicts internally with `:81` (F4) |
| A18 | Code verified by "execution, tests" (`verification-sources.md:8`) | Self-written tests give false positives [3]; feedback quality is the bottleneck [11] | loose (tests' provenance unspecified) |
| A19 | One search snippet is not confirmation (`verification-sources.md:31`) | A sound verifier is what matters [12]; weak verifiers mislead [3] | matches in spirit |
| A20 | Content-filter guardrails (`SKILL.md:33`, `:56`, `:85-87`) | Anthropic filter targets regurgitation [17]; license/doc blocks, retry and new-session reports [18]-[21]; RECITATION [23]; protected material [24] | matches for Claude; mechanism details [unverified] |
| A21 | First word only; `allow_implicit_invocation: false` (`SKILL.md:20-22`; `openai.yaml:7`) | false hides the skill from the catalog; `$name` still works [25][26] | matches as policy; the first-word route cannot fire on Codex (F2) |

## 5. Lineage: what changed from upstream, and what was lost

### 5.1 Diff summary (upstream `recursive-refine` → `dia-iterate`)

Changes (from a word-normalised diff of the two SKILL.md files and the reference):

- **Frontmatter.** Adds `license`, `metadata.version 1.0.0` and `lineage`. The description now lists all five stop conditions and the explicit-name invocations.
- **Removed: skill mode.** The upstream description sentence (`upstream/.../SKILL.md:3`), the "Skill mode" target (`:22`), "Skill mode in brief" (`:70-79`) and `references/skill-loop.md` are gone, as spec §5.7 and non-goal 2 require.
- **Added: "Without tools"** (`SKILL.md:38-40`), the rule required by spec §5.7.
- **Added: output language rule** (`SKILL.md:56`).
- **Invocation widened** (`SKILL.md:20`) from "at the start of the message" to "first word, or explicit by name".
- **Verified now includes user material.** "Only items for which a tool actually ran" (`upstream/.../SKILL.md:87`) became "checked by an external method this session (a tool that actually ran, or the user's instructions and supplied material)" (`SKILL.md:84`). This keeps the guardrail consistent with the tool-less rule.
- **Context7 generalised** to "an official-documentation lookup tool (for example Context7), or a fetch of official docs" (`verification-sources.md:9`), per spec §5.7.
- Everything else is word-for-word, apart from punctuation.

The owner's design notes in `upstream/superclaude-stable-47f791b/docs-features/` contain no material on recursive-refine or self-refine. A search for "refine", "iterat" and "content filter" there returned no hits. The only rationale on record is spec §5.7 and D2.

### 5.2 Was anything needed for output mode lost?

The skill-folder procedure was rightly dropped: it needs `cp -r`, `diff -u`, subagents and `package_skill`, none of which exist on chat surfaces. But `skill-loop.md` held three ideas that were never specific to skill mode:

1. **A better regression definition.** "Regression means 'total confirmed defects rose' or 'a defect that had disappeared in the previous round came back'" (`upstream/.../skill-loop.md:32`). Output mode instead uses "fewer items passed verification than in the previous round" (`SKILL.md:46`), which is defective (F1). The skill-mode wording is the one to port.
2. **The shared-blind-spot limit.** "When the evaluator is the same model as the executor, errors they share go uncaught. Human review fills that gap" (`skill-loop.md:56`; also `:13`). Output mode has the same structure: the model that wrote the draft names its defects. Tyen et al. [10] make this concrete.
3. **Coverage caps improvement.** "The test set's coverage is the improvement's coverage" (`skill-loop.md:55`). Output mode's analogue is that only the claims named in step 1 can improve. The intro states the related point that verification quality caps improvement (`SKILL.md:14`), but not the recall point.

Nothing else in skill mode applies to output mode.

## 6. Risks and failure modes

### 6.1 On LLMs generally

- **Spurious regression stops.** In round 2, fewer items are usually examined than in round 1, because round 1's items are locked. By the letter of `SKILL.md:46`, round 2 then "regresses" and is rolled back even when its fix was externally confirmed. See F1.
- **"No defects" reported when nothing was checkable.** Under the stated order, "zero defects: nothing was confirmed" (`:47`) fires before "verification exhausted" (`:48`). A tool-less run whose named defects are all unverifiable would end "Stopped because: zero defects", and `:52` would have it "say so". That tells the user the draft is clean when it was in fact unchecked. P8 runs reported "verification exhausted", so the model resolved the conflict sensibly at n=2. The text still invites the wrong report.
- **Low recall.** Step 1 depends on the model suspecting a defect [10]. Fluent wrong claims, which are the ones the model believes, are the least likely to be named. CoVe-style enumeration of every checkable claim addresses this [8].
- **Unverified edits through the side doors.** Three rules allow edits without an external check:
  - style and padding in round 1 (`:82`; `verification-sources.md:15`);
  - an un-run counterexample for a logical leap, "apply once, in round 1" (`verification-sources.md:14`);
  - syntax errors "settled without running" (`verification-sources.md:8`).

  The first two contradict `:81` ("do not make edits in such a round") and the self-bias findings [6].
- **Weak verifiers counted as external.** Tests the model wrote itself in the same session [3], or a single search result echoing a common error. The reference covers snippets (`:31`) but not self-written tests.
- **Correcting a misquotation.** Fixing it means inserting the source's words. `SKILL.md:33` forbids copying source text into the final version, and `:34` only allows deleting a "groundless" quotation. A slightly wrong quotation of a real source therefore has no permitted fix. That pushes the model either to break the rule or to delete a correct-in-substance quote.

### 6.2 On tool-less and mobile surfaces

- **Expected behaviour is a one-round stop** that lists what would make each item checkable. P8 passed this in Claude Code with tools disabled (n=2). Claude mobile, ChatGPT mobile and ChatGPT desktop are untested (P2, P4, P5 are open).
- **Arithmetic stays unverified without code.** `verification-sources.md:7` makes "17 × 23" unverifiable without code execution. dia-refine allows "re-deriving the logic or calculation yourself" (`dia-refine/SKILL.md:32`). A user moving from dia-refine to dia-iterate on mobile sees fewer things checked by the "stronger" skill. The strictness is defensible: Huang's GSM8K drops show that self-recomputation can flip correct answers [1]. But it is undocumented as a deliberate difference, and `SKILL.md:14` implies the two skills share standards.
- **Wide tables on phones.** The round-summary table has seven columns (`SKILL.md:64`); on a phone it may wrap badly [unverified].
- **The filter retry assumes the model can see the block.** In chat apps a blocked response surfaces as an error to the user. The next turn begins only when the user retries or writes again, and whether the model is told that the prior output was blocked is not documented for consumer surfaces [unverified]. On the API, handling `refusal` is the client's job [22]. So "retry the same output at most once" (`SKILL.md:85`) is really guidance for when the user reports a block.

### 6.3 Across surfaces (Claude / Codex / ChatGPT)

- **Claude.** No `disable-model-invocation`: the key is barred for claude.ai upload (spec §7.2). The description's "Use only when … begins with dia-iterate" is the only guard, and P6 shows that it held in Claude Code.
- **Codex.** `allow_implicit_invocation: false` hides the skill from the model [26]; P3 confirmed this. Consequences:
  - A plain message beginning `dia-iterate` cannot trigger the skill on Codex, because the model does not know it exists. That contradicts the Codex column of spec §4 ("a message starting `dia-iterate`, or `$dia:dia-iterate`").
  - The fallback in `SKILL.md:22` ("ask in one line for a message beginning with `dia-iterate`") is unreachable there.
  - If the skill is loaded explicitly and the fallback fires anyway, its advice ("type `dia-iterate`") would not work on Codex.
  - `$dia-iterate` (`SKILL.md:20`; `openai.yaml:4` `default_prompt`) does not resolve on the plugin route; only `$dia:dia-iterate` does (P3). It resolves only for a copied folder.
  - A single report says the Codex `$` picker submits the display name ("Dia: Iterate") and fails [26].
- **ChatGPT.** The explicit route is `@` [25]. dia-iterate never mentions `@dia-iterate`, though dia-refine does (`dia-refine/SKILL.md:18`). Whether skills work on ChatGPT Pro at all is open (O4).
- **Filters differ by vendor.** Claude errors [17]; Gemini `RECITATION` [23]; Azure protected material [24]; ChatGPT consumer unknown. The guardrails are written for Claude's behaviour and are harmless elsewhere, but their reasons are stated as universal fact (`SKILL.md:33`, `:56`).

## 7. Findings and recommendations (proposals only)

**F1 (high): the regression metric triggers on normal progress.**
- Evidence: `SKILL.md:46` treats "fewer items passed verification than in the previous round" as regression. Locked items are not re-examined, so later rounds examine fewer items and spuriously "regress". Early stopping requires a quality metric [16]. Upstream skill mode already had a sound definition (`skill-loop.md:32`).
- Proposal, replacing `SKILL.md:46`:
  > 1. **Regression**: a locked item changed; a fix introduced a new confirmed defect; or a defect fixed in an earlier round came back. Roll back to the previous round's result and stop.

**F2 (high): the invocation text is wrong for Codex, and the ChatGPT route is missing.**
- Evidence:
  - P3: `$dia-<x>` does not resolve on the plugin route, and false-policy skills are hidden from the model, so a first-word `dia-iterate` cannot load the skill on Codex [26].
  - `agents/openai.yaml:4` uses `$dia-iterate`.
  - `@` is ChatGPT's explicit route [25] and is not listed.
  - Picker display-name failure: single report [26].
- Proposals:
  - Edit `SKILL.md:20`:
    > Activate only when `dia-iterate` is the first word of the message, or on an explicit invocation by name (`/dia:dia-iterate` in Claude; `$dia:dia-iterate` in Codex, or `$dia-iterate` for a copied skill folder; `@dia-iterate` in ChatGPT).
  - Edit `SKILL.md:22`:
    > … ask in one line for a message that begins with `dia-iterate` (or, in Codex or ChatGPT, that invokes the skill by name), then stop.
  - Edit `openai.yaml:4`: `default_prompt: "Use $dia:dia-iterate to run verified review rounds on the previous answer: "`. This depends on open question Q2.
  - Owner action outside this skill: correct the dia-iterate row of spec §4. Codex supports the explicit name only.

**F3 (medium): "zero defects" swallows "verification exhausted".**
- Evidence: the order at `SKILL.md:46-50` and the wording at `:47` ("nothing was confirmed"), together with `:52`. A tool-less run with all defects unverifiable would be reported as having no defects (§6.1).
- Proposal, replacing `:47`:
  > 2. **Zero defects**: no defect was named, or every named defect was refuted. Stop.
- And replace `:52`:
  > If round 1 names no defects, or refutes all of them, say so and end. If defects were named but none could be checked, the stop is "verification exhausted", not "zero defects".

**F4 (medium): side-door edits without external verification.**
- Evidence: `SKILL.md:82` and `verification-sources.md:8`, `:14`, `:15` permit round-1 edits on style, padding, un-run counterexamples and "obvious" syntax. That contradicts `:81` and `:84`. Self-refinement of fluency amplifies self-bias [6]; un-run self-critique collapses [12].
- Proposal (option a, strict): replace `:82` with
  > Style, concision and padding are edited only against criteria the user supplied. Without such criteria, list them under a final "Suggestions (not applied)" line instead of editing.

  And in `verification-sources.md:14`, replace "Apply once, in round 1 …" with "Not grounds for an edit; list under Unverified with the counterexample".
- Option b, if the owner wants the round-1 exception kept: say so explicitly at `:81`:
  > … Do not make edits in such a round. The one exception: style, concision and syntax edits in round 1, which are listed separately in the change list as "(style, not verified)".

**F5 (medium): defect recall depends on suspicion.**
- Evidence: `SKILL.md:31`. LLMs are poor at finding their own errors [10]; enumerating verification questions per claim reduces hallucination [8]. dia-refine already has "list every candidate … include the premises" (`dia-refine/SKILL.md:30`).
- Proposal, appending to step 1:
  > List every checkable claim (number, date, name, version, quotation, API, stated requirement) as a candidate, whether or not it looks wrong; do not filter by severity. Fluent claims you believe are the ones least likely to be named otherwise.

**F6 (medium): there is no legal fix for a misquotation.**
- Evidence: `SKILL.md:33` (never copy source text into the final version) versus `:34` (only delete groundless quotations).
- Proposal, adding to step 4:
  > A quotation that misstates its source may be corrected with the source's exact words if the quoted span is one sentence or less, marked as a quotation with its source; for longer passages, cut the quotation to its location (work, section) and flag it in the change list.

**F7 (medium): the label names the wrong method; Huang's wording is overstated.**
- Evidence: A1 and A2. The procedure is CRITIC's verify-then-correct [4], not Self-Refine [2], and dia-refine's standard differs (re-derivation counts there).
- Proposal, replacing the first sentence of `SKILL.md:14`:
  > A verify-then-correct loop in the style of CRITIC (Gou et al., ICLR 2024, arXiv:2305.11738): each round needs a signal from outside the model. Unlike dia-refine, your own re-derivation does not count here as verification.
- And change "often makes them worse" to "at times makes them worse".

**F8 (medium): the content-filter rules mix observation with mechanism.**
- Evidence: the vendor docs support "regurgitation is filtered" [17][23][24]. The retry and new-session advice matches field reports [18]-[21]. "Sentence by sentence" and "even when reworded" are not documented [unverified], and the model may not see a block (§6.2).
- Proposal, replacing `SKILL.md:85`:
  > If the user reports that a response was blocked by content filtering (or the conversation shows an empty or errored previous turn), produce the same output at most once more …
- Optionally rephrase `:33` as:
  > Long verbatim overlap with an existing document can trigger the host's content filter, which blocks the whole response.

  This states it as an observed risk rather than a rule of the filter.

**F9 (low): tests written in the same session are not fully external.**
- Evidence: Reflexion's false positives from self-written tests [3]; self-repair is bounded by feedback quality [11]. `verification-sources.md:8`.
- Proposal, appending to the Code row:
  > Tests you write yourself share your blind spots: prefer existing or user-supplied tests, and say in the log which kind ran.

**F10 (low): port the shared-blind-spot limit from skill-loop.md.**
- Evidence: §5.2 items 2 and 3; `skill-loop.md:55-56`.
- Proposal, a sentence at the end of `SKILL.md:14`:
  > Only defects you name can be verified; errors you share with the draft go unnamed, so the round summary is a lower bound, not a clean bill.

**F11 (low): locks are invisible in the output.**
- Evidence: the regression rule depends on the locked set (`:35`, `:46`), but the round summary (`:64-68`) does not record it, so the user cannot audit a rollback.
- Proposal: add a `Locked` column to the round-summary table, or one line under it: `Locked: n items (list)`.

**F12 (low): mobile readability of the round table.**
- Evidence: the table is seven columns wide (`:64`); phone rendering is [unverified].
- Proposal:
  > On narrow screens or when the round table would wrap, one line per round is acceptable: `Round 1: named 4, confirmed 2, refuted 1, unverifiable 1; methods …; changes …`.

**F13 (low): define "materially identical".**
- Evidence: `:49`. Because edits occur only on confirmed defects, the fixed point coincides with zero confirmed fixes; CRITIC's test is "unchanged over two consecutive corrections" [4].
- Proposal:
  > 4. **Fixed point**: this round changed nothing in the text (a safety net; it normally coincides with 2).

## 8. Open questions for the owner

1. **Q1, style edits.** Strict (F4 option a: style only against user criteria) or a labelled round-1 exception (option b)? dia-refine applies concision edits freely, so option a makes the two skills differ further.
2. **Q2, the Codex `default_prompt` name.** `$dia:dia-iterate` (plugin route, P3) or `$dia-iterate` (folder-copy route)? Only one can be right per package. The spec currently ships the plugin route, which argues for `$dia:dia-iterate`. Should the display name also be lowercased (`dia-iterate`) because of the picker report [26]?
3. **Q3, re-derivation.** Should dia-iterate accept your own re-derivation of arithmetic as a weaker, labelled verdict ("re-derived") that can lock but never change a result? That would align it with dia-refine. The evidence that self-recomputation can flip correct answers [1] argues against letting it change anything.
4. **Q4, tool-less coverage.** P8 ran in headless Claude Code on Sonnet only (n=2). Should P2/P5 include one dia-iterate prompt with a known-wrong fact to confirm the round-1 stop on Claude mobile and ChatGPT mobile?
5. **Q5, round cap.** Keep the default at 3? The CRITIC evidence (2-3 rounds give most of the benefit) supports 3 when tools exist. Tool-less runs end at 1 anyway.
6. **Q6, ChatGPT filters.** Is there any first-hand record of ChatGPT blocking reproduced text in the owner's use? If not, the guardrail reasons could be scoped to "some hosts" (F8).

## Sources

[1] https://arxiv.org/abs/2310.01798 — Huang et al. 2024, Large Language Models Cannot Self-Correct Reasoning Yet (ICLR 2024)
[2] https://arxiv.org/abs/2303.17651 — Madaan et al. 2023, Self-Refine: Iterative Refinement with Self-Feedback
[3] https://arxiv.org/abs/2303.11366 — Shinn et al. 2023, Reflexion: Language Agents with Verbal Reinforcement Learning
[4] https://arxiv.org/abs/2305.11738 — Gou et al. 2024, CRITIC: LLMs Can Self-Correct with Tool-Interactive Critiquing (ICLR 2024)
[5] https://arxiv.org/abs/2406.01297 — Kamoi et al. 2024, When Can LLMs Actually Correct Their Own Mistakes? (TACL)
[6] https://arxiv.org/abs/2402.11436 — Xu et al. 2024, Pride and Prejudice: LLM Amplifies Self-Bias in Self-Refinement
[7] https://arxiv.org/abs/2409.12917 — Kumar et al. 2024, Training Language Models to Self-Correct via Reinforcement Learning (SCoRe)
[8] https://arxiv.org/abs/2309.11495 — Dhuliawala et al. 2023, Chain-of-Verification Reduces Hallucination in LLMs
[9] https://arxiv.org/abs/2311.08596 — Laban et al. 2023, Are You Sure? Challenging LLMs Leads to Performance Drops in The FlipFlop Experiment
[10] https://arxiv.org/abs/2311.08516 — Tyen et al. 2023, LLMs cannot find reasoning errors, but can correct them given the error location
[11] https://arxiv.org/abs/2306.09896 — Olausson et al. 2024, Is Self-Repair a Silver Bullet for Code Generation? (ICLR 2024)
[12] https://arxiv.org/abs/2402.08115 — Stechly et al. 2024, On the Self-Verification Limitations of LLMs on Reasoning and Planning Tasks
[13] https://arxiv.org/abs/2310.13548 — Sharma et al. 2023, Towards Understanding Sycophancy in Language Models
[14] https://arxiv.org/abs/2502.20258 — Mohamed et al. 2025, LLM as a Broken Telephone: Iterative Generation Distorts Information
[15] https://arxiv.org/abs/2110.14168 — Cobbe et al. 2021, Training Verifiers to Solve Math Word Problems
[16] https://en.wikipedia.org/wiki/Early_stopping — Wikipedia, Early stopping (quotes Prechelt, Early Stopping - But When?)
[17] https://support.claude.com/en/articles/10023638-why-am-i-receiving-an-output-blocked-by-content-filtering-policy-error — Claude Help Center, Why am I receiving an 'Output blocked by content filtering policy' error?
[18] https://github.com/anthropics/claude-code/issues/33053 — anthropics/claude-code #33053, Content filtering policy blocks legitimate license text output
[19] https://github.com/anthropics/claude-code/issues/16159 — anthropics/claude-code #16159, False positive: content filtering blocking documentation creation
[20] https://github.com/anthropics/claude-code/issues/21880 — anthropics/claude-code #21880, Content filtering blocks legitimate development work mid-session
[21] https://github.com/anthropics/claude-code/issues/2111 — anthropics/claude-code #2111, Output blocked by content filtering policy
[22] https://platform.claude.com/docs/en/build-with-claude/handling-stop-reasons — Claude API docs, Stop reasons and fallback
[23] https://docs.cloud.google.com/python/docs/reference/aiplatform/latest/google.cloud.aiplatform_v1.types.Candidate.FinishReason — Google Cloud Vertex AI, Candidate.FinishReason
[24] https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/content-filter-protected-material — Microsoft Learn, Protected material detection filter
[25] https://learn.chatgpt.com/docs/build-skills — ChatGPT/Codex, Build skills
[26] https://github.com/openai/codex/issues/40600 — openai/codex #40600, allow_implicit_invocation: false and explicit $skill invocation
[27] https://code.claude.com/docs/en/skills — Claude Code Docs, Extend Claude with skills
