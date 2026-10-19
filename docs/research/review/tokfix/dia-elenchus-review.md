Verdict: PASS

Scope: `git diff d135f8e 75d7ac1 -- skills/dia-elenchus` and the dia-elenchus parts of docs/spec.md (D24, §5 intro, §5.2). Line numbers are for the tree at 75d7ac1 unless marked "old" (= `git show d135f8e:<path>`).

## Checks run

- `python3 tools/package.py --check`: exit 0, "ok dia-elenchus" (all seven ok). `diff -r skills/dia-elenchus plugins/dia/skills/dia-elenchus` shows no differences.
- `python3 -m unittest discover -s tests`: 13 tests, OK (skipped=1: the PyYAML frontmatter test. The frontmatter and openai.yaml are unchanged in this diff).
- SKILL.md is 113 lines; no Hangul, product names or new tool use.
- Token counts, re-measured with tiktoken cl100k_base: SKILL.md body 2,699 → 2,445, whole file 2,992 → 2,738, patterns 1,010 → 905, record 532 → 394, theory.md 1,156 (new). These match the implementer's table to within 1 token.
- Citations fetched: Perseus Theaetetus 157c ("claim none of them as mine … merely acting as a midwife … giving you a taste of each of the philosophical theories") supports "the Theaetetus midwife, who offers others' theories". Perseus Laches 187e: Nicias is the speaker, and Laches is in vol. 8, 1999.01.0176, so the URL is right. IEP "Socrates" gives Aristotle's report that Socrates "asked questions without supplying an answer of his own" (IEP misprints the locus as "1836b6-8"; 183b is correct). All 11 theory.md URLs are character-identical to docs/research/dia-elenchus.md refs [2], [7], [8], [10], [13]–[16], [25], [40], [60].

## Check 1: behavior loss, unit by unit

Nothing that governs behavior was lost. Each removed unit is either a locus, an ancient example, scholarly explanation, or a duplicate of a rule still in SKILL.md:

