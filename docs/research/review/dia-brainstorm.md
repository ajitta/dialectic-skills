# Review: docs/research/dia-brainstorm.md

Verdict: **SOUND WITH FIXES**

The research is careful. The skill's file:line references in SKILL.md are correct, the lineage diff in §5.1 is accurate (I re-ran `diff` against `upstream/superclaude-stable-47f791b/socratic-brainstorm/`: only the name, metadata, the three `socratic-elenchus` cross-references, the yaml display name and prompt, and brief-template upstream line 44 changed), and almost every quotation I fetched is verbatim. The problems are in the proposals. Four of them would introduce a new overclaim or break an existing rule if applied as written (F1, F3, F8, F14). Two have weaker evidence than stated (F7, F11). The document is 369 lines (≤ 500: pass). The SKILL.md description is 776 chars and the body 111 lines, so every proposal combined stays under the limits. No proposal adds Hangul, a tool dependency or a product name.

## 1. Per finding (section 7)

**F1 (medium): partly. Lower to low and rewrite the proposal.**
- The problem is real but small. SKILL.md:16 already labels the method honestly ("modern Socratic questioning (Richard Paul's six question types…) … not the strict method of Plato's dialogues"). The owner wrote that label on purpose (upstream `10-two-skills.md` §2, "Honest labels").
- The proposal adds a new method claim: "and guided discovery as used in cognitive therapy". The skill's lineage never drew on Padesky. `04-design.md` §1 and `02-research.md` §2 trace concreteness pull, steelman and the tactics to grammy-jiang/socratic-method, MODE_Brainstorming and socratic-mentor, and no upstream file cites Padesky. The document itself says the skill lacks two of Padesky's four stages (§2.2, F2, F3). Naming guided discovery would therefore be the kind of loose borrowing the owner objects to. Drop it, or add it only after F2 and F3 land.
- "(Paul, 1990)" would ship a date that the document marks [unverified] (§2.1, Q6). The owner's own review attributes the list to "*Critical Thinking*, Paul & Elder" (`13-review.md` §2). Either keep the citation undated or verify it first.
- Keep the useful part: Step 3 adds the assistant's own options and Step 4.3 may give a pick, unlike the midwife (Theaetetus 150c-d, verified).

**F2 (medium): partly. Lower to low.**
- The evidence holds: Padesky says "they don't summarize enough … there should be a summary every few minutes" (socquest.pdf, Stage 3).
- The proposal uses two triggers: "when an answer changes the working thesis, or every ~4 probes". The Rhythm rule (SKILL.md:69) makes moving the thesis the goal of every probe, so the first trigger would put "So far:" on most turns.
- The skill would then have three cadences: the half-budget pacing cue (:72), the deep checkpoint every ~5 probes (:33) and this one. Use a single trigger ("every ~4 probes") and merge it with the pacing cue.

**F3 (medium): partly. The template edit conflicts with an existing rule.**
- The synthesizing question is faithful to Padesky's Stage 4 (verified: "asking the client a synthesizing or analytical question which applies this new information to the client's original concern"), and it handles stop signals correctly.
- The proposed `brief-template.md:12` line, "After: <the user's restatement; your tightening…>", drops the existing clause "any live risky assumption written in as a condition". That clause backs the `risky` rule (brief-template.md:42), and it was validated in the owner's probe F (`08-implementation.md` §2: "the brief marked that belief risky and wrote the condition into the thesis"). Keep the clause.
- Also exempt `quick` depth, or this adds a turn to a ~4-probe session.

**F4 (medium): partly.**
- The evidence is verified. Bond, Carlson & Keeney: "omitted nearly half … almost as important". In their studies the omitted objectives were recovered by *recognition* from a master list, and Study 3 found that re-thinking alone did not fix the gap. A numbered list is therefore justified, and a bare "anything missing?" would not be.
- The proposal clashes with "Get 2-3 criteria in the user's words" (SKILL.md:87) and with the owner's reason for avoiding chips: offered choices anchor answers (`04-design.md` §3). Frame the list as examples ("pick any, or name your own") and record the user's wording. "Fun" is an odd fixed item.
- Low to medium is fair.

