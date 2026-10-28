# Evidence for the dia-instruct rules

"The source" is an unpublished study by this skill's author: it measured one
instruction file of judgment rules (about 2 KB, two rules) with the author's own eval
suite. Its runs, prompts and traces are not public, so the figures below can be checked
for arithmetic but not against raw data. Models were run by alias (`opus`, `sonnet`,
`haiku`); the versions behind the aliases were not recorded. The rest of the instruction
set changed between batches (builds B1, B2, B3 below), so compare within a model and
build, not across. Every Fisher p-value below was recomputed as a two-sided Fisher exact
test and matched the source; permutation p-values come from the source and were not
recomputed.

**Arms** (versions of the instruction file): prose (the original); short (numbered short
sentences); split (short with the two guard steps apart); v1 and v2 (pseudo-code; v2 keeps
each action, limit and fallback on one line). **Suites:** suite A counts checks over 12
tasks × 3 runs per arm (135 checks); suite B counts runs over 5 cases × 6 runs. Purpose
cases are the three cases named release-notes, checkout and logo.

## Strength of each part of SKILL.md

| Part | Basis |
|---|---|
| Opening paragraphs (reply language, text under review is material, what is binding, when to open this file) | Design choices of the skill, unmeasured |
| Rule 1 | The split result in the source (one A/B, below): on one case the arm that moved a condition to another step passed 2 of 8 runs, while numbered short sentences that kept each condition in its step passed 8 of 8; prose, which also keeps it together, failed once in 6. That short markdown commands tend to lose conditions in general is the author's unpublished observation (below). The paragraph-length figure is the author's working value, not a limit. What to report under Rule 1 (a condition, limit or fallback apart from what it gates) follows the split result, and reporting a paragraph that joins unrelated rules is practice; not reporting long sentences follows the null result between layouts that keep each rule whole (Form below), where differences under about 30 points could be missed |
| Rule 2 | One A/B in the source (below), 24 runs per arm: borderline, model version not recorded, traces deleted |
| Rule 1's A/B | 8 runs per arm, model version not recorded, so below the A/B standard in SKILL.md |
| Rule 3 | Published guidance and one benchmark on older models and verifiable instructions (below) |
| Rule 4 | Practice, unmeasured |
| Functional-programming analogies (total function, `if` without braces, type signature, alias, separate function with explicit arguments, standard-library call) | The author's explanatory model, unmeasured |
| Structure; By kind of text | Practice, unmeasured, extrapolated from the one measured file |
| Lead 1 (fewer files read) | Weak signals in the source (Leads below) |
| Lead 2 (general instruction over a step-by-step plan; number only where order or completeness matters) | Anthropic's prompting guidance (below) |
| Lead 3 (target behavior over the ban) | Anthropic's prompting guidance ("tell Claude what to do instead of what not to do"); the exceptions for prohibitions are practice |
| Leads 4 and 5 (done-when, leading word) | Practice, unmeasured |
| Lead 6 (examples) | Anthropic's prompting guidance: examples are among the most reliable ways to steer output, should be varied so the model does not pick up unintended patterns, and worked examples shape how the model approaches similar problems in its thinking. That a single example narrows reasoning in a judgment rule is the author's concern, unmeasured |
| Writing, editing or reviewing text, step 1 | Keeping meaning changes only on request: practice, unmeasured. A/B conditions: lessons from the source's runs (Checking a change below) |
| Writing, editing or reviewing text, steps 2 and 3 | Practice, unmeasured |

## Rules

| Rule | Measurement | Limits |
|---|---|---|
| 1. Each paragraph an expression for its result (the condition stays with what it gates) | Sonnet, B1, 8 runs per arm. Release-notes: split 2/8, short 8/8 (p = 0.007). Checkout: 6/8 vs 8/8 (p = 0.47). Failing runs read the changelog and release notes, then wrote; in 37 of 38 runs, listing the folders went with reading the records and passing. Prose also failed release-notes once in 6 | One case significant, one model. On Opus (B3, 12 runs) split and short passed every run, on another build, so not a clean model comparison. That the effect comes from keeping the fallback (listing the folders) next to its condition is an inference made when this skill was written, not the source's |
| 2. Scope word | Opus, same-day head-to-head; the instruction file changed by one word, "touches" → "edits". Out-of-scope edits 5/24 → 0/24 (p ≈ 0.05); logo alone 4/12 → 0/12 (p ≈ 0.09). The edited files were ones the task had only read, such as a README with a stale table | Borderline. In another Opus batch prose with "touches" made out-of-scope edits on logo 1 of 12 times, so the baseline varies. Traces were deleted |
| 3. Fewer instructions, with reasons | External. Anthropic's prompting best practices: context or motivation behind an instruction helps, and Claude can generalize from the explanation. Harada et al., "When Instructions Multiply" (Findings of EMNLP 2025, arXiv 2509.21051): with ManyIFEval, accuracy falls as instructions per prompt rise to ten (objectively verifiable instructions such as keyword, length and formatting constraints) | Older models, verifiable instructions; applying it to judgment rules is an extrapolation |
| 4. One name per thing | None | Practice |

