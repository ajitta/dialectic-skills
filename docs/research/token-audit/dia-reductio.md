# Token audit: dia-reductio

Counted on `d5e9efa` (skill text as at `6882022`, D23). Read-only audit; nothing in `skills/` was edited. Counts use tiktoken `cl100k_base`; Claude tokens ≈ 1.5 × cl100k (`docs/token-cost.md`, n=2). Savings were checked by applying the recommended edits to a scratch copy and recounting each whole file.

## 1. What loads when

| File | cl100k | When it loads (docs/token-cost.md) |
|---|---|---|
| SKILL.md body (no frontmatter) | 2,882 | every invocation (injected) |
| references/output-template.md | 623 | read in the measured first turns ("read it before writing the first output") |
| references/theory.md | 2,034 | not read in any measured first turn; only when the method is asked about or a step is in doubt |

So the per-invocation cost is the body, plus the template on almost every run. Cutting theory.md text saves nothing on a typical run.

## 2. Per-class totals

Units are sentences or bullets (a line split where its sentences differ in class). Classes: A instruction, B rationale, C provenance/fidelity label or citation, D example, E redundant (restates text in the same file or in a file loaded with it), F meta (pointers, invocation forms). S counts headings, blank lines and `---`. It belongs to F but is shown on its own because it is not a candidate. Unit sums run 1–1.5% above the file counts because pieces are tokenized separately.

| Class | SKILL.md body | output-template.md | theory.md |
|---|---|---|---|
| A instruction | 2,137 (73%) | 473 (75%) | 160 (8%) |
| B rationale | 52 | 7 | 204 |
| C provenance / label / citation | 49 | 0 | 1,001 |
| D example | 274 | 38 | 360 |
| E redundant | 119 | 51 | 175 |
| F meta (pointers, invocation) | 130 | 0 | 39 |
| S structure (headings, blanks) | 161 | 64 | 125 |
| **Unit sum** (file count) | 2,922 (2,882) | 633 (623) | 2,064 (2,034) |

What sits in each non-A class of SKILL.md:
- B: R5 "Refuting a weaker reading is a strawman." (10); Step 2 L57 "That shows neither … found nothing;" (24); Step 5 L75 "This is the strongest result." (6); Step 5 L77 "so the real question is whether those [A] premises are true." (12).
- C: L59 intuitionistic-logic note (34); L81 own-scheme label (15).
- D: Rule 1 "all X are Y" contradicts "some X is not Y" (16); Step 5 L71 `e.g. "Lines 4 and 7 …"` (21); the worked example L83–96 (≈230; 222 as one span).
- E: L14 second sentence (21); R6 second sentence (16); Targets `user` bullet (10); Pitfalls L130, L131, L133, L134 (19 + 26 + 10 + 17).
- F: L16 reference pointers (≈84); L20 flag line (17); L29 "Natural-language equivalents …" (12); L126 "asks about the method" follow-up (17).

**Main finding.** SKILL.md contains very little purely informational text. History, attributions, scholarly sources and method lineage were already placed in theory.md, which typical runs do not open. The only provenance left in the body is two items: the intuitionistic note (L59) and the own-scheme label (L81). Both are recorded decisions (D23 and D22). The removable remainder is restated text and a few rationale clauses: about 110 cl100k (≈ 3.8% of the body).

## 3. Candidates

Line numbers refer to the current files. "LB" means load-bearing.

### SKILL.md (paid on every invocation)

