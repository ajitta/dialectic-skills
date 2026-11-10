# dia-adjudicate 판정 (1차 실행)

## 1. 입력

- 대상 T: `/home/claude/dia-falsification-skill-need.md` (전문 읽음).
- 보고서 2건. 섞은 순서: **R1 = adversary-report.md** (T에 대한 공격), **R2 = blind-report.md** (T를 보지 않고 같은 질문에 답한 독립 판단). 작성자 역할 표시는 판정에 쓰지 않았습니다.
- 독립성: 두 보고서 모두 이 대화에서 제가 쓴 것은 아닙니다. 다만 같은 계열 모델이 썼을 가능성이 높아서, 두 보고서와 T가 오류를 공유할 수 있습니다(Rule 2). 저는 T, 두 보고서, 플러그인 v2.11.0 원문(`/mnt/skills/plugin-files/dia`), IEP 페이지 한 곳만 보았습니다.
- 실행: 두 번 실행 중 **1차**입니다. 2차와의 대조는 호출자가 합니다.
- 도구: Bash(grep/sed)로 원문 대조, WebFetch(요약형)로 IEP "Karl Popper: Philosophy of Science"(https://iep.utm.edu/pop-sci/) 확인.

## 2. 결론

C (T §0, 19행): "**새 dia 스킬이 정당화될 수 있는 곳은 (가-2) 하나뿐**입니다. (가-1)은 기존 스킬을 고치는 것으로 충분하고, (나)는 플러그인 바깥의 평가 인프라로 다루는 것이 맞습니다."

고정한 읽기(Rule 10):
- **읽기 A:** C의 "(가-2)"는 무조건 권고가 아니라 "조건부 후보"입니다(15행 "새 스킬 후보. 조건부 권고", 132행 "판정의 조건"). C가 실패하려면 (가-2)에 빈자리가 없음을 보이거나, (가-1)/(나) 중 하나가 새 스킬을 요구함을 보여야 합니다.
- **읽기 B:** 29행 "엄격성에 해당하는 기록은 `conjecture`의 **Tried** 필드뿐"은 "플러그인 전체에서 시도한 것을 기록하는 장치는 Tried뿐"이라는 주장으로 읽습니다.
- **읽기 C:** "시장은 결국 교정된다"는 쓰인 그대로, 즉 기한 없는 "결국"을 가진 주장으로 읽습니다.

## 3. 대상의 주장

| # | 위치 | 주장(요약) | 유형 | 판정 | 제기 | 근거 | 증거 등급 |
|---|---|---|---|---|---|---|---|
| T1 | 28행 | Prior criterion은 conjecture Step 2에 있고 경험적 C에 첫 반례와 함께 묻는다 | 사실·인용 | 성립 | R1(확인) | conjecture SKILL.md Step 2: "if C is empirical, … ask it with the first case" | 도구 확인(grep) |
| T2 | 29행 | 엄격성 기록은 conjecture의 Tried 필드뿐 | 사실 | **실패** | R1, R2(독립 확인) | reductio 106행 "list the directions and premise sets you tried"; negative 66행 "list them"; warrant 78행 "list the questions"; quaestio "Say which tests did not happen". T 37행 스스로도 reductio가 시도 방향을 나열한다고 씀 | 도구 확인 |
| T3 | 30행 | quaestio falsification pull은 stress에서만 필수 | 인용 | 성립 | R1(확인) | quaestio Rhythm: "in `stress`, at least one falsification pull" | 도구 확인 |
| T4 | 31행 | reductio·negative Step 7이 "the observation that would change the recommendation"을 요구 | 인용 | 성립 | R1(확인) | reductio 98행, negative 86행 | 도구 확인 |
| T5 | 34행 | 새 스킬이면 같은 장치가 두 곳에 다른 이름으로 정의되어 regula Rule 4에 어긋남 | 인용·추론 | 부분 성립 | R1 | 인용에서 범위 한정어가 빠짐: Rule 4 원문 "One name per thing **across the files a model reads together**". 스킬은 따로 로드되므로 적용이 늘어난 것 | 도구 확인 |
| T6 | 37–39행 | (가-1) 수정 후보 3개(reductio/negative Tried, quaestio develop 필수 pull, counterplan 사전 합의 필드) | 제안 | 부분 성립 | R1, R2 | Tried 추가는 이미 있는 기록의 형식 통일에 가까움(T2). counterplan 관찰은 이미 Step 6에서 사용자가 고르기(Step 7) 전에 나옴. 새로운 것은 "합의"뿐 | 도구 확인 |
| T7 | 48행 | 확률·통계 주장은 conjecture Step 0이 거절하고 warrant는 지지 강도만 본다 | 사실 | 성립 | R2 | conjecture Step 0 "'generally', 'usually', 'most' … dia-warrant"; warrant Rule 1 "never whether the claim is true" | 도구 확인 |
| T8 | 49행 | 존재 주장을 받는 스킬이 없음. 순수 존재명제는 반증 불가의 전형 | 사실·포퍼 | 성립 | R2, R1(D1) | Step 0 안내 목록에 존재 주장의 행선지가 없음. IEP: "there is no way of definitively showing that they are false" | 도구 확인 + 요약형 조회(IEP) |
| T9 | 50행 | 표방이 없는 비보편 주장의 면역화를 잡는 곳은 비어 있다 | 사실·추론 | 부분 성립 | R1(A1, C3) | negative, reductio, conjecture에 대한 서술은 맞음. 그러나 quaestio의 "A belief nothing could disconfirm is a finding, not a strength"(모든 모드에서 쓸 수 있는 전술)를 이 행에서 빠뜨림. 다만 quaestio는 "an idea"를 받고 기준 기록 필드가 없음 | 도구 확인 |
| T10 | 50행 예시 | "시장은 결국 교정된다"는 보조가설로 보호된 이론의 예 | 분류 | 부분 성립 | R1(A3, A4) | 읽기 C에서 이 주장은 기한이 없어서 형식상 반증할 수 없음. 보조가설 문제가 아니라 형식 문제임. conjecture가 Step 0에서 받을 수는 있지만 hard rule 2 때문에 검사 가능한 전역 사례를 낼 수 없음 | 재도출 |
| T11 | 51행 | 사전 예측 설계는 quaestio가 일부 다루지만 감사는 아님 | 추론 | 성립 | — | quaestio 설명 "develop an idea into options and a plan" | 도구 확인 |
| T12 | 56행 | warrant에 넣으면 두 번째 판정 축이 생김 | 추론 | 성립 | R1(A6 실패) | warrant Rule 1, 14행 | 도구 확인 + 재도출 |
| T13 | 57행 | conjecture에 넣으려면 Step 0와 Step 4–5 전 구조를 바꿔야 함 | 추론 | 성립 | R2 | Step 0 "only a claim about every member of a class"; Step 5 수리는 반례 한 개를 전제로 함 | 재도출 |
| T14 | 58행 | quaestio는 선택지와 계획을 담은 브리프로 끝나므로 결과물이 다르다 | 사실·추론 | 부분 성립 | R1(A1, C2) | 과장된 부분: Step 3 "If the session was pure stress-testing and the user doesn't want options, skip this step". 그래도 브리프 템플릿에는 합의된 반증 기준 필드가 없음(섹션: Thesis, Decisions, Assumptions, Open questions …). 결과물이 다르다는 결론은 약하게나마 남음 | 도구 확인 |
| T15 | 60–66행 | 반증가능성의 두 층(논리적/방법적) | 포퍼 해석 | 부분 성립 | R1(D3, D5) | IEP는 반증가능성을 논리적 성질로, 반증주의를 방법론 제안으로 구분함(R1 보고, 요약형). "텍스트만으로 충분"은 뒤엠-콰인 때문에 약해짐: IEP "in many cases impossible to test scientific theories in isolation" | 요약형 조회 |
| T16 | 69행 | "결국 교정된다"는 기한을 물어야만 드러나는 방법적 면역화이므로 스킬은 대화형이어야 함 | 추론 | **실패**(예시로서) | R1(A3) | 읽기 C에서 기한 없는 "결국"은 형식상 반증 불가임. T 68행의 "관찰 내용이 없는 주장은 묻지 않고 판정"과 충돌함. 기한을 붙이면 주장이 바뀜(conjecture hard rule 5 "No silent redefinition"과 같은 논리). 대화형 필요성 자체는 다른 예로 뒷받침될 수 있으나 이 예로는 안 됨 | 재도출 |
| T17 | 70행 | 확률적 주장은 엄밀히 반증할 수 없으니 결정 규칙이 필요 | 포퍼 | 확인 불가 | R1(D2), R2 | T 스스로 "기억에 기댄 것이며 미검증"이라 표시. IEP 요약에는 해당 내용 없음. 『과학적 발견의 논리』 8장 원문이 필요 | 기억 |
| T18 | 71행 | 뒤엠-콰인: 고정할 보조가설을 기록 | 포퍼·설계 | 성립 | R1(D5) | IEP 위 인용 | 요약형 조회 |
| T19 | 72행 | 용어 분쟁이면 elenchus로 "넘김", conjecture Step 4와 같은 처리 | 인용 | 부분 성립 | R1(C7) | conjecture: "say so and offer dia-elenchus for that question; the case stays disputed". 원문은 넘기는 것이 아니라 제안하는 것이고 사례는 disputed로 남음 | 도구 확인 |
| T20 | 79행 | 면역화 장치 목록에 "보조가설"을 포함 | 포퍼·설계 | 부분 성립 | R1(D4) | IEP 요약: 보조가설은 "allows for the generation of new, falsifiable predictions"이면 정당함. 문제는 임시방편(ad hoc) 보조가설뿐 | 요약형 조회 |
| T21 | 81·108행 | "숨은 패턴" 가설은 묻지 않고 "형식상 반증 불가" 라벨 | 분류 | 부분 성립 | R1(A3) | 49행은 "이 데이터에"라는 유한·한정 영역의 존재 주장이라 순수(무제한) 존재명제가 아님. 막는 것은 "패턴"의 정의 부재임 | 재도출 |
| T22 | 85행 | reductio Step 2는 "refute T" 요청을 refute 방향 기본값으로 처리 | 인용 | 성립 | R1(확인) | reductio 47행 "Refute (when the user asks to refute T, or names no direction …)" | 도구 확인 |
| T23 | 87행 | techne 질문 4는 외부 점검 | 인용 | 성립 | R1(확인) | techne 29행 | 도구 확인 |
| T24 | 90행 | router는 description을 보고 고른다 | 인용 | 성립 | R1(확인) | router "Choose the one dia skill whose description in your skill list fits" | 도구 확인 |
| T25 | 113–114행 | 메뉴 번호 고정, README·plugin.json의 "Thirteen", router "print the thirteen rows" | 사실 | 부분 성립 | R1(C9) | 모두 맞음. 그러나 목록이 불완전: router 25행 "A number from 1 to 13"도 고쳐야 함 | 도구 확인 |
| T26 | 115행 | regula Rule 3("Fewer instructions")의 논리가 router에도 적용 | 인용·추론 | 성립 | R2 | regula 26행 "Compliance tends to fall as instructions pile up" | 도구 확인 |
| T27 | 140행 | adjudicate는 보고서를 직접 쓰지 못하고, 재판정자는 될 수 있음 | 인용·추론 | 부분 성립 | R1(B5) | "Do not write the reports yourself"는 맞음. 재판정자 역할은 가능하지만, Step 1(단일 C 인용)과 Step 2(주장 목록)가 실행 기록에 잘 맞지 않음 | 도구 확인 + 재도출 |
| T28 | 141행 | regula는 지시문 텍스트를 검토하고 실행은 대상이 아님 | 사실 | 성립 | R2 | regula 설명 "Write or review instructions" | 도구 확인 |
| T29 | 142행 | emend, ratchet은 출력을 고칠 뿐 준수를 판정하지 않음 | 사실 | 부분 성립 | R1(B3, C10) | emend는 "a standard or reference given there, which is supplied material"에 비추어 결함을 확인함. 판정 기능이 있지만 결과물은 수정본임 | 도구 확인 |
| T30 | 148행 | 실패 관찰의 상당수는 기계적으로 판정 가능(한 메시지 한 질문, 고정 라벨, 금지 문구) | 추론 | 부분 성립 | R1(B4) | quaestio hard rule 1: "two asks joined into one sentence still count as two, even under one question mark"는 의미 판단을 요구함. conjecture rule 11은 라벨을 사용자 언어로 번역하게 함. 일부(필드 유무)는 여전히 기계적 | 도구 확인 |
| T31 | 150행 | README: "only Markdown, YAML and JSON files … no scripts, hooks, MCP servers or binaries" | 인용 | 성립 | R1, R2 | README 25행 | 도구 확인 |
| T32 | 157–158행 | adjudicate rule 2(arXiv:2506.07962), ratchet·emend의 Huang et al. 2024 | 인용 | 성립 | R1 | adjudicate Rule 2; emend 34행, ratchet 14행 "arXiv:2310.01798" | 도구 확인 |
| T33 | 161행 | 효과 가설은 한 대화 안에서 통제할 수 없는 실험 문제 | 추론 | 성립 | R1, R2 | conjecture theory.md 56행 "No study has tested this method with users"; regula step 1의 A/B 요건 | 도구 확인 + 재도출 |
| T34 | 165–170행 | 권고 순서: 수정 → 평가 스위트 → 새 스킬 → 루브릭 | 제안 | 부분 성립 | R1(B2) | 168행은 스위트가 있어야 1번 수정을 반증할 수 있다고 함. regula step 1은 eval이 있으면 수정과 함께 A/B를 요구함. 순서와 근거 사이에 긴장이 있음 | 재도출 |
| T35 | 151·176행 | 저장소에 평가 체계가 있는지는 확인하지 않음 | 한계 진술 | 성립 | R1(C11) | 사실 그대로의 자기 보고 | 재도출 |
| C | 19행 | 새 스킬은 (가-2)에만 정당화 가능(조건부), (가-1)은 수정, (나)는 외부 | 결론 | 부분 성립 | R1, R2 | (나)와 (가-1) 방향은 두 보고서 모두 지지함. (가-2)는 빈자리가 실재하지만(T7, T8, R2 라우팅 3–5행) T가 말한 것보다 좁음(T9, T14, T16). T 스스로 조건부로 두었으므로 C 자체는 실패하지 않음 | 도구 확인 + 재도출 |

## 4. 보고서 쟁점

| # | 쟁점 | 제기 | 판정 | 심각도 | 근거 | 증거 등급 |
|---|---|---|---|---|---|---|
| I1 | Tried만이 엄격성 기록이라는 T 주장은 틀림 (R1 B1·C1; R2 P2) | R1, R2 | 타당 | major | T2 참조 | 도구 확인 |
| I2 | quaestio가 방법적 층을 이미 다루고, "결과물이 다르다"는 제외 근거는 틀림 (R1 A1·C2) | R1 | 부분 타당 | major | stress 모드는 선택지 없이 끝날 수 있음(Step 3). 그러나 브리프에 기준 기록 필드가 없고(R2 P1도 같은 지적), 형식 판정 verdict가 없으며, 설명이 "an idea"를 받음. "argument is wrong"은 과장 | 도구 확인 |
| I3 | 갭 표가 quaestio의 반증 불가 신념 지적을 빠뜨림 (R1 C3) | R1 | 부분 타당 | minor | T9 참조. T는 53행에서 pull을 인정하므로 "어떤 스킬도 짚지 않는다"는 함의는 과장 | 도구 확인 |
| I4 | 논리적 층은 한 번에 끝나므로 router의 "None fits"로 충분하고, 남는 것은 기록 필드 두 개 (R1 A2) | R1 | 부분 타당 | major | router "None fits: say so in one line and answer without a dia skill"은 맞음. 기준선 대비 효과 증거가 없다는 점은 R2의 최강 반론과 일치함. 그러나 "필드 두 개뿐"은 R1 스스로 열거한 quaestio의 결여(형식 verdict, `--target`, router 진입)와 맞지 않음 | 도구 확인 + 재도출 |
| I5 | T의 예시 라벨이 틀림: 숨은 패턴은 한정 존재, 시장 예시는 형식 층 (R1 A3·D3) | R1 | 타당 | major | T16, T21 참조. 대화형 필수 근거로 든 예시가 무너짐 | 재도출 |
| I6 | conjecture가 시장 예시를 포함한 경험적 보편 부분을 이미 다룸 (R1 A4·C4·E 5행) | R1 | 부분 타당 | minor | Prior criterion이 "markets"를 명시하고 Step 0이 받을 수 있음은 맞음. 그러나 hard rule 2 "a case whose check you cannot write is not raised" 때문에 기한 없는 주장에는 전역 사례를 낼 수 없어 "stopped before testing"으로 끝남(R2 라우팅 4행과 같음). "already covers"는 과장 | 도구 확인 + 재도출 |
| I7 | counterplan이 계획 밑의 가정에 대한 반박 관찰을 이미 줌 (R1 A5) | R1 | 부분 타당 | minor | Step 6 "Favours the plan if: an observation the user could make"는 맞음. 그 관찰은 어시스턴트가 쓴 것이고 사용자가 합의하지 않음(R2 P1) | 도구 확인 |
| I8 | warrant 공격 실패, T의 "무엇이 반박하는지 묻지 않는다"만 약간 과장 (R1 A6) | R1 | 부분 타당 | minor | 반박 슬롯은 근거(warrant)의 예외이지 주장의 반증 조건이 아님. 다만 "[conclusion] Are there other reasons for or against C?"는 반대 이유를 묻긴 함 | 도구 확인 |
| I9 | negative, elenchus, techne 공격 실패 (R1 A7·A8) | R1 | 타당 | minor | negative Rule 1, Rule 6; router의 techne 규칙 | 도구 확인 |
| I10 | 방법적 층은 보유자가 있어야 하는데 `--target` 텍스트에는 보유자가 없음 (R1 A9) | R1 | 타당 | minor | T 65행 "보유자의 약속", 128행 "보유자에게 묻지 않고 … 라벨을 붙임"이 실패 관찰. conjecture는 "the user takes the claim up for this dialogue"로 해결함 | 도구 확인 + 재도출 |
| I11 | (가-1) "비용이 작다"는 과장: develop 정체성 충돌, counterplan 턴 증가, regula 의미 변경 절차 (R1 B1 나머지) | R1 | 부분 타당 | minor | regula step 1 "a meaning change also needs an A/B … 12 or more such runs per arm"은 맞음. develop 충돌은 약함: "don't manufacture doubt"는 이미 정밀한 아이디어에 대한 문장임 | 도구 확인 |
| I12 | 권고 순서가 자기 논리와 어긋남 (R1 B2) | R1 | 부분 타당 | minor | T34 참조 | 재도출 |
| I13 | emend 기각이 과장됨, 그래도 (나) 결론은 강화됨 (R1 B3·C10) | R1 | 부분 타당 | minor | T29 참조 | 도구 확인 |
| I14 | "기계적 판정"이 과장됨 (R1 B4) | R1 | 타당 | minor | T30 참조 | 도구 확인 |
| I15 | adjudicate 재판정자 역할이 어색함 (R1 B5) | R1 | 부분 타당 | minor | T27 참조. 명시 호출로는 가능함 | 도구 확인 |
| I16 | counterplan 관찰은 이미 사용자 선택 전에 나오므로 새로운 것은 "합의"뿐 (R1 C5) | R1 | 타당 | minor | Step 6에서 보여 주고 Step 7에서 물음. Step 7 "do not suggest an answer" | 도구 확인 |
| I17 | regula Rule 4를 따로 로드되는 스킬에 확대 적용 (R1 C6) | R1 | 타당 | minor | T5 참조. 인용에서 범위 한정어가 생략됨(Rule 5) | 도구 확인 |
| I18 | "conjecture Step 4와 같은 처리"는 부정확: 원문은 제안만 함 (R1 C7) | R1 | 타당 | minor | T19 참조 | 도구 확인 |
| I19 | "트리거 문구"라는 틀이 과장됨 (R1 C8) | R1 | 부분 타당 | minor | 모든 설명에 "a request that only sounds like this is not an invocation"이 있음. T는 90행에서 description이 결정한다고 스스로 정정함 | 도구 확인 |
| I20 | 비용 목록 불완전 (R1 C9) | R1 | 타당 | minor | router 25행 "A number from 1 to 13" | 도구 확인 |
| I21 | "평가 체계 존재 미확인"이라는 한계 진술이 틀렸거나 과장됨 (R1 C11) | R1 | **과장** | minor | 아래 오류 목록 참조 | 도구 확인 |
| I22 | 존재명제는 검증 가능하므로 "반증 불가"가 "공허"는 아님 (R1 D1) | R1 | 타당 | minor | IEP 요약에서 존재명제 부분 확인. 검증 가능성 부분은 표준적 포퍼 해석(기억) | 요약형 조회 + 기억 |
| I23 | 확률 주장에 결정 규칙 필요(LSD 8장) (R1 D2, R2 P3c) | R1, R2 | 확인 불가 | minor | 둘 다 기억임. IEP 요약은 이 내용을 말하지 않음(부재는 반박이 아님) | 기억 |
| I24 | 보조가설을 면역화 장치로 열거한 것은 과장. 임시방편 판정이 필요함 (R1 D4) | R1 | 타당 | minor | T20 참조 | 요약형 조회 |
| I25 | 뒤엠-콰인이 "텍스트만으로 충분"을 약하게 함 (R1 D5) | R1 | 부분 타당 | minor | IEP "in many cases impossible to test … in isolation". "대부분의 주장"은 R1의 일반화 | 요약형 조회 |
| I26 | 라우팅 표에서 새 스킬에 배정된 5행 중 3행이 사례를 약하게 함 (R1 E) | R1 | 부분 타당 | minor | 마케팅 행과 숨은 패턴 행은 타당함. 시장 행은 I6 때문에 과장 | 재도출 |
| I27 | 대체안(quaestio stress 안내 + conjecture 한 줄)을 주 권고로 삼아야 함 (R1 F) | R1 | 부분 타당 | major | 판단 문제임. R2의 최강 반론(eval 먼저, 최소 변경 다음)과 같은 방향. T 132행은 이를 "드물다면"의 대안으로 이미 둠. 사용 빈도와 기준선 비교 없이는 어느 쪽도 확정 못 함 | 재도출 |
| J1 | 사전 기준은 대화형 스킬에서만 의미가 있고, 한 번에 끝나는 스킬에는 합의 상대가 없음 (R2 P1) | R2 | 타당 | minor | negative rule 10 "Whole analysis in one response", reductio rule 9 "Whole chain in one response", warrant rule 9 "One pass in audit mode" | 도구 확인 |
| J2 | quaestio 브리프에 반증 질문의 답을 기록할 필드가 없음 (R2 P1) | R2 | 타당 | minor | brief-template.md 섹션 목록 | 도구 확인 |
| J3 | "held" 결과마다 시도 목록이 이미 요구되고, 자기 부여 심각도 등급은 플러그인이 피함 (R2 P2) | R2 | 타당 | minor | warrant 90행 "In a severity field, write that this method does not give it"; adjudicate Rule 7 | 도구 확인 |
| J4 | conjecture Step 0 안내 목록에 존재·기한 없는 ∀∃·통계 주장의 행선지가 없음 (R2 P3a) | R2 | 부분 타당 | minor | 존재 주장은 맞음. 통계 주장은 "generally/usually/most → dia-warrant"로 행선지가 있음. "every"가 붙은 ∀∃는 Step 0이 받을 수 있음(R2 라우팅 4행 스스로 그렇게 봄) | 도구 확인 |
| J5 | 보유자가 모든 기준을 거부할 때의 라벨이 없음 (R2 P3b) | R2 | 타당 | minor | conjecture 기록 "**Prior criterion:** the user's answer … | not asked" | 도구 확인 |
| J6 | reductio가 연역적 시험에서 보조가설 기록에 맞게 만들어짐 (R2 P3d) | R2 | 부분 타당 | minor | rule 2 "No hidden premises", rule 3 "an empirical or causal claim is never a step: … it goes into the premise list", rule 6 인용 확인. 다만 사전에 고정할 보조가설을 합의하는 장치는 아님 | 도구 확인 |
| J7 | 핵심 반증 감사에는 새 스킬이 필요하고, 최소 변경 대안이 있음 (R2 P3 판정) | R2 | 부분 타당 | major | 빈자리는 확인됨(T7, T8, J5). 필요성은 R2 스스로 반론에서 eval 이후로 미룸 | 도구 확인 + 재도출 |
| J8 | 결정 규칙은 요청이 있을 때 techne로 갈 수 있음 (R2 P3c) | R2 | 부분 타당 | minor | techne Q3 인용 확인. router: techne는 "never start from a request" | 도구 확인 |
| J9 | 형식 준수 검사는 플러그인 밖 (R2 P4) | R2 | 타당 | minor | README 25행; evidence.md "1 of 4", "1/6, then 8/12" 확인 | 도구 확인 |
| J10 | 효과 증거 없음, 효과 검증은 플러그인 밖 (R2 P5) | R2 | 타당 | minor | theory.md 56행; evidence.md 5행 "Its runs, prompts and traces are not public" | 도구 확인 |
| J11 | conjecture는 "결국 교정" 주장에서 hard rule 2 때문에 전역 사례를 못 내고, 결과 라벨이 실제 발견을 가림 (R2 라우팅 4행) | R2 | 타당 | minor | hard rule 2; Step 6 "stopped before testing (no case was ruled on)" | 도구 확인 + 재도출 |
| J12 | 실험 설계 요청은 router가 techne를 직접 실행하지 않고 형식만 안내 (R2 라우팅 6행) | R2 | 타당 | minor | router "dia-skopos, dia-ratchet, dia-adjudicate and dia-techne never start from a request" | 도구 확인 |
| J13 | 최강 반론: 플러그인 기준으로는 eval 전 새 스킬을 정당화할 수 없음 (R2) | R2 | 부분 타당 | major | regula Rule 3과 step 1 인용 확인. 다만 step 1은 기존 텍스트 변경에 대한 규칙이므로 새 스킬에는 유추로만 적용됨 | 도구 확인 + 재도출 |

## 5. 보고서의 오류

- **R1 C11 (I21), 과장.** R1은 T의 "평가 체계 존재 여부를 확인하지 않음"을 "틀렸거나 과장"으로 분류했습니다. 그런데 T의 진술은 사실 그대로의 자기 보고입니다. 또 R1이 반대 증거로 든 것은 저장소의 평가 체계를 보여 주지 않습니다. regula step 1은 조건문입니다("when an eval exercises the changed condition"). evidence.md는 공개되지 않은 저자 연구라고 밝힙니다(141행 "The source: unpublished; raw data not public").
- **R1 A4·C4·E 시장 행 (I6), 과장.** "conjecture already covers … including the document's market example"는 conjecture hard rule 2 "a case whose check you cannot write is not raised"와 맞지 않습니다. 기한 없는 "결국"에 대해서는 어떤 유한 관찰도 결론 위반을 보이지 못하므로, 실행은 "stopped before testing"으로 끝납니다(재도출). 또 C4는 T에 없는 문구 "goes nowhere"를 따옴표로 T에 돌렸습니다. T 50행은 "그런 표방이 없는 비보편 주장의 면역화는 비어 있습니다"라고 썼습니다(귀속 오류, Rule 5).
- **R1 A1 결론부 (I2), 과장.** "the 'different end product' argument is wrong"은 지나칩니다. brief-template.md의 섹션은 "Thesis / Decisions / Assumptions / Open questions / Options considered / Criteria / Parking lot / Not tested this session / Next step"이고, 합의된 반증 기준 필드가 없습니다. 차이는 줄어들지만 사라지지 않습니다.
- **R1 A2 (I4), 일부 과장.** "the distinct content … shrinks to two record fields"는 R1 A1 스스로 열거한 quaestio의 결여(형식 판정 verdict, `--target`, router가 고르지 않는 설명)와 맞지 않습니다.
- **R1 A6 (I8), 경미.** T의 warrant 서술을 "overstated"라고 했지만, 반박 슬롯 질문 "When would that rule not apply?"는 근거의 예외에 관한 것이지 주장을 반박하는 관찰에 관한 것이 아닙니다. 과장 지적은 일부만 성립합니다.
- **R2 P3a (J4), 경미.** "no destination for … statistical claims put as point hypotheses"에서 통계 주장은 Step 0의 "'generally', 'usually', 'most' … dia-warrant" 행선지가 있습니다. 엄밀한 점가설이라면 맞을 수 있으므로 경미한 오류입니다.

## 6. 일관성 점검

읽기 A–C와 "conjecture는 기한 없는 ∀∃ 주장을 받지만 검사할 수 없다"는 전제를 T10, T16, I5, I6, J4, J11에 같이 적용했는지 대조했습니다. I6(R1)과 J11(R2)을 같은 전제로 판정했고, 바꾼 판정은 없습니다.

## 7. 확인했고 문제없음

다음은 플러그인 원문 대조로 확인했습니다.
- T1, T3, T4, T7, T22–T24, T26, T28, T31, T32의 인용과 사실.
- R1의 인용: quaestio "skip this step and Step 4's questions", question-bank "A number or an event?", counterplan Rule 5, warrant "do not fill backing or rebuttal to complete the layout", rebuttal 슬롯 정의, regula "an eval, a probe, a review", adjudicate "dia-emend's job", quaestio "don't manufacture doubt".
- R2의 인용: negative·reductio·warrant의 한 번에 끝나는 규칙, reductio rule 3·6, evidence.md "1 of 4"와 "1/6, then 8/12", "Its runs, prompts and traces are not public", theory.md "No study has tested this method with users", regula "12 or more such runs per arm", router 폴백과 techne 규칙.
- IEP 인용 세 개(존재명제, "permanently immunized", isolation): 요약형 조회로 확인했습니다.
- (나)를 플러그인 밖에서 다룬다는 결론에는 두 보고서 모두 반대 근거가 없습니다.

## 8. 확인하지 못함

| 항목 | 찾아본 곳 | 막힌 이유 | 무엇이 확정하나 |
|---|---|---|---|
| T17 / I23: 확률 주장은 결정 규칙 없이 반증 불가(포퍼 LSD 8장) | IEP 요약(WebFetch) | 페이지가 이 점을 말하지 않음(부재는 반박 아님), 원전 미열람 | 『The Logic of Scientific Discovery』 8장(§65–68) 원문 |
| C의 (가-2) 필요성: 빈자리가 실제로 얼마나 자주 생기는가 | T, R1, R2, 플러그인 | 사용 기록이 자료에 없음(T, R2 모두 인정) | 사용자의 dia 사용 기록, 또는 라우팅 3–5행 입력에 대한 기준선(None fits) 대 스킬 비교 eval |
| R1 D3: IEP가 반증가능성(논리)과 반증주의(방법)를 구분함 | IEP 요약 | 직접 질문하지 않음. 판정에 쓰지 않았으므로 영향 없음 | IEP 원문 대조 |

## 9. 결정적 쟁점

**I27/J13 (I2, I4, I5와 묶임): (가-2)의 대화형 새 스킬이 기존 경로(quaestio stress, conjecture Step 0 안내 한 줄, router "None fits")보다 나은가.** 두 보고서는 독립적으로 같은 반론에 이릅니다. 기준선 비교 없이는 정당화할 수 없고, 최소 변경이 먼저라는 것입니다. T는 이를 "드물다면"의 대안으로 두었습니다.

T의 근거 중 대화형 필요성의 예시(T16)와 quaestio 제외 근거(T14)가 약해져서, 주 권고와 대안의 순서가 뒤집힐 수 있습니다. C의 "정당화될 수 있는 곳은 (가-2) 하나뿐"이라는 조건부 문장은 유지됩니다. 하지만 "새 스킬 후보"를 주 권고로 두려면 다음 조건이 필요합니다. 라우팅 3–5행 같은 입력에서 기준선 답변이 실패한다는 관찰, 또는 사용 빈도 자료입니다.

## 10. 사람이 확인할 것

**반드시 확인** (C에 미치는 영향이 큰 순서):
1. I2 / R1 A1 결론부 "과장" 판정: brief-template에 기준 필드가 없다는 근거가 맞는지, quaestio stress가 사실상 반증 감사를 하는지.
2. I4 / R1 A2 일부 과장 판정: 남는 차이가 "필드 두 개"보다 큰지.
3. I6 / R1 A4·C4·E 시장 행 과장 판정: conjecture hard rule 2가 기한 없는 "결국"의 전역 사례를 정말 막는지(재도출에 기댐).
4. 확인 불가 판정 중 C에 걸린 것: (가-2)의 필요성(사용 빈도, 기준선). C의 조건 자체입니다.
5. I21 / R1 C11 과장 판정.
6. I8 / R1 A6 일부 과장 판정.
7. J4 / R2 P3a 경미한 오류.

**요약 조회에 기댄 판정:** IEP 요약형 조회에 기댄 판정은 T8, T15, T18, T20, I22, I24, I25의 7건입니다. 이 중 원문 표현이 다르면 판정이 바뀔 수 있는 것은 T20/I24("allows for the generation of new, falsifiable predictions"라는 조건)입니다.

개수 대조: 쟁점 표의 과장 1건(I21), 오류 목록 6건(I21, I6, I2, I4, I8, J4), C가 기대는 확인 불가 1건. 겹치는 I21을 하나로 세면 7개 항목이고, 위 목록 7항목과 일치합니다. 7단계에서 바뀐 판정은 없습니다.

이 판정은 T의 주장과 보고서 항목의 근거를 판정한 것이며, C가 참이거나 거짓임을 증명한 것이 아닙니다.
