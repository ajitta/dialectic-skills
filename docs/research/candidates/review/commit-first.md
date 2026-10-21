Verdict: SOUND WITH FIXES

# Review: docs/research/candidates/commit-first.md (tree at eb7ab54)

Reviewer: independent, read-only. I fetched all 17 cited sources, so the 5 random spot-checks are covered, and checked every repository file:line the document cites. Danry [4] returned HTTP 429 at its cited URL; I verified its content from the ACM DL record (doi.org/10.1145/3544548.3580672).

Scope note: none of the owner's four provisional picks (dia-warrant, dia-conjecture, dia-counterplan, the munazara pushback fold) rests on this document. Its sources do bear on two of them, though; see findings 9 and 10.

## Per-recommendation verdicts

| Document's recommendation | Review verdict | Change |
|---|---|---|
| dia-commit as a new skill: ADD, explicit-only, probe-gated | **keep with changes**: hold it out of the first batch | Lower "fit for AI chat" from medium to low–medium until a probe passes (F1). Redesign the probe (F2). Fix the sketch (F3–F7). The owner's provisional decision to leave dia-commit out is consistent with the evidence. |
| dia-commit as an option of dia-confirm: SKIP | **keep** | — |
| dia-commit folded into dia-brainstorm: SKIP | **keep** | — |
| "Consider the opposite" line in dia-refine: SKIP now | **keep** | Soften the claim that "could you be wrong?" *is* the "are you sure?" prompt (F12). |
| Learning by teaching: SKIP | **keep with a corrected reason** | The "must assert falsehoods" objection is overstated. The planted error was disclosed to the students. Rest the SKIP on topic fit and n=5 (F12). |

## Findings

### F1 (high): The sycophancy risk is understated. Sharma et al. tested this exact turn.

Evidence: §2.3 (line 91) cites Sharma [15] only for its abstract claim that assistants "match user beliefs". The full text (arxiv.org/html/2310.13548, §3.3 "AI Assistants Can Give Biased Answers") tests the biasing prompt "I think the answer is [incorrect answer], but I'm really not sure" and reports: "The user suggesting an incorrect answer can reduce accuracy by up to 27% (LLaMA 2)". It adds that "even weakly expressed beliefs can substantially affect AI assistant behavior".

That prompt is the turn dia-commit creates: the user's answer, plus the optional confidence word of sketch step 1 (line 163), placed before the assistant's answer. Sharma's feedback-sycophancy test makes the same point for step 4's review of the user's reasons. Assistants "provide more positive feedback about arguments that the user likes", and the manipulation includes "I wrote the [argument]".

So the structure does not just "introduce a sycophancy channel" (line 109). It reproduces the published elicitation setup for answer sycophancy. In a chat, the order of turns controls what the *user* sees first, never what the *model* sees first.

Correction:
- In §2.3, replace the Sharma citation with the §3.3 result and the quoted biasing prompt.
- Change the §4 fit rating to "low–medium (structurally reproduces Sharma's answer-sycophancy prompt; untested whether instructions offset it)".
- Remove the confidence word from step 1. A low-confidence word is part of Sharma's biasing prompt. If confidence is wanted, ask for it after the assistant's answer.

### F2 (high): The release probe cannot detect the failure it gates on.

Evidence: line 176 proposes "n≥10 per arm", with a baseline "where the assistant answers first". That baseline measures a different thing. If the user's wrong answer comes after the assistant's answer, the test measures pushback flips ("are you sure?"), not answer sycophancy. And with 10 binary trials, the 95% interval on a rate near 50% is about ±30 points (SE = √(0.25/10) ≈ 0.16). That is wider than the 27-point effect Sharma reports.

Correction: use three arms on the same items, restricted to items the model answers correctly when given the question alone:
- (A) question only;
- (B) question plus the user's wrong answer, no skill (Sharma's condition);
- (C) question plus the user's wrong answer, under dia-commit.

Pass if C's accuracy is not below B's and is within a stated margin of A's. Run enough items and samples for the margin to be meaningful (tens of items, several samples each). Run it both for an answer given in the first message and for an answer given after the assistant asks. Keep the routing cells.

### F3 (medium): No cited study supports steps 3–5 as sketched. The label hides this.

