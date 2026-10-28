# dialectic-skills — Specification

| | |
|---|---|
| Status | Approved by the owner on 2026-10-20; pre-release 0.1.0, accepted (§12.3) and released as 1.0.0 on 2026-10-20; 1.1.0 renames dia-intent to dia-confirm (D30), and 1.6.0 renames it back (D42). 1.5.0 (D39, D40) was built on a branch and never released; its changes ship in 1.6.0 (owner, 2026-10-28). 1.7.0 extends dia-intent's goal step (D45); 1.8.0 adds its outcome hypothesis (D46), resolves the D43 rewrite's open proposals (D47) and closes the dia-adjudicate re-test (D48); 1.9.0 settles the decisions 1.8.0 left (D49). Probe results: `docs/probes.md` |
| Date | 2026-10-20 |
| Owner | ajitta |
| Repository | `ajitta/dialectic-skills` (public since 2026-10-20) |
| Scope of this document | What to build and how to verify it. Building it is a separate step. |

## 1. Summary

`dialectic-skills` packages twelve reasoning-and-review skills as one plugin, installed under the plugin name `dia`. A menu skill, `dia-menu` (1.4.0, D38), is the short entry point to them. Seven are rebuilt from the owner's existing skills (socratic-brainstorm, socratic-elenchus, reductio, negative-dialectics, self-refine, recursive-refine, confirm-intent); three were added in 1.3.0 from the candidate research (D35), dia-adjudicate in 1.5.0 (D40) and dia-instruct in 1.6.0 (D41). The target surfaces are:

- Claude Code
- Codex
- Claude desktop
- ChatGPT desktop
- The Claude and ChatGPT mobile apps

The shipped package contains instructions only: Markdown, YAML and JSON. It has no hooks, scripts, binaries or MCP servers, because nothing may depend on an execution harness at run time. Build and validation scripts exist only in the repository, for the developer.

## 2. Goals and non-goals

### Goals

- G1. One plugin, `dia`, containing the skills named in §4 (seven until 1.2.1, ten from 1.3.0, D35, plus dia-menu from 1.4.0, D38, eleven with dia-adjudicate from 1.5.0, D40, and twelve with dia-instruct from 1.6.0, D41).
- G2. The same skill files run unchanged on every target surface, and on a surface that has no tools at all (mobile chat).
- G3. Skill files are written in English. Hangul appears only under `references/ko/` (§6).
- G4. The repository starts by importing the material it is rebuilt from into `upstream/` (§11). That material is kept in the repository and never shipped.
- G5. Every install route and invocation path in §9 is either backed by a source or listed as a probe in §12.

### Non-goals

- Changing or deleting the existing skills or the `socratic` plugin in `ajitta/superclaude`. They are reference material only.
- The skill-folder mode of recursive-refine, which depends on subagents and `scripts.package_skill`.
- Publishing to Anthropic's or OpenAI's public directories.
- Automatic migration of existing installs, such as a marketplace `renames` map. The old skills were used by the owner alone (§10).

## 3. Decision log

These decisions were settled with the owner during the spec interview of 2026-10-20.

