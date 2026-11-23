# Dialectic Skills (`dia`)

**English** | [한국어](README.ko.md) | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

Website: [ajitta.github.io/dialectic-skills](https://ajitta.github.io/dialectic-skills/)

Thirteen reasoning-and-review skills in one plugin, written to run unchanged on any assistant that loads Agent Skills: Claude (web, desktop, mobile, Claude Code), Codex and ChatGPT. The package is instructions only (Markdown, YAML, JSON), so every skill also works in a chat with no tools. Skill files are in English; each skill replies in the language of your message. A skill starts only when your message begins with `dia` or with the skill's full name, or when you select it explicitly; a request in plain words starts none. On a phone, type just `dia`: the router skill (`dia-router`) lists the skills, `dia` with a skill's name starts it, and `dia` with a request picks the skill that fits.

| Skill | What it does | How it starts |
|---|---|---|
| `dia-skopos` | Before work starts: shows what you asked for as it reads it and the result it takes the work to be for, lists only what you alone can decide, and asks whether to make the thing you asked for or to work for the result. Then waits for your word. | `dia-skopos …` or `dia skopos …`; never picked from a plain `dia <request>` |
| `dia-elenchus` | Plato's elenchus: "what is X?", premises agreed one question at a time, contradictions shown, each revision is your new idea. Usually ends in aporia; gives no advice. | `dia-elenchus …`, `dia elenchus …`, or `dia <request>` |
| `dia-quaestio` | Modern Socratic questioning one question at a time, then your options plus up to three labeled ones, convergence by criteria, a verdict and a brief. Never implements. | `dia-quaestio …`, `dia quaestio …`, or `dia <request>` |
| `dia-reductio` | Reductio ad absurdum: everything a position relies on, the unstated premises marked, a strict contradiction (a statement and its exact denial), then each way out tested and the one it would take. | `dia-reductio …`, `dia reductio …`, or `dia <request>` |
| `dia-negative` | Internal critique (narrower than Adorno's immanent critique) in one pass: the target's own standard, strict gaps with cases and "what escapes", the operative purpose with a falsifier, options without forced synthesis. | `dia-negative …`, `dia negative …`, or `dia <request>` |
| `dia-warrant` | Toulmin's warrant: the usually unstated rule each step from reasons to conclusion runs on, the questions that kind of step is open to, answered by evidence and never by recall, then how far the conclusion can be relied on. Keeps weak support apart from false. | `dia-warrant …`, `dia warrant …`, or `dia <request>` |
| `dia-conjecture` | Lakatos's proofs and refutations on an "all / always / never" claim: the argument as numbered steps, counterexamples with their checks (your own material first), a repair that builds the missing condition into the claim, then whether "every" stands and what becomes of what rested on it. | `dia-conjecture …`, `dia conjecture …`, or `dia <request>` |
| `dia-counterplan` | Mason's dialectical inquiry on a plan or decision: the key assumptions, a plausible contrary for each with what would show which is true, a counterplan on the same facts, then the course it would take now and what would change it. Says it wrote both sides. | `dia-counterplan …`, `dia counterplan …`, or `dia <request>` |
| `dia-emend` | One review pass over the last answer or a draft: factual errors, logical leaps, missing requirements, repetition. Fixes only confirmed defects. | `dia-emend …`, `dia emend …`, or `dia <request>` |
| `dia-ratchet` | Repeated review rounds in which only outside evidence counts (a search, a tool run or your own material, never the assistant's own re-derivation); what passed is locked; stops on regression, zero defects, verification exhausted, fixed point or `--max N` (default 3). | `dia-ratchet …` or `dia ratchet …`; never picked from a plain `dia <request>` |
| `dia-adjudicate` | Rules on reports that people or other assistants wrote about a text (critiques, reviews, verification reports): checks the text's claims and every report point against sources, gives a verdict for each, says what the rulings leave of the text's conclusion and what no report raised, and lists where its ruling may be wrong. | `dia-adjudicate …` or `dia adjudicate …`; never picked from a plain `dia <request>` |
| `dia-regula` | Checks or writes text a model will follow (a skill file, an agent prompt, an agent instructions file) against four rules: each paragraph one expression with its conditions and fallback, scope words as narrow as meant, fewer instructions each with its reason, one name per thing. A review lists breaches and changes nothing until you pick. | `dia-regula …`, `dia regula …`, or `dia <request>` |
| `dia-techne` | Takes a request to the result it is for, the way a field's top practitioners would: compares the thing you asked for with other ways of getting there, makes what the result needs, and has it checked by something other than the assistant. Stops before any step it could not take back. | `dia-techne …` or `dia techne …`; never picked from a plain `dia <request>` |
| `dia-router` | Not a method: a short entry point. `dia` shows a menu, `dia reductio …` starts a skill by its name, and `dia <request>` picks the skill that fits and says which. Never starts `dia-skopos`, `dia-ratchet`, `dia-adjudicate` or `dia-techne` from a plain request. | first word `dia` |

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

1. **The router: start the message with `dia`.** `dia` alone (or `dia help`, `dia menu`, `dia ?`) lists the skills. `dia reductio <your text>` (also `dia dia-reductio …`) starts that skill (here `dia-reductio`). `dia <your text>` picks the skill whose description fits, names it in one line, and runs it; if two fit about equally, it asks, and if none fits, it answers without a dia skill. It never starts `dia-skopos`, `dia-ratchet`, `dia-adjudicate` or `dia-techne` from a plain request, but replies with the form to send, for example `dia ratchet --max 2 <draft>`. This is the quickest route on a phone: three letters, no hyphen.
2. **By name in the message.** Start the message with the skill's full name: `dia-skopos …`, `dia-emend …`, `dia-ratchet …`, `dia-adjudicate …`, `dia-techne …`, and so on for all thirteen. Since 1.2.0 this also works on Codex without `$` and on ChatGPT without `@` (owner-checked in the mobile app).
3. **Explicit selection**, written differently on each surface:

| Surface | Syntax | Example |
|---|---|---|
| claude.ai, Claude desktop, Claude Code | `/dia:dia-<x>` | `/dia:dia-reductio` |
| Claude mobile | `/dia-<x>` or `/dia:dia-<x>` typed in full (the `/` menu does not list it) | `/dia-quaestio`, `/dia:dia-quaestio` |
| Codex (plugin) | `$dia:dia-<x>` followed by a space | `$dia:dia-skopos write a backup script` |
| Codex (copied folder) | `$dia-<x>` | `$dia-emend` |
| ChatGPT | `@` then pick the skill | `@dia-negative` |

After `dia`, only a skill's full name (with or without `dia-`) picks a skill; a shortened name does not. A name that reads as part of your sentence (`dia negative feedback on my draft?`) is read as a request, and `dia` picks the skill that fits it.

### Options

Options go after the skill's name or the `dia` selector, as flags or in plain words, in any language:

- `--target=user|claude|text|all` (`dia-negative`): what is examined. `user` is a claim you state, `claude` is the assistant's own earlier answer (on every assistant), `text` is a pasted text, `all` is each of those present. Without the flag the skill infers the target and states it in the first line.
- No flags (`dia-reductio`, `dia-warrant`, `dia-conjecture`, `dia-counterplan`): each says in its first line what it took as the target. To have the assistant's own earlier answer examined, say so in words (`dia reductio check your last answer`).
- Being questioned (`dia-warrant`): ask to be questioned, and you fill in each part yourself, one question per message; the assistant judges at the end.
- `--max N` (`dia-ratchet`): the round cap, default 3.
- Mode and depth (`dia-quaestio`): `develop` (default) or `stress` ("poke holes"), and `quick`, `standard` (default) or `deep`.
- Criteria (`dia-emend`, `dia-ratchet`): anything after the name, for example `dia-emend — check the numbers` or `dia-emend for tone`.

### One rule for one conversation

The dia skills are methods you call for one task; none of them sets a rule for a whole conversation. To keep a rule for the whole conversation, paste a sentence such as this at the start of the chat; it makes the assistant say when an answer you asked it to check rests on its memory:

```
For this conversation: only when I ask you to check or review something, say so when your answer rests on recall, never call recall "verified", and say what you did not check. Add no such note to a common fact asked in passing.
```

It lasts for that conversation only, so paste it again in a new one.

## Skill guide with examples

You don't need any background in philosophy to use these skills. Each one is a way of thinking that people have used for a long time, turned into a routine the assistant follows step by step. Below, each skill gets a plain-language explanation, a prompt to try, and a real session, shortened.

The sessions were run on Claude Code with this plugin, and the user replies in the dialogue examples came from a simulated user, not a scripted one. A note under each session gives the version and model it was recorded on. The wording you get will differ from run to run. Every prompt works in any language, and the assistant replies in the language you write in.

**Pick a skill by what you want to do**

| You want to… | Use |
|---|---|
| make sure the assistant understood the task before it starts | `dia-skopos` |
| find out what you really mean by a word or an idea | `dia-elenchus` |
| turn a rough idea into options and a plan | `dia-quaestio` |
| check whether a claim holds together | `dia-reductio` |
| see whether a slogan, policy or promise lives up to its own words | `dia-negative` |
| see how well the reasons behind a conclusion actually support it | `dia-warrant` |
| test an "always" or "never" rule against counterexamples | `dia-conjecture` |
| hear the strongest case for a different plan before you commit | `dia-counterplan` |
| fix the mistakes in an answer or a draft, once | `dia-emend` |
| fact-check something thoroughly, round by round | `dia-ratchet` |
| decide which points in reviews of a text actually hold | `dia-adjudicate` |
| write or check a prompt, skill or agent file so a model follows it as meant | `dia-regula` |
| do a task the way the field's best would, checked by something other than the assistant | `dia-techne` |
| not sure which, or typing on a phone | `dia` (`dia-router`) |

### dia-skopos: agree on the task before work starts

**In plain words.** Before a contractor starts work, a good one walks you through the job: here is what I understood, here is what I think it is for, here is what only you can decide. `dia-skopos` makes the assistant do that, and then asks one thing: should it make the thing you asked for, or work for the result you are after? It waits for your word instead of guessing.

**Use it when** a request is short but what you are after is bigger than its words: a speech, a plan, a test, an email to someone important. **Skip it** for quick questions with one obvious answer.

**Try:**

```
dia-skopos Write a short speech for my brother's wedding.
```

**What a session looks like** (shortened):

> **Assistant:**
> **What I'd make:** a toast you can deliver in about 2–3 minutes … It would mix warmth and light humour, open with who you are, tell one personal story about your brother, welcome his partner, and end with a raised glass. My reading adds that "short" means under 3 minutes spoken and that the tone is mixed. It leaves out formal roles (best man, officiant) unless you hold one. …
> **The result (my reading):** your brother and his partner feel truly seen and celebrated by you, the room warms to them as a couple, and you stand up feeling confident rather than dreading it. What limits this most is material only you have: real names, a true story, and how comfortable you are speaking in public.
> **What only you can decide** (with my default): names; a story or two; tone; your role and length limit; anything to avoid.
> **The choice.** **As asked:** a short wedding speech, as polished as I can make it with what I have. Nothing gets sent or spent. **For the result (proposed):** "Help me give a toast at my brother's wedding that makes him and his partner feel truly celebrated and that I can deliver with confidence." With this, the written speech becomes one way to get there among others. …
> If my sentence doesn't fit, tell me the result in your own words. A plain "proceed" takes my sentence, and "as asked" keeps to the speech alone.
>
> **You:** dia-techne Go ahead. My brother is Minho, marrying Sara; I'm the best man. He taught me to ride a bike, even though he's younger. Warm, one light joke, about 3 minutes. What I'm after is that the room laughs once and Minho is moved.
>
> **Assistant:** **Outcome I worked toward (yours):** the room laughs once and Minho is moved. I judged everything below by those two moments. … I compared a full script with speaking from bullet-point cue cards. Cue cards can sound more natural, but the line meant to move Minho only works if it's worded exactly right, and nerves tend to blur it. So I wrote the full script. … **The laugh:** the younger brother teaching the older one is the only joke, as you asked. … **The moving moment:** "I've got you" comes back at the end, said back to him. … Whether the room laughs once and Minho is moved can't be known until the wedding; the read-aloud test above is the best check before then.
> *(Recorded on 4.2.0, Claude Opus 5.5.)*

**Tips**

- **Say what you are after in one sentence of your own** ("What I'm after is …"). The work is then done for that sentence, and it is the largest single lever on the result: in our runs the same request reached a clearly better result when the user added it. A bare "proceed" takes the assistant's guess, which on a precise request is often narrower than what you want.
- "As asked" keeps to the thing you named, made as its best practitioner would make it. Corrections plus "proceed" count as approval of the corrected request.
- "Looks good", a question or silence do not count as approval; the assistant keeps waiting and does none of the task.
- On your go-ahead the work passes to `dia-techne` where it is installed; start your reply with `dia-techne` to be sure. The review covers that one task; start a new task with `dia-skopos` again if you want the same check.

### dia-elenchus: find out what you really mean

**In plain words.** This is the method Socrates uses in Plato's dialogues. You say what you think something is ("a good teacher is…"). The assistant doesn't argue back or give its own view. It asks about one concrete case at a time, and each case is chosen so that your own answers start to pull against your definition. You then fix the definition in your own words. Often you end up stuck, and the Greek word for that is **aporia**. Being stuck is a result here, not a failure: you now know exactly which part you don't know, so you won't build on a wrong assumption.

**Use it when** you rely on a word that feels obvious but drives real decisions: a good teacher, a fair split, a successful project, a healthy relationship. **Not for** getting advice; it gives none during the dialogue.

**Try:**

```
dia elenchus I think a good teacher is one whose students get high test scores.
```

**What a session looks like** (real run, shortened):

> **Assistant:** We're looking at **good teacher**. So in your words, a good teacher is one whose students get high test scores. Suppose a teacher gets a class of students who already scored at the top before the year began. The teacher does very little, and the students score just as high at the end of the year. Is that a good teacher?
>
> **You:** Hmm, not really, they'd have scored high anyway. I guess it's more about whether the scores go up because of the teacher?
>
> **Assistant:** ① A good teacher is one whose students get high test scores (definition) ② A teacher who does little, with students who would have scored high anyway, is not a good teacher (agreed). So ① and ② can't both stand. You've chosen to change ①. The shift: "high test scores" → "the scores go up because of the teacher". … Suppose a teacher raises scores by drilling the test format and answer tricks. A month after the test, the students remember almost nothing … Is that a good teacher?
>
> *…a badly made test, a teacher who teaches through fear, the user's daughter's maths teacher who "barely moved her scores but she started loving maths", the class that would have done well anyway…*
>
> **You:** A rough try: a good teacher is one whose teaching makes students learn something real and want to keep going, more than they would have without that teacher. But I honestly don't know how you'd ever tell that for kids with tutors, so I think I'm stuck there.
>
> *…the definition passes one test, then falls on a teacher who reaches three of thirty; its repair, "most of the students", falls on a class where the teacher reaches only the three who had nobody else…*
>
> **You:** No, that's wrong, that teacher is good, those three are exactly the kids who needed a teacher. So "most of the students" doesn't work either, it's more like the ones who actually depended on them, and now I'm stuck again.
>
> **Assistant:** … It seems we've found out that we don't know what a good teacher is. That's the result, not a failure. You now know which part you can't yet say, so you won't build on "high test scores" as if it settled the question. … **Result: aporia. You no longer hold any definition of a good teacher, and the question you take away is which students' difference counts, and why.** *(then the record: eight definitions and how each fell, the ten agreed premises, the ideas born, what you now know you don't know, what a next definition would have to do (for example "⑩ Take in a teacher who reaches the three with nobody else when the rest had other help"), what was not examined, what to check, and the question to take away)*
> *(Recorded on 5.1.0, Claude Opus 5.5 at effort medium; the user was simulated.)*

**Tips**

- Short, honest answers work best. "I'm not sure" is a fine answer.
- It asks first for cases from your own situation (your team, your last month, the people involved). Real cases are where it finds the most; it turns to made-up ones when yours no longer test the definition.
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

> **Assistant:** This will be a quick session of about 4 questions. … Here's how I understand your idea: you want to earn extra income using your weekends, alongside what you already do. … You haven't said how much you want to earn, what kind of work, or what the money is for, so I've left those open. Is that right, or did I assume something you didn't mean?
>
> **You:** Yes, that's right, I work full time in an office on weekdays. The money is for a trip next summer so I don't have to touch my savings.
>
> *…about $300 a month, about 8 hours a weekend, mostly Saturday…*
>
> **Assistant:** Almost there, two more questions. What's something you already know how to do that someone has paid you for, or regularly asks you to help with?
>
> **You:** Nobody's ever paid me, but I'm good at photography and have a decent camera and two lenses. Friends always compliment my photos.
>
> *…you list your own options (photos for local shops, prints at a weekend market, pet portraits in the park), the cheapest, boldest and do-nothing versions, and two limits: no selling face to face to strangers, no long evenings of editing; the assistant adds three of its own (second shooter for an event photographer, stock licensing, a Saturday shift job); you pick three criteria: startup cost under $200, about $300 without loads of unpaid editing, and enjoying it…*
>
> **Assistant:** **Verdict: Open.** You're ready to decide which of your top two to try first: photos for local shops or second-shooting. Settle one thing first: will the bakery or florist actually pay for photos? … **Risky:** the bakery and florist want photos and will pay for them, beyond liking your work. … **Not tested this session:** I didn't press the idea with counterexamples or ask what would make you drop it. … **Next step:** Next Saturday, give the bakery or florist a few free photos as you planned. When you hand them over, ask whether they would pay for photos like these every month, and roughly how much.
> *(Recorded on 5.1.0, Claude Opus 5.5 at effort medium; the user was simulated.)*

**Tips**

- Say how hard it should push: "keep it quick", "go deep", or "poke holes" for a tougher stress test.
- Say "wrap up" at any point to jump to the verdict and the brief.
- A verdict of "open" means the key assumption still needs a real-world test, and the brief says which one.

### dia-reductio: check whether a claim holds together

**In plain words.** Reductio ad absurdum, or proof by contradiction: take a position at its word (a claim, a plan, a set of rules, an argument), list everything it has to rely on, and see whether all of it can be true together. The assistant marks each premise it had to add itself, because a premise the position needs and nobody said is often the most useful thing it finds. A contradiction counts only when it is strict: a statement and its exact denial, reached by logic, a definition or arithmetic, run with a tool where one is available. Then the assistant gives its own judgment. It tests each way out (giving up a commitment, or narrowing the position just far enough) the same way, says what each costs the thing the position is for, and says which it would take. Where you need the thing itself, such as corrected wording, it writes it.

**Use it when** you are about to rely on a rule, a promise or a plan with numbers in it and want to know whether it can all be true at once: a notice, a policy, a confident rule with "always", "never" or "everyone" in it, or your own position before you defend it. **Not for** judging how strongly reasons support a likely conclusion; that is `dia-warrant`.

**Try:**

```
dia reductio Please take a look before I post this in the group chat for the December cup. Like in the league, it says that kids who came to every November practice will play at least half of every match. 16 kids, 8 on the field, two 20-minute halves, so it fits exactly and I don't think there's a problem. The parents are sensitive about playing time, so tell me whether I can post it as is, or what I should change.
```

**What a session looks like** (real run in Korean, translated and shortened):

> **Assistant:** **Under review:** the notice as you described it. I haven't seen its text yet; paste it and I'll go through it wording by wording.
> **I don't recommend posting it as is.** "Fits exactly" means there are 0 minutes to spare. So there are three ways the promise can break: 1. if the players on the field drop below 8 in even one match (a sending-off, an injury that can't be substituted, a shortened match); 2. if one goalkeeper plays all 40 minutes, the others' share falls below 20 minutes; 3. if the cup limits the squad per match, a child left out of the squad doesn't play that match at all. Either way, **you must add an exception clause.** …
> **What the notice assumes:** … Minutes available: 8 places × 40 minutes = **320 minutes** (computed). Minutes promised: 16 × 20 minutes = **320 minutes** (computed). Premise I added ①: all 16 came to every November practice. "Fits exactly" seems to assume it. **Needs checking.** Premise I added ②: the number on the field can drop during a match. …
> **How the contradiction arises:** 1. 16 children must each play 20 minutes or more, so at least 320 minutes are needed (the promise + ①). 2. If one child is sent off and the team plays 10 minutes with 7, the minutes actually played are 310 (② + computation). 3. 320 or more are needed and there are only 310, so the promise can't be kept. … This contradiction holds only if ① and ② are both true. … I checked the calculations by hand; no tool was used.
> **Wording you can add right now:** "However, exceptions apply in unavoidable situations such as a sending-off, injury or a shortened match, or where cup rules (squad, substitutions) make it impossible; in that case we will make it up as far as we can in the next match." …
> **Give me the answers and I'll sort out the rest:** 1. **How many children actually came to every November practice?** If 16, the problem above applies as is. If 15 or fewer, there is slack and "at least half" can stay. 2. **What are the cup's squad limit and substitution rules?** … If the squad limit is under 16, "every match" has to change. 3. **Will you change goalkeepers at half-time?** … 4. **Did you write "at least" to leave room for some children to play more?** … 5. **What is your plan for the children who aren't covered?** …
>
> **You:** I've coached youth football for 8 years and never once failed to keep a playing-time promise; I know that best. November practice was Tuesdays, Thursdays and Saturdays from the 3rd to the 21st, 9 times, and 14 kids came to all 9. In the cup you can only name 13 per match, up to 5 substitutions per match, and a player who comes off can't go back on. I don't know about changing the goalkeeper, why I wrote "at least", or the plan for the kids who missed practice.
>
> **Assistant:** **On the cup rules you gave me, the notice as it stands can't be kept in a single match.** It doesn't take bad luck; the numbers alone decide it. … There are 14 children covered. The match squad is at most 13. So in every match at least 1 covered child doesn't make the squad and plays 0 minutes.
> I don't doubt that you have never broken a playing-time promise in 8 years. But that record doesn't change these numbers. In the league there was probably no squad limit, so the problem never showed; that is my guess.
> … With 5 substitutions and no re-entry, at most **13** can play 20 minutes or more in a match: 3 play all 40, and the other 5 places change exactly once at half-time, so 10 play 20 each. I checked this by computing every possible case, with your rules as given. … To give all 13 their 20 minutes, **all 5 substitutions must be used at half-time.** …
> **How to fix it:** **A. Narrow the promise to "matches where the child is in the squad" (my recommendation)** … **B. Promise over the playing time of the whole cup** … impossible if you play only one match: if you go out in the first match of a knockout, it can't be kept. …
> *…then wording for A, and what only the coach can decide: the 2 children who missed practice, the order in which children are left out, and whether half-time substitutions count among the 5…*
>
> **You:** But on match days two or three kids usually don't show up anyway, so then everyone can play, right? And the cup is Saturday 12 December, two group matches, and only the group winner goes to the semi-final on Sunday the 13th. I don't know whether half-time substitutions count in the 5, or about the two who missed practice and the order.
>
> **Assistant:** **You can't stake an "every match" promise on "two or three usually don't come".** If even 1 of the 14 is absent that day, all the rest can play at least half of every match. But on a day all 14 come, it is a promise that can't be kept from the start. If the 2–3 who are absent are the 2 who missed practice, all 14 still come. A promise to parents who are sensitive about playing time mustn't depend on children being absent.
> Instead, your schedule allows **a promise over Saturday's two matches together**, and that holds even if all 14 come. … **Match 1:** A, B, C 40 minutes; D to M (10 children) 20 minutes each; N left out. **Match 2:** N, A, B 40 minutes; D to M 20 minutes each; C left out. **Result:** all 14 play 40 minutes or more over the two matches, half of the 80. I checked this assignment by computing it, taking the tightest case, with half-time substitutions counted in the 5. …
> **Notice wording:** "Players who attended all 9 November practices will play at least half (40 minutes) of the two group matches on Saturday the 12th combined. Cup rules allow 13 in the squad and 5 substitutions per match, so some players may be left out of a match; they will play more in the other. If we reach the semi-final on Sunday the 13th, players in the squad will play at least half. Exceptions apply in unavoidable cases such as injury, sending-off or a shortened match."
> **For you to decide:** You can use the wording above whatever you decide; only what else goes into the notice changes. …
>
> **You:** Ah, the two who missed practice tend to miss match days too, so absences won't fix it. Got it. I'll post the wording you gave. Thanks, that's all.
> *(Recorded with the 5.0.0 text of the skill, Claude Opus 5.5 at effort medium; the user was simulated.)*

In the first reply the assistant said what it could settle at once (the notice needs an exception clause) and asked everything it needed in one go, each question with what its answer decides. The coach's 8 years without a broken promise moved nothing, and the assistant said why; the facts the coach supplied (14 children, a squad of 13) decided the matter.

**Tips**

- Answer what you can and say "I don't know" for the rest; the assistant judges on what there is and says what is still open.
- A fact the assistant lacked, a premise you don't hold or a term it misread moves the result exactly as far as it reaches. Experience, authority and repetition move nothing.
- Dropping a premise, or saying you meant a word otherwise, makes a changed position: the one first stated has fallen as it was read, and the new one is tested again.
- Every fact says how it is known: a tool ran it, you supplied it, one source, or the assistant's recall, which is never called verified. A way out it did not test is named as untested.
- To test the assistant's own previous answer, write `dia reductio check your last answer`; it says that its author is examining it.

### dia-negative: hold a claim to its own standard

**In plain words.** Instead of judging a claim by your values, judge it by its own words. Take what it promises ("anyone can raise a problem at any time") and look for real cases where it doesn't deliver. Then ask what the claim actually does in practice, as a guess you could check. The name comes from the philosopher Adorno's "negative dialectics"; this skill uses a narrower, practical version of his idea, called internal critique.

**Use it when** a slogan, policy, mission statement or plan sounds good and you want to see what it leaves out. **Not for** explaining what code, a command or a setting does, or for a general review.

**Try:**

```
dia negative "We have an open-door policy, so anyone in the company can raise a problem with management at any time."
```

**What you get** (real run, shortened):

> **Target:** a quoted statement, read as `text` (someone else's policy statement). If it's your own claim, say so and I'll rerun it as `user`.
> **Claim:** … **Reading tested:** "can" means "is actually able to": there is a route that is open to them. The sentence's own "so" points to this reading. …
> **Result: open.** 1 firm finding, 1 conditional. Firm: the claim says anyone can raise a problem **at any time**, but the open-door policy only gives access while a manager is actually there.
> **Its own standard:** "anyone in the company" (everyone, no exceptions); "at any time" (every moment); "We have an open-door policy, **so**…" (the policy alone is enough to produce both).
> **F1 (firm): the policy can't deliver "at any time".** A time when no manager is reachable: night shift, everyone in a meeting, on leave or travelling. … One possible time with the policy in place and no manager reachable is enough to break the "so". *What escapes:* some problems come up when nobody is behind the door, and they may be the urgent ones.
> **F2 (conditional): "anyone" and the door.** Remote or off-site staff, or people on other shifts: the only route the claim names is a door … *Conditional on* whether the company has such staff and whether "open-door" also covers email, chat or calls.
> **What the sentence does in practice (an inference):** it turns "you're allowed to" into "you're able to". … It also shifts responsibility onto employees: if a problem was never raised, the sentence suggests it could have been. *Would be falsified by:* a named deputy, set hours, an escalation path, or a written channel that someone checks.
> **Options:** A. narrow the claim; B. keep it and state what it leaves out; C. change the practice (a route that doesn't depend on someone being present); D. look further at F2. **Recommended: C**, resting on F1. … The decision is yours.
> *(Recorded on 5.1.0, Claude Opus 5.5 at effort medium.)*

**Tips**

- Findings marked conditional depend on facts about your situation, so tell the assistant those facts. If you say a standard isn't really the claim's, it drops the findings that used it and runs again.
- It recommends an option but never picks one for you.

### dia-warrant: see how well the reasons support a conclusion

**In plain words.** Most everyday arguments don't prove anything; they make a conclusion likely: a trial went well, an expert said so, it worked for someone else. Reasons don't reach a conclusion by themselves. A rule takes them there, usually unsaid ("what the film did on one line, it will do on every line"), and every such rule has cases where it fails. The philosopher Stephen Toulmin called this rule the **warrant**. `dia-warrant` lays out the steps from the reasons to the conclusion, states the rule each step runs on (marked as its own reading where you left it unsaid), and asks what that kind of step is open to: what else changed, whether the measure follows the thing, whether the expert's knowledge is about this step, whether the like case is alike where it matters. A question is closed only by evidence (the argument's own words, your files, read or computed with a tool where one is available, your answers, or a source it cites), never by the assistant's memory. Then it judges: what the reasons do and don't support, which step is weakest, and whether it would act on the conclusion as things stand. Weak support is kept apart from "false". Where you need something to act on, it makes it: the reply to send, the figure that would have to be reached, the check that would settle what is open.

**Use it when** you want to know how much a "because" can carry: a trial result, advice from an expert, a comparison with someone else's experience, a prediction about what will happen. **Use a sibling instead** when the claim says "always", "every" or "never" and you mean it strictly (`dia-conjecture`), when you want to know whether it contradicts itself (`dia-reductio`), or when it is a plan you are deciding on (`dia-counterplan`).

**Try:**

```
dia warrant Mr Park in purchasing ran a 12-week trial and wrote a memo (memo.md) proposing we switch all our packaging film from supplier A to supplier B from 4 January 2027: seal defects fell from 0.92% to 0.34%, and it saves about 55 million won a year. I have to sign and reply by Friday the 27th for the Q1 order to go in. Please look at it together with the trial data (trial_weekly.csv) and tell me whether I can sign as is, or what I should reply to purchasing.
```

**What a session looks like** (real run in Korean, translated and shortened):

> **Assistant:** **I'd not sign now for switching lines 1, 2 and 3 as the memo says.** But if you get one piece of data from purchasing before Friday, the judgment settles. … The memo's conclusion is "switching all lines to B from 1/4 cuts defects from 0.92% to 0.34% and saves 55.16 million won a year."
> **On line 2, the case for B's film is fairly solid.** From week 3 on, ten weeks in a row at 0.29–0.31%.
> **The baseline is inflated.** The trial ran only on line 2, but it was compared with A's average over three lines (0.92%). A's figure on line 2 is 0.81%.
> **Whether B does the same on lines 1 and 3 was never tested.** This is what the decision leans on most.
> **The season wasn't filtered out.** A's figures are June–August, B's trial September–November. …
> **I recomputed the figures (directly from the CSV):** weeks 2–12, 2,883 defects in 847,800 packs, 0.340%, the same as the memo. … Comparing line 2 with line 2 (0.81% → 0.34%), the net saving is **about 41.4 million won**. …
> **Data the memo didn't use:** during the 12 weeks, lines 1 and 3 presumably kept running on A's film. Quality inspects every pack, so **A's defect rate for the same period is probably already on record.** … No new trial is needed, only the record.
> **Other things to check (what I can't know):** 1. **Whether the line 1 and 3 sealers run stably at 150 ℃ (B recommends 140–160 ℃).** A's film is recommended at 125–145 ℃, so that temperature has never been tried on the other lines. …
> *…then a draft reply to purchasing asking for that record and three other checks, and what only you can decide…*
>
> **You:** Lines 1 and 3 have the same 2014 sealer model, and the jaws only go up to 145 degrees; we run A's film at 130. Line 2's sealer is new from 2023 and goes to 170. The first trial week (the week of 31 August) line 2 was under maintenance, so we ran B's film on line 3 at 145. And purchasing collected the data for three months, and the plant manager said it was fine.
>
> **Assistant:** … **Don't sign for switching all lines; reply that you'll switch line 2 only.** For lines 1 and 3 the support is worse than weak: the data there is against the switch.
> **Lines 1 and 3 top out at 145 ℃.** Even at the machine's maximum that is the bottom edge of B's 140–160 ℃ range. There is no temperature margin at all.
> **There is exactly one week of B's film on a line 1 or 3 sealer.** Week 1, left out of the memo as "initial setup, excluded from analysis", was in fact line 3 at 145 ℃, and the rate was **1.60%**. A's figure on the same line 3 was 0.99%. …
> **On the three months of work and the plant manager's approval:** the data is enough to support the line 2 result. The plant manager was told the memo's results orally on 11/19. Whether that report said lines 1 and 3 only reach 145 ℃, the memo doesn't show. If it didn't, that approval didn't decide this question. …
> **An easy-to-miss timing problem:** … if only line 2 switches, lines 1 and 3 need **390 rolls** of A's film for Q1. A's lead time is 3 weeks, so to cover production from 1/4 you **must order before mid-December**. …
>
> **You:** The first week was the first time anyone had loaded B's film, so we struggled mounting the rolls and setting the tension. Even in the second week, after moving to line 2, the first two days had quite a few defects.
>
> **Assistant:** That's a fair point. With this fact, **week 1's 1.60% can't be used as evidence that B's film is bad at 145 ℃.** I withdraw what I said last time, that "the data is against the switch". … Week 2 shows how big the setup effect is: on line 2 at 150 ℃ the week came to 0.71%. If the other three days were at the stable level (0.31%) with the same daily output, the first two days work out at roughly 1.3% (by hand). … So for lines 1 and 3 the judgment moves from "the evidence points the other way" to **"there is no evidence at all"**.
> **What stays:** … Lines 1 and 3 are 60% of the volume. At break-even, B's film on lines 1 and 3 has to be **below 0.875%** to cover the price rise. A's film is at 1.00%, so the margin is only 0.125 points. …
> So the conclusion is the same: **switch line 2; there is still no basis to sign for lines 1 and 3.** But the reason for holding lines 1 and 3 has changed from "an unfavourable result" to "never tried", and the remedy for that is a short trial. …
>
> **You:** December has slack on line 3, so we can run a trial on line 3 from 7 to 18 December.
>
> **Assistant:** Two weeks, Monday 7 to Friday 18 December, **is enough to judge lines 1 and 3.** … **1. Exclude setup by the day, not by the week.** … Get **daily defect records**, and fix the rule in advance, for example "count from the day the rate has been stable two days running". If you pick the days to exclude after seeing the results, the number can't be trusted. **2. Use line 1 as the comparison.** … Line 1 is the same 2014 model as line 3 and runs A's film at 130 ℃ over the same two weeks. … the seasonal effect drops out of the comparison. … **Proposed rule:** switch if line 3's stable rate with B is **below 0.875%** and **clearly below line 1 with A** over the same period. …
> **Where the schedule bites:** 1. **Film for the trial:** two weeks needs about 30 rolls. B's lead time is 2 weeks, so to have it on 12/7 you **must order today (11/23)**. … 2. **The A order comes before the result:** for production from 1/4, A's order deadline is **12/14**, but the trial ends on 12/18. …
> **Draft reply (final):** "Mr Park, thank you for putting the trial together. **1. Line 2: agree to switch to B from 2027-01-04** (Q1, 260 rolls). **2. Lines 1 and 3: decide after an extra trial on line 3, 12/7–18.** … Decision: switch if the stable rate is below 0.875% and below line 1 on A (decided around 12/21, switch in January). **3. Please confirm:** whether 30 rolls of B can arrive by 12/7 (ordered today, or leftover rolls) …"
>
> **You:** There are 30 rolls of B's trial film left in the warehouse. We can run the December trial with those. Thanks, that's all.
> *(Recorded with the 5.0.0 text of the skill, Claude Opus 5.5 at effort medium; the user was simulated.)*

The memo spent its words on the line 2 result; the decision leaned on a step it never stated, from line 2 to every line. The assistant computed from the trial file rather than from the memo's summary, and named data the memo didn't use. When the user supplied the setup fact, it withdrew exactly the claim that fact undid and kept the rest; three months of work and the plant manager's word did not settle the line 1 and 3 question.

**Tips**

- Give it the files the argument rests on. It reads them before it judges, and where a tool is available it computes from them.
- A fact you supply that answers an open question is marked as supplied by you, and the step is judged again, for or against. A fact that shows a defect in the assistant's reading moves it exactly as far as it reaches, as the setup fact did above.
- Someone's standing counts only for the step their knowledge is about, as far as its basis is given; it does not move a step that rests on arithmetic or on the record. Repetition moves nothing.
- If the argument is yours and you don't rely on a rule the assistant supplied, say so: it is removed, and the assistant asks which rule you do rely on.
- To build the argument yourself, ask to be questioned: the assistant asks one thing a message (what exactly you claim, what you have to go on, how that gets you there, why that rule holds, how sure you are, when it would not apply), takes your answers in your words, then judges.
- "No step gave way to the questions asked" is support, not proof, and weak support does not make the claim false.

### dia-conjecture: test an "always" rule against counterexamples

**In plain words.** A claim about every case ("all", "always", "never", "not one") can be knocked down by one case that doesn't fit. This skill follows the method the philosopher Imre Lakatos described in *Proofs and Refutations*. It sets out why the claim is held as a few numbered steps, marking the steps it supplied, and for a claim about the world it says beforehand what would count against it. Then it brings the cases most likely to count, first from your own material (records, files, examples), each with its check condition by condition and with what it rests on. Whether a case counts is the assistant's to say wherever the check settles it. A case that counts brings the claim down as worded, and the repair builds the missing condition into the claim ("every A that … is B") instead of listing the case as an exception; the repaired claim is put to the cases again. Then it judges whether "every" stands, what can be said in its place, and what becomes of the decision that rested on it, and makes what you need to act on.

**Use it when** you, or someone whose word you are about to act on, rely on a rule and mean it strictly: "not one booking that got a reminder was a no-show", "buying in bulk always saves money", "the express lane is always faster". **Use a sibling instead** if you mean "usually" (`dia-warrant`), if it is a plan, a policy or a decision (`dia-counterplan`, or `dia-quaestio` to poke holes), or if the real question is what a word means (`dia-elenchus`).

**Try:**

```
dia conjecture Minsu wrote memo_minsu_deposit.txt proposing we drop the booking deposit (10,000 won a person) from 1 December. He says that since we started reminder texts in September, not one booking that got a text was a no-show. I've also put in online_bookings_0901-1121.csv and my phone booking ledger, phone_ledger_0901-1121.csv. Is Minsu really right? Can I approve it as is, or should I do something different?
```

**What a session looks like** (real run in Korean, translated and shortened):

> **Assistant:** **Conclusion: your own ledger already shows Minsu's claim is false. I'd not approve the plan as it stands.** Minsu's claim is "no booking that got a reminder text was a no-show, so reminders alone will do without a deposit." But the phone ledger has 5 bookings, 36 people, that got the text the day before and were no-shows. Minsu got 0 because he looked only at online bookings, and all 313 online bookings had paid a deposit. An option instead: **keep the deposit only for bookings of 5 or more and drop it for 2–4.** Keep the reminders as now.
> **How I checked:** I tallied both CSVs in Python. The memo's figures (313 bookings, 284 visits, 29 cancellations, 301 texts sent, 0 no-shows) match the online file exactly.
> **Cases that break Minsu's claim (phone ledger):** 10/2 Kim○○ (Design) 10 people; 10/2 Kwon○○ (Goods) 6; 10/2 Han○○ (Construction) 7; 10/23 Seo○○ (Electronics) 8; 11/12 Lim○○ (Trading) 5. All five are marked `text the day before O`, `result no-show`, `company group / unreachable`.
> **What Minsu's argument left out:** the online 0 is not the result of "reminders only"; it is "deposit and reminder together". … Online, deposit and reminder together: 0/301 no-shows. Phone: 5/89 (about 5.6%). Company groups alone: 5/21 (about 24%).
> *…a table by party size (phone bookings of 2–4: 0 no-shows; 5 or more: 5), the option put back to the ledger, and the payment-screen figure in the memo marked as not checked…*
> **What only you know (the judgment changes with the answers):** 1. **Did you take deposits on phone bookings?** If not, the phone ledger is the actual result of "reminders only", and the option above fits best. If you did, group no-shows happened even with deposit and reminder together, and groups need something stronger … 2. **Is the ledger's "text the day before" the 3 pm automatic text, or one you sent yourself?** If it is different, "no-show despite a reminder" gets a little weaker. But Minsu's "no no-shows once a text is received" still breaks.
>
> **You:** I don't take deposits on phone bookings; getting transfers is a hassle, so I never did. The day-before text is a reminder I've sent myself the afternoon before since September. But three of those five teams were on 2 October. There was a typhoon that day, with heavy wind and rain, and hardly any customers could come. And Minsu looked at three months of booking records before he wrote it, so he can't be wrong.
>
> **Assistant:** **The conclusion stands. Minsu's claim is false, and I'd not approve the plan as it stands. What you told me makes the grounds clearer.**
> **1. No deposit on phone bookings:** then the phone ledger is three months of actual results for "no deposit, reminder only", which is exactly what Minsu proposes from December. 5 no-shows in 89 bookings: 2–4 people, 0; 5 or more, 5 of 26. A text you sent yourself still meets "got a reminder".
> *(The run mixed two counts here: 89 is the phone bookings that got a text, while 26, like the 66 below, counts all 92 phone bookings by party size. Of the 89, 64 were for 2–4 people and 25 for 5 or more.)*
> **2. The typhoon on 10/2:** even if those three are put down to the weather and left out, Minsu's claim doesn't hold. Two remain, 10/23 Seo○○ (Electronics) 8 people and 11/12 Lim○○ (Trading) 5. Both got the text and were no-shows. "Not one" is false if there is one. …
> **3. Online on the same day:** … the 5 online bookings with a deposit: 1 team came, 4 were cancelled in the system. Kim○○, a phone booking for 2: called to cancel that day. The 3 company groups with no deposit (23 people): "unreachable". The typhoon explains why they didn't come. It doesn't explain why they didn't get in touch. …
> **4. "Minsu looked at all three months":** Minsu's figures aren't wrong; I checked, and they match the online file without a single difference. But going by the memo's attachment, he looked only at online bookings. … And however carefully anyone looked, the five entries in the ledger remain.
> **The recommendation stands:** drop the deposit for bookings of 2–4 from 1 December … Keep it for 5 or more … Keep sending reminders. Consider taking deposits on phone bookings of 5 or more in December as well …
> **Words you can pass straight to Minsu:** "The online numbers are right. But that's with deposit and text together. On my phone bookings, text only, there were five group no-shows (two even leaving out the typhoon day). So let's drop the deposit only for 4 or fewer and keep it for 5 or more."
>
> **You:** Ah, Minsu said the people who quit at the payment step are mostly bookings for two or three. Groups' organisers pay the deposit straight away on the company card, so I've hardly ever seen a group not book because of the deposit. Then I'll do as you said: drop it only for 4 or fewer and keep it for 5 or more.
>
> **Assistant:** … **What to check when Minsu changes the settings on 30 November:** 1. **The threshold:** that "4 or fewer, no deposit; 5 or more, 10,000 won a person" is what went in. … 2. **Changes in party size:** decide whether to take a deposit when a booking for 4 later grows to 6–8 … Left alone, groups can dodge the deposit by "booking for 4, then adding people". 3. **Bookings already made:** … **Early January:** count the no-shows among December bookings of 4 or fewer taken without a deposit. The evidence now is 66 phone bookings, not a large sample. …
>
> **You:** Okay, I'll tell Minsu that and check those three things when he changes the settings. Thanks, that's all.
> *(Recorded with the 5.0.0 text of the skill, Claude Opus 5.5 at effort medium; the user was simulated.)*

The cases that decided it were already in the user's own ledger, which the claim's author had not looked at. Leaving out the typhoon day removed three of them and not the other two, so the claim still fell. "He looked at three months of records" moved nothing; the assistant said what Minsu's figures did get right. In place of "every", the assistant said what the evidence does support (no no-shows in 64 reminded phone bookings of 2–4 without a deposit; all five in groups of 5 or more) and rebuilt the decision on that.

**Tips**

- Give it the records behind the rule. Cases from your own material come first, and a case is raised only with a check it can write out.
- To dispute a case, name what is wrong with it: a condition of its check that fails, a word read wider than the rule means it, a fact the assistant lacked. Where that holds, the case is withdrawn or narrowed exactly that far. Disagreement alone, repetition and someone's standing move nothing.
- Saying "that's not a real A" or "by A I meant …" after a case that met the claim as read changes the claim: the assistant shows the old and new wording and what the new one no longer covers, then tests the new one.
- Listing a case as an exception is not a repair, and neither is redefining a word to shut the case out. A repair builds the condition behind the case into the claim, and is tested before it is offered; one that was not tested is said to be untested.
- Holding against the cases tried is not proof. The assistant says which kinds of case were tried, which were not, and where a counterexample would most likely be found.

### dia-counterplan: hear the case for a different plan

**In plain words.** Before a big decision it helps to hear the case for a different plan, built on the opposite assumptions. This is dialectical inquiry, a planning method from management research (Richard Mason, 1969). The assistant lists what your plan needs to be true, most of it never said, and keeps the few the decision turns on: if the opposite were true, would a different course be right? It gives each of those a specific contrary that could well be true, and for each pair names the cheapest observation that would show which is true. Then it settles what your data and your answers settle, working the plan's own figures under the contrary, builds the course the remaining contraries call for at the plan's level of detail, and says which course it would take now and what would change its mind. The plan left standing is as good a result as the plan overturned. It says openly that it wrote both sides, so this is not an independent test of your plan.

**Use it when** you are about to commit to a plan: a price change, a move, a job offer, a big purchase, a team's next step. **Use a sibling instead** to be questioned about your idea one question at a time, or to have holes poked in it (`dia-quaestio`), to check whether a plan lives up to its own promises (`dia-negative`), or to test how well one argument's reasons hold (`dia-warrant`). For whether a single claim is true, just ask.

**Try:**

```
dia counterplan Since a cheap coffee chain opened by the station on 2 September, our weekday morning sales have dropped a lot. So from 1 December I'm going to take 1,500 won off every drink before 10 am on weekdays, and since customers hate it when you put prices back up soon after, I plan to keep it for at least 3 months. I have to order the banner and the menu boards by Friday (the 27th). Can you look at pos_summary_jul-oct_2026.csv and tell me whether this has any holes, or what I should do differently?
```

**What a session looks like** (real run in Korean, translated and shortened):

> **Assistant:** Examining your plan: **a 1,500-won discount on every drink before 10 am on weekdays from 1 December, for at least 3 months**, read as meant to win back the weekday morning sales lost since the cheap chain opened by the station.
> **Conclusion: I'd hold you back from ordering the banner for this plan now.** The data says the customers the discount aims at are not the ones who left. I compared average daily receipts on weekdays, 07:30–10:00, July–August against September–October (computed this time from the CSV in Python): bread + drink 48.3 → 27.3 (**−44%**); bread only 21.9 → 12.2 (**−44%**); drink only 39.7 → 34.1 (−14%). About 36 fewer morning receipts a day, and 85% (31) of them are **receipts with bread**. … After 10 am on weekdays and on Saturdays, every category fell only 1–4%. …
> **Four assumptions the plan leans on:** **① The customers who left are drink customers** (my reading). Contrary: the ones who left bought bread. Settled: on the data, **the contrary is true.** **② The cause is the chain's cheap coffee** (yours). Contrary: the chain also sells breakfast bread or sandwiches, or our own morning bread (time, kinds) changed in September. Still open. … ❓ Does the chain sell bread or sandwiches in the morning? Did anything change around September in when the morning bread first goes out, its kinds, amount or staff? If the chain sells bread, the answer is a **breakfast set**; if something changed on our side, **undoing it** comes before any discount. … **③ The profit won back exceeds the cost of the discount** (my reading). … 61 × 1,500 won ≈ 92,000 won a day … taking 3 months as about 60 weekdays (a number I chose), **about 5.5 million won** even if not one more customer comes. Open: the CSV has no prices or costs. ❓ What are the average price and cost of a morning drink …? **④ The 3 months must be fixed** (yours). … ❓ …
> **Note:** I built the opposing side myself too, so this is not an independent check of your original plan. …
>
> **You:** That chain is mostly coffee and doesn't sell bread, just cookies. And since late August my husband can't do the early-morning work because of his back, so since September the weekday morning bread, white loaves and salt bread, comes out around 10 (it used to be 7:30). So before 10 on weekdays there's only yesterday's leftover bread and baked sweets. On Saturdays my brother-in-law comes in early to help, so it comes out at 7:30 as before. A drink averages 4,800 won with about 1,100 won in ingredients, and bread comes to 4,200 won a receipt on average with about a 55% margin. I don't know how I'd word the banner.
>
> **Assistant:** **Don't order the drink-discount banner.** The cause is more likely the late morning bread than the coffee price. So the right direction is **bringing back the 7:30 bread on weekdays**, not a discount. What you told me nearly settles it: on Saturdays the bread came out at 7:30 as before, and Saturday mornings fell only 1–4%. Only on weekdays did the bread time change, and on weekday mornings only the receipts with bread fell 44%. The timing is the same too, September.
> **② The cause is the chain's coffee price → mostly not.** … What might be the chain's effect is the drop of 5.6 drink-only customers a day (−14%).
> **③ The discount pays → on your figures, it doesn't.** (computed in Python, assuming one drink per receipt) … To break even, new customers needed a day: 42 if drink-only, while the drop in drink-only was 5.6; 20 if bread + drink, but they stay away because there is no bread, so a coffee discount is unlikely to bring them back. *(lost profit about 170,000 won a day, 88% of it on receipts with bread)*
> **④ The 3 months fixed → no longer a question.** If the price doesn't change, there is no "putting it back up".
> **What I'd do instead (a plan I built):** 1. **Restore the 7:30 bread on weekdays.** How is for you to decide … A 3-hour early-morning part-timer is about 30,000 won a day. I took the 2026 minimum wage as 10,320 won, a figure from my memory that needs checking. … 2. You don't have to do everything at once: start with **one or two kinds, such as salt bread, at 7:30**. 3. **Put up a banner only once the bread restart date is fixed.** … 4. Check the effect on the POS: two weeks after the restart, compare weekday morning bread + drink and bread-only receipts with September–October (27 and 12). …
> **Still unknown:** **when you can find early-morning help on weekdays** is something only you know. If you can't make 1 December, the right thing is to order nothing on Friday. …
>
> **You:** Okay, so the bread was the problem. There's a student from the local baking school who can work weekdays from 5 to 8 am starting in December, at 13,000 won an hour. We're open about 21 weekdays a month, and a new banner and menu boards cost 280,000 won.
>
> **Assistant:** **On the numbers, an early-morning baker pays well. But put the banner up only after you've seen the bread actually come out at 7:30.** I looked at the changed plan the same way (figures computed in Python). Labour is 39,000 won a day (3 hours × 13,000 won), 819,000 won a month (21 days). … About **8 receipts a day** coming back breaks even, about a quarter of the 31 that left. … If half of the lost bread customers come back (an assumed figure), that's about +35,000 won a day, +740,000 won a month. …
> **Check before you order:** 1. **You probably don't need new menu boards**, since the prices stay the same … 2. **Weekly holiday pay may apply.** 3 hours a day × 5 days is 15 hours a week, so the part-timer is likely to qualify. This rests on my memory; check with the Ministry of Employment and Labor or a labour attorney. If it applies, the cost is about 47,000 won a day and break-even about 10 receipts a day. It still pays. 3. **Whether a 5–8 shift gets salt bread and white loaves out by 7:30** is your husband's call … 4. Check the student's skill with a one-day trial shift before 1 December.
> **Banner timing:** you don't have to order by Friday … Put the bread out first from 1 December, and once 7:30 has been kept every day for 1–2 weeks, put the banner up. … Check: if weekday morning bread + drink and bread-only receipts together beat September–October (39 a day) by **8–10 or more** in the second week of December, the labour is covered. …
>
> **You:** Yes, I won't order on Friday. I'll put the bread out from December, look at the POS in the second week, then put up the banner. Thanks, that's all.
> *(Recorded with the 5.0.0 text of the skill, Claude Opus 5.5 at effort medium; the user was simulated.)*

The sales file alone settled the first assumption before any question was asked: the discount aimed at the customers who had stayed. The user's facts settled the cause, and the assistant changed its judgment as far as they reached. The baker plan was a changed plan, so it was examined again, with the cost figures that rest on the assistant's memory marked for checking.

**Tips**

- Give it the data the plan rests on. It settles what the data can settle before it asks you anything, and it asks for everything only you know at once, each question with what its answer decides.
- "I don't know" is a fine answer; the assistant judges on what there is and says what would decide the rest.
- A fact or reason of yours settles a pair as far as it reaches, for either side. Rejecting a contrary counts only when you name a defect in it (it misstates a fact, or it can't hold with another contrary); rejection alone, repetition or someone's standing leaves the pair open, with what would settle it.
- If you change the plan, as with the early-morning baker above, it is a new plan and is examined again, with what the change gives up.
- Ask only "what does my plan rest on?" to get just the key assumptions, each with the question that would settle it.
- Hearing both sides is not evidence that the plan was tested; the reply says what was not examined, such as courses other than these two and whether the shared facts are accurate.

### dia-emend: one careful review of an answer or a draft

**In plain words.** A careful editor's single pass. The assistant lists what is wrong, checks each item, and fixes only the errors it could confirm. Errors it suspects but couldn't confirm are listed separately with the likely correction, so nothing changes silently.

**Use it when** you have a draft, or the assistant's last answer, and want factual errors, logic gaps and missing pieces fixed once. Start the message with `dia-emend` (or `dia emend`), then say what to focus on, if anything.

**Try:**

```
dia-emend check the facts: The Great Wall of China is the only man-made structure visible from the Moon with the naked eye, and it was built entirely during the Ming dynasty.
```

**What you get** (real run with web search, shortened):

> **Requirements, as read:** The thing reviewed is the sentence you gave. "Check the facts" is the criterion. You didn't say what the sentence is for, so I assumed it is meant to leave a reader with accurate facts about the Great Wall.
> **① Confirmed errors:** 1. "the only man-made structure visible from the Moon with the naked eye" is false (search). NASA calls this a myth … The Wall is only about 6 m wide, and the Moon is about 384,400 km away. … 2. "built entirely during the Ming dynasty" is false (search). Walls were built from about the 7th century BC onward. Around 220 BC, Qin Shi Huang joined the existing northern walls into one system. … The Ming rebuilt much of the Wall in brick and stone.
> **② Missing requirements:** none.
> **③ Correct content kept:** the Ming dynasty did build a large part of it, including most of what is standing today.
> **④ Remaining uncertainty:** sources give different lengths for the Han walls, so the revision gives no figure. I did not check whether any man-made structure at all can be seen from the Moon, so the revision makes no claim about that.
> **Revision:** The Great Wall of China is not visible from the Moon with the naked eye. NASA calls that idea a myth … It was also not built entirely during the Ming dynasty. … *(sources listed)*
> *(Recorded on 5.1.0, Claude Opus 5.5 at effort medium.)*

**Tips**

- Without a search tool, the assistant can still fix logic and arithmetic it re-derives, and puts unchecked facts under ④.
- `dia-emend do this task the dia-emend way: <task>` makes it write an answer, review it once and show only the final version.

### dia-ratchet: check and fix in rounds

**In plain words.** Like `dia-emend`, but in rounds, and every fix needs outside evidence: a search, a tool run or a source you supplied. Facts that pass a check are locked so later rounds can't undo them. The loop stops by itself when nothing is left to fix, when it can't verify anything more, or at the round limit.

**Use it when** accuracy matters more than speed, for example facts and dates you are about to publish. Start the message with `dia-ratchet` (or `dia ratchet`); `dia <request>` never picks it.

**Try:**

```
dia-ratchet --max 2 check the dates and facts in this paragraph: "The first iPhone went on sale in 2008, and the App Store opened the same day with 500 apps."
```

**What you get** (real run with web search, shortened):

> I checked the paragraph against Apple's own press releases and found three errors. I fixed all three.
> **Corrected paragraph:** "The first iPhone went on sale in 2007, and the App Store opened on July 10, 2008 with more than 500 apps."
> **Changes:** 1. "went on sale in 2008" → "2007" (June 29, 2007; Apple, June 28, 2007). 2. "opened the same day" → "opened on July 10, 2008" (Apple, July 10, 2008). 3. "with 500 apps" → "with more than 500 apps": Apple's release says "over 500 native applications."
> **Round summary:** round 1: 3 named, 3 confirmed, by web search and the fetched Apple press releases. Round 2: none. Locked: 3 items. Stopped because: zero defects in round 2, before the 2-round cap.
> **Unverified:** none.
> **One detail:** … July 10, 2008 is the date the store opened in iTunes 7.7. iPhones could reach it on July 11, when the iPhone 3G went on sale … *(sources listed)*
> *(Recorded on 5.1.0, Claude Opus 5.5 at effort medium.)*

**Tips**

- `--max N` sets the round limit (default 3).
- In a chat with no search or tools, it stops after round 1 and lists what it couldn't verify instead of guessing.

### dia-adjudicate: decide which review points hold

**In plain words.** A referee for reviews. You give it a text (a proposal, a document, a claim, a figure) and one or more reviews of it, written by people or by other assistants. Before it reads the reviews closely, it lists what the text itself claims that can be checked, so the reviews don't set the scope. Then it rules on each review point once, against the source: holds, holds in part, overstated, wrong, or cannot be verified. How many reviews say a thing, and who wrote them, count for nothing. Reviews that disagree may each be right by its own measure, and it says by which. It overturns a review only with the source's own words or a recomputation shown. Then it gives its judgment: what is left of the text's conclusion, which review was right on which point, what no review raised, and what the text has to satisfy once corrected. Where you need wording to act on, it writes it and says the wording is its own and has not been judged. It ends with where its own ruling is likeliest to be wrong.

**Use it when** several reviews of the same text disagree, or you want a confident review checked before you act on it. Start the message with `dia-adjudicate` (or `dia adjudicate`), then give the text and the reviews; `dia <request>` never picks it.

**Try:**

```
dia adjudicate Dohyun, our manager, put up proposal.md to switch couriers from Gaon to Nuri from January (he says it saves 14.4 million won a year), but Park the tax accountant's review-bookkeeper.md and Subin's review-packing.md say completely opposite things, and I can't tell which is right. Look at quote-nuri.md too, and tell me which of the two reviews is right and whether the saving is real. Nuri's quote is good until 30 November, so I have to tell Dohyun before then whether to sign.
```

**What a session looks like** (real run in Korean, translated and shortened):

> **Assistant:** **Conclusion first. The 14.4 million won a year saving won't happen.** Recomputed with the proposal's own figures, it comes to **about 9.53 million won a year**. And even that 9.53 million comes only **if you ship 2,000 boxes or more in every one of the twelve months of 2027**. That condition is the biggest risk, and neither review covers it.
> **On the saving, the tax accountant is right.** But the VAT worry is unneeded: the quote already says "VAT included".
> **Subin is right about the pickup time.** She put the Jeju surcharge at 6 times its real size.
> On the material so far, it's hard to recommend "sign as is before 11/30". The decision turns on the answer to question 1 below.
> **Questions for you (the decision changes with the answers):** 1. **What were your monthly shipments over the last 12 months, especially in off-season months such as January–February?** If even one month falls below 2,000 boxes, that month costs about 800,000 won more than Gaon. The data covers only August–September, so I can't judge now. 2. **How much does "same-day dispatch for orders by 3 pm" matter to sales?** … 3. **Can you check Gaon's invoices yourself?** The 3,100 won (the same up to 5 kg, VAT included) and the Jeju 2,500 won appear only in the proposal …
> **Rulings by review:** **Tax accountant:** *error of using the average weight* → **holds.** 432 boxes a month (18%) are over 2 kg; Nuri charges 3,400 won for them, 300 won more than Gaon. 1,968 × 500 − 432 × 300 = 854,400 won a month, 10,252,800 won a year … I recomputed it in Python. *VAT may be extra* → **does not apply.** Line 9 of the quote says "per box, VAT included". … *Leaving out Jeju is no big problem* → **holds in part.** … 120 boxes a month × 500 won = 60,000 won a month, 720,000 won a year. It should go in, not be left out. … **Subin:** *2 pm pickup* → **holds** (quote line 34). But line 35 says "pickup time can be negotiated" … *Jeju adds 360,000 won a month* → **overstated.** Gaon already charges 2,500 won; the real increase is 500 won a box, 60,000 won a month. … *Nuri damages a lot* → **cannot be verified.** The only basis is talk in a group chat. …
> **What both reviews missed (in the quote):** **The volume condition is per month, and all or nothing** (lines 21–22): in a month under 2,000 boxes, every box that month gets the base rate, 3,400 won up to 2 kg and 4,000 won over. … **Early termination penalty: remaining months × 300,000 won** (line 29) … **Automatic renewal** (line 30) … The proposal mentions neither.
> **What I checked, and where I may be wrong:** I read all 4 files to the end and ran the calculations in Python. I had a separate agent judge the same input a second time; the conclusion was the same on every item. … 1. **Gaon's figures** (3,100 won, Jeju 2,500 won, VAT included) rest on the proposal alone … 2. **Monthly volume in 2027** is unknown. It matters most to the conclusion. …
>
> **You:** Ordinary months ship about 1,600 boxes; August and September were far above normal because of Chuseok gift sets. In gift-set season it's about 2,400 boxes a month, and the season is the month before Seollal and the two months before Chuseok, so next year that's January, August and September. In ordinary months about 6 boxes in 100 are over 2 kg (the heavy ones are mostly gift sets). Jeju and remote islands are about 5 in 100 even in ordinary months. The product page says "same-day dispatch for orders by 3 pm", and many regulars order because of it. Gaon is 3,100 won a box now, but Gaon also texted that it's going up to 3,200 won a box from January. Did you include that? The Jeju surcharge stays at 2,500. We have no contract with Gaon; we use it month to month.
>
> **Assistant:** **On the quote as it stands, signing means a loss, not a saving: about 660,000 won more a year.** That includes Gaon's rise to 3,200 won. I hadn't included Gaon's rise last time; I calculated with the 3,100 won in the proposal. This time it's in, and the rise works in Nuri's favour. It still comes out as a loss. **What changed the result is the ordinary-month volume.** Nine months of the year ship 1,600 boxes, below Nuri's 2,000-box discount line. In those nine months every box gets the base rate (3,400 won up to 2 kg, 4,000 won over), more than Gaon's 3,200 won.
> **2027 (computed in Python):** gift-set season, 3 months (January, August, September; 2,400 boxes): Gaon 7.98 million won, Nuri 6.95 million; 1,034,000 won saved a month, **+3.1 million** for the three. Ordinary months, 9 (1,600 boxes, 6% over 2 kg, 5% Jeju): Gaon 5.32 million, Nuri 5.74 million; 418,000 won more a month, **−3.76 million** for the nine. **Year: −655,000 won (Nuri dearer).** If Gaon stayed at 3,100 won, −2.82 million. …
> **Rulings that changed:** **The tax accountant's "saves about 10 million a year" → wrong.** The method is right, but it took over the proposal's premise that August–September is the yearly average. **Subin's "no need to switch" → the conclusion holds.** On this data there is no money gain either. Jeju 360,000 won a month is still overstated … The pickup problem weighs more after what you said: with a 2 pm pickup, "same-day dispatch for orders by 3 pm" can't be kept. **The proposal's "2,400 boxes a month on average" and "volume condition met" → wrong.** … Nuri's quote also says its rates were set on these 2,400 boxes (line 24). …
> **What to tell Dohyun:** **On the quote as it stands, the right thing is not to sign.** Gaon is month to month without a contract, so staying ties you to nothing. Nuri ties you for 12 months, with a penalty of remaining months × 300,000 won and automatic renewal. **There is one case worth reopening with Nuri:** if before 11/30 you can get both of these. 1. **The discount rate at the 1,600-box level**, for example by lowering the line to 1,500 boxes; that turns into about 10.69 million won saved a year (computed). 2. **Pickup moved after the 3 pm order cut-off**; how late it has to be, given packing time, Subin will know. If either fails, or you get no answer in time, staying with Gaon is right. …
> **Not yet confirmed:** **1,600 boxes in ordinary months, 6% over 2 kg, 5% Jeju** are your estimates. An ordinary month loses about 410,000 won, so if these figures are a little off, the conclusion that it's a loss doesn't change. …
>
> **You:** Ah, so the ordinary-month volume makes it a loss... Got it. I'll tell Dohyun we won't sign on this quote, and to talk to Nuri about the volume line and the pickup time if he can. Thanks, that's all.
> *(Recorded with the 5.0.0 text of the skill, Claude Opus 5.5 at effort medium; the user was simulated.)*

The point that decided the matter was in the quote, and neither review raised it: the discount applies month by month, all or nothing. The user's ordinary-month volume turned "about 9.53 million saved, on a condition" into a loss, and the assistant made again the rulings that figure bore on, including the tax accountant's saving, which it had first found to hold in part.

**Tips**

- Give it the text, the reviews and the sources they point to (here the courier's quote). It reads them before it rules, and it checks the text's own claims as well, so it can find what no review raised.
- Two reviews saying the same thing are no more evidence than one, and a reviewer's standing counts for nothing; it rules on content.
- Answer what only you know; each question says what its answer decides. Material you add is marked as supplied by you, and the rulings it bears on are made again.
- A ruling you dispute is withdrawn only for a defect you can name (a source misread, a sum wrong, a condition missed, a fact it lacked). The reviewers' agreement, their standing and repetition move nothing.
- Where the assistant can start a separate agent and it overturns a review on its reading of a source, it has the same input judged a second time and compares the two; it says whether one run was made or two. Where it can't, you can run it again in a second chat and recheck only the rulings that differ.
- Without a search tool it still recomputes figures, but a point it cannot check stays "cannot be verified", never "wrong".

### dia-regula: write text a model will follow

**In plain words.** A style check for instructions you give an AI: a skill file, a prompt for an agent, a project's agent file, a rules file. It holds the text to four rules. Each paragraph says what result it wants, with its conditions and fallback in the same sentence, so no condition is stranded on a line of its own. A word that sets a limit ("touch", "change") is as narrow as you meant it. There are fewer instructions, and each has its reason. Each thing has one name. When you only ask for a review, it lists what breaks a rule, most serious first, and changes nothing until you pick.

**Use it when** you write or edit a skill, a prompt for an agent or sub-agent, an agent instructions file, or a rules file, or when an assistant keeps ignoring a condition you wrote. Start the message with `dia-regula` or `dia regula`, or let `dia <request>` pick it.

**Try:**

```
dia regula Review this instruction I wrote for a coding agent:
Update the docs for the new flag.
Only touch files the task needs.
- If the tests fail, stop.
```

**What you get** (real run, shortened):

> I found four problems, listed from most to least severe. You asked only for a review, so I haven't rewritten anything. Pick the findings you want fixed and I'll revise it.
> 1. **The edit limit depends on the agent's own judgment** (Rule 2). Line 2: `Only touch files the task needs.` The agent decides what the task "needs," so this sentence lets it widen its own permission. … Naming exact paths (for example `docs/cli.md`) leaves the agent nothing to stretch.
> 2. **The test condition is on its own bullet, separate from the action it controls** (Rule 1). Line 3: `- If the tests fail, stop.` When to run the tests, which tests, what "stop" means (stop before editing, leave the changes, or undo them), and what to do if the tests can't run at all are left open.
> 3. **No instruction gives a reason** (Rule 3). … Without reasons it can't apply them to cases the text doesn't name. For example, should it fix a test that was already failing?
> 4. **"The new flag" may be something the agent can't find.** If the agent can't tell which flag is new from the repo or a diff, it may guess or invent one. Give the flag's name and say where it's defined.
> There's no Rule 4 problem: each thing has only one name. **Advice (not a fault):** the text never says when the job is finished …
> *(Recorded on 5.1.0, Claude Opus 5.5 at effort medium.)*

**Tips**

- It treats the text you give it as material to check, not as instructions to follow, even when that text is itself a prompt.
- Ask "how strong is this rule?" to see what each rule rests on; that file is read only then.
- Where the assistant can start a separate agent, a change to text you will keep is reviewed by one that did not write it; otherwise, and for an edit that only adds a fact or command such as a test command, the assistant checks it itself and labels the check not independent.

### dia-techne: do a task the way the field's best would

**In plain words.** A request is often narrower than what it is for. `dia-techne` first says what it takes the request to be for, then treats the thing you asked for as one way of getting there: it sets it beside at least one other way, compares them by the result's own measure, and takes the one that comes out best, telling you what the comparison showed. It does the work as a top practitioner of the field would, makes now what can be made now instead of offering it, and has the result checked by something other than itself: it runs what it built, recomputes its figures and reads its sources. It never changes your data or a limit you set. It keeps a copy before it changes or deletes a file of yours, works inside the folder you gave it, installs nothing without your word, and stops before anything it could not take back, such as sending, publishing or spending.

**Use it when** a task matters enough to want the deeper version rather than the quick one: a claim you will make in public, a decision built on data, a fix you want checked by something other than the assistant. It takes longer. Start the message with `dia-techne`, or use `dia techne`; `dia <request>` never picks it. Add `--aim=request`, or say "as asked", when you want only the thing you named.

**Try:**

```
dia-techne Our mobile puzzle game's D30 retention is 12%. Can I tell investors next week that it's above the industry average?
```

**What you get** (real run with web search, shortened):

> **What I take the outcome to be:** investors leave convinced your retention is a real strength, and the claim still holds when they check it in diligence. Correct me if it's something else.
> **Recommendation:** If your 12% is classic D30, it is well above average, and "above average" is too weak a way to say it. … Two ways compared: "above industry average" (vague, breaks if your definition differs from the benchmark's) against a specific number with its definition and source (concrete, holds in diligence).
> **Suggested slide line (beyond what you asked):** "D30 retention: 12% (classic day-30, [iOS/Android], cohorts [month–month 2026], n = [installs]). That's about 2× the typical puzzle-game D30 (~5–7%) and well above the all-genre mobile median (<1%, GameAnalytics 2026)."
> **The comparison (each ratio recomputed):** all mobile genres, median 0.69–0.79%, so 12% is about 15–17×, "read in a secondary summary of the report"; puzzle genre about 5.35%, about 2.2×, "secondary, original source not found"; …
> **Check these before you say it:** the definition (classic or rolling: "Rolling retention can be several times higher. Benchmarks use classic."); the cohort mix; the sample size ("At 1,000 installs, 12% has a 95% range of about ±2 points"); consistency across cohorts; mature cohorts only.
> **Limits of this check:** "I couldn't open a primary GameAnalytics or genre-level report. The figures come from secondary summaries." **Left for you:** confirm the definition, n, cohorts and platform; decide whether to show the cohort table up front. *(sources listed)*
> *(Recorded on 4.0.0, Claude Opus 5.5.)*

**Tips**

- **Tell it what you are after** ("What I'm after is investors who still believe the number after diligence") and it works for that. Otherwise it reads a purpose in and says so first, so that you can correct it.
- What it makes beyond the thing you asked for is marked as such, and `--aim=request` keeps to the thing named.
- It leaves you only what you alone can do: a decision that is yours, a fact only you have, an act in the world. What it could not check, it tells you how to check; it does not check a tool against an outside library unless you allow the install.
- Name another executor ("a prompt for Codex, don't run it") and it writes the prompt instead of running. Without tools it cannot run or look anything up: it says what rests on recall and what you should check.

### dia-router: one short word for every skill

**In plain words.** Not a method of its own, just a quicker way in. Start your message with `dia`. On its own, `dia` lists the thirteen skills. Put a skill's name after it, then your request, to start that skill, or just write what you want and it picks the skill that fits, telling you which in one line first. If two skills fit your request about equally, it asks instead of guessing; if none fits, it answers without one.

**Use it when** you are typing on a phone, or you are not sure which skill you need. `dia-skopos`, `dia-ratchet`, `dia-adjudicate` and `dia-techne` start only by their name, never because `dia` picked them; for such a request `dia` replies with the form to send.

**Try:**

```
dia
dia reductio Assume every prime is odd and show where it breaks.
dia Our churn dropped after we added onboarding emails, so the emails reduced churn. How well do my reasons support that?
```

**What you get** (real runs on Claude Code, shortened):

> `dia` → the menu, a table of the thirteen skills from "dia-skopos | Before work: your request as read and the result it is for; you choose which to do" to "dia-techne | Deepen a one-off request as a field's top practitioners would, then run it", then "`dia <name> <request>` runs that skill, for example `dia reductio …`."
> `dia reductio …` → `dia-reductio` starts at once: "**Judgment:** "Every prime is odd" is false. Its own definitions refute it with the counterexample **2**. … 4. So 2 is odd. *(3, C1)* … 6. So 2 is not odd. *(5, C3)* 7. Steps 4 and 6 say "2 is odd" and "2 is not odd". That is a strict contradiction. … **I'd take A** [narrow the claim to every prime other than 2]. It is the smallest change, it is proved above …"
> `dia Our churn dropped …` → "→ dia-warrant: the request asks how well the reasons given support the conclusion." Then: "Your reasons show that churn fell after the emails launched. That makes the emails a plausible cause. They don't yet show the emails caused the drop. … The argument has only one step, and it's the weak kind: "it happened after, so it was caused by". … You probably have a built-in comparison: customers who signed up just before launch never got the emails. …"
> *(Recorded on 5.1.0, Claude Opus 5.5 at effort medium.)*

**Tips**

- A skill's full name picks it, with or without `dia-` (`dia reductio …`, `dia dia-reductio …`); a shortened name does not.
- Options pass through: `dia ratchet --max 2 <draft>` is the same as `dia-ratchet --max 2 <draft>`.
- `dia` must be the first word on its own. `dia-emend …` and the other full names go straight to their skill.
- A name that is plainly part of your sentence (`dia negative feedback on my draft?`) is not a pick; the whole text is read as a request.
- Where the assistant cannot open a second skill, `dia` still shows the menu and replies with the full form to send (such as `dia-reductio …`); this case has not been tested.

## Using several skills together

- **`dia-elenchus` and `dia-quaestio` in one request:** the definition dialogue comes first and the first message says so; brainstorming starts when you ask for options or the dialogue ends. The two are never interleaved.
- **`dia-emend` and `dia-ratchet` in one request:** they run as two separate passes with separate outputs. The emend pass's own re-derivation does not count as verification for a ratchet round.
- **`dia-reductio` and `dia-negative` in one request:** both run, which makes for long output. On a phone, ask for one at a time.
- **`dia-warrant`, `dia-conjecture` and `dia-counterplan` check what you gave them first.** If the request is another method's work, they say so in one line: `dia-warrant` for a strict contradiction or for counterexamples to a claim about every case, `dia-conjecture` for a rule put as "usually" or "most", `dia-counterplan` for a question whether one claim is true, with no course of action in it. The line need not name the skill to use; ask again, starting the message with the one that fits (see the table above).
- **After `dia-elenchus`:** if you then ask for advice, the assistant says the Socratic part is over and labels each suggestion as its own. For a full options-and-plan session, start a message with `dia-quaestio` and it takes the record from there.
- **Several skills as a review panel:** when an assistant that can start sub-agents runs several skills on one text, give each sub-agent one skill: `dia-counterplan` for a plan or recommendation, `dia-negative` for a text measured against the rules or standards it states, `dia-warrant` for an argument, `dia-reductio` for whether the text holds together. Each skill examines one central claim, so name the claim when it matters which. Start each message with the skill's name and the text and ask for the whole result in one response, with no questions (`dia-counterplan` then judges on what there is: each pair the material does not settle stays open with what would decide it, and the counterplan is given whole), and leave the output format to the skill where you can. When a workflow script or another agent fixes one, these four skills fit their result into it (from 2.11.0): findings go in its items with the proof in the evidence field, a last item labelled as the method's result holds what the format has no place for (for `dia-counterplan`, one item with its whole output, since its pairs are not defects), and where the format forces a value the method does not give (such as a severity), the item says so, so pass every item on, the last one included. In tests on Claude Code with a fixed findings format, the method's own result was still in the items passed on in 0 of 4 runs on 2.10.0 and 7 of 7 on 2.11.0 (spec D68). Give the reports to `dia-adjudicate` twice, each time in a separate agent told that it is one of two (so that it starts no second run of its own), and recheck the verdicts that differ; a counterplan's pairs are for whoever decides, not for the judge. In tests, `dia-adjudicate` ruled a claim in the reviewed text about another session's tool description from what it saw in its own session, so recheck verdicts on claims about another session, version or run mode (such as `claude -p`) yourself. A report written on another assistant (Codex, ChatGPT) can be pasted in the same way. On Claude Code, the companion plugin `dia-panel` from the same marketplace runs this panel as one workflow: install it with `claude plugin install dia-panel@dialectic-skills` and ask `Run /dia-panel:review-panel on <file>`; it gives each lens its own agent, runs `dia-adjudicate` twice with the reports in two orders, and lists the verdicts that differ for you to check. When the reports already exist, `Run /dia-panel:judge on <file> with the reports <files>` makes only the two `dia-adjudicate` runs and the list of verdicts that differ.
- **Asking an agent to use a dia skill:** name the skill in the prompt you give the sub-agent or reviewer and ask for one response, for example `Use the dia-negative skill (dia:dia-negative) on design.md and give the whole result in one response, with no questions.` A request such as "have independent reviewers check design.md with dia skills" also works, with or without `dia` in front: the assistant gives each reviewer one skill to start by name. An agent cannot reach the skills when its tool list leaves out the Skill tool (in Claude Code, add `Skill` to the agent's `tools`, or list the skills under `skills` to preload them), or when it runs where the plugin is not installed.

## Troubleshooting

- **`Repository not found` when adding the marketplace.** Check the spelling: `ajitta/dialectic-skills` (dialectic, not dialectric). The repository is public and needs no GitHub login.
- **No dia skills under `/` on Claude mobile.** Expected: the mobile menu does not list plugin skills. Start the message with `dia` or with the skill's full name, or type the full selection (such as `/dia-quaestio`).
- **A skill did not start.** Since 2.0.0 a request in plain words starts no dia skill. Start the message with `dia` (`dia <request>`, or `dia <name> <request>` such as `dia reductio …` for a chosen skill) or with the skill's full name (`dia-reductio …`). If the message did start with a skill's name and the skill still did not start, the assistant may have read the name as part of your sentence (this happens in Korean when the word for "folder" comes right after the name: the name is then read as that folder's name; other nouns after the name did not cause it); put a line break after the name or use the explicit selection.
- **dia works on one device but not on another.** Desktop installs stay on that computer; web installs are saved to your account and reach the mobile app. Install on the web for the web and mobile, and in each desktop app you use (see Install).
- **Every skill appears twice.** The plugin is installed through two routes (for example `dia@dialectic-skills` and `dia@ajitta`, or an upload and a marketplace). Remove one.
- **Skills section missing or greyed out on claude.ai.** Turn on Settings › Capabilities › Code execution and file creation.
- **`dia-ratchet`, `dia-adjudicate` or `dia-techne` does not start.** Each starts only when its name is the first word of the message or when it is selected explicitly (`/dia:dia-ratchet`, `$dia:dia-ratchet`, `@dia-ratchet`, `dia ratchet`; for `dia-adjudicate` and `dia-techne` the same forms and `dia adjudicate` or `dia techne`). `dia <request>` alone never picks them; it replies with the form to send.
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
docs/token-cost.md              measured token cost, always-on and per invocation (sections through plugin 2.3.0)
docs/skill-effect.md            each skill but dia-techne and dia-router against no skill, blind-judged (rounds through 2026-11-05)
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
