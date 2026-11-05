# Skill effect: each skill against no skill (2026-10-20)

Question (owner): how much does each skill change the result, compared with no skill and only the method's name in the request?

## Method

- **Arms.** S: plugin `dia` at `039e7ff` (D26), prompt `dia-<x>: <request>`. N: an empty plugin, the same `<request>`, which names the method in words ("Reductio ad absurdum on this claim: …", "Self-refine this draft once …", "Socratic elenchus: …"). S loaded its skill in 30/30 runs.
- **Runs.** Claude Code 2.1.303, claude-sonnet-5-5, headless, fresh `CLAUDE_CONFIG_DIR`, claude.ai connectors off, empty working directory, default tools (shell and web need approval, so they were denied). Ten tasks, n=3 per arm, 60 sessions. dia-intent ran with `--tools Skill,Read,Glob`. dia-elenchus (5 turns) and dia-brainstorm (6 turns) used scripted user turns.
- **Judge.** claude-opus, no plugin, fresh config, blind: skill names and the word "skill" redacted as `[x]` in both arms. (1) A 6-item checklist per skill, true/false, plus an overall score 1–10. (2) Pairwise S vs N on the matching replicate, judged twice with the order swapped; a pair counts for an arm only if both orders agree.
- A first judging pass was discarded: its redaction pattern also hit "dialectics" and "dialogue", which garbled N's texts more than S's (18 against 8 marks) and the judge penalised the marks. All figures below are from the corrected pass.

## Results

| Task | Checklist S / N (of 6) | Overall S / N | Pairwise, both orders agree (S–N–split) | Cost per session S / N |
|---|---|---|---|---|
| dia-reductio, remote-work claim | 6.0 / 1.7 | 8.3 / 5.3 | 3–0–0 | $0.099 / $0.030 |
| dia-reductio, "rules with exceptions" | 5.7 / 0.0 | 7.7 / 3.7 | 3–0–0 | $0.131 / $0.033 |
| dia-intent, churn report | 5.7 / 4.0 | 8.0 / 5.7 | 3–0–0 | $0.076 / $0.030 |
| dia-intent, production delete | 4.7 / 4.7 | 7.0 / 6.7 | 2–0–1 | $0.074 / $0.024 |
| dia-negative, unlimited vacation | 5.7 / 2.3 | 7.3 / 5.7 | 3–0–0 | $0.108 / $0.036 |
| dia-negative, meritocracy | 5.0 / 2.0 | 6.3 / 5.7 | 0–0–3 | $0.092 / $0.036 |
| dia-brainstorm, coffee shop (6 turns) | 5.3 / 3.7 | 7.7 / 5.3 | 2–0–1 | $0.816 / $0.617 |
| dia-iterate, draft | 5.3 / 4.7 | 7.0 / 6.0 | 1–1–1 | $0.105 / $0.033 |
| dia-elenchus, courage (5 turns) | 3.0 / 3.7 | 5.7 / 5.7 | 1–2–0 | $0.595 / $0.433 |
| dia-refine, draft | 5.3 / 4.3 | 7.0 / 7.0 | 0–3–0 | $0.098 / $0.029 |
| **All** | | | **21–6–3** (votes 42–18) | |

Single-turn sessions cost about 3× more with the skill (the skill text plus longer, structured answers) and took 2–5× longer; the multi-turn sessions cost about 1.3–1.4× more.

## Per skill

