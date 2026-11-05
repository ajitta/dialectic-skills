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

## Seeded keys and source alignment: dia-warrant, dia-counterplan, dia-conjecture (2026-11-05, plugin 2.3.0)

Question (owner): how to evaluate the skills never compared with no skill, at the least run count that still decides. Observations below are task-specific at one to three runs per arm; broader explanations are marked as hypotheses.

### How to read these results

- **Two kinds of item.** *Finding* items ask whether the seeded defects or readings were found (the item files call them core). *Method* items ask whether the named method was carried out: assumptions listed, a counterplan built from contrary assumptions, the decision left to the user, stated and reconstructed parts kept apart, outside facts and premises marked. For these skills the method is the purpose, not decoration; treating finding as the core was the evaluator's choice.
- **Two baselines.** Rounds 1–2 name the method in the no-skill request ("Toulmin layout and Walton-style critical questions"): a prompt most users would not write, so they ask what the skill adds for an expert prompter. Rounds 5–6 use a plain request ("What do you think of this plan?"), which is what a user without the method's vocabulary types; they are the realistic comparison.
- **Clean material.** Rounds 1–7 use tasks written by the evaluator with figures laid out and defects planted, which makes finding easy. Round 8 uses vague, casual messages instead; there the skills also found more than the plain request (dia-warrant, dia-counterplan), and dia-conjecture's step-by-step dialogue was slower for a casual user.
- **Reading.** Against a plain request, Opus 5.5 finds the same problems without the skill but does not carry out the method: no listed assumptions or counterplan, its own verdict instead of the user's decision, unmarked outside facts. The skill gets the method from one word, the skill's name, at about 1.6–3× the cost per run.

### Method

- **Arms.** S: plugin `dia` 2.3.0, `dia-<x>` first. N: empty plugin, the same request naming the method in words (Toulmin and Walton; Mason's dialectical inquiry; Lakatos). Naming the method is an expert-prompt baseline: it asks what the packaged text adds beyond knowing which method to request, and it understates the value for a user who would not name it.
- **Runs.** Claude Code 2.1.314, claude-opus-5-5 at `--effort low` (owner), generator and first judge; fresh `CLAUDE_CONFIG_DIR`, connectors off, empty working directory, tools `Skill,Read,Glob`. dia-conjecture: two scripted user turns.
- **Items, fixed before the runs.** Finding (core in the item files): seeded defects with an answer key. Source-aligned procedure: items taken from the named method. Plugin design: items that are this plugin's adaptation (dia-counterplan leaving the synthesis to the user is listed under Departures in its `references/theory.md`, not a rule of Mason's). Precision (round 2): a distractor that should not be flagged. E: outside facts marked by their basis. K as in A/B rule 5.
- **Judges.** Opus (one blind pass per run, skill names redacted). Then an independent re-score of the deciding items by Codex (GPT), blind: 28 transcripts under shuffled ids, pasted into the prompt, with the key held outside its reach. The two judges agreed on 51 of 64 item verdicts; Codex was stricter on E and x1.
- **Run count.** Rule set before the runs: one run per arm, a second when the S–N gap is two items or less or a K appears. Round 1 (one task per skill) has two runs per arm. Round 2 (harder seeds with a distractor) has one: its planned second run was not made, and pooling it with round 1 (different tasks) does not replace it.
- Harness defects fixed during the work: a dia-conjecture scripted turn accepted a case before one was raised (both runs discarded); the counterplan K item had absorbed a design item (re-judged); in round 4 a failed packaging step left the B2 runs on the B1 text (discarded and re-run, see Round 4).

### Results, deciding items (S / N; Opus, then Codex)

| Skill (runs per arm) | Finding and distractor | E | Design: synthesis left to the user | K |
|---|---|---|---|---|
| dia-warrant (3) | all, both arms | Opus 3/3 · 0/3; Codex 1/3 · 0/3 | — | none |
| dia-counterplan (3) | all, both arms | Opus 3/3 · 0/3; Codex 1/3 · 0/3 | 3/3 · 0/3 (both judges) | estimates only, counted under E |
| dia-conjecture (3) | all, both arms | Opus 2/3 · 0/3; Codex 2/3 · 0/3 | — | S 0; N 1 (Opus) or 2 (Codex) |

