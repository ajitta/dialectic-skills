# Dialectic Skills (`dia`)

**English** | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

Website: [ajitta.github.io/dialectic-skills](https://ajitta.github.io/dialectic-skills/)

Thirteen reasoning-and-review skills in one plugin, written to run unchanged on any assistant that loads Agent Skills: Claude (web, desktop, mobile, Claude Code), Codex and ChatGPT. The package is instructions only (Markdown, YAML, JSON), so every skill also works in a chat with no tools. Skill files are in English; each skill replies in the language of your message. A skill starts only when your message begins with `dia` or with the skill's full name, or when you select it explicitly; a request in plain words starts none. On a phone, type just `dia`: the router skill (`dia-router`) lists the skills, `dia` with a skill's number or name starts it, and `dia` with a request picks the skill that fits. Five skills were renamed in 2.0.0; How to invoke lists the old and new names.

| Skill | What it does | How it starts |
|---|---|---|
| `dia-skopos` | Before work starts: restates the goal, discloses material assumptions, lists only the decisions you must make, then waits for your approval. | `dia-skopos …` or `dia 1 …`; never picked from a plain `dia <request>` |
| `dia-elenchus` | Plato's elenchus: "what is X?", premises agreed one question at a time, contradictions shown, each revision is your new idea. Usually ends in aporia; gives no advice. | `dia-elenchus …`, `dia 3 …`, or `dia <request>` |
| `dia-quaestio` | Modern Socratic questioning one question at a time, then your options plus up to three labeled ones, convergence by criteria, a verdict and a brief. Never implements. | `dia-quaestio …`, `dia 2 …`, or `dia <request>` |
| `dia-reductio` | Strict reductio ad absurdum in one pass: labeled premises, a Q and not-Q derivation with a rule per line, graded strength, options and a record. | `dia-reductio …`, `dia 4 …`, or `dia <request>` |
| `dia-negative` | Internal critique (narrower than Adorno's immanent critique) in one pass: the target's own standard, strict gaps with cases and "what escapes", the operative purpose with a falsifier, options without forced synthesis. | `dia-negative …`, `dia 5 …`, or `dia <request>` |
| `dia-warrant` | Toulmin's argument layout with Walton's critical questions in one pass: data, warrant (the unstated one supplied and labeled), backing, qualifier and rebuttal, each question tagged with the part it tests, then the weakest link. Never rules on whether the claim is true. | `dia-warrant …`, `dia 6 …`, or `dia <request>` |
| `dia-conjecture` | Lakatos's proofs and refutations as a dialogue on an "all / always / never" claim you hold: your argument split into steps, one counterexample per message with its check, you rule on each case and pick the repair. | `dia-conjecture …`, `dia 7 …`, or `dia <request>` |
| `dia-counterplan` | Mason's dialectical inquiry on a plan or decision: the key assumptions, a plausible contrary for each, a counterplan on the same facts, then you say which assumptions you now hold. Picks no winner. | `dia-counterplan …`, `dia 8 …`, or `dia <request>` |
| `dia-emend` | One review pass over the last answer or a draft: factual errors, logical leaps, missing requirements, repetition. Fixes only confirmed defects. | `dia-emend …`, `dia 9 …`, or `dia <request>` |
| `dia-ratchet` | Repeated review rounds in which only outside evidence counts (a search, a tool run or your own material, never the assistant's own re-derivation); what passed is locked; stops on regression, zero defects, verification exhausted, fixed point or `--max N` (default 3). Named `dia-iterate` before 1.6.0. | `dia-ratchet …` or `dia 10 …`; never picked from a plain `dia <request>` |
| `dia-adjudicate` | Rules on reports that people or other assistants wrote about a text (critiques, reviews, verification reports): checks the text's claims and every report point against sources, gives a verdict for each, and lists the verdicts a person should recheck. Never rewrites the text. | `dia-adjudicate …` or `dia 11 …`; never picked from a plain `dia <request>` |
| `dia-regula` | Checks or writes text a model will follow (a skill file, an agent prompt, an agent instructions file) against four rules: each paragraph one expression with its conditions and fallback, scope words as narrow as meant, fewer instructions each with its reason, one name per thing. A review lists breaches and changes nothing until you pick. | `dia-regula …`, `dia 12 …`, or `dia <request>` |
| `dia-techne` | Deepens a request the way a field's top practitioners would (the outcome it serves, the rawest material, the field's methods, a check by something other than the assistant and you, another field's view), shows each change with its reason, and runs it. Stops before any step a backup cannot undo. | `dia-techne …` or `dia 13 …`; never picked from a plain `dia <request>` |
| `dia-router` | Not a method: a short entry point. `dia` shows a numbered menu, `dia 4 …` or `dia reductio …` starts a skill by its number or name, and `dia <request>` picks the skill that fits and says which. Never starts `dia-skopos`, `dia-ratchet`, `dia-adjudicate` or `dia-techne` from a plain request. | first word `dia` |

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

Then try: `dia reductio Remote work always raises productivity.`

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
4. **Check.** Type `/dia` in the message box. Fourteen entries, `dia:dia-adjudicate` to `dia:dia-warrant` (the thirteen skills and `dia:dia-router`), should appear. Updates arrive through the marketplace (Check for updates, or Sync automatically).

Instead of steps 2 and 3 you can upload the plugin: Customize › Plugins › Add › Upload plugin with [`dialectic-skills.zip`](https://github.com/ajitta/dialectic-skills/releases/latest/download/dialectic-skills.zip) from the latest release. Use Customize › Plugins, not Customize › Skills: the Skills screen rejects a zip that carries a plugin manifest. An upload does not update itself; upload each new release again.

**Claude desktop:** the same Customize › Plugins screens install dia on that computer only. In the owner's tests, a plugin added in Claude desktop did not reach the mobile app, and one added on claude.ai did not appear in Claude desktop. If you use both, install in both places.

### Claude mobile (iOS, Android)

There is no install step. A plugin added on claude.ai (the web) is saved to your account and reaches the mobile app by itself; one added in Claude desktop does not. The mobile `/` menu does not list plugin skills. The shortest route is to start the message with `dia` (see How to invoke); typing the full name also works, for example `/dia-quaestio` or a message starting `dia-quaestio`.

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

There are three ways, and every surface supports at least one of them. A message that starts none of these ways starts no dia skill, even when it asks for a skill's method in words ("use proof by contradiction on…"); in 1.x, nine skills also started from such requests.

1. **The router: start the message with `dia`.** `dia` alone (or `dia help`, `dia menu`, `dia ?`) lists the skills with numbers. `dia 4 <your text>` or `dia reductio <your text>` (also `dia dia-reductio …`) starts that skill (here `dia-reductio`). `dia <your text>` picks the skill whose description fits, names it in one line, and runs it; if two fit about equally, it asks, and if none fits, it answers without a dia skill. It never starts `dia-skopos` (1), `dia-ratchet` (10), `dia-adjudicate` (11) or `dia-techne` (13) from a plain request, but replies with the form to send, for example `dia 10 --max 2 <draft>`. Short codes were removed in 2.1.0. This is the quickest route on a phone: three letters, no hyphen.
2. **By name in the message.** Start the message with the skill's full name: `dia-skopos …`, `dia-emend …`, `dia-ratchet …`, `dia-adjudicate …`, `dia-techne …`, and so on for all thirteen. Since 1.2.0 this also works on Codex without `$` and on ChatGPT without `@` (owner-checked in the mobile app).
3. **Explicit selection**, written differently on each surface:

| Surface | Syntax | Example |
|---|---|---|
| claude.ai, Claude desktop, Claude Code | `/dia:dia-<x>` | `/dia:dia-reductio` |
| Claude mobile | `/dia-<x>` or `/dia:dia-<x>` typed in full (the `/` menu does not list it) | `/dia-quaestio`, `/dia:dia-quaestio` |
| Codex (plugin) | `$dia:dia-<x>` followed by a space | `$dia:dia-skopos write a backup script` |
| Codex (copied folder) | `$dia-<x>` | `$dia-emend` |
| ChatGPT | `@` then pick the skill | `@dia-negative` |

The numbers are fixed: 1 `dia-skopos`, 2 `dia-quaestio`, 3 `dia-elenchus`, 4 `dia-reductio`, 5 `dia-negative`, 6 `dia-warrant`, 7 `dia-conjecture`, 8 `dia-counterplan`, 9 `dia-emend`, 10 `dia-ratchet`, 11 `dia-adjudicate`, 12 `dia-regula`, 13 `dia-techne`. After `dia`, only the number or the full name (with or without `dia-`) picks a skill; a shortened name does not. A short code (`dia red …`), a former name (`dia intent …`), a name that reads as part of your sentence (`dia negative feedback on my draft?`) or a number that counts something (`dia 3 reasons …`) is read as a request, and `dia` picks the skill that fits it.

### Renamed in 2.0.0

Five skills have new names; what each one does is unchanged:

- `dia-intent` → `dia-skopos` (Greek *skopos*, aim)
- `dia-brainstorm` → `dia-quaestio` (Latin *quaestio*, inquiry by questions)
- `dia-refine` → `dia-emend` (to emend: to correct errors in a text)
- `dia-instruct` → `dia-regula` (Latin *regula*, rule)
- `dia-menu` → `dia-router`

Since 2.1.0 the old names no longer work anywhere: a message starting `dia-refine …` starts no skill, and after `dia` an old name is read as part of a request. Use the new names, also for explicit selection (`/dia:dia-<x>`, `$dia:dia-<x>`, `@dia-<x>`).

### Options

Options go after the skill's name or the `dia` selector, as flags or in plain words, in any language:

- `--target=user|claude|text|all` (`dia-reductio`, `dia-negative`, `dia-warrant`): what is examined. `user` is a claim you state, `claude` is the assistant's own earlier answer (on every assistant), `text` is a pasted text, `all` is each of those present. Without the flag the skill infers the target and states it in the first line.
- `--target=user|claude|text` (`dia-counterplan`): whose plan is examined; `claude` only when you point to the assistant's own earlier recommendation.
- `--mode=audit|ask` (`dia-warrant`): `audit` (default) lays out the whole check at once; `ask` has you fill in each part yourself, one question per message.
- `--max N` (`dia-ratchet`): the round cap, default 3.
- Mode and depth (`dia-quaestio`): `develop` (default) or `stress` ("poke holes"), and `quick`, `standard` (default) or `deep`.
- Criteria (`dia-emend`, `dia-ratchet`): anything after the name, for example `dia-emend — check the numbers` or `dia-emend for tone`.

## Skill guide with examples

You don't need any background in philosophy to use these skills. Each one is a way of thinking that people have used for a long time, turned into a routine the assistant follows step by step. Below, each skill gets a plain-language explanation, a prompt to try, and a real session, shortened.

The sessions were run on Claude Code (Sonnet) with this plugin, and the user replies in the dialogue examples came from a simulated user, not a scripted one. They were recorded on 1.x, where the same requests started the skill without its name; the skills' procedures did not change in 2.0.0. The wording you get will differ from run to run. Every prompt works in any language, and the assistant replies in the language you write in.

**Pick a skill by what you want to do**

| You want to… | Use |
|---|---|
| make sure the assistant understood the task before it starts | `dia-skopos` |
| find out what you really mean by a word or an idea | `dia-elenchus` |
| turn a rough idea into options and a plan | `dia-quaestio` |
| check whether a claim holds together | `dia-reductio` |
| see whether a slogan, policy or promise lives up to its own words | `dia-negative` |
| see how well the reasons behind a conclusion actually support it | `dia-warrant` |
| test an "always" or "never" rule of yours against counterexamples | `dia-conjecture` |
| hear the strongest case for a different plan before you commit | `dia-counterplan` |
| fix the mistakes in an answer or a draft, once | `dia-emend` |
| fact-check something thoroughly, round by round | `dia-ratchet` |
| decide which points in reviews of a text actually hold | `dia-adjudicate` |
| write or check a prompt, skill or agent file so a model follows it as meant | `dia-regula` |
| do a task the way the field's best would, checked by something other than the assistant | `dia-techne` |
| not sure which, or typing on a phone | `dia` (`dia-router`) |

### dia-skopos: agree on the task before work starts

**In plain words.** Before a contractor starts work, a good one walks you through the job: here is what I'll build, here is what I'm assuming, here is what only you can decide. `dia-skopos` makes the assistant do that, and then wait for your go-ahead instead of guessing.

**Use it when** a request is short but the result depends on things only you know: a speech, a plan, a script, an email to someone important. **Skip it** for quick questions with one obvious answer.

**Try:**

```
dia-skopos Write a short speech for my brother's wedding.
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
- If you don't say what the work is for, the review guesses it in one line, marked as its hypothesis; correct it or just say "proceed". If you name a result beyond the work itself, such as "a landing page that will increase sales", it keeps the criteria for finishing the page apart from those that would show sales rose, labels indirect measures as proxies, and marks the result unverified until something can check it, saying so again when it reports the finished work.
- "Looks good", silence or a thumbs-up do not count as approval; the assistant keeps waiting.
- It covers that one task and its direct follow-ups. Start a new task with `dia-skopos` again if you want the same check.

### dia-elenchus: find out what you really mean

**In plain words.** This is the method Socrates uses in Plato's dialogues. You say what you think something is ("a good teacher is…"). The assistant doesn't argue back or give its own view. It asks about one concrete case at a time, and each case is chosen so that your own answers start to pull against your definition. You then fix the definition in your own words. Often you end up stuck, and the Greek word for that is **aporia**. Being stuck is a result here, not a failure: you now know exactly which part you don't know, so you won't build on a wrong assumption.

**Use it when** you rely on a word that feels obvious but drives real decisions: a good teacher, a fair split, a successful project, a healthy relationship. **Not for** getting advice; it gives none during the dialogue.

**Try:**

```
dia elenchus I think a good teacher is one whose students get high test scores.
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

### dia-quaestio: grow a rough idea, then decide

**In plain words.** A coach who asks you good questions before handing you options. First it asks one question at a time to pin down what you want and what you know (Socratic questioning). Then you list options, it adds a few of its own, you choose what matters, and it ends with a verdict and a short brief you can act on. Unlike `dia-elenchus`, it does give suggestions, after the questions.

**Use it when** you have a goal but no plan yet: a side income, a career move, a small project, a trip. **Not for** building the thing; it never writes code or acts.

**Try:**

```
dia quaestio keep it quick: I want to earn some extra money on weekends.
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
dia reductio The customer is always right.
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

- To test the assistant's own previous answer, write `dia reductio check your last answer` or add `--target=claude`.
- If you think an [A] premise is wrong, say so; the assistant removes it and runs the argument again. Picking one of the options works the same way.

### dia-negative: hold a claim to its own standard

**In plain words.** Instead of judging a claim by your values, judge it by its own words. Take what it promises ("anyone can raise a problem at any time") and look for real cases where it doesn't deliver. Then ask what the claim actually does in practice, as a guess you could check. The name comes from the philosopher Adorno's "negative dialectics"; this skill uses a narrower, practical version of his idea, called internal critique.

**Use it when** a slogan, policy, mission statement or plan sounds good and you want to see what it leaves out. **Not for** explaining what code, a command or a setting does, or for a general review.

**Try:**

```
dia negative "We have an open-door policy, so anyone in the company can raise a problem with management at any time."
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

### dia-warrant: see how well the reasons support a conclusion

**In plain words.** Most everyday arguments don't prove anything; they make a conclusion likely: an expert said so, it worked for them, this causes that. `dia-warrant` lays such an argument out in parts, after the philosopher Stephen Toulmin: the **claim**, the **data** it rests on, the **warrant** (the general rule that gets you from the data to the claim, which people usually leave unsaid), the **backing** for that rule, the **qualifier** (how sure the claim is) and the **rebuttal** (when the rule would not apply). It then asks the standard **critical questions** for that kind of argument (from the argumentation researcher Douglas Walton), each tagged with the part it tests, and names the weakest link: the one part where the support is thinnest, for example "weakest link: warrant". It judges the support, never whether the claim is true.

**Use it when** you want to know how much a "because" can carry: advice from an expert, a comparison with someone else's experience, a prediction about what will happen. **Use a sibling instead** when the claim says "always", "every" or "never" and you mean it strictly (`dia-conjecture`), when you want to know whether it contradicts itself (`dia-reductio`), or when it is a plan you are deciding on (`dia-counterplan`).

**Try:**

```
dia warrant "My friend is a personal trainer and she says running ruins your knees, so if I take up running I will get knee problems."
```

**What you get** (real run, shortened):

> **Target:** user (inferred). I examine the argument as you stated it.
> **Claim (C):** "if I take up running I will get knee problems." This is stated, with no qualifier ("will").
> **Intermediate claim (C1):** "running ruins your knees." This is stated as your friend's view. The argument is a chain: data → C1 → C.
> **Reading fixed:** "ruins" is ambiguous. I read it as "causes lasting knee damage in people who run."
> **Data (stated):** "My friend is a personal trainer and she says running ruins your knees."
> **Wa (reconstructed):** What a personal trainer says about running's effect on knees is generally reliable. This is the step from data to C1. **Wb (reconstructed):** If running generally ruins knees, then a person who takes up running will generally get knee problems. This is the step from C1 to C.
> **Backing:** none given. **Rebuttal:** none given. **Scheme:** The first step is **expert opinion**. The second applies a **general rule to a case**, which I tested with the general questions.
> **Critical questions** *(eight, all open)*: 1. [data] Is she a genuine expert in the field this claim belongs to? Her stated role is personal trainer. The argument doesn't say whether that covers joint health or injury. **Open.** … 3. [warrant/backing] Is her assertion based on evidence? The argument cites none, only "she says." **Open.** … 7. [rebuttal] Could you be an exception, for example through your running volume, your history, or other factors? **Open.** … I answered none of these with facts of my own. Each needs an answer from you or from a source.
> **Qualifier check:** C says "will". Wa and Wb license only "generally", which is "probably". So the claim is **overstated**. Both warrants are my reconstruction, and the overstatement comes from the "generally" default. If you meant "certainly", say so. …
> **Result:** **Weakest link: warrant (Wa), because "Is her assertion based on evidence?" is left open.** It matters because everything rests on "she says." Without a stated basis for her claim, the data give C very little support. The link would be stronger if you knew what her claim rests on, such as studies, her clients' outcomes, or training in injury. … *(then a record: target and claim, mode, scheme, both warrants reconstructed, 8 questions asked and 0 answered, result, qualifier check, what would strengthen the link, decision on the reconstructed warrants: pending)*
> This audit doesn't decide whether running causes knee problems. It only rates how well the reasons given support that claim.
> If you'd like to check your own argument step by step, I can switch to ask mode.

"Stated" means the argument said it; "reconstructed" means the assistant supplied it because the step needs it. Here the reasons pass through an in-between claim (C1, "running ruins your knees"), so each step gets its own warrant (Wa, Wb) and the result says which step the weak link is on. Before testing, the assistant also fixed one reading of the unclear word "ruins". The tags show which part each question tests: **[data]**, **[warrant/backing]**, **[rebuttal]** or **[conclusion]**. The result names one part: data, warrant, backing, qualifier, rebuttal or claim.

**Tips**

- Answer an open question in your next message ("she says most of her clients who run have sore knees"); the assistant marks it as answered by you and works out the result again.
- If you don't actually rely on a reconstructed warrant, say so: it is removed, and the assistant asks which rule you do rely on.
- When you check your own argument, the audit ends by offering ask mode (`--mode=ask`): the assistant asks for one part at a time and you fill it in. You can also ask for it from the start; it suits an argument you are still building.
- "No weak link found among the questions asked" is not a proof, and a weak link does not make the claim false.

### dia-conjecture: test an "always" rule against counterexamples

**In plain words.** A rule with "always", "every" or "never" in it can be knocked down by one case that doesn't fit. This skill follows the method the philosopher Imre Lakatos described in *Proofs and Refutations*. First it splits your reasons for the rule into numbered steps. Then it brings one counterexample per message and shows, line by line, how the case fits your rule and still breaks it, and what the case rests on (often just arithmetic on numbers it made up for the example). You decide whether each case counts. When one does, you don't have to throw the rule away: the assistant lists the ways to repair it, such as making the broken step part of the rule, and recommends one, but you pick. The rule then says exactly when it holds.

**Use it when** you rely on a rule of thumb and mean it strictly: "buying in bulk always saves money", "the express lane is always faster", "a pricier bottle of wine always tastes better". **Use a sibling instead** if you mean "usually" (`dia-warrant`), if it is a plan, a policy or a decision (`dia-counterplan`, or `dia-quaestio` to poke holes), or if the real question is what a word means (`dia-elenchus`).

**Try:**

```
dia conjecture Buying in bulk always saves money.
```

**What a session looks like** (real run, shortened):

> **Assistant:** This is your own claim. In my words, C is: every purchase made in bulk (a larger quantity than you'd otherwise buy at once) saves money, where "saves money" means you spend less in total than you would have without buying in bulk. Why do you hold it? If you don't have an argument written out, I can reconstruct one as numbered steps, but then I'd be attacking a proof I wrote myself. Which do you want?
>
> **You:** Sure, I can say why: the big pack costs less per item, and I'd buy the stuff anyway, so I end up spending less. Go ahead and write it out as steps if you want, and I'll tell you which ones I agree with.
>
> **Assistant:** Here is the argument as numbered steps. L1 and L2 are your words. I wrote L3 to L5 because the argument needs them. 1. [T] "the big pack costs less per item" 2. [T] "I'd buy the stuff anyway" 3. [A] You would use every item in the big pack. None spoils, expires, gets lost or gets thrown out, and you don't use it faster just because it's there. … 4. [A] The extra costs of buying in bulk are zero or small compared with the per-item saving. These include a membership fee, storage space, upfront cash and transport. … 5. [A] The cheaper per-item price comes from the bulk pack itself, not from a sale on the smaller pack. … I suspect L3 most… Since I wrote L3 to L5 and am attacking them, I'm arguing both sides here. Is this your argument? Correct any line, and tell me which lines you accept.
>
> **You:** Yeah, that's my argument. I agree with 1, 2, 4 and 5, and for 3 I only meant stuff I'd really use up, so if something spoils before I finish it, I guess that doesn't count as saving.
>
> **Assistant:** That's a change to your rule, so here are the old and new wording. **Old C:** every bulk purchase saves money. **New C′:** every bulk purchase of items you will actually use up saves money. **What C′ no longer covers:** anything that spoils, expires, goes stale or gets lost before you finish it. … Before I raise any case, what would you accept as evidence against your rule? …
>
> *…you answer: paying more in total than for the small packs even though you used up every item, for example when the membership fee or the gas to get there costs more than you saved per item…*
>
> **Assistant:** Case 1 (both: against C′ and L4): a one-off club trip. Say you join a warehouse club for a $60 annual fee, just to buy a 40-roll pack of paper towels. The pack costs $0.25 less per roll than the shops near you, and you use all 40 rolls. **A, a bulk purchase of items you'll use up?** Yes. It's a 40-roll pack and every roll gets used. **B fails, you save money?** Yes, it fails. The per-roll saving is 40 × $0.25 = $10, but you paid $60 to get in. … **L4 fails too.** … It rests on arithmetic with numbers I made up, so the evidence class is logic, not a real receipt. Does this count against your rule?
>
> **You:** Yeah, that counts. … I guess I'd have to say bulk saves money only when the extra costs, like a fee, are smaller than what I save.
>
> **Assistant:** Your fix is that bulk saves money only when the extra costs are smaller than what you save. That is true, but it doesn't work as a repair. It says "bulk saves money when it saves money", so no purchase could ever count against it. … 1. **No attributable extra costs.** C′ becomes: every bulk purchase of items you'll use up, where no fee, special trip or storage cost comes from this purchase alone, saves money. … 2. **Fees and special trips only.** … 3. **Give up C′.** … I recommend option 1. It names all the costs L4 was hiding, so you don't end up adding exceptions one at a time. Which do you pick?
>
> **You:** I'll go with option 1. It covers storage and the trips too, not just the fee, and those can eat up the savings the same way, so I'd rather list all the extra costs up front than keep patching one at a time.
>
> **Assistant:** Current claim, C′ as you picked it: … Case 2 (both: against C′ and L1): a bulk pack that costs more per item. Say one store sells a brand of batteries in a 12-pack for $9 ($0.75 each) and in a 48-pack for $42 ($0.875 each). You need 48 batteries and will use every one. … **B fails, you save money?** Yes, it fails. The 48-pack costs $42, while four 12-packs cost 4 × $9 = $36. You spend $6 more. **L1 fails too.** … Does this count against your rule?
>
> **You:** Yeah, that counts. … I'd have to check the per-item price first, since my rule only works when the big pack really is cheaper per item.
>
> **Assistant:** Your fix is to check the per-item price first. That is a repair, and unlike last time it has a condition you can test before buying. Here are three versions: … I recommend option 1… One warning: with this much built in, the rule is close to true by arithmetic. … What's left is closer to a checklist than a discovery. Which do you pick?

**Tips**

- If a case doesn't fit your rule, say which line of its check is wrong. A bare "no" leaves the case "disputed": neither withdrawn nor counted.
- You pick every repair, even one you have already put into words. In the run above you proposed a fix twice, and both times the assistant laid out numbered options, recommended one and asked you to pick. A fix that amounts to "bulk saves money when it saves money" is turned down as a repair, because no purchase could ever count against it.
- Each case says what it rests on. "Arithmetic with numbers I made up" means the numbers are invented and only the sums are checked; whether real prices look like that is yours to judge.
- Narrowing a word of your rule, as with "I only meant stuff I'd really use up" in the run above, is a change of definition: the assistant shows the old and new wording and says what your rule no longer covers. Saying "that's not a real bulk buy" just to shut out a case counts the same way.
- After three rounds it offers to stop, and "wrap up" stops it at any time. The best result is "holding against the cases tried", never "proved"; "open" means a case is disputed, or a case counted and no repair was picked.

### dia-counterplan: hear the case for a different plan

**In plain words.** Before a big decision it helps to hear someone argue for a different plan, built on the opposite assumptions. This is dialectical inquiry, a planning method from management research (Richard Mason, 1969). The assistant lists the assumptions your plan rests on, keeps the ones that would change the decision if they were wrong, gives each a believable opposite, and builds the best rival plan on the same facts. The opposites are its own choice, and any reason it gives for one ("supposing…") is a supposition, not a fact about your situation. Then you say which assumptions you now believe; that mix is the result. The assistant gives no verdict at any point, and it says openly that it wrote both sides itself.

**Use it when** you are about to commit to a plan: a move, a job offer, a big purchase, a team's next step. **Use a sibling instead** to be questioned about your idea one question at a time, or to have holes poked in it (`dia-quaestio`), to check whether a plan lives up to its own promises (`dia-negative`), or to test how well one argument's reasons hold (`dia-warrant`). For whether a single claim is true, just ask.

**Try:**

```
dia counterplan We want to move from our two-bedroom city apartment to a bigger house in the suburbs before our kids (6 and 3) start school next September. The monthly payment is about the same as our rent now, the kids would each get their own room and a yard, and the school there has good reviews. The catch: my commute goes from 20 minutes to about an hour each way.
```

**What a session looks like** (real run, shortened):

> **Assistant:** **Target:** `user` (your plan). I'm giving no verdict. I wrote both sides, so the result will be your set of assumptions.
> **The plan:** "move from our two-bedroom city apartment to a bigger house in the suburbs before our kids (6 and 3) start school next September." Data, all supplied by you and none verified this session: **D1:** The monthly payment is about the same as your current rent. … **D4:** Your commute goes from 20 minutes to about 1 hour each way. …
> **Assumptions:** *(seven, all marked [A], added by the assistant; for example)* **A1 [A]:** "About the same payment" means about the same total cost of housing. The plan needs this for the move to be cost-neutral. … **A6 [A]:** Your commute can't be shortened, for example by remote days. …
> **Key assumptions:** I asked of each: if the opposite were true, would the decision change? **K1 = A2:** Yes. If the commute isn't sustainable, the main cost of the plan outweighs the gains. **K2 = A1:** Yes. If total cost is higher, "same as rent" no longer holds. … *(five in all: commute, cost, school, timing, space)*
> **Contraries (my choice, each a supposition, not a reported fact):** **C1:** The commute proves unsustainable. About 2 hours a day removes you from mornings and evenings, and the hour isn't usable time. … **C2:** The real monthly cost exceeds the rent. I'm supposing maintenance, taxes, insurance, utilities, extra fuel or fares, and possibly a second car. Figures: not supplied. … **C5:** At 6 and 3, parental time and proximity matter more than a private room each and a yard. Shared rooms and public parks are enough for now.
> **Counterplan: stay in the city for now.** Each slot matches the plan's detail, and each part is marked with the contrary it rests on. **Housing and cost:** Stay in the two-bedroom apartment at the current rent (C2, C4). … **School:** Enroll both in the city school option for next September (C3, C4). Name, reviews and distance: not supplied. **Commute:** Keep the 20-minute commute (C1). **Timing:** Hold the decision, then revisit in 12 months. That date is my choice. …
> **Side by side:** 1. **K1 (a ~1-hour commute is sustainable) vs C1 (it isn't).** Favours the plan if a two-week rush-hour trial leaves you and your household fine with it. Favours the counterplan if the trial shows you'd miss routines you care about, or your partner would carry much more. …
> One assistant wrote both sides, so the counterplan may be less developed than a real advocate's version.
> **Your synthesis:** For each pair K1–K5, which assumption do you now hold: the plan's, the counterplan's, your own wording, or "can't tell"?
>
> **You:** K1: Can't tell yet. I can't work from home, so the hour each way is real. But I haven't tried that drive at rush hour, so I don't know how bad it would be. K2: Can't tell yet. I haven't added up property taxes and upkeep, so I don't know if it's really the same as rent. Right now I'd say the counterplan's worry is fair, but I don't have the numbers. … *(can't tell on the school; the counterplan's on timing)* … K5: The plan's, mostly. The kids fight over their shared room most nights, so the space is a real problem for us now. … So overall I'm not ready to say yes to the move. First I need to add up the real monthly costs and try the drive. Then I can decide.
>
> **Assistant:** Your rulings are in. Since K1–K3 are still open, the result is **undetermined**. **Record** … 1. **K1, commute sustainable (plan) vs C1:** Open. … Your clarification on working from home now replaces my A6 as [T]. 2. **K2, total cost ≈ rent (plan) vs C2:** Open. You think the counterplan's worry is fair, but you haven't added up property taxes and upkeep. Lean: counterplan, which I record as a lean, not a ruling. … 4. **K4, move must precede September (plan) vs C4:** Counterplan held. … 5. **K5, rooms and yard are worth it now (plan) vs C5:** Plan held, mostly. … **Result:** undetermined. Three pairs are open, one is held for the counterplan, and one is held for the plan with a caveat. **Kept for the side set aside:** … **K5** (set aside: the counterplan's side): the yard's benefit is unproven, and the commute removes about 80 minutes a day from time with the kids. **Written by:** One assistant wrote both sides of this comparison. **Not tested:** … Alternatives other than these two, such as a closer suburb, or a larger city apartment or one with more bedrooms. … Hearing both sides is not evidence that the plan was tested. … Once you have them, I can rerun just those three pairs with the new numbers, or sketch a plan built on your set if you ask for one.

**Tips**

- Answer pair by pair: the plan's assumption, the counterplan's, your own wording, or "can't tell". "Can't tell" is a fine answer; the record then says what would decide it. A result of "undetermined" (*teyku*, the Talmud's "let it stand") means at least one pair is still open.
- If you only lean one way, say so. The pair is then recorded as open with your lean noted; it counts as held only if you say you hold that side. In the run above, "Right now I'd say the counterplan's worry is fair" left the cost pair open with "Lean: counterplan".
- Facts you give about your situation go into the record: in the run above, "I can't work from home" replaced the assistant's added assumption A6 as your own [T] line. Something new that the plan rests on becomes a new pair with its own contrary.
- Rejecting a contrary counts as your ruling; the assistant records it and doesn't argue. It rewrites a contrary only if you show that it misstates your facts or clashes with another one.
- "Which plan wins?" gets no verdict, during or after the inquiry, because the same assistant wrote both sides. Instead it names the observation that would decide the pair you find hardest.

### dia-emend: one careful review of an answer or a draft

**In plain words.** A careful editor's single pass. The assistant lists what is wrong, checks each item, and fixes only the errors it could confirm. Errors it suspects but couldn't confirm are listed separately with the likely correction, so nothing changes silently.

**Use it when** you have a draft, or the assistant's last answer, and want factual errors, logic gaps and missing pieces fixed once. Start the message with `dia-emend` (or `dia 9`, `dia emend`), then say what to focus on, if anything.

**Try:**

```
dia-emend check the facts: The Great Wall of China is the only man-made structure visible from the Moon with the naked eye, and it was built entirely during the Ming dynasty.
```

**What you get** (real run with web search, shortened):

> **① Confirmed errors:** "visible from the Moon" is false (checked by search): from about 384,000 km no single man-made structure can be seen, and astronauts have said the wall can't be seen unaided from space. "Built entirely during the Ming dynasty" is false: walls were joined under the Qin around 220 BC, and other dynasties added sections.
> **② Missing requirements:** none.
> **③ Correct content kept:** the Ming built most of the stone wall seen today.
> **④ Remaining uncertainty:** exact Qin and Han dates vary by source; only secondary sources were checked.
> **Revised statement:** The Great Wall of China is not visible from the Moon with the naked eye, and no single man-made structure is. It was not built entirely under the Ming… *(sources listed)*

**Tips**

- Without a search tool, the assistant can still fix logic and arithmetic it re-derives, and puts unchecked facts under ④.
- `dia-emend do this task the dia-emend way: <task>` makes it write an answer, review it once and show only the final version.

### dia-ratchet: check and fix in rounds

**In plain words.** Like `dia-emend`, but in rounds, and every fix needs outside evidence: a search, a tool run or a source you supplied. Facts that pass a check are locked so later rounds can't undo them. The loop stops by itself when nothing is left to fix, when it can't verify anything more, or at the round limit.

**Use it when** accuracy matters more than speed, for example facts and dates you are about to publish. Start the message with `dia-ratchet` (or `dia 10`, `dia ratchet`); `dia <request>` never picks it.

**Try:**

```
dia-ratchet --max 2 check the dates and facts in this paragraph: "The first iPhone went on sale in 2008, and the App Store opened the same day with 500 apps."
```

**What you get** (real run with web search, shortened):

> **Changes:** "went on sale in 2008" → "2007" (on sale June 29, 2007). "the App Store opened the same day" → "about a year later, in July 2008".
> **Round summary:** round 1: 3 claims checked, 2 confirmed wrong, 1 correct, by web search. Locked: the iPhone date, the App Store date, about 500 apps at launch. Stopped because no defects remained, so round 2 was not needed.
> **Unverified:** the exact launch app count (sources say 500 to 552) and whether the App Store opened on July 10 or 11, 2008.
> **Corrected paragraph:** "The first iPhone went on sale in 2007, and the App Store opened about a year later, in July 2008, with 500 apps."

**Tips**

- `--max N` sets the round limit (default 3).
- In a chat with no search or tools, it stops after round 1 and lists what it couldn't verify instead of guessing.
- Named `dia-iterate` before 1.6.0; the old name no longer starts it.

### dia-adjudicate: decide which review points hold

**In plain words.** A referee for reviews. You give it a text and one or more critiques or reviews of it, written by people or by other assistants. It checks the text's own claims and every point in the reviews against sources, says which points hold and which are wrong or overstated, and ends with the few verdicts a person should recheck. It never rewrites the text and adds no review of its own.

**Use it when** several reviews of the same text disagree, or you want a confident review checked before you act on it. Start the message with `dia-adjudicate` (or `dia 11`, `dia adjudicate`), then give the text and the reviews; `dia <request>` never picks it.

**Try:**

```
dia-adjudicate
Text: "Moore's 1965 paper predicted that transistor counts double every 18 months, so in 10 years chips hold about 16 times as many."
Review A: "Wrong twice: the 1965 paper said every year, and doubling every two years for 10 years gives 32 times."
Review B: "The 18 months was Moore's own 1975 figure, and doubling every two years gives 64 times in 10 years."
```

**What you get** (real run with web search, shortened):

> **Inputs.** "There are two reports. I shuffled them, so R1 is Review B and R2 is Review A." One web search; "its answer is a model summary, not the raw pages".
> **Claims in the target:** the 18-month period fails: "The 1965 figure was a year, and the 1975 revision was two years", and 18 months "comes from David House, not Moore". 18 months over 10 years "is 120/18 = 6.67 doublings. 2^6.67 ≈ 101.6, about 100×, not 16×" (re-derived), a second error "that neither report mentions". C, about 16×: fails.
> **Report issues:** R2 (Review A): every year in 1965, valid; 32× at two-year doubling, valid. R1 (Review B): 18 months as Moore's 1975 figure, wrong; 64×, wrong: "2^5 = 32. 64 is 2^6, which is 12 years at that rate."
> **Not verified:** "I did not open the 1965 paper or the 1975 talk. I relied on a summarized search."
> **For a human check:** 1. R1's 18-month attribution, which "rests on a summary". 2. R1's 64× figure. 3. T's 16× figure, "my own recomputation, so please check it." *(sources listed)*

**Tips**

- Give it the reviews as they are; it relabels them R1, R2… in a shuffled order and rules on content, not on who wrote them.
- Where the assistant can start separate agents, or you can open a second chat, run it twice on the same input and recheck only the verdicts that differ.
- Without a search tool, it still recomputes numbers and logic, but leaves factual points "unverifiable" instead of overturning them.

### dia-regula: write text a model will follow

**In plain words.** A style check for instructions you give an AI: a skill file, a prompt for an agent, a project's agent file, a rules file. It holds the text to four rules. Each paragraph says what result it wants, with its conditions and fallback in the same sentence, so no condition is stranded on a line of its own. A word that sets a limit ("touch", "change") is as narrow as you meant it. There are fewer instructions, and each has its reason. Each thing has one name. When you only ask for a review, it lists what breaks a rule, most serious first, and changes nothing until you pick.

**Use it when** you write or edit a skill, a prompt for an agent or sub-agent, an agent instructions file, or a rules file, or when an assistant keeps ignoring a condition you wrote. Start the message with `dia-regula`, `dia 12` or `dia regula`, or let `dia <request>` pick it.

**Try:**

```
dia regula Review this instruction I wrote for a coding agent:
Update the docs for the new flag.
Only touch files the task needs.
- If the tests fail, stop.
```

**What you get** (real run, shortened):

> "Review of the three lines against the dia-instruct rules, most severe first. I haven't changed the text."
> 1. **Line 3: "- If the tests fail, stop."** (Rule 1, Rule 3): "The condition sits in its own bullet, apart from the action it guards." "Stop" "could mean halt edits, revert edits, or report and wait", and no reason is given.
> 2. **Line 2: "Only touch files the task needs."** (Rule 2, Rule 1, Rule 3): "'Touch' can be read as read, edit or create, and 'needs' is the agent's own judgment." No paths are named.
> 3. **Line 1: "Update the docs for the new flag."** (Rule 2): "'The docs' and 'the new flag' are unnamed."
> 4. **Across the lines** (Rule 4): "docs", "files" and "the task" may be read as different scopes.
> "Tell me which findings to act on, and give me the flag name, the doc paths and the test command if you want me to draft the rewrite."
>
> *(Recorded on 1.x, when dia-regula was named dia-instruct.)*

**Tips**

- It treats the text you give it as material to check, not as instructions to follow, even when that text is itself a prompt.
- Ask "how strong is this rule?" to see what each rule rests on; that file is read only then.
- Where the assistant can start a separate agent, a change to text you will keep is reviewed by one that did not write it; otherwise, and for an edit that only adds a fact or command such as a test command, the assistant checks it itself and labels the check not independent.

### dia-techne: do a task the way the field's best would

**In plain words.** A request is often narrower than what it is for. Before it works, `dia-techne` asks five questions: what a top practitioner of the field would do here that you did not ask for, which raw material they would start from instead of a summary, which methods and tools they would use, what other than the assistant and you would show the result is right, and which idea from another field, or which opposing view, would change the result. It then rewrites your request, shows each change with its reason so you can take it back, and runs it in the same turn. It never changes what you set as a requirement or a limit, your data, or what you allowed it to do. A file you asked it to overwrite is backed up first (for a file git already holds unchanged, the last commit is the backup), and it stops before anything a backup cannot undo, such as sending or publishing; a push you asked for runs only when it changed nothing in what is pushed and the push forces, rewrites and deletes nothing.

**Use it when** a task matters enough to want the deeper version rather than the quick one: a claim you will make in public, a fix you want checked by something other than the assistant, a decision built on data. It takes longer and its replies are longer. Start the message with `dia-techne`, or use `dia 13` or `dia techne`; `dia <request>` never picks it.

**Try:**

```
dia-techne Our mobile puzzle game's D30 retention is 12%. Can I tell investors next week that it's above the industry average?
```

**What you get** (real run with web search, shortened):

> **Short answer:** "Probably yes, but only if you say which benchmark and which cohort you mean."
> **Outcome and revisions:** "The outcome you need is for investors to believe your retention claim." Three changes, and "each change can be taken back": "industry average" becomes a named benchmark, because "there is no single industry average"; a check that the 12% uses the benchmark's definition (active "on exactly day 30" or "on day 30 or later", blended or organic-only installs); a recommended wording.
> **Rewritten prompt** (in a code block, then run): compare 12% with each genre-level D30 benchmark, naming source, year and region; say which is the fairest comparison; list the questions an investor will ask; give one sentence "that is true under the strongest benchmark and still true under the weakest".
> **Open points:** the assumption that "industry average" means puzzle or match games; placeholders for how the 12% is defined, the cohort size and the install mix; "I saw only search snippets, not the full reports."
> **Result:** puzzle 5.35%, match games 7.15%, board games in the US 5.09% (Android) to 8.13% (iOS), all games median about 0.7%, each marked secondary. Suggested wording: "Our D30 is 12%, against roughly 5–8% for puzzle and match games in public benchmarks (Mistplay/AppsFlyer, 2025)." **Outside check for you to run:** "Recompute D30 from raw install and activity logs", split it by platform, country and organic versus paid, and read the benchmarks' methods. "If the recomputed figure drops below roughly 8%, change the wording." *(sources listed)*
> *(Recorded on 1.13.0. From 2.7.0 the full reply gives the result first and the rewritten prompt last.)*

**Tips**

- When nothing needed changing, the reply is short: the result, what the check showed and the assumptions. In a recorded leap-year fix it compared the new function with Python's `calendar.isleap` "for every year from 1 to 10000", and "the original is saved beside it as `leap.py.bak`".
- Name another executor ("a prompt for Codex, don't run it") and it still does the research but only writes the prompt; the open points list what that executor may not reach.
- Searches carry general public terms only, never your private material. Without tools, the outside check is named for you to run, and facts from memory are marked as recall.
- Asked for something that belongs to a sibling (a skill file to keep, a scope check without running), it runs anyway and names that sibling in one line.

### dia-router: one short word for every skill

**In plain words.** Not a method of its own, just a quicker way in. Start your message with `dia`. On its own, `dia` lists the thirteen skills with numbers. Put a skill's number or name after it, then your request, to start that skill, or just write what you want and it picks the skill that fits, telling you which in one line first. If two skills fit your request about equally, it asks instead of guessing; if none fits, it answers without one.

**Use it when** you are typing on a phone, or you are not sure which skill you need. `dia-skopos` (1), `dia-ratchet` (10), `dia-adjudicate` (11) and `dia-techne` (13) start only by their number or name, never because `dia` picked them; for such a request `dia` replies with the form to send.

**Try:**

```
dia
dia 4 Assume every prime is odd and show where it breaks.
dia Our churn dropped after we added onboarding emails, so the emails reduced churn. How well do my reasons support that?
```

**What you get** (real runs on Claude Code, shortened):

> `dia` → the numbered list, "1. **dia-skopos**: Restate the goal, assumptions and open decisions before work starts … 4. **dia-reductio**: Proof by contradiction: does a position hold together or follow from its premises … 13. **dia-techne**: Deepen a one-off request as a field's top practitioners would, then run it", then "`dia <number or name> <request>` runs that skill, for example `dia 4 …` or `dia reductio …`."
> `dia 4 …` → `dia-reductio` starts at once: "**Target (inferred): user.** … **Thesis T:** "Every prime is odd." … **Where it breaks:** at the number 2. Lines 5 and 8 are Q and not-Q: 2 is odd, and 2 is not odd. …"
> `dia Our churn dropped …` → `dia-warrant` starts: "**Target:** an argument you state (inferred; …). … **Claim (C):** "the emails reduced churn" (stated). … **Weakest link: warrant, because "How strong is the causal generalization?" is left open.** …"
> *(Recorded on 2.1.0.)*

**Tips**

- The numbers stay fixed: 1 skopos, 2 quaestio, 3 elenchus, 4 reductio, 5 negative, 6 warrant, 7 conjecture, 8 counterplan, 9 emend, 10 ratchet, 11 adjudicate, 12 regula, 13 techne. The full name works too, with or without `dia-` (`dia reductio …`, `dia dia-reductio …`); a shortened name does not.
- Options pass through: `dia 10 --max 2 <draft>` is the same as `dia-ratchet --max 2 <draft>`.
- `dia` must be the first word on its own. `dia-emend …` and the other full names go straight to their skill.
- A name that is plainly part of your sentence (`dia negative feedback on my draft?`) or a number that counts something (`dia 3 reasons …`) is not a pick; the whole text is read as a request.
- Short codes (`dia red …`) and the five former names (see How to invoke) stopped picking a skill in 2.1.0; after `dia` they are read as a request.
- Where the assistant cannot open a second skill, `dia` still shows the menu and replies with the full form to send (such as `dia-reductio …`); this case has not been tested.

## Using several skills together

- **`dia-elenchus` and `dia-quaestio` in one request:** the definition dialogue comes first and the first message says so; brainstorming starts when you ask for options or the dialogue ends. The two are never interleaved.
- **`dia-emend` and `dia-ratchet` in one request:** they run as two separate passes with separate outputs. The emend pass's own re-derivation does not count as verification for a ratchet round.
- **`dia-reductio` and `dia-negative` in one request:** both run and both answers are complete, which makes for long output (around 9,000 characters in tests). On a phone, ask for one at a time.
- **`dia-warrant`, `dia-conjecture` and `dia-counterplan` check what you gave them first.** If the request belongs to a sibling, they say so in one line and name it: `dia-conjecture` sends a rule you mean only as "usually" to `dia-warrant` and a plan to `dia-counterplan` or `dia-quaestio`; `dia-warrant` sends a strict "always" claim to `dia-conjecture` and a plan's assumptions to `dia-counterplan`; `dia-counterplan` sends a request to be questioned about your plan to `dia-quaestio`. Ask again, starting the message with the skill they name.
- **After `dia-elenchus`:** if you then ask for advice, the assistant says the Socratic part is over and labels each suggestion as its own. For a full options-and-plan session, start a message with `dia-quaestio` and it takes the record from there.
- **Several skills as a review panel:** when an assistant that can start sub-agents runs several skills on one text, give each sub-agent one skill: `dia-counterplan` for a plan or recommendation, `dia-negative` for a text measured against the rules or standards it states, `dia-warrant` for an argument, `dia-reductio` for whether the text holds together. Each skill examines one central claim, so name the claim when it matters which. Start each message with the skill's name and the text and ask for the result in one response (`dia-counterplan` then ends with its record, every pair open, instead of a question), and do not prescribe an output table: in tests a fixed findings table made the skills drop parts of their method. Give the reports to `dia-adjudicate` in a separate agent, ask for two separate runs, and recheck the verdicts that differ; a counterplan's pairs are for whoever decides, not for the judge. A report written on another assistant (Codex, ChatGPT) can be pasted in the same way.

## Troubleshooting

- **`Repository not found` when adding the marketplace.** Check the spelling: `ajitta/dialectic-skills` (dialectic, not dialectric). The repository is public and needs no GitHub login.
- **No dia skills under `/` on Claude mobile.** Expected: the mobile menu does not list plugin skills. Start the message with `dia` or with the skill's full name, or type the full selection (such as `/dia-quaestio`).
- **A skill did not start.** Since 2.0.0 a request in plain words starts no dia skill. Start the message with `dia` (`dia <request>`, or `dia <number or name> <request>` such as `dia 4 …` for a chosen skill) or with the skill's full name (`dia-reductio …`).
- **A skill name from 1.x is not found.** Five skills were renamed in 2.0.0 (see How to invoke), and the old names stopped working in 2.1.0. Use the new name.
- **dia works on one device but not on another.** Desktop installs stay on that computer; web installs are saved to your account and reach the mobile app. Install on the web for the web and mobile, and in each desktop app you use (see Install).
- **Every skill appears twice.** The plugin is installed through two routes (for example `dia@dialectic-skills` and `dia@ajitta`, or an upload and a marketplace). Remove one.
- **Skills section missing or greyed out on claude.ai.** Turn on Settings › Capabilities › Code execution and file creation.
- **`dia-confirm` is not found.** It is now `dia-skopos`; it was named `dia-confirm` from 1.1.0 to 1.4.0.
- **`dia-iterate` is not found.** It was renamed `dia-ratchet` in 1.6.0.
- **`dia-ratchet`, `dia-adjudicate` or `dia-techne` does not start.** Each starts only when its name is the first word of the message or when it is selected explicitly (`/dia:dia-ratchet`, `$dia:dia-ratchet`, `@dia-ratchet`, `dia 10`, `dia ratchet`; for `dia-adjudicate` and `dia-techne` the same forms and `dia 11`, `dia adjudicate`, `dia 13` or `dia techne`). `dia <request>` alone never picks them; it replies with the form to send.
- **`$dia:dia-skopos:` does not resolve on Codex.** Put a space, not a colon, after the skill name.
- **The upload is rejected on claude.ai.** Use Customize › Plugins › Upload plugin, not Customize › Skills.
- **claude.ai keeps an old version after Check for updates.** Remove `dia` in Customize › Plugins and install it again from the `dialectic-skills` marketplace; turn on Sync automatically for later releases.

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
upstream/                       material the seven original skills were rebuilt from; never shipped
README.<lang>.md                translations of this file (not shipped)
docs/spec.md                    specification
docs/probes.md                  surface and routing probe results
docs/token-cost.md              measured token cost (the seven 1.2.x skills)
docs/skill-effect.md            the seven 1.2.x skills against no skill, blind-judged
docs/writing-for-models/        dia-regula's draft record and its A/B on dia-adjudicate; never shipped
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