- **dia-reductio: large effect.** Without the skill no run labelled premises by source, said what the contradiction depends on, or left the choice of premise to the user; on the rules claim, two of three no-skill runs called it simply false and the third "self-refuting", by applying the rule to itself. With the skill, every run did all three (checklist items 1, 3, 5: S 6/6, 5/6, 6/6; N 0/6, 1/6, 0/6).
- **dia-intent: large on the open-ended task, small on the risky one.** Without the skill the model already holds before deleting production data and names a backup; the skill adds the goal and done-condition, checked facts against assumptions, and a shorter review.
- **dia-negative: large on the checklist, mixed in pairwise.** The skill's runs keep to the claim's own standard, give a falsifier and leave the decision to the user (S 6/6 on each, N 0/6). But the no-skill runs more often showed a strict gap with a particular case (N 5/6, S 2/6). On the meritocracy claim the judge split, describing the no-skill runs as "closer to negative dialectics as Adorno practiced it" and the skill's runs as "more careful, but template-bound". This matches the skill's own label (internal critique, narrower than Adorno).
- **dia-brainstorm: clear effect.** One question per turn (S 3/3, N 0/3) and phone-length turns (S 2/3, N 0/3) held only with the skill.
- **dia-iterate: no net effect here.** With the shell denied, the skill's runs would not count their own arithmetic as verification and left "20%" unedited (by design: own re-derivation is not an outside signal); the judge called that over-cautious in some pairs and rule-following in others.
- **dia-elenchus: no effect measured, and the cell is weak.** The scripted user never answers the assistant's test questions, so no contradiction can be drawn from agreed premises (both arms 0/3 on that item). The no-skill runs used sharper classical counterexamples (the Laches physician); the skill's runs kept a more accurate record of what was agreed.
- **dia-refine: the no-skill runs won every pair.** Both arms found the same errors. The skill's revision left the claim it suspected was false ("Python 3.13 removed the GIL by default") and the unsourced superlative verbatim, because its rule keeps unverified items as drafted; the no-skill revision rewrote them. The judge: "leaves claims it knows are likely false in the revision, which makes the self-refine pass mostly useless."

## Re-run after D27, and with an adaptive respondent

Same harness and judge. dia-refine and dia-iterate: S re-run at `562f336`, judged against the same N runs. dia-elenchus and dia-brainstorm: the user is played by claude-sonnet (no plugin) with a persona that answers the questions (a person who thinks courage is "not being afraid"; a would-be coffee-shop owner with $80k savings, 20 informal student answers, a chain two blocks away), up to 8–9 turns.

| Task | Checklist S / N | Overall S / N | Pairwise S–N–split | Before |
|---|---|---|---|---|
| dia-refine, draft (D27) | 5.7 / 4.7 | 8.0 / 7.0 | 1–0–2 | 0–3–0 |
| dia-iterate, draft (D27) | 5.3 / 4.7 | 7.0 / 6.3 | 2–1–0 | 1–1–1 |
| dia-elenchus, adaptive respondent | 5.7 / 5.3 | 8.0 / 8.0 | 2–1–0 | 1–2–0 (scripted) |
| dia-brainstorm, adaptive respondent | 5.3 / 2.7 | 7.0 / 5.7 | 2–1–0 | 2–0–1 (scripted) |

- dia-refine: the revision now carries the suspected GIL correction, marked; the lost pairs are gone.
- dia-elenchus: with a respondent who answers, the judge credited the skill's runs for quoting the respondent's own words and for setting out the agreed premises that cannot all stand (①②③); the no-skill run that won built a longer Laches-style series of counterexamples.
- dia-brainstorm: the no-skill runs asked several questions at once ("front-loads seven questions"); the one no-skill win "pushed harder" and drew out kill criteria.
- Cost per adaptive session: dia-elenchus $1.36 / $1.00, dia-brainstorm $1.01 / $0.81 (S / N, generator only).

## Limits

- n=3 per cell; one judge model, from the same family as the generator.
- The checklist items come from each skill's own design goals, so they favour S; the pairwise question ("as a rigorous practitioner of the named method would") is the more neutral measure.
- Headless runs could not use the shell or the web, which removes dia-iterate's normal verification path and dia-refine's tool checks.
- Scripted multi-turn users do not react to the questions. The re-run above uses an adaptive simulated respondent for dia-elenchus and dia-brainstorm, but it is still one model playing a persona, not a person.
- Raw sessions and judgments: `~/work/dia-review/eval/` on the build VM (`out/`, `judge2/`, `run.py`, `judge.py`).

## Seeded keys and source fidelity: dia-warrant, dia-counterplan, dia-conjecture (2026-11-05, plugin 2.3.0)