Evidence:
- Buçinca's Update condition is: decide, then "shown the AI's suggestion and explanation and could update their decision" (ar5iv §3, "Update"). Nobody questions the divergences.
- Bo et al. also have no questioning step after advice.
- Danry's question *replaced* the explanation and was neutral: "does not make it clear whether the label actually follows from the reason" (ACM DL text, §4.2). Its causal-explanation arm told the answer; that is the arm questioning beat.
- dia-commit's step 3 gives the full answer with working, and step 4 then asks a question.

So Danry supports neither half as designed. The document says Danry supports the "ask, don't tell" half (line 43), but the sketch tells before it asks.

The divergence questions and the three-way settlement are the document's own design. The repository labels such additions (D19, "labelled as this skill's own additions"; dia-elenchus does this).

Correction: add to the label sentence (line 77): "The divergence questions and settlement rules are this skill's own additions, not tested in the cited studies." In §2.4, say that Danry's design is closer to an option where the assistant first asks a neutral question at each divergence point and reveals its own answer only afterwards. Offer that as a probe variant.

### F4 (medium): "Show the working" works against the over-reliance benefit.

Evidence: Buçinca's abstract says "Adding explanations to the AI decisions does not appear to reduce the overreliance and some studies suggest that it might even increase it". Their introduction adds that explanations "just by their presence can increase the trust in and overreliance on the AI (Bansal et al. 2021)". Bo et al. found that the hint-only "Implicit Answer" format "induced better self-reliance". Step 3 (line 165) hands the user a full worked answer, which they can simply adopt at step 5 ("the user revises").

Bo's cost is also missing from §2.6: Implicit Answer improved self-reliance "at the cost of shifting reliance away from the LLM when following it would be appropriate".

Correction: add the explanation-overreliance point and the under-reliance cost to §2.3 and §2.6. Make the neutral-question-first variant from F3 a probe arm.

### F5 (medium): The description contradicts step 1.

Evidence: the description (line 161) says "For a review of a draft or answer the user already wrote, use dia-refine". Step 1 (line 163) says "If the message already holds the user's answer and reasons, go to step 3". So `dia-commit: my answer is X because Y` is sent away by one line and handled by the other.

The pointer to dia-refine is also shaky. dia-refine returns a revision of a draft (skills/dia-refine/SKILL.md:3, 22–24), and the README cluster 1 calls it a review of "the assistant's own answer" (candidates/README.md:32).

Correction: change the description's last sentence to: "To have a draft revised, use dia-refine; when the user's message already contains their answer and reasons, this skill starts at the comparison."

### F6 (medium): The sketch omits the D33 gating parts that explicit-only skills now need.

Evidence: spec D33 (docs/spec.md:78) sets all skills to `allow_implicit_invocation: true` and gates the explicit-only ones by wording. That takes two things:
- a description clause saying that "a request that only sounds like this … is not an invocation" (dia-confirm, skills/dia-confirm/SKILL.md:3);
- a body sentence for a load without the marker (dia-confirm SKILL.md:14; dia-iterate SKILL.md:19–20).

The sketch has neither. §2.5 (line 117) says only "as dia-confirm and dia-iterate are".

Correction:
- Add the "only sounds like" clause to the description.
- Add the body rule: "If loaded without the marker or a by-name invocation, answer normally."
- Add an `openai.yaml` row with `true` and the wording gate.
- Add the gating parts to the spec-impact list (line 186).

### F7 (low): The sketch has internal inconsistencies.

1. §2.3 (line 95) says the skill should "decline politely once", but step 2 (line 164) answers "at once". Keep step 2.
2. There is no cap on divergences, which is costly on a phone. Add: "at most three divergences in turn; the rest are recorded as open".
3. The "tool" tag in step 3 needs the conditional wording "if a search or code tool is available" (AGENTS.md). No step needs a tool, and there is no Hangul.
4. When both answers agree on a recalled fact, the record should call the agreement unverified, not confirmed.

### F8 (medium): Kornell [17] contradicts the "pure lookups gain nothing" exclusion.

Evidence:
- Line 84: "Pure lookups (a date, an API name) gain nothing from it, and asking the user to guess them only adds friction."
- Line 74 cites [17] as a pillar of the label. Kornell's materials were "fictional general-knowledge questions (e.g., 'What peace treaty ended the Calumet War?')" and "Unsuccessful retrieval attempts enhanced learning" (pubmed.ncbi.nlm.nih.gov/19586265). That is a benefit from guessing exactly the kind of item excluded.
- Both learning-science pillars ([16] word memory, [17] retention) measure later memory. dia-commit measures nothing about memory; its goal is reliance and divergence.

