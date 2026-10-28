# Dialectic Skills (`dia`)

Eleven reasoning-and-review skills for Claude, Codex and ChatGPT. Each skill is a set of written instructions that the assistant follows when you ask for it by name or describe the task.

- `dia-confirm`: before work starts, restates the goal, discloses assumptions, lists the decisions you must make, and waits for your approval.
- `dia-elenchus`: Plato's elenchus. Asks what you mean by a key idea, one question at a time, and shows where your own premises contradict each other. Gives no advice.
- `dia-brainstorm`: Socratic questions one at a time, then options, a comparison by your criteria, a verdict and a brief.
- `dia-reductio`: strict reductio ad absurdum. Lists every premise with its source and derives a contradiction line by line.
- `dia-negative`: internal critique. Holds a claim to its own standard and shows where it falls short, with cases.
- `dia-warrant`: lays out an argument's claim, data and warrant (Toulmin) and tests the warrant with critical questions. Says which link is weakest, not whether the claim is true.
- `dia-conjecture`: tests a claim of the form "all X are Y" by counterexamples, one at a time; you rule on each and repair the claim (Lakatos).
- `dia-counterplan`: builds the opposing plan from your plan's key assumptions and asks which assumptions you now hold. Gives no verdict.
- `dia-refine`: one review pass over an answer or draft. Fixes only defects with a confirmed basis.
- `dia-ratchet`: repeated review rounds with a round cap; only external checks count as evidence, and what passed is locked.
- `dia-adjudicate`: rules on reports others wrote about a text (critiques, reviews), checking each point against sources, and lists the verdicts a person should recheck.

Start a message with `dia` to reach them quickly (`dia-menu`): `dia` alone lists them with numbers, `dia 4 …` or `dia red …` starts one by number or first letters, and `dia` followed by your request picks the skill that fits and names it.

## What the plugin does and does not do

The plugin contains only Markdown, YAML and JSON files. It has no scripts, hooks, MCP servers or binaries, and it does not run, send or fetch anything by itself. It does not read or store personal data. Some skills tell the assistant to use a search or code tool if one is already available in your session, to check a fact or a calculation; without such a tool, the skills work from the conversation alone and mark what they could not verify.

## More

Installation for every surface, examples for each skill and troubleshooting: https://github.com/ajitta/dialectic-skills

License: MIT
