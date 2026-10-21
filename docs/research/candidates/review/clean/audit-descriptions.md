# Description clutter audit: dialectic-skills `next` @ 0d5a949 (main @ eb7ab54)

Independent auditor, read-only. The frozen tree is unchanged (`git status --porcelain` is empty). I checked the rewrites in a `cp -r` copy: with the plugin bumped to 1.3.1, `tools/package.py`, `--check` and `unittest` (19 tests, 1 skipped) all pass. Tokens were counted with tiktoken o200k_base and cl100k_base. Characters are Python `len` of the parsed value, the count `package.py` caps at 1,024.

## Verdict

The concern is valid. Five descriptions are within 10 characters of the cap and six within 54. The cap has already blocked fixes the probes called for: warrant's S1 "fallacy" trigger, a brainstorm pointer to conjecture and warrant, and the Part O leaks marked "not fixed: within 10 characters of the cap".

Only 6 phrase groups have before/after probe evidence that they are needed. The rest is lineage, output detail and sibling pointers that no probe has ever removed to test.

The rewrites below keep every evidenced phrase. They save 1,657 characters and 385 o200k tokens (−20%) and leave at least 128 characters of headroom in every description. dia-confirm stays unchanged (justified). dia-negative stays the longest (896 characters), also justified, because most of its trigger text is evidenced. The decision log ends at D35; there is no D36.

## 1. Size

| skill | chars | headroom | o200k | cl100k |
|---|---|---|---|---|
| brainstorm | 1,014 | 10 | 230 | 228 |
| confirm | 447 | 577 | 88 | 89 |
| conjecture | 1,020 | 4 | 238 | 239 |
| counterplan | 1,019 | 5 | 223 | 225 |
| elenchus | 970 | 54 | 227 | 226 |
| iterate | 582 | 442 | 124 | 126 |
| negative | 1,009 | 15 | 221 | 222 |
| reductio | 1,001 | 23 | 219 | 223 |
| refine | 695 | 329 | 140 | 140 |
| warrant | 1,015 | 9 | 214 | 217 |
| **ten @0d5a949** | **8,772** | | **1,924** | **1,935** |
| seven @eb7ab54 | 5,567 | | 1,219 | 1,225 |

These figures match D35 (1,922 at b30344d; 1,219 at eb7ab54). The seven grew from 4,770 characters at the first build (5851c17) to 5,567 at main (+17%).

## 2. Anatomy (characters)

(e) is gate and scope rules, plus brainstorm's "Never implements".

| skill | a label | b does | c triggers | d excl./pointers | e | d % | siblings in (d) |
|---|---|---|---|---|---|---|---|
| brainstorm | 98 | 179 | 266 | 441 | 26 | 43 | 2 |
| confirm | 0 | 109 | 122 | 0 | 214 | 0 | 0 |
| conjecture | 69 | 383 | 189 | 376 | 0 | 36 | 6 |
| counterplan | 163 | 216 | 192 | 445 | 0 | 43 | 4 |
| elenchus | 62 | 370 | 376 | 159 | 0 | 16 | 1 |
| iterate | 0 | 277 | 185 | 47 | 70 | 8 | 1 |
| negative | 117 | 456 | 273 | 160 | 0 | 15 | 2 |
| reductio | 44 | 351 | 266 | 337 | 0 | 33 | 4 |
| refine | 0 | 254 | 306 | 51 | 81 | 7 | 1 |
| warrant | 79 | 432 | 229 | 272 | 0 | 26 | 4 |
| total | 632 | 3,027 | 2,404 | 2,288 | 391 | 26 | 25 edges |

The biggest part is (b), and much of it is output detail a router cannot use. Examples: "ends with a record" (6×), --target, "labelled reconstructed", iterate's stop list.

(d) growth, measured with a clause heuristic (2,204 at head against 2,288 by hand):

- All descriptions: 723 at the first build → 1,003 at main → 2,155 at b30344d → 2,204.
- brainstorm: 174 → 271 → 297 → 396 → 441 (c0ccd3d, f676e42, 0caa83f, b30344d).
- reductio: 191 → 336 (b30344d).
- elenchus: 122 → 159; negative: 138 → 159.
- counterplan: 328 → 367; conjecture: 365 → 375 (283f6fa).

## 3. History and evidence

Number of distinct versions: brainstorm 5, negative 5, elenchus 3, iterate 3, reductio 3, refine 2, confirm (formerly intent) 2, conjecture 2, counterplan 2, warrant 1.