| # | Unit | Class | cl100k | LB? Reason | Proposal | Risk / what would catch it |
|---|---|---|---|---|---|---|
| S1 | L14 "Then show the user which members of the set could go, recommend one, and let the user decide." | E | 21 | No. It restates Rules 6–7 and Steps 6–7, which come right after it in the same body | **cut** | Very low. The model might stop before the options; the worked example and Step 6 still require them. The pushback probe (probes Part A) and any reductio run would show missing options |
| S2 | L16 pointers: markdown links `[references/x.md](references/x.md)` | F | 7 | The paths are LB; the doubled link syntax is not | **shorten** to plain code paths: "Theory, history and the reasons behind the rules are in `references/theory.md`: read it when the user asks about the method (then answer briefly), or when you are unsure whether a step is strict. The output layout is in `references/output-template.md`; …" (rest unchanged) | Low. Same relative paths, so the Read target does not change. A failed Read would show in a headless run's Read paths |
| S8 | L126 "**The user asks about the method:** answer from the theory reference, briefly." | E/F | 17 | Partly. It repeats L16's read condition; only "briefly" is new | **cut**, with "briefly" folded into L16 as in S2 (S2 + S8 save 24 together) | Low. A follow-up method question still triggers the L16 read condition. No probe covers method questions |
| S3 | R5 "Refuting a weaker reading is a strawman." | B | 10 | No. The rule's instruction is the sentence before it, and Pitfall L133 says the same | **cut** | Very low. Charity behavior has no probe |
| S4 | R6 "A contradiction shows only that the thesis and the premises cannot all be true together." | E | 16 | No. It restates the bold rule title (and L14) | **cut**. The operative sentences ("Write 'the thesis is false' … only when …", "Otherwise present the choice") stay | Low. Over-claiming would show in the result line. No probe checks it; the worked example still says "internal" without "false" |
| S5 | L71 `e.g. "Lines 4 and 7: Q and not-Q. Depends on T, P1, P3 [A]."` | D/E | 22 net | Partly. The same format is in the worked example (L96) and template L30. The only unique part is marking [A] inside the depends-on set | **shorten**: replace the e.g. with "; mark each [A] member." | Low. On a run without the template (P8-style, references unreadable), the depends-on line could lose its [A] marks. No reductio cell in P8 catches it today (see §5) |
| S6 | L75 "This is the strongest result." | B | 6 | No. Step 4 already prefers fewer [A] premises, and the grade order follows from the definitions | **cut** | Negligible |
| S7 | L116 "- **user:** follow the procedure as written." | E | 10 | No. It carries no instruction | **cut** | Negligible. The same line exists in dia-negative (L98). There is no shared-block check, so the two files may differ |
| S9 | L133 pitfall "A strawman from testing the weak reading." | E | 10 | Weak. It is a checklist echo of R5 | keep if S3 is cut (keep one of the two) | — |
| S10 | L81 "The three grades are this skill's own scheme, not a standard classification." | C | 15 | Yes, as an honest label. D22 records it as part of the skill text, and the research (F10) wanted it said. It stops the assistant from presenting the grades as a standard taxonomy, even on a tool-less run where theory.md cannot be opened | **keep**. If the owner wants the 15 tokens back, move it to theory.md §3 (keeps it available, no owner ruling needed); do not cut | Moving it risks the grades being called standard on a tool-less run. No probe |
| S11 | L57 "That shows neither that the premises are consistent nor that they cannot decide T, only that this search found nothing;" | B | 24 | **Yes.** It is the only place that denies *independence* ("cannot decide T"). L112 and Pitfall L134 deny only consistency and truth. This was research F1, severity high | keep (a 10-token shortening is possible: "This shows neither consistency nor that the premises cannot decide T;" but the gain is not worth it) | — |
| S12 | L59 intuitionistic note | C+A | 53 | Yes. The model can say "relies on classical logic" correctly only if it knows the condition (T not a negation), and theory.md is not read on typical runs. D23 records this exact wording | keep (dropping "(see the theory reference)" would save 7 tokens and lose a pointer) | — |
| S13 | Worked example L83–96 | D | 222 | **Yes.** Research F6 ([20]: models do not use proof by contradiction without demonstrations); README theme 5 (fallback when references cannot be read); the diff review checked it line by line. The model copies it | keep, in SKILL.md (it must work when references are unreadable) | — |
| S14 | Pitfalls L130, L131, L134 | E | 62 | Yes, as a reread checklist. L134 was asked for by diff-review nit 7. L130 and L131 carry examples ("then society would collapse", "would lead to") that the rules lack | keep | — |
| S15 | Rule 1 example `"all X are Y" contradicts "some X is not Y"` and the label parenthetical | D/E | 16 + 25 | Yes. Review F4 called the example "the useful part". The parenthetical was diff-review finding 3, which closed the gap where an existence premise could pass as [L] | keep | — |
| S16 | Step 8 record field list (L108) | A (duplicates template L47–54) | ≈40 | Yes. It is the M5 fallback for runs that cannot open the template (probes.md P8 observation) | keep | — |
| S17 | Step 4 "the record says how the derivation was checked" | E | 9 | Yes. It ties the reread rule to the "Checked by" field, so the rule has a field that reads it | keep | — |

### output-template.md (read on almost every run, together with SKILL.md)

| # | Unit | Class | cl100k | LB? Reason | Proposal | Risk |
|---|---|---|---|---|---|---|
| O1 | L3 "Translate every heading and label into the language of the user's latest message. Keep the target's quotes in their original language." | E | 16 net | No. It restates Rule 8, which is always loaded with the template | **shorten** to "Translate headings and labels per Rule 8. Use numbered lines, …" | Low–medium. The template's English headings sit next to this line, so mixed-language output is the failure mode. P7's Korean cells (reply language) would catch it if the reply is inspected |
| O2 | L32 "(Direction "both": one Contradiction and Strength line per direction.)" | E | 14 | No. L27 already says "its own contradiction and strength below", and SKILL.md L79 says it too | **cut** | Low. A "both" run with only one strength line would show it. No probe runs the "both" direction |
| O3 | L18 "(a meaning the derivation relies on gets its own P-line)" | E | 12 | Yes, by request: pass-2 nit 3 made it match Step 3 | keep | — |
| O4 | L31 carried-grade phrasing in parentheses | D | 38 | Yes. It is the sentence the model copies for the "carried" result | keep | — |
| O5 | Slot value lists (evidence classes L17, result values L48, strength L50) | A (duplicate SKILL.md) | ≈60 | Yes. A template slot needs its allowed values | keep | — |

