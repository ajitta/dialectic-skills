# Product

<!-- impeccable:product-schema 1 -->

> Written by `impeccable init` without an interview: nobody was available to answer questions in this
> run. Facts below come from `README.md`, `packaging/openai/interface.json`, `plugin-manifest.json` and
> `docs/spec.md`. Anything marked **(inferred)** is a reading of those files, not an owner answer;
> confirm or correct it before relying on it.

## Platform

web

## Users

- People who use an AI assistant (Claude, Codex, ChatGPT) and want it to question, test or review
  something before they act on it. The README addresses them directly and says no background in
  philosophy is needed, so the primary reader is not assumed to be a developer. **(inferred from README
  "Skill guide with examples")**
- Claude Code and Codex CLI users who install from the command line. **(inferred from the Quick start
  order in README)**
- The job on the project page: understand what the skills do, pick one, install `dia` on the
  surface they use, and know how to start a skill there. **(inferred)**

## Product Purpose

`dia` (Dialectic Skills) is one plugin of reasoning-and-review skills: `dia-skopos`,
`dia-elenchus`, `dia-quaestio`, `dia-reductio`, `dia-negative`, `dia-warrant`, `dia-conjecture`,
`dia-counterplan`, `dia-emend`, `dia-ratchet`, `dia-adjudicate`, `dia-regula`, `dia-techne`, and `dia`,
the one skill that calls them. Each of the thirteen
turns an old way of thinking (Socratic questioning, proof by contradiction, internal critique,
Toulmin's argument layout, Lakatos's proofs and refutations, Mason's dialectical inquiry, an editor's
review pass) into a routine the assistant follows step by step. Success for the page is an
install on the visitor's surface and a first skill started. **(success definition inferred)**

## Positioning

- Instructions only: Markdown, YAML and JSON, no scripts, hooks or servers. The plugin installs on
  Claude (web, desktop, mobile, Claude Code), Codex and ChatGPT.
- Each skill is a function: one purpose, worked from what it is handed, one thing returned.
- Each skill leaves the decision with the user ("The decision is yours"); `dia-elenchus` gives no
  advice and often ends in aporia, which the README treats as a result, not a failure.

## Operating Context

- Install routes (README, Install): Claude Code (`/plugin marketplace add ajitta/dialectic-skills`,
  `/plugin install dia@dialectic-skills`); Codex CLI (`codex plugin marketplace add
  ajitta/dialectic-skills`, `codex plugin add dia@dialectic-skills`); claude.ai and Claude desktop
  (Customize › Plugins); Claude mobile (no install step, reaches the app from a web install); ChatGPT
  (zip upload on the web, marketplace in the desktop app).
- Where you install decides where dia shows up: web installs follow the account to mobile; desktop
  installs stay on that computer.
- A skill starts on its full name as the first word of a message, or by explicit selection
  (`/dia:dia-<x>`, `/dia-<x>` on Claude mobile, `$dia:dia-<x>` on Codex, `@dia-<x>` on ChatGPT). `dia` alone
  loads what each skill needs and returns; `dia` with a target has it criticised by three independent
  agents and judged by a fourth. A request in plain words starts no skill.

## Capabilities and Constraints

- Plugin version 6.0.0 (`plugin-manifest.json`). License MIT. The page is published only from `main`.
- The project page lives at `https://ajitta.github.io/dialectic-skills/` and is plain static
  HTML/CSS/JS in `site/`; all asset URLs must be relative. **(stack observed in the repository)**
- Undecided: whether the page should ever carry translated versions (the README has a Korean
  translation; the page is English only and links to it). **(open)**

## Brand Commitments

- Name: Dialectic Skills, plugin name `dia`. Developer name: ajitta.
- Mark: two overlapping circles with a lens where they meet (`packaging/openai/assets/logo.svg`,
  `icon.svg`); amber lens `#F59E0B`. The page draws the mark in its own palette.
- Voice: plain, exact and modest, as in the README; claims are stated with their limits ("in the
  owner's tests", "real run, shortened", "the wording you get will differ"). **(inferred from README)**

## Evidence on Hand

- No session recorded on the current skill texts is on the page: the sessions recorded on earlier
  texts were taken out with 6.0.0.
- Public-domain pictures and footage with credits in `site/assets/img/credits.json`.
- Absent, and not to be fabricated: users, testimonials, quotes, ratings, star or download counts,
  customer logos, statistics.

## Product Principles

1. The user decides; the page shows what each skill does and leaves the choice to the reader.
   **(inferred)**
2. Show real output, not adjectives: a shortened real session beats a description of one.
   **(inferred)**
3. Exactness over reach: commands, names and surfaces must match the README word for word.
4. Works anywhere, needs nothing: no setup beyond the install route for the surface in use.

## Accessibility & Inclusion

No product-specific requirement was recorded. Treat WCAG 2.2 AA as the floor for the page.
**(inferred default)**