| # | Decision |
|---|---|
| D1 | Scope: seven skills. confirm-intent was added during the interview. Extended to ten in 1.3.0 (D35). |
| D2 | recursive-refine is included in reduced form: output mode only, with no subagents and no scripts. |
| D3 | Existing skills are rebuilt from reference copies. They are not edited in place. |
| D4 | The owner's ChatGPT plan is Pro. Both mobile apps (Claude and ChatGPT) are in scope. |
| D5 | Skill files and references are in English. Korea-specific context, such as Korean law, goes in `references/ko/`. Hangul is allowed only there, and `references/ko/` is shipped. |
| D6 | "No harness" applies to the shipped package. Developer-side build and validation scripts are allowed in the repository. |
| D7 | New repository. Reference material is imported into it at the start of work (§11). |
| D8 | The package, repository, marketplace and zip are named `dialectic-skills`. The plugin `name`, which sets the invocation prefix, is `dia`. |
| D9 | Each skill name carries the prefix itself (`dia-<x>`), so a name stays unique on surfaces that add no plugin namespace. |
| D10 | `dia-refine` and `dia-iterate` both keep first-word invocation. `dia-iterate` replaces the earlier working name `refine-loop`, so that no skill name is the prefix of another. |
| D11 | This spec is written in English and lives at `docs/spec.md`. |
| D12 | The upstream snapshot zip is produced only after the owner approves this spec. |
| D13 | The repository-root folder for imported source material is named `upstream/`, so it is not confused with each skill's shipped `references/`. |
| D14 | The skills are independent, general-purpose plugin skills. Skill text names no other project and no product: the reference templates' superclaude next-step lines are removed, `metadata.source` points to this repository, and "Claude" in skill text becomes "you" or "the assistant". The `--target=claude` value keeps its name (§5.4, §5.5) and means the assistant's own earlier answer on every surface. (Owner direction during the build, 2026-10-20.) |
| D15 | The zip stores its entries uncompressed. Deflate output differs between zlib builds (for example zlib-ng in some CPython builds), so a deflated zip is not byte-reproducible across machines (§12.1). |
| D16 | No portable root `plugin.json` (O2): P3 showed Codex 0.162.1 installs the plugin from `.claude-plugin/` alone, and a root `plugin.json` does not change the skill names. |
| D17 | No `references/ko/` files in 1.0.0 (O1). The mechanism (§6 L2–L5 and its build checks) stays, so a later minor version can add them; P9 is not applicable until then. (Owner, 2026-10-20.) |
| D18 | All seven skills are licensed MIT (O3). (Owner, 2026-10-20.) |
| D19 | Research fixes (`docs/research/`, independently reviewed in `docs/research/review/`) amend §5. They change behavior as follows. dia-elenchus: the "ideas born" record and the user-worded revision are labelled as this skill's own additions; "examine statements, not the person" is labelled as narrower than Socrates' practice; a contradiction is shown as a conflict of the definition and the premises together; a step is withdrawn only when its defect can be named. dia-brainstorm: the departure from the Theaetetus midwife is labelled; a verdict changes under pushback only on a substantive answer. dia-reductio: [L] covers only laws of logic or mathematics, and an unstated definition is [A]; the empty result is "no contradiction found"; the evidence classes add "supplied by the user"; a disputed step is withdrawn only when its defect can be named; a self-examination does not invent a contradiction. dia-negative: labelled internal critique (narrower than Adorno's immanent critique); the evidence classes add "supplied by the user" and own recall is never "verified"; a self-examination neither defends the answer nor concedes a gap that fails Rule 2; a disputed finding is withdrawn only when its defect can be named, and a finding that survives is kept with a one-line reason. dia-refine: each confirmed error carries its basis; "final version only" allows one closing line for what the user would otherwise not see. dia-iterate: fewer passes than the previous round is no longer a regression, and a regression undoes only the offending edit; rounds whose defects are all unverifiable stop as "verification exhausted", not "zero defects"; own re-derivation is not verification here; `@dia-iterate` and a by-name invocation count. dia-intent: values worked out without a tool are labelled re-derived; a correction that conflicts with inspected evidence is named once. All seven: `default_prompt` uses `$dia:dia-<x>` (P3). (Owner direction, 2026-10-20.) |
| D20 | The remaining reviewed research findings amend §5 further. dia-reductio: strength grades work in both directions, "both" records one contradiction per direction, not-Q must be the contradictory of Q, a worked example and a "Checked by" record line. dia-iterate: every checkable claim that bears on the result is a candidate, fixed values are locked on their confirming source, locks are shown, round-1 style edits are marked unverified, and a search snippet alone is a single source. dia-refine: unverified marks go in ④, sources sit next to the sentence concerned in the revision, added requirements and necessary corrections may lengthen the revision. dia-negative: only fitting options, a no-findings path, template and record fallbacks, and a description that calls the purpose an inference. dia-elenchus: premises numbered from the visible answers, label criteria in SKILL.md, an irritation script. dia-brainstorm: a one-line thesis summary every ~4 probes, a synthesizing question before the verdict, a criteria prompt, options that differ in kind, SCAMPER only in Step 3. dia-intent: no private data out or cost before approval, the confirmation names what is sent or spent, an explicit reply language. (Owner direction, 2026-10-20.) |
| D21 | Corrections from the diff reviews of the D19/D20 changes (independent, 2026-10-20): dia-reductio grades and the template work when proving, a "premise set inconsistent" result offers the premises of both derivations, key-term meanings and existence premises carry labels, and theory.md lists its Duhem–Quine sources; dia-iterate's description, step 4 and verification table state the round-1 exception consistently, an undone fix lists the defect it had fixed, and narrowed criteria narrow the candidate list; dia-refine's closing line covers unverified items that bear on the conclusion and file-target sources; dia-negative's label is "narrower than Adorno's immanent critique", theory.md says the same, user-supplied facts are not conditional, and the no-findings path carries through Step 7; dia-elenchus uses one ask ("Which would you change?"), keeps premise numbers stable, and labels the "ideas born" layer in the description; dia-brainstorm has one summary cadence, a fallback for "thesis after", and Hickey's own term; dia-intent's no-data-out rule covers reads and searches, and its language rule ignores an invocation prefix. Routing (L7): the dia-elenchus and dia-brainstorm descriptions say that a request for Socratic dialogue or the Socratic method goes to dia-elenchus unless the user asks to brainstorm or for options and a plan, after the Korean elenchus cell of P7 dropped from a neutral directory (`docs/probes.md`). |
| D22 | Second-pass review corrections (2026-10-20; `docs/research/review/pass2/`): dia-iterate's "verification exhausted" means no defect named this round was confirmed and at least one was unverifiable, and confirmed defects left unfixed get their own line; dia-negative withdraws a disputed finding only when its defect can be named; dia-reductio's options work when proving and for an inconsistent premise set; dia-refine's closing line can carry file-target sources; dia-brainstorm's `deep` checkpoint replaces that turn's probe, and its Step 0 defers general "Socratic" requests to dia-elenchus; dia-elenchus keeps ① for the definition and numbers premises from ②; D19–D21 omissions noted by the reviews (dia-reductio's letter-substitution reread and own-scheme label; dia-refine's tag set and language fallback; dia-brainstorm's narrowed kind rule and standalone pacing cue; dia-iterate's description, round-1 split, undo listing and table rendering) are part of the record. |
| D23 | Remaining low research findings, in the reviewed forms (2026-10-20; `docs/research/review/lowfix/` holds the implementers' accounts and the diff reviews). dia-reductio: the description asks whether a position "holds together or follows from its premises" (P7 re-run at `6882022`: no drop); Step 4 prefers a contradiction that depends on fewer [A] premises; the "carried" check is shown or written "not found"; Step 2's note covers indirect proof in general (intuitionistically acceptable when T is a negation); Step 8 names the record fields as a template fallback; `all` gives one combined record; a pitfall names the tolerance premise of small-step chains; theory.md cites the *Apology* (27b–e) directly, drops Madhyamaka, and adds a hard-cases section with a one-line dialetheism note (kept by owner ruling). dia-iterate: a quotation confirmed to misstate its source may take the source's exact words in one sentence, otherwise only its location, never for set texts; content-filter claims are worded as observed risk; self-written tests are named in the log; confirmed defects are a lower bound; one line per round may replace the table on request; a fixed point lists its unfixed confirmed defects. dia-refine: re-derivation starts from the question or the user's data; the no-subagent rule gains a reason upstream did not give (an addition, not a translation); a bare claim that something is wrong is review criteria; creative work: a conflict with a stated purpose, audience, tone or constraint is a confirmed basis, and taste goes to the closing line; the body labels the skill as not the iterative Self-Refine loop and cites Huang et al. for the softened step-5 reason; the example is plain Markdown and shows a suspected correction. dia-negative: the falsifier is an observation the user can make (a restatement of the purpose does not count); narrowing C notes that it may only move the gap; the function is whose interests the pattern favors, not an intention; Rule 8 does not decide for the user; theory.md labels the falsifier as Popperian and corrects attributions and quotations. dia-elenchus: the scope shift from virtues and the departure from the Theaetetus midwife are labelled; irony is dropped explicitly and the no-answers stance is cited to Aristotle; the paraphrase flag is not a second question; a shift is named in the user's key words with no label of the assistant's; a user who repeats examples gets a model definition of something unrelated; host study-mode hints count as the question-type tour; a user who holds that the cases share no single feature ends in aporia. dia-brainstorm: ask only what the user can answer; a "did I assume something" confirmation; Step 4's questions are skipped with Step 3; one "any more" nudge and one criterion prompt; test cases versus replacement plans; full names for the expert lenses; one "None:" line for empty brief sections; the date only if known. dia-intent: short exact constraints are quoted in the user's words and still checked; an empty decision list is not padded; for an analysis deliverable the review shows only what decides scope or a decision; the confirmation names the limit for open-ended work; a direct follow-up uses the re-agreement rule; the long paragraphs are bulleted without wording changes; `short_description` is 60 characters. |
| D24 | Token audit, recommended set (2026-10-20; `docs/research/token-audit/`). Each skill's text was classified by kind and counted; restated rules, duplicated pitfalls and design defences were cut or shortened, labels were shortened in place and kept, worked examples, template fields and no-reference fallbacks were kept. dia-elenchus moves its dialogue loci and scholarly notes, including D23's Aristotle citation for the no-answers stance, to a new `references/theory.md` (read on request) and keeps the labels in the body. dia-reductio adds one-line rules for rules or practices and for *per impossibile* reasoning (an impossible supposition, result **stopped**) to the body, from theory.md §4 and §6 (owner ruling 2026-10-20, outside the recommended set; theory.md keeps its text). dia-refine's natural-language triggers and passing-mention rule live in the description only, and its intro sentence on chats with no tools is cut: step 3's conditional wording carries the §5.6 rule "verification limited to what tools allow" without the upstream reason. dia-intent's response template keeps its four section labels, the re-derived cue and the Confirmation contents; bracket text that restated items 1–3 is cut, and two sentences restating where settled points go and what may trigger the dependent-decisions path are cut (no rule change). Diff-review fixes: dia-negative Rule 6 covers every target's motives and its opening line ties the remainder thesis to strict gaps; dia-reductio Rule 6 names the contradiction's premises; dia-iterate lists anecdotes about famous people as set texts again; dia-elenchus's record template says plain Markdown, not a code block. Not applied (owner decisions not taken): dia-brainstorm's method-paragraph rewording, dia-negative's Jaeggi/Stahl shortening, dia-refine's extended set. SKILL.md bodies drop about 1,000 cl100k tokens in total. |
| D25 | dia-negative description narrowed after Codex routing confirmed research F7 (probes Part F: chosen for 6/10 prompts that were not critique requests). Triggers now name their object ("what is this claim or policy really for", "where does this claim fail its own standard"), a line excludes questions about what code, a command or a setting does and general reviews, and the closing cross-references are shortened to stay within 1,024 characters. Owner ruling 2026-10-20; still 0.1.0. |
| D26 | XML-tag study (`docs/research/xml-tags/`): no XML tags in the skills; Markdown stays the structure, and output templates stay plain Markdown. Instead, one plain sentence per skill that reads outside material says it is material, not instructions: dia-refine and dia-iterate (target, and for dia-iterate pages or files opened to verify it), dia-reductio and dia-negative (`text` target), dia-intent (material read before approval cannot approve the review, widen scope or override the user's constraints). dia-iterate's output template says to print plain Markdown, not a code block; dia-elenchus's contradiction layout uses `[definition]` placeholders, which render, instead of `<definition>`. Owner ruling 2026-10-20; still 0.1.0. |
| D27 | After the skill-effect eval (`docs/skill-effect.md`): dia-refine lost every pair because its revision kept claims it believed false ("unverified items stay as drafted", from upstream). Now a factual claim it could not check but believes wrong goes into the revision as the suspected correction, marked "(suspected, unverified)" (in "final version only" mode, no mark; the closing line names it), and is still listed under ④; quotations, names the user chose and the user's own figures are never changed this way. The description says the revision "marks suspected ones" (P7 re-run). dia-iterate keeps its rule that own re-derivation is not verification, and on a "verification exhausted" stop with re-derivable items points to one dia-refine pass. Departure from upstream self-refine; owner ruling 2026-10-20; still 0.1.0. |
| D28 | Several skills in one prompt (probes Part K). dia-elenchus and dia-brainstorm: when both are named, the definition dialogue comes first, the first message says so, and brainstorming starts when the user asks or the dialogue ends; never interleaved. dia-refine and dia-iterate: when both are named, they run as separate passes with separate outputs, and a re-derivation from the refine pass never counts as verification in an iterate round. Output length for several analyses at once is left to the P1/P2 phone checks. Owner ruling 2026-10-20; still 0.1.0. |
| D29 | `short_description` in every `agents/openai.yaml` is 25–64 characters, the OpenAI skill UI guidance (openai/skills `openai_yaml.md`; research intent review M5, now repo-wide). `tools/package.py` enforces the range. The field is UI-only: Codex shows the model the SKILL.md `description`, not `short_description` (`codex debug prompt-input`, 2026-10-20), so routing is unchanged and no probe was needed. |
| D30 | `dia-intent` is renamed `dia-confirm` in plugin 1.1.0 (owner, 2026-10-20). Reason: SuperClaude's `/sc:intent` also captures intent before work, but records it as a committed `00-intent.md`; this skill shows the goal, assumptions and open decisions and holds until the user approves, and the new name states that hold. It also continues the lineage name `confirm-intent`. The rename breaks invocation by the old name; released as a minor version because the owner was the only user and the repository was still private. `tools/package.py` rejects `dia-intent` outside `metadata.lineage`. Decision rows and research documents dated before D30 keep the old name as a historical record. `dia-brainstorm` keeps its name despite `/sc:brainstorm` (owner, same day): both brainstorm, and dropping the Socratic cue from a name has hurt routing before (probes Part B). |
| D31 | The README is written in English and translated into Korean, Japanese and Simplified Chinese (`README.ko.md`, `README.ja.md`, `README.zh-CN.md`; owner, 2026-10-20). Each file starts with the same language switcher. The translations are repository files, not shipped, so the shipped-package language rules (§6) do not apply to them; they are an exception to D11 for the README only. A test keeps them in step with `README.md`: same heading levels, tables, link targets and code-block count, command blocks byte-identical, and every in-page anchor resolves. Example prompts are translated so each file shows requests in its own language. |
| D32 | Directory listings, prepared in 1.1.1 (owner, 2026-10-20; requirements in `docs/directory-submission.md`). (1) The plugin folder ships a `README.md` generated from `packaging/plugin-README.md`, because the Anthropic directory blocks a plugin folder without a README of at least 40 words; it states that the plugin runs, sends and fetches nothing itself. (2) The OpenAI directory upload is a separate generated zip, `releases/dialectic-skills-openai.zip`: the same files with `.codex-plugin/plugin.json` (the manifest plus the `interface` listing fields from `packaging/openai/interface.json`) in place of `.claude-plugin/`, and two square SVG images under `assets/` for `interface.logo` and `interface.composerIcon`. Images exist only in that zip, so the marketplace payload stays Markdown, YAML and JSON (§7.1). `tools/package.py` checks the README length and the OpenAI final-submission limits, and the listing files count toward the version digest. The logo is a draft for the owner to replace if wanted. |
| D33 | All seven skills set `allow_implicit_invocation: true` in plugin 1.2.0 (owner, 2026-10-21). Reason: on ChatGPT mobile the four explicit-only skills (dia-confirm, dia-elenchus, dia-brainstorm, dia-iterate) could be reached only through the `@` picker, because `false` drops a skill from the model-visible list (probed on Codex, P3 and Part M; on ChatGPT mobile observed by the owner before and after the change, P5 1.2.0), so a message starting with the skill's name did nothing; on Claude the same message works (P2), and Claude already routed dia-elenchus and dia-brainstorm from natural language (P7). Now dia-elenchus and dia-brainstorm route as on Claude, and dia-confirm and dia-iterate are gated by wording: dia-iterate by its existing description and body marker rule, dia-confirm by a description that names the first word and says a request that only sounds like it is not an invocation, plus a body sentence for a load without the marker (run the review only on an explicit request to confirm first; otherwise do the task without holding it; added after the independent review). Probes Part M (Codex, base 1.1.1 vs 1.2.0; Claude for the dia-confirm description). Cost: the Codex/ChatGPT always-on listing grows from 610 to 1,342 o200k tokens (Codex measured; ChatGPT's own list was not measurable from here). This reverses the upstream `04-design.md` D2 choice for Codex only; `disable-model-invocation` stays unused (§7.2). |
| D34 | dia-brainstorm 1.1.1, plugin 1.2.1 (owner, 2026-10-21). After D33, ChatGPT mobile loaded dia-brainstorm for a plain task written as a bare noun phrase («사진 파일을 날짜별로 이름 바꾸는 스크립트»). The description now says the skill is for a user who asks to think an idea through with questions, poke holes in it or stress-test it, and is not for a request to make or write something (a script, code, a text), even one that names an idea; Step 0 says that if the skill was loaded for such a request anyway, do the task without it. The ChatGPT case did not reproduce on Codex or Claude; the change kept every positive routing cell on both, within n=3 noise (Codex idea cell 2/3; probes Part N). A forced load of the body on Claude wrote the script 6/6 with the 1.2.1 body against 1/6 with the 1.2.0 body (independent review). On ChatGPT mobile with 1.2.1, the owner's noun phrase gave the script directly (P5). |
| D35 | Three skills added in plugin 1.3.0 (owner, 2026-10-21; built on branch `next`, merged to `main` 2026-10-22): `dia-warrant` (Toulmin layout with Walton's critical questions, one pass), `dia-conjecture` (Lakatos's proofs and refutations on a strictly universal claim, multi-turn) and `dia-counterplan` (Mason's dialectical inquiry on a plan or decision; the user synthesizes). Basis: `docs/research/candidates/` (six family documents, weighed by fit for human-AI chat and fidelity) and its independent review (`docs/research/candidates/review/`, all SOUND WITH FIXES); the owner picked dia-warrant (cluster 1) and dia-counterplan (cluster 3), and dia-conjecture, which the index review (F7) moved out of cluster 2 into the distinct candidates; cluster 2 (dia-munazara, dia-defend) was not picked. Each skill applies its review's corrections; the applied and declined findings are in `docs/research/candidates/design/<skill>.md`. Routing: each new description carries exclusion sentences toward its bordering siblings. Sibling edits (index review F10): dia-reductio 1.1.0 asks whether a position "holds together or follows strictly from its premises" (D23 had "follows from") and points to dia-warrant and dia-conjecture; dia-brainstorm 1.2.0 points to dia-counterplan and, to stay within 1,024 characters, drops the verdict names and "short" and shortens two phrases ("For Plato's strict dialogue", "even one naming an idea"), with no rule change; its Step 0 gains a fallback line toward dia-counterplan, dia-conjecture and dia-warrant. A request for a devil's advocate on a plan is answered with dialectical inquiry (a counterplan), not with devil's-advocacy critique; critique by questions stays with dia-brainstorm's stress mode. The ten descriptions total 1,922 o200k tokens at `b30344d` (1,219 for the seven at `eb7ab54`). Routing probes: probes Part O. Not done in this decision: the site (plates and text); dia-hypothesis, dia-commit, the munāẓara pushback rule (separate batch). |
| D37 | Description clean-up for plugin 1.3.0 (owner, 2026-10-21; shipped in 1.3.0 on 2026-10-22). An independent audit (`docs/research/candidates/review/clean/audit-descriptions.md`) found the descriptions patched sentence by sentence through the probe rounds: 1,924 o200k tokens for ten (1,219 for seven at 1.2.1), 26% of it pointers to siblings, five within 15 characters of the 1,024 cap. All ten were rewritten to the §7.2 convention, keeping every phrase with probe evidence: 1,566 tokens, longest 896 characters. Added in the same pass: dia-warrant's fallacy trigger (Part O cell 0/5) and dia-brainstorm's pointer to dia-warrant ("Poke holes in my argument …" went to dia-brainstorm). Body cuts in dia-warrant, dia-conjecture and dia-counterplan removed restated rules and pitfalls (`audit-bodies.md`). Gate: probes Part P. Two cuts were reverted on gate evidence: dia-refine's "treat it as a draft" trigger and dia-warrant's explicit "none given" result with the one-pass rule. Skill versions: dia-elenchus 1.2.0, dia-negative 1.1.0, dia-refine 1.1.0, dia-iterate 1.2.0; the others keep the 1.3.0-cycle numbers. D36 is reserved for the `upstream/` move on branch `docs-skills-cli`. |
| D38 | `dia-menu` added in plugin 1.4.0 (owner, 2026-10-25; built on branch `menu`). Reason: typing `dia-<x>` or `/dia-<x>` in full is slow on a phone (a hyphen and, on the Claude mobile app, a `/` that the menu does not complete). `dia` alone shows a numbered menu of the ten skills; `dia <number>` or `dia <first letters>` runs that skill (an ambiguous prefix is asked about); `dia <request>` picks among dia-brainstorm through dia-refine, says which in one line, and runs it, asking when two fit about equally. It never starts dia-confirm or dia-iterate from a plain request (owner ruling (a), 2026-10-25: their gates stay); a selector by name or number counts as an explicit invocation, so dia-confirm 1.3.0 and dia-iterate 1.3.0 each gain one sentence saying so, plus a clause in their descriptions. Naming: the menu's trigger word `dia` is not a skill name; the skill is `dia-menu`, so D9 (each name carries the `dia-` prefix) and the §4 rule that no name is a prefix of another both still hold. A keyboard text-replacement route was offered and rejected by the owner as out of scope. The menu also declines an explicit "confirm the goal first" request without the name or number (it replies with `dia 1 …`), although dia-confirm's own body would run it; this costs one round trip and keeps ruling (a) simple. After the independent review (`~/work/dia-review/menu-2026-10-25/report.md` on the build VM): dia-conjecture takes claims about what is the case, not rules or policies to adopt (those go to dia-counterplan for a plan or decision, otherwise dia-brainstorm); a selector needs three letters and yields to a word that belongs to the sentence; the warrant, counterplan and elenchus borders follow those skills' descriptions; dia-iterate's selector form is `dia iter`; after the second review pass, a number that counts something (`dia 1 thing …`) is a request, not a selector, and dia-confirm and dia-iterate say so too. Descriptions: 1,706 o200k tokens for eleven (1,566 at 1.3.0): dia-menu 119, dia-confirm +9, dia-iterate +12. Probes: `docs/probes.md` Part Q. D36 is reserved for branch `docs-skills-cli` (not merged). |
| D39 | `dia-iterate` is renamed `dia-ratchet` in plugin 1.5.0 (owner, 2026-10-28; built on branch `adjudicate-ratchet`, not merged). Reason: the skill's defining rule is not repetition but its evidence gate (only an outside check counts, the user's own material included; your own re-derivation does not), and "iterate" suggests the self-judged revision loop the skill exists to prevent (Huang et al., ICLR 2024). A ratchet moves only forward on confirmed evidence, locks what passed and stops on regression, which is the skill's stop-and-lock design. The descriptions now lead with the evidence basis that separates the two review skills: dia-refine fixes on "a tool, the user's material or your own re-derivation of the logic or a calculation"; dia-ratchet fixes only on "an external check ... never on your own re-derivation". dia-ratchet 1.4.0 (its lineage records the old name), dia-refine 1.2.0, dia-menu 1.1.0 (selector `dia ratchet`, `dia rat`). `rat` is a prefix of no other name. As with D30, the rename breaks invocation by the old name; the owner and a few acquaintances are the only users, so no alias is kept, and `tools/package.py` now rejects `dia-iterate` outside `metadata.lineage`. Decision rows, research documents, probes and reviews dated before D39 keep the old name as a historical record. Not done here: routing probes for the edited descriptions (re-run probes Part P's flagged cells and Part Q's gated cells under the new name), the project page (`site/`). |
| D40 | `dia-adjudicate` added in plugin 1.5.0 (owner, 2026-10-28; branch `adjudicate-ratchet`, not merged). A judge that rules on reports others wrote about a target (critiques, reviews, verification reports): it inventories the target's claims independently of the reports, merges report items, checks each against outside evidence and gives verdicts with an evidence class, without rewriting the target. Its rules come from trials in which judge agents misruled (`docs/research/dia-adjudicate.md`): overturning a report item needs a contradicting source span on the same point, and a summarizing fetch caps an overturn at "unverifiable" unless a direct question to the source contradicts the item; not found is not false; quotations are compared to the letter, and a report that misstates its own cited source is always listed; study-to-case conditions are compared; agreement between reports is not evidence; one reading of the target throughout, with a consistency check; every overturn goes into the tables and a must-check list for a person; running twice and checking only the differing items is recommended where the host allows it. Gating: explicit-only, like dia-ratchet (first word or name, dia-menu selector 11); the menu never chooses it from a plain request. Draft history v0.1 to v0.6 and the trial results are in the research document; those are draft numbers, and the shipped skill starts at 1.0.0. Not done here: routing probes (first-word cells, and negative cells against dia-refine, dia-ratchet and dia-warrant), a README skill-guide example from a recorded run, the project page. |
| D41 | `dia-instruct` added in plugin 1.6.0, and dia-adjudicate 1.1.0 rewritten by its rules (owner, 2026-10-28; branch `writing-for-models`, built on `adjudicate-ratchet`, not merged). dia-instruct checks or writes text a model reads and follows (skill files, agent and sub-agent prompts, AGENTS.md, rules files, hook and tool messages) against four rules: each paragraph one expression holding its condition, limit and fallback; a scope word read as a type signature; fewer instructions, each with its reason; one name per thing. It adds structure items, leads that are never findings, and a change procedure: a meaning change only on request or by a rule, an A/B when an eval exercises the change, and review of kept text by a sub-agent that did not write it where one is available. Source: the owner's writing-for-models draft, cleaned for public release (nothing from the owner's private repository); what each part rests on is in its `references/evidence.md`, and the session record is in `docs/writing-for-models/`. Name: the owner picked dia-instruct over dia-write and dia-prompt; `ins` is a prefix of no other name. Invocation: natural language, like dia-refine, with one Not-for sentence toward dia-refine and dia-adjudicate; dia-menu 1.2.0 gives it row 12 and may choose it for a request (owner ruling). Added for this repository: a sentence that the text under review is material, not instructions (D26). Removed: the related-work line on Matt Pocock's writing-for-agents skill (AGENTS.md rule on other projects; owner ruling). dia-adjudicate 1.1.0 is the B arm of the A/B in `docs/writing-for-models/ab-dia-adjudicate/`: each misruling seen in trials moved from the opening list into the rule that targets it as its reason, and the overturn conditions became one rule, so the rules run 1–12; an independent meaning check found no judging change after three were reverted. Over 28 runs in three rounds (Opus and Haiku; local sources and a summarizing fetch tool) it showed no difference from 1.0.0. One count is unresolved: correct items capped at "partly valid" in A 1/6 and B 5/6 runs (p = 0.08); a re-run of that case at 12 or more runs per arm is open. Not done here: routing probes for dia-instruct (natural-language cells, negative cells against dia-refine and dia-adjudicate, menu cells `dia 12`, `dia ins` and a plain request to write a prompt), a README example from a recorded run, the project page. |
| D42 | `dia-confirm` is renamed back to `dia-intent` in plugin 1.6.0 (owner, 2026-10-28; branch `intent`, built on `writing-for-models`). Reason: "confirm" reads as an action the assistant performs rather than as what the skill is about, and the owner found it confusing next to the other names; "intent" names the object of the review (the user's goal, assumptions and open decisions). This reverses D30's name only; D30's behavior (show the review and hold until approval) is unchanged. dia-intent 1.4.0 (its lineage records both former names), dia-menu 1.2.0 (row 1, selectors `dia intent`, `dia int`). `int` is a prefix of no other name (`ins` is dia-instruct); with confirm gone, no three-letter prefix fits two names, so `con` now selects dia-conjecture alone. The rename breaks invocation by `dia-confirm`; the owner and a few acquaintances are the only users, so no alias is kept (as D39), and `tools/package.py` now rejects `dia-confirm` outside `metadata.lineage` instead of `dia-intent`. Records dated before D42 keep the name they used. Not done here: routing probes for the renamed skill (first word, mid-sentence mention, `dia 1`, `dia int`), the project page. |
| D43 | The bodies of eleven skills are rewritten by dia-instruct's rules in plugin 1.6.0 (owner, 2026-10-28): dia-intent, dia-brainstorm, dia-elenchus, dia-reductio, dia-negative, dia-warrant, dia-conjecture, dia-counterplan, dia-refine, dia-ratchet and dia-menu. Reason: the owner wants every skill written so that a model reads and follows it more reliably (conditions inside the sentence they gate, reasons attached, one name per thing); readability for people is not a goal. Scope: body only; frontmatter, descriptions, `agents/openai.yaml` and `references/` are unchanged, so the routing gates (probes Parts P and Q) still describe the same descriptions. Wording and structure only, with no intended behavior change, so no A/B was run and the change is unmeasured (owner accepted). Each body was rewritten by one sub-agent and reviewed for meaning and against the rules by another that did not write it; every confirmed finding was fixed before adoption. dia-elenchus's Pitfalls section is folded into the rules it qualifies; dia-counterplan's Targets bullets moved under Parameters. Versions: dia-brainstorm 1.3.0, dia-elenchus 1.3.0, dia-reductio 1.2.0, dia-negative 1.2.0, dia-warrant 1.1.0, dia-conjecture 1.1.0, dia-counterplan 1.1.0; dia-intent, dia-refine, dia-ratchet and dia-menu keep their unreleased 1.6.0 versions. Meaning changes the rewrite surfaced are listed for the owner in `docs/writing-for-models/rewrite-2026-10-28.md`, not applied. |
| D44 | Two contradictions surfaced by the D43 rewrite are fixed in plugin 1.6.1 (owner, 2026-10-28; `docs/writing-for-models/rewrite-2026-10-28.md`). dia-warrant 1.1.1: "Stop means stop" gave **stopped** whenever the warrant was "never stated or accepted", while Rule 9 limits **stopped** to an ask-mode end before the layout is complete and Follow-up turns give a rejected warrant **weakest link: warrant**; now, at any stop, a rejected reconstruction with no rule of the user's own named after it reads "none given" and gives **weakest link: warrant** (Rule 7, as Follow-up turns already said); otherwise **stopped** applies when, and only when, the stop comes before the user stated or accepted a warrant or before any critical question was asked; Rule 9 defers to that sentence. dia-conjecture 1.1.1: Step 3 labelled only local cases ("local only" or "both") while Step 5 branches on "global only"; now every case is labelled global only, local only or both (Lakatos's Rule 3 applied to every case, against the listed lemmas), Hard rule 2's check, the weaker-lemma repair, the give-up option and the record use the same three labels. theory.md §5 lists the every-case label as a departure. Meaning changes made on the owner's request; no eval exercises these conditions, so they are unmeasured (dia-instruct step 1), and each was reviewed in two rounds by sub-agents that did not write it; the second round's dia-warrant precedence fix was self-checked. |
| D45 | dia-intent 1.5.0 in plugin 1.7.0 separates the deliverable from a result the user wants beyond it (owner, 2026-10-28; branch `intent-outcome`; source: a separate Codex session, summarized in `docs/research/codex/README.md`). Item 1 gains two parts. First, a target or measure that the request, conversation or materials do not state is presented as the assistant's proposal. Second, when the request, conversation or materials state a result beyond the deliverable that the finished deliverable could fail to bring about, the review lists the deliverable's criteria apart from the criteria that would show that result, calls any indirect measure a proxy and says what it cannot show, says when each criterion can be checked (now, once the deliverable exists, or only by later or outside observation), and marks the result unverified when no check can reach it; with no such result stated, the split is left out. The description, `agents/openai.yaml` and every other skill are unchanged, so the routing gates still describe the same text. The Codex draft's other parts were not taken: the "Evaluation basis" for a later evaluation skill that does not exist, and the description change. Its four restored rules were already in 1.4.0. A/B (dia-instruct step 1; `docs/writing-for-models/ab-dia-intent.md`): Sonnet and Haiku, five cases, blind Opus judge. The first text (B, n=6) applied the split whenever the deliverable could miss the intended outcome, and split off unrequested outcomes on simple requests (Sonnet churn 6/6, rename 5/6, delete 2/6; 1.4.0 0/6), so it was not adopted. The adopted text (B2, n=12) limits the split to a stated result and restores the word "proxy": no over-application beyond 1.4.0 (at most 1/12 per cell); Haiku landing page O1 9/11 → 10/10, O2 2/11 → 6/10, O3 7/11 → 10/10; Sonnet claim proxy labelling 6/12 → 11/12; Sonnet landing proxy labelling 8/12 → 3/12 (the judge counts sign-up conversion as a proxy for sales, which B2 lists as a result criterion); replies 7–20% longer. Each text was reviewed by a sub-agent that did not write it. The second review's findings (PASS WITH FIXES: "result" also names a task's output elsewhere in the file; the "unverified" condition can be read narrowly; an inferred outcome can enter as a proposed target without the split; the reporting after approval is not covered) are listed for the owner and not applied, because each would change the tested text; the owner ruled to ship B2 as tested and keep the eight findings open for a later version (2026-10-28). Naming (same session): the plugin, repository and prefix are not renamed (owner, 2026-10-28). |
| D46 | dia-intent 1.6.0 in plugin 1.8.0 states an outcome hypothesis (owner, 2026-10-28; branch `next-1.8`). Reason: a request names a deliverable and the outcome it serves usually goes unstated; the owner wants that purpose inferred, not left out (his coding-harness contract does the same, measured as always-on text in coding tasks). The owner weighed integrating that contract as a new skill or a mode and chose to fold the idea into dia-intent, because an on-demand skill does not carry the always-on effect and dia-intent already holds for approval, so a wrong guess is corrected before work. Item 1: when the request, conversation and materials state no outcome beyond the deliverable, one line, labelled as the assistant's outcome hypothesis, names the outcome the deliverable most likely serves and invites confirmation or correction, in every review (owner ruling), with no split and not as a decision; when the likely outcomes would change the deliverable, the choice is an item 3 decision instead. Recognizing Approval: a proceed instruction (a bare "yes" to the request to proceed included) approves the work with the hypothesis, as confirmed or corrected, as the working interpretation and without the split; a confirmation or correction alone revises the review, which gives that outcome the split when item 1 calls for it. Also applied: D45's review findings 1, 2 and 4–7 ("outcome" as the one name; unverified unless a criterion that would show the outcome, not a proxy, can be checked now or once the deliverable exists; one name for criteria; a criterion or outcome taken from the materials with its source; the split left out when the deliverable cannot fail to bring a stated outcome about), and the D43 proposal on Before Starting (explanations and means are hypotheses unless the user sets them as constraints or requests them as the deliverable). D45's finding 8 (keeping the outcome unverified in the report after approval) stays open, and so does the D43 proposal on a user's correction of a fact that contradicts inspected evidence. Four rounds of independent review; A/B round 3 (`docs/writing-for-models/ab-dia-intent.md`): the labelled hypothesis in every loaded run (1.5.0: none), no rise in over-application, stated-outcome items unchanged or better. |
| D47 | The open meaning-change proposals of the D43 rewrite are resolved in plugin 1.8.0 (owner, 2026-10-28: all of them, each toward the reading the file already supports; `docs/writing-for-models/ab-d43-2026-10-28.md`). Patch versions: dia-brainstorm 1.3.1, dia-elenchus 1.3.1, dia-reductio 1.2.1, dia-negative 1.2.1, dia-counterplan 1.1.1, dia-warrant 1.1.2, dia-conjecture 1.1.2, dia-refine 1.2.1, dia-ratchet 1.4.1, dia-menu 1.2.1; frontmatter and descriptions unchanged except the version, so routing gates other than dia-menu's still describe the same text. Each change was written by one sub-agent and reviewed by another that did not write it (a second review where a fix changed meaning). A/B on the skill-effect eval tasks that reach a change (n=12 per arm on Sonnet and Haiku): dia-reductio's direction rule makes Haiku refute when no direction is named (8/11 → 12/12 on both claims); dia-negative's Rule 3 change (a split finding conditional unless strict on every branch) lost the strict gap on the vacation policy (Sonnet 11/12 → 6/12) and was reverted, so dia-negative keeps only naming ("operative function") and the target bullets under Parameters; the other differences are one or two runs in both directions. dia-menu: the gate is the first case under "Then:"; a new default sending any other rule or policy to dia-brainstorm failed its probe (probes Part U) and was reverted. Also reverted after review: dia-conjecture's "file tool" (the other skills say "filesystem") and dia-refine's "closing line" in Safeguards (default mode has none). Left for the owner: listed in the record, section Left for the owner. |
| D48 | dia-adjudicate 1.1.0 stands after the re-test of its one unresolved count (owner, 2026-10-28; handoff item 28). Round 4 of `docs/writing-for-models/ab-dia-adjudicate/` re-ran case4 at 12 runs per arm on Haiku, headless, with tools restricted by the CLI (Read, Glob, and Bash only for the fetch command) and full streams kept; B is the shipped 1.1.0 text. Correct items downgraded to "partly valid": 1.0.0 6/12 runs, 1.1.0 9/12 (p = 0.40); no correct item overturned in either arm. Round 3's 1/6 vs 5/6 did not reproduce as a difference, so the A/B rule's re-run closes it. |
| D49 | Plugin 1.9.0 settles the owner decisions 1.8.0 left (owner, 2026-10-29: each as recommended). dia-intent 1.7.0: the report of finished work whose review marked an outcome unverified says in one line that the deliverable is done but the outcome is still unverified, and when and how it can be checked (D45's finding 8; A/B round 4 in `docs/writing-for-models/ab-dia-intent.md`: Sonnet claim 7/12 → 12/12, landing at ceiling in both); a user's correction of a fact that conflicts with inspected evidence is the user's to decide (with a proceed instruction the user's value is used and the report notes the difference; without one, both values with sources and an item 3 decision). dia-negative 1.2.2: the record status **stopped**, which had no condition, is removed; the Rules 3/4 resolution was tried and reverted after its A/B (`ab-d43-2026-10-28.md`, Owner rulings after 1.8.0). dia-elenchus 1.3.2: Rule 3 says what follows a withdrawn refutation (premise number, a rejected re-asked premise, a revision made because of it, its record line). dia-conjecture 1.1.3: picking "give up C" ends the dialogue with the record. dia-menu, dia-reductio, dia-counterplan and dia-brainstorm unchanged. Each change was reviewed independently; the dia-elenchus, dia-conjecture and fact-correction changes are not measured (no eval reaches them). |

## 4. Names and identifiers

| Item | Value |
|---|---|
| Repository | `ajitta/dialectic-skills` |
| Marketplace name (`.claude-plugin/marketplace.json`) | `dialectic-skills` |
| Plugin `name` (namespace prefix) | `dia` |
| Plugin `displayName` | `Dialectic Skills` |
| Upload zip | `releases/dialectic-skills.zip` |
| Claude Code install | `/plugin marketplace add ajitta/dialectic-skills`, then `/plugin install dia@dialectic-skills` |

The plugin `name` is the only field that sets the namespace. `displayName` is shown in the UI and is not used for namespacing or lookup. A marketplace entry may carry a different name, but components are still namespaced under the manifest `name` ([Claude Code plugin manifest reference](https://code.claude.com/docs/en/plugins-reference)). The marketplace entry therefore uses `dia`, the same as the manifest, so that install and invocation names agree.

### Skill names

| New skill | Rebuilt from (reference version) | Claude invocation | Codex / ChatGPT invocation |
|---|---|---|---|
| `dia-intent` (named `dia-confirm` from 1.1.0 to 1.4.0, D30, D42) | confirm-intent (installed copy, no version field) | `/dia:dia-intent` | `$dia:dia-intent` / `@dia-intent`, or a message starting `dia-intent` (1.2.0, D33) |
| `dia-elenchus` | socratic-elenchus 1.3.1 (`superclaude@stable`) | `/dia:dia-elenchus` | `$dia:dia-elenchus` / `@dia-elenchus`, or natural language (1.2.0, D33) |
| `dia-brainstorm` | socratic-brainstorm 3.3.1 (`superclaude@stable`) | `/dia:dia-brainstorm` | `$dia:dia-brainstorm` / `@dia-brainstorm`, or natural language (1.2.0, D33) |
| `dia-reductio` | reductio (installed copy) | `/dia:dia-reductio` | `$dia:dia-reductio` / `@dia-reductio` |
| `dia-negative` | negative-dialectics (installed copy) | `/dia:dia-negative` | `$dia:dia-negative` / `@dia-negative` |
| `dia-refine` | self-refine (installed copy) | `/dia:dia-refine` or a message starting `dia-refine` | `$dia:dia-refine` / `@dia-refine` or a message starting `dia-refine` |
| `dia-ratchet` (named `dia-iterate` until 1.4.0, D39) | recursive-refine, output mode only (installed copy) | a message starting `dia-ratchet`, or `/dia:dia-ratchet` | `$dia:dia-ratchet` / `@dia-ratchet`, or a message starting `dia-ratchet` (1.2.0, D33) |
| `dia-warrant` (1.3.0, D35) | new: `docs/research/candidates/argumentation.md` | `/dia:dia-warrant` | `$dia:dia-warrant` / `@dia-warrant`, or natural language |
| `dia-conjecture` (1.3.0, D35) | new: `docs/research/candidates/modern-dialectic.md` | `/dia:dia-conjecture` | `$dia:dia-conjecture` / `@dia-conjecture`, or natural language |
| `dia-counterplan` (1.3.0, D35) | new: `docs/research/candidates/argumentation.md` | `/dia:dia-counterplan` | `$dia:dia-counterplan` / `@dia-counterplan`, or natural language |
| `dia-menu` (1.4.0, D38) | new: menu and router, no method of its own | `dia`, `dia <n>`, `dia <prefix>`, `dia <request>`; `/dia:dia-menu` | the same first word; `$dia:dia-menu` / `@dia-menu` |
| `dia-adjudicate` (1.5.0, D40) | new: `docs/research/dia-adjudicate.md` | a message starting `dia-adjudicate`, or `/dia:dia-adjudicate` | `$dia:dia-adjudicate` / `@dia-adjudicate`, or a message starting `dia-adjudicate` |
| `dia-instruct` (1.6.0, D41) | new: the owner's writing-for-models draft (`docs/writing-for-models/`) | `/dia:dia-instruct` | `$dia:dia-instruct` / `@dia-instruct`, or natural language |

Naming rules:

- Each name is kebab-case and matches its folder name.
- No name is a prefix of another name. A build check enforces this, because `dia-refine`, `dia-ratchet` and `dia-adjudicate` are invoked by first word.

On namespacing outside Claude:

- Codex and ChatGPT invoke skills by `$name` or `/skills` in Codex and by `@` in ChatGPT, or implicitly by description.
- Their documentation does not say whether plugin skills get a namespace. Two skills with the same name are not merged; both appear in selectors ([Build skills](https://learn.chatgpt.com/docs/build-skills)).
- P3 (Codex CLI 0.162.1, n=1) showed that Codex does namespace plugin skills: the plugin route lists them as `dia:dia-<x>`, `$dia:dia-<x>` resolves and `$dia-<x>` does not. `$dia-<x>` is the name only when the skill folder is copied to `~/.agents/skills/`. The Codex column above gives the plugin form.
- The `dia-` prefix inside each name is what keeps the names unique there. In Claude the names appear doubled (`dia:dia-refine`). This is accepted (D9).

Natural-language requests work on every surface and are the safe default on mobile. That is the owner's own finding in `superclaude/portable-skills/README.md`, a single source.

## 5. Skills

The seven rebuilt skills (5.1–5.7) keep their reference behavior unless this section or D19–D35 say otherwise. The three skills added in 1.3.0 (5.8–5.10), dia-menu (5.11, 1.4.0), dia-adjudicate (5.12, 1.5.0) and dia-instruct (5.13, 1.6.0) have no reference; design notes for 5.8–5.10 are in `docs/research/candidates/design/`, dia-menu's design is D38 and §5.11, dia-adjudicate's research is `docs/research/dia-adjudicate.md`, and dia-instruct's record is `docs/writing-for-models/`. For every rebuilt skill, the rebuild:

- renames the skill;
- updates cross-references so that each description names the new skill names;
- removes Hangul outside `references/ko/` (§6);
- adds `agents/openai.yaml` (§7.3);
- sets `metadata.version` to `1.0.0` and records `metadata.lineage` as `<old name> <old version>`.

### 5.1 dia-intent (from confirm-intent; `dia-confirm` from 1.1.0 to 1.4.0, D30, D42)

- Purpose: before work starts, restate the goal, disclose material assumptions and list only the decisions the user must make. Then wait for approval.
- Behavior: the reference, amended by D19–D34; D45 adds the split between the deliverable and a stated result beyond it, and D46 a one-line outcome hypothesis when no outcome is stated.
- Invocation: first word or explicit name. The description says "Use only when the message starts with dia-intent, or when the skill is explicitly selected or invoked by name". `allow_implicit_invocation: true` since 1.2.0 (D33), so the first word works on Codex (probed, Part M); on ChatGPT mobile the owner confirmed it for dia-brainstorm and dia-iterate (P5 1.2.0), and dia-intent there works by the same setting, not checked. A body sentence backs the description up: if the skill loads without the marker, it runs the review only when the user explicitly asked to confirm the goal, assumptions or open decisions first, and otherwise does the task without holding it for approval.
- References: none at present. `references/ko/` is optional (§6).

### 5.2 dia-elenchus (from socratic-elenchus 1.3.1)

- Purpose: Plato's elenchus. Ask "what is X?", collect agreed premises one question at a time, show contradictions, and treat each revision as the user's new idea. It usually ends in aporia and never gives advice.
- Behavior: the reference, amended by D19–D34.
- Cross-reference: "use socratic-brainstorm" becomes "use dia-brainstorm".
- Invocation: natural language or name, as on Claude. `allow_implicit_invocation: true` since 1.2.0 (D33; the reference had false).
- References carried over: `elenchus-patterns.md` and `record-template.md`; `theory.md` added (D24) for the dialogue loci and sources, read only when the user asks about the sources or the method.

### 5.3 dia-brainstorm (from socratic-brainstorm 3.3.1)

- Purpose: modern Socratic questioning, one question at a time. The user lists options, the skill adds up to three labeled ones, and the user converges by criteria. It ends with a verdict and a brief, and never implements anything.
- Behavior: the reference, amended by D19–D35.
- Cross-reference: points to dia-elenchus, to dia-counterplan (description and Step 0) and to dia-conjecture and dia-warrant (Step 0 only) (D35).
- Invocation: natural language or name, as on Claude. `allow_implicit_invocation: true` since 1.2.0 (D33; the reference had false).
- References carried over: `question-bank.md` and `brief-template.md`.

### 5.4 dia-reductio (from reductio)

- Purpose: strict reductio ad absurdum in one pass. The skill:
  - lists premises with source labels [T], [L] and [A];
  - derives Q and not-Q with a named rule on each line;
  - grades the strength of the contradiction;
  - lays out options and recommends one, leaving the decision to the user;
  - ends with a record.
- Parameter: `--target=user|claude|text|all`, unchanged.
- Required change: the description currently contains Hangul trigger terms. They are removed, and the description relies on "or the same in any language". Korean-prompt routing must be probed against a baseline (§12, P7).
- Cross-references: the description points to dia-negative and, since D35, dia-warrant and dia-conjecture; the dia-elenchus pointer was dropped in D37 (no reductio/elenchus confusion recorded). The body has no pointers.
- Invocation: implicit allowed, which is the Codex default; the reference had no `openai.yaml`.
- References carried over: `theory.md` and `output-template.md`.

### 5.5 dia-negative (from negative-dialectics)

- Purpose: internal critique (narrower than Adorno's immanent critique), adapted from Adorno, in one pass. The skill:
  - finds the target's own standard;
  - reports strict gaps with particular cases and "what escapes";
  - infers the operative purpose with a falsifier;
  - gives options without a forced synthesis, recommends one, and ends with a record.
- Parameter: `--target=user|claude|text|all`, unchanged.
- Required change: Hangul in the description (one line) and in `references/theory.md` (one line) is removed or moved to `references/ko/`. The Korean routing probe applies here too (P7).
- Cross-references: point to dia-reductio and dia-elenchus.
- Invocation: implicit allowed.
- References carried over: `theory.md` and `output-template.md`.

### 5.6 dia-refine (from self-refine)

- Purpose: a single review pass over the previous output or a named draft. It checks in this order: factual errors, logical leaps, missing requirements, needless repetition. It fixes only defects whose basis was confirmed and returns one integrated revision.
- Required changes:
  - Translate the whole skill to English. The reference is written in Korean (38 lines contain Hangul). The translation keeps every rule and its reason: candidate listing without a severity filter, verification limited to what tools allow, no subagent self-checks, the output layout ①–④, the "final only" mode, and the safeguards.
  - Invocation:
    - Explicit: a message whose first token is `dia-refine`. Text after it is the review criteria, for example `dia-refine — check the numbers`. `/dia:dia-refine`, `$dia:dia-refine`, `$dia-refine` (copied folder only) and `@dia-refine` also work.
    - Natural language, in English triggers plus "or the same in any language": for example "review your previous answer as a draft", "fix factual errors and logical leaps", "give me only the improved final version".
    - A passing mention of dia-refine in the middle of a sentence is not an invocation.
    - Since D24 the natural-language triggers and the passing-mention rule live in the description only; the body keeps the explicit forms.
    - Multi-round requests belong to dia-ratchet (dia-iterate until 1.4.0, D39).
  - The pointer to recursive-refine becomes a pointer to dia-ratchet.
  - Since D39 the description leads with its evidence basis: a tool, the user's material or its own re-derivation of the logic or a calculation.
- Tool-less surfaces: the behavior is already specified. Unchecked items are marked unverified and left as drafted.
- References: none at present.

### 5.7 dia-ratchet (from recursive-refine, output mode; `dia-iterate` until 1.4.0, D39)

- Purpose: repeated review rounds, each gated by external verification. Each round names defects, assigns an external verification method, verifies, fixes only confirmed defects, locks verified items and logs the round. The loop stops on regression, zero defects, verification exhausted, fixed point, or the round cap (`--max N`, default 3).
- Required changes:
  - Remove skill mode entirely: the "Skill mode" sections, `references/skill-loop.md`, and every mention of `cp -r`, `diff -u`, subagents, `evals/` and `package_skill`. Targets are the last output, a named draft, or a file the surface can read.
  - Invocation: first word or explicit name only. Activate only when the message starts with `dia-ratchet` or the skill is invoked explicitly by name. If the marker is absent but the skill looks right, ask in one line for a message starting with `dia-ratchet`, or an explicit invocation of the skill by name, and stop. Explicit `/dia:dia-ratchet`, `$dia:dia-ratchet`, `$dia-ratchet` and `@dia-ratchet` also count. Until 1.1.1 `allow_implicit_invocation: false` hid it from the model on Codex and ChatGPT, so the first word could not work there; since 1.2.0 it is `true` (D33) and the description and the body's marker rule do the gating.
  - Generalize tool names in `verification-sources.md`. "Context7 doc lookup" becomes "an official-documentation lookup tool (for example Context7) or a fetch of official docs".
  - Add an explicit tool-less rule: when no search, fetch or code tool is available, the only external evidence is the user's instructions and material the user supplies. Most defects are therefore unverifiable, and the loop usually stops after round 1 with the "verification exhausted" list. This is expected behavior, not a failure.
  - Keep the content-filter guardrails: a change-list output by default, no source quotations except a misquotation corrected in one sentence (D23), one retry, then change the output shape.
- Pointers: single-pass requests go to dia-refine.
- References carried over: `verification-sources.md`.

### 5.8 dia-warrant (new in 1.3.0, D35)

- Purpose: a one-pass audit of how well an argument's reasons support a conclusion that is only probable. Lays the argument out in Toulmin's terms (claim, data, warrant, backing, qualifier, rebuttal), supplies the least warrant that licenses the step and labels it reconstructed, tests it with Walton's critical questions tagged by the slot they question, and names the weakest link or says none was found among the questions asked. An "ask" mode has the user fill each slot, one question per message.
- Borders: strict contradiction and deductive validity go to dia-reductio; fixing the previous answer or a draft to dia-refine; counterexamples to a strictly universal claim to dia-conjecture; a plan's assumptions to dia-counterplan; poking holes in an idea or plan to dia-brainstorm (an argument's support stays here).
- Invocation: natural language or name. `allow_implicit_invocation: true`.
- Design note: `docs/research/candidates/design/dia-warrant.md`.

### 5.9 dia-conjecture (new in 1.3.0, D35)

- Purpose: Lakatos's method of proofs and refutations on a strictly universal claim the user holds. The user gives the claim and its argument and rules on each case; the assistant raises one counterexample per message, shown condition by condition, and classifies the user's ruling (invalid, concept-stretching, monster-barring as an explicit definition change, or disputed). Repairs follow Rules 1–4 (local and global counterexamples, hidden lemmas, lemma-incorporation), and the deeper-proof move of section 6a. Popper's prior refutation criterion is a labelled addition. Up to three rounds, then an offer to stop; continues on request.
- Borders: plans, policies, decisions and ideas go to dia-counterplan, dia-brainstorm or dia-negative (C is a rule or generalization about what is the case, not a policy to adopt); the meaning of a word to dia-elenchus; Q and not-Q to dia-reductio; probable claims to dia-warrant; a claim against its own standard to dia-negative.
- Invocation: natural language or name. `allow_implicit_invocation: true`.
- Design note: `docs/research/candidates/design/dia-conjecture.md`.

### 5.10 dia-counterplan (new in 1.3.0, D35)

- Purpose: dialectical inquiry after Mason (1969) on a plan, decision or recommendation. Lists the assumptions it rests on, keeps those that would change the decision if false (SAST test), states a specific contrary for each, checks the contraries are coherent, writes the counterplan at the same level of detail and on the same data, and asks which assumptions from each side the user now holds; that set is the result. The assistant gives no verdict on which plan wins, and the record says one assistant wrote both sides and what the comparison did not test.
- Borders: questioning the user's idea (poke holes, stress-test) goes to dia-brainstorm; counterexamples to a universal claim to dia-conjecture; an argument's support to dia-warrant; a plan against its own standard to dia-negative.
- Invocation: natural language or name. `allow_implicit_invocation: true`.
- Design note: `docs/research/candidates/design/dia-counterplan.md`.

### 5.11 dia-menu (new in 1.4.0, D38)

- Purpose: a short entry point. `dia` alone shows a fixed numbered menu of the skills (ten in 1.4.0; eleven from 1.5.0, with dia-adjudicate as 11, D40; twelve from 1.6.0, with dia-instruct as 12, D41); `dia <n>` or `dia <prefix>` (at least three letters, with or without `dia-`, in any letter case) runs that skill, unless the word plainly belongs to the request's sentence (`red flags …`, `3 reasons …`; this also holds for a number, so `dia 1 thing …` is a request), and an ambiguous prefix lists the matches and asks; `dia <request>` picks one of dia-brainstorm, dia-elenchus, dia-reductio, dia-negative, dia-warrant, dia-conjecture, dia-counterplan, dia-refine and dia-instruct (1.6.0), names it in one line, and runs it, or asks when two fit about equally. A plain task with no fitting method is done without a dia skill; the menu says so in one line and names a skill only if one is close. A rule or policy to adopt goes to dia-counterplan if it is a plan or decision, to dia-brainstorm if the user wants it questioned; a request for exceptions to a rule is a plain answer.
- Gates: dia-intent, dia-ratchet and dia-adjudicate are never chosen from a plain request; the menu replies with the form to send. A selector by number or name is an explicit invocation by name for every skill.
- Hand-off: the chosen skill is loaded the way the host loads skills and followed in full; the menu table is not a substitute. If it cannot be loaded, the menu says so and gives `dia-<x> <request>`.
- Invocation: first word `dia` on its own, or the name. `allow_implicit_invocation: true`.

### 5.12 dia-adjudicate (new in 1.5.0, D40)

- Purpose: rule on reports that others (people or agents) wrote about a target text, answer or draft. Inventories the target's checkable claims before reading the reports closely, merges the reports' points into unique issues, checks each against outside evidence (calculations, quotations to the letter, facts, study-to-case conditions, inference steps) and gives a verdict, a severity by effect on the target's conclusion and an evidence class for each. Does not rewrite the target or write a new critique. Ends with a must-check list of the verdicts where a judge's own errors concentrate: every overturned report item, every "unverifiable" on a claim the conclusion depends on, and every verdict changed by the consistency check.
- Borders: reviewing and fixing a draft yourself goes to dia-refine; fixing through verified rounds to dia-ratchet; an argument's support to dia-warrant (its critical questions may inform the checks).
- Invocation: first word or explicit name only, as dia-ratchet; dia-menu selector 11. `allow_implicit_invocation: true`; the description and the body's marker rule gate it.
- Tool-less surfaces: only the user's material counts as outside evidence; calculations and logic can be re-derived; most factual items stay "unverifiable" and none is overturned.
- Research and trials: `docs/research/dia-adjudicate.md`.

### 5.13 dia-instruct (new in 1.6.0, D41)

- Purpose: check or write text a model reads and follows against four rules (each paragraph one expression holding its condition, limit and fallback; a scope word read as a type signature; fewer instructions, each with its reason; one name per thing) and the structure they imply. A breach of a rule or structure item is a finding; a lead is advice, never a finding. A review-only request yields a report of breaches with location, quote and rule, and no change until the user picks.
- Borders: an answer or a draft for people, checked for factual errors and logical leaps, goes to dia-refine; ruling on reviews others wrote goes to dia-adjudicate.
- Invocation: natural language and by name; dia-menu row 12, and the menu may choose it for a request. `allow_implicit_invocation: true`.
- Tool-less surfaces: without a sub-agent, kept text is self-checked and the check is called not independent; without an eval, a meaning change stays only if it is reported as unmeasured and the user accepts it.
- Owner rulings after the pre-merge review (2026-10-28): replies to the user are in the user's language, while text written or edited keeps its language or the one its rules set; a fix for a confirmed review finding is self-checked, with another sub-agent round only when the fix changes meaning; an edit that only adds or updates a fact or command in kept text (a path, a test command) is self-checked like single-use text; "a general-purpose sub-agent" and the CLAUDE.md trigger stay.
- Research: `docs/writing-for-models/` (session record, A/B on dia-adjudicate); evidence per part in `skills/dia-instruct/references/evidence.md`.

## 6. Language policy

- L1. `SKILL.md`, `agents/openai.yaml`, manifests and every file under `references/` except `references/ko/` contain no Hangul. A test enforces this boundary. The Hangul ranges are U+1100–11FF, U+3130–318F, U+A960–A97F and U+AC00–D7FF, the same ranges as `superclaude`'s `test_shipped_plugin_has_no_hangul`.
- L2. Hangul is allowed only under `skills/<skill>/references/ko/`. Those files are shipped.
- L3. `references/ko/` holds Korea-specific context, such as Korean statutes, case law, or institutional and administrative practice. It does not hold Korean translations of the English files.
- L4. Each `references/ko/*.md` file starts with an English header block:

  ```
  Scope: <what the file covers>
  Source: <primary source, URL>
  As of: <YYYY-MM-DD>
  Use when: <the condition under which SKILL.md tells the model to read this file>
  ```

  Laws change, so the `As of` date is required. The skill must tell the user that date when it relies on the file.
- L5. `SKILL.md` names each `references/ko/` file and the condition for reading it, for example: "If the claim turns on Korean law or a Korean institution, read `references/ko/<file>.md`". Otherwise the file is not read. This keeps the default context small.
- L6. Replies follow the user's language; every skill states this (dia-intent since D20).
- L7. Removing Hangul from descriptions (5.4, 5.5, 5.6) may reduce routing accuracy for Korean prompts. P7 measures this. If routing drops below the baseline, fix the English trigger wording. Do not reintroduce Hangul.

No skill ships `references/ko/` files in 1.0.0 (D17).

## 7. Package format and runtime constraints

### 7.1 Runtime constraints (the "no harness" rule)

The shipped package (`plugins/dia/` and `releases/dialectic-skills.zip`) contains only:

- `.claude-plugin/plugin.json`, plus an OpenAI manifest only if P3 shows it is needed (§7.4);
- `README.md`, generated from `packaging/plugin-README.md` (D32);
- `skills/<skill>/SKILL.md`;
- `skills/<skill>/references/**/*.md`;
- `skills/<skill>/agents/openai.yaml`.

It must not contain any of the following:

- `scripts/`, `bin/` or `hooks/`;
- `.mcp.json` or `.lsp.json`;
- monitors;
- any executable file;
- any non-text file.

Reasons:

- Hooks and scripts do not run on chat surfaces.
- claude.ai and Cowork do not install a plugin that has a top-level `bin/` directory ([plugin manifest reference](https://code.claude.com/docs/en/plugins-reference)).

No skill instruction may require running a command. Tool use is always conditional ("if a search or code tool is available"). Every skill must complete on a surface with no tools.

Prerequisite: claude.ai requires "Code execution and file creation" to be enabled for skills to work, even script-free ones ([Claude Help — skills](https://support.claude.com/en/articles/12512180)). The README states this.

### 7.2 Frontmatter

- Allowed keys: `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`.
  - This is the owner's `superclaude/portable-skills/package.py` whitelist. That project found that claude.ai upload fails hard on Claude Code-only keys such as `disable-model-invocation`, `argument-hint` and `when_to_use` (single source: the owner's probe notes).
- `name` matches the folder name. `description` is at most 1024 characters.
- Description convention (D37): method label (the name a user would type, plus at most one honest qualifier) → what it does, in at most two sentences, only behaviour that separates it from its siblings → "Use when …, or the same in any language." → one "Not for …" sentence naming the sibling for each border. Explicit-only skills: what it does → "Use only when …" → the gate negation → "Not for …". Dates, rule and chapter numbers, lineage, template fields and flags stay in the body. State each border once, on the side probes show over-pulling, unless a probe shows both halves are needed (brainstorm/elenchus, Part B). Target at most 900 characters, so a probe-driven fix still fits. When a description is edited, reread it whole and delete what the new phrase makes redundant; cite the probe cell in the decision row.
- `metadata`: `author: ajitta`, `version`, `lineage`, `source`.
- `license: MIT` (D18).
- Body length guideline: at most 200 lines, the `superclaude` validator limit. Longer material goes in `references/`.

### 7.3 `agents/openai.yaml` (Codex / ChatGPT)

One per skill:

```yaml
interface:
  display_name: "<Display Name>"
  short_description: "<one line, 25–64 characters>"
  default_prompt: "Use $dia:dia-<x> to <action>: "
policy:
  allow_implicit_invocation: <true|false>
```

| Skill | `allow_implicit_invocation` | Reason |
|---|---|---|
| dia-intent | true | First word or explicit name; the description gates it, and a body sentence covers a load without the marker (D33) |
| dia-elenchus | true | Natural-language triggers as on Claude (D33; the reference had false) |
| dia-brainstorm | true | Natural-language triggers as on Claude (D33; the reference had false) |
| dia-reductio | true | Same as the reference (no yaml, default true) |
| dia-negative | true | Same as the reference (no yaml, default true) |
| dia-refine | true | Natural-language triggers are part of its design |
| dia-ratchet | true | First word or explicit name; the description and the body gate it (D33; named dia-iterate until 1.4.0, D39) |
| dia-warrant | true | Natural-language triggers; exclusion sentences toward dia-reductio, dia-refine, dia-conjecture and dia-counterplan (D35) |
| dia-conjecture | true | Natural-language triggers; exclusion sentences toward dia-counterplan, dia-brainstorm, dia-elenchus, dia-reductio, dia-warrant and dia-negative (D35) |
| dia-counterplan | true | Natural-language triggers limited to plans and decisions; exclusion sentences toward dia-brainstorm, dia-conjecture, dia-warrant and dia-negative (D35) |
| dia-menu | true | First word `dia`; the description gates it, and full skill names stay with their skills (D38) |
| dia-adjudicate | true | First word or explicit name; the description and the body gate it (D40) |
| dia-instruct | true | Natural-language triggers for text a model follows; exclusion sentence toward dia-refine and dia-adjudicate (D41) |

`allow_implicit_invocation` defaults to `true`. When it is `false`, explicit `$skill` invocation still works ([Build skills](https://learn.chatgpt.com/docs/build-skills)), but the skill is left out of the model-visible list (P3), so a message that starts with its name cannot reach it. All skills are `true` since 1.2.0 (D33), and the three added in 1.3.0 too (D35), dia-menu (D38), dia-adjudicate (D40) and dia-instruct (D41); explicit-only skills are gated by wording, as on Claude.

### 7.4 Manifests

- `.claude-plugin/plugin.json`:
  - `name: dia`, `displayName: Dialectic Skills`, `version`, an English `description`, `author`, `license`, `homepage`, `repository`.
  - No `skills` key, because `skills/` is scanned by default.
- OpenAI manifest:
  - OpenAI documents a portable `plugin.json` at the plugin root, with `.codex-plugin/plugin.json` as an optional fallback. It also says it accepts Claude-compatible manifests, though new packages should use the portable format ([OpenAI — Build plugins](https://developers.openai.com/plugins/build/plugins)).
  - Default: ship only `.claude-plugin/plugin.json`.
  - If P3 shows that Codex or ChatGPT desktop does not load the plugin, or does not apply `agents/openai.yaml`, add the portable root `plugin.json`. Its content is generated from the same source; OpenAI-specific settings go under `extensions.com.openai`.
  - P3 must also confirm that Claude Code ignores a root `plugin.json` before both are shipped.
- `.claude-plugin/marketplace.json` at the repository root:
  - `name: dialectic-skills`;
  - one plugin entry `dia` with source `./plugins/dia`.
  - ChatGPT desktop reads this file as a legacy-compatible marketplace (same OpenAI page).

### 7.5 Source folders stay plain skills

`skills/<skill>/` in the repository source contains no `.claude-plugin/`, `.codex-plugin/`, `skills/` or `bin/`. The manifest lives in `plugin-manifest.json` and is injected only into the generated `plugins/dia/`.

The reason, from the owner's probe notes (single source, Codex 0.160 and Claude Code 2.1.292):

- A manifest inside a skill folder makes Codex register it as `<name>:<name>` and breaks `$skill`.
- Claude Code then loads it as a `skills-dir` plugin instead of a plain skill.

## 8. Repository layout

```
dialectic-skills/
├── skills/                         source: the plain skills
│   └── dia-<x>/
│       ├── SKILL.md
│       ├── references/*.md
│       ├── references/ko/*.md      optional, Hangul allowed
│       └── agents/openai.yaml
├── plugin-manifest.json            source for .claude-plugin/plugin.json
├── plugin-release.json             digest record for the current version (not shipped)
├── .claude-plugin/marketplace.json marketplace "dialectic-skills" -> ./plugins/dia
├── plugins/dia/                    generated, shipped (committed)
│   ├── .claude-plugin/plugin.json
│   └── skills/dia-<x>/...
├── releases/dialectic-skills.zip   generated, shipped (committed); top-level folder dia/
├── tools/package.py                developer-only
├── tests/                          developer-only
├── upstream/                       material the skills are rebuilt from (§11), never shipped
├── docs/writing-for-models/        dia-instruct's draft record and its A/B on dia-adjudicate (D41), never shipped
├── docs/spec.md                    this document
├── README.md
└── LICENSE
```

## 9. Distribution and invocation by surface

Each route has a status:

- **documented**: a vendor document supports it.
- **owner-probed**: the owner's earlier probe of the `socratic` plugin supports it. This is a single source and must be repeated for `dia`.
- **untested**.

| Surface | Install route | Invocation | Status |
|---|---|---|---|
| claude.ai web / Claude desktop | Customize › Plugins › Upload plugin with `dialectic-skills.zip`. Not Customize › Skills, which rejects a zip that carries a plugin manifest. | `/dia:dia-<x>` or natural language | owner-probed for `dia` (P1) |
| Claude mobile (iOS/Android) | Install once via web or desktop; it reaches the mobile app through the account. The upload screen is not in the mobile app. | Natural language; the mobile `/` menu does not list plugin skills (P2) | owner-probed for `dia` (P2) |
| claude.ai marketplace | Customize › Plugins › Add marketplace `ajitta/dialectic-skills`, then add `dia` from Discover | as above | owner-probed (1.1.0, 2026-10-20; the synced copy on the build VM comes from marketplace `dialectic-skills` and matches 1.1.0) |
| Claude Code | `/plugin marketplace add ajitta/dialectic-skills`, then `/plugin install dia@dialectic-skills`; or account sync after a claude.ai upload | `/dia:dia-<x>`, natural language, first word for refine, ratchet and adjudicate; `dia` for the menu | documented (namespacing) / owner-probed (sync) |
| Codex CLI / IDE | `codex plugin marketplace add <path or owner/repo>`, then `codex plugin add dia@dialectic-skills`; fallback: copy `skills/dia-<x>` to `~/.agents/skills/` | `$dia:dia-<x>` (plugin) or `$dia-<x>` (copied folder), `/skills`, implicit per §7.3 | local-path plugin route probed (P3); GitHub route untested |
| ChatGPT desktop | Upload `dialectic-skills-openai.zip` in the desktop app (saved to the account, reaches web and mobile); or add the GitHub marketplace through Codex in the desktop app (local to that computer only) | `@dia-<x>`, implicit | owner-probed (P4/P5, 2026-10-20; upload vs marketplace observed 1.1.1) |
| ChatGPT mobile | A plugin uploaded as a zip on desktop reaches mobile through the account; a marketplace added on desktop does not | `@dia-<x>`, natural language, first word (1.2.0, D33; owner-probed 2026-10-21) | owner-probed (P4/P5, 2026-10-20; upload vs marketplace observed 1.1.1) |

Sources for the ChatGPT rows: [Build skills](https://learn.chatgpt.com/docs/build-skills), [OpenAI Help — Plugins](https://help-lb.openai.com/en/articles/20001256), [OpenAI Help — Skills in ChatGPT](https://help.openai.com/en/articles/20001066-skills-in-chatgpt).

## 10. Migration (owner's installs)

There are no other users, so there is no automatic migration. Before testing `dia`, remove the old copies on each surface; keeping them loads each method twice under two names.

- claude.ai: Customize › Skills — remove the standalone `reductio`, `negative-dialectics`, `self-refine`, `recursive-refine` and `confirm-intent`. Customize › Plugins — remove `socratic`.
- Claude Code: `/plugin uninstall socratic@ajitta-socratic` if installed, and remove copies under `~/.claude/skills/`.
- Codex / ChatGPT desktop: remove any old copies under `~/.agents/skills/`.

The `superclaude` repository and its `socratic` plugin are left as they are.

## 11. Bootstrap: importing upstream material (first task)

The first commit of the new repository imports the material the skills are rebuilt from. It lives under `upstream/`, is excluded from packaging, and is read-only by convention. Rebuild work reads it; nothing edits it.

`upstream/` (repository root) is unrelated to `skills/<skill>/references/`. The latter holds the documents a skill reads at run time, such as theory notes, output templates and `ko/`, and it is shipped with the plugin (§7.1).

```
upstream/
├── README.md                       provenance table (below)
├── installed/                      from the snapshot zip
│   ├── confirm-intent/
│   ├── reductio/
│   ├── negative-dialectics/
│   ├── self-refine/
│   └── recursive-refine/
└── superclaude-stable-47f791b/     from ajitta/superclaude, branch stable, commit 47f791b
    ├── socratic-brainstorm/
    ├── socratic-elenchus/
    ├── package.py
    ├── README.md                   install matrix and invocation notes
    └── docs-features/              portable-skills-single-plugin/, socratic-brainstorm-skill/
```

Steps:

1. Unpack `dialectic-skills-upstream.zip` into `upstream/installed/`. This is the snapshot produced after spec approval (D12), taken from the copies installed in the owner's claude.ai account on 2026-10-20.
2. Copy the listed paths from `ajitta/superclaude` at `stable` commit `47f791b` into `upstream/superclaude-stable-47f791b/`, using `git archive` or a shallow clone. The snapshot zip will also include them, so step 2 is only a cross-check.
3. Write `upstream/README.md` with one row per item: name, origin, version or commit, date taken, SHA-256 of the folder contents.
4. Add `upstream/` to the packaging exclude list, and add a test that fails if any shipped file path starts with `upstream/`.

Note: the installed copies of reductio, negative-dialectics, self-refine, recursive-refine and confirm-intent carry no `license` or version field. Their provenance row records "installed copy, unversioned". All `upstream/` material is the owner's own work (ajitta): the installed copies were written by the owner on their claude.ai account, and the superclaude items come from the owner's MIT repository (owner statement, 2026-10-20).

## 12. Verification and acceptance

### 12.1 Build checks (`tools/package.py --check`, run in CI and before each release)

- Allowed and forbidden frontmatter keys (§7.2). `name` matches the folder. Description length.
- No skill name is a prefix of another (§4).
- Hangul boundary (L1, L2).
- Forbidden paths and files in the shipped output (§7.1), and no `upstream/` path.
- `plugins/dia/` and `releases/dialectic-skills.zip` match the source byte for byte. Reproducible zip: fixed timestamps, modes and `create_system`, LF line endings, and stored entries (D15).
- Version rule: changed skill files under an unchanged plugin `version` fail. This is the `plugin-release.json` digest rule carried over from `superclaude`. Claude Code updates an installed plugin only when its version changes.
- Cross-references: every skill name mentioned in a description exists.
- `claude plugin validate --strict plugins/dia` passes.

### 12.2 Surface probes

Each probe is run once (n=1) unless stated otherwise, and the result is recorded in `docs/probes.md` with the date and the client version. Any generalization from n=1 is stated as such.

| # | Probe | Pass condition |
|---|---|---|
| P1 | claude.ai upload of `dialectic-skills.zip` | Accepted; every skill in §4 listed as `dia:dia-<x>` |
| P2 | Claude mobile app, one natural-language prompt per skill | The right skill loads; the reply is in the prompt's language. For dia-intent the prompt names the skill, and for dia-ratchet (dia-iterate before 1.5.0) it starts with `dia-ratchet` (a mid-sentence mention should produce the one-line request, not the loop); dia-elenchus and dia-brainstorm use the P7 prompts, which ask for the method by name in natural language. For dia-intent also check that the same request without the name does not load it |
| P3 | Codex CLI plugin install, with only `.claude-plugin/plugin.json` | Plugin loads; `$dia:dia-<x>` resolves (the first run showed that plugin skills are namespaced; `$dia-<x>` applies only to a copied folder); `allow_implicit_invocation: false` holds for the four explicit-only skills. If this fails, add the root `plugin.json` (§7.4), re-run, and confirm that Claude Code still loads with both manifests present |
| P4 | ChatGPT desktop (Pro), local plugin install | Skills appear under `@`; one prompt per skill routes correctly |
| P5 | ChatGPT mobile (Pro) after P4 | Skills are usable; if not, record the plan limitation and test the Codex-cloud fallback |
| P6 | First-word invocation | `dia-refine — check numbers` runs one pass; `dia-ratchet` (`dia-iterate` before 1.5.0) runs the loop; "please refine this paragraph" does not trigger either; a sentence mentioning dia-refine in the middle does not trigger it |
| P7 | Routing baseline, n=2 | Korean and English prompts for reductio, negative dialectics, elenchus and brainstorm. Compare against the old skills from `upstream/`. No drop allowed; on a drop, fix the English wording (L7). From 1.3.0 (D35) also the routing tables in `docs/research/candidates/design/dia-*.md`, with negative cells against every bordering sibling (probes Part O; the dia-warrant/dia-refine border is covered only by a first-word cell) |
| P8 | Tool-less run | On a surface or session with no tools, `dia-ratchet` (`dia-iterate` before 1.5.0) stops after round 1 with a "verification exhausted" list, and `dia-refine` marks unchecked items unverified instead of changing them |
| P9 | `references/ko/` loading, once O1 is filled | A Korean-law prompt makes the skill read the ko file and state its `As of` date; an unrelated prompt does not read it |

### 12.3 Acceptance

The plugin is accepted when:

- 12.1 passes;
- P1, P2, P3, P6, P7 and P8 pass;
- P4 and P5 have recorded results, pass or documented limitation.

## 13. Open items

| # | Item | Needed by |
|---|---|---|
| O1 | Resolved: no `references/ko/` files in 1.0.0 (D17) | — |
| O2 | Resolved by P3: no portable root `plugin.json` (D16) | — |
| O3 | Resolved: MIT for all seven skills (D18) | — |
| O4 | Resolved by P5: ChatGPT mobile works on Pro (owner, 2026-10-20) | — |
| O5 | Plugin `version`: `0.1.0` during development; first a 0.x pre-release (tag and GitHub pre-release), then P1 and P2 on that release, then `1.0.0` at acceptance (owner, 2026-10-20). Done: `v0.1.0` pre-release, P1/P2/P4/P5 on it, `v1.0.0` released 2026-10-20 | — |

## 14. Sources

- Claude Code — Plugin manifest reference: https://code.claude.com/docs/en/plugins-reference
- Claude Help — Skills (zip upload, code-execution requirement): https://support.claude.com/en/articles/12512180
- OpenAI — Build plugins: https://developers.openai.com/plugins/build/plugins
- ChatGPT / Codex — Build skills: https://learn.chatgpt.com/docs/build-skills
- OpenAI Help — Plugins in ChatGPT and Codex: https://help-lb.openai.com/en/articles/20001256
- OpenAI Help — Skills in ChatGPT: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- Owner's prior work (single source): `ajitta/superclaude` at `stable` 47f791b — `portable-skills/README.md`, `portable-skills/package.py`, `docs/features/portable-skills-single-plugin/`
