# Candidate methods: Indian, Buddhist and Chinese dialogue and debate

Written 2026-10-21 against `main` at `becc4b3`. Proposals only; nothing here changes a skill. Two criteria carry equal weight: **fidelity** to the named method, and **fit for human-AI chat** (one model in a chat, the user as the other party). Every source below was fetched for this document; claims I could not source are marked `[unverified]`.

## 1. Scope

Covered:

- **Nyaya debate theory** (vada / jalpa / vitanda, the five members, tarka, points of defeat): a defined procedure exists in the *Nyaya-sutra*.
- **Catuskoti and Nagarjuna's prasanga method**: covered to settle the overlap with dia-reductio.
- **Tibetan monastic debate** (consequences, *thal 'gyur*): the most procedural candidate. It has fixed roles, fixed answer types and a clear end condition.
- **Mohist disputation (bian)**: the fairness principle and the four moves of the "Lesser Selection".

Covered briefly, folded into the sections above:

- **Kathavatthu**: a canonical Theravada refutation form, treated under the Tibetan section.

Dropped:

- **School of Names**: SEP presents the paradoxes (for example the "White Horse Discourse") as the harmful, victory-seeking style of disputation, not as a procedure to follow [7].
- **Confucian "correcting names"** (*zheng ming*, *Analects* 13.3): a doctrine about governing with consistent names, not a dialogue procedure [7]. Its concern for definitions is already served by dia-elenchus.
- **Zen koan**: dropped. A koan is built so that "intellectual reasoning alone cannot solve it", and a master must verify the practitioner's state of mind in private consultation [19]. No step can be stated as a reasoning procedure, and an assistant certifying insight would be the over-reliance failure in its purest form.
- **Milinda-panha**: SEP calls it mostly expository and analogical, with no identifiable argumentative pattern [2].

## 2. Candidates

### 2.1 Nyaya debate theory (vada, jalpa, vitanda; five members; tarka; nigrahasthana)

**Primary source.** The *Nyaya-sutra* (Vidyabhusana's 1913 translation) defines the three kinds of debate. NS 1.2.1: "Discussion is the adoption of one of two opposing sides. What is adopted is analysed in the form of five members, and defended by the aid of any of the means of right knowledge, while its opposite is assailed by confutation, without deviation from the established tenets" [3]. NS 1.2.2: wrangling (jalpa) "aims at gaining victory" by "quibbles, futilities, and other processes which deserve rebuke". NS 1.2.3: cavil (vitanda) "consists in mere attacks on the opposite side" [3]. Prets gives the Sanskrit of NS 1.2.1–3, and of a later sutra (NS 4.2.49 in his numbering) that justifies jalpa and vitanda "for the protection of the ascertainment of truth, just as thorns or branches are used for the protection of the seedlings" [25]. Prets also cites NS 4.2.46f. (his numbering): friendly discussion is held with pupils, teachers, fellow students and other seekers of the good who are free of envy [25]. Sutra numbers differ between editions.

**Five members** (NS 1.1.32): proposition, reason, example, application, conclusion. Stock instance: "This hill is fiery / Because it is smoky / Whatever is smoky is fiery, as a kitchen / So is this hill / Therefore this hill is fiery" [3]. IEP gives the same form with the Sanskrit names pratijna, hetu, udaharana, upanaya, nigamana [1]. SEP stresses that the early form is analogical: the example is a similar case (sadharmya) or a dissimilar one (vaidharmya), and the deductive canonical form comes later, with Vasubandhu and Dignaga [2].

**Tarka** (NS 1.1.40) "reveals the character by showing the absurdity of all contrary characters" [3]. Vidyabhusana notes that the term is rendered variously as "confutation", "reductio ad absurdum" and "hypothetical reasoning" [3]. IEP adds two points [1]:

- tarka is only an "assistant to the pramanas", not an independent means of knowledge;
- it is "a reductio which depends not only on logical inconsistency, but on incoherence with deeply-held beliefs or norms".

**Faults.** NS 1.2.4 names five pseudo-reasons: the erratic, the contradictory, the equal to the question, the unproved, the mistimed [3]. NS 5.2 lists 22 grounds for defeat (nigrahasthana) [2]. Vidyabhusana's list includes hurting, shifting, opposing and renouncing the proposition, shifting the reason or topic, saying too little or too much, repetition, silence, evasion, and overlooking or censuring wrongly [3]. Keating reports Jayanta Bhatta's view on how these apply in discussion [6]:

- only defeats relevant to the argument count; a momentary loss for words (apratibha) does not;
- accidental errors are pointed out but do not end the discussion;
- quibble (chala, NS 1.2.10) and misleading rejoinders (jati) are excluded from discussion by definition;
- discussion ends in certainty (nirnaya), "the ascertainment of a fact by both standpoint and contrary standpoint" (NS 1.1.41).

**Procedure (vada) as the sources give it:**

1. A doubt with two opposed theses on one subject.
2. Each side states its thesis in five members.
3. Each supports its own thesis by means of knowledge and attacks the other's by tarka, without contradicting settled tenets and without chala or jati.
4. Relevant faults are pointed out.
5. The exchange ends in nirnaya, or the doubt remains.

**Faithful LLM version?** Partly.

- The five members and the five pseudo-reasons are well defined and can be applied in text.
- Vada needs two parties, each holding a thesis. In a chat the assistant would have to hold the counter-thesis.
- Tarka, in IEP's account, admits incoherence with "deeply-held beliefs". That is the loose reductio dia-reductio excludes on purpose (Rule 1).
- Honest-label departures: a one-party audit is not a vada; the analogical example becomes an explicit general rule; school tenets (siddhanta) are replaced by what the user accepts.

**Shape.** Debate is multi-turn; an "argument audit" (five members plus pseudo-reason check) would be one pass. **Needs from the user:** a thesis and a reason. In debate, the user also defends it.

**Overlap with the seven skills:**

- **dia-reductio** (partial to high): tarka and the contradiction pseudo-reason.
- **dia-refine** (partial): "logical leaps".
- **dia-negative** (partial): no contradiction of one's own settled tenets, which is close to internal critique.
- **dia-elenchus** (low): no definition dialogue.
- **dia-brainstorm, dia-confirm, dia-iterate**: none.

**Routing risk:** "does my argument hold" requests, which belong to dia-reductio.

**Human-AI fit: medium.**

- **Roles:** the user is the proponent (paksa) and the assistant is either the opponent (pratipaksa) or an auditor. An assistant that argues the other side has some support: in a group study, LLM devil's advocates that argued against the AI's recommendation promoted more appropriate reliance on the AI [21]. That opposition was aimed at an AI recommendation, though, not at a user's thesis.
- **One model on both sides:** if the assistant writes the counter-thesis, it is arguing a side. If it also judges, one model plays both sides. Liang et al. report "Degeneration-of-Thought" in self-reflection, and note that LLMs "might not be a fair judge" [23].
- **Two-sided debate needs two debaters:** multi-agent debate gains are reported for several model instances debating over rounds [17], not for one instance alone. Michael et al. find that debate between two experts helps a non-expert judge more than a single consultant does (84% vs 74%) [24]. A single chat has only one assistant, so the vada's two-sided structure cannot be honestly reproduced unless the user carries one side.
- **Invented premises:** reconstructing the user's argument into five members invites the assistant to supply the example and the general rule. These must be labelled as added, as dia-reductio does with [A].

**LLM research.** Sathish fine-tunes small models on a six-phase Navya-Nyaya scaffold (doubt, evidence source, five members, tarka, pseudo-reason detection, ascertainment), trained on 55 logic problems [10]. It is a single-author arXiv preprint about puzzle solving, not dialogue, and its "tarka = counterfactual verification" is the author's own mapping. It is not evidence for a chat skill.

### 2.2 Catuskoti (tetralemma) and Nagarjuna's prasanga method

**Primary sources.** Priest: early Buddhist logic assumed four possibilities for any state of affairs, "that it held, that it did not, both, or neither" [9]. His example is the Buddha's undeclared questions in the *Majjhima-nikaya*, left undeclared "because they are not connected with the goal" [9]. Nagarjuna rejects all four corners, as in *Mulamadhyamakakarika* XXII.11 ("'Empty' should not be asserted. 'Non-empty' should not be asserted. Neither both nor neither should be asserted") and XXV.17 [9]. Priest reads this with paraconsistent semantics (First Degree Entailment) and grants that "classical logicians have had a hard time making sense of this" [9]. IEP, on MMK 1.1, describes the fourfold denial as "an exhaustive refutation of the efficacy and coherence of the category in question" [8].

**Prasanga.** IEP describes the Prasangika reading [8]:

- Nagarjuna shows "only the unwanted consequences ('prasanga') entailed by his opponents' claims", "not as defending any philosophical 'thesis' (pratijna) of his own";
- Bhavaviveka objected that Buddhapalita's version gave "no reason and no example";
- Candrakirti defended Buddhapalita.

SEP adds that Nagarjuna has no "master argument". The refutation must "proceed in a step-by-step manner", with a different argument for each opponent [4].

**Faithful LLM version?** Prasanga in the procedural sense is assuming the opponent's thesis and deriving consequences the opponent rejects, while asserting no thesis of one's own. That is dia-reductio's `--target=user` refute direction with an "internal" strength grade. The catuskoti as Nagarjuna uses it is tied to emptiness and svabhava, so a general "consider yes / no / both / neither" check would carry the name without the doctrine. Faithful "both" needs a paraconsistent reading that ordinary users do not hold. Fidelity: high for prasanga (as reductio), low for a catuskoti skill.

**Shape:** one pass. **Overlap:** dia-reductio high (prasanga); dia-brainstorm partial (four corners as an option generator, which it is not). **Routing risk:** reductio requests.

**Human-AI fit:** prasanga, medium to high: the assistant asserts no counter-view, so the user has nothing to over-rely on. Catuskoti, low: an assistant that produces "both" and "neither" positions invites false profundity, and the user cannot check them. **LLM research:** my searches found formal-logic papers on the tetralemma but no LLM study [unverified: absence of evidence].

dia-reductio's `theory.md` dropped its Madhyamaka line because it rested on Wikipedia alone (`docs/research/dia-reductio.md` B6). IEP [8] and Priest [9] are now scholarly sources if the owner wants a note back.

### 2.3 Tibetan monastic debate (consequences, thal 'gyur)

**Primary and reference sources.** Samuels (Oxford Research Encyclopedia) calls debate (*rtsod pa*) "a uniquely Tibetan method of structured analysis and discourse" [12]. It is chiefly Geluk, learned through the Collected Topics (*bsDus grwa*) primers of sample debates, and "only truly comprehensible in terms of the institutional context of its performance" [12]. Hugon translates *thal 'gyur* neutrally as "consequence" [13]. In Phya pa (1109–1169) she finds consequences that prove and consequences "that fail to prove the proponent's thesis but still succeed in refuting the opponent" [13]. The procedure below is from Dreyfus, a Geluk *geshe lharampa*, in excerpts from *The Sound of Two Hands Clapping* [11].

**Procedure (Dreyfus [11]):**

1. **Roles.** A defender answers; a questioner asks. Quoting Perdue: "The defender puts forth assertions for which he is held accountable. The challenger raises qualms … and is not subject to reprisal." The questioner's questions must "logically follow from the points already made"; their truth "is irrelevant".
2. **Opening (jorwa).** The questioner elicits the defender's thesis and seeks clarifications, "to establish a starting point … an area of agreement".
3. **Main part.** The questioner draws consequences of the form "It follows that S is P, because S is R", to make the defender "contradict himself or … take a blatantly absurd position".
4. **Answers.** The defender must give one of three answers: "I accept", "The reason is not established" (R does not hold of S), "There is no pervasion" (R does not entail P). For an ill-formed or loaded consequence he says "the subject is faulty". Evasions such as "What I really mean is…" are "not accepted"; the questioner insists on one of the three answers.
5. **Root consequence.** The defender's thesis is restated as a consequence that he must later be forced to contradict.
6. **Ending.** Absurdity is "not favored, for it is difficult to distinguish a blatant absurdity from an apparently counterintuitive but valid point", so "debaters prefer to end with their opponents' self-contradiction". There are three possible endings: a direct contradiction (formally clear, so no witness is needed); a stalemate or a successful defence; or the questioner's line breaking down.

Dreyfus notes that the three answers are a Tibetan development; in Dharmakirti's tradition the defender had four, more specific answers [11]. Pressure is part of the practice: handclaps, "chir, chir, chir" ("why"), audience teasing [11].

**Precursor: Kathavatthu.** SEP gives its canonical form [2]:

1. "Is A B?" "Yes."
2. "Is C D?" "No."
3. "Acknowledge your refutation": if A is B then C is D, and holding A-is-B with C-not-D is wrong.

It is the same commitment-based shape.

**Faithful LLM version?** Largely yes. The consequence form, the three answers, the opening and the self-contradiction ending can all run in text. Honest-label departures:

- no audience, gestures or time pressure;
- no shared Buddhist curriculum as background, so the common ground has to be built in the opening;
- Geluk debate targets doctrinal topics, while this adaptation would target any thesis.

**Shape:** multi-turn, one consequence per message. **Needs from the user:** a thesis they hold, and willingness to answer in the three forms.

**Overlap with the seven skills:**

- **dia-elenchus** (partial to high): one question at a time, contradiction from the user's own answers; its patterns include a "Consequence" question. Differences: elenchus is about "what is X?", keeps the revisions as ideas and ends in aporia. Dreyfus's root example is a definition (impermanence as "momentary") [11], but the form tests any thesis, and the three answers make the user say which link fails.
- **dia-reductio** (partial): the same strict-contradiction ending, but reductio lays out the whole chain at once, while the user answers each step here.
- **dia-brainstorm** (routing only): "poke holes in my plan".
- **dia-negative, dia-refine, dia-iterate, dia-confirm**: none.

**Routing risk:** "debate me", "argue with me", "stress-test my plan". The description must say that the user defends their own thesis and the assistant asserts nothing.

**Human-AI fit: high.**

- **Roles.** The assistant is the questioner and the user is the defender. The questioner asserts nothing and is "not subject to reprisal" [11], so the user has no assistant answer to over-rely on. This matches HCI findings: AI-framed questions improved people's detection of logically flawed statements more than causal AI explanations did (N=204) [20], and cognitive forcing cut over-reliance, at the cost of lower user ratings [22].
- **Invented premises.** Every consequence names its reason, so a premise the user never gave shows up as a reason they can reject with "reason not established". The skill should require each reason to be the user's words, an item agreed in the opening, or a fact marked with its evidence class.
- **Sycophancy.** Tested in the reverse mode, where the user questions and the assistant defends its own earlier answer, the three answers block silent flipping. Laban et al. find models flip 46% of the time after "Are you sure?" [15]. Wang et al. find LLMs "cannot maintain their beliefs in truth" against "oftentimes absurdly invalid arguments" [14]. Sharma et al. tie sycophancy to human preference data [16]. A defender who may only say "accept", "reason not established" or "no pervasion" has to name a defect, or else accept a consequence that visibly contradicts its thesis. This is a structural guard derived from analogues; no study tests this method.
- **One model on both sides:** does not arise, because the user is the other party.
- **Tool-less:** the method rests on contradiction between statements already in the chat. Mündler et al. found 35.2% of ChatGPT self-contradictions cannot be verified with online text, yet can be detected by prompting alone [18].
- **Costs:** consequence chains are long on a phone, and forced answers can feel adversarial; Buçinca et al. report lower ratings for the interventions that worked best [22].

### 2.4 Mohist disputation (bian)

**Primary source, via SEP.** In Canons A73–74, disputation is "contending over which of two complementary terms, such as 'ox' and 'non-ox', 'fits'" a thing [5]. The "Lesser Selection" (*Xiao qu*) states a fairness rule: "Having it in our case, we do not reject it in the other's; lacking it in our case, we do not demand it in the other's" [5]. It also names four moves [5]:

- **Analogy** (*pi*).
- **Paralleling** (*mou*).
- **Pulling** (*yuan*): "You are so, how is it that I alone cannot be so?"
- **Pushing** (*tui*): "On the grounds that what they don't accept is the same as what they do accept, propose it."

SEP judges that the moves are not a fixed sequence [5]. It warns that parallel phrasing can mislead: the Mohists hold "killing robbers is not killing people", a "this but not so" case, without a principled diagnosis [5]. A 3rd-century text quoted in SEP's School of Names entry contrasts good disputation (separating kinds, clarifying what one refers to, so that "the loser gains what he's seeking") with twisting the other's words [7].

**Faithful LLM version?** The moves are rhetorical techniques, not a procedure with a start and an end. Pulling and pushing are commitment-based analogy: you accepted it for A, and B is the same kind. A skill could use them faithfully as moves, but "Mohist disputation" as a whole has no stopping rule to follow.

**Shape:** a move within multi-turn dialogue. **Overlap:** dia-elenchus partial (its too-broad and too-narrow cases are analogy questions); dia-negative partial (the fairness rule is a consistency-of-standards check). **Routing risk:** low as a move, unclear as a skill.

**Human-AI fit: high as a move.** The assistant cites the user's own precedent and asks how the new case differs; the user supplies the difference. The danger is citing a precedent the user never accepted, so it must be quoted. **LLM research:** none found specific to bian.

## 3. Comparison

| Candidate | Fidelity achievable | Fit for AI chat | Overlap | User value | Recommendation |
|---|---|---|---|---|---|
| Tibetan consequence debate | high (with a label for no audience, pressure or shared tenets) | high: the assistant asserts nothing; named reasons expose invented premises; the three answers block silent flips | partial-high: dia-elenchus; partial: dia-reductio | high: tests any thesis turn by turn, ends only on visible self-contradiction | **ADD**: the only candidate with roles, answer types and an end rule that run unchanged in a chat |
| Nyaya vada (two-sided debate) | medium (needs a second debater) | medium-low: the assistant must argue a side, or one model plays both | partial: dia-reductio | medium | **SKIP** as a debate: one assistant cannot honestly supply both sides |
| Nyaya argument audit (five members + five pseudo-reasons) | medium (one-party audit, not vada) | medium: a reconstruction invites added premises | partial-high: dia-reductio, dia-refine | medium | **ADD later, optional**: only if the owner wants an argument-structure check distinct from strict contradiction |
| Tarka | high as a description | n/a | high: dia-reductio (the loose variant it excludes) | low | **SKIP**: name it in dia-reductio theory as the looser Indian counterpart |
| Prasanga | high (as reductio) | medium-high | high: dia-reductio | low as a new skill | **FOLD** into dia-reductio `theory.md` as a sourced note (IEP [8], SEP [4]) |
| Catuskoti | low outside Madhyamaka doctrine | low | partial: dia-brainstorm (misuse) | low | **SKIP** |
| Kathavatthu form | high | high | high: Tibetan candidate, dia-elenchus | low alone | **FOLD** into the Tibetan skill's theory reference as a precursor |
| Mohist pulling/pushing | high as moves | high | partial: dia-elenchus, dia-negative | medium | **FOLD** into the Tibetan skill as a labelled consequence type, else SKIP |
| School of Names, *zheng ming*, koan | n/a | low (koan) | n/a | n/a | **SKIP** (§1) |

## 4. Ranked recommendation

**1. `dia-defend` (working name; alternatives in §5).**

- **Honest label:** "Consequence debate adapted from Geluk Tibetan monastic debate as Dreyfus describes it: two parties in text, with no audience, gestures, time pressure or shared Buddhist tenets; the common ground is built in the opening."
- **Steps:**
  1. Ask for the thesis the user holds.
  2. Opening: clarify key terms one question at a time and number the agreed items.
  3. State the root consequence in the user's own words: "It follows that [S] is [P], because [S] is [R]."
  4. Each turn: one well-formed consequence. Its reason must be the user's quoted words, a numbered agreed item, or a fact with its evidence class.
  5. The user answers "I accept", "reason not established", "no pervasion", or "subject faulty" (ambiguous or loaded). Any other reply gets one request for one of these answers.
  6. After "reason not established" or "no pervasion", the next consequence either supports the rejected link or opens another line.
  7. Optional move, labelled as Mohist pushing: "You accepted X for A; it follows that B is X, because B is like A in R." Here "no pervasion" is the user's way to name the difference.
- **Stop rule:** end on a direct contradiction between two of the user's numbered answers, shown side by side. Otherwise end when the assistant's line breaks down (it says so plainly: "the thesis held against these consequences"), on a stop signal, or after the user picks a revision. Accepting a counterintuitive consequence is noted, never scored as defeat [11]. Close with a record: thesis, agreed items, the consequences with their answers, and one result (**self-contradiction**, **held**, **stalemate**, **stopped**).
- **Optional reverse mode** (owner decision): the user questions and the assistant defends its own earlier answer, bound to the same three answers. It concedes plainly when an accepted consequence contradicts its thesis, and never flips without naming which answer applies.
- **Never:** assert its own view on the thesis while questioning; use a reason the user did not give without a label; apply pressure or mockery; count hesitation or wording slips as defeat (Jayanta's rule for discussion [6]); continue after stop; interleave with dia-elenchus.

**2. `dia-nyaya` argument audit (optional, lower priority).**

- **Honest label:** "Uses the Nyaya-sutra's five-member argument and five pseudo-reasons as a one-pass audit; not a vada, which needs a second debater."
- **Steps:** reconstruct the target argument as thesis, reason, example with its general rule, application and conclusion, labelling every member the target did not state; test the reason against the five pseudo-reasons; apply tarka to the contrary thesis, labelled as resting on accepted beliefs, not strict contradiction; give one result (ascertained on these grounds / doubt remains) and leave the decision to the user.
- **Stop:** one pass.
- **Never:** quibble on a second meaning (chala); count an added member as the target's; call a merely implausible consequence a contradiction. That last case goes to dia-reductio.

**3. No third skill.** Fold prasanga, tarka and the Kathavatthu into theory references (§3).

## 5. Open questions for the owner

1. Is the overlap with dia-elenchus acceptable? Both build contradictions from the user's answers one question at a time. dia-defend differs in target (any thesis versus "what is X"), answer form (three fixed answers) and result (no aporia, no "ideas born").
2. Name: `dia-defend`, `dia-debate` (higher routing risk: "debate me about X" usually asks the assistant to argue a side), or `dia-consequence`.
3. Should the reverse mode (the assistant defends its own answer) ship? It targets sycophancy directly, but has no direct evidence and could make the assistant stubborn.
4. Should the forced three answers be strict, as in Dreyfus [11], or softened for chat? Strict forms reduce over-reliance but are rated lower by users [22].
5. Should dia-reductio's `theory.md` regain a Madhyamaka/prasanga note, now that scholarly sources exist?

## Sources

[1] https://iep.utm.edu/nyaya — Nyaya (IEP, Dasti)
[2] https://plato.stanford.edu/entries/logic-india — Logic in Classical Indian Philosophy (SEP)
[3] https://archive.org/stream/TheNyayaSutrasOfGotama/Vidyabhusana_Nyaya-Sutras_1913_djvu.txt — The Nyaya Sutras of Gotama, tr. S.C. Vidyabhusana (1913), archive.org text
[4] https://plato.stanford.edu/entries/nagarjuna — Nagarjuna (SEP)
[5] https://plato.stanford.edu/entries/mohist-canons — Mohist Canons (SEP)
[6] https://doi.org/10.3390/rel12100875 — Keating, The Pragma-Dialectics of Dispassionate Discourse: Early Nyaya Argumentation Theory (Religions 2021)
[7] https://plato.stanford.edu/entries/school-names/disputation.html — School of Names > Disputation in Context (SEP supplement)
[8] https://iep.utm.edu/madhyamaka — Madhyamaka Buddhist Philosophy (IEP, Arnold)
[9] https://scholarworks.sjsu.edu/cgi/viewcontent.cgi?article=1032&context=comparativephilosophy — Priest, The Logic of the Catuskoti, Comparative Philosophy 1.2 (2010)
[10] https://arxiv.org/abs/2604.04937 — Sathish, Pramana: Fine-Tuning LLMs for Epistemic Reasoning through Navya-Nyaya (arXiv 2604.04937)
[11] https://texts.mandala.library.virginia.edu/book_pubreader/16164 — Dreyfus, Tibetan Monastic Education (excerpts from The Sound of Two Hands Clapping), Mandala/UVA
[12] https://academic.oup.com/edited-volume/62249/chapter/551439251 — Samuels, Debate in the Tibetan Tradition, Oxford Research Encyclopedia of Religion (abstract)
[13] https://www.oeaw.ac.at/fileadmin/Institute/IKGA/PDF/digitales/Hugon_2016_Phya_pa_on_thal_gyur_2_JIABS39.pdf — Hugon, Phya pa on Argumentation by Consequence (thal 'gyur) (2), JIABS 39 (2016)
[14] https://arxiv.org/abs/2305.13160 — Wang, Yue, Sun, Can ChatGPT Defend its Belief in Truth? Evaluating LLM Reasoning via Debate (EMNLP Findings 2023)
[15] https://arxiv.org/abs/2311.08596 — Laban et al., Are You Sure? The FlipFlop Experiment (arXiv 2311.08596)
[16] https://arxiv.org/abs/2310.13548 — Sharma et al., Towards Understanding Sycophancy in Language Models (arXiv 2310.13548)
[17] https://arxiv.org/abs/2305.14325 — Du et al., Improving Factuality and Reasoning through Multiagent Debate (arXiv 2305.14325)
[18] https://arxiv.org/abs/2305.15852 — Muendler et al., Self-contradictory Hallucinations of LLMs (arXiv 2305.15852)
[19] https://plato.stanford.edu/entries/japanese-zen — Japanese Zen Buddhist Philosophy (SEP)
[20] https://www.media.mit.edu/publications/don-t-just-tell-me-ask-me-ai-systems-that-intelligently-frame-explanations-as-questions-improve-human-logical-discernment-accuracy — Danry et al., Don't Just Tell Me, Ask Me (CHI 2023), MIT Media Lab page
[21] https://dl.acm.org/doi/fullHtml/10.1145/3640543.3645199 — Chiang et al., Enhancing AI-Assisted Group Decision Making through LLM-Powered Devil's Advocate (IUI 2024)
[22] https://arxiv.org/abs/2102.09692 — Bucinca, Malaya, Gajos, To Trust or to Think: Cognitive Forcing Functions (CSCW 2021)
[23] https://aclanthology.org/2024.emnlp-main.992 — Liang et al., Encouraging Divergent Thinking in LLMs through Multi-Agent Debate (EMNLP 2024)
[24] https://arxiv.org/abs/2311.08702 — Michael et al., Debate Helps Supervise Unreliable Experts (arXiv 2311.08702)
[25] https://istb-staticsites.univie.ac.at/caraka/file_download/Prets2003-JIP-Parley%20reason%20and%20rejoinder.pdf_%3b%20size%20%3d%20_164995 — Prets, Parley, Reason and Rejoinder, Journal of Indian Philosophy 31 (2003)
