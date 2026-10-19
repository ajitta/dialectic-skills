# Dialectic Skills (`dia`)

Seven reasoning-and-review skills in one plugin, written to run unchanged on any assistant that loads Agent Skills: Claude (web, desktop, mobile, Claude Code), Codex and ChatGPT. The package is instructions only (Markdown, YAML, JSON), so every skill also works in a chat with no tools. Skill files are in English; each skill replies in the user's language.

| Skill | What it does | Invocation policy |
|---|---|---|
| `dia-intent` | Before work starts: restate the goal, disclose material assumptions, list only the decisions the user must make, then wait for approval. | explicit only |
| `dia-elenchus` | Plato's elenchus: "what is X?", premises agreed one question at a time, contradictions shown, each revision is the user's new idea. Usually ends in aporia; gives no advice. | explicit only |
| `dia-brainstorm` | Modern Socratic questioning one question at a time, then the user's options plus up to three labeled ones, convergence by criteria, a verdict and a brief. Never implements. | explicit only |
| `dia-reductio` | Strict reductio ad absurdum in one pass: labeled premises, a Q and not-Q derivation with a rule per line, graded strength, options and a record. `--target=user\|claude\|text\|all`. | implicit allowed |
| `dia-negative` | Immanent critique after Adorno in one pass: the target's own standard, strict gaps with cases and "what escapes", the operative purpose with a falsifier, options without forced synthesis. `--target=user\|claude\|text\|all`. | implicit allowed |
| `dia-refine` | One review pass over the last answer or a draft: factual errors, logical leaps, missing requirements, repetition. Fixes only confirmed defects. | implicit allowed; also first word `dia-refine` |
| `dia-iterate` | Repeated review rounds, each gated by external verification; stops on regression, zero defects, verification exhausted, fixed point or `--max N` (default 3). | first word `dia-iterate` only |

`--target=claude` means the assistant's own earlier answer, on every assistant.

## Install

The repository is private: marketplace routes need GitHub access to it. The zip upload does not.

| Surface | How | Invoke |
|---|---|---|
| claude.ai web / Claude desktop | Download [`releases/dialectic-skills.zip`](releases/dialectic-skills.zip), then Customize › **Plugins** › Upload plugin. Not Customize › Skills: that screen rejects a zip with a plugin manifest. Requires "Code execution and file creation" to be enabled, even though no skill runs code. | `/dia:dia-<x>` or in words |
| Claude mobile | Install once through web or desktop; it reaches the app through the account. | in words |
| Claude Code | `/plugin marketplace add ajitta/dialectic-skills`, then `/plugin install dia@dialectic-skills` | `/dia:dia-<x>`, in words, first word for `dia-refine` and `dia-iterate` |
| Codex CLI / IDE | `codex plugin marketplace add ajitta/dialectic-skills` (or a local clone's path), then `codex plugin add dia@dialectic-skills`; fallback: copy `skills/dia-<x>` to `~/.agents/skills/` | `$dia:dia-<x>` for the plugin, `$dia-<x>` for a copied folder; `/skills` |
| ChatGPT desktop | Local plugin install from this repository (it reads `.claude-plugin/marketplace.json`); fallback: `~/.agents/skills/` | `@dia-<x>` |
| ChatGPT mobile | Plugin skills, where the plan allows; fallback: Codex cloud tasks on a repository that commits `.agents/skills/dia-<x>/` | `@dia-<x>`, in words |

Asking in words works on every surface and is the safe default on mobile. Which routes are verified is tracked in [docs/probes.md](docs/probes.md).

### Moving from the old skills

Remove the old copies first; otherwise each method loads twice under two names. On claude.ai: Customize › Skills — remove `reductio`, `negative-dialectics`, `self-refine`, `recursive-refine`, `confirm-intent`; Customize › Plugins — remove `socratic`. In Claude Code: `/plugin uninstall socratic@ajitta-socratic` and remove copies under `~/.claude/skills/`. For Codex / ChatGPT desktop: remove old copies under `~/.agents/skills/`.

## Repository layout

```
skills/dia-<x>/                 source: plain skills (SKILL.md, references/, agents/openai.yaml)
plugin-manifest.json            source for .claude-plugin/plugin.json
plugin-release.json             content digest for the current version (not shipped)
.claude-plugin/marketplace.json marketplace "dialectic-skills" -> ./plugins/dia
plugins/dia/                    generated, shipped
releases/dialectic-skills.zip   generated, shipped (top-level folder dia/)
tools/package.py                validate and build (developer-only)
tests/                          developer-only
upstream/                       material the skills were rebuilt from; never shipped
docs/spec.md                    specification
```

## Develop

```bash
python tools/package.py            # validate, write plugins/dia/ and the zip
python tools/package.py --check    # validate; fail if the committed output lags the source
python -m unittest discover -s tests -v
claude plugin validate --strict plugins/dia
```

Edit `skills/`, never the generated output. Any change to a skill file needs a new `version` in `plugin-manifest.json` (and the skill's `metadata.version`): Claude Code updates an installed plugin only when the version changes, and the check fails otherwise. Hangul is allowed only under `skills/<skill>/references/ko/`.

## License

MIT
