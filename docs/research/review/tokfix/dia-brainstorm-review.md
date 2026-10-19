Verdict: PASS

Scope: `git diff d135f8e 75d7ac1 -- skills/dia-brainstorm` (3 deletions, 0 additions) plus D24 and §5 in docs/spec.md. Every claim below was checked against the files in the tree and against `git show d135f8e:<path>`, not against the implementer's account.

## What changed (verified)

| Audit item | Old text (d135f8e) | Now |
|---|---|---|
| S9 | SKILL.md:66 `... A belief nothing could disconfirm is a finding, not a strength. Required at least once in `stress`.` | The last sentence is deleted. The same rule stays at SKILL.md:72: "In `stress`, do at least one falsification probe." |
| S17 | SKILL.md:115 `- **Wall of text on a phone**: if a turn needs scrolling, cut it.` | The bullet is deleted. The same rule stays at SKILL.md:21 (Rule 2): "A turn fits a phone screen without scrolling." |
| Q1 | question-bank.md:57 `- **Edges** (Step 3): cheapest version · most extreme version · do nothing.` | The bullet is deleted. The same edges stay at SKILL.md:82: "Push the edges once: the cheapest version, the most extreme version, the do-nothing option." |

Token counts, re-measured with tiktoken cl100k_base in a scratch venv:
- SKILL.md file: 2,963 → 2,937.
- SKILL.md body: 2,695 → 2,669 (−26).
- question-bank.md: 725 → 706 (−19).
- brief-template.md: 465, unchanged.

These match the account and the audit's forecast for S9 + S17 + Q1.

## Check 1: Behavior loss

None found.

- S9: the tactic line and the Rhythm line had the same scope ("in `stress`", any depth). The kept copy, SKILL.md:72, is a standalone sentence and is not bound to "At standard depth", so `quick` + `stress` still requires the probe. The rationale "A belief nothing could disconfirm is a finding, not a strength" (audit S8) is kept.
- S17: Rule 2 (SKILL.md:21) states the constraint, and SKILL.md:83 keeps the explicit Step 3 exception. The removed pitfall had no exception, so it slightly conflicted with SKILL.md:83. Removing it eases that conflict and creates none. The only loss is an end-of-file reminder, which is a position effect (evidence.md §4). Rule 2 sits at the top of the body, which is also a favoured position. Risk: low.
- Q1: deleting this line removes a latent inconsistency. In the old bank, Edges was listed under "Optional lenses (pick at most two, only when the idea calls for one)" (question-bank.md:46). In SKILL.md:82, edges are not optional ("Push the edges once"). SKILL.md:75 never listed Edges as a lens. So no lens, edge or fallback is lost, and the no-reference path is untouched because the body still holds the edges.
- D19–D23, checked one by one in the current files. All are present and word-for-word unchanged:
  - D19: L16 label and midwife sentence.
  - D21: one summary cadence (L74), the thesis-after fallback (L97, brief-template:12), Hickey's term (bank:54).
  - D22: deep checkpoint replaces the probe (L33), Step 0 Socratic deferral (L37), narrowed kind rule (L83), standalone pacing cue (L74).
  - D23: answerable-only questions (L47), "did I assume something" (L43), Step 4 skipped with Step 3 (L79), "Any more" nudge (L81) and criterion prompt (L82), test vs replace (L112), full expert names (bank:50–55), "None:" line (brief-template:3), date only if known (L105, brief-template:6).

  L16 is byte-identical to d135f8e. The description, the frontmatter, agents/openai.yaml and `metadata.version` "1.0.0" are untouched.

## Check 2: Contradictions introduced

None. I read the whole of SKILL.md (114 lines), question-bank.md and brief-template.md after the change:
- No dangling references. Nothing pointed to the "Wall of text" pitfall or to the Edges bullet; grep for "Edges", "Wall of text" and "scroll" finds only Rule 2 and brief-template:3.
- No renumbering: the steps, hard rules and section headings are unchanged.
- The template and the body still agree.

## Check 3: Moved text

Nothing was moved. No new reference file was added, so spec §5.3's reference list ("question-bank.md and brief-template.md") is still correct.

## Check 4: Fidelity

No citation, attribution or label was moved or changed. The expert names and Paul's label are untouched, so there was nothing to fetch.

## Check 5: Set conformance

- Applied: S9, S17, Q1. These are exactly the items the audit's §4 marks as having no owner-decision dependency.
- Not applied: S1–S3, the L16 rewording. The audit lists it in §4, but its own row S1 says "Needs a light owner OK, because it rewords the owner's label text", and §4 gives a "safe remainder" for the case where the owner declines. Under the stated approval scope ("no owner-decision ... items"), leaving it out is correct. D24 records it as "Not applied (owner decisions not taken): dia-brainstorm's method-paragraph rewording". I cannot verify the owner's chat, but the record agrees with the brief I was given.
- Optional items S6, Q2, B1 and B2 were not applied. Correct.
- No item outside the set was applied.

## Check 6: Repo rules and commands

- `python3 tools/package.py --check`: "ok" for all seven skills, rc=0.
- `python3 -m unittest discover -s tests`: 13 tests OK, with 1 skipped for missing PyYAML under the system python. Re-run in a scratch venv with PyYAML: 13 tests OK, 0 skipped.
- `plugins/dia/skills/dia-brainstorm` is identical to the source (`diff -r`). The brainstorm .md files inside `releases/dialectic-skills.zip` are byte-identical to the source.
- All three files: no CR characters, no Hangul, end with one LF. SKILL.md is 114 lines (limit 200). The text stays assistant-neutral and tool use is still conditional (L105 "If a filesystem is available").
- Spec D24 and §5 are accurate for brainstorm. "Duplicated pitfalls ... were cut, labels ... kept", "D19–D24" in §5.3, and an unchanged reference list all match the diff.

## Findings

1. nit: docs/research/review/tokfix/dia-brainstorm-applied.md:3, wording only.
   - Problem: the account says "Worktree: `/home/ubuntu/work/dia-review/tokfix` (branch `tokfix`)... No commit was made." It is now committed as 75d7ac1, so the note reads as stale.
   - Replacement: "Applied in the `tokfix` worktree and committed as part of 75d7ac1."

2. nit: SKILL.md:72 and SKILL.md:21; open verification, not a defect.
   - Problem: evidence.md:95 (rule 13) asks for probe validation of removals. No brainstorm dialogue probe exists, and the audit's suggested checks (§6.1: a `stress` session of 5+ turns with at least one falsification probe and every turn within one phone screen) were not run. The removals are exact in-file duplicates, so the expected effect is nil. The account records this gap honestly (lines 34–35).
   - Replacement: none in skill text. Keep it listed under docs/research/README.md "Still open" with the multi-turn brainstorm probes.

3. nit, pre-existing (not introduced by this diff, optional): SKILL.md:83.
   - Problem: "this one message may run past the line limit" refers to a "line limit" that the skill never defines. Rule 2 (L21) sets a screen limit, not a line count. The deleted S17 pitfall did not define one either, so the diff neither caused nor worsened this.
   - Replacement, if the owner wants it: "Number every option so far; this one message may run past one phone screen, so keep each option to one short line."

No blocker or should-fix findings.
