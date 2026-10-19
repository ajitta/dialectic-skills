# Evidence: is explanatory text in a SKILL.md worth its tokens?

Evidence base for the token audit of the seven dia skills. Every source below was fetched on 2026-10-20 (this session); claims that could not be sourced are marked [unverified], and my own inferences are labelled *inference*. Repo figures come from `docs/token-cost.md`.

The question: the skill bodies carry rationale sentences ("because …"), scholarly citations (Stephanus numbers, arXiv ids), attributions ("after Adorno", "Gou et al."), method history, and honest-label notes ("not Adorno's own procedure"). Do these change model behaviour, or do they only cost tokens?

## 1. Vendor guidance

### Anthropic

- **Give the reason behind an instruction.** Claude's prompting guide has a section "Add context to improve performance": giving the motivation behind an instruction "can help Claude better understand your goals and deliver more targeted responses". Its example replaces "NEVER use ellipses" with a version that says the output goes to a text-to-speech engine, adding: "Claude is smart enough to generalize from the explanation."[1]
- The same guide says newer models respond more strongly to the system prompt and may overtrigger, and recommends replacing "CRITICAL: You MUST use this tool when..." with "Use this tool when...".[1]
- Anthropic's own skill-creator skill says: "Explain the why… Today's LLMs are *smart*. They have good theory of mind", and calls ALWAYS/NEVER in capitals "a yellow flag". The same list includes "Keep the prompt lean. Remove things that aren't pulling their weight", judged by reading transcripts.[7]
- The constitution states the training-side version: Anthropic "generally favor[s] cultivating good values and judgment over strict rules… and we try to explain any rules", because "a minimal set of well-understood rules tends to generalize better than rules or decision procedures imposed as unexplained constraints".[8] This is about training, not prompts. It shows what the vendor believes, not a measured effect of rationales in a prompt.
- **Concision in skills.** The Skills best-practices page opens with "Concise is key… The context window is a public good". Its default assumption is "Claude is already very smart. Only add context Claude doesn't already have", and it asks of each item: "Does Claude really need this explanation?" and "Does this paragraph justify its token cost?"[2] Its bad example is a paragraph explaining what a PDF is before giving the instruction.[2]
- The same page says to keep SKILL.md under 500 lines, keep references one level deep, avoid time-sensitive information (old material goes in a collapsed "Old patterns" section), and build evaluations before writing extensive documentation, with "just enough content to address the gaps".[2] It also says to watch for "Missed connections", meaning Claude not following a reference it needed.[2]
- **Progressive disclosure.** Name and description load at startup, SKILL.md loads when the skill triggers, and bundled files load only when read. "There's no context penalty for bundled content that isn't used."[3][4]
- Claude Code's CLAUDE.md guidance applies the same reasoning to always-loaded text: "For each line, ask: 'Would removing this cause Claude to make mistakes?' If not, cut it. Bloated CLAUDE.md files cause Claude to ignore your actual instructions!" Its exclude list includes "Long explanations or tutorials" and "Standard language conventions Claude already knows".[6] It adds: "If Claude keeps doing something you don't want despite having a rule against it, the file is probably too long and the rule is getting lost", and emphasis works only when used sparingly.[6]
- Context engineering: aim for "the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome". Minimal "does not necessarily mean short", and prompts should sit at the "right altitude", neither brittle hardcoded logic nor vague guidance.[5]

### OpenAI (GPT-5 family, Codex, ChatGPT skills)

- GPT-5 follows instructions "with surgical precision". Contradictory or vague instructions therefore cost more: the model "expends reasoning tokens searching for a way to reconcile the contradictions".[9]
- GPT-5-Codex: "over prompting can reduce quality"; the core principle is "less is more"; start minimal and "add only the essential guidance you truly need". The Codex CLI prompt uses about 40% of the GPT-5 prompt's tokens.[10]
- The GPT-5.6 guidance says to remove one instruction group at a time and rerun evals. **Trim:** repeated rules, "process instructions for behavior the model already performs reliably", and examples that do not change behaviour. **Keep:** outcome, success and stopping criteria, "safety, business, evidence, and permission constraints", and output shape. Use ALWAYS/NEVER "only for true invariants"; for judgment calls "prefer decision rules" and "provide decision criteria".[11]
- The GPT-6 Astra post says skills should use progressive disclosure, with the root document as "a minimal router". It also says "overly specific guidance can now hinder results where it previously helped". Its recommended permission text includes a reason: "The local tests use disposable fixtures and have no production access. Run them…"[12]
- The Codex skill-creator says: "The entrypoint should be as short as the task permits while retaining important constraints. A large upper bound is not a target". References should hold "task-specific information that changes the agent's decisions", with no "generic tutorials already available from authoritative sources", no changelog, and nothing duplicated between the entrypoint and the references.[13] Codex loads SKILL.md only when it uses a skill, and caps the skill list at 2% of context or 8,000 characters, shortening descriptions first.[14]

