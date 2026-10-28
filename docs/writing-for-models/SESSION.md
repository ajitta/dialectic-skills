# Session record, 2026-10-28

How the writing-for-models draft became `skills/dia-instruct/` and why it reads the way
it does, so a later session can continue without the chat. Sections 1–8 describe the
skill while it was still called writing-for-models; section 9 covers the move into
`dia`. The session ran in Korean; the owner's words are
translated. Where a ruling settled a question, it is marked **Ruling**.

## 1. Starting point

The owner attached a draft `SKILL.md` and `evidence.md` and asked for them to be verified,
cleaned of references that mean nothing outside their origin, and made into a skill,
analysis first. The draft came from the owner's private repository: its rules were
measured there in an unpublished study ("the source" in `evidence.md`). The private
repository was opened only to check the figures; nothing from it is in this folder.

The first pass, with an independent checker sub-agent comparing draft and rewrite:

- Removed references to that repository's scripts, artifacts, file names and runs.
- Recomputed every Fisher p-value in `evidence.md` (two-sided Fisher exact). All matched.
  Permutation p-values are reported as the source gives them.
- Corrected one overstatement. The draft said short commands generally lose conditions.
  The measured result is narrower: the arm that moved a condition to another step
  failed, while numbered short sentences that kept each condition in its step passed
  8/8. Rule 1 now names the failure as a condition separated from what it gates, and the
  general claim is recorded as the author's unpublished observation.

## 2. Scope and audience

- **Ruling:** the skill is for a Claude Code plugin that is also used on claude.ai, where
  sub-agents are available.
- **Ruling:** `evidence.md` must not load when the skill runs. SKILL.md keeps one pointer
  line saying it holds what each rule rests on, for when the user asks how strong a rule
  is or wants to change one. The owner later asked whether a model ever needs to open it.
  The answer was only in those two cases, and the owner accepted that the pointer need
  not say "stays unopened unless…".
- **Ruling:** it will be given to others, and the owner's repository is private, so all
  of that content goes. That covers repository names, commit hashes, internal paths,
  plugin versions, quotes from internal files, the measurement date, and a reference to
  a recorded cleanup. `evidence.md` calls the study the author's unpublished work, with
  builds B1–B3 and model aliases only.
- **Ruling:** the purpose of the skill is to get the most reasoning out of a model
  through how instruction text is written. It is not about skill format or packaging.
  So `disable-model-invocation`, description triggering, and a "Checking files" section
  about files around the skill were removed. The owner raised `disable-model-invocation` as the
  case in point and invited a counter-argument; none changed the outcome, and the
  owner's go removed it.
- **Ruling:** per-item strength labels ("unmeasured practice"), p-values and source names
  do not belong in SKILL.md. The owner objected that "unmeasured" was wrong for practices
  tested heavily in their repository, and that such statements have no reason to sit in
  the skill. They moved to the "Strength of each part of SKILL.md" table in
  `evidence.md`.

## 3. Credit

- Matt Pocock's recent writing-for-agents skill was first mentioned as related.
  **Ruling:** remove the mention from the skill. A credit line was then agreed for
  `evidence.md`.
- The owner pointed out that many ideas attributed to Pocock were the owner's own. The
  line now says his skill is related and makes similar points (pointers, co-location,
  splitting at a context boundary, completion criteria, leading words), not that ideas
  were adapted from it.

## 4. Form of the rules

The owner explained the intent, and the text was rebuilt around it:

- A paragraph is one line, long and self-contained: one expression that defines the
  result, with its condition, limit and fallback inside it. Declarative, expression-like
  sentences beat bare imperative statements. The owner's example contrasted "lower the
  air-conditioner setting on hot days" (a statement) with a sentence that defines the
  target state with its condition and fallback.
- **Ruling:** about 300 characters is an experimental working value, not a fixed figure
  and not a limit. It may differ by model and effort; longer is fine, since low models
  and low effort will not be used. SKILL.md says "a few hundred characters is a working
  value, not a limit".
- **Ruling:** connect the rules to programming languages, functional ones in particular.
  The result:
  - a paragraph as a total function (the fallback is the default branch);
  - a split rule as an `if` without braces;
  - a scope word as a type signature, and an exact path as a concrete type;
  - a second name as an alias;
  - a context boundary as a separate function that receives only its arguments;
  - a pretrained leading word as a standard-library call, and a coined word as a
    user-defined function.

  `evidence.md` labels this framing as the author's explanatory model, not a measured
  mechanism.
- What counts as a Rule 1 breach was pinned down: a condition, limit or fallback on
  another line, bullet or step from what it gates, or one paragraph joining unrelated
  rules. Never a sentence or paragraph merely for being long. Moving this definition to
  the opening once narrowed it and broke the Structure item on keeping a concept in one
  place, so it went back into Rule 1.

## 5. Examples

- **Ruling:** remove the single examples from Rules 1 and 2. The owner's concern: a model
  follows an example, and current practice leaves the "how" to frontier models. The
  owner also noted that Anthropic's guidance already supports this: examples should be
  varied, and worked examples shape how the model approaches similar problems.
