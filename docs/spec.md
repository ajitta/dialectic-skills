# dialectic-skills: specification

What each skill does is defined by its `skills/<skill>/SKILL.md`, and the package by `tools/package.py` and `tests/`. Where this document disagrees with them, they hold and this document is corrected. The current state and what is open are in `docs/handoff.md`. The reason for a change is in its commit and pull request; evidence from runs stays in the batch folders outside the repository. Everything up to plugin 5.4.2 (the decision rows, the probe records, the research) is in git at the tag `v5.4.2`.

Owner: ajitta. Repository: `ajitta/dialectic-skills`.

## 1. Summary

`dialectic-skills` packages thirteen reasoning-and-review skills and `dia`, the one skill that calls them, as one plugin installed under the name `dia`. The shipped package contains instructions only: Markdown, YAML and JSON. Build and validation scripts exist only in the repository, for the developer.

## 2. Goals

- One plugin, `dia`, containing the skills named in §4.
- Each skill is a function (§3). The skills are written for claude-fable-5-2 at effort high and run on it; no other model is run, and nothing is promised or disclaimed about one.
- The package installs on Claude Code, claude.ai (web, desktop, mobile), Codex and ChatGPT: the manifests, the marketplace, both zips and `claude plugin validate --strict` hold.
- The material the first skills were rebuilt from is kept in `upstream/` as read-only provenance and never shipped.

## 3. The design

1. **A skill is a function.** Each of the thirteen opens with its purpose and is written in one order: what it is for, what it works from, what it does, what it returns. It names no other dia skill, hands nothing over and reads no other skill's state. It does the same thing wherever it is called, given the same input. "No hidden state" binds the writer, not the model: the text assumes nothing that exists only in one place, and the model uses every piece of context it has.
2. **Input is the source itself.** What a skill works from is stated as sources: the target's own text, the user's own words, the files and data. No skill carries sentences that validate its input, because a skill can only catch a hole it can see, and the costly hole (a summary in place of the original) is invisible from inside. Holes are closed on the calling side, by `dia`.
3. **Written from the purpose.** A text is written from its skill's purpose at the level of judgment the engine has, not grown case by case. Not in any text: protection of files, data or accounts; limits on sending or installing; paragraphs for a particular caller; fixed labels; lists of cases; a skill starting agents or second runs of its own. A fault shown by a run is changed at its cause in the design or left and reported, never met by a sentence for its case.
4. **Invocation is the description's gate.** `disable-model-invocation` and `allow_implicit_invocation: false` are not used, because a skill hidden from the model cannot be handed to an agent by a session that no longer knows what it needs. Every description is one line of what the skill does and then the gate (§7.2).
5. **`dia` is the one skill that calls.** It holds the contract of each of the thirteen (what to hand it, what it returns, whether it needs someone who answers), the rules for handing work to an agent, and one procedure: three critics in independent agents, chosen by where the target could be wrong, then dia-adjudicate once in an agent of its own. The thirteen do not know it. It is instructions only.
6. **Skills that hold a dialogue** (dia-skopos, dia-elenchus, dia-quaestio) take their respondent's answers as input, and the respondent may be a person or an agent. A dialogue can be continued by calling the skill again with the record so far and the new answer.
7. **The contract in two places.** The table of contracts is written once, in `dia`, and the plugin README carries the same table; a test holds them equal. No skill's reply has a fixed form.
8. **What runs of the released texts taught is kept.** A text written from the purpose alone lost behaviour that earlier runs had put into the released text, so each new text was reviewed beside the text it replaces, and two things were carried over whole. dia-elenchus is the released method (its stance, its six steps and its patterns reference, in the released wording) in the form of a function. The five skills that judge and then ask the user (dia-reductio, dia-warrant, dia-conjecture, dia-counterplan, dia-adjudicate) say at once what the evidence in hand settles and, where they put questions to the user, hold back a way out, a course and the thing made to act on until the user has replied, because what is handed over beside open questions gets used before the answers come; what they then hand over carries each question still open as its condition, an agent told that nobody will answer gets everything at once in that form, and with no question put nothing is held. Three things about its wording came from runs of the 6.0.0 texts. The condition is a fact of the conversation (the user has replied) and stands in each sentence that orders such a thing: keyed to a judgment ("as far as it turns on those questions"), or stated away from the sentence it gates, it did not hold. A question is glossed with what its answer settles and not with what it decides, which carried courses by case under the questions. And the rule that what is not known is not written as known stands at the sentence that makes the thing for the user and says where the condition goes, into the thing's own wording, because stated under "What it works from" it left the condition in a list beside the thing. dia-warrant alone names a second place for an open point, the words to send to whoever holds the answer; there what is open is put to the user before anyone else and those words are written only once the user has replied, since a first reply that asked the user nothing had nothing to hold.

