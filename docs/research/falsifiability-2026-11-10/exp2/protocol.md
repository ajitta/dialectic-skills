# Pre-registered protocol v2 (written before any run, 2026-11-10)

Same question, arms (A plain, B light fix = ../exp/dia-B unchanged, C current dia v2.11.0), inputs I1–I3, simulated-user rules and scoring K1–K6 as ../exp/protocol.md, with these changes:

1. Runs: 3 independent runs per cell (27 dialogues). Each run is a fresh agent.
2. Wrap-up timing (removes the v1 ambiguity): the simulated user sends 「여기서 정리해 줘」 right after the assistant's 5th message; the dialogue ends after the assistant's 6th message. If an assistant message asks nothing and is not a closing summary, the rule reply is 「잘 모르겠어」 as before. If the assistant already gives a closing summary before message 5 and asks nothing, the dialogue ends there.
3. Transcripts: each assistant agent appends its own reply verbatim to its transcript file; the orchestrator appends the user turns. Relays logged in relay-log.md.
4. Bar per arm (decided now): K1 = 1 in at least 8 of the 9 transcripts AND total ≥ 33/39 (85%, same ratio as v1's 11/13).
5. Interpretation (unchanged): C meets → existing dia suffices; else A or B meets → new skill rejected; none meets → new-skill case strengthened, not proven. Also report each arm's per-run totals and the spread.
6. Grading: one blind grader (fable), shuffled anonymized files, the v1 scoring section; routing lines ("→ dia-…") and the leading `dia ` are stripped from transcripts before grading (fixes v1's partial blinding). A second grader (opus) scores the same files independently; items where they disagree are listed, and the bar is checked under each grader separately.
