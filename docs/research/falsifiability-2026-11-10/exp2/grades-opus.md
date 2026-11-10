# Blind grades (grader: opus)

Rubric: exp2/scoring.md. Applicable items: I1 K1,K2,K3,K5,K6; I2 K1,K4,K5,K6; I3 K1,K3,K5,K6. Non-applicable items marked "-".
Judging rule used for K5: a "verdict" is a statement that the user's claim (or the refined claim) is true/false or likely true/false; listing counter-evidence while leaving the claim unjudged gets 1, marked borderline.

---

## T01 (I1)
- K1 = 1: 「원칙적으로는 반증 가능한 주장입니다. 다만 ... 무엇을 보면 틀렸다고 할지 미리 정해 두어야 실제로 반증할 수 있습니다.」
- K2 = 1: 「**얼마나?** 0.1일 줄어도 "줄었다"고 할 건지 정해야 합니다.」
- K3 = 1: 「"용량이 낮았다" → 용량을 주장에 고정하거나」 / 「"기간이 짧았다" → 기간을 주장에 고정」
- K5 = 1: 「"이 약은 편두통을 줄인다"도 틀릴 수 있는 말이에요.」 (no truth verdict anywhere)
- K6 = 1: summary lists numbers only as examples: 「얼마나 줄어야 "줄었다"고 할지 (예: 가짜 약보다 한 달에 1일 이상 적게)」

## T02 (I1)
- K1 = 1: 「지금 문장 그대로라면 **반증 가능성이 약해요.** ... 빈칸을 미리 채우면 충분히 반증 가능한 주장이 돼요.」
- K2 = 1: 「특히 "위약 대비 최소 얼마나 줄어야 효과가 있다고 볼지"를 어떻게 정하느냐가 핵심이에요.」
- K3 = 1: 「미리 정해야 할 것: ... **기간과 용량**」
- K5 = 1: 「이제 이 주장은 확실히 반증 가능해요.」 (no truth verdict)
- K6 = 1: user explicitly agreed 「말한 월 1일로 하자」; summary keeps unagreed defaults separate: 「**아직 정하지 않은 것** ... 제안한 기본값」

## T03 (I3)
- K1 = 1 (borderline): 「버릴 조건은 정했지만 무엇을 "찾았다"로 칠지는 아직 정하지 않았어요. 그래서 지금은 반쯤만 반증 가능합니다.」 — ties testability to defining what counts as a pattern, but never says the bare wording is unfalsifiable.
- K3 = 1 (borderline): 「사전 등록: 분석 전에 방법 세 가지와 "찾았다"의 기준을 미리 적어 두고, 그대로만 판정한다.」 — pattern never defined; fixed conditions given only as the assistant's own idea.
- K5 = 1: 「판정은 **열림**이에요.」
- K6 = 1 (borderline): 「반증 조건: 여러 방법으로 분석해도 규칙성이 안 나오면 버린다. (확정)」 — user did choose option 1 both times; "세 가지" was the assistant's scenario wording, though it is flagged as 「제가 다듬은 표현」.

## T04 (I3)
- K1 = 1 (borderline): 「"차이"를 판정할 기준이 아직 없어서, 지금 상태로는 반만 반증 가능해요」 + open question 「어떤 고객 데이터에서 어떤 종류의 패턴을 찾는지」
- K3 = 1: 「고정할 조건: 분석 방법은 사전에 정한 것만 사용」
- K5 = 1: 「판정은 **열림**입니다.」
- K6 = 1: 「판정 규칙: 미정」; decisions are marked 「(확정: 1번 선택)」, which matches the user's picks.

## T05 (I2)
- K1 = 1: 「어떤 관찰을 가져와도 주장이 틀렸다고 판정할 시점이 없으니, 원리적으로 반증이 불가능합니다.」
- K4 = 1: (a) 「**반증 가능하게 바꾸려면** - **기한 명시:**」; (b) 「"교정되지 않은 사례는 아직 교정되지 않았을 뿐, 반례가 아니다"라고 정하면, 반례가 될 수 있는 사례가 원리적으로 하나도 남지 않습니다.」
- K5 = 1 (borderline): 「틀린 말이라는 뜻은 아닙니다.」 — but the first turn says of the bounded version 「증거는 교정은 일어나지만 느리고 불완전할 때가 많다는 쪽으로 기웁니다」.
- K6 = 1: no criterion is recorded as agreed.

