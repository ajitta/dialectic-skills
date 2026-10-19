Verdict: PASS WITH FIXES

Scope: `git diff 1b3f139 b430a97 -- skills/dia-brainstorm` (3 files, 12 lines in SKILL.md, 2 in brief-template.md, 7 in question-bank.md). The same diff shows no changes to docs/spec.md, README.md, tests/ or docs/research/README.md, so this batch has no spec or tracking record (finding 1). The checks are against docs/research/dia-brainstorm.md §7 as corrected by docs/research/review/dia-brainstorm.md.

Runs (in the tree, read-only):
- `python3 tools/package.py --check`: "ok dia-brainstorm" … "ok dia-refine", exit 0.
- `python3 -m unittest discover -s tests`: 13 run, OK (skipped=1, PyYAML missing). Under `/usr/bin/python3` with PyYAML: 13 run, OK, 0 skipped.
- `diff -r skills/dia-brainstorm plugins/dia/skills/dia-brainstorm`: identical.
- No Hangul in skills/dia-brainstorm. SKILL.md has 115 lines (was 113). The description is 899 chars and unchanged, and so is agents/openai.yaml. No tool use or product name was added.
- Side effect: the unittest run created the gitignored `tests/__pycache__/` and `tools/__pycache__/` (timestamped 04:02:34 today). No tracked file changed.

Hunk-by-hunk (check 1), all confirmed:
- F8, SKILL.md:43: "Is that right, or did I assume something you didn't mean?" This is the review's exact wording. The second sentence is dropped, as the review asked, because it conflicted with the marked-assumption steelman. It is one ask in the "is it A or B?" form Rule 1 allows, and it now refers back to the "mark what you assumed" clause in the same sentence.
- F7, SKILL.md:47: the research's text, placed at the start of Step 2 as the review asked. Rule 1 is untouched. "Open questions" matches the brief section (brief-template.md:20) and the verdict rule at :100.
- M3, SKILL.md:79: "Skip this step and Step 4 … go to Step 5." Minimal. Options and Criteria then become "none" under brief-template.md:3.
- F12, SKILL.md:81: the research text. It sits at the end of item 1 instead of after its first sentence. That placement is better, because the nudge follows the "yes, and" turns.
- F6, SKILL.md:82: the research text ("add one prompt" became "also ask once"). It is asked of the user before "My ideas", so the user-first order holds. Steps are not reordered, so Q2 stays open.
- F10, SKILL.md:112: only the test-versus-replace sentence was appended, as the review asked. It agrees with the Counterexample tactic (:63) and Rule 3.
- F11, question-bank.md:50-55: full names only. The names are correct: Drucker, "Who is our customer? … What does the customer value?"; Christensen, jobs-to-be-done; Taleb, antifragility; Nygard, Release It!; Hickey, "incidental complexity" (fixed in D21); Kent Beck, TDD. The full name also removes the clash with Aaron T. Beck.
- M2, question-bank.md:61: "move to Step 3". This now matches SKILL.md:71. With M3, Step 3 sends a pure stress session on to Step 5, so no path is lost by dropping "or 5".
- F13, brief-template.md:3: merged instead of replaced. The single-empty-section "none" rule survives, which the research's full replacement would have lost. Correct.
- M5, brief-template.md:6: "<YYYY-MM-DD, if known>", as the review asked.

Logic and contradictions (checks 2 and 4): I traced the paths quick/standard/deep × develop/stress × stop signal × Step 3 skip. Step 2 dry switches lead to Step 3. Step 3 is either skipped to Step 5 or runs into Step 4, then Step 5, then the brief. Rule 3's "jump to Step 3" still holds. Rule 5's stop goes straight to Step 5. No rule now contradicts another rule, the template or the description. The description's "draws out the user's own options … converges by criteria" was already conditional, because the skip existed before. Smaller frictions are in findings 3-5.

Fidelity (check 3): the only method-adjacent change is the expert names, all correct (above). No Stephanus number, Paul, Osborn or Padesky claim changed.