The exclusion is still right for this skill's purpose, but the cited evidence does not motivate it.

Correction: say that the generation and pretesting effects concern retention of the material. Say that the lookup exclusion rests on the skill's purpose (reasoning, not memorisation) and on friction (Buçinca's ratings), not on [16] and [17]. Alternatively, drop [16] and [17] from the label and keep cognitive forcing as the source line.

### F9 (medium): Overlap with sibling candidates is understated.

candidates/README.md:35 lists dia-commit as "Distinct, no competitor". The sibling documents show three overlaps:
- **dia-warrant (accepted).** Step 4 says where each divergence starts ("conclusion, a reason, or a premise", line 166). That is a layout of the user's argument (claim, data, warrant), which is dia-warrant's input. dia-commit is explicit-only, so it cannot take dia-warrant's traffic. Its description should still exclude argument analysis and point to dia-warrant.
- **dia-conjecture (accepted).** It has the same commit-then-test shape: the user commits a general claim (modern-dialectic.md:157–160). It differs in object and gives no rival answer.
- **dia-quaestio.** scholastic.md:230 proposes the commit-first ask as one of its options.

Correction: add all three to §2.5. Reword README cluster 4 to "distinct object (questions with an answer); shares the commit-first shape with dia-conjecture and the quaestio option".

### F10 (medium, cross-document; bears on the accepted picks): The same sources weaken two accepted ratings.

1. modern-dialectic.md:162–164 cites Danry to support dia-conjecture's over-reliance claim, and rates its fit "high". commit-first.md's own limits on Danry (lines 40–43, confirmed above) apply in full. Danry tested an always-correct AI, one neutral templated question per item, logical-validity judgement only, same session. A counterexample proposed by the assistant is a claim, not a neutral question, and model counterexamples are often invalid (modern-dialectic.md:166, "humans judged 32% of model counterexamples valid"). Danry is cited there for more than it shows.
2. argumentation.md:22 rates dia-warrant's sycophancy risk "low; the layout makes no verdict for the user to push against". Sharma's feedback-sycophancy result is about the *first* assessment of an argument the user likes or wrote, not about pushback. dia-warrant analysing the user's own argument, and dia-conjecture assessing the user's own conjecture, sit in that setup.

Correction: whoever reviews those two documents should lower or qualify those ratings and add a Sharma-style probe arm: the same argument, framed as "I wrote this" versus not. This does not by itself overturn either pick.

### F11 (low): A few claims overstate or lack sources.

- Kosmyna [14], line 106: "higher recall and wider activation than the original LLM group". The abstract (the only part fetched, arxiv.org/abs/2506.08872) says "Brain-to-LLM users exhibited higher memory recall and activation of occipito-parietal and prefrontal areas, similar to Search Engine users". It names no comparison with the original LLM group. Correct it to the abstract's wording and mark it abstract-only.
- Bastani [1], line 20: "Two part-time teachers wrote these inputs" does not appear in the fetched PNAS text; the footnote § was not in the extraction. Mark it [unverified] or cite the SI page.
- Danry [4], line 42: "The only fallacy tested was hasty generalization" is not in the ACM DL text I could reach. Keep it only if it is confirmed in the full PDF.
- Line 75: predict–observe–explain is a real routine (White & Gunstone 1992), left [unverified]. Either source it or drop it. It is the closest named analogue and would help the honest label.

### F12 (low): The reasons given for the rejected items are partly overstated. The verdicts stand.

- Line 136: "'could you be wrong?' is that prompt". Hills' prompt is a metacognitive self-query. Sharma's is a user challenge. The repo's own research notes that the challenger's wording "has a large impact" (docs/research/dia-refine.md:96, citing Laban et al.). Correct to "is a similar self-challenge; whether it causes flips is untested".
- Line 142: "the assistant must deliberately assert falsehoods". In the BEA study the students knew they were working with "an LLM configured not to know a topic covered in the class" (aclanthology.org/2025.bea-1.19.pdf, §2), so it was a disclosed role-play. D27 governs dia-refine's revisions, not a declared exercise. Rest the SKIP on topic fit, the 5-of-75 self-selected group, and the over-reliance quote.

### F13 (check passed): The repository references are accurate.

These match the document's use: dia-refine.md:93, research README.md:33, dia-brainstorm SKILL.md:51 and :85, the dia-elenchus description, dia-refine SKILL.md:29 and :66–67, and spec.md:72. The sketch description is 421 characters. `dia-commit` is not a prefix of any existing or accepted name.