- **Finding: no difference when the method is named.** Both arms found every seeded defect and flagged no distractor; with the method named in the request, the no-skill arm also carried out most of the method.
- **E: same direction under both judges, smaller under Codex.** No no-skill run marked its outside facts; the skill's runs did in 8/9 runs by Opus, 4/9 by Codex (unmarked examples in skill runs: "At 40 people, losing 1 in 3 new hires is expensive"; cardiology being outside interface design).
- **dia-counterplan:** every no-skill run ended with its own verdict or hybrid ("Why this is better than either original plan"); every skill run asked which assumptions the user holds. This is the plugin's design, not Mason's rule.
- **dia-conjecture K:** a no-skill run offered "a kite with equal diagonals" A(0,1) B(2,0) C(0,−1) D(−1,0), whose diagonals are 2 and 3 (both judges, checked by hand). Codex also flagged a non-sequitur in another no-skill run ("OB = OD, meaning A lies on the perpendicular bisector of BD"). Two cases do not give an error rate.
- Cost per run, S / N: dia-warrant $0.16 / $0.09, dia-counterplan $0.14 / $0.11, dia-conjecture $0.40 / $0.33.
- **Judge errors found by the audit:** the Opus judge passed p1 for a plain-baseline run that says "The p-value is probably overstated", passed E for a Sonnet run that asserts "Annual customers are contractually locked in", and passed f4 for a counterplan run that relies on a "weak office market" not in the material. Item totals other than the deciding items above were not re-scored.

### Follow-up: why dia-warrant showed no effect against the method-named baseline (one run per cell)

Round-2 warrant task; Opus judge; two items for rules only the skill has (s1: stated and reconstructed parts marked apart; s2: support judged, never truth).

| Cell | Core (3) | Toulmin/Walton (2) | s1 | s2 |
|---|---|---|---|---|
| Opus, skill | 2–3 (judge passes differ) | 2 | yes | yes |
| Opus, no skill, method named | 3 | 2 | yes | yes |
| Opus, no skill, plain "How strong is this argument?" | 3 | 0 | no | yes |
| Sonnet, skill | 2 | 2 | yes | yes |
| Sonnet, no skill, method named | 3 | 2 | no | yes |

- Hypotheses, not findings (one task, one run per cell): the core result does not need Opus (Sonnet without the skill also found every seeded defect); with a plain request the no-skill run found the defects but did not carry out the method (no Toulmin layout or critical questions, stated and reconstructed parts not kept apart), which is what the skill supplies.
- The skill's runs asked the deferred-renewal question and left it **open** (hard rule 5), where no-skill runs stated it. That led to Round 4.

### Round 4: dia-warrant rule 5, answered from the argument's own words (spec D60)

Texts: A = dia-warrant 2.2.0 (plugin 2.3.0); B1 = first D60 text ("by arithmetic, a definition or a term the argument states"); B2 = adopted text after the independent review ("plain meaning of a word it uses"; any further premise keeps the question open). SHA-256 of B2's packaged SKILL.md: `B2-text.sha256` in the eval directory. Runs, round-2 churn task + round-1 onboarding task: A 2 + 1 (A's churn run 1 is the round-2 S run, reused), B1 6 + 2, B2 2 + 1. Items: a1, the renewal defect stated as a finding from the argument's words; x1, no question settled with a premise the argument does not state.

| Churn task | A | B1 | B2 |
|---|---|---|---|
| a1, Opus / Codex | 0/2 · 0/2 | 5/6 · 6/6 | 0/2 · 0/2 |
| x1, Opus / Codex | 2/2 · 2/2 | 5/6 · 2/6 | 2/2 · 2/2 |

- **B1 rejected:** it stated the finding by adding contract premises ("a contract they had prepaid"; "Prepaid customers who decide to leave would normally do so at renewal"), four of six runs by Codex.
- **B2 adopted:** both churn runs derive the renewal limitation from "annual" and "three months" ("no renewal-time churn has been seen yet") and keep cancellation terms open ("depends on the contract terms, which aren't given"). Both judges score a1 false because the item demands a settled finding; the audit holds that an open question with the derivation stated is the right output here, and that the a1 and k1 keys themselves assumed the contract premise.
- **Residual:** B2's first churn run over-reads its own arithmetic ("The whole drop is a mix shift", from group averages). Onboarding task: B2 keeps the four seeded concerns and says sample adequacy "needs a premise ... the argument doesn't supply".