Marks used:

- **E**: needed, with before/after probe evidence.
- **C**: present in passing cells but never ablated.
- **N**: added without probe evidence (review, fidelity or first build).
- **R**: redundant.

The complete E list:

1. **Socratic deferral (Part B, 1/6 → 6/6, p≈0.015).** Three halves changed together:
   - elenchus: "A request for Socratic dialogue … comes here even when it arrives with a product or plan idea"
   - elenchus: "or when the user asks to brainstorm"
   - brainstorm: "or when the user asks for Socratic dialogue or the Socratic method without asking to brainstorm"
2. **brainstorm make/write clause (D34; P5 owner ChatGPT 1.2.0 → 1.2.1; Part N kept every positive).** Changed jointly: "asks to think an idea through with questions" and "Not for … a request to make or write something (a script, code, a text), even one naming an idea".
3. **negative narrowing (Part F → G; Codex false loads 6/10 → 0/15, p≈0.001).** Changed jointly: "what is this claim or policy really for", "where does this claim fail its own standard" and "Not for what code, a command or a setting does, or a general review".
4. **counterplan claim-level exclusion (Part O; Codex claim-level devil's advocate 2/2 → 0/2, n=2).** Changed jointly: "Use only when asked for … on a plan or decision" and "Not for a devil's advocate on a claim or question …; answer directly".
5. **Gates of confirm and iterate (D33, Parts L and M).**
6. **"Socratic" in the brainstorm and elenchus labels.** This one is an inference from Part B and D30, not an ablation.

No D35 pointer has a before/after: the var arms always contained it, and base lacked the target skill. Part O shows some pointers not working:

- conjecture's "(dia-elenchus)": the game-definition cell still went to conjecture on Codex (2/2).
- conjecture's "(dia-negative)": the refund cell still went to conjecture on Claude (2/3).
- warrant's "(dia-reductio)": the deductive cell went to no skill on Claude in every arm (0/3).

## 4. Clutter

**Mutual pointers.** 9 of the 25 edges form mutual pairs, each stating one border twice:

- brainstorm↔elenchus, brainstorm↔counterplan
- conjecture↔counterplan, conjecture↔reductio, conjecture↔warrant
- counterplan↔warrant, iterate↔refine, negative↔reductio, reductio↔warrant

The router sees all ten descriptions, and the receiving skill's trigger already claims the request. Only brainstorm↔elenchus has evidence that both halves are needed (Part B).

**Self-contradiction.** conjecture sends "to poke holes or stress-test" to dia-brainstorm, but its own design cell 11 ("Poke holes in my claim that every microservice …") expects dia-conjecture. That cell fails on Claude (0/3).

**Parentheses.** None is nested more than one level deep. But conjecture's 9 parentheses, including a semicolon list inside a parenthesis inside a five-item list, read as nested.

**Example lists.** refine has 6 paraphrases of one request, yet Part J shows natural-language loads on Claude of only 1/9. elenchus repeats "socratic dialogue" and "elenchus" right after the same trigger words.

**Router-irrelevant jargon:**

- conjecture: "(Rules 1-4)", "monster-barring", "each with its check", "a repair Lakatos allows"
- warrant: "labelled reconstructed", "each tagged with the part it tests", "ask mode … slot by slot"
- negative, reductio: "--target"
- iterate: "(none named, or all refuted)"

**Lineage that belongs in the body:** "Mason (1969) in the Churchman lineage", "Paul's six question types", "Plato's Socratic dialogues", and negative's double "Adorno's". The bodies already carry all of these (checked by grep). elenchus's "(this skill's addition)" is not in its body, so it stays (D21).

**Patch-like wording:**

- brainstorm grafts "or when the user asks for Socratic dialogue …" onto a "For Plato's strict dialogue (…)" sentence, so one sentence carries two conditions.
- brainstorm's "Never implements anything" was made redundant by E2. It was present when ChatGPT loaded the skill at 1.2.0.
- counterplan's "is X healthy?" echoes the fasting probe.
- conjecture's "(not a policy to adopt)" echoes the Friday cell.
- refine has "or do a task the dia-refine way".

## 5. Consistency

- **Part order.** Most descriptions run label → does → Use when → pointers. counterplan puts a fidelity clause first. iterate and refine embed the pointer in the gate.
- **Pointer forms.** Five are in use: "use X instead", "For …, use X", "for …, X", "(X)" and "belong to X".
- **"or the same in any language".** It sits inside the e.g. parenthesis in brainstorm and elenchus, and outside it in the other six that use triggers. It is absent from confirm and iterate, which is correct for name gates.
- **Gates.** confirm and refine say "starts with", iterate says "begins with". The explicit-name clause also differs: "explicitly selected or invoked by name" in confirm, "invoked explicitly by name (for example …)" in iterate, and none in refine.

## 6. Proposed house convention

1. **Order:** label → what it does (at most 2 sentences) → "Use when …, or the same in any language." → one "Not for …" sentence. Gate skills: does → "Use only when …" → gate negation → "Not for …".
2. **Label:** the method name a user would type, plus at most one honest qualifier where the skill departs from the original. Dates, rule and chapter numbers and lineage go in the body.
3. **Does:** only behaviour that separates the skill from its siblings (one question at a time, one pass, writes the opposing case, gives no advice). No template fields, flags or "ends with a record".
4. **Triggers:** method names plus at most 2 quoted plain phrases that do not repeat them. "or the same in any language" goes last, outside parentheses.
5. **Exclusions:** "Not for <request> (dia-x), <request> (dia-y), or <request>." State each border once, on the side probes show over-pulling, unless a probe shows both sides are needed.
6. **Budget:** target ≤ 900 characters, which keeps at least 124 free for a probe-driven fix.
7. **Patches:** cite the probe cell in the spec decision. After an edit, reread the whole description and delete what the new phrase makes redundant.

## 7. Rewrites (proposals; savings in characters / o200k / cl100k)

Totals: 8,772 → 7,115 characters; 1,924 → 1,539 o200k; 1,935 → 1,550 cl100k. The seven at main come to 1,046 o200k (against 1,219).

**Regression gate.** All ten share one listing, so ship them as one batch. Before shipping, re-run at n=3 on Claude and Codex:

- P6 and P7
- Parts B and C (the Socratic and plan cells)
- Parts G, M and N
- all of Part O, both tables
- the per-skill cells listed below

If the batch is adopted, spec §5.4, §5.5, §5.6 and §5.10 need edits.

### dia-brainstorm (1,014 → 809; −205 / −47 / −45)

> Socratic brainstorming partner. Tests an idea with modern Socratic questions, one at a time, then draws out the user's own options before adding up to three, converges by criteria, and ends with an honest verdict and a brief with a next step. Use when the user asks to think an idea through with questions toward options and a plan, to poke holes in it, or to stress-test it before committing ("socratic brainstorm", "poke holes in this plan"), or the same in any language. Not for Socratic dialogue or the Socratic method asked for without brainstorming, options or a plan, or Plato's strict what-is-X dialogue (dia-elenchus); a counterplan or devil's advocate on a plan (dia-counterplan); factual or how-to requests; or a request to make or write something (a script, code, a text), even one naming an idea.

- **Keeps:** E1 (reworded into the "Not for" form); E2 verbatim; E6; C: the two quoted phrases (P7, Part N) and the counterplan pointer.
- **Drops:** "Paul's six question types" (N, in the body); "question me about this idea" (N); the four-item Plato parenthesis (R, elenchus says it); "Never implements anything" (R).
- **Re-run:**
  - Part N, all 9 cells
  - Part M: "Brainstorm three names…" and the rate-limiting cell
  - Part O: s-poke-*, s-verify-ko, s-bs-*, the counterplan cells, and the boundary rows "Poke holes in my argument" and "…every microservice"
  - P5 noun phrase (owner, ChatGPT)
- **Owner option, now affordable:** "how well reasons support a conclusion (dia-warrant)". Brainstorm over-pulls that request (Part O, 3/3).

### dia-elenchus (970 → 825; −145 / −36 / −37)

> Socratic dialogue (elenchus) as in Plato. Asks "what is X?" about the concept an idea stands on, gets the user's agreement to premises one short question at a time, and shows where they contradict the definition so the user revises it (each revision is kept as the user's new idea, this skill's addition). Usually ends in aporia; gives no advice or ideas of its own. Use when the user asks for the Socratic method, Socratic dialogue or elenchus, or to test whether they really know what they mean ("what do I even mean by X", "make me define it first"), or the same in any language. A request for Socratic dialogue or the Socratic method comes here even when it arrives with a product or plan idea. Not for questioning toward options and a plan or a request to brainstorm (dia-brainstorm), or for factual or how-to questions.

- **Keeps:** E1, both halves; E6; the D21 label; C: the two quoted phrases (P7 en, Part O s-el-fair).
- **Drops:** the aporia gloss (N); the repeated example words (R).
- **Re-run:**
  - Part B Korean elenchus, n=6 (the critical cell)
  - P7 en; Part C plan cells
  - Part M closure cell; Part D Great Wall
  - Part O s-el-*; the "a game is any activity" boundary row

### dia-negative (1,009 → 896; −113 / −25 / −25)

> Internal critique (narrower than Adorno's immanent critique) adapted from his negative dialectics, in one pass. Takes a claim, concept, plan or policy, states its own standard, and shows with particular cases where what it claims and what it delivers come apart; names what it leaves out and infers what it actually does; offers options and leaves the decision to the user, forcing no synthesis. Works on the user's claim, the assistant's earlier answer or a pasted text. Use when the user asks for negative dialectics, immanent critique, "what does this concept hide", "what is this claim or policy really for", "where does this claim fail its own standard", or wants the real purpose behind a stated goal examined, or the same in any language. Not for what code, a command or a setting does, a general review, logical consistency (dia-reductio) or a Socratic definition dialogue (dia-elenchus).

- **Keeps:** E3 verbatim; the D19/D21 label; "infers", which carries D20; the §5.5 pointers.
- **Drops:** the second "Adorno's" (R); "as a checkable inference" (R); "with a recommendation", "ends with a record", "--target" (N).
- **Re-run:**
  - Part G in full (Codex 5 negatives and 3 positives at n=3; the Claude P7 cells, «내재적 비판», vacation)
  - Part O s-neg-policy and the refund row
  - counterplan design cell 10

### dia-reductio (1,001 → 825; −176 / −45 / −45)

> Strict reductio ad absurdum in one pass. States the thesis and every premise with its source, derives a strict contradiction (Q and not-Q) line by line, then lays out which premises could be given up and recommends one, leaving the decision to the user. Works on the user's claim, the assistant's earlier answer or a pasted text. Use when the user asks for reductio, proof by contradiction, indirect proof, "assume it's true and show where it breaks", "find the contradiction", or whether a position holds together or follows strictly from its premises, or the same in any language. Not for the gap between what a claim or plan promises and delivers, or its real purpose (dia-negative); how well reasons support a merely probable conclusion (dia-warrant); or counterexamples to an all, always or never claim (dia-conjecture).

- **Keeps (all C):** the triggers (P7, Parts D and O); "holds together or follows strictly" (D23, D35); the pointers to negative, warrant and conjecture.
- **Drops:** the elenchus pointer (N; no reductio/elenchus confusion recorded); "--target"; "ends with a record".
- **Re-run:**
  - Part D reductio cells
  - Part O s-red-* and the boundary rows (perfect number, syllogism, "every prime is odd")
  - conjecture design cells 6, 8, 14; warrant cell 5

### dia-refine (695 → 586; −109 / −26 / −26)

> Review the previous answer or a named draft once for factual errors, logical leaps, missing requirements and needless repetition, and return one integrated revision that fixes defects whose basis was confirmed and marks suspected ones. Use when the message starts with dia-refine, or when the user asks to review or recheck the previous answer or a draft, fix its factual errors and logical leaps, or give only the improved final version, or the same in any language. A passing mention of dia-refine mid-sentence is not an invocation. Not for repeated verification rounds (dia-iterate).

- **Keeps:** the first-word trigger and the passing-mention rule (P6, Part J; D24); the D27 wording; the natural-language triggers, merged (Codex routes them, Part M 3/3).
- **Drops:** duplicate paraphrases (R); "do a task the dia-refine way" (N); "checking in order" (body).
- **Re-run:**
  - P6
  - Part J: passing mention and the 3 natural-language cells
  - Part M: the no-name iterate cell
  - warrant cells 6 and 14 (never run)

### dia-iterate (582 → 470; −112 / −24 / −24)

> Improve an output through repeated rounds gated by external verification; each round fixes only defects that a verification method confirmed, until a stop condition is met. Use only when the user's message begins with dia-iterate, or when the skill is invoked explicitly by name (for example /dia:dia-iterate, $dia:dia-iterate, $dia-iterate or @dia-iterate). Without that marker do not activate, however close the request sounds. Not for single-pass review (dia-refine).

- **Keeps:** E5 verbatim; the invocation forms (D19).
- **Drops:** the five-item stop list (in the body under "Stopping conditions"). This also removes the D21 consistency burden.
- **Re-run:** P6; Part M iterate cells; Part K refine+iterate.

### dia-confirm (447; no change)

Every clause is either a gate (E5) or the cross-turn scope rule that exists only in the description. Optional: harmonize "starts/begins with" across the gate skills. Re-run: the Part M confirm cells, as a listing regression check.

### dia-warrant (1,015 → 846; −169 / −38 / −38)

> Toulmin's argument layout tested with Walton's critical questions, in one pass. Lays out the data, warrant and qualifier behind a merely probable conclusion, supplies the unstated warrant, asks the critical questions for its argument type and names the weakest link; never rules on whether the claim is true. Works on the user's argument, the assistant's earlier answer or a pasted text, or questions the user step by step. Use when the user asks how well reasons support a conclusion, for the unstated warrant behind an argument, for Toulmin or critical questions, or whether an expert, analogy or causal argument holds up, or the same in any language. Not for a strict contradiction or a deductive step (dia-reductio), counterexamples to an all, always or never claim (dia-conjecture), or assumptions under a plan or decision (dia-counterplan).

- **Keeps (C):** all triggers (Part O); "never rules on … true" (cell 10); ask mode, in plain words (w-ask-ko); the pointers in cells 5, 7 and 8.
- **Drops:** "backing … rebuttal", "labelled reconstructed", "each tagged…", "or finds none", "Ends with a record" (N); the refine pointer (N; cell 6 never run).
- **Owner option, now affordable:** S1, "or is a fallacy" (cell 11 is 0/5).
- **Re-run:** design cells 1–14 (6 and 14 for the first time); Part O warrant rows and the boundary rows.

### dia-conjecture (1,020 → 726; −294 / −68 / −68)

> Lakatos's proofs and refutations as a dialogue. Takes a strictly universal claim the user holds (all, every, always, never) about what is the case, not a policy to adopt; splits its argument into lemmas and raises one counterexample per message; the user rules on each and picks a repair (replace the lemma, or build it into the claim). Use when the user asks for proofs and refutations, Lakatos, counterexamples to their conjecture, rule or proof, or "does this hold in every case", or the same in any language. Not for plans, policies, decisions or ideas (dia-counterplan, dia-brainstorm), what a word means (dia-elenchus), finding Q and not-Q (dia-reductio), or how well reasons support a probable conclusion (dia-warrant).

- **Keeps:** "not a policy to adopt" (C, cell 16; whether it is needed is unmeasured); the triggers (C); four pointers (C).
- **Drops:** "(Rules 1-4)", "monster-barring", "each with its check", "Lakatos allows", "ends with a record" (N); "usually-true" (R); "to poke holes or stress-test" (contradicts cell 11); the negative pointer (cell 13 leaked with it, and conjecture is accepted there).
- **Re-run:** design cells 1–16 (11 may improve; watch 12, 13 and 16); Part O conjecture and boundary rows.

### dia-counterplan (1,019 → 685; −334 / −76 / −77)

> Dialectical inquiry after Mason, adapted for one assistant in one chat. Turns the key assumptions of a plan or recommendation into plausible contraries, writes the counterplan on the same data, and asks which assumptions from each side the user holds; picks no winner and leaves the synthesis to the user. Use only when asked for a counterplan or a devil's advocate on a plan or decision ("make the case for the opposite plan", "what if our key assumptions are wrong"), or the same in any language. Not for a devil's advocate on a claim or question ("is X true?", "is X healthy?"); answer directly. Not for questioning the user to poke holes in or stress-test an idea (dia-brainstorm).

- **Keeps:** E4 verbatim; the I-F8 one-model honesty; the brainstorm border, which absorbs "does not question the user".
- **Drops:** "(1969) in the Churchman lineage" (body); "ends with a record"; the pointers to conjecture, warrant and negative (C and R; each sibling states that border itself).
- **Re-run:**
  - design cells 1–10, with cell 3 as written (never run)
  - Codex n-da-claim at n≥3 (the evidenced cell); n-gtm
  - the "hidden assumptions" boundary row and the pass-2 N5 cell

## 8. Caveats

- n is 2–3 throughout. "C" means a phrase has never been tested by removing it, not that it is useless, so the regression gate is required.
- I ran no routing probes. Every rewrite is unprobed.
- Only the owner can check P5 (ChatGPT mobile), and it is the sole evidence for E2.
- Pointer drops change spec text. That decision is the owner's.