Declines (check 6):
- F11 intro rewording and quote removal: justified. question-bank.md:49 already says "in that person's spirit". Every bank entry uses quotes for question shapes ("Shapes, not scripts", :3), and the review documented the lenses' provenance.
- F15 (probes): justified. It is a docs/probes.md item and owner-run (handoff: P2 open).
- M6: the decline is justified (spec §5.3 and table line 269: explicit-only, accepted upstream D2), but the reason given is off. The review's remedy was an open question, not a description change. It must stay tracked (finding 1).
- M7 (versioning) is not mentioned in the implementer's per-finding list. It is a research-document/process item, and the pre-release exception (AGENTS.md; handoff "still 0.1.0") covers it. Acceptable, but the bump at release still applies.
- The implementer's report says "Not packaged, not committed", but b430a97 contains the regenerated plugins/ and releases/ (package --check passes). The report is stale, which is harmless.

Not applied (check 5): nothing intended is missing from the skill text. F14 (`$dia:dia-brainstorm`, openai.yaml:4) was done in D19.

Findings

1. should-fix: docs/spec.md:64-67 and :136, and docs/research/README.md:53. The batch is unrecorded. Spec §5.3 says "Behavior: the reference, amended by D19–D22", but this commit adds new behavior: ask only answerable questions, skip Step 4 with Step 3, the "Any more" nudge, the criterion prompt, and the collapsed "None:" line. No decision row covers it. docs/research/README.md:53 "Still open" still lists "brainstorm F6–F15 and M2, M3, M5, M6". F14 has been stale since D19, and F6-F13, M2, M3 and M5 are now applied. The commit touches all seven skills, so the record is presumably batch-wide. The brainstorm part:
   - Add a spec row after D22: `| D23 | Remaining low research findings, in the reviewed forms (2026-10-20). dia-brainstorm: ask only what the user can answer and record uncheckable facts as open questions; a "did I assume something" confirmation; Step 4 is skipped with Step 3; one "any more" nudge and one criterion prompt in Step 3; test cases versus replacement plans in advisor drift; full names for the expert lenses; one "None:" line for several empty brief sections; the brief date only if known. … (other skills) |`. Change spec :121, :128 and :136 (and the other §5 lines) to "amended by D19–D23".
   - In docs/research/README.md:53, replace "brainstorm F6–F15 and M2, M3, M5, M6" with "brainstorm F15 (probes) and M6 (surface routing, owner)". Add a "## Applied, fourth batch (spec D23, 2026-10-20)" section listing "dia-brainstorm F6, F7, F8 (first sentence), F10, F11 (full names), F12, F13, M2, M3, M5".

2. nit: SKILL.md:47. "a fact neither of you can check here" implies that the assistant should check a fact when it can. That leaves the tool case undefined and sits badly with brief-template.md:3 ("Fill every section from the user's answers only") and SKILL.md:105 ("Build it only from the user's answers"): a fact the assistant looked up has no legitimate place in the brief. Replacement:
   "Ask only what the user can answer from their own experience or knowledge. If the idea turns on a fact the user can't answer from what they know, don't ask them to guess it; record it under open questions as something to find out."

3. nit: SKILL.md:79 together with :93. When Step 4 is skipped, the rule "Record each decision as confirmed … or delegated …" is skipped with it. Yet a stress session can produce decisions during probing, and the brief still has Decisions (confirmed | delegated). Replacement for :79:
   "Skip this step and Step 4's questions if the session was pure stress-testing and the user doesn't want options; record any decision already made as Step 4 describes, then go to Step 5."

4. nit: SKILL.md:105. M5 was fixed in the template but not in the default file name `notes/brainstorm/<slug>-YYYYMMDD.md`. "A filesystem is available" does not guarantee a known date without a tool call, so the same "invent nothing" issue remains, even if it is less likely. Replacement:
   "(default `notes/brainstorm/<slug>-YYYYMMDD.md`, or `<slug>.md` if the date isn't known)"

5. nit, optional (touches owner question Q2): SKILL.md:89. F6 now uses a criterion the user named during probing, and Step 4.1 then asks "What matters most here?" from scratch, so the user may give the same answer twice. Replacement for the first sentence of :89:
   "\"What matters most here?\" Get 2-3 criteria in the user's words, starting from any they already named."

6. nit: brief-template.md:3. The collapsed line's "None:" label is English, but the template says only to translate the section headers. Replacement for the clause:
   "list them on one line (\"None: parking lot, criteria, options\", in the user's language)"

No blockers. The skill-text changes are faithful, minimal and consistent. Finding 1 is a record fix, not a behavior fix.