### Round 5: dia-warrant A vs B2 vs a plain request, corrected keys (2026-11-05)

Before merging D60 (owner). Keys rewritten after the Codex audit so that no item assumes a premise the argument does not state: c1 counts asking about contract terms as well as asserting them; r1 credits the renewal derivation stated as derived even when the wider question stays open; u1 (no question settled with an unstated premise) and o1 (no conclusion the numbers cannot support) added. Arms: A (dia-warrant 2.2.0), B2 (D60 text, SHA in `B2-text.sha256`), N (no skill, the same request without a method name: "How well do the reasons support the conclusion of this argument?"). Two runs per arm on the churn and onboarding tasks; A and B2 churn runs and three onboarding runs reused from earlier rounds, five new runs. Both judges blind; they agreed on 107 of 114 verdicts.

| Churn task, Opus / Codex | A | B2 | N |
|---|---|---|---|
| c1–c3, p1 (seeded concerns, distractor) | all | all | all |
| r1 renewal derivation stated | 0/2 · 0/2 | 2/2 · 2/2 | 1/2 · 1/2 |
| u1 no unstated premise | 1/2 · 1/2 | 2/2 · 2/2 | 0/2 · 0/2 |
| o1 no over-read numbers | 2/2 · 2/2 | 1/2 · 1/2 | 1/2 · 1/2 |
| s1 stated vs reconstructed | 2/2 | 2/2 | 0/2 |
| E | 2/2 · 1/2 | 2/2 · 2/2 | 0/2 · 0/2 |

- Onboarding task: A and B2 identical on every item under both judges. N: s1 0/2; o1 2/2 by Opus, 0/2 by Codex ("too small" without a stated standard); E 1/2; one Opus K for an unrun Fisher test whose conclusion is correct, not counted by Codex.
- **B2 against A:** r1 +2 and u1 +1 on the churn task, o1 −1 (the run already recorded under Round 4, "The whole drop is a mix shift"; the second B2 run did not repeat it, spec D51). Nothing else changes. This supports merging D60.
- **Skill against a plain request:** the seeded concerns are found either way; only the skill's runs carry out the method: the marked layout (s1), marked outside facts (E) and, on the churn task, no question settled by an unstated premise (u1). Two runs per arm on two tasks.

### Round 6: dia-counterplan and dia-conjecture against a plain request (2026-11-05)

The comparison the Codex audit asked for. Same request in both arms, the skill name only in S: "What do you think of this plan?" with the round-2 Japan plan; "Is my proof right?" with the rhombus conjecture and its flawed proof (follow-ups "Go on.", "OK. What now?"). Keys reviewed so that none assumes a premise the material does not state; items labelled core, precision, source (from the named method), design (this plugin's adaptation), E and K. Plugin 2.4.0 (neither skill changed since 2.3.0); Opus 5.5 at effort low; two runs per arm; Opus and Codex judges, both blind, agreeing on 62 of 72 verdicts.

| dia-counterplan, S / N (Opus; Codex) | |
|---|---|
| k1–k3, p1 (seeded readings, no datum disputed) | all, both arms |
| u1 no unstated premise as established | 2/2 · 0/2; Codex 1/2 · 0/2 |
| f1 assumptions listed (source) | 2/2 · 0/2 |
| f3 full counterplan from contrary assumptions (source) | 2/2 · 0/2; Codex 2/2 · 2/2 (the plain runs propose a staged test instead) |
| d1 choice left to the user (design) | 2/2 · 0/2 |
| E | 2/2 · 0/2; Codex 1/2 · 0/2 |
| cost per run | $0.14 · $0.06 |

| dia-conjecture, S / N (Opus; Codex) | |
|---|---|
| k1, k3, k4, f1 (local case found, conjecture kept, proof repaired) | all, both arms |
| k2 the case shown to keep perpendicular diagonals | 2/2 · 2/2; Codex 2/2 · 0/2 |
| d1 repair offered, not imposed (design) | 2/2 · 0/2; Codex 1/2 · 0/2 |
| E | 1/2 · 0/2; Codex 0/2 · 0/2 |
| K | S 1 (Codex; checked by hand) · N 0 |
| cost per run | $0.38 · $0.23 |

- **Finding: no difference.** With a plain request and no method named, Opus still found every seeded reading of the plan and, for the conjecture, the local counterexample, kept the conjecture and repaired the proof.
- **dia-counterplan** adds the method's form (assumptions listed, the choice left to the user), and its runs used fewer unmarked outside premises. A Codex K on one skill run ("about 120 paying customers from the whole waitlist") is a contrary assumption labelled *(my choice)*; it is recorded as disputed, not counted.
- **dia-conjecture K, from the skill:** in its proof-analysis one run labels the congruence of the four triangles "(follows from 1 and 2)", from equal diagonals that bisect each other, and adds "the proof never uses the fact that a rhombus has four equal sides". Equal bisecting diagonals give a rectangle, whose four triangles are not congruent unless it is a square; the step needs the equal sides. The Opus judge missed it. One run; recorded as a lead for the skill's proof-analysis step (an annotation of its own inside the user's steps), not yet a change.
- **Plain-request comparisons for the three skills agree.** Without the skill, Opus 5.5 finds the same problems in this clean material but does not carry out the method the user would have asked for by name: it lists no assumptions and builds no counterplan, decides for the user, and leaves outside facts and premises unmarked. With the skill's name alone the method is carried out in most runs, at about 1.6–3× the cost per run (dia-warrant about 3× in Round 5). On vague messages (Round 8) the skills also found more, except dia-conjecture, which found the same but more slowly.

