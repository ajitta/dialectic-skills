# Pre-registered protocol (written before any run, 2026-11-10)

## Question
Do existing paths handle falsifiability audits of non-universal empirical claims well enough that no new dia skill is needed?

## Arms
- A (baseline): plain assistant, no dia plugin. Input given as is.
- B (light fix): dia plugin copy with the light changes described in dia-falsification-skill-need.md §1.2 "판정의 조건" (router border line to quaestio stress; conjecture Step 0 destinations; criterion-refusal label; quaestio brief fields for criterion, decision rule, auxiliaries). Changes written by the orchestrator (author of T) — disclosed bias. Input sent as `dia <input>`.
- C (current dia v2.11.0, unmodified): input sent as `dia <input>`, run via the installed router.

## Inputs (claim context given in the message)
- I1 drug: 「이 약은 편두통 발작 빈도를 줄인다」는 내 주장인데, 뭘 보면 틀렸다고 할래? 반증 가능한 주장이야?
- I2 market: 「시장은 잘못된 가격을 결국 교정한다」는 내 주장인데, 반증 가능해?
- I3 pattern: 「우리 고객 데이터에 숨은 패턴이 있다」는 내 가설인데, 반증 가능해?

## Simulated user (fixed rules, applied mechanically by the orchestrator; every relay logged)
General: one short line per reply; answer only what is asked; if asked to choose among options, pick the one marked recommended, else the first; if asked something the rules do not cover, reply 「잘 모르겠어」. At the start of user turn 3 (i.e. after the assistant's third message) reply 「여기서 정리해 줘」 and accept whatever follows; stop after the assistant's 4th message at most.
- I1: Holds the claim. If asked what would count against it: 「위약과 차이가 없으면」. If asked for a threshold/size/decision rule: no own number; accept one if offered. If asked about conditions held fixed (dose, measurement, population): accept those offered. If asked for reasons: 「임상시험 결과를 봤어」.
- I2: Holds the claim. Refuses every deadline or bounded version: 「기한은 못 정해. 언젠가는 교정돼」. If asked whether any observation would count against it: 「아직 교정 안 된 것뿐이지 반례는 아니야」. If asked what "correct" means: 「적정 가치로 돌아가는 거」.
- I3: Holds the claim. If asked what "pattern" means: 「구매 간격이 길어지면 이탈한다는 관계」. Then if asked what would count against it: 「그 관계가 없으면」. Accept offered thresholds/conditions.

## Scoring (per transcript; 1 = met, 0 = not met, NA = not applicable)
- K1 Form classification correct: I1 statistical — falsifiable only given a decision rule; I2 as worded (no time bound) unfalsifiable by form; I3 unfalsifiable/untestable until "pattern" is defined, testable once defined.
- K2 Asks for or states the need for a decision rule (threshold/effect size) — I1 only.
- K3 Names conditions/auxiliary hypotheses to hold fixed (I1, I3 after definition).
- K4 I2 only: (a) a bounded version is treated as a change to the claim, AND (b) the holder's refusal of every criterion is named as making the claim unfalsifiable/immunized.
- K5 Gives no verdict on whether the claim is true (all).
- K6 Does not record a criterion as agreed unless the user agreed to it (all where a criterion appears).
Applicable items: I1: K1,K2,K3,K5,K6 (5); I2: K1,K4,K5,K6 (4); I3: K1,K3,K5,K6 (4) → 13 per arm.

## Bar (decided now)
An arm MEETS THE BAR if K1 = 1 on all three inputs AND total ≥ 11/13.

## Interpretation (decided now)
- If C meets the bar → existing dia already suffices; new skill rejected.
- Else if A or B meets the bar → new skill rejected (plain answer or light fix suffices).
- If none meets the bar → new-skill case strengthened, not proven.
- n = 1 per cell: a single run; differences of 1–2 points are noise. Report raw scores.

## Grading
A separate grader on a different model than the arms (fable), given the 9 transcripts shuffled and unlabeled, this scoring section only (not the hypotheses or arm descriptions), must quote the transcript span for each 1.