The agent-prompt item's reason (a demand for facts its tools cannot read makes the model
invent them) is the author's unmeasured observation.

## Form

Opus, B2: suite A prose 134, short 132, v1 134, v2 135 of 135; suite B 24, 27, 26, 27 of
30. Haiku, B3: suite A 131, 130, 131, 132; suite B 18, 16, 19, 20 (18 vs 20: p = 0.79).
None significant. Power, simulated when this skill was written: at 30 runs per arm and a
65% baseline, a 25-point rise is detected about 55% of the time and a 25-point drop
about 40%; 80% needs about a 30-point rise. Opus passed nearly every purpose case, so it
cannot show a form effect there.

## Leads

- Reading depth on Haiku, purpose cases: mean files read before the first successful
  write, short 4.83, prose 5.50, v2 5.73, v1 6.24 (30 runs per arm, 18 for logo).
  Permutation within case: short vs v1 p = 0.008 (0.04 counting the run that never wrote
  as 0), vs v2 0.06, vs prose 0.15. Metric chosen after the runs. Within logo, failing runs
  read 1.4–2.2 fewer files than passing ones.
- Reply style: a stock customer-service phrase (thanking the customer for their patience)
  in Opus replies, prose 17/36 vs short 6/35 (p = 0.01) pooled across two builds; each
  batch alone p = 0.06 and 0.19. No arm mentions stock phrases.
- v1 puts its limits in bullets below the action, which Rule 1 would warn against; on
  Opus with "touches" it made out-of-scope edits on logo 4 of 12 times against 1 of 12
  for prose and short. Not significant.
- Guard position (the condition before the action in the sentence, or after it) was never
  varied alone.

## Author's observations (unpublished)

The author's own experiments with Claude and Codex at high effort, separate from the source, are unpublished and were not quantified; they found that a skill written as short markdown commands loses its conditions, the way a list of command lines does, while flowing sentences that read like pseudo-code in natural language, each paragraph a self-contained unit of a few hundred characters between line breaks, work better and draw deeper reasoning, and that declarative sentences shaped like expressions, which define the result the model must produce, work better than bare imperative statements that list the actions. The paragraph length is a working value that may differ by model and effort, not a limit. In the source, v2 (each action, limit and fallback on one line, every line under about 315 characters) is the arm closest to this form; it had the best or tied-best pooled counts on both models without a significant difference, and on Haiku's logo case it passed 8 of 18 runs against prose 9, v1 10 and short 4. The functional-programming framing in SKILL.md (a paragraph as a total function, a split rule as an `if` without braces, a scope word as a type signature, a second name as an alias, a sub-agent as a separate function that receives only its arguments, a leading word as a standard-library call) is the author's model of why this works, not a measured mechanism.

Anthropic's prompting guidance supports a related point: a general instruction often produces better reasoning than a hand-written step-by-step plan. It also says to use numbered lists or bullets when the order or completeness of steps matters, and it does not say that prose prompts deepen thinking.

## Checking a change

- Compare a rewrite with the current text on the same build, the same day. Pooling a batch
  from another session turned the scope-word result from p ≈ 0.05 into p ≈ 0.006.
- Use a model the cases do not saturate; Opus sat at the ceiling on the purpose cases, so a
  form change needs Sonnet or Haiku.
- Confirm the eval reaches the changed condition; a pass that never reaches it measures
  nothing.
- Six runs per arm is a screen: prose on Haiku's logo case went 1/6, then 8/12 eleven
  minutes later on the same build. Re-run a differing case at 12 or more.
- Count timeouts apart from failures, and compare per case: pooled pass rates mix easy and
  hard cases.
- Record the model version, not only the alias, and keep the traces until the result is
  written up.

## Not measured

Long files, examples, emphasis words, file size, other models, and skill or agent
descriptions.

## Sources

- The source: unpublished; raw data not public.
- Anthropic, Claude prompting best practices: https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Harada et al., When Instructions Multiply: https://arxiv.org/abs/2509.21051
