# Dialectic Skills (`dia`)

Thirteen reasoning-and-review skills, and `dia`, the one skill that calls them. Each skill is a set of written instructions the assistant follows when your message starts with the skill's name. Each is a function: it has one purpose, works from what it is handed and returns one thing, and it does not know the other skills.

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

## Starting a skill

Start a message with a skill's name: `dia-negative our company is flat, so anyone can speak up freely`. A request that only sounds like a skill starts none.

`dia` is the skill that calls the others. Alone, it loads the table above and the rules for handing work to an agent: the agent gets the sources themselves and your own words, never a summary, and its report comes back whole. With a skill's name, or a request for work that one row describes, it runs that skill and says which. With a target and no skill asked for (`dia docs/plan.md`, or `dia` and a pasted claim), it has the target criticised by three independent agents, each looking for a different kind of fault, and has `dia-adjudicate` rule on their reports in a fourth; you may name the critics.

## What the plugin does and does not do

The plugin contains only Markdown, YAML and JSON files. It has no scripts, hooks, MCP servers or binaries, and it does not run, send or fetch anything by itself. It does not read or store personal data. The skills tell the assistant to use the tools your session already has (a search, a shell, the files you point to) to check a fact, a figure or a result; what could not be checked is said to be unchecked. `dia-techne` carries out the request you give it with those tools.

## Install

On Claude Code:

```
/plugin install dia --marketplace ajitta/dialectic-skills
```

Installation on the other surfaces and troubleshooting: https://github.com/ajitta/dialectic-skills

License: MIT