**F5 (medium): confirmed, with one gap in the evidence.**
- The citations hold: [18] (4,000 seed ideas gave 200 unique), [21], [19], [20], and [22] "no main effects of disclosure".
- The evidence omits the strongest direct support. Meincke, Nave & Terwiesch, "ChatGPT decreases idea diversity in brainstorming" (Nature Human Behaviour, Matters Arising, 14 May 2025, https://www.nature.com/articles/s41562-025-02173-x) is a published reply to the document's own [27].
- The text change is minimal and keeps the line-limit clause.

**F6 (low): confirmed.** Siebert & Keeney's abstract says that using objectives "enhances both the number and quality of created alternatives". The change is optional and harmless.

**F7 (medium): partly. Lower to low.**
- The rule is sound and fits tool-less surfaces.
- The evidence for a defect is thin. The cited example, "How many cases is that?" (question-bank.md:19, which the document gives as :20), asks about the user's own observations, which they can answer. No probe recorded a question the user could not answer.
- Put the sentence at the start of Step 2, not in Rule 1, which is already the longest rule.
- Paul and Elder's own checklist asks "How could we check that to see if it is true?" (2006 guide). "Record it under open questions as something to find out" is compatible with that.

**F8 (low): partly. The second sentence conflicts with Step 1.**
- The Pew acquiescence passage is verified.
- "What did I get wrong?" presupposes an error, which makes it a mild leading question (pitfall, SKILL.md:109). Pew's own remedy is "a choice between alternative statements", which Rule 1 already allows ("is it A or B?").
- "Never by adding parts they did not say" contradicts the steelman in SKILL.md:43, which allows assumptions as long as they are marked ("mark what you assumed versus what they said").
- The owner's probes show "맞나요?" working (`08-implementation.md` probe A).
- Suggestion: "Is that right, or did I assume something you didn't mean?" Drop the second sentence.

**F9 (medium): confirmed.** Sharma et al. and SYCON Bench ("alignment tuning amplifies sycophantic behavior", Turn of Flip and Number of Flip) are verified. The proposal is consistent with the verdict conditions at :97-99.

**F10 (low): confirmed, with a wording fix.** The first sentence of the proposed text already exists at SKILL.md:108 ("Before Step 3, ask about the user's reasoning, not your alternative."). Append only the test-versus-replace sentence. The tension with the counterexample tactic (:61) is real.

**F11 (low): partly. The evidence is under-researched.**
- question-bank.md:49 already says "asked as a question in that person's spirit". The cited lines are 48-55, not 50/51-57.
- The lenses have documented in-repo provenance. `upstream/.../02-research.md` §1 traces them to SuperClaude's panel personas (Nygard "what happens at 3AM?", Drucker, Taleb "what breaks first?"). "No source checked" missed this.
- Drucker's line is near-verbatim of a real Drucker question: "Who is the customer? … What does the customer consider value?" (*Management*, ch. 7; summarized at peterdruckerreview.com).
- The Hickey line uses Brooks's term. Hickey says "incidental complexity" (Simple Made Easy transcript); "accidental complexity" is Brooks, *No Silver Bullet* (1986). See missed issue M4.
- Full names are a good idea. "Kent Beck" is an inference, though a reasonable one given "first test".

**F12 (low): confirmed.** The Osborn rules quotation is verbatim (Diehl & Stroebe 1987, p. 497). "Three other ways" is a prompt, not a cap, so the finding is about adding one nudge. That is fine.

**F13 (low): confirmed.** One nit: the template has nine sections plus a verdict line, not "ten sections" (§6.2).

**F14 (medium): partly. Incomplete.**
- The facts are verified: probes.md:32 and :34, and spec §7.3.
- Missed: `tests/test_package.py:62` asserts `default_prompt.startswith(f"Use ${s.name} ")`, so the proposed change also needs a test change. The upstream predecessor test deliberately pinned `$<name>` (`13-review.md` M1).
- The spec's own P3 pass condition says "`$dia-<x>` resolves" (spec §12.2), yet probes.md records P3 as "pass" although `$dia-<x>` did not resolve. The spec and the probe log disagree, and the document did not flag it.
- The issue affects all seven skills, not only brainstorm.

**F15 (low): confirmed.** probes.md:58-77 has no brainstorm run, and P2 is open.

## 2. Citation problems

I fetched all 41 sources. No link is dead: [9] redirects with a 301 to the trailing-slash URL, and [8]'s PMC page returned only metadata, so I confirmed "55 depressed adults" and "the first empirical support" through the Europe PMC abstract. Quotes and numbers for [1]-[8], [10]-[13], [15]-[19], [21]-[32], [34]-[41] match their sources. The problems:

1. **[9] SEP misattribution (should-fix, fidelity).** The elenctic-dialogue list in SEP "Socrates" is presented as Vlastos's developmentalist grouping ("The evidence Vlastos uses varies … The dialogues of Plato's Socratic period, called 'elenctic dialogues'…"). It is not SEP's own classification. The document writes "The SEP entry on Socrates names…". Write "Vlastos's grouping, as reported in SEP".
2. **[27] missing published rebuttal (should-fix).** Lee & Chung (2024) now carries a Matters Arising, Meincke, Nave & Terwiesch (2025), "ChatGPT decreases idea diversity in brainstorming", plus an authors' reply. §3.1 presents [27] only as "Where models help".
3. **[41] overstated scope (nit).** The page says "When `false`, Codex won't implicitly invoke the skill". It does not say that ChatGPT honors the flag, or that it "affects only Codex and ChatGPT" (§6.3).
4. **§2.2 lineage claim (should-fix).** "The skill takes 'concreteness first' (:60) and 'no leading questions' (:109) from this family [Padesky]". The upstream design notes say otherwise (`02-research.md` §2, `04-design.md` §1: socratic-method and MODE_Brainstorming). The behaviour is consistent with Padesky, but the skill did not take it from Padesky, and F1 builds on this claim.
5. **A1 verdict "matches the 1990 list".** The source chain is Thoms (1998-99), quoting "(Paul, 1990)" at p. 270, plus EACL [5] ("Paul and Binker, 1990"). That is secondary only, as the document admits. The verdict should read "matches as attributed by secondary sources; primary unchecked".
6. **Wrong line numbers in `question-bank.md` (nit, but edits will use them).** Premortem is at :48 (cited :50). The expert lenses are at :49-55 (cited :51-57). "How many cases" is at :19 (cited :20).
7. **Minor section references.** The split of the strict method into its own skill is `10-two-skills.md` §1, not §2. "the description says so ('followed by brainstorming', SKILL.md:16)": line 16 is the body intro, not the description.

## 3. Fidelity audit (section 4) disagreements

- **A1:** see item 5 above. Downgrade to "matches (secondary attribution)".
- **A6 "matches":** loose. Padesky's (c) describes how a sequence of questions generally runs, from concrete to abstract. Concreteness pull is a reactive tactic, and the skill's usual order (A5, :47) is not concrete-to-abstract. The document rates A5 "loose" and A6 "matches", which is inconsistent.
- **A25 "unsupported":** partly wrong. Provenance exists in `02-research.md` §1 (panel personas). The Drucker line is close to a primary text, and the Hickey line mixes in Brooks's term.
- **A7:** citing [9] SEP for "elenctic moves" is fine, but see the attribution note above.
- I agree with the other verdicts. I re-checked the Theaetetus passages for A16 and A21 (150b-d, Fowler), Pew for A2 and A4, Klein for A24 and NGT for A12.

## 4. Missed issues

**M1 (should-fix): SCAMPER can run during probing when `references/` is unread.**
- SKILL.md:73 lists "Lenses (premortem, expert viewpoints, SCAMPER)" under Step 2 Rhythm.
- The restriction "SCAMPER (… in Step 3 only)" lives only in question-bank.md:56.
- Headless runs sometimes cannot open `references/` (probes.md:77). A model working from SKILL.md alone may then run SCAMPER while probing, generating alternatives before Step 3 and breaking Rule 3 (SKILL.md:22).
- Fix: change :73 to "(premortem and expert viewpoints here; SCAMPER only in Step 3)".

**M2 (nit): the switch rule says two different things.** SKILL.md:69 says that after two dry switches you "go to Step 3". question-bank.md:61 says "move to Step 3 or 5".

**M3 (nit): no instruction for Step 4 when Step 3 is skipped.** Step 3 can be skipped (SKILL.md:77), but Step 4 (:85-91) assumes there are options. The skill never says to skip Step 4 or what to put in the brief's Options and Criteria sections.

**M4 (nit, fidelity): the Hickey lens borrows Brooks's term.** question-bank.md:54 attributes "accidental complexity" to Hickey. That is Brooks's term; Hickey's is "incidental complexity". Either reword the question or attribute it to Brooks.

**M5 (nit): the brief date may be invented.** The brief template needs `<YYYY-MM-DD>` (brief-template.md:6). On a surface with no date in context the model has to invent one, which goes against "invent nothing" (SKILL.md:101). Add "if known".

**M6 (nit): routing differs between surfaces.** §6.3 notes that Claude can load the skill implicitly from "poke holes in this plan" (SKILL.md:3), while Codex cannot (`allow_implicit_invocation: false`; owner probe N1 in `08-implementation.md`). Spec §5.3 treats the skill as explicit-only. This surface difference is accepted in upstream `04-design.md` D2, but the document draws no finding or open question from it.

**M7 (process): Q5 understates the versioning rule.** The skill's behaviour stays "unchanged from the reference" (spec §5.3) only until any of F2-F9 lands. Under spec §12.1 and AGENTS.md, *any* skill-file change requires a plugin version bump and a `metadata.version` bump. That holds whether or not the change counts as "behavior", so Q5's framing of this as an open question is too soft.

## 5. Line count

`wc -l docs/research/dia-brainstorm.md` gives 369, which is within the 500-line limit.
