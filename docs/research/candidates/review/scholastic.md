Verdict: SOUND WITH FIXES

Review of `scholastic.md` at `eb7ab54`. All 41 citations fetched on 2026-10-21 (Sefaria via a browser, since plain fetches returned an empty JS shell; Karabela [11] in full). Every citation is reachable and broadly supports its sentence. The weaknesses lie in carrying the sources over to chat. The munāẓara rules match Arif's translation of Ṭaşköprüzāde [10]. The document never maps them onto the existing skills, and that mapping is the part the owner accepted.

## Per-recommendation verdicts

| Recommendation | Verdict | Change |
|---|---|---|
| Munāẓara pushback rule folded into the dialogue skills (owner-accepted, from §5 Q1 and README:42) | **keep with changes** | Add the legitimacy condition. Map who holds the claimant role in each skill. Reconcile "prove the premise" with the evidence classes. Keep the existing "re-check honestly first" step. Add the backing-equivalence (sanad) rule. Exact wording is in F1–F3. |
| `dia-munazara` as a skill (§4.1) | **drop** | Near-duplicate of `dia-defend` (asian.md). Its user-as-claimant slot now goes to `dia-conjecture`, and "challenge my argument" falls inside `dia-warrant`'s triggers. The claim that the assistant plays only one side fails once muʿāraḍa switches the roles (F6). |
| `dia-quaestio` (§4.2), with the disputatio/quodlibet and teyku folds | **drop** | Cluster 3 goes to `dia-counterplan`. One model writes both sides and then gives a verdict. The label omits most of its departures, and step 6 is undefined when the result is "undetermined" (F7). The folds into it become moot. |
| `dia-sic-et-non` (§4.3) | **keep with changes, as a later candidate** | The most distinct candidate in the document (no sibling owns conflicting supplied sources). But the sketch gives the assistant the harmonising that Abelard left to the reader, misstates the Prologue's order, and drops its charitable presumption (F8). |
| SKIP obligationes, havruta, pilpul | keep | One factual slip in the obligationes reasoning (F9). |

## Findings