Rulings on names that still bind:

- A skill name must not be a word of ordinary requests, because a message's first word starts a skill.
- The plugin name `dia`, the repository name and the `dia-` prefix stay: a rename breaks every install and invocation.
- Every description keeps the full gate sentence; a shorter gate let a request that only sounded like a skill load it.
- `short_description` in `agents/openai.yaml` is shown in a UI and not to the model, and each sample prompt in the OpenAI listing starts with a skill's name.
- The READMEs, the site, the manifests and the plugin README name no retired way to start a skill, because a removed form shown still teaches it.

## 4. Names and identifiers

| Item | Value |
|---|---|
| Repository | `ajitta/dialectic-skills` |
| Marketplace name (`.claude-plugin/marketplace.json`) | `dialectic-skills` |
| Plugin `name` (namespace prefix) | `dia` |
| Plugin `displayName` | `Dialectic Skills` |
| Upload zips | `releases/dialectic-skills.zip`, `releases/dialectic-skills-openai.zip` |
| Claude Code install | `/plugin marketplace add ajitta/dialectic-skills`, then `/plugin install dia@dialectic-skills` |

The plugin `name` is the only field that sets the namespace, so the marketplace entry uses `dia` as well.

Skills: `dia`, and the thirteen `dia-skopos`, `dia-techne`, `dia-emend`, `dia-ratchet`, `dia-regula`, `dia-negative`, `dia-reductio`, `dia-warrant`, `dia-conjecture`, `dia-counterplan`, `dia-adjudicate`, `dia-elenchus`, `dia-quaestio`.

- Each name is kebab-case and matches its folder name.
- Each of the thirteen starts with `dia-`, and none is a prefix of another, because a skill starts on the first word of a message. `dia` is a first word of its own.
- A skill is selected as `/dia:<name>` on Claude, `$dia:<name>` on Codex and `@<name>` on ChatGPT, or by a message that starts with its name.

## 5. Skills

What each skill does is in its `skills/<skill>/SKILL.md` and that skill's `references/`. They are the only description of its behaviour. By kind: dia-skopos, dia-techne, dia-emend, dia-ratchet and dia-regula do work; dia-elenchus and dia-quaestio question an idea in a dialogue; dia-reductio, dia-negative, dia-warrant, dia-conjecture, dia-counterplan and dia-adjudicate examine a position or a text; `dia` calls them. How a skill is judged is in `AGENTS.md`.

## 6. Language

- `SKILL.md`, `agents/openai.yaml`, the manifests and every file under `references/` contain no Hangul. `tools/package.py` enforces this.
- Hangul is allowed only under `skills/<skill>/references/ko/`, for context specific to Korea (statutes, institutions), never for translations; such a file starts with the lines `Scope:`, `Source:`, `As of:` and `Use when:`, and its `SKILL.md` names it. No skill ships one now.
- Descriptions carry no Hangul: a request in Korean reaches a skill by its name as the first word.
- `README.ko.md` translates `README.md`; command blocks stay identical.

## 7. Package format

### 7.1 What is shipped

The shipped package (`plugins/dia/` and both zips in `releases/`) contains only:

- `.claude-plugin/plugin.json`, or in the OpenAI zip `.codex-plugin/plugin.json`;
- `README.md`, generated from `packaging/plugin-README.md`;
- `skills/<skill>/SKILL.md`, `skills/<skill>/references/**/*.md` and `skills/<skill>/agents/openai.yaml`;
- in the OpenAI zip only, the listing images `assets/icon.svg` and `assets/logo.svg`.