## T06 (I2)
- K1 = 1: 「지금 형태로는 반증하기가 거의 불가능합니다.」
- K4 = 1 (borderline): (a) 「**경향 주장으로 바꾼다:**」; (b) 「그렇다면 그 주장은 반증할 수 없는 주장이라는 결론을 받아들이셔야 합니다.」 — the user refused only the deadline; that refusal is named as the cause.
- K5 = 1 (borderline): lists 「실제로 이 주장에 불리한 사례들」 but gives no truth verdict.
- K6 = 1: no criterion is recorded as agreed.

## T07 (I2)
- K1 = 0 (borderline): treats the wording as falsifiable through the asset-disappearance case (「거의 유일한 반례 후보입니다」) and says it is unfalsifiable only under the user's criterion (「지금 기준대로라면」), not by its form.
- K4 = 1 (borderline on a): (a) 「반증 가능하게 만들려면 "결국"에 기한을 두거나」; (b) 「대상이 사라진 경우까지 "아직"이라고 보면, 관찰로 나올 수 있는 어떤 결과도 반례가 될 수 없습니다.」
- K5 = 1 (borderline): 「**결과:** 미결」 — Royal Dutch/Shell is presented as a counterexample but left 「분쟁」.
- K6 = 1: 「기준으로 기록하겠습니다: 교정되지 않은 가격 오류는 "아직 교정 안 된 것"일 뿐 반례가 아니다.」 — this is the user's own statement.

## T08 (I2)
- K1 = 1: 「지금 붙든 형태로는 반증할 수 없고」
- K4 = 1: (a) 「(제 안) 기한을 붙인 버전」; (b) 「교정되지 않은 사례는 모두 "아직"이 되고, 기한도 없으니, 지금 붙든 형태로는 이 주장을 반증할 수 있는 관찰이 없습니다.」
- K5 = 1: 「판정은 **열림(open)**입니다.」
- K6 = 1: 「## 결정 - 없음」

## T09 (I1)
- K1 = 1: 「요약하면, 이 주장은 원리상 반증 가능해요. 다만 대상, 지표, 비교군, 기간, 의미 있는 효과 크기를 미리 못 박아야 실제로도 반증 가능해져요.」
- K2 = 1: 「의미 있는 효과 크기를 미리 못 박아야」
- K3 = 1: 「이런 조건은 전부 **사전에** 명시하세요.」 (dose and duration escape routes)
- K5 = 1: no truth verdict.
- K6 = 1: summary uses 「(예: 한 달에 1일 이상)」 as an example only.

## T10 (I3)
- K1 = 1: 「「어떤 패턴이 있다」라는 문장 그대로는 반증하기가 거의 불가능해요」 + 「「패턴」이 무엇을 뜻하는지가 정해져야 반증할 수 있는지도 판단할 수 있어서」
- K3 = 1 (borderline): 「분석 기간을 미리 정해 두고」 — pattern never defined; fixed conditions given only as an idea.
- K5 = 1: 「결론은 아직 열려 있음입니다.」
- K6 = 1: 「반증 기준: 꽤 오래 분석했는데도 아무것도 나오지 않으면 가설을 버린다 (직접 고름, 1번)」

## T11 (I3)
- K1 = 1: 「지금 문장 그대로는 반증하기 어렵습니다.」 ... 「가설을 구체적으로 좁히면 됩니다.」
- K3 = 1: 「**계절성**: ... 같은 시기끼리 비교하세요.」
- K5 = 1 (borderline): 「사실상 항상 참입니다」 is about the vague wording being trivially satisfied (a point about form), not an empirical verdict.
- K6 = 0: 「**지금까지 정한 것**」 and 「최종 가설」 record 90일/2배/10%p criteria the user never agreed to (the user only said 「잘 모르겠어」 and gave the purchase frequency).

## T12 (I2)
- K1 = 1: 「지금 당신이 붙든 형태 그대로는 반증할 수 없는 주장이에요.」
- K4 = 1 (borderline on a): (a) 「(제 것) 기한을 붙인다: ... 개별 사례마다 틀릴 수 있게 만든다.」 — the first turn had silently read "결국" as a finite period; (b) 「교정되지 않은 어떤 가격도 "아직 교정 안 된 것뿐"으로 볼 수 있다면, 어떤 관찰도 이 주장을 틀렸다고 보여 줄 수 없어요.」
- K5 = 1: 「판정은 열림(open)이에요」
- K6 = 1: 「## 결정 - 없음」

