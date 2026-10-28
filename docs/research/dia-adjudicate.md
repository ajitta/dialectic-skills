# dia-adjudicate and the dia-ratchet rename: design session record

Record of one design session (2026-10-28) that started from a question about two review methods, ran a series of small multi-agent trials, and ended with a new skill, `dia-adjudicate`, and the rename of `dia-iterate` to `dia-ratchet` (spec D39, D40). Built on branch `adjudicate-ratchet`; not merged.

Everything below was run by one assistant session (Claude Opus 5.5 in the Claude app, with web search, web fetch and a shell) that started subagents. Critic and verifier agents ran on the session model; judge agents ran on the `sonnet` model alias. Web pages reached the agents through a fetch tool that returns a model's summary of the page, not the raw page; this matters for several findings. Every trial is n=1 or n=2. Numbers are counts from these runs, not rates.

## 1. The starting question

The owner asked how two methods differ: verifying an output with an **independent agent**, and criticising it with an **adversarial agent**.

- An independent verifier asks "is each claim supported?" It works inside the target's own claims, rules item by item, and credits what is right. It tends to miss what the target's framing leaves out.
- An adversarial critic asks "if the conclusion were wrong, why?" It brings outside counter-evidence and finds omissions, but inflates severity and states findings without the conditions they need.

