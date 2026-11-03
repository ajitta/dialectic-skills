# Router-only invocation and five renames (design record, plugin 2.0.0)

Status: owner rulings taken 2026-11-03 (all as recommended); implementation on branch `router`.
Base: plugin 1.13.0 (`main` at `2172469`). Decision row: spec D56 (draft in §7 below).

## 1. Goal

Separate who chooses a skill from who runs it.

- A message that does not start with `dia` (or a full skill name, or an explicit platform
  invocation) starts no dia skill. Natural-language routing to the nine routed skills ends.
- `dia <request>` hands the choice to the router; `dia <selector> <request>` and
  `dia-<name> <request>` name the skill.
- Each skill's description keeps a short label of what it does plus one gate sentence. The
  borders between siblings live in the router body only.
- Each skill's method, checks, stops and output rules are unchanged.

Not in scope: any change to a skill's reasoning procedure, checks or output form.

## 2. Names

| Old | New | Why |
|---|---|---|
| `dia-intent` | `dia-skopos` | "intent" is a word of ordinary AI requests; Greek *skopos* (aim, target) names the object of the review |
| `dia-brainstorm` | `dia-quaestio` | sets it apart from a plain request for ideas; Latin *quaestio* (inquiry by questions) names the method |
| `dia-refine` | `dia-emend` | "refine" is an everyday edit command; *emend* keeps the sense of correcting errors |
| `dia-instruct` | `dia-regula` | "instruct" is an everyday command; Latin *regula* (rule) names what the skill writes and checks |
| `dia-menu` | `dia-router` | the skill shows a menu, resolves selectors, chooses and hands off |

The other nine names stay. The criterion is not one etymology for all names but replacing the
names that collide with ordinary work requests. `dia` stays the shortest entry word; the
router is not one of the thirteen numbered methods.

## 3. Invocation

Order in which the first command of a message is read:

1. an explicit platform invocation (`/dia:dia-x`, `$dia:dia-x`, `@dia-x`);
2. a first word that is a full skill name (`dia-emend …`);
3. a first word `dia` on its own, in any letter case (the router);
4. anything else: no dia skill.

| Input | Result |
|---|---|
| `review this claim` | no dia skill |
| `dia`, `dia help`, `dia menu`, `dia ?` | menu |
| `dia <request>` | router chooses among the routed skills |
| `dia 5 <request>`, `dia neg <request>`, `dia negative <request>`, `dia dia-negative <request>` | that skill |
| `dia-emend <request>` | dia-emend directly |
| `dia <request that needs a gated skill>` | the form to send, no run |
| `dia rat <request>` | dia-ratchet (the selector is an explicit choice) |