### Round 7: reproducing the dia-conjecture proof-analysis error (2026-11-05)

Four more runs of the Round 6 skill arm, first turn only (where the proof-analysis is written), plugin 2.4.0, Opus 5.5 at effort low; read and checked by hand against the geometry (no model judge).

- **Not reproduced, 0/4.** Three runs annotate the congruence step, and each annotation is true: "By SSS: each triangle has two half-diagonal sides, which are equal by L1 and L2, and one rhombus side as its third side"; "(this needs L1, L2 and the four equal sides)"; one run adds the equal sides as an [A] lemma ("I added this because steps 1 and 2 only give four triangles whose two shorter sides all match"). The fourth says only "Steps 2 to 5 follow standard reasoning".
- With Round 6 the false annotation is 1 run in 6. No change to the skill: a rule against it would be tested on an error that four runs did not show.
- Observation for a later edit: in two of the four runs the assistant's own note sits inside a line labelled [T] (the user's words), where Step 2 reserves [A] for what the assistant supplies; the run that used [A] kept them apart.

### Round 8: vague real-user input, in Korean (2026-11-05)

The test the clean material could not give. Three short, casual messages of the kind a user without the method's vocabulary sends, each with gaps and no figures: a team lead's "everyone uses AI, other companies do it, so no new hires this year"; "shop 1 does well, so a second café should too; rates are a bit high; should I?"; "exercise always makes you lose weight, because it burns calories, right?" (two vague follow-ups: "음... 그런가요?", "그럼 어떻게 말해야 맞는 거예요?"). S is the same message with the skill's name in front. One run per arm, a second for dia-conjecture (gap of two items under Codex); Opus and Codex blind (42 of 50 verdicts agree on the first runs; the second dia-conjecture pair Opus only). Codex also scored how useful each whole reply would be to this user (1–10).

| | Finding (3), Opus · Codex | Method items | Outside facts marked | Useful (Codex) | Cost per run |
|---|---|---|---|---|---|
| dia-warrant S · N | 3 · 3 / 2 · 1 | 2/2 · 0/2 | yes · no | 8 · 6 | $0.19 · $0.06 |
| dia-counterplan S · N | 3 · 3 / 3 · 2 | 3/3 · 1/3 | yes · no | 7 · 6 | $0.18 · $0.07 |
| dia-conjecture S · N (run 1) | 3 · 3 / 3 · 2 | 2 · 1 of 2 / 0 · 0 | yes · no | 5 · 5 | $0.59 · $0.41 |
| dia-conjecture S · N (run 2, Opus) | 3 / 3 | 1 of 2 / 0 | yes · no | — | $0.37 · $0.19 |

