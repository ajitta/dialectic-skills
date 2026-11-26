# Dialectic Skills (`dia`)

**English** | [한국어](README.ko.md)

Website: [ajitta.github.io/dialectic-skills](https://ajitta.github.io/dialectic-skills/)

Thirteen reasoning-and-review skills in one plugin, and `dia`, the one skill that calls them. Each skill is a function: it has one purpose, works from what it is handed, and returns one thing. None of them knows the others. The package is instructions only (Markdown, YAML, JSON). A skill starts only when your message starts with its name.

| Skill | What it is for | Hand it | It returns | Someone to answer |
|---|---|---|---|---|
| `dia-skopos` | Before any work, show what is being asked for and the result it is for, and let you choose which of the two is the request | The request in your words; the project or material it points to | A review: what would be made, the result it is for, what was found and what is assumed, what only you can decide, and the choice. It does none of the work | Yes: it stops for your word |
| `dia-techne` | Do a task for the outcome it serves, as the field's best practitioners would, checked outside the model | The request; your words on what it is for, your facts and limits; the files and data. `--aim=request` keeps to the thing asked for | The finished work, with the outcome worked to, the ways compared, what was made or changed, the methods that ran and what the check showed | No |
| `dia-emend` | Review a draft once and return one revision that fixes what is confirmed and marks what is only suspected | The draft itself (text or file), the criteria, what the draft is for, any reference to check it against | The defects found and the one revision; a file is edited in place | No |
| `dia-ratchet` | Revise in rounds that move only on evidence from outside the model, so that you know which claims were checked | The target (text or file), the criteria, what it is for, your own sources. `--max N` caps the rounds | The changes, what each round locked, why it stopped and what stays unverified. No verdict on the target | No |
| `dia-regula` | Write or review text a model follows (a prompt, instructions, a skill) against four rules | The text itself, and the old text where it was edited; your words on what it has to make a model do | A report of each breach, quoted, with the rule it breaks; or the written or revised text with any change of meaning reported | No |
| `dia-negative` | Hold a claim, plan or text against the standard it states for itself | The target in its own words, the text itself and not an account of it; the purpose it or you state for it | The judgment first (open, or holding against the cases tested), the findings firm and conditional, what the claim does against what it says it is for, options and one recommendation | No |
| `dia-reductio` | Hold a position against its own commitments: what it has to rely on, and whether all of it can be true together | The position in its own words; what its holder said or promised earlier on the matter; the files it points to; what it is for | The judgment first, the contradiction with the premises it needs, what came to the surface, and what each way out costs | No: it lists what it would have asked |
| `dia-warrant` | Hold a conclusion against the step that carries it: the rule each step runs on, and whether it holds in this case | The argument in its own words (a conclusion with its reasons), the material it points to, what the conclusion has to carry | The judgment first (how far the conclusion can be relied on), the step it turns on, the evidence, and what was at hand and not used | No: it lists what it would have asked |
| `dia-conjecture` | Hold a claim about every case against the cases that press it hardest, and repair the claim where one counts | The claim in its source's words, the records or code it covers, what rests on it | The judgment first (whether "every" stands), the deciding cases, and the repaired claim with what it no longer covers | No: it lists what it would have asked |
| `dia-counterplan` | Hold a plan against the plan its opposite assumptions give, on the same facts | The plan's text, its figures and files, what the plan is for, what you have said that settles an assumption | The judgment first (which course to take and what would change it), each assumption with its contrary, and the counterplan | No: it lists what it would have asked |
| `dia-adjudicate` | Rule on reports about a target by the evidence, check the target's own claims, and judge what is left of its conclusion | The target, the reports whole, the sources both point to, your words on what the ruling is for | The judgment first, a ruling on each point with its basis, what no report raised, and what has to change in the target | No: it lists what it would have asked |
| `dia-elenchus` | Examine the concept an idea stands on, through a definition, agreed premises, a contradiction and a revision, to bring out a fork in the respondent's own thinking | The idea in the respondent's words. To continue a dialogue: the exchange or the record so far, and the new answer | One question a message; at the end a record of the definitions, the agreed premises, the ideas born and what is still not known | Yes, a person or an agent. With none, it gives its first question only |
| `dia-quaestio` | Question an idea until its owner sees it clearly, then help them grow options and choose | The idea in its owner's words and what it is for. `stress` tests it harder; `quick` and `deep` set the length | One question a message; at the end a verdict and a brief with the options and one next step | Yes |

## Contents

- [Install](#install)
- [Starting a skill](#starting-a-skill)
- [`dia`: a target criticised and judged](#dia-a-target-criticised-and-judged)
- [Handing a skill to an agent](#handing-a-skill-to-an-agent)
- [Troubleshooting](#troubleshooting)
- [Repository layout](#repository-layout)
- [Develop](#develop)

## Install

Where you install decides where dia shows up. An install made on the web (claude.ai, chatgpt.com) is saved to your account and appears on the web and in the mobile app. An install made in a desktop app stays on that computer.

### Claude Code

```
/plugin marketplace add ajitta/dialectic-skills
/plugin install dia@dialectic-skills
```

- Update: `/plugin marketplace update dialectic-skills`, then update the plugin (or turn on auto-update for the marketplace).
- Uninstall: `/plugin uninstall dia@dialectic-skills`.
- A plugin you added on claude.ai also syncs into Claude Code when you sign in with the same account. Do not install it a second time from the command line.

### claude.ai web, Claude desktop and mobile

1. Settings › Capabilities: turn on **Code execution and file creation**. Skills need it.
2. Customize › Plugins › Add › Add marketplace, and enter `ajitta/dialectic-skills`.
3. In Customize › Plugins, open Discover, select `dia` (Dialectic Skills), and select Add.
4. Type `/dia` in the message box. Fourteen entries should appear: the thirteen skills and `dia:dia`.

Instead of steps 2 and 3 you can upload [`dialectic-skills.zip`](https://github.com/ajitta/dialectic-skills/releases/latest/download/dialectic-skills.zip) from the latest release with Customize › Plugins › Add › Upload plugin. An upload does not update itself.

Claude desktop installs on that computer only. The mobile app has no install step: a plugin added on claude.ai reaches it through your account. Its `/` menu does not list plugin skills, so start the message with the skill's name.

### Codex and ChatGPT

```
codex plugin marketplace add ajitta/dialectic-skills
codex plugin add dia@dialectic-skills
```

For ChatGPT on the web and mobile, upload [`dialectic-skills-openai.zip`](https://github.com/ajitta/dialectic-skills/releases/latest/download/dialectic-skills-openai.zip) from the latest release on chatgpt.com. In the ChatGPT desktop app, add the marketplace `ajitta/dialectic-skills` and install `dia` from its plugin list; that install stays on the computer.

## Starting a skill

Start the message with the skill's name: `dia-reductio Remote work always raises productivity.` A message that only asks for a skill's method in words ("use proof by contradiction on ...") starts no skill.

A skill can also be selected the way each surface selects one:

| Surface | Syntax | Example |
|---|---|---|
| claude.ai, Claude desktop, Claude Code | `/dia:dia-<x>` | `/dia:dia-reductio` |
| Codex | `$dia:dia-<x>` followed by a space | `$dia:dia-skopos write a backup script` |
| ChatGPT | `@` then pick the skill | `@dia-negative` |

What follows the name is what the skill works from: the claim, the plan, the draft, a path to a file, your words on what it is for. The table at the top says what each skill needs. A few skills read an option from the request:

- `--aim=request` (`dia-techne`): keep to the thing asked for instead of working for the outcome behind it.
- `--max N` (`dia-ratchet`): the round cap, three where none is given.
- `stress`, `quick`, `deep` (`dia-quaestio`): test the idea harder, or set the length of the dialogue.

`dia-skopos`, `dia-elenchus` and `dia-quaestio` hold a dialogue: they ask and wait for your answer. The others give their whole result in one reply and list what only you can answer as questions, each with what its answer decides.

## `dia`: a target criticised and judged

`dia` is the skill that calls the others.

- **`dia` alone** loads the table above and the rules for handing work to an agent. They hold for the rest of the conversation.
- **`dia` with a skill's name, or with a request for work that one skill's row describes,** runs that skill and says in a line which and why.
- **`dia` with a target and no skill asked for** (`dia docs/plan.md`, or `dia` and a pasted claim) has the target criticised by three independent agents and judged by a fourth. The session gathers the target, the sources it points to and everything you said about it; picks three critics by the kinds of fault this target could have (a dia skill where one fits, or an agent briefed for the occasion); starts them apart from each other; then hands the target, the sources, your words and the three reports whole to `dia-adjudicate` in its own agent. You get the judge's reply as the judge gave it.
- **You may name the critics:** `dia docs/plan.md with dia-counterplan, dia-warrant and a security reviewer`.

Where agents cannot be started, `dia` says so: criticisms made inside one conversation are not independent of each other.

## Handing a skill to an agent

An agent sees nothing of your conversation. What it is not handed it fills with a guess, and the guess comes back looking like a finding. `dia` holds these rules, and they are worth following by hand as well:

- Hand the agent the sources themselves (the target as a path or its whole text, the files it rests on), never a summary.
- What only the conversation holds goes in word for word and marked as whose it is: what the target is for, a fact you stated, a limit you set. If your words also ask for what the session itself is doing (several critics, a verdict), the brief says which place in it the agent has.
- Give it none of the session's own view of the target.
- Begin its brief with the skill's name alone on the first line, and ask for the skill's whole reply as its last message.
- Tell it that nobody will answer its questions, so that what it would have asked comes back listed as open. A skill that holds a dialogue is the exception: its answers are passed to it one at a time, by continuing its agent or by starting it again with the exchange so far.
- Pass its report on whole.

## Troubleshooting

- **A skill did not start.** A request in plain words starts no dia skill. Start the message with the skill's full name.
- **`dia` followed by a text did something unexpected.** `dia` with a target and no skill asked for has the target criticised by three agents and judged by a fourth. To run one skill, start the message with that skill's name.
- **`Repository not found` when adding the marketplace.** Check the spelling: `ajitta/dialectic-skills`.
- **Every skill appears twice.** The plugin is installed through two routes (an upload and a marketplace, for example). Remove one.
- **dia works on one device but not on another.** Desktop installs stay on that computer; web installs are saved to your account and reach the mobile app.
- **Skills section missing or greyed out on claude.ai.** Turn on Settings › Capabilities › Code execution and file creation.

## Repository layout

```
skills/<skill>/                 source: plain skills (SKILL.md, references/, agents/openai.yaml)
plugin-manifest.json            source for .claude-plugin/plugin.json
packaging/plugin-README.md      source for plugins/dia/README.md
packaging/openai/               OpenAI directory listing fields and images
plugin-release.json             content digest for the current version (not shipped)
.claude-plugin/marketplace.json marketplace "dialectic-skills" -> ./plugins/dia
plugins/dia/                    generated, shipped
releases/dialectic-skills.zip   generated, shipped (top-level folder dia/)
releases/dialectic-skills-openai.zip
                                generated, OpenAI directory upload
tools/package.py                validate and build (developer-only)
tests/                          developer-only
upstream/                       material the seven original skills were rebuilt from; never shipped
docs/spec.md                    the package rules
docs/handoff.md                 the current state and what is open
```

## Develop

```bash
python tools/package.py            # validate, write plugins/dia/ and the zips
python tools/package.py --check    # validate; fail if the committed output lags the source
python -m unittest discover -s tests -v
claude plugin validate --strict plugins/dia
```

Edit `skills/`, never the generated output. Any change to a shipped file needs a new `version` in `plugin-manifest.json`, and a changed skill a new `metadata.version`. When this README changes, update `README.ko.md` in the same commit; a test checks that it keeps the same structure.

## License

MIT
