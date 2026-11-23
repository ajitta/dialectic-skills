# Dialectic Skills (`dia`)

Thirteen reasoning-and-review skills for Claude, Codex and ChatGPT. Each skill is a set of written instructions that the assistant follows when your message starts with the skill's name or with `dia`.

- `dia-skopos`: before work starts, shows what you asked for as it reads it and the result it takes the work to be for, lists what only you can decide, and asks whether to make the thing you asked for or to work for the result; then waits for your word.
- `dia-elenchus`: Plato's elenchus. Asks what you mean by a key idea, one question at a time, and shows where your own premises contradict each other. Gives no advice.
- `dia-quaestio`: Socratic questions one at a time, then options, a comparison by your criteria, a verdict and a brief.
- `dia-reductio`: holds a position against its own commitments. Lists what it relies on, including what nobody said, derives any strict contradiction line by line, tests each way out and says which it would take.
- `dia-negative`: internal critique. Holds a claim to its own standard and shows where it falls short, with cases.
- `dia-warrant`: finds the unstated rule that carries an argument from its reasons to its conclusion (Toulmin), tests it with critical questions and the exceptions nobody looked at, and says how far the conclusion can be relied on for what it has to carry.
- `dia-conjecture`: tests a claim of the form "all X are Y" against cases, finds the condition it needs and does not state, and says whether the claim and the decision built on it stand (Lakatos).
- `dia-counterplan`: builds the opposing plan from your plan's key assumptions, says which of the two the evidence favours now and what observation would decide.
- `dia-emend`: one review pass over an answer or draft. Fixes only defects with a confirmed basis.
- `dia-ratchet`: repeated review rounds with a round cap; only external checks count as evidence, and what passed is locked.
- `dia-adjudicate`: rules on reports others wrote about a text (critiques, reviews), checking each point against sources; says what no report raised, what the rulings leave of the conclusion, and where its own ruling may be wrong.
- `dia-regula`: checks or writes text a model will follow (a skill file, a prompt, an agent file) against four rules, so conditions stay with what they gate and each instruction carries its reason.
- `dia-techne`: takes a request to the result it is for, the way a field's top practitioners would: compares the thing you asked for with other ways of getting there, makes what the result needs, and has it checked by something other than the assistant, stopping before any step it could not take back. Starts only by name.

Start a message with `dia` to reach them quickly (`dia-router`): `dia` alone lists them, `dia reductio …` starts one by name, and `dia` followed by your request picks the skill that fits and names it. A request that does not start with `dia` or a skill name starts no skill.

## What the plugin does and does not do

The plugin contains only Markdown, YAML and JSON files. It has no scripts, hooks, MCP servers or binaries, and it does not run, send or fetch anything by itself. It does not read or store personal data. Some skills tell the assistant to use a search or code tool if one is already available in your session, to check a fact or a calculation; without such a tool, the skills work from the conversation alone and mark what they could not verify. `dia-techne` carries out the request you give it with the tools your session already has, and stops before any step a backup cannot undo, such as sending, publishing or pushing.

## More

Installation for every surface, examples for each skill and troubleshooting: https://github.com/ajitta/dialectic-skills

License: MIT
