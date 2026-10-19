# Token audit: dia-negative

Audit only. No skill file was changed. Tree: `d5e9efa`. Shipped copy `plugins/dia/skills/dia-negative/SKILL.md` is identical to the source.

## Method

- Units: each sentence or bullet of the SKILL.md body (lines 12–118, frontmatter excluded, because Claude Code injects the body without it) and of each reference. Table rows, headings and rule numbers are their own units.
- Tokens: tiktoken `cl100k_base`. Unit sums exclude joining whitespace (SKILL.md body as a whole: 2,412; unit sum: 2,392). Claude tokens ≈ 1.5 × cl100k (docs/token-cost.md).
- Classes: **A** instruction, **B** rationale, **C** provenance/fidelity label/citation, **D** example, **E** redundant (same file, or a file loaded with it), **F** meta (headings, pointers, structure). A mixed unit was split by sub-span (e.g. the parenthesis in Step 4's "What escapes").
- What loads together: on invocation SKILL.md; in the measured first turns, also `output-template.md` (token-cost.md: both measured dia-negative runs read it). `theory.md` loads only for method questions or doubt. So redundancy between SKILL.md and the template is real double cost, but the template is the reference the skill most needs to work without (P8; research README theme 5).
- Evidence used: spec §5.5 and D19–D23, docs/probes.md (P7 negative cells, P8, pushback Parts A and C), docs/research/dia-negative.md (F1–F13), review/dia-negative.md, review/diff, review/pass2, review/lowfix.

## Per-class totals (cl100k)

| File | A | B | C | D | E | F | Sum of units | File body |
|---|---|---|---|---|---|---|---|---|
| SKILL.md (body) | 1,807 (76%) | 25 | 128 | 89 | 179 | 164 | 2,392 | 2,412 |
| references/output-template.md | 452 (76%) | 0 | 0 | 0 | 115 | 30 | 597 | 624 |
| references/theory.md | 38 | 300 | 1,681 (80%) | 0 | 30 | 62 | 2,111 | 2,116 |

SKILL.md by section: intro (lines 12–16) 261, Parameters 200, Hard rules 691, Procedure 800, Targets 130, Follow-up turns 214, Pitfalls 115.
theory.md by section: §1 history 96, §2 core ideas 544, §3 adaptation 479, §4 objections 321, §5 reductio 93, Sources 496.

Reading: the SKILL.md body is three-quarters instruction. Purely informational text (B + C) is 153 tokens, 6% of the body; most of it is honest-method labels that D19/D21 require. The larger non-A share is E (179), mostly the Pitfalls list restating Hard rules. theory.md is almost all provenance, but it does not load per invocation.

## SKILL.md: non-A units and verdicts

Line numbers refer to `skills/dia-negative/SKILL.md` at `d5e9efa`. "LB" = load-bearing.

| ID | Unit (line) | Class | Tok | LB? | Reason | Proposal |
|---|---|---|---|---|---|---|
| K1 | L14 "To think is to identify: to put a particular thing under a concept." + "The thing never goes into its concept without a remainder." | C | 26 | weak | Paraphrase of ND p. 5 (research A1). The term "remainder" is defined again where rules use it (Rule 7 "what it still does not capture", Step 4 "What escapes", Step 6). Already in theory.md §2 (Identity thinking, The nonidentical). | **shorten** L14 to: `No concept captures its object without a remainder.` (9 tok) |
| K1 | L14 "Critique works by pointing out specific contradictions … and it does not end in a reconciling synthesis." | E | 39 | no | Restates Rules 1, 2, 5 and 7 in one sentence; theory.md §2 has the SEP source sentence. | **cut** (part of K1; K1 total saving 56) |
| K2 | L16 "…not Adorno's own procedure; he held that his philosophy could not be reduced to a set of steps." | C | 34 | label yes, clause no | "Practical adaptation, not Adorno's own procedure" is the honest label for the step procedure (research A15). The reason clause is attribution; theory.md §3 carries it with its citation ("Adorno resisted summary … (SEP)"). | **shorten** to `…not Adorno's own procedure.` (saves 15) |
| — | L16 "It runs internal critique: the standard is what the target itself states." | C | 14 | yes | D19/D21 label; also needed for method questions when theory.md cannot be opened (P8). | keep |
| K8 | L16 "Immanent critique, in Adorno and in later accounts such as Jaeggi's and Stahl's, goes further: …can change those norms." | C | 43 | yes (label), attribution partly | The boundary ("goes further … can change those norms") plus "This skill does not reconstruct such norms" keeps the model from reconstructing implicit norms against Rule 1. The scholar names are citation; theory.md §4 has them with sources. The text is the diff review's D21 replacement, and pass2 N4 offered dropping "Jaeggi's and" as an alternative fix. | **owner decision**: optionally shorten the head to `Adorno's immanent critique goes further` (saves 16). Not in the recommended set: it is reviewed D21 text, and crediting "can change those norms" to Adorno alone is slightly stronger than SEP §7.2 (which cites Jaeggi). |
| — | L16 theory/template pointers, read conditions, "If you cannot open it, follow the order of Steps 1–8." | F/A | 91 | yes | Read conditions; the template fallback is D20 (review M3, P8). Merging the two theory sentences saves only 2 tokens. | keep |
| — | L25 "; the value is `claude` on every assistant" | A | 10 | yes | D14; stops renaming the value on Codex/ChatGPT. | keep |
| — | L29 "so the user can correct it" | B | 6 | yes | Tells the model why the inferred target goes in the first line. | keep |
| — | L33 example `("this is unfair" when it never claimed fairness)` | D | 13 | yes | The only concrete case of an outside value; Rule 1 is the core of the skill (research F1). | keep |
| K4 | L35 "That C can be read two ways is not a finding by itself, because under one of the readings there may be no gap at all." | E+B | 28 | no | The next sentence states the rule ("count a finding only where the gap is strict *within* a single reading"); template L11 repeats "Ambiguity alone is not a finding." | **shorten** to `Ambiguity alone is not a finding.` (saves 19) |
| — | L37 `"It's more complex than that" negates nothing in particular and is not allowed.` | D | 17 | yes | Concrete negative example for Rule 5; the Part C pushback runs named an abstract negation (Rule 5) as the real defect of a first-pass finding (probes.md:89). | keep |
| — | L38 Rule 6 vs L72 Step 5 (falsifier, inference label, evidence pattern) | E (overlap) | 75 | yes | The falsifier is the main guard against confabulated purposes (research F2, §6.1 risk 3; D23 tightened it). The hard rule is the short form; Step 5 the full one. | keep |
| — | L48 "Typical forms: \"X is Y\", … \"this measures Z\"." | D | 34 | yes | Helps locate C across target kinds; "merit-based company" sets up Step 5's "merit depends on measurement" example. A 3-form version would save about 14. | keep |
| K5 | L56 ", from the target's material first" | E | 7 | no | Rule 4 says the same ("Take D from the target's own material first"). | **cut** (saves 7) |
| — | L58 "(determinate negations)", L66 "(the nonidentical remainder)" | C | 9 | yes | Rule 9 allows Adorno's terms in parentheses; research F8 was dropped by the review and owner ruling (README:57). | keep |
| — | L74 `(for example "merit" depends on "measurement")` | D | 12 | yes | Only example of the optional constellation step; without it the step is abstract. | keep |
| — | L94 "; by design nothing is closed" | B | 6 | yes | Keeps "open" from being changed to a closing status after an option is chosen. | keep |
| — | L94 record fallback ("If the template cannot be read, the record is: …") | A (E with template) | 41 | yes | P8 / research F11 / D20. | keep |
| K6a | L98 "- **user:** follow the procedure as written." | F | 10 | no | Says nothing; the procedure is the default. | **cut** (saves 10) |
| K6b | L100 "Treat the text's purpose statements as its standard. Describe what the text does, not what its author intended." | E | 23 | no | Rule 1 ("stated goals"), Step 2 ("what it says it is for"; "stated purpose") and Rule 6 ("For texts and for your own answers, speak about what the claim or text does, not about a person's hidden motives") cover both. | **cut**; L100 becomes `- **text:** quote with location.` (saves 22) |
| — | L99 claude target ("not independent"; "do not defend … do not concede …") | A | 51 | yes | D19 self-examination guard (research F6). | keep |
| — | L108 "The user asks about the method: answer from the theory reference, briefly." | F | 17 | yes | Read pointer and length cue. | keep |
| K7 | L112 "- External critique: judging by a standard the target never adopted." | E | 13 | no | Restates Rule 1 and its example. | **cut** |
| — | L113 "- Abstract negation: \"everything is socially constructed\", \"nothing captures reality\"." | D (E) | 16 | yes | New examples, not repeated in Rule 5; abstract negation is the observed failure (probes.md:89). | keep |
| K7 | L114 "- Mind-reading: asserting a person's hidden motive instead of what the claim does." | E | 18 | no | Rule 6 sentence 2 and Step 5 "(as a function, not an intention)" say the same. | **cut** |
| K7 | L115 "- Closure: ending with a neat synthesis that hides its own remainder." | E | 14 | no | Restates Rule 7 almost word for word. | **cut** (K7 total saving 45) |
| — | L116 "- Jargon: Adorno's vocabulary standing in for an argument." | E | 14 | yes | Adds "standing in for an argument" to Rule 9; research §3.3 / §6.1 risk 4 (fluent but empty critique). | keep |
| — | L117 "- Dismissal by default: if C holds against the particulars, say so." | E | 17 | yes | Counterweight to manufactured gaps (research §6.1 risk 1); "first-pass strictness … is the case to watch" (probes.md:89). | keep |
| — | L118 "- Filling the template: an empty section is a result, not a gap to fill." | E | 19 | yes | Added on purpose against template pressure (research F5, D20). | keep |
| — | Headings, rule numbers, table header and separator | F | ~110 | yes | Structure the model navigates by ("Rules 2–4", "Step 5", "Steps 1–8"). | keep |

## References

### output-template.md (read on the typical first turn)

| ID | Unit (line) | Class | Tok | LB? | Reason | Proposal |
|---|---|---|---|---|---|---|
| K9 | L3 "Translate every heading … latest message. Keep the target's quotes in their original language. Use plain words, numbered items and short lines so it reads on a phone. Adorno's terms may appear in parentheses after the plain label, never instead of it." | A+E | 59 | partly | Rule 9 is in context whenever the template is (SKILL.md is always loaded first). The headings instruction and the phone layout are template-specific and stay. | **shorten** to `Translate every heading and label into the user's language (Rule 9). Use numbered items and short lines so it reads on a phone.` (saves 31) |
| — | L11 "Ambiguity alone is not a finding.", L28 conditional definition, L30 no-findings line, L40 "With no strict finding: …", L49 "(With no strict finding: the tested particulars.)" | E | 84 | yes | They repeat SKILL.md, but they sit in the slot the model fills; they are the D20/D21 fixes against template pressure (research F5; diff review finding 3). | keep |
| — | Remaining fields and placeholders | A/F | ~480 | yes | The layout itself. | keep |

### theory.md (loaded only for method questions or doubt; no per-invocation cost)

| ID | Unit (line) | Class | Tok | LB? | Reason | Proposal |
|---|---|---|---|---|---|---|
| K10 | L3 "Read this when the user asks about the method, or when you are unsure …" | E | 31 | no | The same read condition is in SKILL.md L16, which is always loaded before this file. | **cut** (saves 31 only when the file is read) |
| — | L3 translation note ("page references … Ashton translation") | C | 38 | yes | Makes the ND page numbers and quotations checkable (lowfix M5). | keep |
| — | §1 history (L7) | C | 96 | yes (user questions) | "Where does this come from" is a likely method question; it is the Preface citation the owner had fixed (D23). | keep |
| — | §2 core ideas (L11–27) | C, B | 544 | yes | Lets the model answer method questions and judge "is this finding determinate / is this standard the target's own"; the B sentences tie concepts to Rule 1, the "depends on" step and Step 5. | keep |
| — | §3 Kept / Changed (L31–37) | C | 479 | yes | The honest-label store: strictness vs exaggeration (F3), counterexamples vs models (F9), Popperian falsifier (F2), options and recommendation. D23 put these here; cutting needs an owner decision. | keep |
| — | §4 objections (L41–43) | B, C | 321 | yes | Habermas/Rosen/Jaeggi–Stahl answers; L43 repeats the internal-vs-immanent label (D21: "theory.md says the same"). | keep |
| — | §5 relation to reductio (L47) | B, A | 93 | yes | Scope boundary with dia-reductio for "which skill" questions; one A sentence (a reductio may serve inside a finding). | keep |
| — | Sources (L51–60) | C | 496 | yes | Citations the user may ask for; every entry is used in the body. | keep |

theory.md is the destination for moved provenance, and the provenance proposed for removal from SKILL.md (K1, K2, K8) is already there. Nothing needs to be added to it.

## Recommended set and saving

| ID | Change | cl100k saved per invocation |
|---|---|---|
| K1 | L14 → `No concept captures its object without a remainder.` | 56 |
| K2 | L16 drop "; he held that his philosophy could not be reduced to a set of steps" | 15 |
| K4 | L35 → `Ambiguity alone is not a finding.` | 19 |
| K5 | L56 drop ", from the target's material first" | 7 |
| K6a+b | Targets: drop the `user` bullet and the two `text` sentences | 32 |
| K7 | Pitfalls: drop External critique, Mind-reading, Closure | 45 |
| **SKILL.md** | body 2,412 → 2,238 (applied together and measured: 174) | **174** (≈ 260 Claude tokens, 7.2%) |
| K9 | output-template.md L3 shortened | 31 (whenever the template is read; that is the typical first turn) |
| **Typical first turn** | SKILL.md + template | **≈ 205 cl100k ≈ 310 Claude tokens** (6.8% of 3,036) |
| K10 | theory.md L3 read condition | 31, only when theory.md is read |
| K8 (owner) | L16 "Adorno's immanent critique goes further" | +16 if approved |

Applying all SKILL.md items, K8 included, measured 2,412 → 2,222 (190 saved). Any edit to a skill file falls under AGENTS.md's version rule (pre-release exception: stays 0.1.0 / 1.0.0). The description is unchanged, so no P7 re-run is required by L7.

## Risks and how to catch them

| ID | What could change | Probe that would catch it |
|---|---|---|
| K1 | Less framing for the "What escapes" line. A method question answered while theory.md is unreadable has only the L16 labels to work from. | P8 (`--tools Skill`) with a follow-up "what method is this?"; check that the answer still says practical adaptation + internal critique. Compare "What escapes" lines in the P7 negative cells (ko/en, n=2) before and after. |
| K2 | A "why is it in steps?" question without theory.md loses the reason; the label stays. | Same P8 method follow-up. |
| K4 | The model might report an ambiguity as a finding. Unit 35 and template L11 still forbid it. | New cell (none exists): an ambiguous claim ("our hiring is fair"); pass if the ambiguity gets one line and findings are per reading. |
| K5 | None expected (Rule 4 unchanged). | — |
| K6 | For `--target=text`, author-intent talk or an outside purpose taken as the standard. Rule 1, Step 2, Rule 6 and Step 5 still cover both. | A `--target=text` run on a mission statement; pass if every standard is quoted from the text and the function is worded as what the text does. No current probe covers `text`. |
| K7 | Pitfalls act as a last-read checklist; dropping three may weaken the final self-check on outside standards, motive claims or a closing synthesis. The four strictness-related pitfalls stay. | P7 negative cells (en "Do an immanent critique …", the Korean "immanent critique" cell) with output review: no outside value, no motive, no master definition without a remainder. Medium-low risk. |
| K9 | None expected: Rule 9 is always in context with the template. | P7 Korean cell: headings translated, quotes in the original. |
| K10 | None. | — |

## Not recommended (considered and rejected)

- **Move "Follow-up turns" (214) to a reference.** It would save the most, but the dispute rule is the D22 pushback guard (probes Parts A and C); on a surface where references cannot be opened (P8) a bare objection would again strip findings.
- **Move the Parameters table (200) or the record fallback (41).** The first line of every run states the target. The record fallback exists because references were unreadable in headless runs (research F11, README theme 5).
- **Fold Rule 6 into Step 5, or Rule 2 into Step 4.** Rules are the short binding form and the steps the full form. The falsifier and strictness are the skill's two main guards against invented findings and purposes (research F2, §6.1 risks 1–3).
- **Cut the template's repeated no-findings and conditional lines.** They are the in-slot fixes against template pressure (D20/D21).
- **Cut or move any honest label** (L16 "practical adaptation", "internal critique", the immanent boundary; Rule 4 "your own recall is never verified"; theory.md §3). They are required by D19–D23; only the attribution clauses (K2, optionally K8) are trimmed, and their sources stay in theory.md.
- **Trim theory.md beyond K10.** It does not load per invocation, and it is where method questions and the labels' sources live.

## What stays in SKILL.md and why

- Every A unit (1,807): rules, steps, targets, follow-ups, fallbacks.
- The L16 labels and read conditions: honest labels must survive unreadable references (spec §7.1, P8).
- The examples the model copies or uses as boundaries (Rule 1 fairness, Rule 5 "more complex", Step 1 forms, the "merit/measurement" constellation, abstract-negation pitfall).
- The four pitfalls about manufactured or empty findings (Abstract negation, Jargon, Dismissal by default, Filling the template). First-pass strictness is the open risk (research README:56).