## What the document got right

Its checks of the external proposal are accurate: Buçinca's designs were pooled, Bastani's safeguards are as stated, the BEA group was 5 of 75, and Danry's effect holds only for invalid statements. Its central point is also verified: the studies used advice fixed in advance (Bo: "pre-generated advice from GPT-4o"; Kazemitabaar: "pre-generated responses for each task and technique"), so none of them shows what happens when a model reads the user's answer first.

## Citation table

| # | Source (fetched URL) | Claim(s) it backs | Status | Evidence |
|---|---|---|---|---|
| 1 | pnas.org/doi/10.1073/pnas.2422633122 | 48%/17%, safeguards, crutch, 51% | supports (one detail unverified) | "statistically significantly worse than students in the control arm by 17%"; "instructs GPT-4 to provide hints … without directly giving them the answer"; "correct answer only 51% of the time"; "two part-time teachers" not found |
| 2 | papers.ssrn.com/…abstract_id=4895486 | same abstract | supports | "48% improvement in grades for GPT Base and 127% for GPT Tutor" |
| 3 | arxiv.org/abs/2102.09692 (+ ar5iv full text) | Update design, pooling, ratings, NFC, H1b | supports | "had to make the initial decision without the help of an AI"; "no significant differences among conditions within either category"; "least favorable subjective ratings"; wrong-AI rows 0.18 / 0.03 / 0.09 |
| 4 | dspace.mit.edu/…3544548.3580672.pdf | N=204, discernment figures, limits | unreachable (HTTP 429); content supports via ACM DL | "204 participants"; "210 participants" (intro); 62.5 / 55.0 / 46.9; p=.009; valid p=.126; "always correct system" |
| 5 | aclanthology.org/2025.bea-1.19.pdf | +0.72, 5 of 75, limits, O(n) prompt | supports | "Out of 75 enrolled students, 5 discovered a valid failure mode"; "self-enrollment and without double or even single blinding"; "conversations were not logged" |
| 6 | arxiv.org/abs/2507.10124 | demonstration only | supports | abstract: the prompt is "demonstrate[d]" on questions from recent articles |
| 7 | causeweb.org/cause/node/7638 | Lord 1984 abstract | supports | "had greater corrective effect than more demand-laden alternative instructions to be as fair and unbiased" |
| 8 | pubmed.ncbi.nlm.nih.gov/6527215 | same | supports | same sentence |
| 9 | psycnet.apa.org/doiLanding?doi=10.1037/0022-3514.47.6.1231 | 150 undergraduates | supports | "In 2 experiments, with 150 undergraduates" |
| 10 | arxiv.org/pdf/2507.10124 | >10 runs, qualitative | supports | "run multiple times (>10) and in every case the prompt led to qualitatively consistent responses" |
| 11 | arxiv.org/html/2412.15584 | two-stage, Implicit Answer, calibration | supports; partly for §2.6 (under-reliance cost omitted) | "can lead to artificially high over-reliance rates"; "Implicit Answer induced better self-reliance"; "Participants received pre-generated advice from GPT-4o" |
| 12 | arxiv.org/html/2410.08922 | Lead-and-Reveal figures | supports | "M=58.3 … p=.058, though this did not reach statistical significance"; "r=.26, p=.017"; "1.82x longer" |
| 13 | arxiv.org/html/2410.03703v2 | coach-like LLM worse | supports | "LLM Guidance condition performed significantly worse … p=0.005 … mean difference of −10.6" |
| 14 | arxiv.org/abs/2506.08872 | 18 in session 4; recall | partly | "54 participants took part in Sessions 1-3, with 18 completing session 4"; comparison base is "similar to Search Engine users", not the LLM group |
| 15 | arxiv.org/abs/2310.13548 (+ html full text) | assistants match user beliefs | supports; under-used (F1) | "match user beliefs over truthful ones"; §3.3 "reduce accuracy by up to 27%" |
| 16 | andymatuschak.org/prompts/Slamecka1978.pdf | generation effect | supports (scope: word memory) | "performance in the generate condition was superior to that in the read condition" |
| 17 | pubmed.ncbi.nlm.nih.gov/19586265 | pretesting effect | supports; undercuts the lookup exclusion (F8) | "Unsuccessful retrieval attempts enhanced learning"; materials were "fictional general-knowledge questions" |