**F1 (high). As written, the accepted fold contradicts dia-elenchus and leaves the roles undefined.**
- The fold is summarised as "a bare denial obliges proof of the named premise; a charge without a witness is obstinacy" (README:42; scholastic.md:229). That drops the source's condition. Arif [10]: munāqaḍa "would be legitimate only if the premise is neither evidently true nor conceded by both parties."
- Without the condition, the fold is unfaithful. With it, applied to "all dialogue skills", it forbids the user to deny a premise they conceded, which contradicts dia-elenchus/SKILL.md:88: "The user may withdraw a premise instead of the definition. That is their call."
- No role mapping per skill. In elenchus, brainstorm, conjecture and defend the user is claimant, so what binds the assistant is the ghaṣb ban (no usurping the claimant's role). In reductio and negative the assistant's derivation is a naqḍ whose contradiction is the witness, so a user disputing a step is attacking that witness.
- Correction: write the rule per role.
  - (i) When the assistant asserts something (an [A] premise, a finding, its own earlier answer) and the user denies a premise that is neither evident nor conceded, give its support with its evidence class, or mark everything that depends on it as conditional.
  - (ii) A premise the user stated or agreed to is answered by quoting it. In dia-elenchus the user may still withdraw it, and that counts as a revision (keep line 88).
  - (iii) A rejection of a conclusion or step that names no defect and gives no counter-case is not a reason to withdraw, but the assistant still re-checks it.
  - (iv) As questioner, never argue the opposite thesis except as a labelled counter-argument.

**F2 (high). "Prove the premise" is not reconciled with the repo's rule that recall is not verification. Both yielding and entrenchment remain open.**
- Without tools, the assistant's "proof" of an empirical premise is usually recall, and recall is never "verified" here (dia-reductio/SKILL.md:34; dia-negative/SKILL.md:36). Configuration (b) (lines 154-156) then fails one of two ways: every bare denial of a factual premise ends in ifḥām (new yielding), or the assistant calls its premise "evident" or its recall proof (entrenchment).
- The document weighs only yielding ([25][26]). FlipFlop shows flips after "Are you sure?" on classification tasks; it does not show that burden rules fix them.
- The mukābara rule ("need not be accepted") omits the re-check the siblings require: "check it honestly" (elenchus:88), "check it" (reductio:123), "recheck it" (negative:105). Without it, wrong answers harden whenever the user is right but cannot name a witness. asian.md §5 Q3 flags this risk; scholastic.md does not.
- Correction: "proof" means support with its evidence class (quote, supplied material, re-derivation, or labelled recall). Recall-only support makes everything that depends on it conditional, neither a concession nor a win. "Evident" covers only logic, definitions the user stated, and what is already in the chat. Re-check every challenge before the burden rule applies.

**F3 (medium). The sketch drops a rule the source calls "important and subtle".**
- §2.6 states the sanad-equivalence rule (scholastic.md:142). The §4.1 step 4 reply list (line 192) leaves it out.
- Arif [10]: the claimant should refute the questioner's backing "only if it can be shown to be logically equivalent (musāwī) to the denial", because the questioner "may legitimately respond that the corroboration … is only one of several possible reasons, and the claimant would still be bound to establish the premise."
- In chat this is the rule that stops the assistant "winning" by knocking down the user's stated reason without supporting its own premise.
- Correction: add to the fold and to any sketch: "Refuting the user's reason for doubting a premise does not support the premise; support it, or mark it conditional."

**F4 (medium). The status of theme 2 is wrong, and so is where the pushback rules live.**
- scholastic.md:163 credits pushback rules ("theme 2") to dia-refine and dia-iterate; neither has one (grep for dispute, disagree, insist, withdraw). They are in elenchus:88, brainstorm:107, reductio:123 and negative:105.
- README:42 calls theme 2 "open"; `docs/research/README.md:33` lists it as applied (spec D19). The fold therefore refines existing rules, and the document never states what it adds.
- Correction: state the delta. It is (a) a premise denial shifts the burden only for non-evident, unconceded premises; (b) the sanad-equivalence rule; (c) the ban on usurping the claimant's role (ghaṣb). Name the four target skills plus the new accepted ones (conjecture, counterplan), and use one wording. counterplan's "only when the user supplies a fact" (argumentation.md §5) is a different standard from conjecture's "without naming a defect".

**F5 (medium). LLM/HCI studies are cited for more than they show.**
- [33] Khan: two debaters who "possess the necessary information" the judge lacks. argumentation.md §2.9 rejects carrying this over to one assistant; here it is munāẓara "evidence" (line 166) without a caveat. [27] (several model instances) has the same problem.
- [32] Chiang: a group devil's advocate "that argue[s] against the AI model's decision recommendation". It is cited for the quaestio (line 46), where the assistant argues for its own determination, the opposite direction. [28] reports group satisfaction only.
- [41] tested interface interventions. "The burden of proof … is a form of cognitive forcing" (line 153) is an interpretation.
- munāẓara's "Fit: high" (§3) has no direct evidence; the document says "No implementation … was found".
- Correction: caveat [27][33] as different setups, label [28][32] as group analogues, and mark the fit ratings as design inference.

**F6 (medium). dia-munazara: the one-side claim fails, and the overlap is understated.**
- Line 150: "the assistant only ever plays one side". Under muʿāraḍa "the roles then switch" (line 140). In configuration (a), the assistant as questioner can put forward its own counter-thesis at any time and defend it. That brings back the advice-drift and over-reliance that ghaṣb is credited with blocking (line 152).
- Overlap:
  - dia-defend (asian.md §4) has the same roles and the same reverse mode.
  - dia-conjecture has the user as claimant who rules on objections.
  - dia-warrant: "challenge my argument" (line 165) is a "what is wrong with this argument" request (README cluster 1).
- Correction: drop the skill. Keep the rule (F1–F3).

**F7 (medium). dia-quaestio: unlabelled departures, a logic gap, an unsourced claim.**
- The label (line 203) names two departures; the sketch adds four unlabelled: a quota of one partly conceded objection (line 206, which risks false balance), the rejected side's best argument (line 210), basis, evidence class and what would change it (line 208), and ordered quodlibet articles. Fidelity "high" (§3) is overrated.
- Steps 2 and 6 rely on "the side the response will reject", which is undefined when step 4 ends "undetermined".
- Line 33 ("Writing the objections before the answer helps a little") has no source and no `[unverified]` tag (cf. line 3). The form fixes the answer first: Freddoso [3] has objections "to the position that the master … will ultimately defend".
- "Argue both sides" and "pros and cons" (line 45) collide with dia-counterplan's "argue the other side".
- Correction: drop. If revived, label every departure, define steps 2 and 6 for the undetermined case, and source or tag line 33.

**F8 (medium). dia-sic-et-non: roles misassigned, Prologue misread.**
- SEP [6]: "Abelard does not attempt to harmonize these apparently inconsistent remarks." The Prologue's aim is to "lure the weaker readers to the greatest exercise of seeking the truth" (330–350), and its rules address "the reader who is eager to resolve conflicts" (188–194). The sketch has the assistant harmonise (line 67, steps 3–5). Faithful, and better against over-reliance: the assistant compiles and quotes, and the user resolves with the checks.
- "Checks in order" (step 3) starts with authorship; the Prologue starts with usage and word meaning (11–43), then attribution and corruption (54–85).
- Dropped: the charitable presumption ("we lack felicity in understanding rather than that they lack felicity in writing", 1–11), and the canonical versus later-author split (249–291), under which later works are read "with the freedom to evaluate". User-supplied sources are later authors, so this needs a label.
- Correction: the user resolves (or the assistant's resolution is labelled as the departure), follow the Prologue's order, and state that the presumption is dropped for ordinary sources.

**F9 (low). Small factual slips.**
- [29]: the title says "implicit and critical premises", not "implicit and explicit" (line 46).
- Karabela [11] dates al-Samarqandī's death "702/1302" (abstract, appendix) and "1303" (contents), not only 1303 (line 134). Karabela also gives al-Samarqandī four objection types (man', naqḍ, munāqaḍa, muʿāraḍa); the three-move list is Ṭaşköprüzāde's [10]. The label (line 184) should credit the three moves to Ṭaşköprüzāde.
- Line 97, "truth is suspended by design", contradicts Burley's rule 4 in [1]: irrelevant propositions are answered by "what we take its truth value to be".
- Line 29: in the quodlibet the students brought questions, not objections (SEP [2]: "brought forward by students rather than masters").
- Line 130 cites Eduyot 1:5 for keeping the minority view; 1:6 (same citation [35]) gives Rabbi Judah's rival reason (kept "to set it aside"), which is omitted.

**F10 (low). Wording.** Shipped text must not call the user "obstinate"; gloss mukābara neutrally ("an objection with no reason or case given"). Keep diacritics out of descriptions. No AGENTS.md breach otherwise: assistant-neutral, the one tool reference is conditional, no Hangul, every sketch runs without tools (Sic et Non stops without pasted sources).

**Missed (point 6).** No fatal objection to the fold. The material omission is F2: a win/lose burden rule must serve the stated aim, iẓhār al-ḥaqq (making the truth appear) [12], which here means re-checking plus evidence classes. Smaller: Karabela [11] gives the Latin counterpart ("a bare negation of a premise that throws the burden of proof on to the opponent", nego/concedo/distinguo), so the rule can be labelled shared scholastic/munāẓara practice. Eduyot 1:4 ("a man should not [always] persist in his opinion"), next to the cited passage, is an anti-entrenchment counterweight.

## Citation table

Statuses: S = supports, P = partly, N = does not support, U = unreachable. Five spot-checks chosen at random from the citations not behind a recommendation are marked (sc).

| # | Used for | Status | Evidence (fetched text) |
|---|---|---|---|
| 1 | obligationes rules (SKIP) | S | "consistency maintenance game" |
| 2 | quaestio and quodlibet form | S | "artificial, carefully composed imitations of disputations" |
| 3 | article structure | S | "most often a brief Scripture quote or passage from a Father" |
| 4 | ST I q.2 a.1 | S | Objection 1, sed contra with Psalm 53:2, distinction |
| 5 | Sic et Non Prologue | S | line ranges match; "stronger witnesses and greater confirmation" |
| 6 | Sic et Non | S (against sketch roles) | "Abelard does not attempt to harmonize these apparently inconsistent remarks" |
| 7 | obligationes as dialogue game | S | "Cedat tempus"; "nothing further that hinges upon winning or losing" |
| 8 | al-Samarqandī founder | S (abstract) | "a general theory of scientific discussion" |
| 9 | jadal to ādāb lineage | S | "At the end of the thirteenth century there arose a new discipline" |
| 10 | munāẓara moves, burden, endings | S | "neither evidently true nor conceded"; "sheer obstinacy (mukābarah)"; failure "will amount to his defeat" |
| 11 | roles, glossary, date | P | glossary terms present; four objection types; 702/1302 and 1303 |
| 12 | aim iẓhār al-ḥaqq | S | "manifestation of truth (iẓhār al-ḥaqq)" |
| 13 (sc) | machloket | S | "for the sake of Heaven, will in the end endure" |
| 14 | Eruvin 13b | S | "words of the living God"; Beit Shammai cited first |
| 15 | havruta | S | "sharpen one another"; "a lone stick of wood" |
| 16 (sc) | quodlibet definition | S | "the disputation on any question raised by anyone of the attenders" |
| 17 | teyku | S | "more than 300 instances"; "come and hear"; "contrived nature of the … sugya" |
| 19 | havruta practices | S | six practices in pairs; "the third partner -- the text" |
| 20 (sc) | Stammaitic pseudo-dialogue | S | "the rhetorical and … pseudo-dialogue" |
| 21 | BM 84a | S | "twenty-four difficulties" |
| 22 | Berakhot 63b | S | "A sword … who sit alone [bad bevad]" ("sharpen" is in [15]) |
| 23 (sc) | pilpul dropped | S | "degenerated into sophistry" |
| 24 | sycophancy | S | "match user beliefs over truthful ones" |
| 25 | FlipFlop | S (classification tasks) | 46% flips, 17% drop |
| 26 | defending beliefs | S | "absurdly invalid arguments" |
| 27 | multi-agent debate | P | multiple model instances |
| 28 | DA in groups | P | four-person groups; satisfaction |
| 29 | counter-argument generation | P | "implicit and critical premises" (misquoted) |
| 30 | dialogue games and LLMs | S | "regulate dialogical utterances generated by an LLM" |
| 31 | commitments in context | P | 20-questions game; an analogy |
| 32 | LLM devil's advocate | P | group DA against the AI recommendation |
| 33 | debate accuracy | P | 88% vs 60%; information asymmetry |
| 34 | Avot 5:7 | S | "I have not heard … acknowledges the truth" |
| 35 | Eduyot 1:5-6 | S | 1:5 minority kept "it may depend on him"; 1:6 omitted |
| 36 (sc) | Jastrow qashya | S | "open to objection; … contradiction" |
| 37 | sugya form | S (abstract) | "a statement with a support, followed by a challenge" |
| 38 | theological quodlibeta | S | "ca. 1230-1330 … 'about anything'" |
| 39 | knowledge conflicts | S (abstract) | "inter-context" conflict |
| 40 | fabricated citations | S | 55% / 18% fabricated |
| 41 | over-reliance | S; P for "burden = cognitive forcing" | "least favorable subjective ratings" |
| 42 | DoT; judge bias | S (DoT); P (self-judging) | DoT; judge prefers "the same LLM as the backbone" |

No citation was unreachable or failed to support its sentence outright. Gap in numbering: [18] is not used, so there are 41 sources.
