Verdict: PASS WITH FIXES

Scope: `git diff cae2e4d 7115d2a -- skills/dia-elenchus` plus the dia-elenchus parts of docs/spec.md (D19, D20, §4, §5, §7.3, §12.2), README.md and tests/. Line numbers refer to the tree at 7115d2a.

## Checks run

- `python3 tools/package.py --check`: exit 0, "ok dia-elenchus" (all seven ok). plugins/dia/skills/dia-elenchus/SKILL.md is byte-identical to the source.
- `python3 -m unittest discover -s tests`: 13 tests, OK, but skipped=1. The skipped test is `test_frontmatter_and_openai_yaml_parse` ("PyYAML not installed"), and it holds the one changed assertion (`startswith(f"Use $dia:{s.name} ")`). I re-ran with PyYAML installed into my scratch dir (PYTHONPATH only): 13 tests, OK, none skipped. CI installs pyyaml, so CI does exercise it.
- SKILL.md is 113 lines, the description 795 chars. No Hangul in skills/dia-elenchus, and no product names in the skill text. The only tool use is still conditional ("If a filesystem exists", l.100).
- Citations fetched from Perseus (Fowler/Lamb):
  - Euthyphro 9d ("shall we now emend our definition … Do you wish this now to be our definition") ✓
  - Laches 192d ("So, by your account, wise endurance will be courage") ✓
  - Charmides 166e ("whether it is Critias or Socrates who is being refuted: give the argument itself your attention") ✓
  - Laches 187e ✓ (it is Nicias speaking)
  - Protagoras 333c ✓, with a caveat (finding 5)
- Hunks that are correct and match the review's corrected form:
  - l.23: "emended or dropped" replaces the false "simply discarded", and Theaetetus is no longer cited as the authority.
  - l.31: the review's F5 text, verbatim.
  - l.86 and patterns l.39 (F3): the fix is in SKILL.md as the review asked, with a named-defect test.
  - l.92 (F4): the label uses the review's loci.
  - l.100 (F13): checked by script. All four criteria match record-template.md l.38-41 verbatim, including the second aporia condition.
  - patterns l.40 (F10): the anecdote is dropped, as the review asked.
  - l.76 (F8): the "restate the definition each turn" clause is dropped, as the review asked.
  - openai.yaml: `Use $dia:dia-elenchus …`.
- Logic: the worked example (l.82-84) holds. ① makes "spares deliberating" sufficient for "good", and ② is a case that spares deliberating and is not good, so the pair is inconsistent, and "can't both stand" claims no more than that.
- Version: still 0.1.0, and metadata.version is unchanged. docs/handoff.md:7 allows this before the first release, but AGENTS.md:26 states the rule with no exception. This affects the repo as a whole, not dia-elenchus alone, so it is not counted as a finding here.

## Findings

1. should-fix: SKILL.md:84, SKILL.md:92, elenchus-patterns.md:31. The new script breaks Rule 1.
   - Problem: Rule 1 (SKILL.md:35) says "Two asks joined in one sentence count as two ('where do you buy it, and how do you know?' is bundling)". The new script "Which would you change, and how?" has exactly that shape, and it now sits in the worked example that models copy word for word.
   - Neither document proposed ", and how". Both the research (F2) and the review proposed "Which would you change?". The addition first appears in the author's docs/research/README.md, so the change goes beyond the reviewed form.
   - Replacement at l.84: `> So ① and ② can't both stand as they are. Which would you change?`
   - Replacement at patterns l.31: `So ① and ② (or ①–③) can't all stand together. Which would you change?`
   - Replacement at l.92: replace `ask "Which would you change, and how?" and wait.` with `ask "Which would you change?" and wait; if they name only which one, ask in the next message how they would put it.`

2. should-fix: SKILL.md:76 and elenchus-patterns.md:23. Renumbering at layout time conflicts with the record format.
   - Before the change there was one running list ("a silent numbered list", "numbered silently"), so numbers stayed stable across contradictions.
   - Now the premises are numbered "then", at each layout, and every layout starts with ① = definition.
   - The second contradiction will therefore reuse ② and ③. record-template.md:11-18 assumes one global numbering ("fell on ② + ③", one "Agreed premises" list with ②, ③), so the record becomes ambiguous.
   - "Keep the agreed premises in the conversation itself, not in memory" can also be read as an instruction to print a running ledger each turn, which works against Rule 2 and the phone limit. On surfaces with a memory feature, "memory" can also be read as that feature. The research's wording was "recoverable from the conversation itself".
   - Replacement at l.76: `Don't rely on a private list: the agreed premises are the user's own answers in the conversation. Before laying out a contradiction, re-read those answers and number them then; a premise keeps its number for the rest of the dialogue and in the record. Patterns: [references/elenchus-patterns.md](references/elenchus-patterns.md).`
   - Replacement at patterns l.23: `Number premises when you first lay them out, from the user's actual answers, and keep each number once given. Use only those numbers in Step 4.`