Question (owner): how to evaluate the skills that were never compared with no skill, at the least run count that still decides.

### Method

- **Arms.** As above: S is plugin `dia` 2.3.0 with `dia-<x>` first; N is an empty plugin with the same request naming the method in words (Toulmin and Walton; Mason's dialectical inquiry; Lakatos's proofs and refutations).
- **Runs.** Claude Code 2.1.314, claude-opus-5-5 at `--effort low` (owner), generator and judge; fresh `CLAUDE_CONFIG_DIR`, connectors off, empty working directory, tools `Skill,Read,Glob`. dia-conjecture: two scripted user turns.
- **Items, fixed before the runs.** Core: seeded defects with an answer key. Fidelity: from the primary method, not from the skill text. Precision (round 2): a distractor that should not be flagged. E: every outside fact is marked by its basis. K as in A/B rule 5. One blind judge pass per run (skill names redacted), true/false with a quote.
- **Minimum level.** Pilot (dia-warrant): each output judged twice, 18/18 items agreed; one later re-judge flipped one item, so judge noise is about one item per run. Rule: n=1 per arm, a second run when the S–N gap is two items or less or a K appears.
- **Rounds.** Round 1: one task per skill, n=2 per arm. Round 2: harder seeds with a distractor (annual-billing churn; a Japan launch whose waitlist is one viral spike; a true conjecture whose proof has a false lemma, so the right case is local only), n=1 per arm. The round-2 gaps were one or two items, but the second run was not made: pooled with round 1 every skill had three runs per arm on the deciding items, all in the same direction (AGENTS.md: stop once the answer is clear).
- Two harness defects were fixed during round 1: dia-conjecture's scripted turn accepted a case before one was raised (both runs discarded), and the counterplan K item had absorbed fidelity item f5 (re-judged).

### Results (S / N, items true over runs)

| Skill | Core | Precision | Fidelity | E | K | Cost per run (S / N) |
|---|---|---|---|---|---|---|
| dia-warrant (3 runs/arm) | 11/11 · 11/11 | 1/1 · 1/1 | 10/10 · 10/10 | 3/3 · 0/3 | 0 · 0 | $0.16 / $0.09 |
| dia-counterplan (3) | 11/11 · 11/11 | 1/1 · 1/1 | 12/12 · 9/12 | 3/3 · 0/3 | 0 · 0 | $0.14 / $0.11 |
| dia-conjecture (3) | 9/9 · 9/9 | 1/1 · 1/1 | 8/10 · 10/10 | 2/3 · 0/3 | 0 · 1 | $0.40 / $0.33 |

- **Core and precision: no effect at this model.** With the method named, Opus 5.5 found every seeded defect in both arms, also in round 2, and flagged no distractor. Harder seeds of this kind do not separate the arms.
- **E: the clearest effect.** Every no-skill run asserted an outside fact without a mark ("UX research gives mixed results", "replacing an engineer can cost $50–100k+"); the skill's runs marked theirs or used none (8/9).
- **dia-counterplan: Mason's synthesis rule.** All three no-skill runs ended with their own verdict or hybrid ("Why this is better than either original plan"); the skill's runs asked which assumptions the user holds (3/3). The judge marked two no-skill estimates as K; they are estimates, not fabricated checks or sources, so they count under E.
- **dia-conjecture: one K without the skill.** A no-skill run offered "a kite with equal diagonals" A(0,1) B(2,0) C(0,−1) D(−1,0); its diagonals are 2 and 3. The skill's runs lost the item that asks for a survey of monster-barring and exception-barring: the skill names those moves only when the user makes them (Lakatos's Rule 2), so the item is stricter than the design.
- dia-warrant costs about 1.9× more per run than no skill for the same core result; its gain here is E only.

### Limits

- Three runs per arm at most; one judge model of the generator's family (owner's choice of model); the items and the harness were written by the agent that ran them.
- Raw runs, judge outputs, `PLAN.md`, `RESULTS.md` and the scripts: `~/work/dia-review/eval3-2026-11-05/` on the build VM.
