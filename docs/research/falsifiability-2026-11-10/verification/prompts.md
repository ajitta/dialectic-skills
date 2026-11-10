# Agent launch prompts (verification)

Verbatim first message given to each sub-agent, extracted from the session log after the fact. The serving model is the one recorded in that agent's log. Absolute paths point at the original session's scratch folder; the reports they wrote are in this folder.

## Blind falsifiability judge

Model: `claude-opus-5-5`

````text
You are an independent judge. Read-only task. Do NOT open any file under /home/claude/ (another analyst's conclusions are there and you must not see them). Do not edit or create files except one report file in /tmp/claude-0/-home-claude/543eb0e4-0af5-5b32-9fc8-3978303f9208/scratchpad/blind-report.md. Do not send any plugin text to web services; a web search with general public terms (e.g. Popper on probability statements) is allowed if you need it, and mark such facts by source.

Material: the `dia` plugin v2.11.0 at /mnt/skills/plugin-files/dia (README.md, skills/*/SKILL.md, skills/*/references/*). Read the SKILL.md files themselves; do not rely on README summaries.

Question: can each problem below be solved with the plugin's EXISTING skills (as written, used alone or in combination, including via dia-router), or does it need a NEW dia skill, a change to an existing skill, or something outside the plugin (e.g. an eval suite)? Also challenge whether each problem is real.

P1. Popper's prior refutation criterion (agree beforehand which observations would refute an empirical claim) — is it available wherever an empirical claim is tested, or only in some skills?
P2. Recording test severity (how hard a claim was tested) for results that say a claim "held".
P3. A falsifiability audit of empirical claims that are NOT strictly universal: probabilistic/statistical claims, existential claims, claims shielded by auxiliary hypotheses or open-ended terms ("the market will eventually correct"). Includes the user question "is this falsifiable?", detecting methodological immunization (the holder refuses every refutation criterion), a decision rule for probabilistic claims, and recording auxiliary hypotheses held fixed during the test.
P4. Checking whether a run of a dia skill obeyed that skill's own rules (format conformance: fixed labels, record fields, one question per message, etc.).
P5. Checking judgment-dependent rule conformance and whether the plugin improves reasoning at all (effect hypotheses).

Also test routing concretely: for each input below, decide which skill dia-router and the skill's own Step 0/Scope would send it to TODAY, and whether that skill would produce what the request needs (cite rules):
1 "이 마케팅 전략은 반증 가능한가?" 2 "모든 정렬 리스트는 이분 탐색이 된다, 반박해 봐" 3 "그 약이 효과 있다는 걸 뭘 보면 틀렸다고 할래?" 4 "결국 시장이 교정한다는 말, 반증 가능해?" 5 "숨은 패턴이 있다는 가설 반증 가능해?" 6 "이 가설 시험할 실험 설계해 줘".

Rules for your report: for every verdict give the evidence — file path plus a short quote (one clause) of the rule you rely on; distinguish what the text says from your inference; if a combination of existing skills solves a problem, say exactly how and what is still missing. Do not invent rules. Verdict per problem: "solved by existing skills" / "solved by changing existing skill(s)" / "needs new dia skill" / "belongs outside the plugin" / "not a real problem". End with an overall verdict and the single strongest argument against it.

Write the report (Markdown, English or Korean) to the scratchpad path above and also return it in full as your final message.
````

## Adversarial refuter of analysis

Model: `claude-fable-5-2`

````text
You are an adversarial reviewer. Your job is to REFUTE the conclusions of the document /home/claude/dia-falsification-skill-need.md (you may also read /home/claude/dia-falsifiability-analysis.md, the earlier analysis it builds on). Read-only: do not edit those files or the plugin. Write one report file only, at /tmp/claude-0/-home-claude/543eb0e4-0af5-5b32-9fc8-3978303f9208/scratchpad/adversary-report.md. Do not send any plugin or document text to web services; a web search with general public terms (e.g. Popper on existential statements or probability) is allowed, marked by source.

Material to check against: the `dia` plugin v2.11.0 at /mnt/skills/plugin-files/dia (skills/*/SKILL.md and skills/*/references/*). Read the actual SKILL.md text; do not trust the document's quotes.

The document concludes roughly: (가-1) spreading Popper's prior criterion and severity recording needs only changes to existing skills; (가-2) a falsifiability audit of non-universal empirical claims (probabilistic, existential, auxiliary-shielded; "is this falsifiable?"; methodological immunization) is a gap that justifies a NEW conversational dia skill (conditional on usage frequency); (나) checking that dia runs obey their rules, and testing the plugin's effects, need no new skill but an eval suite / rubric / experiments outside the plugin, with dia-adjudicate usable as a re-judge.

Attack every conclusion, strongest first:
- Show, with quotes from SKILL.md, existing skills or combinations (incl. dia-router, dia-quaestio stress mode with its falsification pull, dia-warrant rebuttal slot and critical questions, dia-conjecture prior criterion and Step 0, dia-negative rule 6 falsifier, dia-elenchus, dia-counterplan observations, dia-techne outside check) that already solve (가-2) — or show the gap is not real.
- Conversely, argue where the document is too conservative (e.g. (나) really does need a skill, or (가-1) cannot be done by small edits without breaking a skill's identity).
- Check every factual claim and quote the document makes about the plugin; list any that are wrong or overstated, with the correct SKILL.md wording (one clause) and path.
- Check the document's Popper/Lakatos/Duhem-Quine claims; flag any that are wrong.
- Check the routing-test table in §1.2 against the actual router and Step 0 rules: which rows would route differently today, and does that undermine or support the new-skill case?

Rules: every attack needs evidence (path + short quote, or a concrete counterexample); persistence is not evidence. Where an attack fails after you check, say so explicitly ("attack failed: ...") — do not hide failed attacks. Label each item: refutes / weakens / fails. End with: which of the document's conclusions survive, which fall, and your single best argument.

Write the report to the scratchpad path above and return it in full as your final message.
````

## dia-adjudicate run 1

Model: `claude-opus-5-5`

````text
dia-adjudicate

First load the skill by name with the Skill tool (skill: "dia:dia-adjudicate") and follow it in full. This is the first of two independent runs on the same input.

Target (T): the document /home/claude/dia-falsification-skill-need.md (read it in full).
Reports:
- /tmp/claude-0/-home-claude/543eb0e4-0af5-5b32-9fc8-3978303f9208/scratchpad/blind-report.md (written independently, without seeing T, on the same question T answers)
- /tmp/claude-0/-home-claude/543eb0e4-0af5-5b32-9fc8-3978303f9208/scratchpad/adversary-report.md (written as an attack on T)
Sources to check claims against: the dia plugin v2.11.0 at /mnt/skills/plugin-files/dia (skills/*/SKILL.md and references). For claims about Popper/Lakatos/Duhem-Quine you may use web search with general public terms only; never put plugin or document text into a query.

The question T answers: can the falsifiability problems T discusses be solved with the existing dia skills, or is a new dia skill needed? Rule on T's claims and on both reports' items as the skill requires. Read-only: do not edit any file. Write your full output (in Korean, as the user writes Korean) to /tmp/claude-0/-home-claude/543eb0e4-0af5-5b32-9fc8-3978303f9208/scratchpad/adjudicate-run1.md and also return it in full as your final message.
````

## dia-adjudicate run 2

Model: `claude-fable-5-2`

````text
dia-adjudicate

First load the skill by name with the Skill tool (skill: "dia:dia-adjudicate") and follow it in full. This is the second of two runs on the same input; start no run of your own (no further agents) and do not look for or read any other run's output (do not open files named adjudicate-run1.md).

Target (T): the document /home/claude/dia-falsification-skill-need.md (read it in full).
Reports:
- /tmp/claude-0/-home-claude/543eb0e4-0af5-5b32-9fc8-3978303f9208/scratchpad/blind-report.md (written independently, without seeing T, on the same question T answers)
- /tmp/claude-0/-home-claude/543eb0e4-0af5-5b32-9fc8-3978303f9208/scratchpad/adversary-report.md (written as an attack on T)
Sources to check claims against: the dia plugin v2.11.0 at /mnt/skills/plugin-files/dia (skills/*/SKILL.md and references). For claims about Popper/Lakatos/Duhem-Quine you may use web search with general public terms only; never put plugin or document text into a query.

The question T answers: can the falsifiability problems T discusses be solved with the existing dia skills, or is a new dia skill needed? Rule on T's claims and on both reports' items as the skill requires. Read-only: do not edit any file. Write your full output (in Korean, as the user writes Korean) to /tmp/claude-0/-home-claude/543eb0e4-0af5-5b32-9fc8-3978303f9208/scratchpad/adjudicate-run2.md and also return it in full as your final message.
````
