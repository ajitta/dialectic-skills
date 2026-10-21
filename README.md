# Dialectic Skills (`dia`)

**English** | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

Website: [ajitta.github.io/dialectic-skills](https://ajitta.github.io/dialectic-skills/)

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
- [Skill guide with examples](#skill-guide-with-examples)
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

claude.ai (web): Customize › Plugins › Add › Add marketplace with `ajitta/dialectic-skills`, then Discover › `dia` › Add. This reaches the web and the mobile app. Step by step below.

Then try: `Use proof by contradiction on this claim: remote work always raises productivity.`

## Install

**Where you install decides where dia shows up.** An install made on the web (claude.ai, chatgpt.com) is saved to your account and appears on the web and in the mobile app. An install made in a desktop app (Claude desktop, Codex in the ChatGPT desktop app) stays on that computer. To use dia everywhere, install it once on the web and once in each desktop app you use; the owner runs it this way.

### claude.ai web and Claude desktop

1. Settings › Capabilities: turn on **Code execution and file creation**. Skills need it, even though no dia skill runs code.
2. **Add the marketplace.** Customize › Plugins › Add › Add marketplace, and enter:

   ```
   ajitta/dialectic-skills
   ```

   The Git URL `https://github.com/ajitta/dialectic-skills.git` works too, and Claude desktop also accepts a local folder (a clone of this repository). Copy the name rather than typing it: a misspelling such as `dialectric` fails with "Repository not found".
3. **Add the plugin.** Adding the marketplace installs nothing yet. In Customize › Plugins, open Discover, select `dia` (Dialectic Skills), and select Add.
4. **Check.** Type `/dia` in the message box. Seven entries, `dia:dia-brainstorm` to `dia:dia-refine`, should appear. Updates arrive through the marketplace (Check for updates, or Sync automatically).

Instead of steps 2 and 3 you can upload the plugin: Customize › Plugins › Add › Upload plugin with [`dialectic-skills.zip`](https://github.com/ajitta/dialectic-skills/releases/latest/download/dialectic-skills.zip) from the latest release. Use Customize › Plugins, not Customize › Skills: the Skills screen rejects a zip that carries a plugin manifest. An upload does not update itself; upload each new release again.

**Claude desktop:** the same Customize › Plugins screens install dia on that computer only. In the owner's tests, a plugin added in Claude desktop did not reach the mobile app, and one added on claude.ai did not appear in Claude desktop. If you use both, install in both places.

### Claude mobile (iOS, Android)

There is no install step. A plugin added on claude.ai (the web) is saved to your account and reaches the mobile app by itself; one added in Claude desktop does not. The mobile `/` menu does not list plugin skills, but typing the full name still starts one, for example `/dia-brainstorm`. You can also ask in words or start the message with the skill name.

### Claude Code

```
/plugin marketplace add ajitta/dialectic-skills
/plugin install dia@dialectic-skills
```

- Update: `/plugin marketplace update dialectic-skills`, then update the plugin (or turn on auto-update for the marketplace).
- Uninstall: `/plugin uninstall dia@dialectic-skills`.
- A plugin you added on claude.ai also syncs into Claude Code when you sign in with the same account. Do not install it a second time from the command line.
- Through the catalog instead: `/plugin marketplace add ajitta/claude-plugins`, then `/plugin install dia@ajitta`. Same code, different install name.

### Codex CLI and IDE

```
codex plugin marketplace add ajitta/dialectic-skills
codex plugin add dia@dialectic-skills
```

- Update: `codex plugin marketplace upgrade` refreshes the marketplace; `codex plugin list` shows the installed version.
- Without the plugin: copy `skills/dia-<x>/` folders into `~/.agents/skills/`. Skills copied this way are named `$dia-<x>` instead of `$dia:dia-<x>`.

### ChatGPT desktop (with Codex) and mobile

There are two routes. Use the first for the web and mobile, the second for the desktop app; the owner uses both.

1. **Upload the zip on the web (web and mobile).** Download [`dialectic-skills-openai.zip`](https://github.com/ajitta/dialectic-skills/releases/latest/download/dialectic-skills-openai.zip) from the latest release and upload it on chatgpt.com with the plugin zip upload. The plugin is saved to your account, so it appears on ChatGPT web and mobile. This zip carries the ChatGPT listing (descriptions, starter prompts, logo). An upload does not update itself; upload each new release again.
2. **Add the marketplace in the desktop app (this computer only).** Codex is part of the ChatGPT desktop app. Add a marketplace from a GitHub repository (`ajitta/dialectic-skills`), a Git URL (`https://github.com/ajitta/dialectic-skills.git`) or a local folder (a clone of this repository), then select `dia` in its plugin list and install it. This installs into the desktop app's local Codex folder and is not saved to your account, so it does not appear on mobile or the web. Updates arrive through the marketplace.

On Business and Enterprise workspaces, an admin can also add the plugin for the whole workspace (upload the zip or import the GitHub marketplace).

### Windows

All routes above work on Windows. The skills contain no scripts, so no Python or shell setup is needed.

## How to invoke

There are three ways, and every surface supports at least one of them:

1. **In words.** Ask for the method: "use proof by contradiction on…", "do an immanent critique of…", "Socratic dialogue please…". This works on every surface and is the safe default on mobile. It works for `dia-reductio`, `dia-negative`, `dia-elenchus` and `dia-brainstorm`.
2. **By name in the message.** Start the message with the skill name: `dia-confirm …`, `dia-refine …`, `dia-iterate …`. Since 1.2.0 this also works on Codex without `$` (probed) and is expected to work on ChatGPT without `@` (owner check pending), which would make it the quickest route on a phone. `dia-refine` and `dia-iterate` are meant to start this way or by an explicit selection: `dia-iterate` never starts from a plain request, and on Claude Code a plain "fix this draft" request rarely loads `dia-refine`.
3. **Explicit selection**, written differently on each surface:

| Surface | Syntax | Example |
|---|---|---|
| claude.ai, Claude desktop, Claude Code | `/dia:dia-<x>` | `/dia:dia-reductio` |
| Claude mobile | `/dia-<x>` or `/dia:dia-<x>` typed in full (the `/` menu does not list it) | `/dia-brainstorm`, `/dia:dia-brainstorm` |
| Codex (plugin) | `$dia:dia-<x>` followed by a space | `$dia:dia-confirm write a backup script` |
| Codex (copied folder) | `$dia-<x>` | `$dia-refine` |
| ChatGPT | `@` then pick the skill | `@dia-negative` |

Since 1.2.0 every skill is visible to the model on Codex (probed) and, by the same setting, on ChatGPT, as on Claude. `dia-reductio`, `dia-negative`, `dia-elenchus`, `dia-brainstorm` and `dia-refine` may start when your request matches them; `dia-confirm` and `dia-iterate` are meant to start only when the message begins with their name or when you select them (`$dia:dia-<x>`, `@`). On Codex, a request that spells out `dia-confirm`'s steps ("restate my goal and list the open decisions first") can also load it.

### Options

Options can be written as flags or in plain words, in any language:

- `--target=user|claude|text|all` (`dia-reductio`, `dia-negative`): what is examined. `user` is a claim you state, `claude` is the assistant's own earlier answer (on every assistant), `text` is a pasted text, `all` is each of those present. Without the flag the skill infers the target and states it in the first line.
- `--max N` (`dia-iterate`): the round cap, default 3.
- Mode and depth (`dia-brainstorm`): `develop` (default) or `stress` ("poke holes"), and `quick`, `standard` (default) or `deep`.
- Criteria (`dia-refine`, `dia-iterate`): anything after the name, for example `dia-refine — check the numbers` or `dia-refine for tone`.

## Skill guide with examples

You don't need any background in philosophy to use these skills. Each one is a way of thinking that people have used for a long time, turned into a routine the assistant follows step by step. Below, each skill gets a plain-language explanation, a prompt to try, and a real session, shortened.

The sessions were run on Claude Code (Sonnet) with this plugin, and the user replies in the two dialogue examples came from a simulated user, not a scripted one. The wording you get will differ from run to run. Every prompt works in any language, and the assistant replies in the language you write in.

**Pick a skill by what you want to do**

| You want to… | Use |
|---|---|
| make sure the assistant understood the task before it starts | `dia-confirm` |
| find out what you really mean by a word or an idea | `dia-elenchus` |
| turn a rough idea into options and a plan | `dia-brainstorm` |
| check whether a claim holds together | `dia-reductio` |
| see whether a slogan, policy or promise lives up to its own words | `dia-negative` |
| fix the mistakes in an answer or a draft, once | `dia-refine` |
| fact-check something thoroughly, round by round | `dia-iterate` |

### dia-confirm: agree on the task before work starts

**In plain words.** Before a contractor starts work, a good one walks you through the job: here is what I'll build, here is what I'm assuming, here is what only you can decide. `dia-confirm` makes the assistant do that, and then wait for your go-ahead instead of guessing.

**Use it when** a request is short but the result depends on things only you know: a speech, a plan, a script, an email to someone important. **Skip it** for quick questions with one obvious answer.

**Try:**

```
dia-confirm Write a short speech for my brother's wedding.
```

**What a session looks like** (shortened):

> **Assistant:**
> **Goal and success conditions:** a short wedding speech about your brother, ready to read aloud, about 1–2 minutes, warm, with a toast.
> **Evidence and assumptions:** nothing tells me about your brother or the couple. I'm assuming he's the groom, the tone is warm with light humor, and it's in English.
> **Decisions needed from the user:** 1. names; 2. one or two real details, such as a shared memory; 3. tone; 4. anything to avoid. Without these I'd have to write a generic speech with placeholders.
> **Confirmation:** reply "proceed" with your answers, or tell me to use a generic template.
>
> **You:** My brother is Minho, marrying Sara; I'm the best man. He taught me to ride a bike, even though he's younger. Warm, one light joke, about 3 minutes. proceed
>
> **Assistant:** Here's your speech, about 400 words… *(the speech follows, built around the bike story)* …Notes: I invented small details of the story; change any that don't match what really happened.

**Tips**

- Answer only the questions you care about and add "proceed". Corrections plus "proceed" count as approval of the corrected task.
- "Looks good", silence or a thumbs-up do not count as approval; the assistant keeps waiting.
- It covers that one task and its direct follow-ups. Start a new task with `dia-confirm` again if you want the same check.

### dia-elenchus: find out what you really mean

**In plain words.** This is the method Socrates uses in Plato's dialogues. You say what you think something is ("a good teacher is…"). The assistant doesn't argue back or give its own view. It asks about one concrete case at a time, and each case is chosen so that your own answers start to pull against your definition. You then fix the definition in your own words. Often you end up stuck, and the Greek word for that is **aporia**. Being stuck is a result here, not a failure: you now know exactly which part you don't know, so you won't build on a wrong assumption.

**Use it when** you rely on a word that feels obvious but drives real decisions: a good teacher, a fair split, a successful project, a healthy relationship. **Not for** getting advice; it gives none during the dialogue.

**Try:**

```
Socratic dialogue please. I think a good teacher is one whose students get high test scores.
```

**What a session looks like** (real run, shortened):

> **Assistant:** I don't know what makes a good teacher, so I'll test your definition. Suppose a teacher gives the students the exam questions and answers the day before, and they all score high. Is that a good teacher?
>
> **You:** No, that's basically cheating. Maybe a good teacher is one whose students get high scores *because they actually learned the material*.
>
> **Assistant:** Your wording has shifted from "high test scores" to "high scores because they actually learned the material." Now take a teacher whose students really did learn, but the test was badly made, so the scores came out low. Is that a good teacher?
>
> **You:** Yes, the bad test is the test's fault. So scores aren't really what makes a teacher good.
>
> **Assistant:** … Take a class where every student learned everything, but entirely on their own, from a book and a private tutor. The teacher contributed nothing. Is that a good teacher?
>
> **You:** No. So a good teacher is one whose teaching actually helps the students learn.
>
> *…three more cases: a teacher whose students skip class, two equally clear teachers with different classes, a teacher who tries everything and nothing works…*
>
> **Assistant:** Earlier you called the teacher with the skipping students still good. Were those students "reasonably able to take part"?
>
> **You:** They could have, they just chose not to, so by my new idea that teacher isn't good. That contradicts what I said earlier. I'm stuck. Where does that leave me?
>
> **Assistant:** You've reached aporia, and that's a result, not a failure. Whether a good teacher is defined by what the students end up learning or by what the teacher does is still open for you… *(then a record: how your definition changed, the premises you agreed to, what you now know you don't know, and a question to take away; result: aporia)*

**Tips**

- Short, honest answers work best. "I'm not sure" is a fine answer.
- When it points out a "shift", it is only showing you how your wording changed. You decide what to keep.
- Say "stop" at any time to get the record. If you then want suggestions, ask; the assistant will say the Socratic part is over and label its ideas as its own.

### dia-brainstorm: grow a rough idea, then decide

**In plain words.** A coach who asks you good questions before handing you options. First it asks one question at a time to pin down what you want and what you know (Socratic questioning). Then you list options, it adds a few of its own, you choose what matters, and it ends with a verdict and a short brief you can act on. Unlike `dia-elenchus`, it does give suggestions, after the questions.

**Use it when** you have a goal but no plan yet: a side income, a career move, a small project, a trip. **Not for** building the thing; it never writes code or acts.

**Try:**

```
Socratic brainstorm with me, keep it quick: I want to earn some extra money on weekends.
```

**What a session looks like** (real run, shortened):

> **Assistant:** Quick mode, about 4 questions. Your idea is to earn some extra money on weekends, alongside your current job. Is that right, or did I assume something you didn't mean?
>
> **You:** Right. About 8 hours each weekend, roughly $300 a month, no more than $200 to start.
>
> **Assistant:** Eight hours a weekend is about 32 hours a month, so $300 comes to about $9 an hour. What do you already know how to do that someone would plausibly pay for?
>
> **You:** I'm good at photography and own a decent camera. Maybe photos for small local shops.
>
> **Assistant:** Compliments are a good sign, but nobody has paid you yet, so the biggest unknown is whether a shop would… Suppose you approach shops over the next few weekends. What would you have to see to decide this isn't working?
>
> **You:** If I pitch about 10 shops over three weekends and none say yes to even a cheap trial shoot, I'd call it not working.
>
> *…you add more options (prints at weekend markets, stock photos, headshots, a "pet photo morning"); the assistant adds its own (second shooter at weddings, a beginner photo walk, do nothing); you pick three criteria: low startup cost, about $300 without much unpaid editing, and enjoying the work…*
>
> **Assistant:** **Verdict: open.** The idea held up where I tested it, but the central assumption, that someone will pay you for these photos, hasn't been tested yet… **Next step:** this week, post in two neighborhood groups offering 3–4 park slots, and track bookings, price paid and editing minutes per client.

**Tips**

- Say how hard it should push: "keep it quick", "go deep", or "poke holes" for a tougher stress test.
- Say "wrap up" at any point to jump to the verdict and the brief.
- A verdict of "open" means the key assumption still needs a real-world test, and the brief says which one.

### dia-reductio: check whether a claim holds together

**In plain words.** Reductio ad absurdum, or proof by contradiction: take a claim at its word, follow it step by step, and see whether it leads to two statements that can't both be true. If it does, something in the starting point has to give. The assistant lists every premise it used, marks which ones it added itself, and leaves the choice of what to give up to you.

**Use it when** you hear a confident rule with "always", "never" or "everyone" in it, or want to test your own position before you defend it. **Not for** deciding whether an idea is wise overall; it only tests consistency.

**Try:**

```
Use proof by contradiction on this claim: the customer is always right.
```

**What you get** (real run, shortened):

> **Reading tested:** "right" means true, so whatever a customer says is correct.
> **Premises:** P1 [A] "right" means "true"; P2 [A] customer C1 says the coat was bought here and customer C2 says it was not, about the same coat; P3 [L] if not-p is true, p is not true.
> **Derivation:** 1. every customer's assertion is true (the claim). … 4. p is true. … 6. p is not true.
> **Contradiction:** lines 4 and 6. **Strength:** it rests on added premises P1 and P2, which are ordinary facts, not logic.
> **Options:** give up "always"; give "right" another meaning; deny that customers ever disagree; or repair the claim: "a customer's good-faith complaint deserves a fair hearing and, where the business can, a remedy."
> **Recommendation:** the repaired claim, because it keeps what the slogan is for. The decision is yours.

The labels mean: **[T]** stated by the claim, **[L]** a rule of logic, **[A]** added by the assistant. A contradiction that needs an [A] premise is only as strong as that premise, and the assistant says so.

**Tips**

- To test the assistant's own previous answer, write "check your last answer by contradiction" or add `--target=claude`.
- If you think an [A] premise is wrong, say so; the assistant removes it and runs the argument again. Picking one of the options works the same way.

### dia-negative: hold a claim to its own standard

**In plain words.** Instead of judging a claim by your values, judge it by its own words. Take what it promises ("anyone can raise a problem at any time") and look for real cases where it doesn't deliver. Then ask what the claim actually does in practice, as a guess you could check. The name comes from the philosopher Adorno's "negative dialectics"; this skill uses a narrower, practical version of his idea, called internal critique.

**Use it when** a slogan, policy, mission statement or plan sounds good and you want to see what it leaves out. **Not for** explaining what code, a command or a setting does, or for a general review.

**Try:**

```
Do an immanent critique of this claim: "We have an open-door policy, so anyone in the company can raise a problem with management at any time."
```

**What you get** (real run, shortened):

> **Its own standard:** "anyone" (no exceptions), "at any time" (no time limit), "raise a problem with management" (it reaches management), and "so" (the policy alone is enough).
> **F1. "Anyone" fails for problems about management.** If your problem is with your manager, the open door opens onto the person you are complaining about, and the policy names no second path. *What escapes:* the problems least likely to be raised.
> **F2. "At any time" fails against real working hours.** A night-shift or remote worker can't raise it *with* a manager at 3 a.m.
> **F3. The "so" overreaches.** A policy grants permission; whether people can speak also depends on what happens afterwards, such as no response or retaliation.
> **What it actually does (an inference):** it moves the blame for silence onto whoever didn't walk through the door. *What would prove this wrong:* a record of complaints about managers raised through the policy and acted on.
> **Options:** narrow the claim; change the practice (a second channel, after-hours reporting, a no-retaliation commitment); keep it and say its limits openly; withdraw it; test it on one real case. **Recommendation:** change the practice. The decision is yours.

**Tips**

- Findings marked conditional depend on facts about your situation, so tell the assistant those facts. If you say a standard isn't really the claim's, it drops the findings that used it and runs again.
- It recommends an option but never picks one for you.

### dia-refine: one careful review of an answer or a draft

**In plain words.** A careful editor's single pass. The assistant lists what is wrong, checks each item, and fixes only the errors it could confirm. Errors it suspects but couldn't confirm are listed separately with the likely correction, so nothing changes silently.

**Use it when** you have a draft, or the assistant's last answer, and want factual errors, logic gaps and missing pieces fixed once. Start the message with `dia-refine`, then say what to focus on, if anything.

**Try:**

```
dia-refine check the facts: The Great Wall of China is the only man-made structure visible from the Moon with the naked eye, and it was built entirely during the Ming dynasty.
```

**What you get** (real run with web search, shortened):

> **① Confirmed errors:** "visible from the Moon" is false (checked by search): from about 384,000 km no single man-made structure can be seen, and astronauts have said the wall can't be seen unaided from space. "Built entirely during the Ming dynasty" is false: walls were joined under the Qin around 220 BC, and other dynasties added sections.
> **② Missing requirements:** none.
> **③ Correct content kept:** the Ming built most of the stone wall seen today.
> **④ Remaining uncertainty:** exact Qin and Han dates vary by source; only secondary sources were checked.
> **Revised statement:** The Great Wall of China is not visible from the Moon with the naked eye, and no single man-made structure is. It was not built entirely under the Ming… *(sources listed)*

**Tips**

- Without a search tool, the assistant can still fix logic and arithmetic it re-derives, and puts unchecked facts under ④.
- "Do this task the dia-refine way" makes it write an answer, review it once and show only the final version.

### dia-iterate: check and fix in rounds

**In plain words.** Like `dia-refine`, but in rounds, and every fix needs outside evidence: a search, a tool run or a source you supplied. Facts that pass a check are locked so later rounds can't undo them. The loop stops by itself when nothing is left to fix, when it can't verify anything more, or at the round limit.

**Use it when** accuracy matters more than speed, for example facts and dates you are about to publish. Start the message with `dia-iterate`; it never starts from a plain request.

**Try:**

```
dia-iterate --max 2 check the dates and facts in this paragraph: "The first iPhone went on sale in 2008, and the App Store opened the same day with 500 apps."
```

**What you get** (real run with web search, shortened):

> **Changes:** "went on sale in 2008" → "2007" (on sale June 29, 2007). "the App Store opened the same day" → "about a year later, in July 2008".
> **Round summary:** round 1: 3 claims checked, 2 confirmed wrong, 1 correct, by web search. Locked: the iPhone date, the App Store date, about 500 apps at launch. Stopped because no defects remained, so round 2 was not needed.
> **Unverified:** the exact launch app count (sources say 500 to 552) and whether the App Store opened on July 10 or 11, 2008.
> **Corrected paragraph:** "The first iPhone went on sale in 2007, and the App Store opened about a year later, in July 2008, with 500 apps."

**Tips**

- `--max N` sets the round limit (default 3).
- In a chat with no search or tools, it stops after round 1 and lists what it couldn't verify instead of guessing.

## Using several skills together

- **`dia-elenchus` and `dia-brainstorm` in one request:** the definition dialogue comes first and the first message says so; brainstorming starts when you ask for options or the dialogue ends. The two are never interleaved.
- **`dia-refine` and `dia-iterate` in one request:** they run as two separate passes with separate outputs. The refine pass's own re-derivation does not count as verification for an iterate round.
- **`dia-reductio` and `dia-negative` in one request:** both run and both answers are complete, which makes for long output (around 9,000 characters in tests). On a phone, ask for one at a time.
- **After `dia-elenchus`:** if you then ask for advice, the assistant says the Socratic part is over and labels each suggestion as its own. For a full options-and-plan session, name `dia-brainstorm` and it takes the record from there.

## Troubleshooting

- **`Repository not found` when adding the marketplace.** Check the spelling: `ajitta/dialectic-skills` (dialectic, not dialectric). The repository is public and needs no GitHub login.
- **No dia skills under `/` on Claude mobile.** Expected: the mobile menu does not list plugin skills. Type the full name (such as `/dia-brainstorm`), ask in words, or start the message with the skill name.
- **dia works on one device but not on another.** Desktop installs stay on that computer; web installs are saved to your account and reach the mobile app. Install on the web for the web and mobile, and in each desktop app you use (see Install).
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
