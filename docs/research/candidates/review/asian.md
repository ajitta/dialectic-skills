Verdict: SOUND WITH FIXES

# Review of `docs/research/candidates/asian.md` (tree `eb7ab54`)

All 25 sources re-fetched (copies in `../asian-src/`) and searched for each quoted sentence; AGENTS.md, spec §1–7, the seven SKILL.md files and sibling documents read.

Bottom line. The citations are accurate: every classical quotation I checked appears verbatim in its source, and Dreyfus's debate procedure is reproduced faithfully. The problems are in the conclusions drawn from the sources. The document rates the fidelity and chat fit of its top pick (`dia-defend`) too high. It cites HCI studies for more than they show. Its reverse-mode guard against sycophancy does not cover the failure it cites. None of this weakens the owner's provisional picks. Two points sharpen them: F3 favours the munāẓara pushback rule over the Tibetan answer set, and F8 says the counterplan decision must explain why it escapes this document's own objection to one model arguing both sides.

## Per-recommendation verdicts

1. `dia-defend` (Tibetan consequence debate): **drop for this round.** It is a near-duplicate of `dia-munazara` (README cluster 2). `dia-conjecture` now covers "the user owns a claim, the assistant challenges it". Its fidelity and fit ratings need the corrections in F1–F4. If it is revived later, apply F1, F2 and F10 and remove the reverse mode (F3).
2. `dia-nyaya` argument audit: **drop.** Cluster 1 goes to `dia-warrant`. Walton's critical questions cover defeasible chat arguments better than the five pseudo-reasons, and the sketch has two defects (F11).
3. Prasaṅga/tarka note for dia-reductio `theory.md`: **keep with changes.** Prasaṅga is broader than a strict, internally graded reductio (F7).
4. Kathāvatthu and Mohist folds into `dia-defend`: **drop** along with `dia-defend`. Nothing is lost: dia-elenchus already asks too-broad and too-narrow analogy questions.
5. Effect on the owner's provisional picks:
   - `dia-warrant`: this document has no stronger competitor.
   - `dia-conjecture`: no objection. Dreyfus's rejection of "What I really mean is…" corroborates Lakatos's refusal of "I meant…" (modern-dialectic.md:146).
   - `dia-counterplan`: needs one explicit justification (F8).
   - munāẓara pushback batch: supported (F3), with the additions in F14.

## Findings

**F1 (medium): The fidelity rating "high" for Tibetan debate is overstated.**
- asian.md:171 rates fidelity "high (with a label for no audience, pressure or shared tenets)".
- At asian.md:103 the document quotes only half of the sentence it relies on. Samuels's abstract [12] says: "debate is primarily to be understood as a face-to-face practice, distinct from what is represented in the written medium, and only truly comprehensible in terms of the institutional context of its performance."
- Dreyfus [11] shows that shared tenets are what force the defender. The questioner's task is "to oblige the defender to contradict either previous statements or common sense". In the worked example, the defender loses when "no pervasion" would contradict "a basic Buddhist tenet". The winning defender "has contradicted a basic Buddhist tenet for the sake of argument", so the thesis is often not the defender's own.
- Remove the curriculum and the audience, and a user can answer "reason not established" to every consequence. Stalemate then becomes the normal ending on a contested claim. The document lists these departures (asian.md:126–128) but never draws that consequence.
- Correction: rate fidelity "medium: a text adaptation of the consequence form and answer set". Add to the label: "the thesis is the user's own, not curricular; without shared tenets the questioner can use only the user's agreed items, so stalemate is the expected outcome on contested claims."

