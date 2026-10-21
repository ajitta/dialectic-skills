# Dialectic Skills (`dia`)

**English** | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

Website: [ajitta.github.io/dialectic-skills](https://ajitta.github.io/dialectic-skills/)

Ten reasoning-and-review skills in one plugin, written to run unchanged on any assistant that loads Agent Skills: Claude (web, desktop, mobile, Claude Code), Codex and ChatGPT. The package is instructions only (Markdown, YAML, JSON), so every skill also works in a chat with no tools. Skill files are in English; each skill replies in the language of your message.

| Skill | What it does | How it starts |
|---|---|---|
| `dia-confirm` | Before work starts: restates the goal, discloses material assumptions, lists only the decisions you must make, then waits for your approval. | by name only |
| `dia-elenchus` | Plato's elenchus: "what is X?", premises agreed one question at a time, contradictions shown, each revision is your new idea. Usually ends in aporia; gives no advice. | by name, or by asking for a Socratic dialogue |
| `dia-brainstorm` | Modern Socratic questioning one question at a time, then your options plus up to three labeled ones, convergence by criteria, a verdict and a brief. Never implements. | by name, or by asking for a Socratic brainstorm |
| `dia-reductio` | Strict reductio ad absurdum in one pass: labeled premises, a Q and not-Q derivation with a rule per line, graded strength, options and a record. | by name, or in words |
| `dia-negative` | Internal critique (narrower than Adorno's immanent critique) in one pass: the target's own standard, strict gaps with cases and "what escapes", the operative purpose with a falsifier, options without forced synthesis. | by name, or in words |
| `dia-warrant` | Toulmin's argument layout with Walton's critical questions in one pass: data, warrant (the unstated one supplied and labeled), backing, qualifier and rebuttal, each question tagged with the part it tests, then the weakest link. Never rules on whether the claim is true. | by name, or in words |
| `dia-conjecture` | Lakatos's proofs and refutations as a dialogue on an "all / always / never" claim you hold: your argument split into steps, one counterexample per message with its check, you rule on each case and pick the repair. | by name, or in words |
| `dia-counterplan` | Mason's dialectical inquiry on a plan or decision: the key assumptions, a plausible contrary for each, a counterplan on the same facts, then you say which assumptions you now hold. Picks no winner. | by name, or in words |
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
4. **Check.** Type `/dia` in the message box. Ten entries, `dia:dia-brainstorm` to `dia:dia-warrant`, should appear. Updates arrive through the marketplace (Check for updates, or Sync automatically).

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

1. **In words.** Ask for the method: "use proof by contradiction on…", "do an immanent critique of…", "Socratic dialogue please…", "how well do the reasons support this?", "find counterexamples to my rule…", "devil's advocate on this plan…". This works on every surface and is the safe default on mobile. It works for `dia-reductio`, `dia-negative`, `dia-elenchus`, `dia-brainstorm`, `dia-warrant`, `dia-conjecture` and `dia-counterplan`.
2. **By name in the message.** Start the message with the skill name: `dia-confirm …`, `dia-refine …`, `dia-iterate …`. Since 1.2.0 this also works on Codex without `$` and on ChatGPT without `@` (owner-checked in the mobile app), which makes it the quickest route on a phone. `dia-refine` and `dia-iterate` are meant to start this way or by an explicit selection: `dia-iterate` never starts from a plain request, and on Claude Code a plain "fix this draft" request rarely loads `dia-refine`.
3. **Explicit selection**, written differently on each surface:

| Surface | Syntax | Example |
|---|---|---|
| claude.ai, Claude desktop, Claude Code | `/dia:dia-<x>` | `/dia:dia-reductio` |
| Claude mobile | `/dia-<x>` or `/dia:dia-<x>` typed in full (the `/` menu does not list it) | `/dia-brainstorm`, `/dia:dia-brainstorm` |
| Codex (plugin) | `$dia:dia-<x>` followed by a space | `$dia:dia-confirm write a backup script` |
| Codex (copied folder) | `$dia-<x>` | `$dia-refine` |
| ChatGPT | `@` then pick the skill | `@dia-negative` |

Since 1.2.0 every skill is visible to the model on Codex and ChatGPT, as on Claude. `dia-reductio`, `dia-negative`, `dia-elenchus`, `dia-brainstorm`, `dia-warrant`, `dia-conjecture`, `dia-counterplan` and `dia-refine` may start when your request matches them; `dia-confirm` and `dia-iterate` are meant to start only when the message begins with their name or when you select them (`$dia:dia-<x>`, `@`). On Codex, a request that spells out `dia-confirm`'s steps ("restate my goal and list the open decisions first") can also load it.

### Options

Options can be written as flags or in plain words, in any language:

- `--target=user|claude|text|all` (`dia-reductio`, `dia-negative`, `dia-warrant`): what is examined. `user` is a claim you state, `claude` is the assistant's own earlier answer (on every assistant), `text` is a pasted text, `all` is each of those present. Without the flag the skill infers the target and states it in the first line.
- `--target=user|claude|text` (`dia-counterplan`): whose plan is examined; `claude` only when you point to the assistant's own earlier recommendation.
- `--mode=audit|ask` (`dia-warrant`): `audit` (default) lays out the whole check at once; `ask` has you fill in each part yourself, one question per message.
- `--max N` (`dia-iterate`): the round cap, default 3.
- Mode and depth (`dia-brainstorm`): `develop` (default) or `stress` ("poke holes"), and `quick`, `standard` (default) or `deep`.
- Criteria (`dia-refine`, `dia-iterate`): anything after the name, for example `dia-refine — check the numbers` or `dia-refine for tone`.

## Skill guide with examples

You don't need any background in philosophy to use these skills. Each one is a way of thinking that people have used for a long time, turned into a routine the assistant follows step by step. Below, each skill gets a plain-language explanation, a prompt to try, and a real session, shortened.

The sessions were run on Claude Code (Sonnet) with this plugin, and the user replies in the dialogue examples came from a simulated user, not a scripted one. The wording you get will differ from run to run. Every prompt works in any language, and the assistant replies in the language you write in.

**Pick a skill by what you want to do**

| You want to… | Use |
|---|---|
| make sure the assistant understood the task before it starts | `dia-confirm` |
| find out what you really mean by a word or an idea | `dia-elenchus` |
| turn a rough idea into options and a plan | `dia-brainstorm` |
| check whether a claim holds together | `dia-reductio` |
| see whether a slogan, policy or promise lives up to its own words | `dia-negative` |
| see how well the reasons behind a conclusion actually support it | `dia-warrant` |
| test an "always" or "never" rule of yours against counterexamples | `dia-conjecture` |
| hear the strongest case for a different plan before you commit | `dia-counterplan` |
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

### dia-warrant: see how well the reasons support a conclusion

**In plain words.** Most everyday arguments don't prove anything; they make a conclusion likely: an expert said so, it worked for them, this causes that. `dia-warrant` lays such an argument out in parts, after the philosopher Stephen Toulmin: the **claim**, the **data** it rests on, the **warrant** (the general rule that gets you from the data to the claim, which people usually leave unsaid), the **backing** for that rule, the **qualifier** (how sure the claim is) and the **rebuttal** (when the rule would not apply). It then asks the standard **critical questions** for that kind of argument (from the argumentation researcher Douglas Walton), each tagged with the part it tests, and names the weakest link: the one part where the support is thinnest, for example "weakest link: warrant". It judges the support, never whether the claim is true.

**Use it when** you want to know how much a "because" can carry: advice from an expert, a comparison with someone else's experience, a prediction about what will happen. **Use a sibling instead** when the claim says "always", "every" or "never" and you mean it strictly (`dia-conjecture`), when you want to know whether it contradicts itself (`dia-reductio`), or when it is a plan you are deciding on (`dia-counterplan`).

**Try:**

```
How well do the reasons support this? "My friend is a personal trainer and she says running ruins your knees, so if I take up running I will get knee problems."
```

**What you get** (real run, shortened):

> **Target:** `user` (inferred), audit mode.
> **Claim:** "if I take up running I will get knee problems." This is stated, with no qualifier. The strength is "will".
> **Data:** "My friend is a personal trainer and she says running ruins your knees" (stated).
> **Warrant W1 (reconstructed):** What a personal trainer says about running and knees is generally reliable. **Warrant W2 (reconstructed):** If running generally harms knees, then a person who takes it up will probably get knee problems.
> **Backing:** none given. **Rebuttal:** none given. **Schemes:** expert opinion (W1) and cause to effect (W2).
> **Critical questions** (seven, all open), among them: **[data]** Is the friend a genuine expert in the relevant field? Open. A personal trainer knows exercise practice. Orthopedics and sports medicine are a different field… · **[warrant/backing]** Is her assertion based on evidence? Open. No studies, clinical experience or observed cases are cited. · **[rebuttal]** Could other factors prevent knee problems in your case (technique, footwear, running volume, body weight, prior injury)? Open. …
> **Qualifier check (compared with my reconstructed W2):** W2 licenses "probably" or "may". The claim says "will", so it is overstated.
> **Result:** **Weakest link: warrant, because "Is her assertion based on evidence?" is left open.** … What would strengthen the link is a stated basis for her view, such as studies, injury data or her own client history. *(then a record: scheme, warrants, questions asked and left open, what would strengthen the link)*
> This audit does not decide whether running harms knees. … If you'd like me to question you slot by slot about your own argument, I can switch to ask mode.

"Stated" means the argument said it; "reconstructed" means the assistant supplied it because the step needs it. The tags show which part each question tests: **[data]**, **[warrant/backing]**, **[rebuttal]** or **[conclusion]**. The result names one part: data, warrant, backing, qualifier, rebuttal or claim.

**Tips**

- Answer an open question in your next message ("she says most of her clients who run have sore knees"); the assistant marks it as answered by you and works out the result again.
- If you don't actually rely on a reconstructed warrant, say so: it is removed, and the assistant asks which rule you do rely on.
- When you check your own argument, the audit ends by offering ask mode (`--mode=ask`): the assistant asks for one part at a time and you fill it in. You can also ask for it from the start; it suits an argument you are still building.
- "No weak link found among the questions asked" is not a proof, and a weak link does not make the claim false.

### dia-conjecture: test an "always" rule against counterexamples

**In plain words.** A rule with "always", "every" or "never" in it can be knocked down by one case that doesn't fit. This skill follows the method the philosopher Imre Lakatos described in *Proofs and Refutations*. First it splits your reasons for the rule into numbered steps. Then it brings one counterexample per message and shows, line by line, how the case fits your rule and still breaks it, and what the case rests on (often just arithmetic on numbers it made up for the example). You decide whether each case counts. When one does, you don't have to throw the rule away: the assistant lists the ways to repair it, such as making the broken step part of the rule, and recommends one, but you pick. The rule then says exactly when it holds.

**Use it when** you rely on a rule of thumb and mean it strictly: "buying in bulk always saves money", "the express lane is always faster", "a pricier bottle of wine always tastes better". **Use a sibling instead** if you mean "usually" (`dia-warrant`), if it is a plan, a policy or a decision (`dia-counterplan`, or `dia-brainstorm` to poke holes), or if the real question is what a word means (`dia-elenchus`).

**Try:**

```
Find counterexamples to my rule: buying in bulk always saves money.
```

**What a session looks like** (real run, shortened):

> **Assistant:** The claim is yours, so I'll treat it as your rule. In my words, C is "every purchase made in bulk saves the buyer money"… Why do you hold this rule? What is your argument for it?
>
> **You:** Well, the big pack costs less per item, and I'd buy the stuff anyway, so I'm just paying less for the same things. …
>
> **Assistant:** Here is your argument split into steps. … 1. [T] "the big pack costs less per item". 2. [T] "I'd buy the stuff anyway". I read this as meaning every item in the big pack gets used, and used up before it goes bad… This is the step I suspect most. 3. [A] The only thing that changes is the price per item… 4. [A] Lower price per item, with the same items used, means lower total spending…
>
> *…you accept the steps, adding that you never counted storage; asked what you would accept as a case against the rule, you name spending more in total, throwing some away, and buying much more than usual just because it was a good deal…*
>
> **Assistant:** Case 1 (both: against C and against L2): a 12-pack of yogurt with a short shelf life. … A 12-pack costs $6.00, which is $0.50 per cup. A 4-pack costs $3.20, which is $0.80 per cup. These numbers are made up for the example. You eat about 4 cups before the date on the pack runs out. The other 8 get thrown away. … Does it save money? No. You spend $6.00 for the 4 cups you eat… This rests on arithmetic from the stipulated numbers. … Does this case count against your claim?
>
> **You:** Yeah, that one counts. … So my rule fails for stuff that goes bad before I can use it.
>
> **Assistant:** … 1. Build L2 into the rule. C′ would be "every bulk purchase that you fully use up before it spoils saves money"… 2. Use a deeper condition… 3. Give up the rule. I recommend option 2… Pick 1, 2 or 3…
>
> **You:** I'll pick option 1, since it's the simplest… The percentage thing in option 2 sounds like too much math for me to do every time I'm at the store.
>
> **Assistant:** Your repair is recorded as an explicit change to the claim. … No longer covered: bulk purchases where you use some and waste some. … Round 2, Case 2 (both: against C′ and against L3…): a shelf-stable box of snack bars. … You normally eat about 6 bars a month. With 24 in the cupboard you eat all 24 within the month… You spend $9.60, where your normal habit would have cost $3.00. … Does this case count against your new claim?
>
> **You:** Yeah, that one counts. … I'd have to say it only saves money if I'd have bought that many anyway.
>
> **Assistant:** You have already named the repair in your own words, and it matches option 1 below. The rules say I lay out the options and you pick, so here they are: … Which do you pick: 1, 2 or 3?

**Tips**

- If a case doesn't fit your rule, say which line of its check is wrong. A bare "no" leaves the case "disputed": neither withdrawn nor counted.
- You pick every repair, even one you have already put into words. The assistant recommends an option, but your choice is what goes into the rule, as in the run above where option 1 was picked over the recommended option 2.
- Each case says what it rests on. "Arithmetic from the stipulated numbers" means the numbers were made up and only the sums are checked; whether real prices look like that is yours to judge.
- Saying "that's not a real bulk buy" to shut out a case is a change of definition; the assistant names it and says what your rule no longer covers.
- After three rounds it offers to stop, and "wrap up" stops it at any time. The best result is "holding against the cases tried", never "proved"; "open" means a case is disputed, or a case counted and no repair was picked.

### dia-counterplan: hear the case for a different plan

**In plain words.** Before a big decision it helps to hear someone argue for a different plan, built on the opposite assumptions. This is dialectical inquiry, a planning method from management research (Richard Mason, 1969). The assistant lists the assumptions your plan rests on, keeps the ones that would change the decision if they were wrong, gives each a believable opposite, and builds the best rival plan on the same facts. The opposites are its own choice, and any reason it gives for one ("supposing…") is a supposition, not a fact about your situation. Then you say which assumptions you now believe; that mix is the result. The assistant gives no verdict at any point, and it says openly that it wrote both sides itself.

**Use it when** you are about to commit to a plan: a move, a job offer, a big purchase, a team's next step. **Use a sibling instead** to be questioned about your idea one question at a time, or to have holes poked in it (`dia-brainstorm`), to check whether a plan lives up to its own promises (`dia-negative`), or to test how well one argument's reasons hold (`dia-warrant`). For whether a single claim is true, just ask.

**Try:**

```
Devil's advocate on this plan: we want to move from our two-bedroom city apartment to a bigger house in the suburbs before our kids (6 and 3) start school next September. The monthly payment is about the same as our rent now, the kids would each get their own room and a yard, and the school there has good reviews. The catch: my commute goes from 20 minutes to about an hour each way.
```

**What a session looks like** (real run, shortened):

> **Assistant:** **Target:** user (your plan). One assistant wrote both sides below.
> **The plan:** … D1: payment is about the same as current rent (supplied by you) … D3: the school has good reviews (supplied by you; single source, reviews) …
> **Assumptions:** *(eight, each marked [T] stated by you or [A] added by the assistant)*, for example A2 [A]: "About the same" covers the full cost of the house: maintenance, taxes, utilities, and a second car or more fuel if needed. …
> **Key assumptions (would the opposite change the decision?):** K1 = A2: yes. If the true cost is well above rent, the "same payment" advantage disappears. K2 = A3: yes. A 2-hour daily commute is the largest cost in the plan. … *(five in all: cost, commute, school, network, timing)*
> **Contraries (my choice):** C1: The all-in cost is clearly above rent once you add a second car or heavier fuel, maintenance, and taxes (supposing, for example, that you must buy a second car for school runs and errands). C2: The commute costs more than it seems… (supposing it makes you miss most dinners and bedtimes). …
> **Counterplan: stay in the city a while, change the space and the school path.** Keep your 20-minute commute and your city network (C2, C4). Stay in the apartment for now, or move to a larger city or inner-ring place if the cost fits. The payment slot is "not supplied": no figure for a larger city home (C1). … Revisit the move when the younger child is nearer school age, with the commute and all-in costs verified first (C5, C1). …
> **Side by side:** … 2. K2 (plan): the commute is tolerable. / C2: it takes away most weekday family time. Favours the plan if: a trial week of the full commute at real hours feels sustainable, or you can work from home some days. Favours the counterplan if: the trial week leaves you missing dinners and bedtimes, or you can't work remotely. …
> One assistant wrote both sides. I give no verdict on which is better.
> **Your synthesis:** For each pair (K1/C1 to K5/C5), which assumption do you now hold: the plan's, the counterplan's, one in your own words, or "can't tell"?
>
> **You:** 1. Cost (K1/C1): Can't tell yet. I haven't added up the property taxes or the upkeep… 2. Commute (K2/C2): I lean toward the counterplan. I can't work from home, so the hour each way is fixed. … *(can't tell on school and network; a lean toward the counterplan on timing)* … One thing I do know is that the kids need their own rooms. The fighting is real, and that's the main reason I want to move…
>
> **Assistant:** … You said the kids need their own rooms… That makes A4 a key assumption. … C6 (my choice): Separate rooms would not much reduce the fighting. Suppose it comes mostly from the age gap and tired evenings… **Record** … K2/C2 commute: counterplan held (leaning). … K6/C6 space: plan held. … **Result:** undetermined. Three pairs are open, and two rulings are leanings you haven't tested. **Kept for the side set aside:** … K6/C6. For the counterplan: the fighting may continue with separate rooms (a supposition, not a reported fact). Deciding observation: how the kids behave when apart. **Written by:** one assistant wrote both sides of this comparison. **Not tested:** … Hearing both sides is not evidence that the plan was tested. … I give no verdict on which plan wins.

**Tips**

- Answer pair by pair: the plan's assumption, the counterplan's, your own wording, or "can't tell". "Can't tell" is a fine answer; the record then says what would decide it. A result of "undetermined" (*teyku*, the Talmud's "let it stand") means at least one pair is still open.
- If you only lean one way, say so. The pair is then recorded as open with your lean noted; it counts as held only if you say you hold that side (the run above predates this rule and wrote "counterplan held (leaning)").
- Something new you bring in, like "the kids need their own rooms", becomes a new pair with its own contrary.
- Rejecting a contrary counts as your ruling; the assistant records it and doesn't argue. It rewrites a contrary only if you show that it misstates your facts or clashes with another one.
- "Which plan wins?" gets no verdict, during or after the inquiry, because the same assistant wrote both sides. Instead it names the observation that would decide the pair you find hardest.

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
- **`dia-warrant`, `dia-conjecture` and `dia-counterplan` check what you gave them first.** If the request belongs to a sibling, they say so in one line and name it: `dia-conjecture` sends a rule you mean only as "usually" to `dia-warrant` and a plan to `dia-counterplan` or `dia-brainstorm`; `dia-warrant` sends a strict "always" claim to `dia-conjecture` and a plan's assumptions to `dia-counterplan`; `dia-counterplan` sends a request to be questioned about your plan to `dia-brainstorm`. Ask again with the skill they name.
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