- E1 (l.14): the D23 scope label survives as "instead of a virtue". The L3 label survives as "aids, not as the method". The anti-"question types" anchor is kept.
- E2 (l.23): the D19 "adds one thing the dialogues do not have" label and the D23 midwife departure ("stricter than the Theaetetus midwife, who offers others' theories") are kept. The "emended or dropped" correction (diff review, F-l.23) moved to theory.md §3, unchanged.
- E3 (l.27): the exhortation departure is kept: "(Socrates also exhorted; you never do)". The no-answers rule is kept in full: "Give no answers, advice, solutions or options".
- E4 (l.28): the "drop" label is kept: "Drop Socrates' irony".
- E5, E6, E8, E10, E11: only loci were cut (E6's phone point is in Rule 2, l.36). The E10 label, "stricter than Socrates, who sometimes worded the revision himself" (l.92), is intact.
- E7 (l.31): the D19 label is kept. See nit 3.
- E9 (l.70): the Scythians example was upstream 1.3.1 text, not a D-fix (upstream/…/socratic-elenchus/SKILL.md:70). "Too narrow" is still fully defined at l.70.
- P1: "Ask in the user's language" is covered by Rule 7 (l.41).
- P3: the dropped numbering sentence restated l.76. The D21 stability rule is at l.76, and the D22 rule "① definition, premises from ②" is at patterns l.24.
- P5: the dropped "<old> → <new>" naming is at l.92, which is the stricter copy.
- P6: the dropped "rewording is not a birth" is at l.94.
- R2: I compared the old record-template.md l.38-43 with SKILL.md l.100 clause by clause. All six criteria, including both D21/D22 tie-breaks, are in SKILL.md verbatim. The two template-only clauses ("Name the tests it passed", "Name which definitions fell before that") are kept at record l.38.
- R3: old "Mention it only if the user asks what's next" is covered by "After the dialogue (not Socratic, only on request)" (l.102-104).
- D23 elenchus items still present: paraphrase flag (l.61), shift in key words with no label (l.92), repeated examples → unrelated model definition with the Laches 192b tag (patterns l.14), study-mode hints (l.108), no-single-feature aporia (patterns l.55). The "cited to Aristotle" item moved to theory.md §2. See nit 2.

## Check 2: contradictions and dangling references

None found. "SKILL.md Step 6" (record l.38) exists and holds the criteria. "Step 4" and "Step 5" in patterns (l.24, l.42) still resolve. The "code block above" sentence was removed together with the code block (P4). The patterns contradiction template (l.28-31) now has the same quote-block form as the worked example at SKILL.md l.82-84. theory.md §1-3 match the labels in SKILL.md.

## Check 3: moved text

theory.md is linked at l.14 with a read condition: "read it only if the user asks about the sources or the method". This mirrors dia-reductio's theory.md condition (dia-reductio/SKILL.md:16) and spec §5.2 l.133. Nothing in theory.md is needed on a first turn or when references cannot be read: every label and rule it explains stays in SKILL.md. Only loci, the early-dialogue names, the Scythians example and the scholarly qualifications moved.

## Check 4: fidelity

All 21 moved loci (old SKILL.md and patterns l.22) are in theory.md l.7-24, unchanged.

## Check 5: recommended set vs applied

- All of E1–E11, P1–P6, R1–R3 and theory.md were applied. O1–O3 were not applied (pitfalls l.111 and l.113 and the six-step shape are unchanged). Nothing outside the set was applied.
- The P/R items belong to the recommended set: the audit's saving section (l.147) counts them under it, and its owner-decision list (l.160-164) names only theory.md, the cut-only alternative and O1–O3.
- One deviation: the E1 read condition says "the sources or the method" where the audit has "them". The implementer attributes this to the owner. spec §5.2 records the same wording, and it matches the dia-reductio convention, so I accept it.

## Findings

1. nit: references/record-template.md:3, R1. The template is still a fenced ```markdown block (l.5-34), and R1 removed the sentence that told the model not to print it that way.
   - The rule survives at SKILL.md:100, so nothing is lost when references can't be read. But at the end of a long dialogue, the template is the most recently read text, and it shows a code fence.
   - The dia-brainstorm audit kept the identical sentence in brief-template.md (token-audit/dia-brainstorm.md:75, "Keep"), so the two skills now treat the same rule differently.
   - Restoring it would go beyond the approved set, so this is the owner's call.
   - Optional replacement for l.3: `Lead with one plain line: the result, and the question the user takes away. Translate the headers into the user's language. Print plain Markdown, not a code block. Use only what the user said or agreed to. Keep an empty section as "none" rather than dropping it.` (about 8 tokens)

2. nit: docs/spec.md:69 (D24). The D23 row (l.68) still says the no-answers stance "is cited to Aristotle", and SKILL.md no longer carries that citation.
   - D24's "moves its dialogue loci and scholarly notes" covers the move only implicitly. The implementer's account (tokfix/dia-elenchus-applied.md:3, 11) says the owner approved it explicitly, but the spec does not record that approval.
   - Replacement in D24: `dia-elenchus moves its dialogue loci and scholarly notes to a new `references/theory.md` (read on request) and keeps the labels in the body.` → `dia-elenchus moves its dialogue loci and scholarly notes, including D23's Aristotle citation for the no-answers stance, to a new `references/theory.md` (read on request) and keeps the labels in the body.`

3. nit: SKILL.md:31, E7. The shortened label drops the hedge "by Nicias's account". That hedge came from the earlier diff review (review/diff/dia-elenchus.md finding 5).
   - Without its loci, the bare claim is still defensible from the Apology (38a, "the unexamined life"; research ref [37]), and theory.md:19 keeps the hedge.
   - No change required. If the owner wants the hedge kept in the body (+4 tokens): `- **Examine statements, not the person** (narrower than Socrates, who by Nicias's account also tested how people lived). A contradiction belongs to the statements; the user decides what to give up.`

4. nit, informational: theory.md is 1,156 cl100k tokens, not the audit's ~488 draft, because of the 11 source URLs.
   - The audit's claim that the move "does not raise the worst case" (token-audit/dia-elenchus.md:148) no longer holds: the all-files-read total is +659. The implementer reports this honestly (applied.md:45).
   - The cost applies only when the user asks about sources or the method. No change required.

No blocker or should-fix findings.