**F2 (medium): "The assistant asserts nothing" is not true of the sketch, and the sketch reopens the invented-premise risk.**
- asian.md:143 justifies the "high" fit rating by saying the questioner "asserts nothing". Yet sketch step 4 (asian.md:190) lets a reason be "a fact with its evidence class". That is an assistant assertion, and the repo's evidence classes include "unverified recall" (dia-reductio SKILL.md:34).
- Dreyfus [11] says the truth of the questioner's questions "is irrelevant". Transferred to chat, that licenses the assistant to supply false reasons, with only the user left to catch them.
- The sketch has no counterpart of dia-elenchus's rule against agreement given to please (SKILL.md:29: "An agreement given just to please you poisons the argument"). A user who defers to the assistant will "accept" the consequences it frames. That is user-side yielding, and the document never analyses it.
- Correction:
  - Reasons may come only from the user's quoted words or from numbered agreed items.
  - A fact may enter only as an item the user agrees to in the opening.
  - A **self-contradiction** result may not rest on an item the assistant supplied.
  - Add elenchus's please-agreement rule.
  - Replace "asserts nothing" with "asserts no view on the thesis".

**F3 (medium): The reverse-mode guard against sycophancy does not cover the case it cites. This supports the owner's munāẓara choice.**
- asian.md:145 and asian.md:195 claim that the three answers "block silent flipping", citing Laban et al. [15].
- Laban's challenge is a bare "Are you sure?" ("models flip their answers on average 46% of the time", on seven classification tasks). A bare challenge contains no consequence, so none of "accept / reason not established / no pervasion" applies. The guard is silent in exactly the case that was measured.
- Munāẓara's bare denial (man') does cover it: the claimant must prove the named premise (scholastic.md:138, :155).
- The document also misses that the repository already has the core rule: a step is withdrawn only when its defect can be named (dia-elenchus SKILL.md:88, dia-reductio SKILL.md:123, `docs/research/README.md:33`). The marginal value of the reverse mode is therefore smaller than claimed.
- Correction: say that the three answers apply only to challenges in consequence form, and drop the reverse mode in favour of the pushback-rule batch.

**F4 (medium): HCI studies are cited for more than they show.**
- asian.md:143 says "This matches HCI findings". Neither study tests a questioner pressing the user's own thesis.
- Danry et al. [20] studied "discernment of logical validity of socially divisive statements". The AI held a classification and phrased it as a question, and the effect is reported for "logically flawed statements".
- Buçinca et al. [22] tested forcing functions on AI *recommendations* ("they accept an AI's suggestion even when that suggestion is wrong"). `dia-defend` gives the user no recommendation to over-rely on, so the mechanism differs.
- Chiang et al. [21], cited at asian.md:74, say devil's advocates "have the potential to promote" appropriate reliance. The document drops that hedge.
- Correction: "No study tests this role split. The nearest analogues are AI-framed questions on given statements [20] and forcing functions on AI recommendations [22]." Restore the hedge on [21].

**F5 (low): The Liang et al. quotation [23] is truncated, which changes its meaning.**
- asian.md:75 quotes that LLMs "might not be a fair judge", in support of "one model plays both sides".
- The full sentence is "LLMs might not be a fair judge if different LLMs are used for agents". It is a finding about judge bias across different models, not about one model judging its own two sides.
- Correction: quote the condition in full, or drop the citation.

**F6 (low): The Mündler et al. claim [18] is stretched.**
- asian.md:147 says self-contradictions "cannot be verified with online text, yet can be detected by prompting alone".
- The paper studies contradictions within a model's *own* generated text. Its detector reaches "around 80% F1", which is not the same as "can be detected".
- Correction: "a prompting-only detector found about 80% F1 on a model's own self-contradictions; this is an analogue for checking statements already in the chat."

**F7 (low–medium): The prasaṅga fold maps prasaṅga onto dia-reductio too tightly.**
- asian.md:93 says prasaṅga "is dia-reductio's `--target=user` refute direction with an 'internal' strength grade".
- IEP [8] describes "the unwanted consequences ('prasaṅga') entailed by his opponents' claims". An unwanted consequence need not be Q and not-Q. dia-reductio counts only strict contradiction (Rule 1, SKILL.md:33), and its internal grade allows only [T] and [L] premises (SKILL.md:75).
- Correction for the `theory.md` note: "Prasaṅga (the Prāsaṅgika reading, IEP; SEP) draws consequences the opponent cannot accept. When a consequence is a strict contradiction from the opponent's own premises, it matches the refute direction with an internal grade. Consequences that are only unacceptable fall outside Rule 1, as tarka does."