**Vendor consensus.** Both vendors want (a) the reason behind a rule when it lets the model handle cases the rule did not anticipate, and (b) no text the model does not need in order to act. Neither vendor publishes numbers for (a). Their examples of useful reasons are one clause long and tied to the instruction.[1][12]

## 2. Research: do explanations or rationales improve adherence or generalization?

- **Explanations of examples help large models.** Across 40 tasks, explanations attached to few-shot answers improved performance and beat matched controls, "suggesting that the benefits are due to the link between an example and its explanation… However, only large models benefit."[15] This tested explanations of *examples*, not reasons attached to *rules*.
- **Reasoning over written principles generalizes (training-time).** Deliberative alignment teaches the model the spec and has it reason over the spec. It reports more precise policy adherence, fewer jailbreaks and fewer over-refusals at once, and better out-of-distribution generalization.[18] In Constitutional AI, one general principle ("do what's best for humanity") generalized in the largest models, while "more detailed constitutions still improve fine-grained control over specific types of harms".[17] *Inference:* a stated purpose helps with unanticipated cases, and specific rules still govern specific behaviour. That supports a short "why" plus a specific rule, not a long "why" in place of the rule.
- **Counter-evidence: models are not very sensitive to what instructions mean.** Models in Webson & Pavlick learned "just as fast" with irrelevant or "pathologically misleading" prompts as with good ones, including instruction-tuned models.[16] These are 2021–22 models on NLI tasks, so this is weak evidence about current models. Prompt effects are also "complicated and contingent": the same technique helps on some questions and hurts on others.[34]
- **What instructions cannot do.** A 2026 preprint found models agreeing to follow a process instruction and then not doing it. Removing the shortcut tool raised compliance from 0% to 75%; the authors conclude the gap is "environmentally afforded, not weight-encoded".[38] One preprint, not replicated. *Inference:* for process rules that matter, structure (scripts, templates, required record fields) does more than extra prose. Claude Code docs say the same about hooks versus CLAUDE.md: "Unlike CLAUDE.md instructions which are advisory, hooks are deterministic".[6]
- **Gap.** No controlled study found this session compares "rule" with "rule + one-clause reason" on adherence in a current model. The case for rationales rests on vendor guidance[1][7][11][12] and on adjacent findings.[15][17][18] [unverified: effect size for current models]

## 3. Do citations, attributions or authority cues inside a prompt change behaviour?

- **Authority cues change model judgments, usually in the wrong direction.** In LLM-as-judge tests, inserting a fake citation into one answer changed which answer the judge preferred; "quote and book-type references strongly influence most models".[23] Across 11 models, misleading endorsements did more damage as the stated expertise of the source rose, causing "accuracy degradation but also increased confidence in wrong answers"; reasoning models were not immune.[24] Another study found models swayed by added explanations "irrespective of the quality", and swayed more by authoritative framing, "but the effect is small in size".[25]
- **Personas and authority framing do not raise accuracy.** 162 personas in system prompts did "not improve model performance" on 2,410 factual questions; the effect of any one persona was "largely random".[21] Expert personas showed "no consistent benefit" on GPQA and MMLU-Pro, and low-knowledge personas hurt.[22]
- **Naming a source can steer retrieval.** "According to [source]" prompting raised the share of output quoting that corpus and often improved task performance; asking for less grounding lowered it.[26] That is an *instruction* to ground, not a citation offered as justification. *Inference:* a bare term of art the model already knows ("elenchus", "Paul's six question types", "CRITIC") can work as a retrieval key for a known method. A citation apparatus (page numbers, arXiv ids, "found that…") adds no further instruction. [unverified: no study isolates attribution-as-retrieval-key in instructions]
- **Implications for the dia skills.** The studies concern citations attached to *content being judged*, not to the skill's own rules, so they do not show that a citation in SKILL.md harms adherence. They do show that an authority cue is a lever on judgment. A skill whose job is to examine claims critically gains nothing from authority framing in its own body. Nothing found shows that citations make a model follow a procedure more faithfully.