### theory.md (only when read; no saving on a typical run)

| # | Unit | Class | cl100k | LB? Reason | Proposal | Risk |
|---|---|---|---|---|---|---|
| T1 | §8 "Failure modes to watch" (L57–64) | E | 125 | No. All six items restate SKILL.md rules and pitfalls (Rules 1, 2, 4, 5, 6 and Pitfalls), which are always in context when theory.md is read | **cut**, and renumber §9 → §8 (no file refers to either number) | Very low |
| T2 | L17 "This skill allows only the first. A falsehood … reject it if they want." | E/B | 32 net | Partly. It is the bridge from Rescher's three kinds to Rule 1; the mechanics restate Rule 1 | **shorten** to "**This skill allows only the first** (SKILL.md Rule 1 says how a falsehood or implausibility is made strict)." | Very low |
| T3 | Sources (L72–84) | C | 435 | Yes. These are citations the user may ask about, and L3 promises "Sources are listed at the end". The diff reviews asked for the Duhem–Quine, Jowett and Aristotle entries | keep | — |
| T4 | §7 History, including *Apology* 27b–e and the "silence gives consent" caveat | C | 158 | Yes. L16 promises "history", the passage was corrected by D23, and a user may ask about it | keep | — |
| T5 | §9 hard cases, including the dialetheism line | D/C/A | 268 | Yes. The dialetheism line was kept by owner ruling (research README item 2). The Zeno bullet carries an [L]/[T]/[A] labelling rule | keep | — |
| T6 | §1–§6 (Rescher's kinds, logical form, Duhem–Quine, targets of reductio, diagonal proof, per impossibile) | B/C/D | ≈900 | Yes. This is what "answer from the theory reference" answers with, and §4 L43 and §6 L51 contain instructions found nowhere else (see §5) | keep | — |

## 4. Recommended set and saving

| Set | Edits | Saving, cl100k (whole-file recount) | ≈ Claude |
|---|---|---|---|
| SKILL.md, every invocation | S1, S2 + S8, S3, S4, S5, S6, S7 | **109** (3,136 → 3,027; body 2,882 → 2,773, 135 → 133 lines) | ≈ 165 |
| output-template.md, runs that read it (typical first turn) | O1, O2 | **30** (623 → 593) | ≈ 45 (plus about 2× again as a cache write, because every Read result is cache-written) |
| theory.md, runs that read it | T1, T2 | **157** (2,034 → 1,877) | ≈ 235, on those runs only |
| **Typical invocation** (body + template) | | **139** (3,759 → 3,620, −3.7%) | ≈ 210 |

None of these edits touches a D19–D23 label, the description, the frontmatter, the worked example, the result or strength vocabulary, or any no-reference fallback. No owner ruling is needed. Under AGENTS.md, applying them changes skill files, so it needs the version rule (0.1.0 may be kept before the first install).

## 5. What to keep, and gaps the audit found

Keep in SKILL.md, because the skill must work when references cannot be opened (spec §7.1; probes.md "worked from the SKILL.md body alone"):
- the worked example (S13);
- the Step 8 field list (S16);
- the Rule 1 contradictory/contrary example and label parenthetical (S15);
- the L59 classical-logic condition (S12);
- the L57 independence non-claim (S11);
- the own-scheme label (S10, an honest label under D22);
- the pitfalls checklist (S14).

Each one is either a recorded decision or the only copy of a behavior on the no-reference path.

Gaps found during the audit (not savings; for the owner):
- **Instructions that live only in theory.md:**
  - §4 L43: applying reductio to a rule or practice needs its stated aim written as a premise.
  - §6 L51: when the user is exploring consequences, say it is *per impossibile* and that no refutation is claimed.
  - Typical runs do not read theory.md, so both behaviors are not on the default path. If they matter, each needs a one-line rule in SKILL.md, which would add about 30 tokens.
- **No probe covers dia-reductio without references.** P8 runs only dia-refine and dia-iterate. S5 (the [A] marks in the depends-on line) and O1/O2 (template wording) could only be caught by a reductio run with `--tools Skill`, which is not in the probe list today. Suggested cell, if the set is applied:
  - a reductio prompt whose chain needs one [A] premise, run in two variants: `--tools Skill` (no Read), and with the "both" direction.
  - Check: the depends-on line marks [A], there is one strength line per direction, the record has all eight fields, and the reply is in the prompt's language.
- **Duplication shared with dia-negative.** S7 and S8 also appear byte-identical in dia-negative (L98, L108). No check enforces that they match, but whoever applies this audit should decide both skills together so the two do not drift.
- **Not measured:** how far each edit changes behavior. With the per-invocation saving at about 3.7%, a 10-run A/B is not justified on token grounds alone. Apply the set with the next behavior batch and let that batch's probes cover it.
