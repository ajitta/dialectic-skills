# External proposal (forwarded by the owner, 2026-10-21)

English summary of another agent's proposal, as forwarded by the owner in Korean. Kept as received; it is checked against primary sources in [argumentation.md](argumentation.md) §3 and [commit-first.md](commit-first.md) §1, which supersede it.

The other agent proposed three new skills (all chat-only, no scripts) and rejected four.

## Proposed

1. dia-commit: the user states their own answer and reasons first; then the assistant gives its answer, and asks questions at the points where the two diverge.
   - Bastani 2025 (field experiment, ~1,000 high-school students): unrestricted GPT-4 raised practice scores 48% but students scored 17% lower than no-AI students on an exam without AI; a tutor version with learning safeguards mostly prevented the loss. The agent could not confirm what the safeguards were.
   - Danry 2023 (N=204, CHI): when AI asked questions instead of explaining, people found logical flaws more accurately.
   - Buçinca 2021 (N=199): one of three cognitive forcing designs was "decide yourself first, then see the AI answer" (Update). Significant only for reduced reliance on wrong AI suggestions in one task; overall overreliance difference not significant.
   - Certainty: all from research interfaces; unknown whether skill instructions alone reproduce the effect.
   - Would change: if users keep wanting to skip it, make it an option of dia-intent (now named dia-confirm) instead of a skill.
   - Strongest objection: friction; the abstract says the most effective designs were rated lowest, and the effect was larger for people high in need for cognition.
2. dia-premortem: assume the plan has already failed and work backward to the reasons.
   - All evidence from ONE secondary summary (https://corporate.jcx.au/premortem):
     - 1989 study: imagining an event as already happened produced ~30% more reasons (count, not quality).
     - 178-student study: overconfidence fell about twice as much as with pros/cons; but after planning fixes, confidence rebounded most in this condition.
     - 101-practitioner study: more high-quality risks than ordinary brainstorming.
   - Certainty medium; no study tracks real project outcomes.
   - Would change / objection: merge into dia-brainstorm's "poke holes" if indistinguishable in tests.
3. dia-debate: build the strongest case for the user's position and for an alternative plan starting from the opposite assumption; the user judges.
   - Khan 2024 (ICML): human judge accuracy 60% no expert, 78% with one AI consultant arguing one side, 88% with two AIs debating; in the consultancy condition, more persuasive AI lowered accuracy. Claim "consultancy has the same structure as ordinary chat" is the agent's own interpretation.
   - Schweiger & Sandberg 1989: dialectical inquiry and devil's advocacy groups beat the members' average; "better than consensus" is from prior work the paper cites.
   - Lee 2025 (48 people): an LLM devil's advocate raised group satisfaction; decision accuracy not reported in the abstract.
   - Certainty: weakest of the three. Debate studies used different AIs presenting hidden source text with verified quotes; a skill has one model playing both sides in one chat.
   - Would change: drop if one side is consistently built weaker in tests.
   - Reason recommended: best fit for the name "dialectic"; structurally counters sycophancy. Cited: an analysis of 11 models affirming user actions ~50% more than humans; a 1,604-person experiment where people preferred and trusted sycophantic AI more (Cheng 2025).

## Not recommended
- Consider the opposite: Lord 1984 ("consider the opposite" beat "be fair" at reducing bias); a 2025 LLM paper only demonstrates cases. -> one rule line in dia-refine.
- Learning by teaching: BEA 2025 preliminary result, students who found the AI's errors gained 0.72 on a 6-point scale. -> off-topic, hold.
- Argument mapping: a meta-analysis reported in one textbook, ~0.8 SD in intensive courses; author has a conflict of interest (software developer). -> overlaps dia-reductio, hold.
- Double crux: one search found only a proposal post to test its efficacy. -> drop.

## Spec impact (agent's note)
D1 7 -> 10 skills; §4 name table and §5 three entries; P7 probe scope widened.

## Sources the agent listed
- https://arxiv.org/html/2402.06782v4 (Khan 2024)
- https://www.media.mit.edu/publications/don-t-just-tell-me-ask-me-ai-systems-that-intelligently-frame-explanations-as-questions-improve-human-logical-discernment-accuracy/ (Danry 2023)
- https://ar5iv.labs.arxiv.org/html/2102.09692 (Buçinca 2021)
- https://ideas.repec.org/a/nas/journl/v122y2025pe2422633122.html (Bastani PNAS 2025)
- https://papers.ssrn.com/abstract=4895486 (Bastani SSRN)
- https://corporate.jcx.au/premortem (premortem summary)
- https://ideas.repec.org/a/bla/stratm/v10y1989i1p31-43.html (Schweiger & Sandberg 1989)
- https://arxiv.org/abs/2503.14263 (Lee 2025)
- https://arxiv.org/abs/2510.01395 (Cheng 2025)
- https://causeweb.org/cause/node/7638 (Lord 1984)
- https://arxiv.org/pdf/2507.10124 (Could you be wrong, 2025)
- https://aclanthology.org/2025.bea-1.19 (LLM Protégés, BEA 2025)
- https://ecampusontario.pressbooks.pub/criticalthinking1234/chapter/introduction/ (argument mapping)
- https://www.greaterwrong.com/posts/mnszbzJ2XawR4wXJh/testing-the-efficacy-of-disagreement-resolution-techniques (double crux)
