# Dialectic Skills (`dia`)

**English** | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

Seven reasoning-and-review skills in one plugin, written to run unchanged on any assistant that loads Agent Skills: Claude (web, desktop, mobile, Claude Code), Codex and ChatGPT. The package is instructions only (Markdown, YAML, JSON), so every skill also works in a chat with no tools. Skill files are in English; each skill replies in the language of your message.

| Skill | What it does | How it starts |
|---|---|---|
| `dia-confirm` | Before work starts: restates the goal, discloses material assumptions, lists only the decisions you must make, then waits for your approval. | by name only |
| `dia-elenchus` | Plato's elenchus: "what is X?", premises agreed one question at a time, contradictions shown, each revision is your new idea. Usually ends in aporia; gives no advice. | by name, or by asking for a Socratic dialogue |
| `dia-brainstorm` | Modern Socratic questioning one question at a time, then your options plus up to three labeled ones, convergence by criteria, a verdict and a brief. Never implements. | by name, or by asking for a Socratic brainstorm |
| `dia-reductio` | Strict reductio ad absurdum in one pass: labeled premises, a Q and not-Q derivation with a rule per line, graded strength, options and a record. | by name, or in words |
| `dia-negative` | Internal critique (narrower than Adorno's immanent critique) in one pass: the target's own standard, strict gaps with cases and "what escapes", the operative purpose with a falsifier, options without forced synthesis. | by name, or in words |
| `dia-refine` | One review pass over the last answer or a draft: factual errors, logical leaps, missing requirements, repetition. Fixes only confirmed defects. | first word `dia-refine`, or by name |
| `dia-iterate` | Repeated review rounds, each gated by external verification; stops on regression, zero defects, verification exhausted, fixed point or `--max N` (default 3). | first word `dia-iterate`, or by name only |

## Contents

- [Quick start](#quick-start)
- [Install](#install)
- [How to invoke](#how-to-invoke)
- [Examples](#examples)
- [Using several skills together](#using-several-skills-together)
- [Troubleshooting](#troubleshooting)
- [Repository layout](#repository-layout)
- [Develop](#develop)
- [License](#license)

## Quick start

Claude Code:

```
/plugin marketplace add ajitta/dialectic-skills
/plugin install dia@dialectic-skills
```

Codex CLI:

```
codex plugin marketplace add ajitta/dialectic-skills
codex plugin add dia@dialectic-skills
```

claude.ai: Customize › Plugins › Add › Add marketplace, enter `ajitta/dialectic-skills`, then add `dia` from the list.

Then try: `Use proof by contradiction on this claim: remote work always raises productivity.`

## Install

Install through one route per account or machine. Two routes (for example this repository and the [ajitta/claude-plugins](https://github.com/ajitta/claude-plugins) catalog) give you every skill twice.

### claude.ai web and Claude desktop

1. Settings › Capabilities: turn on **Code execution and file creation**. Skills need it, even though no dia skill runs code.
2. Customize › Plugins › Add, then either:
   - **Add marketplace** with `ajitta/dialectic-skills`, then add `dia` from the list. Instead of `ajitta/dialectic-skills` you can enter the Git URL `https://github.com/ajitta/dialectic-skills.git`, and Claude desktop also accepts a local folder (a clone of this repository). Adding the marketplace alone installs nothing; the second step is needed. Updates arrive through the marketplace (Check for updates, or Sync automatically).
   - **Upload plugin** with [`dialectic-skills.zip`](https://github.com/ajitta/dialectic-skills/releases/latest/download/dialectic-skills.zip) from the latest release. Use Customize › Plugins, not Customize › Skills: the Skills screen rejects a zip that carries a plugin manifest. An upload does not update itself; upload each new release again.
3. Check: type `/dia` in the message box. Seven entries, `dia:dia-brainstorm` to `dia:dia-refine`, should appear.

### Claude mobile (iOS, Android)

There is no install step. A plugin added on claude.ai or Claude desktop belongs to your account and reaches the mobile app by itself. The mobile `/` menu does not list plugin skills; ask in words or name the skill in your message.

### Claude Code

```
/plugin marketplace add ajitta/dialectic-skills
/plugin install dia@dialectic-skills
```

- Update: `/plugin marketplace update dialectic-skills`, then update the plugin (or turn on auto-update for the marketplace).
- Uninstall: `/plugin uninstall dia@dialectic-skills`.
- A plugin you added on claude.ai also syncs into Claude Code when you sign in with the same account. Do not install it a second time from the command line.
- Through the catalog instead: `/plugin marketplace add ajitta/claude-plugins`, then `/plugin install dia@ajitta`. Same code, different install name.

### Codex app, CLI and IDE

```
codex plugin marketplace add ajitta/dialectic-skills
codex plugin add dia@dialectic-skills
```

- Codex app (desktop): add a plugin marketplace from a GitHub repository (`ajitta/dialectic-skills`), a Git URL (`https://github.com/ajitta/dialectic-skills.git`) or a local folder (a clone of this repository), then install `dia` from it. The CLI commands above do the same.
- Update: `codex plugin marketplace upgrade` refreshes the marketplace; `codex plugin list` shows the installed version.
- Without the plugin: copy `skills/dia-<x>/` folders into `~/.agents/skills/`. Skills copied this way are named `$dia-<x>` instead of `$dia:dia-<x>`.

### ChatGPT desktop and mobile

On a Pro plan the owner has run the skills on ChatGPT desktop and mobile. The exact install route depends on your plan and workspace:

- through Codex in the ChatGPT desktop app or the Codex app (the Codex marketplace routes above), or
- on Business and Enterprise workspaces, through the workspace's plugin admin (upload the zip or import the GitHub marketplace).

Skills bundled in a plugin are then available in ChatGPT on desktop, web and mobile, where your plan allows plugins.

### Windows

All routes above work on Windows. The skills contain no scripts, so no Python or shell setup is needed.

### Moving from earlier versions

- **From 1.0.0:** `dia-intent` is now `dia-confirm` (1.1.0). Call it by the new name. A marketplace install picks the change up on update; an uploaded zip must be removed and the new one uploaded.
- **From the owner's earlier standalone skills:** remove the old copies first, or each method loads twice under two names. On claude.ai: Customize › Skills, remove `reductio`, `negative-dialectics`, `self-refine`, `recursive-refine` and `confirm-intent`; Customize › Plugins, remove `socratic`. In Claude Code: `/plugin uninstall socratic@ajitta-socratic`, and remove copies under `~/.claude/skills/`. For Codex and ChatGPT desktop: remove old copies under `~/.agents/skills/`.

## How to invoke

There are three ways, and every surface supports at least one of them:

1. **In words.** Ask for the method: "use proof by contradiction on…", "do an immanent critique of…", "Socratic dialogue please…". This works on every surface and is the safe default on mobile. It works for `dia-reductio`, `dia-negative`, `dia-elenchus` and `dia-brainstorm`.
2. **By name in the message.** Start the message with the skill name: `dia-confirm …`, `dia-refine …`, `dia-iterate …`. `dia-refine` and `dia-iterate` are meant to start this way or by an explicit selection: `dia-iterate` never starts from a plain request, and on Claude Code a plain "fix this draft" request rarely loads `dia-refine`.
3. **Explicit selection**, written differently on each surface:

| Surface | Syntax | Example |
|---|---|---|
| claude.ai, Claude desktop, Claude Code | `/dia:dia-<x>` | `/dia:dia-reductio` |
| Codex (plugin) | `$dia:dia-<x>` followed by a space | `$dia:dia-confirm write a backup script` |
| Codex (copied folder) | `$dia-<x>` | `$dia-refine` |
| ChatGPT | `@` then pick the skill | `@dia-negative` |

On Codex, `dia-confirm`, `dia-elenchus`, `dia-brainstorm` and `dia-iterate` never start on their own; select them with `$dia:dia-<x>`. `dia-reductio`, `dia-negative` and `dia-refine` may also start when your request matches them.

### Options

Options can be written as flags or in plain words, in any language:

- `--target=user|claude|text|all` (`dia-reductio`, `dia-negative`): what is examined. `user` is a claim you state, `claude` is the assistant's own earlier answer (on every assistant), `text` is a pasted text, `all` is each of those present. Without the flag the skill infers the target and states it in the first line.
- `--max N` (`dia-iterate`): the round cap, default 3.
- Mode and depth (`dia-brainstorm`): `develop` (default) or `stress` ("poke holes"), and `quick`, `standard` (default) or `deep`.
- Criteria (`dia-refine`, `dia-iterate`): anything after the name, for example `dia-refine — check the numbers` or `dia-refine for tone`.

## Examples

The prompts below are in English; the same requests work in any language, and the reply follows the language you write in. Output descriptions are shortened.

### dia-confirm: agree on the task before work starts

```
dia-confirm Write a script that renames all my photos by date.
```

You get four short sections and no work yet:

- **Goal and success conditions:** what will be built and how you can tell it is done.
- **Evidence and assumptions:** what the assistant checked and what it assumed (for example, that the date comes from the photo's metadata).
- **Decisions needed from the user:** only what you must decide (operating system, subfolders, which date to use).
- **Confirmation:** what to reply to proceed.

Reply with your answers and "proceed". Corrections plus "proceed" count as approval of the corrected task; corrections alone get a revised review. The skill applies to that task and its direct follow-ups only.

### dia-elenchus: test what you mean by a word

```
Socratic dialogue please, make me define it first. I want to build a lunch-menu recommendation app.
```

The assistant asks one short question per message, for example what a "good recommendation" is. It argues only from what you agreed to, and when two of your statements cannot both stand it shows them side by side and asks which you would change. It gives no advice during the dialogue. It ends when you stop, when you run out of definitions (aporia), or when a definition survives several tests, and then prints a record with the result: aporia, holding (provisional), partly tested, or stopped before testing.

### dia-brainstorm: grow an idea by questions, then decide

```
Socratic brainstorm with me: I need a weekend side-project idea. Keep it quick.
```

One question per message while the idea is probed (about 4 questions for `quick`, 8–10 for `standard`). Then your own options plus up to three labeled suggestions, a comparison by the criteria you set, a verdict, and an optional brief. It never writes code or acts. Say "stop" or "wrap up" at any point to jump to the verdict.

### dia-reductio: find a contradiction

```
Use proof by contradiction on this claim: remote work always raises productivity.
```

One response with the whole chain: the thesis; every premise labeled by source ([T] stated by the target, [L] a law of logic or mathematics, [A] added by the assistant, such as an unstated assumption, definition or fact); numbered derivation lines that each name their rule; the contradiction Q and not-Q with its strength; the premises you could give up; one recommendation; and a record. The assistant does not decide for you. To test its own previous answer: `--target=claude`, or "check your last answer by contradiction".

### dia-negative: hold a claim to its own standard

```
Do an immanent critique of this claim: our company is flat, so anyone can speak up freely.
```

The claim's own standard, quoted; findings where what it claims and what it delivers come apart, each with a particular case; what the claim leaves out; what it actually does, stated as an inference you can check, with an observation that would prove it wrong; then options, one recommendation, and a record. It does not force a new master definition. For what code, a command or a setting does, or for a general review, ask normally instead.

### dia-refine: one review pass

```
dia-refine check the facts: Mount Everest is the second-highest mountain, so it gets the most climbers.
```

A defect list in four parts (① confirmed errors, ② missing requirements, ③ correct content kept, ④ remaining uncertainty), then one revised version. Only defects with a confirmed basis are fixed: a tool that ran, your instructions or material, or the assistant's own re-derivation. Suspected errors it could not confirm are listed under ④ with the suspected correction instead of being changed silently. Without a draft, "do this task the dia-refine way" writes an answer, checks it once, and shows only the final version.

### dia-iterate: several rounds, each checked

```
dia-iterate --max 2 check the dates and figures in your last answer
```

Each round names defects, settles each one by an external check (search, a tool run, a source you supplied), fixes only the confirmed ones and locks what passed. The loop stops on regression, when no defects remain, when verification runs out, at a fixed point, or at the round cap, and reports the changes, a round summary and anything left unverified. In a chat with no tools it stops after round 1 with the list of items it could not verify. A mid-sentence mention of `dia-iterate` does not start the loop; the assistant asks for a message that starts with the name.

## Using several skills together

- **`dia-elenchus` and `dia-brainstorm` in one request:** the definition dialogue comes first and the first message says so; brainstorming starts when you ask for options or the dialogue ends. The two are never interleaved.
- **`dia-refine` and `dia-iterate` in one request:** they run as two separate passes with separate outputs. The refine pass's own re-derivation does not count as verification for an iterate round.
- **`dia-reductio` and `dia-negative` in one request:** both run and both answers are complete, which makes for long output (around 9,000 characters in tests). On a phone, ask for one at a time.
- **After `dia-elenchus`:** if you then ask for advice, the assistant says the Socratic part is over and labels each suggestion as its own. For a full options-and-plan session, name `dia-brainstorm` and it takes the record from there.

## Troubleshooting

- **`Repository not found` when adding the marketplace.** Check the spelling: `ajitta/dialectic-skills` (dialectic, not dialectric). The repository is public and needs no GitHub login.
- **No dia skills under `/` on Claude mobile.** Expected: the mobile menu does not list plugin skills. Ask in words or start the message with the skill name.
- **Every skill appears twice.** The plugin is installed through two routes (for example `dia@dialectic-skills` and `dia@ajitta`, or an upload and a marketplace). Remove one.
- **Skills section missing or greyed out on claude.ai.** Turn on Settings › Capabilities › Code execution and file creation.
- **`dia-intent` is not found.** It was renamed `dia-confirm` in 1.1.0.
- **`dia-iterate` does not start.** It starts only when `dia-iterate` is the first word of the message or when it is selected explicitly (`/dia:dia-iterate`, `$dia:dia-iterate`, `@dia-iterate`).
- **`$dia:dia-confirm:` does not resolve on Codex.** Put a space, not a colon, after the skill name.
- **The upload is rejected on claude.ai.** Use Customize › Plugins › Upload plugin, not Customize › Skills.

Which routes have been verified, and how, is recorded in [docs/probes.md](docs/probes.md).

## Repository layout

```
skills/dia-<x>/                 source: plain skills (SKILL.md, references/, agents/openai.yaml)
plugin-manifest.json            source for .claude-plugin/plugin.json
plugin-release.json             content digest for the current version (not shipped)
.claude-plugin/marketplace.json marketplace "dialectic-skills" -> ./plugins/dia
plugins/dia/                    generated, shipped
releases/dialectic-skills.zip   generated, shipped (top-level folder dia/)
tools/package.py                validate and build (developer-only)
tests/                          developer-only
upstream/                       material the skills were rebuilt from; never shipped
README.<lang>.md                translations of this file (not shipped)
docs/spec.md                    specification
docs/probes.md                  surface and routing probe results
docs/token-cost.md              measured token cost per skill
docs/skill-effect.md            each skill against no skill, blind-judged
```

## Develop

```bash
python tools/package.py            # validate, write plugins/dia/ and the zip
python tools/package.py --check    # validate; fail if the committed output lags the source
python -m unittest discover -s tests -v
claude plugin validate --strict plugins/dia
```

Edit `skills/`, never the generated output. Any change to a skill file needs a new `version` in `plugin-manifest.json` (and the skill's `metadata.version`): Claude Code updates an installed plugin only when the version changes, and the check fails otherwise. In the shipped package, Hangul is allowed only under `skills/<skill>/references/ko/`. When this README changes, update the translations in the same commit; a test checks that they keep the same structure.

## License

MIT
