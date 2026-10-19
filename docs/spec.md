# dialectic-skills — Specification

| | |
|---|---|
| Status | Approved by the owner on 2026-10-20; built as plugin version 0.1.0. Probe results: `docs/probes.md` |
| Date | 2026-10-20 |
| Owner | ajitta |
| Repository | `ajitta/dialectic-skills` (private) |
| Scope of this document | What to build and how to verify it. Building it is a separate step. |

## 1. Summary

`dialectic-skills` packages seven reasoning-and-review skills as one plugin, installed under the plugin name `dia`. The skills are rebuilt from the owner's existing skills (socratic-brainstorm, socratic-elenchus, reductio, negative-dialectics, self-refine, recursive-refine, confirm-intent). The target surfaces are:

- Claude Code
- Codex
- Claude desktop
- ChatGPT desktop
- The Claude and ChatGPT mobile apps

The shipped package contains instructions only: Markdown, YAML and JSON. It has no hooks, scripts, binaries or MCP servers, because nothing may depend on an execution harness at run time. Build and validation scripts exist only in the repository, for the developer.

## 2. Goals and non-goals

### Goals

- G1. One plugin, `dia`, containing seven skills with the names in §4.
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
| D1 | Scope: seven skills. confirm-intent was added during the interview. |
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
| D19 | Research fixes (`docs/research/`, independently reviewed in `docs/research/review/`) amend §5. They change behavior as follows. dia-elenchus: the "ideas born" record and the user-worded revision are labelled as this skill's own additions; "examine statements, not the person" is labelled as narrower than Socrates' practice; a contradiction is shown as a conflict of the definition and the premises together; a step is withdrawn only when its defect can be named. dia-brainstorm: the departure from the Theaetetus midwife is labelled; a verdict changes under pushback only on a substantive answer. dia-reductio: [L] covers only laws of logic or mathematics, and an unstated definition is [A]; the empty result is "no contradiction found"; the evidence classes add "supplied by the user"; a disputed step is withdrawn only when its defect can be named; a self-examination does not invent a contradiction. dia-negative: labelled internal critique (narrower than Adorno's immanent critique); the evidence classes add "supplied by the user" and own recall is never "verified"; a self-examination neither defends the answer nor concedes a gap that fails Rule 2; disputed findings are checked, and a finding that survives is kept with a one-line reason. dia-refine: each confirmed error carries its basis; "final version only" allows one closing line for what the user would otherwise not see. dia-iterate: fewer passes than the previous round is no longer a regression, and a regression undoes only the offending edit; rounds whose defects are all unverifiable stop as "verification exhausted", not "zero defects"; own re-derivation is not verification here; `@dia-iterate` and a by-name invocation count. dia-intent: values worked out without a tool are labelled re-derived; a correction that conflicts with inspected evidence is named once. All seven: `default_prompt` uses `$dia:dia-<x>` (P3). (Owner direction, 2026-10-20.) |
| D20 | The remaining reviewed research findings amend §5 further. dia-reductio: strength grades work in both directions, "both" records one contradiction per direction, not-Q must be the contradictory of Q, a worked example and a "Checked by" record line. dia-iterate: every checkable claim that bears on the result is a candidate, fixed values are locked on their confirming source, locks are shown, round-1 style edits are marked unverified, and a search snippet alone is a single source. dia-refine: unverified marks go in ④, sources sit next to changed sentences, added requirements may lengthen the revision. dia-negative: only fitting options, a no-findings path, template and record fallbacks, and a description that calls the purpose an inference. dia-elenchus: premises numbered from the visible answers, label criteria in SKILL.md, an irritation script. dia-brainstorm: a one-line thesis summary every ~4 probes, a synthesizing question before the verdict, a criteria prompt, options that differ in kind, SCAMPER only in Step 3. dia-intent: no private data out or cost before approval, the confirmation names what is sent or spent, an explicit reply language. (Owner direction, 2026-10-20.) |
| D21 | Corrections from the diff reviews of the D19/D20 changes (independent, 2026-10-20): dia-reductio grades and the template work when proving, a "premise set inconsistent" result offers the premises of both derivations, key-term meanings and existence premises carry labels, and theory.md lists its Duhem–Quine sources; dia-iterate's description, step 4 and verification table state the round-1 exception consistently, an undone fix lists the defect it had fixed, and narrowed criteria narrow the candidate list; dia-refine's closing line covers unverified items that bear on the conclusion and file-target sources; dia-negative's label is "narrower than Adorno's immanent critique", theory.md says the same, user-supplied facts are not conditional, and the no-findings path carries through Step 7; dia-elenchus uses one ask ("Which would you change?"), keeps premise numbers stable, and labels the "ideas born" layer in the description; dia-brainstorm has one summary cadence, a fallback for "thesis after", and Hickey's own term; dia-intent's no-data-out rule covers reads and searches, and its language rule ignores an invocation prefix. Routing (L7): the dia-elenchus and dia-brainstorm descriptions say that a request for Socratic dialogue or the Socratic method goes to dia-elenchus unless the user asks to brainstorm, after the Korean elenchus cell of P7 dropped from a neutral directory (`docs/probes.md`). |

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
| `dia-intent` | confirm-intent (installed copy, no version field) | `/dia:dia-intent` | `$dia:dia-intent` / `@dia-intent` |
| `dia-elenchus` | socratic-elenchus 1.3.1 (`superclaude@stable`) | `/dia:dia-elenchus` | `$dia:dia-elenchus` / `@dia-elenchus` |
| `dia-brainstorm` | socratic-brainstorm 3.3.1 (`superclaude@stable`) | `/dia:dia-brainstorm` | `$dia:dia-brainstorm` / `@dia-brainstorm` |
| `dia-reductio` | reductio (installed copy) | `/dia:dia-reductio` | `$dia:dia-reductio` / `@dia-reductio` |
| `dia-negative` | negative-dialectics (installed copy) | `/dia:dia-negative` | `$dia:dia-negative` / `@dia-negative` |
| `dia-refine` | self-refine (installed copy) | `/dia:dia-refine` or a message starting `dia-refine` | `$dia:dia-refine` / `@dia-refine` or a message starting `dia-refine` |
| `dia-iterate` | recursive-refine, output mode only (installed copy) | a message starting `dia-iterate`, or `/dia:dia-iterate` | `$dia:dia-iterate` / `@dia-iterate`; a message starting `dia-iterate` cannot load it on the Codex plugin route, because the skill is hidden from implicit use (inferred from P3) |

Naming rules:

- Each name is kebab-case and matches its folder name.
- No name is a prefix of another name. A build check enforces this, because `dia-refine` and `dia-iterate` are invoked by first word.

On namespacing outside Claude:

- Codex and ChatGPT invoke skills by `$name` or `/skills` in Codex and by `@` in ChatGPT, or implicitly by description.
- Their documentation does not say whether plugin skills get a namespace. Two skills with the same name are not merged; both appear in selectors ([Build skills](https://learn.chatgpt.com/docs/build-skills)).
- P3 (Codex CLI 0.162.1, n=1) showed that Codex does namespace plugin skills: the plugin route lists them as `dia:dia-<x>`, `$dia:dia-<x>` resolves and `$dia-<x>` does not. `$dia-<x>` is the name only when the skill folder is copied to `~/.agents/skills/`. The Codex column above gives the plugin form.
- The `dia-` prefix inside each name is what keeps the names unique there. In Claude the names appear doubled (`dia:dia-refine`). This is accepted (D9).

Natural-language requests work on every surface and are the safe default on mobile. That is the owner's own finding in `superclaude/portable-skills/README.md`, a single source.

## 5. Skills

All seven skills keep their reference behavior unless this section or D19–D21 say otherwise. For every skill, the rebuild:

- renames the skill;
- updates cross-references so that each description names the new skill names;
- removes Hangul outside `references/ko/` (§6);
- adds `agents/openai.yaml` (§7.3);
- sets `metadata.version` to `1.0.0` and records `metadata.lineage` as `<old name> <old version>`.

### 5.1 dia-intent (from confirm-intent)

- Purpose: before work starts, restate the goal, disclose material assumptions and list only the decisions the user must make. Then wait for approval.
- Behavior: the reference, amended by D19–D21.
- Invocation: explicit only. Its own description already says "Use only when explicitly selected or invoked", so `allow_implicit_invocation: false`.
- References: none at present. `references/ko/` is optional (§6).

### 5.2 dia-elenchus (from socratic-elenchus 1.3.1)

- Purpose: Plato's elenchus. Ask "what is X?", collect agreed premises one question at a time, show contradictions, and treat each revision as the user's new idea. It usually ends in aporia and never gives advice.
- Behavior: the reference, amended by D19–D21.
- Cross-reference: "use socratic-brainstorm" becomes "use dia-brainstorm".
- Invocation: `allow_implicit_invocation: false`, as in the reference.
- References carried over: `elenchus-patterns.md` and `record-template.md`.

### 5.3 dia-brainstorm (from socratic-brainstorm 3.3.1)

- Purpose: modern Socratic questioning, one question at a time. The user lists options, the skill adds up to three labeled ones, and the user converges by criteria. It ends with a verdict and a brief, and never implements anything.
- Behavior: the reference, amended by D19–D21.
- Cross-reference: points to dia-elenchus.
- Invocation: `allow_implicit_invocation: false`, as in the reference.
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
- Cross-references: the description and body point to dia-negative and dia-elenchus.
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
    - Multi-round requests belong to dia-iterate.
  - The pointer to recursive-refine becomes a pointer to dia-iterate.
- Tool-less surfaces: the behavior is already specified. Unchecked items are marked unverified and left as drafted.
- References: none at present.

### 5.7 dia-iterate (from recursive-refine, output mode)

- Purpose: repeated review rounds, each gated by external verification. Each round names defects, assigns an external verification method, verifies, fixes only confirmed defects, locks verified items and logs the round. The loop stops on regression, zero defects, verification exhausted, fixed point, or the round cap (`--max N`, default 3).
- Required changes:
  - Remove skill mode entirely: the "Skill mode" sections, `references/skill-loop.md`, and every mention of `cp -r`, `diff -u`, subagents, `evals/` and `package_skill`. Targets are the last output, a named draft, or a file the surface can read.
  - Invocation: first word or explicit name only. Activate only when the message starts with `dia-iterate` or the skill is invoked explicitly by name. If the marker is absent but the skill looks right, ask in one line for a message starting with `dia-iterate`, or an explicit invocation of the skill by name, and stop. Explicit `/dia:dia-iterate`, `$dia:dia-iterate`, `$dia-iterate` and `@dia-iterate` also count. `allow_implicit_invocation: false`, so on the Codex plugin route only `$dia:dia-iterate` reaches it (inferred from P3).
  - Generalize tool names in `verification-sources.md`. "Context7 doc lookup" becomes "an official-documentation lookup tool (for example Context7) or a fetch of official docs".
  - Add an explicit tool-less rule: when no search, fetch or code tool is available, the only external evidence is the user's instructions and material the user supplies. Most defects are therefore unverifiable, and the loop usually stops after round 1 with the "verification exhausted" list. This is expected behavior, not a failure.
  - Keep the content-filter guardrails: a change-list output by default, no source quotations, one retry, then change the output shape.
- Pointers: single-pass requests go to dia-refine.
- References carried over: `verification-sources.md`.

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
- `metadata`: `author: ajitta`, `version`, `lineage`, `source`.
- `license: MIT` (D18).
- Body length guideline: at most 200 lines, the `superclaude` validator limit. Longer material goes in `references/`.

### 7.3 `agents/openai.yaml` (Codex / ChatGPT)

One per skill:

```yaml
interface:
  display_name: "<Display Name>"
  short_description: "<one line>"
  default_prompt: "Use $dia:dia-<x> to <action>: "
policy:
  allow_implicit_invocation: <true|false>
```

| Skill | `allow_implicit_invocation` | Reason |
|---|---|---|
| dia-intent | false | Its description says explicit only |
| dia-elenchus | false | Same as the reference |
| dia-brainstorm | false | Same as the reference |
| dia-reductio | true | Same as the reference (no yaml, default true) |
| dia-negative | true | Same as the reference (no yaml, default true) |
| dia-refine | true | Natural-language triggers are part of its design |
| dia-iterate | false | First word only by design |

`allow_implicit_invocation` defaults to `true`. When it is `false`, explicit `$skill` invocation still works ([Build skills](https://learn.chatgpt.com/docs/build-skills)).

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
├── skills/                         source: seven plain skills
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
| claude.ai web / Claude desktop | Customize › Plugins › Upload plugin with `dialectic-skills.zip`. Not Customize › Skills, which rejects a zip that carries a plugin manifest. | `/dia:dia-<x>` or natural language | owner-probed |
| Claude mobile (iOS/Android) | Install once via web or desktop; it reaches the mobile app through the account. The upload screen is not in the mobile app. | Natural language (the safe default on mobile per the owner's notes) | owner-probed |
| claude.ai marketplace | Customize › Plugins › Add marketplace `ajitta/dialectic-skills`, then add `dia` from Discover | as above | untested (marked "not yet confirmed" in the owner's notes) |
| Claude Code | `/plugin marketplace add ajitta/dialectic-skills`, then `/plugin install dia@dialectic-skills`; or account sync after a claude.ai upload | `/dia:dia-<x>`, natural language, first word for refine and iterate | documented (namespacing) / owner-probed (sync) |
| Codex CLI / IDE | `codex plugin marketplace add <path or owner/repo>`, then `codex plugin add dia@dialectic-skills`; fallback: copy `skills/dia-<x>` to `~/.agents/skills/` | `$dia:dia-<x>` (plugin) or `$dia-<x>` (copied folder), `/skills`, implicit per §7.3 | local-path plugin route probed (P3); GitHub route untested |
| ChatGPT desktop | Local plugin install (reads `.claude-plugin/marketplace.json`); fallback: `~/.agents/skills/` through Codex | `@dia-<x>`, implicit | documented in general; untested on Pro |
| ChatGPT mobile | Plugin-bundled skills are documented to work in ChatGPT on web, desktop and mobile; fallback: Codex cloud tasks on a repository that commits `.agents/skills/dia-<x>/` | `@dia-<x>`, natural language | untested: personal Skills are documented for Business, Enterprise, Healthcare and Edu, and plugin availability "depends on plan", so Pro is unconfirmed |

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

Note: the installed copies of reductio, negative-dialectics, self-refine, recursive-refine and confirm-intent carry no `license` or version field. Their provenance row records "installed copy, unversioned".

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
| P1 | claude.ai upload of `dialectic-skills.zip` | Accepted; seven skills listed as `dia:dia-<x>` |
| P2 | Claude mobile app, one natural-language prompt per skill | The right skill loads; the reply is in the prompt's language. For dia-intent the prompt names the skill, and for dia-iterate it starts with `dia-iterate` (a mid-sentence mention should produce the one-line request, not the loop); dia-elenchus and dia-brainstorm use the P7 prompts, which ask for the method by name in natural language. For dia-intent also check that the same request without the name does not load it |
| P3 | Codex CLI plugin install, with only `.claude-plugin/plugin.json` | Plugin loads; `$dia:dia-<x>` resolves (the first run showed that plugin skills are namespaced; `$dia-<x>` applies only to a copied folder); `allow_implicit_invocation: false` holds for the four explicit-only skills. If this fails, add the root `plugin.json` (§7.4), re-run, and confirm that Claude Code still loads with both manifests present |
| P4 | ChatGPT desktop (Pro), local plugin install | Skills appear under `@`; one prompt per skill routes correctly |
| P5 | ChatGPT mobile (Pro) after P4 | Skills are usable; if not, record the plan limitation and test the Codex-cloud fallback |
| P6 | First-word invocation | `dia-refine — check numbers` runs one pass; `dia-iterate` runs the loop; "please refine this paragraph" does not trigger either; a sentence mentioning dia-refine in the middle does not trigger it |
| P7 | Routing baseline, n=2 | Korean and English prompts for reductio, negative dialectics, elenchus and brainstorm. Compare against the old skills from `upstream/`. No drop allowed; on a drop, fix the English wording (L7) |
| P8 | Tool-less run | On a surface or session with no tools, `dia-iterate` stops after round 1 with a "verification exhausted" list, and `dia-refine` marks unchecked items unverified instead of changing them |
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
| O4 | ChatGPT mobile on Pro: supported route or documented limitation | Decided by P5 |
| O5 | Plugin `version`: `0.1.0` until acceptance, then `1.0.0` | At acceptance |

## 14. Sources

- Claude Code — Plugin manifest reference: https://code.claude.com/docs/en/plugins-reference
- Claude Help — Skills (zip upload, code-execution requirement): https://support.claude.com/en/articles/12512180
- OpenAI — Build plugins: https://developers.openai.com/plugins/build/plugins
- ChatGPT / Codex — Build skills: https://learn.chatgpt.com/docs/build-skills
- OpenAI Help — Plugins in ChatGPT and Codex: https://help-lb.openai.com/en/articles/20001256
- OpenAI Help — Skills in ChatGPT: https://help.openai.com/en/articles/20001066-skills-in-chatgpt
- Owner's prior work (single source): `ajitta/superclaude` at `stable` 47f791b — `portable-skills/README.md`, `portable-skills/package.py`, `docs/features/portable-skills-single-plugin/`