Direct follow-ups of a task started this way need no new `dia`; a skill's state ends at its own
end condition, on the user's request, when another skill is invoked, or when an unrelated task
starts (each skill's existing rules already say this where they hold state).

### Selectors (owner ruling 2: fixed table)

Accepted: the fixed number 1–13, the full name with or without `dia-`, and one fixed
three-letter code per skill. Arbitrary prefixes are no longer read, because with the new names
ordinary words would become picks (`tech` → dia-techne, an explicit-only skill that acts;
`counter`, `count` → dia-counterplan).

| # | Skill | Code |
|---|---|---|
| 1 | dia-skopos | sko |
| 2 | dia-quaestio | qua |
| 3 | dia-elenchus | ele |
| 4 | dia-reductio | red |
| 5 | dia-negative | neg |
| 6 | dia-warrant | war |
| 7 | dia-conjecture | con |
| 8 | dia-counterplan | cou |
| 9 | dia-emend | eme |
| 10 | dia-ratchet | rat |
| 11 | dia-adjudicate | adj |
| 12 | dia-regula | reg |
| 13 | dia-techne | tec |

Codes and full names that are English words (`red`, `war`, `con`, `rat`, `neg`, `adj`,
`negative`, `warrant`, `ratchet`, `conjecture`) keep the existing rule: a word that reads as part
of the request's sentence (`red flags …`) is not a selector, and when unsure the router asks in
one line. A counting number (`dia 3 reasons …`) is not a selector either.

No `--` separator (ruling 3): iOS Smart Punctuation, on by default, turns `--` into an em dash
(Apple Support, "Format dashes and quotation marks"), and the sentence rule already handles the
known collisions (probes Part Q, `s-redflags`).

### Former names (ruling 1: kept until the next minor release)

- The router's description names the five former names, so a first word `dia-refine …` reaches
  the router, which reads it as `dia refine …`.
- The router body maps `intent`/`int` → dia-skopos, `brainstorm`/`bra` → dia-quaestio,
  `refine`/`ref` → dia-emend, `instruct`/`ins` → dia-regula, `menu` → the menu, and names the new
  skill in its one-line choice.
- The package check allows the former names only on the router's alias lines and in
  `metadata.lineage`; a test fails once the plugin version passes 2.0.x, so the aliases are
  removed in 2.1.0.

### Choosing for a request (ruling 8)

The router's current "Choosing for a request" bullets stay, renamed, as the only border text;
they are not replaced by a one-row-per-skill table. Routed skills: 2–9 and 12. Gated (never chosen
from a plain request; the router replies with the form to send): 1, 10, 11, 13. One wording
change: the bullets no longer point at "each skill's own description", which no longer carries
borders.

## 4. Descriptions

Each of the thirteen descriptions is one plain YAML line: the label, then the gate sentence that
was measured (ruling 4):

> `<label>.` Use only when the message starts with `dia-<x>`, when the skill is invoked by name,
> or when dia-router selects it; a request that only sounds like this is not an invocation.

Labels:

| Skill | Label |
|---|---|
| dia-skopos | Confirm the user's goal, assumptions and open decisions before work. |
| dia-quaestio | Use modern Socratic questions to develop an idea into options and a plan. |
| dia-elenchus | Examine a definition through classical Socratic dialogue and agreed premises. |
| dia-reductio | Test a thesis by deriving a strict contradiction from stated premises. |
| dia-negative | Critique a claim or practice against its own stated standard. |
| dia-warrant | Examine how well reasons support a defeasible conclusion. |
| dia-conjecture | Test a universal claim using counterexamples and user-directed repairs. |
| dia-counterplan | Construct a counterplan from contrary assumptions using the same evidence. |
| dia-emend | Review a draft once and correct confirmed defects while marking uncertainty. |
| dia-ratchet | Revise through repeated rounds using external checks and locked results. |
| dia-adjudicate | Rule on reports about a target using evidence, without rewriting the target. |
| dia-regula | Write or review instructions for models against four structural rules. |
| dia-techne | Deepen and execute a task using expert methods and outside checks. |

The router keeps its 1.13.0 description, renamed, plus the former-names sentence.

`allow_implicit_invocation` stays `true` for every skill (D33): `false` removes a skill from the
model-visible list on Codex and ChatGPT, so a message starting with its name could not reach it.
`disable-model-invocation` stays unused on Claude for the same reason and because the router
loads the chosen skill through the Skill tool.

## 5. Bodies (ruling 8)

Bodies change only where they name a renamed skill or the router's selectors. Invocation
sentences stay: they exist in five bodies, about 4,600 of about 190,000 body characters, are
paid only on invocation, and hold rules that were added after real misses (the counting-number
exception in dia-ratchet, dia-adjudicate and dia-intent after Codex started the confirm-first
skill from `dia 1 thing …`, probes Part Q round 3; the run-without-marker fallback in dia-intent,
D33). The bodies of the nine routed skills have no invocation sentences to remove.

## 6. Evidence before the build (2026-11-03)

Claude Code 2.1.314, sonnet, `--tools Skill`, a fresh configuration per run, connectors off,
neutral directory, n=3 per cell; 159 runs. Smoke counts, not a measurement. Arms built from
`2172469` with bodies renamed only: A = the first draft's descriptions ("Use only on direct
invocation or selection by dia-router."), B = labels plus the measured gate sentence, B2 = B plus
the former-names route.

| Cells | 1.13.0 | A | B | B2 |
|---|---|---|---|---|
| six natural requests without `dia` (dia skill loaded) | 18/18 | 2/18 (dia-conjecture 2/3 on a counterexample request) | 0/18 | refine cell 0/3 |
| Korean request starting with the full name (emend, quaestio, regula, skopos; old names on 1.13.0) | 12/12 | 12/12 | 12/12 | emend 3/3 |
| `dia qua …`, `dia <review this draft once>` | right skill 6/6 | 6/6 | 6/6 | |
| `dia devil's advocate: is coffee healthy?`, `dia <counterexamples to a rule>` (none fits) | 6/6 | 6/6 | 6/6 | |
| `dia <verify in rounds until no defects>` (form handed back, no ratchet) | 3/3 | 3/3 | 3/3 | |
| `dia-refine <draft>` (old first word) | | 0/3 loaded, reviewed by hand | 0/3, same | 3/3 via router to dia-emend |
| `dia-brainstorm <idea>` | | | | 3/3 to dia-quaestio |
| `dia refine <draft>` | | | 3/3 to dia-emend (by meaning) | 3/3 |

Always-on listing (`claude plugin details`): 1.13.0 3,023 tokens; A 709; B 1,278; B2 1,328.
Not covered: Codex and ChatGPT, mobile apps, Claude Code with all tools (the Part Y name effect
was seen there), borders not in these cells, n of 12 or more.

## 7. Draft of spec D56

> D56 | Plugin 2.0.0 makes every dia skill router-only and renames five skills (owner,
> 2026-11-03; branch `router`; record `docs/research/router-redesign.md`). Names: dia-intent →
> dia-skopos, dia-brainstorm → dia-quaestio, dia-refine → dia-emend, dia-instruct → dia-regula,
> dia-menu → dia-router. Invocation: a skill runs only on a message starting with its name, an
> explicit invocation by name, or a choice by dia-router; natural-language routing of the nine
> routed skills ends (this reverses the routing half of D33's reason and the "natural language is
> the safe default on mobile" line of §4; the `allow_implicit_invocation: true` setting of D33
> stays). Descriptions: a label plus the measured gate sentence; the router body's border bullets
> are the only border text. Router selectors: the fixed number, the full name with or without
> `dia-`, a fixed three-letter code; no prefix matching; no `--` separator. Former names route
> through dia-router until 2.1.0. Major version because the way every skill is reached changes.
> Acceptance probes P2, P6 and P7 are redefined (§12.2).

Redefined probes:

- **P2** (Claude mobile): `dia` shows the menu; one `dia <number or code> <request>` per skill
  and one `dia <request>` load the right skill; the reply is in the prompt's language.
- **P6** (first word): `dia-emend — check numbers` runs one pass; `dia-ratchet` runs the loop;
  "please refine this paragraph" and "review this draft" start neither; a mid-sentence mention
  starts nothing.
- **P7** (routing): (a) natural requests without `dia` load no dia skill, with the 1.13.0 routing
  prompts as cells; (b) `dia <request>` cells and the router's border cells from probes Part Q
  keep their 1.13.0 results.

## 8. Release

Branch `router`; plugin 2.0.0 and every skill's `metadata.version` to its next major (the gate
of each changed); the release notes (the tag message) open with a "Breaking" section listing the
old and new names and the end of natural-language routing; catalog `ajitta/claude-plugins`
entry and the repository description synced after the release; the owner re-uploads the OpenAI
zip and checks P2 on the phone.
