# dia-techne: design session record

Record of one design session (2026-10-31 to 2026-11-01) that started from the owner's proposal for a prompt-rewriting skill, went through five drafts and three small pilots, and ended with `skills/dia-techne/` on branch `techne`. §1 to §10 describe the branch's first commit; §11 records the review of 2026-11-01, the fixes and the integration into plugin 1.13.0 (not merged or released).

Everything below was run by one assistant session (Claude Opus 5.5 in the Claude app, with web search, web fetch, a shell and sub-agents). Pilot executors and graders were sub-agents on the session model. Arms by run-folder letter: pilots 1 and 2, A = skill draft, B = no skill; pilot 3, A = 0.5.0, B = no skill, C = 0.4.1 (keys in each pilot's `*key.json` map blinded X/Y/Z to these letters). The graders' verdicts and rankings and the run times were not committed; they rest on this record. Web pages reached agents through a fetch tool that returns a model's summary of the page, not the raw page. Every pilot cell is n=1. Numbers are counts from these runs, not rates.

## 1. Status of this branch

The owner chose to add the skill and this record only (2026-11-01). The branch therefore does **not** touch dia-menu, `plugin-manifest.json`, the README files, `docs/spec.md`, `AGENTS.md`, the plugin version or the generated output, and `python tools/package.py --check` fails on purpose with `skill set [...] != spec §4 [...]`.

In a scratch copy with dia-techne added to spec §4 and to `EXPECTED_IMPLICIT` in `tools/package.py`, the only remaining errors were the integration ones (plugin version not bumped; `plugins/dia/` and both zips lag the source). The skill's own checks passed: allowed frontmatter keys, `name` matches the folder, description 493 characters, body 36 lines as `tools/package.py` counts them at the first commit (39 after the review fixes), no Hangul, every `dia-*` name it mentions exists, `agents/openai.yaml` in the §7.3 shape.

`python -m unittest discover -s tests` at the first commit: 6 of 19 tests fail with PyYAML installed (`test_skills_match_expected_table`, `test_implicit_invocation_table`, `test_validation_passes`, `test_committed_output_is_current`, `test_openai_zip_layout`, and an error in `test_frontmatter_and_openai_yaml_parse`, a `KeyError: 'dia-techne'` on `EXPECTED_IMPLICIT`), all from the same missing integration; without PyYAML, 5 fail and the YAML test is skipped; without the new files all 19 pass.

Merging and integration are left for a later instruction from the owner; §9 lists what integration needs.

## 2. Starting point

The owner proposed a separate skill, `dia-reprompt` ("expert-guided prompt reconstruction"), distinct from dia-intent: dia-intent asks what the user actually wants; the new skill asks how a top expert would redesign the request. Four internal questions (how would a top expert define the problem, which raw material would they start from, which methods and tools would they use, how would they verify the result) feed a rewritten prompt, returned with key changes and unresolved points and not run automatically.

First review in the session, checked against the installed SKILL.md files:

- Separation from dia-intent is sound: dia-intent may not draft the deliverable before approval, so a rewrite inside it would change its contract. But dia-intent item 1 already sets observable completion criteria, so the borders are better drawn as "what counts as done" (dia-intent) and "how it is checked during execution" (the new skill).
- The nearest sibling is dia-instruct, not dia-intent: its description covers agent and sub-agent prompts, and dia-menu routes such requests to it. dia-instruct governs form; the new skill governs content (problem, sources, method, checks).
- The "top expert" wrapper was criticised as a persona. Evidence found: personas in system prompts did not improve accuracy over no persona across 162 roles and 2,410 factual questions in four model families (arXiv:2311.10054); expert personas helped in some specialised domains at a cost elsewhere (arXiv:2407.02099, in the paper's body; its abstract reports only greater variability); role prompting shifted depth against clarity rather than raising capability (arXiv:2605.29420); one paper (Mullens and Shen, arXiv:2603.20225) argues that the Wharton Generative AI Lab's null result was a design artefact, a baseline near ceiling among five flaws. All are about a role given to the answering model, so they bear only indirectly on a design heuristic.

The owner later corrected the reading of "top expert": the intent was never a persona but a procedure for finding the execution method a top practitioner would use, and then applying it (§4).

## 3. Source: Felix Rieseberg's tutorial

The owner named the idea's origin: Felix Rieseberg, "How to be more ambitious: A tutorial for humans with models", felixrieseberg.com, 13 October 2026 (read in this session through a summarising fetch tool; the review of 2026-11-01 fetched the page in full and compared it point by point, §11). Rieseberg works at Anthropic, where, in his own words, he has led engineering for Claude.ai, Cowork and Code Desktop; he was first recalled in the session as a Codex developer, which was wrong.

What the tutorial says, in short:

- Four kinds of ambition. **Speed** (skipped as well known). **Altitude**: consider the outcome rather than the task. **Depth**: work as a field's top expert would, with their tools and raw data, until experts might learn from the result. **Range**: bring in other fields; turn nouns into verbs (a quarterly review as "getting busy people to believe a story about cause and effect, and to decide under uncertainty, in 30 minutes") and assemble a crew including opposing roles.
- A depth prompt asking for "a deeper version of this task, not a bigger one": what a top professional would do that the user is not asking for; the rawest material; the methods and tools; what, other than the model or the user, would show the result is right. The model then rewrites the user's prompt to ask for those things.
- Do not let the model grade its own work; insist on outside validation, ideally a tool the model can run.
- Skip role-play: a persona changes vocabulary, not method; use it only to find the relevant fields.
- Limits: altitude fits work with an end result better than creative work; ambition needs a computer, data and tools.

A secondary report of an interview (DEV Community, Oct 2026) adds his view that packaged skills have a short useful life and that deleting a stale skill can improve output, and advises "a separate adversarial session when you cannot" use hard outside evidence: that is the source of question 4's separate-agent option, which the tutorial does not have. Not checked against the interview itself.

The tutorial's depth section also lists "Pick unreasonable goals", "Challenge what you know" (ask the model "to adversarially check assumptions" against the raw data) and "Produce new knowledge". The skill takes none of them by name; "Challenge what you know" is the tutorial's closest basis for revising a request's stated conclusion.

What dia-techne takes from the tutorial: altitude (the outcome), depth (the first four of five questions), range (question 5), outside verification, deeper-not-bigger, no role-play, the creative-task limit. What it adds, not in the tutorial: question 4's separate-agent option (from the secondary report above), running the work in the same turn, revising the request's terms (§4, owner decision), and the safety and report rules from the pilots (stops, backups, source marks, report integrity).

## 4. Owner decisions

| Date | Decision |
|---|---|
| 2026-10-31 | A separate skill rather than part of dia-intent. Draft it (0.1.0). |
| 2026-10-31 | "reprompt" does not describe the skill; renamed **dia-techne** (Aristotle's technē, a reasoned state of making that knows the cause and not only the fact, NE VI.4 and Metaphysics I.1, used as a label only; the earlier gloss "the end, the material, the means and the standard" read outside verification into Aristotle). Chosen over dia-praxis and dia-method; `tec` is a prefix of no other name. |
| 2026-10-31 | No automatic invocation: by name, by first word, or picked in dia-menu by number or name; never chosen by dia-menu for a plain request. |
| 2026-10-31 | Run the work in the same turn with stops (option 1 of three): stop for a placeholder or a step that cannot be undone. |
| 2026-10-31 | After pilot 1, accept the four recommendations: a requested local overwrite proceeds after a backup while external irreversible steps still stop; steps that do not depend on a placeholder run; an unreachable primary source is replaced by a marked copy or secondary source; a short reply for simple tasks. Main experiment (12+ runs per arm) postponed. |
| 2026-11-01 | The skill exists to break the narrowness of the request: the outcome and the field's practice override the request's framing and stated conclusion. Never revised: the user's authority, the user's data, constraints stated as requirements or prohibitions. |
| 2026-11-01 | Compact the skill; no fixed English labels in replies. |
| 2026-11-01 | Shorter description for Codex's skill-list budget (0.4.1). |
| 2026-11-01 | Rebuild on Rieseberg's tutorial (0.5.0). |
| 2026-11-01 | Branch `techne` with the skill and this record only; `allow_implicit_invocation: true` as in spec §7.3 (D33) rather than `false`; description in the D37 explicit-only form, kept short. Merging and later steps on a separate instruction. |

On the last row: the session had first recommended `allow_implicit_invocation: false` from OpenAI's Build skills page, which says Codex then skips implicit invocation while `$skill` still works. Spec §7.3 records from probe P3 that `false` also hides the skill from the model-visible list, so a message starting with its name cannot reach it; the repository's convention (true, gated by wording) was kept.

## 5. Draft history

Every draft is in `dia-techne/drafts/`. Each was reviewed against dia-instruct's rules by a sub-agent that had not written it, given the file and dia-instruct's path but none of the author's reasons; findings counted only after their quote was found in the file. Rounds of high-only review were added when a fix changed meaning.

| Draft | Main change | Reason |
|---|---|---|
| 0.1.0 `dia-reprompt` | Rewrite only; fixed points (deliverable, constraints, authority) kept; four criteria; never runs | Owner's proposal minus the persona wrapper |
| 0.2.0 `dia-techne` | Established-practice search (with public-term web searches); runs in the same turn with stops; invocation by name only | Owner: the intent is finding the method, then applying it |
| 0.3.0 | Backup then overwrite for requested local changes; partial runs around placeholders; source tiers; short output when nothing needs review | Pilot 1 |
| 0.4.0 | Outcome governs; request terms (framing, method, stated conclusion, form) are hypotheses; checks against report drift and selective reporting; no English labels; a third shorter | Owner; pilot 2 root causes (§6.2) |
| 0.4.1 | Description cut from 895 to 144 characters; Codex `agents/openai.yaml` with `allow_implicit_invocation: false` | Codex skill-list budget: 2% of the context window (8,000 characters when the window is unknown), descriptions shortened first, then skills omitted (learn.chatgpt.com, Build skills) |
| 0.5.0 | Five questions after Rieseberg (practitioner's extra step, rawest material, methods and tools, outside check, another field or opposing view); deeper not bigger; creative-task limit; additions shown with reason and mark | Rieseberg's tutorial; the 0.4 compaction had weakened outside verification and had no range |
| 1.0.0 (this branch) | Tool use made conditional and a no-tool path for the outside check (spec §7.1); invocation names as the siblings write them; D37 description (493 characters); `allow_implicit_invocation: true` | Repository rules |

Review findings that changed the text, by kind: a fallback sitting apart from what it gates (dia-instruct Rule 1); one thing with two names ("framing" for one term and for all of them; "basis" and "tier" scales); description contradicting the body on when to stop; a same-pass review counted as an outside check; additions from the questions not shown with a reason; reply-language rule swallowing the rewritten prompt; "marks as required" readable two ways (fixed by listing must, only, never, do not and stated limits).

## 6. Pilots

Each pilot ran every task once per arm, each arm a fresh sub-agent. Skill arms were told to read the frozen skill file and follow it as if the user's message started with `dia-techne`; the no-skill arm got the bare message. No user was available, so a stop ended the run. Each agent worked in its own folder. Graders were separate sub-agents; quality graders saw only label-blinded deliverables (keys in each pilot's `*key.json`), and the session checked every quote they relied on against the files before using a finding. Skill replies show their structure, so blinding was partial (pilots 2 and 3 note where results were cut to the deliverable).

### 6.1 Pilot 1: draft 0.2.0 against no skill (`dia-techne/pilot1/`)

Tasks: T1 legal summary (pseudonymised data under Korea's Personal Information Protection Act), T2 a calculation with the target missing, T3 fix and overwrite a notice file, T4 a translation.

- Stop behaviour as designed in all four. T2: the skill arm wrote the targets as a placeholder and stopped; the no-skill arm also declined to compute but gave the quarterly totals. T3: the skill arm made a backup, a revised copy and a diff, then stopped before overwriting (original file hash unchanged); the no-skill arm overwrote.
- Blind quality: T1 skill slightly better (verification status, two penalties the other missed; the other had more verified specifics and one unsupported claim); T3 tie; T4 essentially tie.
- Cost: T4 26 s against 5 s, T3 61 s against 13 s; replies several times longer.
- Compliance graders found labelled assumptions missing from the open points and basis labels misapplied.

### 6.2 Pilot 2: draft 0.3.0 against no skill (`dia-techne/pilot2/`)

Tasks chosen so that a wrong method gives a wrong conclusion; references computed in `p2_ref.py`. Q1 A/B test (p ≈ 0.13), Q2 admissions with Simpson's paradox, Q3 seasonal sales forecast (expected value 112), Q4 survey nonresponse.

- No method failure in either arm.
- Blind quality: Q1 tie; Q2, Q3, Q4 skill arm better (stratified test with MH odds ratio 1.42 and CMH p = 0.022; back-test MAPE 2.7%; conditional "most respondents" claim). Q2 and Q4 skill replies were cut to the result for grading, which favours them on length.
- The no-skill Q3 reply said January 2024 was missing from the data; it was not.
- Cost: Q1 75 s against 46 s, Q2 113 s against 40 s, Q3 192 s against 36 s, Q4 119 s against 53 s.
- Root cause of two Q3 defects in the skill arm, from its files and timestamps: the stated range 105–120 is exactly ±7% around 112.5, the first method's estimate, while the reported estimate was later averaged to 111 (±7% gives 103–119); and the Fourier script printed K = 1 to 6 forty seconds before the reply, K = 5 being best by its own AICc and back-test (113.9, MAPE 3.0%), yet the reply reported only K = 1 to 3 as unfit. It also averaged in an unvalidated method and dropped Holt-Winters for looking low. Common cause: the answer chosen first, alternatives summarised to fit it, and final numbers written after the last computation. Fix in 0.4.0: fix the comparison criterion first and apply it to every alternative, compute reply numbers from final values, check the reply against tool output.
- Q2 also showed the skill revising the user's stated conclusion ("discrimination") to what the data support; under 0.3.0 that broke the fixed-points rule, which led to the owner's decision of 2026-11-01.

### 6.3 Pilot 3: draft 0.5.0 against 0.4.1 against no skill (`dia-techne/pilot3/`)

Tasks where an outside check or another field should matter. R1 a buggy `business_days_between` (weekend holidays and duplicate holidays subtracted), graded by a hidden test of 3,000 random cases against a day-by-day oracle (`p3_hidden_test.py`); R2 a launch email given past rates of 9% open and 0.8% click; R3 whether a 12% D30 retention may be called higher than the industry average.

| Task | 0.5.0 | 0.4.1 | No skill |
|---|---|---|---|
| R1 hidden test | pass | pass | pass |
| R2 blind rank | 1st | 2nd | 3rd |
| R3 blind rank | 1st | 2nd | 3rd |
| Time R1 / R2 / R3 | 236 / 269 / 171 s | 136 / 224 / 138 s | 62 / 69 / 81 s |

- R1: all fixed both bugs; 0.5.0 and 0.4.1 both left re-runnable checks against NumPy's `busday_count` and a day-by-day count (0.5.0's is a pytest file that fails on the original and passes on the fix); the no-skill arm checked 20,000 cases but kept no file.
- R2: all three diagnosed opening as the bottleneck (click-to-open about 8.9%). Only 0.5.0 compared against a benchmark it read (MailerLite 2025); 0.5.0 and 0.4.1 both set feature activation, not opens, as the success measure. The no-skill reply had one unbracketed feature claim and an unsourced legal statement. 0.5.0 and the no-skill arm both gave the minimum detectable open-rate difference for 2,000 per arm as 2.5 points; the grader's recomputation gives 2.7.
- R3: 0.5.0 gated any ranking claim on the metric definition; every figure the grader could check matched its source. The no-skill reply called the "puzzle D30 5.35%" figure an upper-quartile number misquoted as recent; the source page the grader could read (Mistplay, citing AppsFlyer Q3 2022) presents it as a genre average. AppsFlyer's original was not reachable.
- The separate-agent form of the outside check never ran: all three 0.5.0 runs reported that they could not start another agent, and used tests and source comparison instead.

### 6.4 What the pilots do and do not show

- The no-skill model avoided every planted method trap; the skill's gains were in depth of checking and factual accuracy, consistent with Rieseberg's emphasis on outside verification.
- Cost is roughly two to four times the time and two to three times the reply length.
- n=1 per cell, same-model graders, partial blinding, sub-agents that may not carry the owner's preferences. These are directions, not effects. dia-instruct step 1 asks for 12 or more runs per arm before a meaning change counts as measured; that experiment was postponed by the owner.

## 7. Adaptation for this repository (1.0.0)

Changes from draft 0.5.0, all required by repository rules:

- Spec §7.1: searches are conditional ("if a search tool is available"); the outside check runs "when the tools it needs are available" and, on a surface with no tools, is named for the user to run.
- Invocation names written as the siblings write them (`/dia:dia-techne`, `$dia:dia-techne`, `$dia-techne`, `@dia-techne`).
- Description in the D37 explicit-only form: what it does, "Use only when …", the gate negation, one "Not for …" sentence naming dia-instruct, dia-intent and dia-refine. 493 characters, against 166 in 0.5.0, to keep the borders.
- `agents/openai.yaml` in the §7.3 shape with `allow_implicit_invocation: true` (D33).
- `metadata.version` 1.0.0, with the drafts named in `lineage`; dia-adjudicate also started at 1.0.0 (D40), its lineage naming its research record.

## 8. Things worth knowing before integration

- The skill can override the user's stated conclusion. That is the owner's intent (§4); the tutorial itself is written for humans raising their own requests and does not say a model should override one; its closest basis is "Challenge what you know" (§3).
- The skill is about 1,650 words after the review fixes (about 1,500 in the body). Rieseberg's depth prompt is about a hundred words, and his remark on skills debt argues for keeping it thin.
- Codex budget: with all fourteen descriptions, Codex CLI 0.166.0 showed every description uncut (review of 2026-11-01, §11).
- The pilots ran in a session where sub-agents could not start further agents, so the separate-agent outside check is untested.

## 9. Open items for integration

- dia-menu: row 13, explicit-only like rows 1, 10 and 11 (never chosen for a plain request); number range 1–13; a border line between dia-techne and dia-instruct.
- `docs/spec.md`: a decision row, §4 names table, §5 section, §7.3 table row, G1 count; `tools/package.py` `EXPECTED_IMPLICIT`.
- `plugin-manifest.json` description ("Thirteen …") and version 1.13.0; `AGENTS.md` count; README and its three translations; `packaging/` listing fields; regenerate with `tools/package.py`.
- Probes: P1/P2 listing and natural-language cells; P6 first-word cells (`dia-techne …` runs, a mid-sentence mention does not); P7 negative cells against dia-instruct, dia-intent and dia-refine; P8 tool-less run (outside check named, not faked); dia-menu cells `dia 13` and `dia tec`.
- A/B at 12 or more runs per arm, if the owner wants the effect measured.

## 10. Files

- `drafts/0.1.0.md` … `drafts/0.5.0.md`: every draft as reviewed (0.1.0 reconstructed from the text shown to the owner; the others are the files the pilots used, where they used one).
- `pilot1/`: tasks, the notice file, replies, blinded deliverables, key, and the T3 files showing the original kept and overwritten.
- `pilot2/`: tasks, reference, scripts, every run folder with the reply and the agent's own scripts and outputs, blinded deliverables, key.
- `pilot3/`: tasks, reference, the buggy file, the hidden test, every run folder, blinded deliverables, the grader's scratch scripts, key.
- `pilot2/grading/` and `pilot3/grading/`: the graders' recomputations (`pilot3/grading/mdd.py` is the only evidence for the 2.7-point figure).
- The backup copies (`notice.orig-backup.md`, `bizdays.py.bak`) are byte-identical to the originals: they show the backup behaviour. The blinding scripts hard-code the session's paths and do not run from this repository.

Paths inside the replies point to the session's working directory (`/home/claude/exp/…`), not to this repository.

## 11. Review of 2026-11-01 and integration

An independent review of the first commit (fresh sub-agents that had not written the skill; the probe and listing files are kept outside this repository) found, and the owner accepted as recommended:

- **Sources.** The tutorial was fetched in full and compared with §3 point by point; the corrections are in §2, §3, §5 and the Sources list (role wording, the Codex budget sentence, the "story about cause and effect" quote, the techniques §3 left out, the separate-agent option's source). Pilot numbers reproduced from the committed files: pilot 2 Q1 p = 0.126, Q2 MH odds ratio 1.42 and CMH p = 0.0215, Q3 expected value 112 and the Fourier output (K = 5, 113.9, MAPE 3.02%); pilot 3's hidden test fails the original on 1,041 of 3,000 cases and passes all three fixes; R2's minimum detectable difference is 2.54 points by the replies' formula and 2.70 by the grader's.
- **Skill text.** Running stops before any step the assistant could not reverse itself from what it holds, and always before sending, publishing, pushing, spending, changing a database it holds no copy of, installing outside the project, rewriting version-control history or deleting data held elsewhere; backups get a name no existing file has and their path is reported; when the user's own words say content must not survive, it is deleted without a copy; an unstated outcome is a point only the user can settle; nothing private leaves the session except opening a path or URL the user gave; an explicit invocation for a case the description sends to a sibling runs, keeps any limit on running and names the sibling; for another executor the material is still read. Where the method and the name come from moved to `references/theory.md`, read only when the user asks (owner: not in the body). A second independent review of these fixes (PASS WITH FIXES) led to the wording above; its fixes were applied and checked by the author, not independently.
- **Smoke probes** (Claude Code 2.1.314, n = 2 to 16 per cell, not a measurement): explicit-only gating held (requests that only sound like the skill loaded it 0/6, and 0/9 on two description variants); a short Korean code-fix request starting with `dia-techne` loaded it 2/16 on Sonnet and 0/4 on Haiku, against 4/4 in English, 4/4 on Opus, 4/4 for a Korean non-code request, 4/4 with `dia-techne:` and 8/8 (Sonnet) and 4/4 (Haiku) for the same skill renamed `dia-deepen`; three description rewordings gave 0/8 each; dia-intent on the same prompt loaded 1/4. With the fixes: an existing backup was kept and a new name used (2/2), a requested push stopped (2/2), a secret was deleted without a copy (2/2, by slash invocation), another executor's prompt was written after reading the file (2/2); a requested local SQLite change stopped once and ran after a backup once (before the database wording above).
- **Codex.** On a scratch integration copy, Codex CLI 0.166.0 listed all fourteen dia descriptions uncut.
- **Integration.** Plugin 1.13.0 (spec D55): dia-menu row 13 (explicit-only), spec tables, manifest, listings and the four READMEs with an example from a recorded run. Not done: the project page, the routing probe set of §9 beyond the smoke cells, and the A/B the owner postponed.


## 12. Revision of 2026-11-07 (plugin 2.7.0, dia-techne 2.3.0)

A comparison with a third-party skill built on the same tutorial (robonuggets/be-ambitious) and with no skill (probes Part AD, round 1) showed the cost side of four rules: a `.bak` copy beside a clean tracked file, a stop before a push the user asked for when nothing had been revised, a separate critic agent for a short poem, and a full reply whose result came after the meta sections. The owner accepted all four changes as recommended (spec D63). The same comparison supports a choice made in §3: the skill does not take "Pick unreasonable goals". On a request to raise conversion tenfold in a quarter with no data, the arm that treated the user's target as reasonable kept it unexamined and stated a wrong sample size, while dia-techne named the conflict with the benchmarks it found.

## Sources

- Felix Rieseberg, [How to be more ambitious: A tutorial for humans with models](https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/), 2026-10-13 (read through a summarising fetch).
- Yao Xiao, [Stop Telling Claude to Act Like an Expert](https://dev.to/blobxiaoyao/stop-telling-claude-to-act-like-an-expert-felix-rieseberg-on-costume-prompts-and-skills-debt-2pha), DEV Community, 2026-10-26 (secondary report of an interview).
- Zheng et al., [When "A Helpful Assistant" Is Not Really Helpful](https://arxiv.org/abs/2311.10054), Findings of EMNLP 2024.
- [Helpful assistant or fruitful facilitator?](https://arxiv.org/abs/2407.02099), arXiv:2407.02099.
- [When Does Persona Prompting Actually Help?](https://arxiv.org/abs/2605.29420), arXiv:2605.29420.
- Mullens and Shen, [The Arrival of AGI? When Expert Personas Exceed Expert Benchmarks](https://arxiv.org/abs/2603.20225), arXiv:2603.20225.
- OpenAI, [Build skills](https://learn.chatgpt.com/docs/build-skills) (skill-list budget, `allow_implicit_invocation`).