- **With vague input the skills also find more.** Against the plain request, dia-warrant and dia-counterplan found every reading the material allowed; the no-skill replies found fewer under Codex (dia-warrant 1 of 3: it called the other-companies reason weak without saying that adoption is not evidence of results; dia-counterplan did not tie the stated high rate to repayment). The no-skill replies were practical and confident, and that is where they went wrong: thresholds and facts stated as known with no source ("매달 대출 상환액이 예상 순이익의 30~40%를 넘으면 위험해요", "오늘의 신입이 3~5년 뒤의 실무 핵심이에요", "30분 조깅은 대략 250~350kcal"). Codex rated these K; under A/B rule 5 they are unmarked estimates, so they are counted under E. The skills' replies asked for the missing facts instead.
- **dia-conjecture: friction for a casual user.** In both runs it restated the claim, reconstructed the argument into lemmas (L3, "운동을 해도 먹는 양은 늘지 않는다", marked most suspect), and by the third turn had raised no concrete case; asked "how should I say it then?", it declined to settle an answer before cases were checked and offered a candidate ("운동으로 늘어난 소비만큼 섭취가 늘지 않는다면…"). The no-skill replies gave the counterexample and the corrected claim at once ("먹는 양을 유지하면 살이 빠진다"). Both found the same thing; Codex rated both 5. A lead for the skill (raise the first case in the same message as an [A] reconstruction when the user offers no argument, and answer a direct request for the corrected claim with the candidate first), not yet a change.
- Usefulness is one model's rating of one run per arm; the messages were written by the evaluator to read like real ones, not taken from users.

### Round 9: dia-conjecture pace, A/B (2026-11-05, spec D61)