## 4. Prompt length, instruction density and position

- **More simultaneous instructions, lower adherence.** In IFScale (500 keyword instructions, 20 models), the best frontier model reached 68% at maximum density. Reasoning models stayed "near-perfect" through 100–250 instructions before declining; other models declined linearly or exponentially.[27] ManyIFEval (up to 10 instructions) found performance "consistently degrades as the number of instructions increases", well predicted by instruction count alone.[28] A 2026 preprint found the perfect-response rate fell to zero by 80 rules for every model, format and placement tested.[33]
- **Position matters.** Retrieval is highest at the start or end of the context and lowest in the middle.[29] IFScale found later instructions violated more often, peaking at 150–200 instructions; "packing more important instructions towards the beginning of a prompt may help".[27] Multi-constraint prompts do better in hard-to-easy order.[32]
- **Irrelevant length hurts reasoning before the window fills.** Padding the same question with irrelevant text degraded reasoning "at much shorter input lengths than their technical maximum".[30] Context Rot found degradation with input length "in surprising and non-uniform ways" even on simple tasks.[31] Anthropic calls this an "attention budget" that "every new token… depletes".[5]
- **Scale check (inference).** These effects were measured with tens to hundreds of separate constraints or thousands of padding tokens. A dia SKILL.md is about 2.8k–4.7k Claude tokens on top of a ~19k base (`docs/token-cost.md`). Cutting a few hundred explanatory tokens is unlikely to change adherence measurably. What does matter at this scale: (a) the number of separate imperatives, since a rationale sentence that reads as one more rule adds to the count;[27][28] (b) contradictions, especially on GPT-5-class models;[9][11] (c) burying operative rules in the middle of scholarly prose.[27][29]

## 5. Prompt compression: what removing tokens costs

- LLMLingua reached up to 20x compression with about a 1.5-point drop. Its budget controller gives **instructions and questions less compression** than demonstrations, because they "have a direct influence on the generated results", and the ablation showed "Instructions and questions necessitate a lower compression ratio."[19]
- A six-method comparison across 13 datasets found compression hurts more in long contexts than short ones, and that moderate compression *improved* LongBench scores.[20]
- *Inference:* compression research supports cutting redundant and illustrative material and keeping instruction text largely intact. A skill body is mostly instruction, so the savings come from repeated rules, examples that do not change behaviour,[11] and explanation aimed at a human reader, not from shortening the rules themselves.

## 6. Cost mechanics on Claude Code

Pricing (Claude API list, fetched today), per million tokens:[35]

| Model | Base input | 5-min cache write | 1-h cache write | Cache hit |
|---|---|---|---|---|
| Sonnet 5.5 | $2 | $2.50 | $4 | $0.10 (0.05x) |
| Opus 5.5 | $4 | $5 | $8 | $0.20 (0.05x) |

- Loading a skill appends its text as a conversation message, "so the cached prefix stays intact".[36] Plugin skills never invalidate the cache; their content is appended after the existing conversation.[36] The main conversation uses the one-hour cache TTL on a subscription and five minutes on other access paths.[36]
- **300 extra tokens on Sonnet 5.5:** one cache write ≤ 300 × $4/M = $0.0012, then 300 × $0.10/M = $0.00003 per later turn. A 30-turn session totals about $0.002 (Opus: about $0.004). Each turn's cached read of the ~19k base costs about $0.0019, so 300 tokens is about 1.6% of the base per turn. Claude Code averages "around $13 per developer per active day".[37] *Conclusion:* the dollar cost of a few hundred tokens in a SKILL.md is negligible. The real costs are context share (§4) and, for subscribers, usage-limit consumption. [unverified: how subscription limits weight cached tokens]
- **Always-on text costs more per token than body text.** Descriptions load in every conversation (dia: 1,749 Claude tokens measured), while a body loads only on invocation.[3] On Codex the listing is capped and descriptions are shortened first when it overflows,[14] and OpenAI warns that long descriptions push the model to load skills that do not help.[12] A token saved in a description is worth more than one saved in a body.
- **Moving text to references is nearly free when it is not needed.** In the measured runs, `theory.md` was not read on the first turn (`docs/token-cost.md`), and unread bundled files cost nothing.[3] The risk is the reverse case: text needed for correct behaviour that the model does not open.[2]

