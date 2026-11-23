# Outside research on dia-regula and dia-skopos drafts, read against plugin 5.1.0

Research date: 2026-11-22; read 2026-11-24. Status: record. Nothing in it changes a skill, and no run was made for this reading.

The owner ran this research in a separate private folder outside this repository (`C:/Users/ajitta/Repos/ajitta/dia_3_reviewers_independent_judge`, commits `cfbef9b` and `b55341f`), against dia-regula 3.0.0 and dia-skopos 4.2.0. A session on 2026-11-24 read it against plugin 5.1.0 to ask whether any of it should change a skill. Its runs used Codex CLI 0.171.0 with `gpt-6.2-sol`, an engine this repository does not use (AGENTS.md, Probes and evals). They are not counted as verification of any released text on Codex.

## What the folder holds

- The owner's view, which the reviews examined, verbatim:

  > 의미의 완전성. = 닫힌 공리계
  > 논리적 구조성 = 완전함수 리커스브 함수. expression
  > 표면적 문체 = 일관된 도메인 용어
  >
  > 이게 나의 관점이야

  Its aim was a writing principle that raises both a model's instruction following and a person's understanding and maintenance of the text, with dia-regula's rules open to refutation.
- Three lens reviews: dia-negative, dia-reductio and dia-warrant, each run in its own chat.
- Two blind judgments with dia-adjudicate. Reports carried no authors and were given in a shuffled order. The verdicts:
  - As a writing perspective, each correspondence holds in part.
  - Read as a mathematical equivalence, each one fails:
    - a deductively closed theory with no axioms decides neither P nor ¬P;
    - μy[y+1=0] is undefined;
    - the same terms can carry a different register.
  - None conflicts directly with dia-regula's four rules.
  - The joint gain for model and person is unverified.
  - The reports' errors were minor.
- Drafts: dia-regula 3.1.0-draft and 4.0.0-draft, and dia-skopos 4.2.1-draft.
- Model runs, a human-evaluation form with no responses, and handoff notes.

## What the reading found

1. **No run used the released dia-regula.**
   - The early screen compared the 3.1 draft with a 4.0 pre-draft, one run each, judged by the person who wrote the drafts.
   - The validation compared the 3.1 draft with the final 4.0 draft: six author sessions and six execution sessions per arm. Both arms scored 144/144 on fixed policies, and 24/24 and 168/168 after a policy change.
   - The author sessions were given fully specified policies, precedence included ("else"), and asked to return JSON. The task was transcription, and the skill's reply form was bypassed, so a ceiling was to be expected.
2. **Both dia-regula drafts conflict with later decisions or with the rules themselves.**
   - Both require the fixed "Outcome, as stated / as read" lines that D120 removed.
   - The 4.0 draft drops most of the reasons, against Rule 3.
   - It splits conditions into short commands, the failure Rule 1 names.
   - Its "Compare versions" section adds human prediction and maintenance criteria to every A/B. That is a meaning change taken from this research's aim, not from a fault.
3. **4.0's new R2 clause answers a fault seen only under the 4.0 pre-draft.** The clause limits a source's authority to the decisions or conflicts it governs.
   - The fault: `policy.md` had precedence only when two sources' data conflicted, and the output also used it as the basis for an approval exception.
   - The 3.1 draft did not show this fault.
   - That the pre-draft's own "Name the authority for each decision" induced it is a reading only, because the pre-draft text was not kept.
4. **dia-skopos showed no fault in the released text.**
   - The source arm loaded 4.2.0 (checked in its inputs).
   - Six single-turn cases each reached the expected step in both arms: the review, waiting, or handing over. A correction to the goal alone updated the pending review and kept waiting.
   - Handed over to dia-techne, both arms produced the same artefact under each of the two approvals: 3/3 against 3/3.
   - Removing `selected_choice` from the handover changed nothing (3/3).
   - These were dry runs from a synthetic context that returned JSON, not skill runs.
   - The draft re-adds four labelled lines, against D114 and D116.
5. **The total-function idea is already reported in practice.** The idea is that every case in a rule has exactly one result.
   - Rule 1's breach list names placement only. It names neither a case with no result nor a case two lines both claim.
   - Probes Part AO show the released text already reports both kinds of fault: a rewrite listed the source's undefined cases (2 of 2), and a review reported a word cap that can conflict with the content asked for.
   - Probes Part CC show the same: a review of dia-skopos reported an undefined "unless" case and no instruction for when dia-techne is absent (2 of 2).
   - So no probe was proposed. The functional-programming analogies themselves left dia-regula in D75.
6. **The review method is dia-panel's.** Like the folder's method, dia-panel gives reports letters only, runs two judges on two orders and compares the verdicts that differ. The folder's notes say an earlier recheck that had looked at the progress chat was left out of the comparison: on a chat surface whose chats can see one another's history, a new conversation is not an independent one.
