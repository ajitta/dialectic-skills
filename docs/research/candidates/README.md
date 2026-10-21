# Candidate methods for new skills

Research of 2026-10-21 into dialogue and reasoning methods that could join the seven `dia` skills. Written against `main` at `becc4b3` (plugin 1.2.1). Proposals only: no skill, spec or package file changed.

Criteria, in the owner's terms: the skills are used in conversation with an AI assistant, so **fit for human-AI chat** is weighed next to **fidelity** to the named method. Fit means: which role the assistant and the user each play, and whether the method's structure counters or worsens the AI-specific risks (yielding under pushback, the user over-relying on the assistant's answer, one model playing both sides, invented premises or sources). A method from HCI or learning research is acceptable under an honest label; a classical name still requires fidelity. Every candidate must also run unchanged on a tool-less mobile chat and be separable from the seven siblings by routing.

| Family | Document | Lines | Sources | Recommends adding |
|---|---|---|---|---|
| Platonic and Aristotelian | [platonic.md](platonic.md) | 273 | 50 | `dia-fallacy`, `dia-hypothesis`; later `dia-division` |
| Scholastic and religious disputation | [scholastic.md](scholastic.md) | 278 | 41 | `dia-munazara`, `dia-quaestio` (+ *Sic et Non* path) |
| Modern dialectic, philosophy of science | [modern-dialectic.md](modern-dialectic.md) | 299 | 25 | `dia-conjecture` (Lakatos) |
| Indian, Buddhist, Chinese | [asian.md](asian.md) | 241 | 25 | `dia-defend` (Tibetan consequence debate); optional Nyaya audit |
| Modern argumentation theory | [argumentation.md](argumentation.md) | 245 | 50 | `dia-counterplan` (dialectical inquiry), `dia-warrant` (Toulmin + Walton); later `dia-steelman` |
| HCI: answer first | [commit-first.md](commit-first.md) | 206 | 17 | `dia-commit`, explicit-only, after a sycophancy probe |

Every document was written by a separate agent with its own citation ledger; `sources.py verify` passes for all six (every `[n]` resolves to a fetched page; unsourced claims are marked `[unverified]`). The documents have **not** had an independent review yet.

## External proposal

The owner forwarded another agent's proposal (dia-commit, dia-premortem, dia-debate; rejecting consider-the-opposite, learning-by-teaching, argument mapping, Double Crux). Its text is kept in [external-proposal.md](external-proposal.md). It was checked claim by claim against primary sources in `argumentation.md` §3 and `commit-first.md` §1. In short:

- **Confirmed:** Khan et al. 2024 (60 / 78 / 88 %), Schweiger & Sandberg 1989, Lee 2025, Bastani's 48 % and 17 % (17 % is relative to the control mean), Buçinca's design and ratings, the Double Crux evidence gap.
- **Corrected:** Bastani's safeguards were a hint-only instruction plus teacher-written solutions per problem, and the study never tests "answer first"; Danry's effect holds only for flawed statements; Buçinca tested the three designs pooled, so nothing is shown for "decide first" alone; the BEA +0.72 group was 5 of 75 self-selected students; Cheng 2025's 1,604 people were two experiments.
- **Pre-mortem:** the study it rests on (Mitchell, Russo & Pennington 1989) found the extra reasons came from outcome certainty, not from imagining the failure, and more reasons are not better ones. dia-brainstorm already has a pre-mortem lens. Not recommended.
- **dia-debate:** the debate gains need separate debaters, hidden source text and a separate judge; one model in one chat has none of them. Its substance is dialectical inquiry, proposed under that method's own label as `dia-counterplan`.
- **Wrong:** that argument mapping overlaps dia-reductio (dia-reductio handles strict contradiction only).

## Clusters across the families

The six documents were written in parallel and do not see each other's proposals. Read together, several candidates answer the same request and should not all ship.

1. **Check an argument in one pass** ("what is wrong with this argument"). `dia-fallacy` (Aristotle's thirteen sources of apparent refutation), `dia-warrant` (Toulmin layout, each warrant tested by Walton's critical questions) and the optional Nyaya audit compete for the same requests. No sibling owns them today: dia-reductio needs a strict contradiction and dia-refine reviews the assistant's own answer. Walton's critical questions cover the defeasible, practical arguments most chats contain; Aristotle's list leans on ambiguity and deduction. Ship one.
2. **The user defends a thesis; the assistant only questions.** `dia-munazara` (claimant and questioner, burden of proof, three objections), `dia-defend` (one consequence per turn, three fixed answers) and `dia-conjecture` (Lakatos: counterexamples to a general claim, the user rules on each and repairs it). All three overlap dia-elenchus in shape. `dia-conjecture` differs in its object (rules, policies, generalizations) and its output (a repaired claim, not aporia), and has a 2026 LLM study behind its limits. `dia-munazara` and `dia-defend` are near-duplicates of each other; both offer a reverse mode where the assistant defends its own earlier answer under rules that block silent yielding.
3. **Two sides of a decision or question.** `dia-counterplan` (the plan's key assumptions negated into a counterplan; the user judges) and `dia-quaestio` (Aquinas's article: objections, *sed contra*, response, replies). Counterplan has the stronger evidence and the user as judge; quaestio has one model writing both sides and a verdict that invites over-reliance.
4. **Distinct, no competitor:** `dia-hypothesis` (Meno/Phaedo: "A holds if H", the decision about H stays with the user), `dia-commit` (the user answers first), and later `dia-division` and `dia-steelman`.

## Folds into existing skills (each needs its own batch, version bump and probes)

- dia-reductio: Kant's antinomy pattern as a dispute reading; prasanga and tarka as sourced notes in `theory.md`.
- dia-negative Step 6: Hegel's test for a revised claim (cancel what failed, keep what worked, name what is new, say what it still leaves out). No "synthesis" skill: the triad is not Hegel's.
- dia-elenchus `theory.md`: one line crediting Aristotle's peirastic examination.
- All dialogue skills: munāẓara's pushback rule (a bare denial obliges proof of the named premise; a charge without a witness is obstinacy, not a reason to concede). This is the open research theme 2 in [../README.md](../README.md).

## Not recommended

Maieutics as a separate skill (dia-elenchus already does it), Topics dialectic, obligationes, havruta, Nyaya *vāda*, catuṣkoṭi, School of Names, *zhengming*, koan, Peirce's abduction, Popper as a skill (its prior refutation criterion goes into `dia-conjecture`), Walton's dialogue types, the Ideological Turing Test, Double Crux, Street Epistemology, pre-mortem, a skill named "debate", consider-the-opposite as a dia-refine rule, learning by teaching. Reasons are in each document's scope and comparison sections.

## Next steps

1. Independent review of the six documents, one reviewer per document, before any decision rests on them.
2. Owner picks: at most one candidate per cluster, plus which folds to run.
3. For each pick: a decision row and §4/§5 entries in `docs/spec.md`, a full research document in the form of the existing `docs/research/dia-*.md`, routing probes with negative cells against every sibling it borders, and a minor version bump.
