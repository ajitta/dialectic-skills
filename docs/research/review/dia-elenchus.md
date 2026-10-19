# Review: docs/research/dia-elenchus.md

Verdict: **SOUND WITH FIXES.** The citations are mostly accurate: every Perseus locus I fetched exists and says roughly what the document claims, and all the LLM-paper numbers check out. Section 7 identifies real issues. However, four proposals would introduce wrong or inconsistent text if applied as written (F1, F2, F3, F13). Two fidelity verdicts are overstated (F5/A11, A9). The document also never notes that its proposals conflict with spec §5.2.

Method: I read the skill files with line numbers and diffed them against upstream. I fetched all 40 Perseus URLs, SEP, IEP, Wolfsdorf, BMCR and the 14 LLM/vendor sources. Document length: 427 lines (OK, <= 500). SKILL.md: 113 lines. Description: 795 chars. No Hangul.

## 1. Per-finding verdicts (section 7)

**F1 "ideas born" layer, high: partly.** The problem is real. See description l.3, SKILL l.23, patterns l.50, record l.20-21. 10-two-skills.md §1 confirms the layer came from socratic-brainstorm 2.0.0. Theaetetus 210b is quoted correctly ("all the offspring that have been born are mere wind-eggs and not worth rearing"). Changes needed:
- The proposed l.23 text says "in the dialogues a fallen definition is simply discarded (Theaetetus 210b)". That is false for the early dialogues, where definitions are emended rather than discarded:
  - Euthyphro 9d: "shall we now emend our definition and say that whatever all the gods hate is unholy and whatever they all love is holy ...?"
  - Laches 192d: "So, by your account, wise endurance will be courage."

  The text also cites Theaetetus as the authority for "the dialogues", which contradicts the skill's own l.14 ("aids, not the method").
- The proposal is incomplete. It leaves several "birth" and "idea" phrasings in place:
  - the Step 5 heading, l.90 ("A revision is a new idea");
  - l.92 ("That shift is an idea the user just gave birth to; keep a list");
  - patterns l.42 ("Noticing a birth") and l.50 ("is not a birth");
  - record l.20-21 ("Ideas born") and l.44 ("start from the ideas born").

  A partial edit would leave the skill self-contradictory.
- The spec conflict is not flagged (see missed issue M1). Spec §5.2 defines the skill's purpose as "treat each revision as the user's new idea" and requires "Behavior: unchanged from the reference". This is an owner decision (doc §8 Q1), not a text fix. Severity should be medium until the owner decides.

**F2 l.84 overclaim, high: partly.** l.84 does say "So ① can't stand as it is", against patterns l.31 and SKILL l.86/l.111. The logical point is right: Wolfsdorf quotes Vlastos's "problem of the elenchus": "all he has proved ... is that the thesis is inconsistent with the conjunction of agreed upon premises". But:
- The fidelity framing is wrong. Concluding against the thesis *is* Plato's Socrates' practice (Vlastos step 5; Laches 191c: "I was to blame for your wrong answer, by putting my question wrongly"). l.84 departs from the skill's own non-constructivist stance, not from the source. A9's verdict "departs" should read "matches Socratic practice; inconsistent with l.86".
- The fix is incomplete. "Where would you change it?" also appears at patterns l.31 and as the scripted question at l.92 ("ask 'Where would you change it?' and wait"). Changing only l.84 to "Which would you change?" leaves three different scripts. Change all three together.
- Severity: medium. l.86, which explicitly allows premise withdrawal, directly follows the example.

**F3 sycophantic withdrawal, high: partly.** The risk is real. Sharma et al. (arxiv.org/html/2310.13548v4): "All LMs tend to change their initial answer (between 32% for GPT-4 and 86% for Claude 1.3 ...) and admit they made a mistake (between 42% for GPT-4 and 98% for Claude 1.3)". But:
- The line reference is wrong. Patterns l.38 is "That's not what ② meant"; the "That's a leap" handler is l.39. Inserting the text "after l.38" would put it in the wrong bullet.
- The fix belongs in SKILL.md l.86 ("check honestly; if they're right, withdraw the step"). That is the only copy guaranteed to be read: the document's own §6.2 and probes P8 show reference files are sometimes unreadable. Add one clause there; the patterns edit is optional.
- The evidence comes from 2023 models on factual QA, not argument steps. Medium-high is defensible, but say so.

**F4 "never offer a definition" stricter than Socrates, medium: partly.** The verdict is right, but the evidence should change:
- The best counter-loci are missing:
  - Euthyphro 9d, where Socrates formulates the revised definition and asks "Do you wish this now to be our definition ...?" This is exactly what l.92 forbids.
  - Laches 192d, where Socrates states "wise endurance will be courage".
