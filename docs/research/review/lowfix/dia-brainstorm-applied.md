# Low-severity fixes: dia-brainstorm

Scope: `skills/dia-brainstorm/` only (SKILL.md, references/brief-template.md, references/question-bank.md). The description and agents/openai.yaml are unchanged. Not packaged, not committed.

## Per finding

- **F6 (criterion as option prompt): applied.** SKILL.md Step 3.2: "…the do-nothing option." -> "…the do-nothing option. If the user named what matters during probing, also ask once: "What option would win on <their criterion>, even if it loses elsewhere?"". The step order stays the same. Research Q2 (criteria before options) is still an owner question.
- **F7 (ask only what the user can answer): applied at the start of Step 2, as the review placed it.** SKILL.md Step 2: new opening paragraph "Ask only what the user can answer from their own experience or knowledge. If the idea turns on a fact neither of you can check here, don't ask them to guess it; record it under open questions as something to find out." Rule 1 is unchanged. The brief's Open questions section and the "find out X first -> open" verdict rule already fit this text.
- **F8 (confirmation phrasing): applied in the review's wording; the second sentence was dropped.** SKILL.md Step 1: `ask "Is that right?"` -> `ask "Is that right, or did I assume something you didn't mean?"`. "Never add parts they did not say" was not added because it conflicts with the marked-assumption steelman.
- **F10 (where advisor drift begins): applied, test-versus-replace sentence only.** SKILL.md Pitfalls, Advisor drift: added "Offering a concrete case to *test* their idea is fine; offering a different plan to *replace* it is not." after the existing sentence.
- **F11 (expert lenses): applied, full names only.** question-bank.md: "Drucker/Christensen/Taleb/Nygard/Hickey/Beck:" -> "Peter Drucker / Clayton Christensen / Nassim Taleb / Michael Nygard / Rich Hickey / Kent Beck:". Declined: the intro rewording and removing the quotation marks. The review found that the intro already says "in that person's spirit" and that the lenses have provenance (the upstream panel personas). Hickey's "incidental complexity" was already fixed (M4).
- **F12 (three is a floor): applied.** SKILL.md Step 3.1: added "When they stop, ask once "Any more, even odd ones?" before moving on." I put it at the end of the item, after "Build on each one…", not after the first sentence. It belongs after the building turns, and this order reads correctly.
- **F13 (shorter early-stopped brief): applied, merged with the existing rule.** brief-template.md:3: "Keep an empty section with "none" rather than dropping it, so the reader knows it was considered." -> "Mark an empty section "none" rather than dropping it; if several are empty, list them on one line ("None: parking lot, criteria, options") so the reader still sees they were considered." The single-empty-section case is kept, which the research's full replacement would have lost.
- **F14:** already done (per task). Untouched.
- **F15 (brainstorm probes): declined.** It adds probes to docs/probes.md, which is outside this skill's folder and is not a skill-text change. The probes have to be run first. That is an owner/process item.
- **M2 (switch rule Step 3 vs "3 or 5"): applied.** question-bank.md last line: "and move to Step 3 or 5." -> "and move to Step 3.". SKILL.md:71 already says Step 3. Step 3's skip rule (see M3) now sends pure stress tests on to Step 5, so going to Step 3 covers both cases.
- **M3 (Step 4 when Step 3 is skipped): applied.** SKILL.md Step 3: "Skip this step if the session was pure stress-testing and the user doesn't want options." -> "Skip this step and Step 4 if the session was pure stress-testing and the user doesn't want options; go to Step 5." The brief's Options and Criteria sections then get "none" under the existing template rule.
- **M5 (brief date): applied.** brief-template.md:6: `<YYYY-MM-DD>` -> `<YYYY-MM-DD, if known>`. The default file name `notes/brainstorm/<slug>-YYYYMMDD.md` (SKILL.md Step 5) is unchanged. It applies only when a filesystem is available, where the date is normally known. The owner can extend "if known" to it if wanted.
- **M6 (routing differs by surface): declined.** This is an owner/spec matter: spec §5.3 and §7.3 set explicit-only invocation, and upstream D2 accepted the Claude/Codex difference. Fixing it would mean changing the description, which this task forbids.

## Consistency check

I reread all of SKILL.md, brief-template.md and question-bank.md after editing:
- The new prompts are each one ask (Rule 1), and their quotation marks mark question templates, not user quotes (Rule 4).
- F7 adds no tool use. Its "open questions" matches the brief section and the "open" verdict rule.
- The Step 3/4 skip, the Step 2 "go to Step 3" rule and the question-bank ring now agree.
- F13 keeps "none" for a single empty section, so it agrees with SKILL.md Step 5's section list.
- No Hangul, no product names.

## Counts

- SKILL.md: 115 lines (was 113; limit 200).
- Description: 899 characters (unchanged; limit 1024).
- AGENTS.md requires version bumps for any skill-file change: `metadata.version` stays 1.0.0 under the pre-release exception. I did not touch plugin-manifest.json.