It contains no `scripts/`, `bin/`, `hooks/` or monitors, no `.mcp.json` or `.lsp.json`, and no executable or non-text file. claude.ai does not install a plugin that has a top-level `bin/` directory.

### 7.2 Frontmatter

- Allowed keys: `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`. An upload to claude.ai fails on keys only Claude Code knows.
- `name` matches the folder name. `description` is at most 1024 characters: one line of what the skill does, then the gate, "Use only when the message starts with <name>, or when the skill is invoked by name; a request that only sounds like this is not an invocation." The gate of `dia` is the first word `dia` on its own.
- `metadata` holds `version` and nothing else. `license: MIT`.
- A body is at most 200 lines; longer material goes in `references/`.

### 7.3 `agents/openai.yaml`

One per skill: `interface.display_name`, `interface.short_description` (25 to 64 characters), `interface.default_prompt` starting `Use $dia:<name> `, and `policy.allow_implicit_invocation: true` for every skill (§3, item 4).

### 7.4 Manifests

- `plugin-manifest.json` is the source of `.claude-plugin/plugin.json`: `name: dia`, `displayName: Dialectic Skills`, `version`, `description`, `author`, `license`, `homepage`, `repository`, and no `skills` key.
- The OpenAI manifest exists only in `releases/dialectic-skills-openai.zip`, generated from `plugin-manifest.json` and `packaging/openai/interface.json`.
- `.claude-plugin/marketplace.json` lists one plugin: `dia` with source `./plugins/dia`. Its `renames` map sets the companion plugin retired in 6.0.0 (`dia-panel`) to `null`, and `forceRemoveDeletedPlugins` is true, which is how a marketplace takes a removed plugin off its users' machines ([Host and maintain a marketplace](https://code.claude.com/docs/en/plugins/host-marketplace)).

### 7.5 Source folders stay plain skills

`skills/<skill>/` contains no `.claude-plugin/`, `.codex-plugin/`, `skills/` or `bin/`. A manifest inside a skill folder makes Codex register it under a doubled name and makes Claude Code load it as a plugin of its own.

## 8. Repository layout

```
dialectic-skills/
├── skills/                          source: the plain skills
│   └── <skill>/
│       ├── SKILL.md
│       ├── references/*.md          optional
│       └── agents/openai.yaml
├── plugin-manifest.json             source for the plugin manifests
├── plugin-release.json              digest record for the current version (not shipped)
├── packaging/                       source: plugin README, OpenAI listing fields and images
├── .claude-plugin/marketplace.json  marketplace "dialectic-skills" -> ./plugins/dia
├── plugins/dia/                     generated, shipped (committed)
├── releases/                        generated, shipped (committed): both zips
├── tools/package.py, tests/         developer-only
├── upstream/                        read-only provenance, never shipped
├── docs/                            this specification, the handoff, the site's design notes; never shipped
├── site/                            project page (GitHub Pages)
├── README.md, README.ko.md
└── LICENSE
```

## 9. Verification

`python tools/package.py --check`, `python -m unittest discover -s tests -v` and `claude plugin validate --strict plugins/dia` pass before a release; CI runs all three. Together they check:

- the frontmatter keys, the name and the description length (§7.2), and that `metadata` holds the version only;
- that no skill name is a prefix of another (§4), and that every `dia-` name a shipped file mentions is a skill;
- that only `dia` names another skill;
- the Hangul boundary (§6) and the forbidden paths and files (§7.1);
- that `plugins/dia/` and both zips match the source byte for byte (the zips are reproducible: fixed timestamps and modes, LF line endings, stored entries);
- that changed shipped files come with a new plugin `version`, because Claude Code updates an installed plugin only when its version changes;
- that every description carries its gate, that the table of contracts in `dia` and in the plugin README are one table, and that `README.ko.md` keeps `README.md`'s structure;
- that the READMEs, the site and the manifests name no retired form.

Rules for runs are in `AGENTS.md`.

## 10. Sources

- Claude Code, plugin manifest reference: https://code.claude.com/docs/en/plugins-reference
- Claude Help, skills (zip upload, the code-execution requirement): https://support.claude.com/en/articles/12512180
- OpenAI, build plugins: https://developers.openai.com/plugins/build/plugins
- ChatGPT and Codex, build skills: https://learn.chatgpt.com/docs/build-skills