- Two cited loci are weak for "early dialogues":
  - Meno 75b is transitional; the document itself says (§2.1) that Meno is not on Vlastos's list.
  - Hippias Major is where, per Wolfsdorf on Vlastos 1983, "Socrates abandons adversarial argumentation ... both proposes and criticizes his own theses".
- Euthyphro 12d proposes a genus ("holiness is a part of the right"), not a full definition.

Recommended label text: "(Stricter than Socrates, who sometimes worded the revision himself, e.g. Euthyphro 9d, Laches 192d ...)". The Laches 192b quickness move is verified ("The faculty that gets a great deal done in a little time is what I call quickness") and fits the rules.

**F5 "examine statements, not the person" departs, medium: partly (verdict overstated).** Laches 187e-188a and Apology 38a are quoted correctly. Wolfsdorf on Brickhouse & Smith 1991 ("tests not merely propositions but ... human lives") is correct. But the document omits primary texts that support the skill's rule:
- Protagoras 333c: "my first object is to test the argument, the result perhaps will be that both I, the questioner, and my respondent are brought to the test".
- Charmides 166e: "[never mind] whether it is Critias or Socrates who is being refuted: give the argument itself your attention".

The document even cites Charm. 166d [40] for another point. A11 should be "loose", not "departs". The proposed text ("Socrates examined how people lived ... You don't") is half-true. A better version: "Socrates put the argument first (Protagoras 333c, Charmides 166e), though he also tested how people lived (Laches 187e-188a); here only statements are examined." Severity: low.

**F6 irony, low: confirmed, borderline nit.** Republic 337a is verified: "the well-known irony of Socrates ... you would refuse and dissemble". l.28 already scopes itself ("Irony *here* means ..."). The proposed text is fine.

**F7 "never advise" wrong citation, low: partly.** Apology 21d supports exactly what it is attached to, "You don't know" ("what I do not know I do not think I know either"). The real issue is that "give no answers, advice" is uncited. A cleaner source than Theaetetus 150c (the "aid" dialogue) is Aristotle's report via IEP: "Socrates asked questions without supplying an answer of his own".

**F8 silent premise list, medium: partly, downgrade to low.** The premises are the user's own visible answers, so "silent" means "unprinted", not stored privately. The cited doc [54] actually says current Claude models "keep prior turns' thinking blocks in context" (Opus 4.5 and 4.6+). The first proposal sentence ("re-read the user's actual answers and number them then") is good. "Restate the current definition at the start of a premise question" adds text to every turn; it pulls against Rule 2 and duplicates the restatements in Step 2 and Step 5. Drop that clause.

**F9 "name the shift" invites interpretation, medium: partly, downgrade to low.** The cited evidence is misapplied. 09 §6's "remaining imperfection" is the model turning a *premise* into a definition ("summarized ... from an answer that was a premise, not a definition"), not shift-naming. The l.92 example already uses the user's words. The proposal is harmless and consistent with Rule 4.

**F10 no script for frustration, medium: partly.** The gap is real: patterns l.52-58 and Stance l.27 cover "I don't know" and advice requests, not irritation. There is stronger evidence the document missed: in 09 §6 Claude's retro run "answered the confusion by explaining the link". The proposed script adds a Plato anecdote ("Meno compared Socrates to a numbing sea-fish"), which reads as lecturing an annoyed user. Keep the name-it plus "keep going or stop and get the record" choice and drop the anecdote. Low-medium.

**F11 priority of definition, low: partly.** SEP is verified: "attacked as the Socratic fallacy by Peter Geach ... no text unequivocally assigns either claim to Socrates". The proposal must map the outcome to an existing label (aporia / "What we now know we don't know"). Otherwise it collides with l.100 "Don't invent other labels".

**F12 scope shift, low: confirmed.** SEP: "a claim to wisdom or to knowledge of a subject related to virtue".

**F13 label criteria only in the reference, low: partly.** The labels are at record l.38-41, not l.36-41. The proposed one-line summary drops the second aporia condition from record l.38 ("or the current one is admittedly unclear"), so SKILL.md and the template would disagree. Copy the criteria verbatim.

**F14 host study modes, low: confirmed.** The OpenAI ("Combines Socratic questioning, hints, and self-reflection prompts") and Anthropic ("What evidence supports your conclusion?") quotes are verified, and the wording is assistant-neutral.

**F15 probes missing, medium: confirmed.** docs/probes.md: P2 and P5 are "not run (owner)". Note that the P2/P5 pass conditions (spec §12.2) are about routing, not multi-turn dialogues, so the proposed scripted runs would be a new probe.

**Rule compliance of the proposals:** none uses a product name or Hangul, and none requires tools. SKILL.md would stay under 200 lines.

## 2. Citation problems