Background checked during the session (each paper's abstract was fetched):

- Correlated errors: on the HELM leaderboard, model pairs agree on about 60% of the items both get wrong; errors correlate more for the same provider, the same architecture and for more accurate models, and an LLM judge inflates the accuracy of models whose errors it shares (arXiv:2506.07962).
- Critic models: trained critics caught more bugs than paid contractors but also produced hallucinated bugs; human-plus-critic teams hallucinated less (arXiv:2407.00215).
- Self-correction: without external feedback, LLMs struggle to correct their own reasoning, and performance sometimes drops (Huang et al., ICLR 2024, arXiv:2310.01798).
- Multi-agent debate improves factuality and reasoning on several tasks (Du et al., arXiv:2305.14325); a consensus method, different in aim from both methods above.

## 2. Trials before the skill

### 2.1 Test text 1: coffee

A short paragraph written by the assistant with planted errors: Poole et al. 2017 (BMJ umbrella review) cited for "3–4 cups a day is good for health"; a caffeine half-life calculation (200 mg at 2 pm leaves "about 25 mg" at 11 pm; recomputed 57.4 mg); "no effect on sleep"; FDA "400 mg a day is generally safe for healthy adults"; conclusion "every adult should aim for 4 cups". Planted: the calculation, the unsupported sleep claim, association read as causation, the dropped exceptions (pregnancy, fracture risk in women), a safety ceiling turned into a target. One unplanted error surfaced later: the FDA page says "most adults", not "healthy adults" (the assistant had written it from memory).

### 2.2 Trial A: one independent verifier and one adversarial critic

| | Verifier | Critic |
|---|---|---|
| Five planted errors | all | all |
| Credited correct citations | yes | no |
| Named its own unchecked items | yes | no |
| Noted that Drake et al. 2013 (400 mg six hours before bed) does not match the text's case (200 mg nine hours before) | yes | no |
| Brought new outside evidence (Mendelian randomization, CYP1A2, cumulative intake) | no | yes |
| Severity | none | inflated ("fatal" for the calculation) |

The critic's new evidence checked out in the sources the assistant opened; its interpretation ("the basis of the conclusion disappears") overreached.

### 2.3 Trial B: three adversarial critics and one judge

Three critics with the same prompt, then one judge (different model) on the anonymized, shuffled reports.

- The critics found nearly the same issues; each added only peripheral evidence of its own.
- **All three made the same error**: each applied Drake et al. without the condition difference. A majority vote would have endorsed it. This is the correlated-error prediction in miniature.
- The judge recalibrated severities, caught the shared Drake error and several single-report errors.
- The judge also erred: it marked "after adjusting for smoking, the pregnancy risk remained" as unverifiable, though the BMJ abstract says harmful associations were largely nullified by smoking adjustment "except in pregnancy".

### 2.4 Trial C: one critic, one verifier, one judge

The trial A reports, judged by a fresh judge. Breadth was similar to trial B, but the verifier had already flagged the Drake mismatch and credited correct items, so the two reports' errors were complementary rather than shared. The judge erred once: it "corrected" a report's "should possibly be excluded" (women at increased fracture risk) as too strong, while the BMJ abstract uses that wording. The two judges (B and C) also named different "decisive" issues.

### 2.5 Trial D: a critic that loads a dia skill

An adversarial agent told to attack the text with `dia-warrant` (loaded through the host's skill tool, by its own report). It was the most calibrated critic and the only agent, in any trial, to flag the FDA misquotation ("healthy adults" for "most adults"), which the verifier and both judges had passed as correct. It brought no new outside evidence and left the ceiling-versus-target arithmetic as an open question.

### 2.6 Trial E: the unknowns plugin's independent-reviewer as verifier

The unknowns plugin has no critic-shaped skill; its `independent-reviewer` agent is a verifier built for work with a plan and done criteria. Given only the text and a claim list, it reported conformance as not judgeable (expected), then gave the most usable output: per-issue failure scenarios, fixes and a full not-verified list, and it found the caffeine half-life range from a National Academies source. It missed the FDA misquotation (although it quoted "most adults" itself), applied Drake without the condition difference, and read "harmful associations reduced by smoking adjustment" as weakening the beneficial association.

### 2.7 What the trials suggested

- More copies of the same critic add little breadth and replicate errors; agreement between them is not evidence.
- Different roles or instructions (verifier, critic, dia-warrant, independent-reviewer) missed different things: their errors did not overlap.
- Judges add precision (severity, condition mismatches, misquotations) but err themselves, in recognisable places.

## 3. Where a judge skill belongs

Neither plugin had one. dia was chosen: the judge's rules are of the same family as dia-refine and dia-iterate (confirmed-only changes, "unverifiable is not false", evidence classes), and the trials judged plain texts with no plan, where the unknowns workflow's conformance checks do not apply. dia-refine's rule against subagents concerns checking one's own work; a judge ruling on others' reports, possibly in a separate agent or on a different model, is consistent with it. The orchestration (starting critics, verifiers and judges) fits unknowns better and was left for later, because cross-plugin references break when only one plugin is installed.

## 4. The judge skill, draft by draft

Each draft was tested by judge agents that read the draft file and followed it. The rule each draft added is listed with the failure that prompted it.

| Draft | Added | Prompted by |
|---|---|---|
| v0.1 | Overturning needs the source's words; unverifiable is not false (record where you looked); claim inventory of the target before reading reports; quotations to the letter; condition fit; severity by effect on the conclusion; agreement is not evidence; must-check list | Trials B and C |
| v0.2 | The quoted span must address the report's own point (search the report's key terms); summarized fetches flagged; must-check list built mechanically from the tables; material errors only | v0.1: an overturn quoted a neighbouring passage; a nitpick ("95 mg" fits under 400 mg, but "exactly 100") was listed as an error |
| v0.3 | Not found is not false, and claims about a person's position need a search beyond the cited document; one reading of the target throughout; consistency check; two-tier must-check list; optional second run | v0.2: both runs faulted one report on a premise they rejected in another; three of four judges so far ruled "the authors do not recommend coffee" wrong because the paper does not say it, while the lead author said so in an interview (Healio, checked) |
| v0.4 | With a summarizing fetch, put the report's claim to the tool as a direct question before overturning; summaries alone cap an overturn at "unverifiable"; running twice recommended | v0.3 on test text 2: correct report items overturned because the summary omitted the supporting sentence or kept a neighbouring one |
| v0.5 | Every overturn goes into the tables and the must-check list, wherever it is stated | v0.4: a judgment stated only in prose escaped the must-check list |
| v0.6 | A report that misstates its own cited source is always listed, even when immaterial (the quotation rule wins over "material errors only") | v0.5 on seeded reports: a wrong date attributed to a source was noted but not listed |

The shipped skill (1.0.0) is v0.6 adapted to this repository's rules: every tool use is conditional, a "Without tools" section and a marker rule for a load without the first word were added, running twice is conditional on the host allowing it, and the description follows spec §7.2's convention for explicit-only skills.

Two test-design faults were found and fixed during the drafts:

- v0.1 used the trial's own misquotations ("healthy adults" for "most adults", "should" for "possibly") as rule examples, so its catch of the FDA misquotation cannot be credited to the rule. From v0.2 the examples are unrelated to any test text, and each draft was searched for test-specific words before a run.
- The v0.4 draft's first example ("found X in most cases") resembled a test item; it was replaced before the run.

### 4.1 Test text 1 (coffee): judges on the three critics' reports

| Failure | Judge without skill | v0.1 | v0.2 ① | v0.2 ② | v0.3 ① | v0.3 ② |
|---|---|---|---|---|---|---|
| FDA misquotation missed | missed | caught (example leak) | caught | caught | caught | caught |
| Not found taken as false ("authors do not recommend") | wrong | wrong | wrong | right | right | right |
| Same premise used and rejected | – | – | yes | yes | no | no |
| Nitpick or off-point overturn | – | yes | no | no | no | no |
| Source-stated claim left unverifiable (pregnancy and smoking) | yes | no | no | – | no | yes (not ruled wrong) |
| Must-check rows | – | 6 | 14 | 23 | 5 | 7 |

### 4.2 Test text 2: the 4% withdrawal rule

A paragraph with seven planted errors: Bengen (1994) misdescribed (100% stocks instead of 50–75%; "over 50 years in any period" instead of at least 33 years on a 30-year plan, with 50 years for 3%), the Fed's goal as 3% (it is 2%, PCE), raising withdrawals by the target instead of actual inflation, the rule of 72 at 7% as about 12 years (10.3), "no worry about the principal" (sequence risk), "Bengen has repeatedly recommended 4% as safe for everyone" (his 2025 update to about 4.7% says the universal rate was too safe for many), and "everyone, for life". Three fresh critics wrote the reports; several of their correct items look wrong at first sight (Bengen did call 50/50 "near-optimum" while advising close to 75% stocks; 4% did last 50 years or more "in most cases").

| Report item (truth) | v0.3 ① | v0.3 ② | v0.4 ① | v0.4 ② |
|---|---|---|---|---|
| "4% mostly lasted 50+ years" (correct) | ruled baseless | unverifiable | confirmed | confirmed |
| "Bengen thought 50/50 near-optimum" (correct) | not ruled | ruled wrong | not overturned | confirmed |
| "Bengen's view is the opposite of the text's" (correct) | valid | ruled overstated | valid | valid |
| "50 years was the 3% result" (half wrong) | accepted | accepted | flagged | flagged |
| "Pfau (2010), 19 countries" (conflates the 17-country 2010 paper and a later 19-country article) | caught | caught | caught | noted, not listed |

All four runs found all seven planted errors in the text. Every wrong overturn by a v0.3 judge was in its must-check list, and the items on which the two v0.3 runs differed included every one of those errors.

### 4.3 Test text 3: Moore's law (generalization)

A domain not used to write any rule: the 1965 paper misdated to 18 months (it projected doubling every year; 18 months was Intel's David House, about performance), "never wrong" (revised in 1975; slower since about 2010), two-year doubling over ten years as 16 times (32), clock speed rising with transistor count (Dennard scaling ended about 2005–2007; clocks stalled), "Moore said it would continue forever" (2005: "It can't continue forever"), and "no need to optimize". Three fresh critics; their items were nearly all correct, so the test mainly asked whether a v0.5 judge overturns correct items.

Both v0.5 runs found all six planted errors, overturned no correct report item, confirmed a correct figure that one of its two cited sources did not contain (single-core growth 23% to about 7% per year, found in another source), left one unconfirmable figure "unverifiable", and routed every overturn to the must-check list. They differed on two judgement calls, both in the must-check lists.

### 4.4 Seeded reports (v0.5)

Three reports written by the assistant on test text 3, with fifteen items: eight wrong (a wrong date attributed to a source, the 18 months attributed to Moore in two reports, a wrong calculation, "the 1965 paper does not exist", an invented quotation, two people's positions swapped, a single example generalized to "all programs, on average", an inflated severity) and seven correct, including one that looks wrong, one whose number is right but absent from its cited source, and one that contradicts a wrong item in another report.

Both runs named the error in every wrong item and overturned no correct item; the shared wrong item was ruled wrong in both reports, and the invented quotation was refuted with the real one. One exception: one run noted the wrong date but kept that issue "valid" and did not list it as an error, because "material errors only" outranked the quotation rule; v0.6 fixes that.

### 4.5 Cost

A judge run took about 90,000 to 115,000 tokens and 2 to 5 minutes; a critic run about 75,000 tokens and 1 to 2 minutes.

## 5. Lessons the skill encodes

- A judge's own errors concentrate in overturns and in "unverifiable" rulings on points the conclusion needs. The skill does not aim for a judge that never errs, but for one whose errors land where a person will look: the must-check list, and the items on which two runs differ.
- Overturning on the absence of a sentence, or on a neighbouring sentence, was the commonest judge error. With a summarizing fetch tool it is structural: the summary drops sentences. Asking the source the report's claim as a direct question fixed it in these trials.
- Two runs disagreeing is a cheap, effective pointer: in the trials the minority verdict was sometimes the correct one.

## 6. The rename: dia-iterate to dia-ratchet

The difference between dia-refine and dia-iterate is not how many passes they make but what counts as a basis for a change: dia-refine accepts its own re-derivation of logic and calculations; dia-iterate accepts only outside evidence (a tool that ran, or the user's material), and its repetition is a consequence of that gate (without tools it usually stops after round 1). "Iterate" names the incidental feature and suggests the self-judged loop the skill guards against. Candidates weighed: `dia-ratchet` (moves forward only on confirmed evidence, locks what passed, stops on regression; a metaphor that may be unfamiliar to non-native readers), `dia-verify` (plain, but reads as check-only and collides with the judge's role), `dia-gated` (an adjective). `dia-ratchet` was chosen; dia-refine keeps its name. Both descriptions now lead with their evidence basis. The owner noted that only he and a few acquaintances use the plugin, so no alias is kept.

## 7. Limits

- n=1 or n=2 per cell, on three short texts in three domains; the test texts, the answer keys and the seeded reports were written by the same assistant that designed the skill.
- All agents were Claude models; the judges were a different model from the critics but the same provider, so error correlation is reduced at best, not removed.
- The answer keys were checked through the same summarizing fetch tool the agents used.
- The seeded errors were clean, checkable facts on public pages. Paywalled figures and subtly wrong interpretations were not tested.
- The drafts were tested as a file the agents read. The shipped 1.0.0 was then run once as an installed plugin skill on the seeded-report test (probes Part R, n=2, search summaries only, since the fetch tool was blocked there): it loaded by first word both times and overturned no correct item. No other routing probes were run for dia-adjudicate, and none for the edited descriptions of dia-refine, dia-ratchet and dia-menu.

## 8. Sources

Checked in this session (abstracts or pages fetched through a summarizing tool):

- Correlated Errors in Large Language Models: https://arxiv.org/html/2506.07962v1
- LLM Critics Help Catch LLM Bugs: https://arxiv.org/abs/2407.00215
- Huang et al., Large Language Models Cannot Self-Correct Reasoning Yet: https://arxiv.org/abs/2310.01798v2
- Du et al., Improving Factuality and Reasoning in Language Models through Multiagent Debate: https://arxiv.org/abs/2305.14325v1
- Poole et al. 2017, BMJ umbrella review of coffee: https://www.bmj.com/content/359/bmj.j5024
- FDA, Spilling the Beans: https://www.fda.gov/consumers/consumer-updates/spilling-beans-how-much-caffeine-too-much
- Healio interview with Poole (2017): https://www.healio.com/internal-medicine/nutrition-and-fitness/news/online/%7B2fb24efd-7107-46e5-9917-e108d95be838%7D/coffee-more-likely-to-benefit-than-harm-health
- Nordestgaard and Nordestgaard 2016, Mendelian randomization: https://paperity.org/p/90687617/coffee-intake-cardiovascular-disease-and-all-cause-mortality-observational-and-mendelian
- Bengen 1994, summary: https://robberger.com/research/determining-withdrawal-rates-using-historical-data
- Bengen's 2025 update: https://www.advisorperspectives.com/articles/2025/08/29/bill-bengen-boosts-the-4-rule-to-4-7 and https://wtop.com/news/2026/07/the-4-rule-no-longer-works-for-retirees-says-the-man-who-invented-it/
- Pfau, international safe withdrawal rates: https://retirementresearcher.com/the-shocking-international-experience-of-the-4-rule/ and https://robberger.com/research/an-international-perspective-on-safe-withdrawal-rates-the-demise-of-the-4-percent-rule
- Federal Reserve, Statement on Longer-Run Goals: https://www.federalreserve.gov/monetarypolicy/2026-07-mpr-statement.htm
- Moore's law and Dennard scaling: https://en.wikipedia.org/wiki/Moore%27s_law and https://en.wikipedia.org/wiki/Dennard_scaling
- Leiserson et al. 2020, reported: https://www.theregister.com/2020/06/05/moores_law_coding/
- Gelsinger, December 2023: https://gigazine.net/gsc_news/en/20231226-moores-law-intel-ceo
