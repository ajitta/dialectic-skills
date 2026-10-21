# Candidates: scholastic, Talmudic and Islamic disputation methods

Research for possible new `dia-*` skills, written 2026-10-21 against plugin `dia` 1.2.1 (`main` at `becc4b3`). Proposals only: no skill file is changed. Two primary criteria, weighed together: **fidelity** to the named method, and **fit for human-AI chat** (one model in a chat, the user as the other party). Sources were fetched and registered in a citation ledger; claims without a source carry `[unverified]`.

## 1. Scope

- **Covered: scholastic quaestio (article form of Aquinas's *Summa Theologiae*).** The best-documented written form; it is a one-pass text, so a chat can reproduce it.
- **Covered: university disputatio and the quodlibet.** Covered together, because in chat they reduce to role assignments around the quaestio (§2.2).
- **Covered: Abelard's *Sic et Non*.** Its Prologue gives explicit rules for reconciling sources that seem to conflict, which is a distinct procedure.
- **Covered: obligationes (positio).** Explicit rules, but a logic exercise of low everyday value (§2.4).
- **Covered: Talmudic machloket, sugya (kushya and resolution, teyku) and havruta.** Three different things that are often run together. Kept separate (§2.5).
- **Covered: Islamic ādāb al-baḥth wa-l-munāẓara (jadal's later, general form).** Explicit roles and moves (§2.6).
- **Dropped: classical jadal of kalām and fiqh as a separate candidate.** Its later systematisation in ādāb al-baḥth is the form with fetchable rules; Miller traces that path from theology through jurisprudence to the new discipline at the end of the 13th century [9].
- **Dropped: pilpul.** The Jewish Encyclopedia describes its later form as degenerating into sophistry, an end in itself [23]. Not a method to build a skill on.
- **Dropped: medieval sophismata and insolubilia.** These are kinds of propositions argued in disputation form, not a separate dialogue procedure [2].

## 2. Candidates

### 2.1 The quaestio / article (Aquinas)

- **In the sources.** An article runs: (1) the question; (2) objections against the position the master will defend; (3) the *sed contra*, "most often a brief Scripture quote or passage from a Father"; (4) the *respondeo* or body, which is the master's determination; (5) a reply to each objection [3].
  - *Summa Theologiae* I q.2 a.1 shows the shape. "Objection 1. It seems that the existence of God is self-evident…" The sed contra combines Aristotle and Psalm 53. The answer works by a distinction: self-evident in itself versus self-evident to us. "Reply to Objection 1" grants part of the objection and denies the rest [4].
  - The *Summa*'s questions are "artificial, carefully composed imitations of disputations". Aquinas arranges the objections "to achieve a rhetorical as well as a logical effect", "always finds arguments on both sides", and aims to give beginners "training in a certain way of thinking" [2].
  - Bazán's definition of the disputed question ends with the master reaching "a doctrinal solution by an act of determination" [2].
- **Procedure (as given).** Pose "Whether X?". State the objections for the side to be rejected. Give one sed contra. Determine, usually by distinguishing senses. Answer every objection in turn [3][4].
- **Faithful in chat?** High: the *Summa* article is itself a written, single-author form [2], which is exactly what one assistant produces. There are two honest-label departures if adopted:
  - Aquinas's sed contra is usually an authority [3]. Here it would be a source the user supplied, or one argument labelled as such, never a recalled quotation.
  - Aquinas always determines [2]. An "undetermined" outcome would be a borrowing, for example from the Talmud's *teyku* (§2.5).
- **Roles in chat.** The assistant plays the master: it writes the objections, the sed contra, the determination and the replies. The user plays the questioner who poses the question; in the quodlibet variant the user also supplies objections.
- **AI-specific risks, and how the form acts on them:**
  - **One model plays both sides.** This invites strawman objections. A model that is confident in a solution tends not to generate new thoughts by self-reflection ("Degeneration-of-Thought") [42]. The form only partly counters this: it requires that every objection be answered, but the author picks the objections. A rule that at least one objection must be partly conceded would push against strawmen.
  - **Over-reliance.** "I answer that" reads as authority. People over-rely on AI suggestions, and explanations do not reduce this; cognitive forcing does, at a cost in user ratings [41]. The form worsens the risk unless the determination states what it rests on and what would change it.
  - **Sycophancy.** Assistants match user beliefs over truth [24]. If the user's view is known, the determination may drift toward it. Writing the objections before the answer helps a little.
  - **Invented sources.** Fabricated citations were 55% of GPT-3.5's and 18% of GPT-4's citations in one study [40]. A sed contra built from authorities makes this worse unless it is limited to supplied material.
- **One-pass or multi-turn.** One pass; follow-ups answer new objections.
- **Needs from the user.** A contested question, plus optional sources or objections.
- **Tool-less.** Yes.
- **Overlap with the seven skills:**
  - dia-confirm: none.
  - dia-elenchus: none. Elenchus works multi-turn from agreed premises, gives no answer, and ends in aporia.
  - dia-brainstorm: partial. Stress mode also tests an idea, but by questions and the user's options.
  - dia-reductio: partial. Both are one-pass with an argued result, but reductio needs a strict contradiction.
  - dia-negative: none.
  - dia-refine and dia-iterate: none.
- **Routing risk.** Medium. "Argue both sides", "pros and cons" or "is X true?" could be pulled away from ordinary answers, and "does this hold up" from dia-reductio. The description needs the named form ("disputed question", "objections and replies", "quaestio") and an exclusion for factual lookups.
- **LLM/HCI evidence (nearest analogue).** An LLM devil's advocate that argued against the AI's recommendation promoted appropriate reliance in group decisions, and interactive versions felt more collaborative [32]. AI counterarguments raised satisfaction in power-imbalanced groups without a significant workload increase [28]. One-step counter-argument prompts that target implicit and explicit premises beat multi-step pipelines [29]. No study implementing the quaestio itself was found.

### 2.2 University disputatio and the quodlibet

- **In the sources.** The disputation grew out of the *lectio*. Its supporting and opposing arguments "are supplied by students", and it was held both privately and "solemnly" [2]. Quodlibetal questions "were brought forward by students rather than masters", "display much less unity", and "might be designed to put the master on the spot". In both kinds the master's *determinatio* orders the questions into articles [2].
  - Theological quodlibeta were "special disputations held before Christmas and Easter ca. 1230-1330, mostly at the University of Paris", on questions *de quolibet*, "about anything" [38].
  - Weijers likewise defines the disputatio de quolibet as "the disputation on any question raised by anyone of the attenders" [16].
- **Fidelity and fit.** The oral form needs several parties: opponents, a respondent and a master. In chat the assistant would play opponent and master at once and judge its own debate. Liang et al. also report that an LLM "might not be a fair judge" when the debaters are different LLMs [42]. Fidelity: medium. Fit: medium.
- **What it adds beyond §2.1.** A multi-question mode, in which the user brings any questions and gets one short article each, ordered by the determinatio. **FOLD into the quaestio skill.**

### 2.3 Abelard, *Sic et Non*

- **In the sources.** Abelard raises a question and arranges citations from scriptural and patristic authorities "into positive and negative responses". His Prologue gives advice for resolving the apparent conflicts: check whether words are used in the same sense, draw distinctions, look at context, and check whether the author speaks in his own voice [6]. The Prologue itself (Lewis tr., Boyer–McKeon line numbers) lists:
  - Unfamiliar usage and words that change meaning (11–18).
  - False attributions of authorship and textual corruption (54–85).
  - Statements later retracted, stated "reflecting the opinion of others", or left "under investigation" (86–148).
  - Distinguishing "command", "indulgence" and "exhortation to perfection"; whether a rule is general or specific; and its times and causes (176–187).
  - Only when logic cannot resolve the conflict: compare the authorities and keep "whatever has stronger witnesses and greater confirmation" (188–194).
  - The aim: "through doubting we come to questioning and through questions we perceive the truth" (330–350) [5].
  - The Sourcebook's introduction notes that Abelard left the 158 questions open [5]. Lombard, not Abelard, achieved the systematic organisation [2].
- **Faithful in chat?** High for the procedure. The honest-label departure: the "authorities" become whatever sources the user supplies (studies, policies, style guides), not the Church Fathers.
- **Roles in chat.** The assistant compiles and harmonises; the user supplies the sources and decides.
- **AI-specific risks:**
  - **Invented quotations.** This is the decisive risk. Citation fabrication is common [40], so the method is safe only if every "sic" and "non" item is quoted from supplied material or from a page opened in the session.
  - **Conflicting sources in the context.** LLMs blending conflicting sources is an open problem ("inter-context conflict") [39]. The Prologue's ordered checks give the model a procedure in place of silent blending.
  - **Over-harmonising.** A risk of its own. Abelard's last step keeps real conflicts as real.
  - **Sycophancy and over-reliance.** Low, because the output is a map of the sources, not a verdict.
- **One-pass.** **Needs:** two or more sources and a question. **Tool-less:** yes, if the user pastes the sources; without them, it should stop.
- **Overlap:**
  - dia-reductio: partial. Reductio finds a contradiction within one premise set; Sic et Non tests whether two texts really contradict.
  - dia-negative: partial. Both read texts closely, but dia-negative critiques one target against its own standard.
  - dia-refine: low. It fact-checks one draft.
  - None with the others.
- **Routing risk.** Low to medium. "These two sources disagree, which is right?" now goes to plain chat; few existing triggers compete.
- **LLM/HCI evidence.** Only the analogues above [39][40]. No implementation of Sic et Non found.

### 2.4 Obligationes

- **In the sources.** An opponent puts forward propositions and a respondent grants or denies them; doubting is allowed only rarely [1]. In *positio* a usually false *positum* must always be granted [1]. Burley's core rules:
  - Grant the positum.
  - Grant what follows from it.
  - Deny what is incompatible with it.
  - Answer irrelevant propositions "on the basis of its own quality", that is, their known truth value.
  - Relevance is judged against all answers given so far, so the order of propositions matters and "one can prove any false proposition that is compossible with it" [1].
  - Kilvington, the anonymous *De arte obligatoria* and Swyneshed revised these rules in rival ways [1].
  - Uckelman models obligationes as formal dialogue systems. The disputation ends when *cedat tempus* is called, and the opponent wins by forcing the respondent into inconsistency; "nothing further … hinges upon winning or losing" [7]. Hamblin cited obligationes as inspiration [7].
  - Their purpose "remains stubbornly unclear" [7]. SEP calls the genre a "consistency maintenance game" and notes its closeness to the Socratic elenchus [1].
- **Fidelity and fit.** Fidelity is high, but a skill must pick one rule set (Burley is the standard [1]). Two arrangements are possible:
  - Assistant as respondent: it keeps a numbered commitment list visibly in the chat. That matters, because LLMs struggle to keep a hidden goal consistent across turns unless it is written in context [31].
  - User as respondent: a logic drill.
  - Formal dialogue games can regulate LLM utterances in a goal-oriented dialogue [30].
  - Sycophancy is irrelevant here, since truth is suspended by design.
  - User value is low outside logic teaching. dia-reductio already marks reasoning from an impossible supposition as *per impossibile*, with result "stopped".
- **Verdict.** **SKIP.** Possibly a teaching game later.

### 2.5 Talmudic machloket, sugya (kushya, resolution, teyku) and havruta

- **Machloket.**
  - "Every dispute that is for the sake of Heaven, will in the end endure", with Hillel and Shammai as the model [13].
  - Both houses' views are "the words of the living God", yet the law follows Beit Hillel because they "would teach both their own statements and the statements of Beit Shammai", stating Beit Shammai's first [14].
  - The Mishnah records the minority opinion so that a later court may rely on it [35].
- **Sugya.**
  - Its basic form is "a statement with a support, followed by a challenge a resolution of the challenge, another challenge, another resolution" (Brodsky, abstract) [37].
  - Aramaic *qashya* means "difficult, open to objection; unanswerable objection; contradiction" (Jastrow) [36].
  - The Hebrew term *terutz* for the answer is yeshiva usage [unverified].
  - A *baʿya* poses two equally balanced definitions. It is solved only by appeal to an earlier authority ("come and hear"); without one it ends *teyku*, "let it stand", inherently unsolved (more than 300 instances in the Bavli) [17].
  - The give-and-take sits mostly in the anonymous Stammaitic layer, which favoured "rhetorical questions" and "pseudo-dialogue" [20]. Jacobs likewise argues the sugya's debate is a literary construction [17]. So the dialectic on the page is partly composed, not a transcript.
- **Havruta.**
  - "When Torah scholars study together, they sharpen one another". Fire does not ignite "in a lone stick of wood". There is "a sword" upon scholars who study alone [15][22].
  - Rabbi Yoḥanan valued Reish Lakish's "twenty-four difficulties" over a student who brought supporting texts: "your bringing proof to my statements does not" serve a purpose [21].
  - The wise person "does not break into his fellow's speech", "asks what is relevant", says "I have not heard" and "acknowledges the truth" [34].
  - Kent's empirical study names six practices in pairs: listening and articulating, wondering and focusing, supporting and challenging. It counts the text as a third partner [19].
- **Fidelity.**
  - Havruta is a human peer practice around canonical texts [19]. A model as the "peer", reading arbitrary texts, would be an adaptation and needs an honest label.
  - Naming a secular tool after a religious study practice is a sensitivity the owner should rule on.
  - A "kushya chain" is faithful to the literary sugya form [37], not to oral practice.
- **Roles and fit.** Assistant and user as partners over a supplied text; in the kushya form, the assistant raises a challenge and the user resolves it.
  - The structure counters sycophancy explicitly: the BM 84a norm prefers challenge to confirmation [21].
  - It counters over-reliance by keeping the minority view and a teyku outcome [35][17].
  - The model is not a peer, though: its challenges may be generated rather than read from the text.
  - Fit: medium.
- **Overlap and routing.**
  - The one-at-a-time challenges overlap dia-elenchus (partial) and dia-brainstorm (partial); text critique overlaps dia-negative (partial).
  - Routing risk is high: "help me read this text" is an everyday request.
- **Verdict.** **SKIP** as a skill for now. **FOLD** two elements into the quaestio: a *teyku* outcome (the question stays undetermined, with the balanced considerations), and recording the rejected side's best argument (Eduyot 1:5) [35][17].

### 2.6 Ādāb al-baḥth wa-l-munāẓara (munāẓara)

- **In the sources.** Al-Samarqandī founded the discipline as a general theory of scientific discussion, drawn from Aristotelian logic and Islamic law [8]. Karabela dates his death to 702/1303 [11]; Belhaj says the first half of the 14th century [8].
  - Ṭaşköprüzāde's handbook (Arif tr.) defines disputation as investigation "by two opposing sides … in order to discover the truth", with set tasks and codes of conduct [10]. The tradition's stated goal is the "manifestation of truth (iẓhār al-ḥaqq)" [12].
- **Roles.** The *sāʾil* (questioner) attacks; the *muʿallil* (claimant, also *mujīb*) defends a thesis and its proof [10][11].
- **The questioner's three moves [10][11]:**
  - **Man' / munāqaḍa: deny a premise.** Legitimate only if the premise is neither evident nor conceded by both. The denial may come with a backing (*sanad*) or bare (*man' mujarrad*). The questioner must not go on to prove the premise false, which would be usurping the claimant's role (*ghaṣb*).
  - **Naqḍ: the proof as a whole fails.** For example, the same proof yields a known falsehood, or it is circular or regressive. A witness (*shāhid*) is required, "lest the opponent charge him with sheer obstinacy (mukābarah)".
  - **Mu'āraḍa: a counter-argument for an incompatible thesis.** The roles then switch for that argument.
- **The claimant's replies [10]:**
  - To a denial: prove the premise, or point out that it is evident or was conceded. Refute the backing only if it is equivalent to the denial.
  - To naqḍ: refute the witness, accept the consequence ("biting the bullet"), or give another proof.
- **Endings.** *Ilzām*, the claimant forces the questioner to concede, or *ifḥām*, the questioner refutes the claimant. The burden of proof lies on the claimant [10].
- **Other terms.** The glossary also names digression (*intiqāl*), confusing brevity (*ījāz*), wordiness that loses the issue (*iṭnāb*), the point of dispute (*maḥall al-nizāʿ*), and asking for a quotation or proof to be verified (*muṭālaba bi-taṣḥīḥ*) [11].
- **Faithful in chat?** High. The moves are explicit, finite and textual. Honest-label departures:
  - The conduct code's social parts (rank, setting) drop out.
  - A written list of premises with their status, and evidence labels, would be this skill's additions.
  - The claim that a defeated proof leaves the thesis itself unsettled would also be an addition; in the tradition the claimant's failure is simply defeat [10].
- **Roles in chat.** There are two configurations, and the assistant only ever plays one side.
  - **(a) User as claimant, assistant as questioner.**
    - Ghaṣb forbids the assistant to argue its own view except through an explicit mu'āraḍa. That is a structural guard against advisor drift and against the user adopting the AI's answer.
    - The burden of proof stays on the user, which is a form of cognitive forcing; cognitive forcing reduced over-reliance but was rated less pleasant [41].
  - **(b) Assistant as claimant, defending its earlier answer; user as questioner.**
    - The rules say what a challenge obliges. A bare denial (man') obliges the assistant to prove *that named premise*, not to concede. A charge that the proof fails (naqḍ) without a witness is mukābara and need not be accepted. If the assistant cannot support a denied premise, the honest result is ifḥām.
    - This directly targets the "are you sure?" failure: on average models flipped 46% of answers and lost 17% accuracy [25]. ChatGPT also often fails to hold correct beliefs against "absurdly invalid arguments" [26].
- **Invented premises.** The claimant's proof is written out as premises, and the questioner may attack only listed premises, so a premise the user never gave becomes visible. Asking for a quotation to be verified covers invented sources [11].
- **Multi-turn**, one move per message. **Needs:** a thesis with a proof, or an earlier assistant answer. **Tool-less:** yes.
- **Overlap:**
  - dia-elenchus: partial. Both are multi-turn and premise-based, but elenchus tests a definition and the user agrees to the premises; munāẓara tests the claimant's proof by moves, with a burden of proof.
  - dia-reductio: partial. Naqḍ, "the same proof yields a falsehood", is reductio-like, but reductio is one-pass and needs a strict contradiction.
  - dia-brainstorm: partial. Stress mode also pokes holes, but it ends in options and a plan.
  - dia-refine and dia-iterate: low. Their pushback rules (cross-cutting theme 2) say what to do; munāẓara would say how.
  - dia-confirm and dia-negative: none.
- **Routing risk.** Medium. "Debate me", "challenge my argument" and "make me prove it" would pull from dia-brainstorm's stress mode and dia-elenchus. The description must name munāẓara, claimant and questioner roles, or burden of proof.
- **LLM/HCI evidence.** Debate with two expert LLMs raised non-expert human accuracy to 88% (versus 60% naive) [33]. Multi-agent debate improves factuality and reasoning [27]. No implementation of ādāb al-baḥth with LLMs was found.

## 3. Comparison

| Candidate | Fidelity achievable | Fit for AI chat | Overlap | User value | Recommendation |
|---|---|---|---|---|---|
| Munāẓara (ādāb al-baḥth) | high | high: assistant plays one side; rules counter yielding and advice drift | partial (elenchus, reductio, brainstorm-stress) | high: argue a thesis, or defend an answer under pushback | **ADD** `dia-munazara`. Its explicit moves map onto the main AI-chat risks. |
| Quaestio / article | high | medium: one model writes both sides; the determination invites over-reliance | partial (reductio, brainstorm-stress) | high: contested yes/no questions | **ADD** `dia-quaestio`. A faithful written form; needs anti-strawman and no-invented-authority rules. |
| *Sic et Non* | high (Prologue rules) | high with supplied sources; low without | partial (reductio, negative) | medium-high: conflicting sources | **ADD** `dia-sic-et-non`, or FOLD into dia-quaestio as its sources path. Distinct input and output. |
| Disputatio / quodlibet | medium | medium: the assistant judges its own debate | high with the quaestio | low as a separate skill | **FOLD** into dia-quaestio (multi-question mode). |
| Obligationes | high (one rule set) | medium: mechanical, needs visible commitments | partial (reductio *per impossibile*, elenchus) | low | **SKIP.** A logic drill. |
| Machloket / sugya / teyku | medium (literary form) | medium | partial (elenchus, negative) | medium | **FOLD** teyku and the kept minority view into dia-quaestio. |
| Havruta | low-medium (a human peer practice) | medium: the model is not a peer | partial (elenchus, brainstorm, negative) | medium | **SKIP** for now. High routing risk and a naming question. |

## 4. Ranked recommendation

**1. `dia-munazara`.**

- **Label:** "A two-role disputation after the ādāb al-baḥth wa-l-munāẓara of al-Samarqandī as summarised in Ṭaşköprüzāde's handbook. It keeps the claimant and questioner roles, the claimant's burden of proof and the questioner's three objections. It drops the conduct code's rules of rank and setting, and adds a numbered premise list with a status per premise."
- **Steps:**
  1. Fix the roles: the user as claimant (default), or the assistant defending its named earlier answer. Fix the point of dispute.
  2. The claimant's proof is written as numbered premises and a conclusion. The questioner may first ask what a term means, or for a quotation to be verified.
  3. The questioner makes one move per message:
     - deny a named premise that is neither evident nor conceded, with or without a backing;
     - charge that the proof fails, always with a witness (the same proof yields a known falsehood, or it is circular);
     - or give a counter-argument, after which the roles switch for that argument.
  4. The claimant answers in kind: prove the premise, point out that it is evident or conceded, refute the witness, accept the consequence, or offer another proof.
  5. The premise list updates each turn: conceded, proved, or denied and unsupported.
- **Stop rule:** ilzām (the questioner has no legal move left, or concedes), ifḥām (the claimant cannot support a denied premise), or a stop signal. The record says the outcome concerns this proof, not the truth of the thesis (an addition).
- **Never:**
  - As questioner, never argue the opposite outside a counter-argument.
  - Never treat bare insistence as a counter-argument, or as a reason to concede.
  - Never add a premise the claimant did not state.
  - Never quote a source that was not supplied or opened.

**2. `dia-quaestio`.**

- **Label:** "A disputed question in the article form of Aquinas's *Summa Theologiae*: objections, *sed contra*, response, replies. Departures: the *sed contra* is a supplied source or one labelled argument, not a recalled authority; and the response may end undetermined (*teyku*, borrowed from the Talmud)."
- **Steps:**
  1. Restate the request as "Whether …?".
  2. Write two to four objections for the side the response will reject. Each rests on a different ground, is one a competent defender would make, and at least one will be partly conceded.
  3. Write one *sed contra*.
  4. Write the response: the determination, usually by distinction. It states its basis and evidence class and the observation that would change it, or it declares the question undetermined and names the balanced considerations.
  5. Reply to every objection: concede, deny or distinguish.
  6. Add a line keeping the strongest argument for the rejected side.
- **Several questions (quodlibet):** one short article each, ordered.
- **Stop rule:** one article per question. A follow-up objection gets a reply. The determination changes only when the new objection cannot be answered, not on insistence.
- **Never:** strawman objections, invented quotations or authorities, or a determination shown as settled authority.

**3. `dia-sic-et-non` (or a sources path inside dia-quaestio).**

- **Label:** "Abelard's *Sic et Non* method applied to sources the user supplies: the question, the passages arranged for and against, then the Prologue's checks for apparent conflict."
- **Steps:**
  1. State the question.
  2. Quote each supplied passage with its location under Yes or No.
  3. Test each conflicting pair against the Prologue's checks in order: authorship and corruption; retraction, reported opinion, or a view left under investigation; the same word in another sense; command, indulgence or counsel, general or specific; time and cause.
  4. Mark each pair apparent (resolved by check *k*) or real.
  5. For a real conflict, compare the support behind each side (Abelard's "stronger witnesses and greater confirmation") or leave it open.
- **Stop rule:** one pass; then the user decides.
- **Never:** quote from memory, harmonise a real conflict, or run without the sources (ask for them and stop).

## 5. Open questions for the owner

1. Is munāẓara configuration (b), the assistant defending its own answer, wanted as a skill? Or should only its rule ("a bare denial obliges proof of the named premise; a charge that the proof fails needs a witness") be folded into the existing pushback rules (README theme 2)?
2. Should dia-quaestio ask for the user's own answer before determining (cognitive forcing [41]; one extra turn), or stay one-pass?
3. Is borrowing *teyku* into a scholastic form acceptable with a label, or should "undetermined" be dropped to keep Aquinas's form pure?
4. *Sic et Non*: a separate skill (a clear trigger: conflicting sources), or a path inside dia-quaestio (fewer skills, but a mixed description)?
5. Names: should skills use transliterated non-English method names (`dia-munazara`), and is a havruta-named skill acceptable at all?
6. Seven skills already cost 1,342 o200k tokens in the Codex listing (spec D33). How many additions is the budget for?

## Sources

[1] https://plato.stanford.edu/entries/obligationes — SEP: Medieval Theories of Obligationes
[2] https://plato.stanford.edu/archives/fall2006/entries/medieval-literary — SEP (Fall 2006 archive): Literary Forms of Medieval Philosophy
[3] https://freddoso.com/courses/intro/quaestio.htm — Freddoso: The structure of a medieval quaestio
[4] https://www.newadvent.org/summa/1002.htm — Aquinas, Summa Theologiae I q.2 (New Advent, Benziger 1920 tr.)
[5] https://sourcebooks.fordham.edu/source/Abelard-SicetNon-Prologue.asp — Abelard, Sic et Non, Prologue (Medieval Sourcebook)
[6] https://plato.stanford.edu/entries/abelard — SEP: Peter Abelard
[7] https://link.springer.com/article/10.1007/s10503-012-9266-7 — Uckelman, Medieval Disputationes de obligationibus as Formal Dialogue Systems (Argumentation 27, 2013; open access)
[8] https://doi.org/10.1017/s0957423916000059 — Belhaj, Adab al-bahth wa-al-munazara: the neglected art of disputation in later medieval Islam (Arabic Sciences and Philosophy 2016), abstract
[9] https://link.springer.com/book/10.1007/978-3-030-45012-0 — Miller, Islamic Disputation Theory (Springer 2020)
[10] https://doi.org/10.22452/afkar.vol22no1.7 — Arif, The Art of Debate in Islam: Textual Analysis and Translation of Taskopruzade's Adab al-Bahth wa al-Munazarah (Afkar 2020)
[11] https://philpapers.org/archive/KARTDO.pdf — Karabela, The development of dialectic and argumentation theory in post-classical Islamic intellectual history (PhD, McGill 2010)
[12] https://munazara.ihu.edu.tr/en/introduction-to-munazara — Ibn Haldun University: Introduction to Munazara
[13] https://www.sefaria.org/Pirkei_Avot.5.17 — Mishnah Avot 5:17 (Sefaria, Kulp tr.)
[14] https://www.sefaria.org/Eruvin.13b.10-11 — Babylonian Talmud Eruvin 13b:10-11 (Sefaria, William Davidson ed.)
[15] https://www.sefaria.org/Taanit.7a.8-10 — Babylonian Talmud Taanit 7a:8-10 (Sefaria, William Davidson ed.)
[16] https://olgaweijers.com/book/part-iii-3-disputation-techniques — Weijers: Disputation techniques (incl. In Search of the Truth, Brepols 2013, contents)
[17] https://booksof.louisjacobs.org/book/teyku — Jacobs, Teyku: The Unsolved Problem in the Babylonian Talmud (1981), introduction
[19] https://scholarworks.brandeis.edu/view/pdfCoverPage?download=true&filePid=13466309550001921&instCode=01BRAND_INST — Kent, Interactive Text Study and the Co-Construction of Meaning: Havruta in the DeLeT Beit Midrash (PhD, Brandeis 2008)
[20] https://as.nyu.edu/content/dam/nyu-as/faculty/documents/ThematizationDialectics.pdf — Rubenstein, The Thematization of Dialectics in Bavli Aggada (JJS 2003)
[21] https://www.sefaria.org/Bava_Metzia.84a.17 — Babylonian Talmud Bava Metzia 84a:17 (Sefaria, William Davidson ed.)
[22] https://www.sefaria.org/Berakhot.63b.12 — Babylonian Talmud Berakhot 63b:12 (Sefaria)
[23] https://www.studylight.org/encyclopedias/eng/tje/d/dialectics-rabbinical.html — Jewish Encyclopedia (1901-06): Dialectics, Rabbinical
[24] https://arxiv.org/abs/2310.13548 — Sharma et al., Towards Understanding Sycophancy in Language Models
[25] https://arxiv.org/abs/2311.08596 — Laban et al., Are You Sure? The FlipFlop Experiment
[26] https://arxiv.org/abs/2305.13160 — Wang et al., Can ChatGPT Defend its Belief in Truth? (EMNLP-23 Findings)
[27] https://arxiv.org/abs/2305.14325 — Du et al., Improving Factuality and Reasoning through Multiagent Debate
[28] https://arxiv.org/html/2503.14263v1 — Conversational Agents as Catalysts for Critical Thinking (CHI EA 2025)
[29] https://aclanthology.org/2025.naacl-srw.44 — LLM Debate Opponent: Counter-argument Generation focusing on Implicit and Critical Premises (NAACL SRW 2025)
[30] https://ceur-ws.org/Vol-3822/short3.pdf — Snaith & Wells, Formal Dialogue and Large Language Models (CEUR 3822)
[31] https://arxiv.org/html/2603.25187 — Probing the Lack of Stable Internal Beliefs in LLMs
[32] https://doi.org/10.1145/3640543.3645199 — Chiang et al., Enhancing AI-Assisted Group Decision Making through LLM-Powered Devil's Advocate (IUI 2024)
[33] https://arxiv.org/abs/2402.06782 — Khan et al., Debating with More Persuasive LLMs Leads to More Truthful Answers
[34] https://www.sefaria.org/Pirkei_Avot.5.7 — Mishnah Avot 5:7 (Sefaria, Kulp tr.)
[35] https://www.sefaria.org/Mishnah_Eduyot.1.5-6 — Mishnah Eduyot 1:5-6 (Sefaria, Kulp tr.)
[36] https://en.wikisource.org/wiki/A_Dictionary_of_the_Targumim,_the_Talmud_Babli_and_Yerushalmi,_and_the_Midrashic_Literature/%D7%A7%D7%A9%D7%99%D7%90_-_%D7%A7%D7%A9%D7%A7%D7%A9 — Jastrow, Dictionary of the Targumim, Talmud and Midrashic Literature: qashya
[37] https://doi.org/10.1163/9789004277311_009 — Brodsky, From Disagreement to Talmudic Discourse (Brill 2014), abstract
[38] https://brill.com/edcollbook/title/7493 — Schabel (ed.), Theological Quodlibeta in the Middle Ages: The Thirteenth Century (Brill), publisher page
[39] https://arxiv.org/abs/2403.08319 — Xu et al., Knowledge Conflicts for LLMs: A Survey (EMNLP 2024)
[40] https://www.nature.com/articles/s41598-023-41032-5 — Walters & Wilder, Fabrication and errors in the bibliographic citations generated by ChatGPT (Sci Rep 2023)
[41] https://arxiv.org/abs/2102.09692 — Bucinca et al., To Trust or to Think: Cognitive Forcing Functions Can Reduce Overreliance on AI (CSCW 2021)
[42] https://arxiv.org/abs/2305.19118 — Liang et al., Encouraging Divergent Thinking in LLMs through Multi-Agent Debate