All 40 Perseus loci resolve and support their use; quoted wording matched in every case I checked (some fetches needed retries after Varnish 503s). The secondary and LLM sources also check out: SEP Socrates (the elenctic list), IEP (method sections and quotes), Wolfsdorf (Vlastos 1983a: 30 definition, the five steps, Kraut, Benson, Tarrant, Robinson), Laban ("average drop of 39%"), Li ("within eight rounds"), MathDial, LearnLM, GuideEval, Dinucu-Jianu (EMNLP 2025), Al-Hossami [45] and Paul & Elder.

Problems found:
1. [5] Brickhouse & Smith 2002. The quotation-marked phrase "there is no such thing as 'the Socratic elenchus'" is Wolfsdorf's paraphrase ("denying that there is such thing as the elenchus"). B&S's own quoted words are "The very idea of 'the Socratic elenchus' ... is an artifact of modern scholarship" (2002b: 147). Nit: it is a paraphrase in quotation marks.
2. [46] The paper's "premature" example is GPT-3.5's utterance, not GPT-4's ("premature utterances ... as seen in GPT-3.5's second utterance"). Only "too direct" is GPT-4's. Nit.
3. [1] The summary calls non-constructivism "the more defensible ... side of the scholarly debate". SEP's author says the opposite: "Vlastos has argued persuasively that elenchus in fact supports Socrates' ethical doctrine". This is the author's own judgment presented as the state of the field. Should-fix (wording).
4. [1] "as is usual for works in this group" is said of the Hippias Major. SEP states the Euthyphro and Charmides impasses separately. The attribution is fine; the quote is slightly stitched. Nit.
5. [48] "treats ... as interchangeable prompt techniques": the abstract only lists them as techniques. "Interchangeable" is an overstatement. Nit.
6. [6] BMCR: plain curl returns HTTP 500. The content loads via the extractor at the URL with a trailing slash and supports "complex ironies, statements true in one sense though false in another" and the "Does Socrates cheat?" chapter. Link flaky, claim OK.
7. Line-reference errors in the document:
   - "patterns l.37-38/l.38" should be l.39;
   - "record l.36-41" should be l.38-41;
   - §5 lists two socratic-brainstorm → dia-brainstorm pointers, but there are three: the description at l.3 also changed (verified by diff).

No dead primary links. No misquoted Stephanus numbers.

## 3. Fidelity table disagreements

- **A9:** l.84 matches Socrates' practice (Vlastos step 5; Laches 191c). It is inconsistent with the skill's own l.86/l.111, not "departs" from the source.
- **A11:** "loose", not "departs". See Protagoras 333c and Charmides 166e above.
- **A12** "matches" is too strong. Sincere assent is typical but not universal. Protagoras 333c: "It is all the same to me ... so long as you make answer, whether it be your own opinion or not." Verdict should be "matches the usual rule (Crito 49d, Gorgias 495a), not every dialogue".
- **A14:** the verdict is right, but the decisive loci are Euthyphro 9d and Laches 192d. Even the midwife reading is not clean. At Theaetetus 157c-d the midwife Socrates says he is "giving you a taste of each of the philosophical theories", so he supplies theories to test. l.23 ("you have no ideas to hand over") is stricter than the Theaetetus too. Upstream 09 §2 itself cites 157c-d.
- **A18:** see F1. Revisions in the early dialogues are emendations (Euthyphro 9d, Laches 192d), so "failed attempts at one definition" is true but not "simply discarded".

## 4. Missed issues

**M1 (should-fix).** Proposals F1, F4, F5, F7, F8, F9 and F13 change behaviour. Spec §5.2 says "Behavior: unchanged from the reference" and states the purpose as "treat each revision as the user's new idea". AGENTS.md and spec §12.1 require a new plugin `version` and skill `metadata.version` for any skill edit. The document says the rebuild "matches spec §5.2" but never says its own proposals require a spec amendment and version bumps. Evidence: docs/spec.md §5.2; AGENTS.md "Changing any skill file requires a new plugin `version`".

**M2 (should-fix).** SKILL.md l.92 forbids exactly the move Socrates makes at Euthyphro 9d ("shall we now emend our definition ...? Do you wish this now to be our definition") while the skill presents itself as the early-dialogue method (l.14). This is the strongest fidelity gap in the skill, and the document cites weaker loci for it.

**M3 (nit).** Patterns l.31 hard-codes "So ① and ② can't both stand" right under a shape that includes ③. With three premises the line should read "①-③ can't all stand".

**M4 (nit).** The description (l.3) says "Gives no advice or ideas of its own". The skill does allow labelled suggestions after the dialogue, on request (l.102-104). Adding "during the dialogue" would make it accurate.

**M5 (nit).** Step 2 (l.61) asks for a restatement "in my words so they can correct it" plus a premise question in the same message. That is an implicit second ask, in tension with Rule 1 (one ask per message). Probes have not shown harm, so it is low priority.

**M6 (nit).** The lineage section misses that upstream 09 §2 cites Theaetetus 157c-d for the midwife. The shipped skill dropped it, and it is relevant to A14 (see §3).
