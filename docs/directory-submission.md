# Directory submission: Anthropic and OpenAI

What listing `dia` in each vendor's public plugin directory requires, checked against the repository at 1.1.0. Researched 2026-10-20 from the vendors' current documentation (sources at the end). Nothing has been submitted.

Why list at all: on mobile, neither Claude nor ChatGPT lets a user add a marketplace or upload a zip. A directory listing is the only way to install from a phone. ChatGPT mobile has a Plugins page that browses the directory. Whether the Claude mobile app can browse the directory is not documented and not yet checked.

## Anthropic directory (claude.ai Discover, Cowork, Claude Code)

**Who and where.** A paid claude.ai plan (Pro, Max, Team or Enterprise). The developer portal is at `claude.ai/directory/manage` (Submit new › Plugin bundle). The submitter's GitHub account must be connected on claude.ai and able to push to the repository. The repository must be public before the listing goes live; `ajitta/dialectic-skills` is.

**Source fields.** Repository `ajitta/dialectic-skills`, plugin path `plugins/dia`, branch empty (default branch).

**Review.** Validate in the portal, fix every Blocking finding, then submit. Each version gets automated validation and a security scan; a person reviews a new listing before it goes live. After approval, Publish (a reviewer publishes by default). Later versions are picked up by GitHub push webhook or a scheduled check.

| Check | `dia` at 1.1.0 | Result |
|---|---|---|
| `.claude-plugin/plugin.json` in the plugin folder | `plugins/dia/.claude-plugin/plugin.json` | passes |
| README of at least 40 words **in the plugin folder** (code blocks don't count) | `plugins/dia/` has no README | **Blocks** |
| `LICENSE` in the plugin folder, or `license` in `plugin.json` | `"license": "MIT"` | passes |
| `name`: lowercase ASCII, digits, hyphens, at most 64 | `dia` | passes the pattern |
| Name not taken by another organization; not a generic word; not a known brand | `dia` is short and generic-looking | unknown until Validate; a generic name is held for a reviewer, a taken name blocks |
| `description`, `author`, `version` set | all set | passes |
| Only text files, images and fonts; each non-image file under 256 KiB; at most 512 files | Markdown, YAML and JSON only | passes |
| No `.DS_Store`/`Thumbs.db`, no symlinks, submodules or LFS; Windows-safe file names | none | passes |
| No `export-ignore`/`export-subst` or content filters in `.gitattributes` | `* text=auto eol=lf`, `*.zip binary` | passes |
| Repository under 50 MiB archived, under 10,000 files | 6.2 MB `.git`, 174 files | passes |
| Valid skill front matter, `description` a single string | checked by `tools/package.py` | passes |
| No hooks, MCP servers, launchers, credentials | none (spec §7.1) | passes |
| README describes everything the plugin runs, sends or fetches (security scan) | the skills run nothing; "if a search tool is available" use is described in the skills | to state in the plugin README |

**Data handling answers.** Reads or stores personal data: no. Sends data to other services: no. Retention: none. Intended for people under 18: no.

## OpenAI plugin directory (ChatGPT and Codex)

**Who and where.** An OpenAI Platform organization. The submitter needs Apps Management write (organization owners have it). The publisher must complete **individual verification** (own name) or business verification in organization settings; an unverified identity is rejected. Submission is a ZIP upload in the plugin submission portal (Plugins › Upload new or existing plugin, path "Skills only").

**Review.** Upload, resolve automated findings, Submit for review with policy attestations. Skill safety and security scans can take up to 2 hours. After approval, the developer publishes. Metadata or skill changes need a new ZIP. Skills-only plugins "may be subject to additional eligibility requirements".

| Requirement | `dia` at 1.1.0 | Result |
|---|---|---|
| Manifest: `.codex-plugin/plugin.json`, or `.claude-plugin/plugin.json` (converted by the portal) | `.claude-plugin/plugin.json` in the zip's single top-level folder `dia/` | accepted, normalized |
| `name` ASCII, at most 64; semantic `version`; `description` at most 1,024; `author.name` | all present | passes |
| Skill identity `plugin:skill` at most 64 characters; unique skill names | `dia:dia-brainstorm` (18) is the longest | passes |
| Each skill's `agents/openai.yaml`: `interface.display_name`, `interface.short_description` | present in all seven | passes |
| `interface.displayName` at most 30 | "Dialectic Skills" (16) from `displayName` | likely passes after conversion |
| `interface.shortDescription`, one line, **at most 30** for final submission | not set | **missing** |
| `interface.longDescription` (at most 4,000), `interface.developerName`, `interface.category` (e.g. `Productivity`, `Education & Research`) | not set | **missing** |
| `interface.capabilities` (up to 20) and starter prompts `interface.defaultPrompt` (up to 3, at most 128 characters, one line) | not set | recommended |
| `interface.logo` and `interface.composerIcon`: square PNG, JPEG, WebP or SVG, 48–4,096 px | no image in the package (spec §7.1 ships Markdown, YAML and JSON only) | **missing; needs a spec change or an OpenAI-only zip** |
| Website, privacy, terms, support URLs | optional for skills-only ZIPs | optional |
| Test cases, demo video, reviewer credentials | required for remote MCP plugins only | not required |
| Guidelines: clear purpose, not a generic single-word name, no comparison claims, works on desktop and mobile | owner probes P4/P5 passed on Pro | to confirm in review |

## Gaps to close, in order

1. **Anthropic, blocking:** a plugin-folder README (`plugins/dia/README.md`, at least 40 words outside code blocks) that says the plugin is instructions only and runs, sends and fetches nothing itself. It is a shipped file, so spec §7.1 needs a row for it and the plugin needs a version bump.
2. **Anthropic, owner:** connect GitHub on claude.ai, then Validate in the portal. Validate also tells whether the name `dia` is taken or held as generic.
3. **OpenAI, owner:** individual verification on the OpenAI Platform; check Apps Management write.
4. **OpenAI, package:** the `interface` listing fields and two square images. Either a separate OpenAI build (`.codex-plugin/plugin.json` with `interface` plus image assets, generated by `tools/package.py` into its own zip) so the main package stays text-only, or images added to the main package by a spec change.

## Sources

- Anthropic: [Publish to the directory](https://claude.com/docs/directory/publish), [Submit your plugin](https://claude.com/docs/plugins/submit), [Plugin pre-submission checklist](https://claude.com/docs/plugins/pre-submission-checklist), [Track your directory submission](https://claude.com/docs/directory/submission-status).
- OpenAI: [Submit plugins (Developers)](https://developers.openai.com/plugins/deploy/submission), [Submit plugins (ChatGPT Learn)](https://learn.chatgpt.com/docs/submit-plugins), [Plugin submission errors](https://developers.openai.com/plugins/deploy/submission-errors), [Plugin guidelines](https://developers.openai.com/plugins/plugin-guidelines), [Plugins in ChatGPT (Help Center)](https://help-lb.openai.com/en/articles/20001256).