A = dia-conjecture 2.2.0; B1 = first D61 text; B2 = adopted text (B1 plus the hard-rule-2 sentence on stating every condition a check needs); SHA-256 of both in `C2-text.sha256`. Opus 5.5 at effort low. Vague exercise claim (Round 8 messages): A 2 runs (Round 8's), B1 2, B2 2. Vague rain claim with no reason given: A 1, B1 1. Rhombus regression (clean proof): B1 1, B2 1 against Round 6's A. New items: t1, a concrete case by the second reply; t2, the candidate corrected claim given first when asked.

| Exercise claim | A | B1 | B2 |
|---|---|---|---|
| t1 case by the second reply (Opus · Codex) | 0/2 · 0/2 | 2/2 · 2/2 | 2/2 · 2/2 |
| t2 candidate first when asked | 2/2 · 0/2 | 2/2 · 2/2 | 2/2 · 2/2 |
| K | 0 · 0 | 0 · 2 | 0 · 0 |
| useful (Codex, 1–10) | 4, 4 | 6, 6 | 6, 6 |
| B3 (after the Codex review: provisional lemmas accept nothing; criterion apart from the ruling), 2 runs | | | t1 2/2 · 2/2; t2 2/2 · 2/2; K 0 · 0; useful 7, 7 |

- B1's case had no starting balance ("운동으로 약 300kcal를 쓰고 400kcal를 더 먹으니, 하루 100kcal가 남아"); whether that person gains depends on what they ate before, so Codex rated the check K in both runs. B2's runs state it ("운동 전: 하루에 2,000kcal를 먹고 2,000kcal를 썼습니다"; "운동 전에는 하루 섭취와 소모가 똑같아서").
- Rain claim: A asked for a reason, offered a reconstruction and, asked how to put it, asked which reading was meant (Codex 3); B1 reconstructed on the second reply and on the third gave the candidate and an indoor-venue case marked as recall (Codex 6). Not run on B2; B3, one run: candidate and an indoor-venue (station convenience store) case on the third reply, marked as recall, the criterion asked apart from the ruling (Codex 6).
- Rhombus: Opus core items match A; e1 is A 1/2, B1 0/1, B2 0/1. Codex's B1 scores match A; B2 was not scored by Codex.
- Codex criticizes the candidates' weight-loss guarantee (a candidate such as "운동하면서 먹는 양을 늘리지 않는 사람은 살이 빠진다" leaves out a deficit), including in B2's explanations; its g3 scores are false for B1 and true for B2. Opus marks g3 true throughout. The candidates remain unadopted and untested, which is the method's next round.

### Round 10: the remaining skills on vague messages, in Korean (2026-11-05)

The Round 8 design for the skills not yet compared with a plain request: dia-reductio, dia-negative, dia-elenchus, dia-quaestio, dia-skopos, dia-emend, dia-ratchet, dia-regula, dia-adjudicate (dia-techne left out: its A/B waits on real use, D55; dia-router is a menu). One casual message each, two of them with three vague follow-ups; S is the same message with the skill's name in front. Plugin 2.5.0, Opus 5.5 at effort low, one run per arm (a survey: every difference below is a lead, not a measured effect). Opus and Codex judges, blind; they agreed on 81 of 108 verdicts. Codex marked K on most runs of both arms for unsourced general statements ("20대와 50대는 원하는 게 달라요"); those are E under A/B rule 5, and two it marked as invented were real checks (the empty working directory, read with a tool), so no K is counted.

| Skill | Finding, S · N (Opus; Codex) | Method, S · N | Useful (Codex), S · N |
|---|---|---|---|
| dia-reductio | 2/2 · 2/2 | 2/2 · 0/2 | 6 · 7 |
| dia-negative | 2/2 · 1/2 | 2/2 (Codex 1/2) · 0/2 | 6 · 6 |
| dia-adjudicate | 2/2 · 1/2 | 2/2 (Codex 1/2) · 0/2 | 6 · 6 |
| dia-skopos | 2/2 · 1/2 (Codex 0/2) | 2/2 · 1/2 | 5 · 6 |
| dia-emend | 2/3 · 3/3 | 1/1 · 1/1 (Codex 0/1) | 8 · 6 |
| dia-ratchet | 2/2 · 2/2 | 2/2 · 2/2 (Codex 1/2) | 7 · 7 |
| dia-regula | 3/3 (Codex 2/3) · 3/3 | 0/1 · 1/1 | 6 · 8 |
| dia-elenchus | 1/2 · 1/2 | 2/2 · 0/2 | 4 · 8 |
| dia-quaestio | 1/2 (Codex 0/2) · 2/2 (Codex 1/2) | 1/2 · 0/2 | 4 · 6 |

- **Analytical skills** (dia-reductio, dia-negative, dia-adjudicate, dia-skopos) carried out their method where the plain reply did not (numbered premises with sources, the company's own standard and a falsifier, item-by-item rulings, the work held until the open decisions are settled) and found as much or more; usefulness was rated about the same.
- **dia-emend**: the plain reply changed the date to "9일" in its revision without saying it was unconfirmed; the skill's revision marked the date to check (useful 8 · 6). **dia-ratchet**: no difference; the plain reply also asked for the facts behind "30%".
- **dia-regula** reviewed the prompt and stopped at findings ("원하는 항목을 골라 주시면 고쳐 드릴게요"); the plain reply also gave a revised prompt ready to use (useful 6 · 8). Lead: when the user asks to look at a prompt without saying review only, return the revision with the findings.
- **dia-elenchus** kept to the method with a casual user: asked "what is a true friend?", raised a case, and when asked "그럼 뭐라고 해야 돼요?" answered "저도 정답을 몰라요" and asked again. That is the elenchus (no answer from the questioner, aporia), and the plain reply's explanation was rated far more useful (4 · 8). Lead, not a defect: say in one line, when the user asks for the answer, that this method gives none, and name where an answer is (dia-quaestio or a plain question).
- **dia-quaestio** spent its turns restating and confirming ("이렇게 이해한 게 맞을까요?" twice), then closed with "고려한 선택지 … 다루지 않은 것": no options were grown, against its own purpose (useful 4 · 6). Lead, like dia-conjecture before D61: a vague reply should move the dialogue on, not trigger another confirmation.

### Limits

- One to three runs per arm on one task per skill per round; the items, keys and harness were written by the agent that ran them, and two keys (warrant2 k1, round-4 a1) assumed an unstated premise.
- Codex re-scored only the deciding items; the audit (Codex, read-only) is in `codex-audit.out`, the blind scores in `codex-blind.out`.
- Raw runs, judgments, `PLAN.md`, `RESULTS.md` and scripts: `~/work/dia-review/eval3-2026-11-05/` on the build VM.
