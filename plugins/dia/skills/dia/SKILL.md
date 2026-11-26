---
name: dia
description: Call the dia skills. Alone, it loads what each skill needs and returns and the rules for handing work to an agent; with a target, it has the target criticised by three independent agents and judged by a fourth. Use only when the first word of the message is dia on its own, or when this skill is invoked by name; a first word that is a full skill name (dia-emend) goes to that skill, and a request that only sounds like this is not an invocation.
license: MIT
metadata:
  version: "1.0.0"
---

The thirteen dia skills are functions: each has one purpose, works from what it is handed and returns one thing. None of them knows the others. This skill is the one that calls them: it holds what each needs and returns, the rules for handing work to an agent, and one procedure that has a target criticised and judged.

## Called alone

With nothing after `dia`, answer with the thirteen in a line each and how to call this skill with a target. From then on in this conversation the table and the rules below are what you work by whenever a dia skill is run or work goes to an agent.

With a skill named after `dia`, or a request for work that one row describes, run that skill, saying in a line which and why, and hand it what its row names.

## Handing work to an agent

An agent sees nothing of this conversation. What it is not handed it fills with a guess, and the guess comes back looking like a finding.

- Hand it the sources themselves: the target as a path or as its whole text, and the files and sources the target rests on, by path. Never a summary of them.
- What only this conversation holds goes in word for word and marked as whose it is: what the user said the target is for, a fact they stated, a limit they set, an earlier answer that is itself the target. Put nothing in the user's name that they did not say.
- Give it none of your own view: not what you think of the target, not what you expect it to find.
- To have it run a dia skill, begin its brief with the skill's name, alone on the first line, and ask for that skill's reply entire as its last message. Do not list in the brief what to return: the skill says that itself, and your list would take its place. An agent made for the occasion is told what you need back.
- Tell an agent that nobody will answer its questions, so that what it would have asked comes back listed as open. A skill that needs someone to answer is the exception: give it the answers one at a time, by continuing its agent or by starting it again with the exchange so far and the new answer, and let them be the respondent's own, the user's, or yours where it is your thinking that is examined.
- Whatever you pass on, to the user or to an agent that works from it, goes whole. A reading of your own goes after the report and is marked as yours.

## A target criticised and judged

With a target after `dia` (a document, a plan, a claim, an answer) and no one skill named or asked for:

1. Gather what the agents will work from: the target, the sources it points to, and everything the user has said about it. What no file holds goes to every critic and to the judge in the user's words.
2. Where the user names the critics, those are the critics. Otherwise choose three by the kinds of fault this target could have, each looking for a different kind. A critic is a dia skill where one fits (dia-negative, dia-reductio, dia-warrant, dia-conjecture, dia-counterplan), or an agent briefed for the occasion with the kind of fault it looks for and what it must return. Such an agent has no tested method behind it, so its report is only as good as its brief. dia-regula is not chosen as a critic: holding text a model follows against rules is a different job.
3. Start the three as independent agents, together where that is possible, each under the rules above. No critic is shown another's report.
4. When all three reports are in, start one agent with dia-adjudicate and give it the target, the sources, the user's words and the three reports whole, each under its critic's name.
5. Give the user the judge's reply as the judge gave it, and say which critics ran and what kind of fault each looked for. The critics' reports follow whole when the user asks for them.

Where agents cannot be started, say so; criticisms made inside one conversation are not independent of each other or of you, and are not given as if they were.

## The thirteen

| Skill | What it is for | Hand it | It returns | Someone to answer |
|---|---|---|---|---|
| dia-skopos | Before any work, show what is being asked for and the result it is for, and let the user choose which of the two is the request | The request in the user's words; the project or material it points to | A review: what would be made, the result it is for, what was found and what is assumed, what only the user can decide, and the choice. It does none of the work | Yes: it stops for the user's word |
| dia-techne | Do a task for the outcome it serves, as the field's best practitioners would, checked outside the model | The request; the user's words on what it is for, their facts and limits; the files and data. `--aim=request` keeps to the thing asked for | The finished work, with the outcome worked to, the ways compared, what was made or changed, the methods that ran and what the check showed | No |
| dia-emend | Review a draft once and return one revision that fixes what is confirmed and marks what is only suspected | The draft itself (text or file), the criteria, what the draft is for, any reference to check it against | The defects found and the one revision; a file is edited in place | No |
| dia-ratchet | Revise in rounds that move only on evidence from outside the model, so that the user knows which claims were checked | The target (text or file), the criteria, what it is for, the user's own sources. `--max N` caps the rounds | The changes, what each round locked, why it stopped and what stays unverified. No verdict on the target | No |
| dia-regula | Write or review text a model follows (a prompt, instructions, a skill) against four rules | The text itself, and the old text where it was edited; the user's words on what it has to make a model do | A report of each breach, quoted, with the rule it breaks; or the written or revised text with any change of meaning reported | No |
| dia-negative | Hold a claim, plan or text against the standard it states for itself | The target in its own words, the text itself and not an account of it; the purpose it or the user states for it | The judgment first (open, or holding against the cases tested), the findings firm and conditional, what the claim does against what it says it is for, options and one recommendation | No |
| dia-reductio | Hold a position against its own commitments: what it has to rely on, and whether all of it can be true together | The position in its own words; what its holder said or promised earlier on the matter; the files it points to; what it is for | The judgment first, the contradiction with the premises it needs, what came to the surface, and what each way out costs | No: it lists what it would have asked |
| dia-warrant | Hold a conclusion against the step that carries it: the rule each step runs on, and whether it holds in this case | The argument in its own words (a conclusion with its reasons), the material it points to, what the conclusion has to carry | The judgment first (how far the conclusion can be relied on), the step it turns on, the evidence, and what was at hand and not used | No: it lists what it would have asked |
| dia-conjecture | Hold a claim about every case against the cases that press it hardest, and repair the claim where one counts | The claim in its source's words, the records or code it covers, what rests on it | The judgment first (whether "every" stands), the deciding cases, and the repaired claim with what it no longer covers | No: it lists what it would have asked |
| dia-counterplan | Hold a plan against the plan its opposite assumptions give, on the same facts | The plan's text, its figures and files, what the plan is for, what the user has said that settles an assumption | The judgment first (which course to take and what would change it), each assumption with its contrary, and the counterplan | No: it lists what it would have asked |
| dia-adjudicate | Rule on reports about a target by the evidence, check the target's own claims, and judge what is left of its conclusion | The target, the reports whole, the sources both point to, the user's words on what the ruling is for | The judgment first, a ruling on each point with its basis, what no report raised, and what has to change in the target | No: it lists what it would have asked |
| dia-elenchus | Examine the concept an idea stands on, through a definition, agreed premises, a contradiction and a revision, to bring out a fork in the respondent's own thinking | The idea in the respondent's words. To continue a dialogue: the exchange or the record so far, and the new answer | One question a message; at the end a record of the definitions, the agreed premises, the ideas born and what is still not known | Yes, a person or an agent. With none, it gives its first question only |
| dia-quaestio | Question an idea until its owner sees it clearly, then help them grow options and choose | The idea in its owner's words and what it is for. `stress` tests it harder; `quick` and `deep` set the length | One question a message; at the end a verdict and a brief with the options and one next step | Yes |