3. should-fix: elenchus-patterns.md:51. F1 was applied in part, and the one-skill-era residue remains.
   - "These moves are the brainstorm's output." The research (F1) named this line as part of the residue.
   - The review (F1) warned that "A partial edit would leave the skill self-contradictory".
   - SKILL.md:23 now presents the list of ideas as this skill's own addition and no longer mentions brainstorming. The description (l.3) sends brainstorming to dia-brainstorm. This line now contradicts both.
   - Replacement: `These moves go in the record under "Ideas born". A rewording that changes nothing is not a birth; say so.`

4. should-fix: docs/spec.md:406 (§12.2 P2). The probe was narrowed for dia-elenchus beyond what the review intended.
   - The review asked to fix P2's wording for dia-intent (review/dia-intent.md M2, F7(a)). The diff applies "the prompt names the skill or uses its marker" to dia-elenchus and dia-brainstorm as well.
   - "Explicit-only" for dia-elenchus is a Codex/ChatGPT policy flag (`allow_implicit_invocation: false`). On Claude, the description is built for natural-language triggers ("socratic dialogue", "make me define it first", "or the same in any language"), and P7 measured exactly that (probes.md:53, 2/2).
   - dia-elenchus has no "marker".
   - docs/handoff.md:20 also says to use the P7 natural-language prompts for P2, which contradicts the new P2 text.
   - With this wording, P2 would no longer test the only route mobile users actually use.
   - Replacement for the sentence: `For dia-intent the prompt names the skill, and for dia-iterate it starts with dia-iterate; dia-elenchus and dia-brainstorm use the P7 prompts, which ask for the method by name in natural language. For dia-intent also check that the same request without the name does not load it.`

5. nit: SKILL.md:31. Protagoras 333c is accurate, but it undercuts the Stance bullet two lines above.
   - The full locus reads: "It is all the same to me … so long as you make answer, whether it be your own opinion or not. For although my first object is to test the argument, the result perhaps will be that both I, the questioner, and my respondent are brought to the test."
   - So it supports "argument first", but in the same breath it waives the sincere-assent rule that SKILL.md:29 presents as Socratic, and it says the respondent is tested too. Review §3 (A12) flagged this locus for that reason.
   - Charmides 166e alone supports the claim cleanly. Laches 187e-188a is Nicias's report.
   - Replacement: `Socrates put the argument first (Charmides 166e), though by Nicias's account he also tested how people lived (Laches 187e-188a); here only statements are examined.`

6. nit: SKILL.md:3 (description). The "ideas born" layer is labelled in the body but not in the description.
   - The description still opens "as in Plato's Socratic dialogues" and goes on to "each revision is a new idea the user gives birth to", which reads as part of Plato's method.
   - D19 says the layer is "labelled as this skill's own additions".
   - Replacement for the clause: `each revision is kept as a new idea of the user's (this skill's addition).` This stays well under 1024 chars.

7. nit: SKILL.md:100 (and record-template.md:38-41). The label criteria, now promoted into SKILL.md together with "exactly one of", are neither exhaustive nor exclusive.
   - Not exhaustive: a user who cannot give even a first definition (nothing fell, nothing to test) fits no label.
   - Not exclusive: a current definition that is "admittedly unclear" and has also passed some test fits both aporia and partly tested.
   - This gap was already in the template. The diff makes it a SKILL.md rule.
   - Replacement: append `If no definition was ever given, use stopped before testing. If aporia and another label both fit, use aporia.`

8. nit: docs/spec.md:64 (D19). The list is incomplete for dia-elenchus.
   - The diff also adds the "statements, not the person" label (SKILL.md:31; research README "Theme 4 … statements not persons"), and D19 does not mention it.
   - Replacement: after "labelled as this skill's own additions;", insert `"examine statements, not the person" is labelled as narrower than Socrates' practice;`.

## Intended items vs applied (check 5)

- Applied in full: Theme 1, Theme 2 (F3), the Theme 4 labels for the user-worded revision and for statements, not persons, F2 together with M3, F8, F10 and F13.
- Applied in part: the Theme 4 "ideas born" label. The l.23 label is in, but patterns l.51 (finding 3) and the description (finding 6) still frame the layer the old way.
- Applied with a deviation: F2's script (finding 1).
- Not intended in either batch, and not applied, which is correct: F4's quickness pattern, F9, F11, F12, F14, M4 and M5.

## D19/D20 vs the diff (check 6)

- D19's three dia-elenchus clauses (labels, the contradiction as a conflict of the set, withdrawal on a named defect) match l.23, l.84, l.86, l.92 and patterns l.31 and l.39. The omission is in finding 8.
- D20's three clauses (premises numbered from the visible answers, label criteria in SKILL.md, an irritation script) match l.76, patterns l.23, l.100 and patterns l.40.
- §4 and §7.3 are consistent with openai.yaml and the test.
- The §5 preamble ("unless this section, D19 or D20 says otherwise") covers §5.2's "Behavior: unchanged from the reference".