## 7. Limits of this evidence

- Vendor guidance is current (2026 model generations) but gives no effect sizes. The research mostly predates current models, and several 2026 items are single preprints.[33][38]
- No study isolates the dia text classes (scholarly attribution, method history, honest-label notes) as prompt components. The rules below extrapolate, and their confidence is set accordingly.
- The surest test is the one both vendors prescribe: remove one class and rerun evals on representative tasks.[2][11] The repo's probes (`docs/probes.md`) are where that check belongs.

## 8. Decision rules

Each rule names the class, the action, the evidence and a confidence level.

1. **Keep operative rules, criteria, output fields, stop conditions and scope boundaries in SKILL.md**, near the top of their section, stated once. These are the parts that change behaviour and resist compression. *Evidence:* [11][13][19][27][29]. **High.**
2. **Keep a rationale only if it is about one clause long, attached to its rule, and tells the model what the rule protects, so it can handle cases the rule does not cover.** Example (dia-iterate): "your own re-derivation does not count as one, because a loop that feeds on its own judgment amplifies its own errors." *Evidence:* [1][7][12][17][18]; no direct measurement. **Medium.**
3. **Cut rationales that defend the design to a human reader, repeat something the model already knows, or restate a rule in other words.** Move the defence to `references/theory.md` if it is worth keeping. *Evidence:* [2][6][10][11]. **High** for repeats and common knowledge; **medium** for design defences.
4. **Turn a bare ALWAYS/NEVER into a plain rule plus its reason. Keep absolute wording only for true invariants.** *Evidence:* [1][7][11]. **Medium-high.**
5. **Keep a bare name or term of art when it points the model at a method it knows and the skill follows that method** ("Paul's six question types", "elenchus"). Cost: a few tokens. *Evidence:* [26] by analogy; [unverified] for instructions. **Low-medium.**
6. **Move full citations (Stephanus numbers, arXiv ids, author-year, "X found that…") out of SKILL.md into references.** No source shows they improve adherence; authority cues are shown to sway judgment;[23][24][25] vendors exclude material available from authoritative sources and tutorials.[6][13] **Medium-high.** Exception: keep a citation only if the model has to quote or point the user to it during the run.
7. **Move method history, lineage and comparisons with the original author ("Socrates also exhorted…", "stricter than Socrates, who…") to references, but keep the operative clause they carry** (e.g. "you never advise"; "the user writes the revision"). *Evidence:* [2] time-sensitive/old patterns, [6][13] no tutorials or changelogs, [11] keep constraints. **Medium-high.**
8. **Keep honest-label notes in SKILL.md only where they bound behaviour or routing** (e.g. "does not reconstruct implied norms"; "for the strict method, use dia-elenchus"; evidence classes the output must carry). Move the scholarly qualification behind them to references. *Evidence:* [11] evidence/permission constraints, [14][12] routing and scope. **Medium.**
9. **Remove contradictions and near-duplicates before cutting anything else**, since these hurt GPT-5-class models more than missing detail. *Evidence:* [9][11]. **High.**
10. **Do not compress rules into telegraphic text to save tokens.** Instruction text is the most compression-sensitive part of a prompt, and the dollar saving is about $0.002 per session. *Evidence:* [19][35][36]. **Medium-high.**
11. **Spend the trimming effort on descriptions first, then on SKILL.md bodies, then on references.** Descriptions are paid in every conversation and are truncated on Codex. *Evidence:* [3][12][14], `docs/token-cost.md`. **High.**
12. **Every reference link must say when to read it**, and anything needed on a typical first turn stays in SKILL.md, because unread references are free but missed ones break behaviour. *Evidence:* [2][3][13]. **High.**
13. **Validate each class removal with the probes before shipping** (remove one class, rerun, compare). The vendors prescribe this, and prompt effects are contingent. *Evidence:* [2][11][34]. **High.**

## Sources