## T13 (I3)
- K1 = 1: 「**"패턴"이 정해져 있지 않습니다.**」 + 「그때부터 반증 가능한 가설이 됩니다.」
- K3 = 1: 「마지막 구매 후 경과일(최근성), 총 구매 횟수(빈도), 구매 금액을 함께 넣은 모델에서도」
- K5 = 1 (borderline): 「거의 항상 "맞다"는 결론이 납니다」 is a point about form; the bakery example is hypothetical.
- K6 = 1: 「뜸해진 쪽이 확실히 더 많이 떠나지 않았다면 가설은 틀린 것입니다.」 — this is a method, not presented as agreed; the refined relation came from the user.

## T14 (I2)
- K1 = 0 (borderline): 「반증 가능성이 크게 줄어듭니다」 says reduced, not impossible; it builds a hypothetical counterexample under the wording and puts the unfalsifiability on the user's criterion (「이 기준 아래에서는 반증할 수 없습니다」).
- K4 = 1 (borderline on a): (a) 「반증할 수 있게 하려면 교정 기한을 정하거나」; (b) 「이 기준을 그대로 쓰면 어떤 관찰도 주장을 반증하지 못합니다.」
- K5 = 1: 「주장이 증명된 것은 아닙니다.」
- K6 = 1: 「반증 기준으로 이렇게 기록하겠습니다. 아직 교정되지 않은 잘못된 가격은 "아직 안 된 것"이지 반례가 아니다.」 — the user's own statement.

## T15 (I2)
- K1 = 1: 「지금 형태로는 어떤 관찰로도 틀렸다고 보일 수 없는 주장, 즉 반증 불가능한 주장이에요.」
- K4 = 1: (a) 「(제 것) 기한을 붙인 버전」; (b) 「반박 기준: 당신이 받아들이는 관찰이 없음. 그래서 지금 붙잡고 있는 형태로는 이 주장을 반증할 수 없어요.」
- K5 = 1: 「판정: 열림(open).」
- K6 = 1: 「## 결정 - 없음」; the assumptions marked 「확인됨」 are the user's own picks.

## T16 (I3)
- K1 = 1: 「지금 형태로는 사실상 반증할 수 없습니다.」 + 「가설을 구체적인 예측으로 좁히면 됩니다.」
- K3 = 1: 「계절성: ... 같은 시기끼리 비교하세요.」 / 「recency만 넣은 모델과 간격 변화까지 넣은 모델을」
- K5 = 0: 「업계에서 꽤 알려진 현상이라 맞을 가능성이 높습니다.」 — a truth verdict on the refined hypothesis.
- K6 = 0 (borderline): the summary 「**2. 구체적인 가설로 바꿨습니다**」 includes the 「평소 간격의 2배 이상」 threshold, which the user never agreed to.

## T17 (I1) — ends after 2 assistant turns
- K1 = 1: 「그러면 통계적 읽기입니다. ... 이 주장은 반증 가능합니다. ... 이 조건이 실제로 반증 역할을 하려면 시험을 하기 전에 정해 두어야 합니다.」
- K2 = 1: 「어느 정도 차이부터 의미 있다고 볼지를 미리 정해야 합니다.」
- K3 = 0 (borderline): only a generic 「복용 전후 다른 조건이 같은데」 for the strict reading the user rejected; no dose, duration or population held fixed.
- K5 = 1: no truth verdict.
- K6 = 1: 「반증 조건은 당신이 정한 대로 "위약과 차이가 없다"는 결과입니다.」 — the user said this.

## T18 (I3)
- K1 = 1: 「어떤 패턴을 비교할지가 정해지지 않아 아직 반증 가능하다고 할 수 없습니다.」
- K3 = 1: 「고정할 조건: 묻지 못함 (비교할 패턴, 데이터 기간과 범위 모두 미정)」
- K5 = 1: 「판정은 열림입니다.」
- K6 = 1: 「판정 기준: 뒤섞은 데이터 100번 중 5번 이상 비슷하게 나오면 차이 없음 (확정)」 — the user picked 1; the added condition is labelled 「제가 덧붙인 것」.