- Lead 6 now says: leave examples out of a rule whose method the model should work out;
  where one is needed, use several varied ones. The owner's own "one-way door" example,
  restored after it had been wrongly credited to Pocock, went with the others.

## 6. Questions that changed wording

- **Sub-agent prompts:** the owner asked whether the rules apply to instructions handed
  to a sub-agent. Yes. The Structure item on context boundaries says a prompt handed
  across is the receiver's whole context. Under "By kind of text", every instruction you
  write for a model is subject to all four Rules.
- **Session context passed as input:** the owner asked whether material such as session
  context, handed to a sub-agent as input, should be rewritten. No. "By kind of text"
  says input material is passed unchanged and marked as data, and the Rules apply to the
  instructions around it.
- **"Writing, editing or reviewing a file"** read as if the work must be a file. It is
  now "…text": the review step covers kept text, while single-use text such as a
  sub-agent prompt is self-checked and called not independent.
- **Description:** now "…against four rules and the structure they imply", on the
  owner's go.

## 7. Reviews of the skill

- Independent checker sub-agents reviewed the rewrite three times while it took shape.
  Each got the files and the owner's requirements but not the author's reasons.
- The owner asked for an independent agent to run `dia-refine` on both files. It
  applied confirmed fixes. One change was reverted: it added a run count taken from a
  private commit, and the line went back to the p-value alone.
- The owner asked what happens when the skill is applied to its own SKILL.md. A checker
  reviewed old against new under the skill's own rules. **Ruling:** apply the findings
  it rated by severity; they are in the current text.

## 8. Trial on dia-adjudicate

The owner asked to try the skill on `dia-adjudicate` (branch `adjudicate-ratchet`), then
for an independent comparison of the skill applied and not applied. The setup and raw
data are in `ab-dia-adjudicate/`; results and their reading are in `README.md`.

- B was written by the skill's rules: reasons moved into the rules they explain, the
  overturn conditions brought into one rule, and one name per thing. An independent
  meaning check of B against A found three meaning changes, which were reverted before
  any run.
- The owner's choices (asked in the session): Opus first, sources as local files, and a
  2-run screen before deciding further. On seeing the cost, time and difference: rerun
  on Haiku. Then the harder design, with a summarizing fetch tool and summary traps.
  **Ruling:** that design was proposed at 6 runs per cell; the owner set 3.
- After three rounds (28 runs) no difference was found. The next step under the skill's
  A/B rule, and the alternative, are open item 2 in `README.md`.

## 9. Into dia

**Ruling:** everything for this work goes in one folder named after the branch,
`docs/writing-for-models/`, because files added straight to `docs/` would mix with
other branches. The first push put the folder at the repository root by mistake; it was
moved under `docs/` afterwards. Then the owner decided to put the skill into `dia` and
to apply B on this branch, merging later, separately.

- `adjudicate-ratchet`, the only branch that has `dia-adjudicate`, was merged into this
  branch (commit `e68bf61`). A rebase was tried first, but publishing it needed a force
  push, which was refused; the merge gives the same files and keeps the pushed history.
- **Ruling:** the name is `dia-instruct`; dia-write and dia-prompt were the other
  options. Every `dia` name needs the `dia-` prefix (spec §4), and `ins` is a prefix of
  no other name.
- **Ruling:** it loads on natural-language requests, like dia-refine, rather than by
  name only. dia-menu 1.2.0 lists it as row 12 and may choose it for a request to write
  or review text a model follows.
- **Ruling:** the related-work line on Matt Pocock's skill is removed, because AGENTS.md
  allows no references to other projects in skill text. The credit stays in section 3.
- Added under spec D26: one sentence that the text under review is material, not
  instructions. A reviewed instruction file would otherwise be in a position to steer
  its own review. This is a meaning change that a repository rule requires, which the
  skill's own step 1 allows.
- The description follows spec §7.2: label, what it does, "Use when …", one "Not for"
  sentence toward dia-refine and dia-adjudicate. `evidence.md` now calls them the
  dia-instruct rules too (Rule 4).
- B replaced `skills/dia-adjudicate/SKILL.md` unchanged apart from `metadata.version`
  1.1.0. The plugin is 1.6.0. Spec D41 records all of this.
- A sub-agent that had not written these changes reviewed dia-instruct and dia-menu
  against dia-instruct, AGENTS.md and spec §7.2, with the old texts. The confirmed
  findings caused by this pass were fixed:
  - The material sentence now says the host's own session rules (a repository's
    AGENTS.md) still bind while that file is edited (Rule 2).
  - The description drops the rule list (§7.2: only what separates it from siblings)
    and says "a draft written for people" and "reports", as dia-adjudicate does
    (Rule 4).
  - In the menu, a request to draft a toast or email no longer reads as going to
    dia-refine; reports about a prompt go to the dia-adjudicate form; "agent file"
    became "AGENTS.md"; and `instruct me how …` joined the sentence-word examples.
  The fixes were self-checked, not reviewed again. Findings on text that predates this
  pass were left for the owner (`README.md`, open item 5).

## 10. Not kept

- The owner's original attachments, because they contain private-repository content.
- Intermediate drafts of the skill, including the version before self-application.
- Full judge replies and traces: only each run's JSON verdict block, usage and fetch
  log were saved.