- [1] https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices — Anthropic: Prompting best practices
- [2] https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices — Anthropic: Skill authoring best practices
- [3] https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview — Anthropic: Agent Skills overview
- [4] https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills — Anthropic Engineering: Equipping agents for the real world with Agent Skills
- [5] https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents — Anthropic Engineering: Effective context engineering for AI agents
- [6] https://code.claude.com/docs/en/best-practices — Claude Code Docs: Best practices
- [7] https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md — anthropics/skills: skill-creator SKILL.md
- [8] https://www.anthropic.com/constitution — Anthropic: Claude's Constitution
- [9] https://developers.openai.com/cookbook/examples/gpt-5/gpt-5_prompting_guide — OpenAI: GPT-5 prompting guide
- [10] https://github.com/openai/openai-cookbook/blob/a46b4185/examples/gpt-5-codex_prompting_guide.ipynb — OpenAI: GPT-5-Codex prompting guide
- [11] https://developers.openai.com/api/docs/guides/prompt-guidance-gpt-5p6.md — OpenAI: Prompt guidance for GPT-5.6
- [12] https://developers.openai.com/blog/rethinking-skills-and-prompts-for-gpt-6-astra — OpenAI: Rethinking skills and prompts for GPT-6 Astra
- [13] https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/skill-creator/SKILL.md — openai/codex: skill-creator SKILL.md
- [14] https://developers.openai.com/codex/skills — OpenAI: Codex skills
- [15] https://arxiv.org/abs/2204.02329 — Lampinen et al. 2022: Can language models learn from explanations in context?
- [16] https://arxiv.org/abs/2109.01247 — Webson & Pavlick 2022: Do prompt-based models really understand their prompts?
- [17] https://arxiv.org/abs/2310.13798 — Kundu et al. 2023: Specific versus general principles for Constitutional AI
- [18] https://arxiv.org/abs/2412.16339 — Guan et al. 2024: Deliberative Alignment
- [19] https://arxiv.org/abs/2310.05736 — Jiang et al. 2023: LLMLingua
- [20] https://arxiv.org/abs/2505.00019 — Zhang et al. 2025: An empirical study on prompt compression
- [21] https://arxiv.org/abs/2311.10054 — Zheng et al. 2024: Personas in system prompts do not improve performance
- [22] https://arxiv.org/abs/2512.05858 — Prompting Science Report 4: Expert personas don't improve factual accuracy
- [23] https://arxiv.org/abs/2410.02736 — Ye et al. 2025: Justice or Prejudice? Biases in LLM-as-a-Judge
- [24] https://aclanthology.org/2026.gem-main.75.pdf — Who Endorsed It? Authority bias across expertise levels (GEM 2026)
- [25] https://arxiv.org/html/2408.11865 — Anagnostidis & Bulian 2024: How susceptible are LLMs to influence in prompts?
- [26] https://arxiv.org/abs/2305.13252 — Weller et al. 2024: According to... prompting
- [27] https://arxiv.org/html/2507.11538 — Jaroslawicz et al. 2025: How many instructions can LLMs follow at once? (IFScale)
- [28] https://aclanthology.org/2025.findings-emnlp.896 — Harada et al. 2025: When instructions multiply (ManyIFEval)
- [29] https://arxiv.org/abs/2307.03172 — Liu et al. 2024: Lost in the Middle
- [30] https://arxiv.org/abs/2402.14848 — Levy et al. 2024: Same Task, More Tokens
- [31] https://research.trychroma.com/context-rot — Hong et al. 2025 (Chroma): Context Rot
- [32] https://doi.org/10.18653/v1/2025.findings-acl.646 — Order Matters: position bias in multi-constraint instruction following (ACL Findings 2025)
- [33] https://doi.org/10.48550/arxiv.2607.19257 — Eliav 2026: Prompt design at scale (VeyraBench)
- [34] https://arxiv.org/abs/2503.04818 — Meincke et al. 2025: Prompting Science Report 1
- [35] https://platform.claude.com/docs/en/about-claude/pricing — Anthropic: Pricing
- [36] https://code.claude.com/docs/en/prompt-caching — Claude Code Docs: How Claude Code uses prompt caching
- [37] https://code.claude.com/docs/en/costs — Claude Code Docs: Manage costs effectively
- [38] https://arxiv.org/abs/2605.01771 — 2026 preprint: The Compliance Gap