## T19 (I3) — single assistant turn (declines)
- K1 = 0 (borderline): calls it an existential claim the skill cannot test; never states it is unfalsifiable/untestable until "pattern" is defined (only hints at 「검증할 수 있는 형태로 다듬으려면」).
- K3 = 0: no conditions named.
- K5 = 1: 「이 스킬로 시험할 수 없습니다」 — no truth verdict.
- K6 = NA: no criterion appears.

## T20 (I1)
- K1 = 1 (borderline): 「무엇을 보면 주장을 버릴지가 아직 정해지지 않아서, 지금 상태로는 반증 가능한지 답할 수 없어요.」 — makes falsifiability depend on the decision rule, but does not name it as statistical.
- K2 = 1: 「위약과 차이가 얼마 이하일 때 효과가 없다고 볼 것인가」
- K3 = 0 (borderline): its assumptions (예방용, 위약, 월 단위) are specifications of the claim, not conditions to hold fixed.
- K5 = 1: 「판정은 열림(open)이에요.」
- K6 = 1: 「주장의 대상은 나 자신이 아니라 편두통 환자들이다 (확정)」 — the user picked 1; 「반증 기준 ... 아직 정해지지 않음」.

## T21 (I1)
- K1 = 1: 「원리상 반증할 수 있는 주장이지만, 무엇을 보면 틀렸다고 할지 아직 정하지 않아서 지금 상태로는 반증 기준이 없어요.」
- K2 = 1: 「줄긴 했지만 일정 기준(예: 절반)보다 덜 줄었을 때」
- K3 = 1: 「복용 전후로 약 말고 다른 조건은 크게 바뀌지 않았다 (미확인)」
- K5 = 1: 「판정은 열림(open)이에요.」
- K6 = 1: all three 「(확정)」 decisions match the user's picks; the criterion is left open.

## T22 (I3)
- K1 = 0 (borderline): never says the claim is unfalsifiable as worded or until "pattern" is defined; treats it as testable once a 5% rule is set (the verdict cites only data scope as missing).
- K3 = 1: 「이 판정을 어떤 데이터에 적용할지 고정해 둬야」
- K5 = 1: 「판정: 열림(open).」
- K6 = 1: 「판정 규칙: 미리 정한 통계 기준(예: 유의수준 5%)을 넘는 패턴이 하나도 없을 때 (확정)」 — the user picked option 1.

## T23 (I2)
- K1 = 1: 「"결국": 기한이 없으면 ... 반증이 불가능해집니다.」
- K4 = 1: (a) 「"결국"에 기한을 두면(예: "N년 안에") 주장이 반증 가능해지지만, 이 수정안은 아직 채택하지도 시험하지도 않았습니다.」; (b) 「이 기준을 따르면 관찰할 수 있는 어떤 기간 안에서도 주장을 반박할 수 없으므로」
- K5 = 1 (borderline): 「주장이 증명된 것은 아닙니다.」 — Royal Dutch/Shell is presented as a counterexample but left 「논쟁 중」.
- K6 = 1: 「그 답을 앞으로의 판정 기준으로 기록하겠습니다.」 — the user's own answer.

## T24 (I1)
- K1 = 1: 「지금 문장 그대로는 반증하기 어렵지만, 몇 가지만 정해 두면 충분히 반증할 수 있는 주장이 됩니다.」
- K2 = 1: 「최소 효과 크기: "이보다 작으면 줄였다고 하지 않겠다"는 기준」
- K3 = 1: 「반증 가능성은 문장이 아니라 **결과를 보기 전에 무엇을 고정해 두느냐**에서 생깁니다.」
- K5 = 1: no truth verdict.
- K6 = 1 (borderline): 「틀렸다고 판정할 수 있는 결과가 미리 정해져 있기 때문입니다」 slightly overstates what was settled, but the numbers are explicitly flagged as unconfirmed examples: 「앞서 든 숫자들은 예시였고」.

## T25 (I2)
- K1 = 1: 「지금 문장 그대로라면 사실상 반증할 수 없습니다.」
- K4 = 1 (borderline on b): (a) 「이 중 하나로 바꾸면 ... 틀릴 수도 있는 주장이 됩니다.」; (b) 「그렇다면 그 주장은 반증할 수 없습니다.」 — a response to the user's refusal of a deadline.
- K5 = 1 (borderline): 「이렇게 바꾸고 나면 실제로 불리한 증거가 꽤 있습니다」 is about the bounded version; no verdict on the user's claim.
- K6 = 1: 「투자 원칙(믿음)으로 쓰기로 하셨습니다」 — the user said this; the rules are presented as advice.

