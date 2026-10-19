# Token audit: dia-elenchus

Date 2026-10-20. Tree at `d5e9efa`. Research only: no skill file was edited.

## Method

- Units: each sentence, bullet, table row or heading in the SKILL.md body (frontmatter excluded, since Claude Code injects the body only; `docs/token-cost.md`) and in each reference. Embedded parentheticals such as a Stephanus locus were carved out and counted under their own class.
- Classes: **A** instruction, **B** rationale, **C** provenance, label or citation, **D** example or template, **E** redundant (restates the same file, or a file loaded with it; SKILL.md is always in context when a reference is read), **F** meta (pointers). **H** is structure (headings, list numerals, code fences). It is outside A–F and is not a candidate.
- Tokens: tiktoken `cl100k_base`. The class sums are per-unit counts, so they fall short of the file totals by 9–12 tokens (newlines and joins). Every saving below is the exact whole-file delta, computed by applying the proposed text to a scratch copy. Claude ≈ 1.5 × cl100k (`docs/token-cost.md`).
- Evidence used: spec §5.2, §7.1 and D19–D23; `docs/probes.md` (P7, and P8's observation that some headless runs could not open references); `docs/research/dia-elenchus.md`; the reviews in `docs/research/review/` (first pass, diff, pass2, lowfix); `docs/research/README.md` theme 4 ("honest method labels") and theme 5 (fallbacks when references are unreadable); `tools/package.py` (it validates relative Markdown links).

## Per-class totals (cl100k)

| File | A | B | C | D | E | F | H | File total |
|---|---|---|---|---|---|---|---|---|
| SKILL.md body (per invocation) | 1,689 | 45 | **416** | 220 | **154** | 53 | 110 | 2,699 (2,992 with frontmatter) |
| references/elenchus-patterns.md | 406 | 7 | 16 | 423 | 83 | 0 | 66 | 1,010 |
| references/record-template.md | 116 | 7 | 0 | 235 | **155** | 0 | 8 | 532 |

Reading the table:

- SKILL.md carries 416 tokens of class C: Stephanus loci, scholarly attributions and the D19/D23 fidelity labels, which is 15% of the body. Every turn pays them, and a long dialogue pays them again as cached input on each later turn.
- About 150 of the 416 are the labels themselves ("this skill's addition", "stricter than Socrates", "narrower than…", "drop the irony", "instead of a virtue"). These are load-bearing: they tell the model to override what it knows of Plato's Socrates, who words revisions, exhorts and is ironic. The other ~260 are loci and the scholarly reasons behind them. No rule depends on those.
- Class E in SKILL.md is mostly the six-step "shape" overview (restated by Steps 1–6) and three pitfalls that repeat rules.
- Class E in record-template.md is the result-label criteria, which SKILL.md Step 6 already holds verbatim (added there for the P8 fallback, D20/F13). The SKILL.md copy has to stay, so the template's copy is the redundant one.
- Class D is almost all load-bearing. The research (F2) notes that models copy the worked contradiction word for word, and the patterns file is mostly scripts and templates.

## Candidates: SKILL.md (per invocation)

"Save" is the exact file delta. "LB" is load-bearing.

**E1. Intro, l.14** (C+E, 114 → 77, save 37 before the pointer). "the method of Plato's early (Socratic) dialogues such as the Euthyphro, Laches and Charmides … Plato applied it to virtues such as piety and courage; here it is applied to the concept behind the user's idea."
- LB: partly. The scope label (D23) and the "aids, not the method" label (upstream review L3) are load-bearing. The dialogue names are not.
- Proposal, shorten to: `This skill runs the **elenchus** of Plato's early dialogues, applied to the concept behind the user's idea instead of a virtue. Two later images serve as aids, not as the method: aporia as a gain (Meno) and the midwife (Theaetetus). It is not the modern list of "Socratic question types". Sources and departures from Plato: [references/theory.md](references/theory.md); read it only if the user asks about them. The shape:` The pointer costs 28 tokens.
- Risk: very low. The D23 scope label survives as "instead of a virtue".

**E2. Addition and midwife, l.23** (C+E, 152 → 80, save 72). "In the early dialogues a definition that falls is emended or dropped … (Theaetetus 150b-151d; the wind-egg image is at 151e) … stricter than the Theaetetus, where the midwife, claiming none as his own, still offers others' theories to bring out the respondent's view (157c-d)."
- LB: the two labels (D19 "this skill's addition"; D23 the midwife departure) and "no ideas to hand over" are. The loci and the explanation of what the dialogues do are not.
- Proposal: `This skill adds one thing the dialogues do not have: **the revisions are kept as ideas**, each a direction the user had not stated before. You are the midwife, with no ideas to hand over (stricter than the Theaetetus midwife, who offers others' theories): you help the user's ideas come out and test whether each is sound or a wind-egg.`
- Risk: low. Step 5 ("keep a list") and the record's "Ideas born" still drive the behavior. A multi-turn elenchus probe (still open, research README item 1) would catch a dropped list.

**E3. Stance "You don't know", l.27** (C+E, 70 → 39, save 31). "(Apology 21d) … Socrates too asked without answering (Aristotle, Sophistical Refutations 183b), though he also exhorted (Apology 29d); you never advise."
- LB: the departure (Socrates exhorted; you don't) is a label. The citations are not load-bearing, and "you never advise" repeats Rule 6.
- Proposal: `- **You don't know.** Ask as someone who wants to learn what X is. Give no answers, advice, solutions or options (Socrates also exhorted; you never do).` The rest of the bullet is unchanged.
- Risk: low. D23 says the stance "is cited to Aristotle". The citation moves to theory.md, so it stays available but leaves SKILL.md, and the owner should confirm (see Decisions).

**E4. Irony, l.28** (C, save 12). "Plato's Socrates was known for irony (Republic 337a); you drop it: no feigned…"
- Proposal: `Drop Socrates' irony: no feigned…`
- LB: the rule and the "drop" label are; the locus is not. Risk: none.

**E5. Sincere assent, l.29** (C, save 14). "(Crito 49c-d, Gorgias 495a)". Cut it and move it to theory.md. LB: no. Risk: none.

**E6. Brevity, l.30** (C+B, save 16). Cut "(Protagoras 334c-335c)" and ", which also suits a phone". The phone point repeats Rule 2. LB: no. Risk: none.

**E7. Statements, not the person, l.31** (C+E, 68 → 40, save 28). "Socrates put the argument first (Charmides 166e), though by Nicias's account he also tested how people lived (Laches 187e-188a); here only statements are examined."
- LB: the D19 label "narrower than Socrates' practice" is. The loci, and "here only statements are examined" (which repeats the bullet's heading), are not.
- Proposal: `- **Examine statements, not the person** (narrower than Socrates, who also tested how people lived). A contradiction belongs to the statements; the user decides what to give up.`
- Risk: low.

**E8. Step 2, l.59** (C, save 17). Cut "(Euthyphro 6d-e, Meno 72a-c)". LB: no. Risk: none.

**E9. Step 3, l.70** (D+C, save 28). "In Laches 190e-191c, courage was defined as standing your ground, yet the Scythians fight while retreating."
- LB: no. "Too narrow" is fully defined in the bullet. The model copies domain examples, not ancient ones; the domain examples are l.74 and patterns l.19.
- Proposal: cut it and move it to theory.md. Risk: low. A model that is unsure what "too narrow" means can read the patterns template.

**E10. Step 5, l.92** (C, save 15). Cut "(Euthyphro 9d, Laches 192d)" and keep the label: `This is stricter than Socrates, who sometimes worded the revision himself; here the user's own wording is the point.`
- LB: the label and its reason are. Research M2 calls this the strongest fidelity gap, and the label stops the model imitating Euthyphro 9d. The loci are not load-bearing. Risk: none.

**E11. Step 6, l.98** (C, save 16). Cut "(Meno 84a-c, Theaetetus 210b-c)". LB: no; the instruction (tell the user what aporia gives them) stays. Risk: none.

Optional, not in the recommended set:

**O1. The six-step "shape", l.16-21** (E, 98 → 51, save 47). Every step is restated in Steps 1–6.
- LB: weak. It orients the model before the details, and "That is the result, not a failure" (B) guards against rescuing the user at aporia (research risk 6.1.2).
- Proposal: `Ask "What is X?", get a definition, collect agreed premises one at a time, show where they contradict it; the user revises, and you go round again. Most dialogues end in **aporia**: a result, not a failure.`
- Risk: low to medium. The overview is the model's first picture of the loop. Gate it on a multi-turn probe.

**O2. Pitfall "Declaring the user wrong", l.111** (E, save 23). It repeats Stance l.31 and Step 4 l.86. Risk: low. The pitfalls act as a closing checklist, so expect a small recency loss.

**O3. Pitfall "Wall of text", l.113** (E, save 19). It repeats Rule 2. Risk: low. The phone limit is the rule models break most over long dialogues (research §3), so keeping both copies is defensible.

## Candidates: references (paid only when read)

`docs/token-cost.md` found that a first elenchus turn reads no reference. record-template.md is read once, at the end. elenchus-patterns.md is read when the model looks up premise or pushback shapes.

**P1. patterns l.3** (E, save 7). Cut "Ask in the user's language." It repeats SKILL.md Rule 7, which is in context. Risk: none.

**P2. patterns l.22** (C, save 10). Cut "(Meno 86e-87b)" and move it to theory.md. Risk: none.

**P3. patterns l.24** (E, save 24). Cut "Number premises when you first lay them out, from the user's actual answers, and keep each number once given."
- This repeats SKILL.md l.76 nearly word for word. Keep "① is always the current definition. Agreed premises start at ② …" (D22).
- Risk: low. The D21 stability rule stays in SKILL.md, the copy that P8 guarantees.

**P4. patterns l.28-35** (D+A, save 24). Write the contradiction template as a quote block (`> ① <definition> (definition)` and so on), then drop "In chat, render it as plain lines or a quote block, not a code block. The code block above only shows the shape."
- Risk: low. It removes the code block the warning exists to neutralise, and SKILL.md l.82-84 already uses a quote block.

**P5. patterns l.46** (E, save 25). Replace it with `Moves usually go one of these ways; the kinds help you notice a move (Step 5), so don't print them:`.
- The cut part ("name the move in one line, in the user's own key words: <old> → <new>") restates SKILL.md l.92, which is the stricter copy (lowfix review finding 4).
- Risk: low.

**P6. patterns l.52** (E, save 15). Cut "A rewording that changes nothing is not a birth; say so." It repeats SKILL.md l.94. Risk: none.

**R1. record l.3** (E+B, save 16). Cut "Print plain Markdown, not a code block (code blocks scroll sideways on phones)." SKILL.md l.100 says the same at the moment the template is read. Risk: none.

**R2. record l.38-43** (E, 130 → 36, save 94). Replace the six label bullets with `- Result: use the criteria in SKILL.md Step 6. For partly tested, name the tests it passed; for stopped before testing, name which definitions fell before that.`
- The criteria are verbatim copies of SKILL.md l.100, which must stay there for P8. The two "name …" clauses are the template's only additions, and they are kept.
- Risk: low. It also ends the drift that pass2 finding 3 had to repair, because there is now one source.

**R3. record l.46** (E, save 28). Cut "A later `dia-brainstorm` session can start from the ideas born. Mention it only if the user asks what's next." SKILL.md "After the dialogue (only on request)" already says it. Risk: low.

## Kept on purpose (non-A units)

- **Every fidelity label, in SKILL.md, shortened where shown.** These are: this skill's addition (D19); the user-worded revision being stricter than Socrates (D19); statements narrower than Socrates' practice (D19); scope instead of a virtue, the departure from the midwife, irony dropped, and the exhortation departure (D23); Meno/Theaetetus as aids (L3). They are load-bearing as overrides of the model's knowledge of Plato's Socrates, who words revisions, exhorts and uses irony. They must also survive unreadable references (P8). Only their loci move.
- **"It is not the modern list of 'Socratic question types'"** (l.14, E, 13 tokens). It anchors against the strongest prior: v1 of this skill was Paul-style questioning (research §5), and hosts' study modes push the same way (D23).
- **Short rationales:** "That is the result, not a failure" (l.21), "poisons the argument" (l.29), "that stalls the examination" (l.61) and "seeing the collision is the point" (l.80), 45 tokens together. The last two came from probe-driven fixes (upstream 09 §6), and each tells the model how to handle cases the rule does not list.
- **All SKILL.md examples** (220 tokens): the Step 1 concept examples, the restatement example, the retro premise example, the worked contradiction (copied verbatim, research F2), the forbidden-revision example and the shift example. The patterns scripts and the record template are kept too, including the quickness model definition with its "Laches 192b" tag (D23; the definition is the example, and the tag is 5 tokens).
- **The result-label criteria and "plain Markdown" in SKILL.md l.100.** These are the P8 fallback (research theme 5, D20).
- **The general "Socratic" routing line, l.53** (82 tokens). It came from the routing fixes (D21/D22, P7 Part B).
- **Markdown link syntax for references.** Plain paths would save about 30 tokens, but `tools/package.py` (l.157-159) checks relative links only in `](…)` form, so they would lose that check. Rejected.

## Where the moved citations go

Add `references/theory.md`, the convention dia-reductio and dia-negative already use. It would be read only on the user's question, through the E1 pointer. The draft below holds every moved locus and attribution with the label it supports, and is 488 cl100k tokens. In outline:

- the early dialogues by name, with virtues as the original scope;
- Meno 84a-c and Theaetetus 210b-c (aporia), Theaetetus 150b-151d and 151e (the midwife), and 157c-d (the midwife's departure);
- Apology 21d, Aristotle *Soph. El.* 183b and Apology 29d;
- Republic 337a;
- Crito 49c-d, Gorgias 495a and Protagoras 334c-335c;
- Charmides 166e and Laches 187e-188a;
- Euthyphro 6d-e and Meno 72a-c;
- the Laches Scythians example, Meno 86e-87b and Laches 192b;
- Euthyphro 9d and Laches 192d;
- "in the early dialogues a definition that falls is emended or dropped, and nobody keeps a list of ideas".

The alternative of appending a Sources section to elenchus-patterns.md is worse: the file is read mid-dialogue, so the citations would load with it.

## Recommended set and saving

| Set | SKILL.md body cl100k | Saving per invocation |
|---|---|---|
| Today | 2,699 | — |
| E1–E11 with the theory.md pointer (recommended) | 2,441 | **258 cl100k (−9.6%), ≈ 390 Claude tokens** |
| E1–E11, citations cut with no theory.md (owner decision, D19–D23) | 2,413 | 286 |
| Recommended plus O1–O3 | 2,352 | 347 |

- References: patterns 1,010 → 905 (P1–P6) and record 532 → 394 (R1–R3), saving 105 and 138 when read. Most sessions that finish read the record once, so a full session saves about 400 cl100k before counting multi-turn re-sends.
- Worst case (every file read): 4,534 → 4,529 with theory.md (488) included. The move does not raise the worst case.
- Multi-turn: SKILL.md stays in context, so the 258 tokens are also saved as cached input on every later turn.

## Risks and how to catch them

- **No behavior rule changes in E1–E11:** every instruction, label and example stays, and only loci, ancient examples and explanations of the scholarship move. The behavior these moves could most plausibly change:
  - Answers to "is this really what Socrates did?" now depend on reading theory.md. If references are unreadable (P8), the model still has the labels but answers loci from recall. Catch: a turn asking "where does the no-advice rule come from?", checking that theory.md is read and the answer matches it.
  - Shortened labels might weaken the override of Socratic priors, for example the model wording the revision itself as at Euthyphro 9d. Catch: the scripted lunch/retro multi-turn dialogues, which the research README lists as still open and which have not yet been run for dia, checking Step 5 (user writes the revision) and Rule 6 (no advice at aporia).
- **P7 routing is unaffected:** the description and frontmatter do not change.
- **P8 (references unreadable):** unaffected. Every fallback the research asked for (label criteria, plain Markdown, the pushback rule at l.86, stable numbering) stays in SKILL.md.
- **R2 and P3** remove the reference-side copies of SKILL.md rules. If SKILL.md is ever trimmed later, check these first.

## Owner decisions needed

1. Moving the citations into a new `references/theory.md`. This needs a spec §5.2 "References" update, a D-row, and the version rule in AGENTS.md. D23 records the no-answers stance as "cited to Aristotle": confirm that the citation may move to theory.md while the label stays in SKILL.md.
2. Cutting the citations instead (saving 286), with no theory.md. This would remove the provenance the owner asked for in D19–D23, so it is not recommended.
3. O1–O3: hold them until a multi-turn elenchus probe exists.