**F8 (medium; bears on an accepted pick): This document's own argument against one model arguing both sides applies partly to `dia-counterplan`.**
- asian.md:76 and asian.md:172 skip Nyāya vāda because "one assistant cannot honestly supply both sides", citing [17] and [24].
- `dia-counterplan` has the same assistant write the counterplan, including against "the assistant's own earlier answer" (argumentation.md:162, :189), and argumentation.md:87 concedes "One model plays both sides".
- The picks can coexist, but only on the grounds argumentation.md gives: the user, not the assistant, is the judge, and the counterplan is built mechanically from listed negated assumptions. A sound decision record should say this, or the two documents contradict each other.
- Correction: in the spec decision row for `dia-counterplan`, give the reason it is exempt from the "one assistant, two sides" objection. Consider making the user's own plan the default target rather than the assistant's own recommendation.

**F9 (low): The routing analysis is understated (moot if dropped).**
- asian.md:139 lists the triggers "debate me", "argue with me" and "stress-test my plan", and names a risk only against dia-brainstorm.
- "Stress-test" is in dia-brainstorm's description, "argue the other side" is a planned `dia-counterplan` trigger (argumentation.md:93), and claim-defence requests belong to `dia-conjecture` and `dia-munazara`.
- Correction: list all four collisions.

**F10 (low): The `dia-defend` sketch is internally inconsistent.**
- Step 5 (asian.md:191) lists four answers, while asian.md:130, :145 and :195 say "three".
- The stop rule ends "after the user picks a revision" (asian.md:194), but no step produces revisions; that would be an elenchus addition with no label.
- "Held" and "stalemate" are given no distinguishing definitions, although Dreyfus separates a stalemate, a successful defence and the questioner's line breaking down.
- "Never scored as defeat [11]" is stronger than Dreyfus, who says absurdity "can be seen as tantamount to a defeat" but "is not favored". Label it as this skill's choice.
- "Any other reply gets one request" has no fallback, and there is no phone turn-length rule like dia-elenchus Rule 2 (cf. asian.md:148).

**F11 (low; moot): The Nyāya audit sketch has two defects.**
- asian.md:203: "call a merely implausible consequence a contradiction. That last case goes to dia-reductio". This is backwards: dia-reductio rejects merely implausible consequences (Rule 1).
- The audit's result "ascertained on these grounds" uses nirṇaya, which NS 1.1.41 defines (Keating [6]) as ascertainment "by both standpoint and contrary standpoint, after having deliberated". A one-party audit announcing it is the assistant certifying a result, which is the over-reliance risk the document warns about elsewhere.

**F12 (low): Omissions that do not change the ranking.** Dignāga's triple condition on a reason (SEP [2]), from which "reason not established" and "no pervasion" derive, is missing from the audit discussion; Jain anekāntavāda is neither in scope nor dropped.

**F13 (low): Citation precision.** [7] says the White Horse Discourse "is probably an example" (asian.md:20 drops "probably"); [2] puts the earliest deductive syllogism in the Upāya-hṛdaya, before Vasubandhu (asian.md:31); [4], [5], [19] need trailing slashes (HTTP 301).

**F14 (low–medium): A useful fold for the owner's munāẓara batch that the document leaves stranded.**
- Jayanta's rules for discussion (Keating [6]) are symmetric guards. Only defeats relevant to the argument count; being "momentarily embarrassed or without an idea (apratibhā) is not a reason to declare victory"; "accidental errors do not bring about the end of the c[onversation]".
- They stop a pushback rule from being turned against the user. asian.md:196 uses them only in `dia-defend`'s "Never" list.
- The document's own open question 3 (asian.md:211) names the opposite risk: the assistant "could make the assistant stubborn".
- Correction: the pushback-rule batch should state three things:
  - A bare denial obliges the assistant to re-check, then prove or concede.
  - A user's slip or hesitation is never scored against them.
  - Like the Tibetan guard, the rule rests on analogues and is not tested by any study.

## What holds