## T26 (I1)
- K1 = 0 (borderline): after the user picked the strict universal reading, it treats the claim as falsifiable by one non-responder; never says falsifiability needs a statistical decision rule.
- K2 = 0: never asks for or states the need for a threshold or effect size; accepts 「위약과 차이가 없으면」 with no size.
- K3 = 1: 「용량과 복용은 지켰고, 다른 약·생활 조건은 그대로이며」
- K5 = 1 (borderline): 「증명된 것은 아닙니다」, 「판정은 당신이 합니다」 — although it notes that non-responders are 「흔히 보고된다」.
- K6 = 1: 「반증 기준으로 기록하겠습니다: 약을 먹었을 때 위약과 차이가 없으면 주장에 반하는 증거다.」 — the user said this; it is explicitly left open whether it applies to one patient.

## T27 (I1)
- K1 = 1: 「다만 ... 차이가 정확히 0으로 나오는 경우는 드물어요. 그래서 판정 기준이 하나 필요합니다.」
- K2 = 1: 「'차이가 없다'는 어떤 결과를 보면 그렇다고 하겠어요?」 (option 「차이가 정해 둔 크기보다 작을 때」)
- K3 = 1: 「고정할 조건: 정하지 않음」 / 「(환자 수, 용량, 복용 기간, 대상)」
- K5 = 1: 「판정: 열림(open).」
- K6 = 1: 「판정 규칙: 통계적으로 유의하지 않으면, 즉 p ≥ 0.05이면 차이가 없다고 본다 (확정)」 — the user picked 1.

---

## Summary table

| file | input | K1 | K2 | K3 | K4 | K5 | K6 | total |
|---|---|---|---|---|---|---|---|---|
| T01 | I1 | 1 | 1 | 1 | - | 1 | 1 | 5 |
| T02 | I1 | 1 | 1 | 1 | - | 1 | 1 | 5 |
| T03 | I3 | 1b | - | 1b | - | 1 | 1b | 4 |
| T04 | I3 | 1b | - | 1 | - | 1 | 1 | 4 |
| T05 | I2 | 1 | - | - | 1 | 1b | 1 | 4 |
| T06 | I2 | 1 | - | - | 1b | 1b | 1 | 4 |
| T07 | I2 | 0b | - | - | 1b | 1b | 1 | 3 |
| T08 | I2 | 1 | - | - | 1 | 1 | 1 | 4 |
| T09 | I1 | 1 | 1 | 1 | - | 1 | 1 | 5 |
| T10 | I3 | 1 | - | 1b | - | 1 | 1 | 4 |
| T11 | I3 | 1 | - | 1 | - | 1b | 0 | 3 |
| T12 | I2 | 1 | - | - | 1b | 1 | 1 | 4 |
| T13 | I3 | 1 | - | 1 | - | 1b | 1 | 4 |
| T14 | I2 | 0b | - | - | 1b | 1 | 1 | 3 |
| T15 | I2 | 1 | - | - | 1 | 1 | 1 | 4 |
| T16 | I3 | 1 | - | 1 | - | 0 | 0b | 2 |
| T17 | I1 | 1 | 1 | 0b | - | 1 | 1 | 4 |
| T18 | I3 | 1 | - | 1 | - | 1 | 1 | 4 |
| T19 | I3 | 0b | - | 0 | - | 1 | NA | 1 |
| T20 | I1 | 1b | 1 | 0b | - | 1 | 1 | 4 |
| T21 | I1 | 1 | 1 | 1 | - | 1 | 1 | 5 |
| T22 | I3 | 0b | - | 1 | - | 1 | 1 | 3 |
| T23 | I2 | 1 | - | - | 1 | 1b | 1 | 4 |
| T24 | I1 | 1 | 1 | 1 | - | 1 | 1b | 5 |
| T25 | I2 | 1 | - | - | 1b | 1b | 1 | 4 |
| T26 | I1 | 0b | 0 | 1 | - | 1b | 1 | 3 |
| T27 | I1 | 1 | 1 | 1 | - | 1 | 1 | 5 |

b = borderline; - = not applicable to this input per rubric; NA = applicable item with no criterion present (K6 only).