Dreyfus's procedure (asian.md:107–114) and the Nyāya, Kathāvatthu, Zen and Milinda material are quoted verbatim and correctly; neither sketch needs a tool, uses Hangul or names a product.

## Citation table

All 25 citations were fetched and checked; this subsumes the random spot-check of 5.

| # | Source | Used for | Status | Evidence |
|---|---|---|---|---|
| 1 | IEP Nyāya | tarka; five members | supports | "a reductio which depends not only on logical inconsistency, but on incoherence with deeply-held beliefs or norms" |
| 2 | SEP Logic in Classical India | 22 grounds; Kathāvatthu; Milinda; sādharmya | supports (minor dating, F13) | "NS 5.2 sets out 22 cases"; "Is A B? … Acknowledge your refutation" |
| 3 | Vidyābhūṣaṇa NS (archive.org) | NS 1.2.1–4, 1.1.32, 1.1.40 | supports | "Discussion is the adoption of one of two opposing sides" |
| 4 | SEP Nāgārjuna | no master argument | supports (URL 301) | "The Madhyamaka refutation of svabhāva must proceed in a step-by-step manner" |
| 5 | SEP Mohist Canons | fairness rule; four moves | supports (URL 301) | "It is unlikely they form a fixed sequence of steps" |
| 6 | Keating 2021 | Jayanta's rules; nirṇaya | supports | "momentarily embarrassed or without an idea (apratibhā) is not a reason to declare victory" |
| 7 | SEP School of Names, disputation | drop of School of Names | partly | "(The 'White Horse Discourse' of Gongsun Long is probably an example of this style of disputation.)" |
| 8 | IEP Madhyamaka | prasaṅga; Bhāvaviveka | supports | "no reason and no example are given" |
| 9 | Priest 2010 | catuṣkoṭi | supports | "four possibilities: that it held, that it did not, both, or neither" |
| 10 | Sathish arXiv 2604.04937 | Nyāya LLM study | supports | single author; "55 Nyaya-structured logical problems" |
| 11 | Dreyfus, Mandala/UVA | whole Tibetan procedure | supports (fidelity inference: F1) | "Their truth content is irrelevant" |
| 12 | Samuels, ORE (abstract) | institutional context | supports, quoted selectively (F1) | "primarily to be understood as a face-to-face practice" |
| 13 | Hugon 2016 | thal 'gyur; Phya pa | supports | "consequences that fail to prove the proponent's thesis but still succeed in refuting the opponent" |
| 14 | Wang et al. 2023 | yielding to invalid arguments | supports | "cannot maintain their beliefs in truth … when challenged by oftentimes absurdly invalid arguments" |
| 15 | Laban et al. | 46% flips | supports the figure; does not support the guard (F3) | "models flip their answers on average 46% of the time" |
| 16 | Sharma et al. | sycophancy from preference data | supports | "likely driven in part by human preference judgments" |
| 17 | Du et al. | multi-instance debate | supports | "multiple language model instances propose and debate" |
| 18 | Mündler et al. | tool-less contradiction detection | partly (F6) | "35.2% for ChatGPT) cannot be verified using online text"; "around 80% F1" |
| 19 | SEP Japanese Zen | koan drop | supports (URL 301) | "intellectual reasoning alone cannot solve it"; "private consultation" |
| 20 | Danry et al. CHI '23 (abstract) | questions beat explanations | partly (F4) | "discernment of logical validity of socially divisive statements" |
| 21 | Chiang et al. IUI '24 | devil's advocate, reliance | partly (hedge dropped, F4) | "have the potential to promote groups' appropriate reliance on AI" |
| 22 | Buçinca et al. 2021 | forcing functions; ratings | partly (different mechanism, F4) | "least favorable subjective ratings" |
| 23 | Liang et al. EMNLP 2024 | DoT; unfair judge | partly (truncated, F5) | "LLMs might not be a fair judge if different LLMs are used for agents" |
| 24 | Michael et al. | debate 84% vs consultancy 74% | supports | "84% judge accuracy compared to consultancy's 74%" |
| 25 | Prets 2003 | NS 4.2.49; friendly debate | supports | "just as thorns or branches are used for the protection of the seedlings" |
