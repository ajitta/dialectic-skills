# dia-adjudicate 판정 (2회차): dia-falsification-skill-need.md

## 1. 입력

- 보고서 2건. 섞은 순서: **R1** = `adversary-report.md`(T를 공격한 보고서), **R2** = `blind-report.md`(T를 보지 않고 같은 질문에 답한 보고서). 작성자 역할은 판정에 쓰지 않았습니다.
- 독립성: 두 보고서를 어떤 모델이 썼는지는 주어지지 않았고, 저와 같은 계열일 수 있습니다(그 경우 오류를 공유할 수 있음). 이 대화에서 제가 쓴 보고서는 없습니다. T와 보고서 외에 본 것은 dia v2.11.0 설치본(`/mnt/skills/plugin-files/dia`)과 공개 웹 페이지 2건(IEP, SEP)입니다. 웹 가져오기 도구는 원문이 아니라 요약을 돌려주므로 해당 판정은 "도구 확인(요약 경유)"입니다.
- 이 실행은 **두 번 중 두 번째 실행**입니다. 다른 실행의 출력은 보지 않았고, 별도 실행도 시작하지 않았습니다. 파일은 수정하지 않았습니다.
- 경로 표기: 아래 `skills/…`는 모두 `/mnt/skills/plugin-files/dia/` 아래입니다.

## 2. 결론 (C)

T §0, 19행: "**새 dia 스킬이 정당화될 수 있는 곳은 (가-2) 하나뿐**입니다. (가-1)은 기존 스킬을 고치는 것으로 충분하고, (나)는 플러그인 바깥의 평가 인프라로 다루는 것이 맞습니다."

- 고정한 읽기 ①: (가-2)는 "새 스킬이 필요하다"가 아니라 "새 스킬 **후보**, 조건부 권고"(15행)입니다. 조건은 사용 빈도이며, 드물면 가벼운 대안(132행: `quaestio` stress 진입점 + `conjecture` Step 0 안내 한 줄)을 씁니다. 모든 판정에 이 읽기를 썼습니다.
- 고정한 읽기 ②: "엄격성에 해당하는 기록"(29행)은 "유지 결과가 나올 때 무엇을 시도했는지 남기도록 요구되는 기록"으로 읽었습니다.
- 고정한 읽기 ③: "기계적으로 판정"(148행)은 "판단 없이 문자열·구조 검사로 판정"으로 읽었습니다.
- 나머지 결론: §3의 권고 순서(부수 결론).

## 3. 대상의 주장

판정: 성립 / 부분 성립 / 불성립 / 확인 불가. 증거 등급: 도구 = 이번 세션에 파일을 직접 읽거나 grep·diff로 확인, 요약 = 요약 경유 웹 확인, 재도출 = 제 논리, 기억 = 미확인.

| # | 위치 | 주장(요약) | 유형 | 판정 | 제기 | 근거 | 등급 |
|---|---|---|---|---|---|---|---|
| T1 | 6행 | 설치본과 synced 사본은 diff 차이 없음 | 사실 | 성립 | 미제기 | `diff -rq` 결과 차이 없음 | 도구 |
| T2 | 28행 | 사전 반박 기준은 `conjecture` Step 2 "Prior criterion", 경험적 C에 첫 반례와 함께 묻는다 | 사실 | 성립 | R1, R2 | `skills/dia-conjecture/SKILL.md` 56행 "ask it with the first case" | 도구 |
| T3 | 29행 | 엄격성 기록은 `conjecture`의 Tried 필드**뿐** | 사실 | **불성립** | R1, R2 | reductio 106행 "list the directions and premise sets you tried", negative 66행 "holds against the particulars tested, list them", warrant 78행 "list the questions and name the one you would ask next", quaestio 103행 "Say which tests did not happen". T 자신도 37행에서 reductio의 나열을 인정 | 도구 |
| T4 | 30행 | falsification pull은 stress에서만 필수 | 사실·인용 | 성립 | R1, R2 | quaestio 76행 "in `stress`, at least one falsification pull" | 도구 |
| T5 | 31행 | reductio Step 7, negative Step 7이 "the observation that would change the recommendation" 요구 | 인용 | 성립 | R1 | reductio 98행, negative 86행 | 도구 |
| T6 | 34행 | (가-1)을 새 스킬로 하면 같은 장치가 두 이름이 되어 regula Rule 4 위반. 인용 "One name per thing … a second word…" | 인용·추론 | 부분 성립 | R1 | 생략부에 범위 한정어가 있음: regula 27행 "across the files a model reads together". 따로 로드되는 두 스킬에의 적용은 유추. 중복 정의가 생긴다는 추론 자체는 성립 | 도구 |
| T7 | 37행 | reductio·negative의 유지 결과 라벨, reductio는 이미 시도 방향을 나열 | 사실 | 성립 | R1 | reductio 102·106행, negative 90행 | 도구 |
| T8 | 38행 | develop 모드에도 경험적 예측이 있으면 pull 필수(제안) | 제안 | 판정 대상 아님(제안). 긴장 있음 | R1, R2 | quaestio 32행 "`develop` (default: grow a fragile idea, gentle probes)". R2는 같은 수정을 선택 사항으로 제안 | 도구 |
| T9 | 39행 | counterplan의 "Favours the plan if" 관찰을 사용자가 고르기 **전** 합의 필드로 | 인용·제안 | 부분 성립 | R1, R2 | 인용 성립(85행). 관찰은 이미 Step 6에서 Step 7 질문보다 먼저 나옴. 새로운 것은 "합의"뿐 | 도구 |
| T10 | 48행 | 확률·통계 주장: conjecture Step 0 거절, warrant는 지지만 판정 | 사실 | 성립(표현 약간 넓음) | R1, R2 | conjecture 34행, warrant 35행 "Support, not truth". 단 warrant ask 모드에 "When would that rule not apply?"(124행)가 있음: 보증의 예외이지 주장의 반증 조건은 아님 | 도구 |
| T11 | 49행 | 존재 주장을 받는 스킬이 없다 | 사실 | 성립 | R1, R2 | conjecture Step 0 안내 목록(34–37행)에 존재 주장 행 없음. reductio 55행은 간접증명 맥락뿐 | 도구 |
| T12 | 50행 | negative는 자체 기준만, reductio는 엄격 모순만, conjecture의 몬스터 배제는 보편명제 한정 → 비보편 주장의 면역화는 "비어 있다" | 사실·추론 | 부분 성립 | R1 | 앞의 세 사실은 성립(negative 31행, reductio 29행, conjecture 76행). "비어 있다"는 quaestio 70행 "A belief nothing could disconfirm is a finding, not a strength"를 이 행에서 빠뜨림. 다만 quaestio에는 그 결과 라벨도 기록 필드도 없음 | 도구 |
| T13 | 51·58행 | quaestio는 선택지·계획 브리프로 끝나므로 결과물·종료 조건이 다르다 | 사실·추론 | 부분 성립 | R1 | quaestio 83행 "If the session was pure stress-testing and the user doesn't want options, skip this step": 선택지 없이 끝날 수 있음. 반면 브리프 양식(Thesis, Decisions, Assumptions, Open questions, Options, Criteria, Parking lot, Not tested, Next step)에 반증 기준 필드는 없고 판정은 Sharpened/Open/Refuted뿐 | 도구 |
| T14 | 53행 | pull의 존재는 저자가 필요를 인식한 간접 증거 | 추론 | 확인 불가 | 미제기 | 저자 의도는 텍스트로 확정 못 함. C는 이에 기대지 않음 | 재도출 |
| T15 | 56행 | warrant에 넣으면 두 번째 판정 축이 생긴다 | 인용·추론 | 성립 | R1(공격 실패) | warrant 14·35행 | 도구, 재도출 |
| T16 | 57행 | conjecture에 넣으려면 Step 0와 Step 4–5 구조를 바꿔야 한다 | 추론 | 성립 | R2 | conjecture 34행 "a rebuttal condition, not a refutation"; Step 4–5는 반례 1건 판정·수리 구조 | 도구, 재도출 |
| T17 | 60–65행 | 논리적/방법적 반증가능성 두 층(포퍼) | 외부 사실 | 성립 | R1, R2 | SEP: "a clear distinction between the logic of falsifiability and its applied methodology"; IEP: "a normative, methodological proposal" | 요약 |
| T18 | 68행 | 순수 존재명제 등은 형식상 반증 불가 | 외부 사실 | 성립(존재명제에 한해 확인) | R1, R2 | IEP: "no way of definitively showing that they are false" | 요약 |
| T19 | 69행 | "결국 교정된다"는 기한이 붙으면 반증 가능, 모든 기한 거부면 방법적 면역화 → 대화형이어야 함 | 추론 | 부분 성립 | R1, R2 | 기한 없는 문장은 **형식상** 반증 불가이고 기한 추가는 주장 변경. T의 68행 규칙("묻지 않고 판정")과 107행 표("기한을 묻고…")가 같은 예에서 충돌. "보유자가 한정된 판본을 받는지는 물어야 안다"는 부분은 성립 | 재도출 |
| T20 | 70행 | 확률적 주장은 엄밀히 반증 불가, 결정 규칙 필요 | 외부 사실 | 확인 불가 | R1, R2 | IEP·SEP 요약에 해당 문장 없음. T·R1·R2 모두 기억에 의존 | 기억 |
| T21 | 71행 | 뒤엠-콰인: 고정할 보조가설 기록 | 외부 사실·제안 | 성립 | R1, R2 | IEP: "in many cases impossible to test scientific theories in isolation" | 요약 |
| T22 | 72행 | 용어 분쟁은 elenchus로 "넘긴다. conjecture Step 4와 같은 처리" | 귀속 | 부분 성립 | R1 | conjecture 78행은 "offer dia-elenchus for that question; the case stays disputed": 넘김이 아니라 제안 | 도구 |
| T23 | 79행 | 면역화 장치 목록에 "보조가설"을 한정 없이 포함 | 외부 사실 | 부분 성립 | R1 | IEP: "can be legitimately saved from falsification by the introduction of an auxiliary hypothesis"(새 반증 가능 예측을 낳는 조건). 금지되는 것은 ad hoc한 것 | 요약 |
| T24 | 85행 | reductio Step 2는 "refute T" 요청을 refute 방향 기본값으로 처리 | 사실 | 성립 | R1 | reductio 47행 | 도구 |
| T25 | 86행 | "반증 가능한가"를 받는 스킬이 지금 없다 | 사실 | 성립 | R1, R2 | 13개 description·메뉴 행 중 맞는 것 없음. router 68행 "None fits" 경로로 감 | 도구 |
| T26 | 87행 | "어떻게 시험하나"는 techne 질문 4(외부 점검)나 dia 밖의 일 | 사실 | 부분 성립 | R1, R2 | techne 29행 질문 4는 과제 결과의 외부 점검. 실험 설계 자체는 질문 3 쪽이고, router 64행상 techne는 요청으로 시작되지 않음 | 도구 |
| T27 | 90행 | router는 description과 경계 항목으로 고른다(인용) | 인용 | 성립 | R1 | router 57행 | 도구 |
| T28 | 101–110행 | 라우팅 시험표: "숨은 패턴"은 묻지 않고 형식상 반증 불가 | 제안·추론 | 부분 성립 | R1, R2 | "패턴"의 범위가 정해지지 않아 반증 불가라는 판정은 방어 가능. 그러나 "패턴"을 유한한 종류로 정의하면 시험 가능해지므로, T의 실패 관찰 125행("존재명제에 기준을 억지로 붙임")이 그 수리를 막음 | 재도출 |
| T29 | 113–114행 | 추가 비용: 번호 고정, "Thirteen"(README, plugin.json), "print the thirteen rows" | 사실 | 성립(목록은 불완전) | R1 | router 49행, README 3행, plugin.json. 추가로 router 25행 "A number from 1 to 13", 각 스킬의 경계 목록 | 도구 |
| T30 | 115행 | regula Rule 3의 논리가 router 수준에도 적용 | 추론 | 부분 성립(유추) | R2(같은 유추 사용) | Rule 3(26행)은 한 텍스트 안의 지시문 수에 관한 것. 스킬 수로의 확장은 유추 | 도구, 재도출 |
| T31 | 117행 | Prior criterion과 새 스킬의 기준 합의는 같은 장치 → 공유 패턴 | 추론·제안 | 성립(추론). 부작용 있음 | R1 | 같은 질문을 두 스킬이 물으면 router 67행 "Two fit about equally … ask which, and stop"이 걸릴 수 있음 | 도구, 재도출 |
| T32 | 132행 | 빈도는 이번 자료로 알 수 없다. 드물면 가벼운 대안 | 한계 진술 | 성립 | R1, R2 | 플러그인에 사용 기록 없음 | 도구 |
| T33 | 140행 | adjudicate는 채점자는 못 되고 재판정자는 될 수 있다 | 사실·추론 | 성립(적합성은 빠듯함) | R1, R2 | adjudicate "Do not write the reports yourself". 단 Step 1 "Quote T's conclusion C", Rule 7 "by effect on the conclusion"는 결론이 하나인 문서를 전제 | 도구 |
| T34 | 141행 | regula는 지시문 텍스트만 본다 | 사실 | 성립 | R1, R2 | regula description "Write or review instructions for models" | 도구 |
| T35 | 142행 | emend·ratchet은 출력을 고칠 뿐 준수 판정은 아니다 | 사실 | 부분 성립 | R1, R2 | emend 22·33행: 기준 문서를 "supplied material"로 받아 그에 비춰 결함을 확인할 수 있음. 다만 산출은 수정본이고 같은 모델의 자기 검토 | 도구 |
| T36 | 148행 | 실패 관찰의 상당수는 기계적으로 판정 가능(한 메시지 한 질문, 고정 라벨, 필드 유무, 금지 문구) | 추론 | 부분 성립 | R1 | quaestio 20행 "two asks joined into one sentence still count as two, even under one question mark"; conjecture 28행 "Reply in the user's language, including labels and the fixed result values". 필드 유무·표 금지는 기계적 | 도구 |
| T37 | 150행 | README: Markdown·YAML·JSON만, 스크립트 없음 | 인용 | 성립 | R1, R2 | README 25행 | 도구 |
| T38 | 151·176행 | 저장소에 평가 체계가 있는지는 확인하지 않았다 | 한계 진술 | 성립. 단 플러그인 안에 단서가 있었음 | R1 | adjudicate 8행 "rules drawn from adjudication trials, docs/research/dia-adjudicate.md", regula `references/evidence.md`, regula 52행 A/B 규칙 | 도구 |
| T39 | 155행 | 판단 의존 규칙("strongest reasonable reading", "least warrant")을 dia 스킬로 채점하면 같은 모델의 자기 채점 | 인용·추론 | 성립 | 미제기 | reductio 33행, warrant 37행. 추론은 재도출 | 도구, 재도출 |
| T40 | 157–158행 | adjudicate rule 2는 arXiv:2506.07962, ratchet·emend는 Huang et al. 2024를 든다 | 귀속 | 성립(플러그인이 그렇게 적는다는 점) | R1 | adjudicate 32행, ratchet 14행, emend 34행. 논문 자체의 내용은 확인하지 않음(T도 미검증이라 밝힘) | 도구 |
| T41 | 160행 | 채점자 간 불일치 항목은 기존 adjudicate로 재판정 가능 | 추론 | 성립(적합성은 빠듯함) | R1, R2 | T33과 같은 근거. "Running twice" 절 존재 | 도구 |
| T42 | 161행 | H1–H3은 통제 실험이 필요하고 한 대화 안의 스킬로는 통제 불가 | 추론 | 성립 | R1, R2 | 재도출. `dia-conjecture/references/theory.md` 56행 "No study has tested this method with users"와도 맞음 | 재도출, 도구 |
| T43 | 167–168행 | 순서: (가-1) 수정 먼저, 평가 스위트 다음. (가-1)은 "비용이 작다" | 권고 | 부분 성립 | R1, R2 | T 스스로 스위트가 있어야 수정을 반증할 수 있다고 함. regula 52행: 의미 변경은 사용자가 요청했거나 발견이 요구할 때만 남고, 평가가 없으면 "report it as unmeasured and the user accepts it". 53행: 별도 sub-agent 검토. 즉 평가 선행이 강제되지는 않으나 "작은 비용"은 과소 | 도구 |
| T44 | 19행 | **C** | 결론 | **부분 성립(좁혀야 함)** | R1, R2 | (나)와 (가-1)의 방향은 성립. (가-2)는 "조건부 후보"라는 읽기에서 성립하나, 빈자리는 T가 쓴 것보다 좁음(아래 9절) | 도구, 재도출 |

## 4. 보고서 쟁점

판정: 타당 / 부분 타당 / 과장 / 틀림 / 확인 불가. 심각도는 C에 대한 영향으로 다시 매겼습니다(치명 = 고치지 않으면 C가 무너짐, 중대 = 뒷받침 주장이 무너지거나 C를 좁혀야 함, 경미).

| # | 쟁점 | 제기 | 판정 | 심각도 | 근거 | 등급 |
|---|---|---|---|---|---|---|
| I1 | quaestio가 방법적 층의 대화를 이미 갖고 있고, T의 배제 이유("선택지와 계획으로 끝남")가 틀렸다 | R1 A1, C2 | 부분 타당 | 중대 | quaestio 70·83행, question-bank 43행 "A number or an event?" 확인. 그러나 기준을 기록하는 필드가 없고(브리프 양식), 판정은 Sharpened/Open/Refuted뿐이며, 대상은 사용자의 아이디어. R1도 이 빠진 것들을 스스로 적음 | 도구 |
| I2 | 논리적 층은 한 번에 판정하므로 router "None fits"의 일반 답변으로 충분하고, T는 스킬이 그 기준선보다 낫다는 증거를 내지 않았다 | R1 A2; R2 반대 논거 1 | 부분 타당 | 중대 | router 68행 확인. T가 기준선 비교 증거를 내지 않은 것은 사실. 반대로 일반 답변이 충분하다는 증거도 없음(실행 없음). T의 조건부 권고가 이 불확실성을 이미 담음 | 도구, 재도출 |
| I2b | 그 결과 새 스킬 고유 내용은 "기록 필드 둘과 기준 정렬"로 줄어든다 | R1 A2, F | **과장** | 경미 | R1 A1이 quaestio에 없는 것으로 직접 든 "a one-pass verdict on logical form", "a `--target` for pasted text"가 빠짐. conjecture 56행은 "Record the answer"뿐이라 모든 기준 거부에 대한 라벨도 없음 | 도구, 재도출 |
| I3 | "숨은 패턴" 예는 순수 존재명제가 아니라 제한된 존재명제이고, 막는 것은 정의되지 않은 "패턴"이다 | R1 A3 | 부분 타당 | 경미 | 데이터는 유한하나 양화 범위는 패턴 전체여서 "제한된 존재명제"라는 분류는 확정 못 함. "정의를 물으면 시험 가능해진다"는 점은 타당(T28) | 재도출 |
| I4 | 시장 예는 형식상 반증 불가이고 기한 추가는 주장 변경이다. T는 이를 방법적 층에 잘못 놓았다 | R1 A3, D3; R2 라우팅 4 | 타당 | 중대 | T 68·69·107행의 내부 충돌(T19). conjecture 22행 "No silent redefinition"도 좁힘을 주장 변경으로 다룸 | 재도출, 도구 |
| I5 | conjecture가 경험적 보편명제(시장 예 포함)를 이미 받는다. 남는 구멍은 "어떤 관찰도 받지 않는 사용자"에 라벨이 없는 것뿐이며 한 문장으로 고친다 | R1 A4 | 부분 타당 | 중대 | conjecture 39·56행 "(people, systems, markets, measurements)" 확인. 그러나 R2가 보인 대로 hard rule 2("a case whose check you cannot write is not raised")가 반례 제기를 막아 "stopped before testing"으로 끝날 수 있음(100행). "한 문장으로 고친다"는 시험되지 않은 제안 | 도구, 재도출 |
| I5b | 새 스킬과 conjecture가 같은 사전 기준 질문을 물어 router의 "Two fit about equally"가 걸린다 | R1 A4 | 타당 | 경미 | router 67행. T 95행의 경계가 바로 이 중복을 만듦(T31) | 도구 |
| I6 | conjecture가 이 주장을 다루면 형식상 반증 불가를 이름 붙이지 못하고 오도하는 결과 라벨로 끝난다 | R2 라우팅 4 | 타당(추론, 실행 없음) | 중대 | conjecture 19·97·100행 | 도구, 재도출 |
| I7 | counterplan이 계획 밑 가정마다 판별 관찰을 이미 준다 | R1 A5, E 1행 | 부분 타당 | 경미 | counterplan 85행, 46행 확인. 그러나 그 관찰은 조수가 쓰고 사용자가 합의하지 않으며(R2 P1), T도 전략 자체는 counterplan으로 보냄(103행) | 도구 |
| I8 | warrant의 rebuttal 칸, negative rule 6, elenchus·techne로는 감사가 안 된다(공격 실패, T의 읽기 성립) | R1 A6–A8; R2 P1 | 타당 | 경미 | warrant 36·60행, negative 31·36행, router 64행 | 도구 |
| I9 | `--target` 텍스트에는 보유자가 없어 방법적 면역화 라벨을 붙일 수 없다 | R1 A9 | 타당 | 경미(설계 조건) | T 75행 대 128행. conjecture 41행 "the user takes the claim up for this dialogue"가 해법의 선례 | 도구, 재도출 |
| I10 | "Tried가 유일한 엄격성 기록"은 틀렸다. 유지 결과를 내는 스킬은 모두 시도한 것을 적게 한다 | R1 B1, C1; R2 P2 | 타당 | 중대 | T3의 근거 인용 4건 모두 확인. elenchus 100행 "the holding bar", 기록 양식 "Not examined"도 확인 | 도구 |
| I11 | 등급 매긴 엄격성은 플러그인이 자기 부여 등급을 피하는 것과 어긋난다 | R2 P2 | 부분 타당 | 경미 | 인용은 정확(warrant 90행 "In a severity field, write that this method does not give it"). 그러나 그 규칙은 다른 에이전트가 출력 형식을 정할 때 **발견의 심각도**에 관한 것이지 **시험의 엄격성**이 아님: 조건 불일치 | 도구 |
| I12 | develop 모드 pull 필수화는 모드 정체성과 "don't manufacture doubt"에 어긋난다 | R1 B1 | 부분 타당 | 경미 | "gentle probes"(32행)와의 긴장은 타당. "don't manufacture doubt"(43행)는 "If the idea is already precise" 조건의 문장이라 다른 경우 | 도구 |
| I13 | counterplan 관찰은 이미 사용자 선택 전에 나온다. 사전 합의는 차례를 하나 늘린다 | R1 B1, C5 | 타당 | 경미 | counterplan Step 6→7, 53행(한 응답으로 Step 7 질문까지) | 도구 |
| I14 | (가-1)의 수정은 regula상 의미 변경이라 비용이 작지 않다(A/B, 12회 이상, sub-agent 검토) | R1 B1 | 타당 | 경미 | regula 52·53행 인용 모두 확인. A/B는 "when an eval exercises the changed condition"일 때만이라는 조건도 R1이 적음 | 도구 |
| I15 | 권고 순서가 자기 논리와 어긋난다(평가가 수정보다 먼저 또는 함께) | R1 B2; R2 반대 논거 3 | 부분 타당 | 경미 | T43. regula는 평가 선행을 강제하지 않음("report it as unmeasured and the user accepts it") | 도구 |
| I16 | (나)에 스킬이 필요한가: 아니다. emend·adjudicate·regula가 이미 평가를 스킬 밖에 둔다 | R1 B3, C10; R2 P4, P5 | 타당 | 경미(C를 지지) | emend 22·33행, regula 52행 "any further check a repository rule requires (an eval, a probe, a review)", README 25행 | 도구 |
| I17 | 도구 없는 호스트의 사용자는 하네스를 못 돌린다는 점을 T가 따지지 않았다 | R1 B3 | 타당 | 경미 | T에 해당 고려 없음. README 3행은 여러 호스트를 대상으로 함 | 도구 |
| I18 | "기계적으로 판정 가능"은 과장이다 | R1 B4 | 타당 | 경미 | T36의 두 인용 | 도구 |
| I19 | 형식 규칙(고정 라벨, 한 메시지 한 질문 등)은 린터로 기계적 검사가 된다 | R2 P4 | **과장** | 경미 | I18과 같은 구절: quaestio 20행 "even under one question mark", conjecture 28행 "including labels and the fixed result values". 기록 필드·표 금지에 한해서는 타당 | 도구 |
| I20 | adjudicate는 재판정자로 잘 맞지 않는다 | R1 B5 | 타당 | 경미 | adjudicate Step 1·2, Rule 2·7 인용 모두 확인. 명시 호출로는 가능 | 도구 |
| I21 | adjudicate가 린터 보고 위의 판정 층, 두 번 실행이 판단 규칙 불일치의 방법이 된다 | R2 P4, P5 | 부분 타당 | 경미 | T33·T41과 같은 근거와 같은 한계(I20) | 도구 |
| I22 | regula Rule 4를 따로 로드되는 스킬에 적용한 것은 늘린 것이다 | R1 C6 | 타당 | 경미 | regula 27행 "across the files a model reads together" | 도구 |
| I23 | conjecture는 elenchus를 "제안"할 뿐이다 | R1 C7 | 타당 | 경미 | conjecture 78행 | 도구 |
| I24 | "트리거 문구" 틀은 과장이다. 문구는 `dia`가 앞에 올 때만 의미가 있다 | R1 C8 | 부분 타당 | 경미 | 각 description "a request that only sounds like this is not an invocation" 확인. 다만 `dia` 뒤에서는 router가 요청 문구를 description에 맞춰 보므로 문구 검토가 무의미하지는 않음 | 도구 |
| I25 | 비용 목록이 불완전하다 | R1 C9 | 타당 | 경미 | router 25행, conjecture Step 0, quaestio 39행, warrant Scope(31행) | 도구 |
| I26 | 평가 체계의 단서는 플러그인 안에 있었다 | R1 C11 | 타당 | 경미 | T38의 근거. 단 이는 시험이 있었다는 단서이지 준수 검사 하네스가 있다는 증거는 아님 | 도구 |
| I27 | T가 "반증 불가능한 믿음을 짚는 스킬이 없다"고 함의했다 | R1 C3 | 부분 타당 | 경미 | T는 그렇게 쓰지 않았고 51·53행에서 pull을 인정. 다만 50행 "비어 있습니다"가 quaestio 70행을 빠뜨린 것은 맞음(T12) | 도구 |
| I28 | T가 시장 예는 "갈 곳이 없다"고 했다 | R1 C4 | **과장** | 경미 | T 50행은 "`conjecture`는 몬스터 배제를 잡지만 엄격 보편명제에 한합니다"라고 적어 conjecture 경로를 인정함. "goes nowhere"는 T의 문구가 아님. conjecture가 markets를 명시한다는 사실 자체는 정확 | 도구 |
| I29 | 사전 기준 문제는 quaestio에서만 실제이고, 한 번에 끝나는 스킬에는 합의할 상대가 없어 문제가 아니다 | R2 P1 | 부분 타당 | 경미 | 한 번에 끝난다는 인용 3건 확인. 그러나 reductio·negative Step 7은 이미 "the observation that would change the recommendation"을 사전에 적게 함(T5): 합의는 못 해도 사전 명시는 가능. IEP의 "consensus of the relevant scientific community"는 기본 진술에 관한 것이라 대화 양자 합의에의 적용은 조건 불일치 | 도구, 요약 |
| I30 | 감사의 핵심(형식 분류, 존재·무기한 주장, 면역화 명명)에는 새 스킬이 **필요하다** | R2 P3 | 부분 타당 | 중대 | 빈자리의 사실은 확인(T11, T25, I6). "필요"는 R2 자신이 "a scope decision, not a fix for broken behavior"라 적어 낮춤. 빈도·기준선 증거 없음 | 도구, 재도출 |
| I31 | 보조가설 기록은 reductio로, 결정 규칙은 techne로 이미 풀 수 있다 | R2 P3 c, d | 부분 타당 | 경미 | reductio 30·34·73행, techne 28행 확인. 그러나 reductio는 모순 도출의 전제 목록이지 시험 전에 고정하는 보조가설 기록이 아니고(R2도 빈틈을 적음), techne는 요청으로 시작되지 않음(router 64행) | 도구 |
| I32 | 플러그인이 효과 증거가 없음을 스스로 인정한다 | R2 P5 | 부분 타당 | 경미 | 인용 3건 확인. 범위가 좁음: theory.md 56행은 "this method"(conjecture), counterplan 16행은 그 형식, evidence.md 5행은 regula의 연구에 관한 말 | 도구 |
| I33 | 14번째 스킬은 지시 부담과 router 동률을 늘린다(Rule 3, "1 of 4 runs") | R2 반대 논거 2 | 부분 타당 | 경미 | Rule 3 인용 확인(26행). "1 of 4 runs"는 Haiku의 기준선 점검 한 건(evidence.md 123행)이라 일반화는 조건 불일치. T30과 같은 유추 | 도구 |
| I34 | "실험 설계해 줘"의 현재 경로 | R1 E("None fits") / R2("techne를 고르되 보낼 형식 한 줄만 답함") | R2 타당, R1 부분 타당 | 경미 | router 64행 "never start from a request: reply in one line with the form to send". 어느 쪽이든 T의 "새 스킬 아님"에 영향 없음 | 도구 |
| I35 | 나머지 라우팅 예측(마케팅 전략, 약 효과 등) | R1 E; R2 표 | 확인 불가 | 경미 | router의 선택은 모델 판단이고 아무도 실행하지 않음 | 재도출 |
| I36 | 포퍼: 순수 존재명제 반증 불가 / 두 층 / 뒤엠-콰인 | R1 D1, D3, D5; R2 | 타당 | 경미 | T17, T18, T21의 근거 | 요약 |
| I37 | 보조가설을 한정 없이 면역화 장치로 든 것은 과장이며 ad hoc 여부 시험이 필요하다 | R1 D4 | 타당("용량 부족" 예는 부분 타당) | 경미(설계 조건) | T23. "용량 부족"은 용량을 미리 정하면 시험 가능하나, 상한 없이 사후에 쓰면 ad hoc | 요약, 재도출 |
| I38 | 뒤엠-콰인은 "텍스트만으로 충분"(논리적 층)도 약화한다 | R1 D5 | 타당 | 경미 | IEP 인용(T21). 대부분의 경험적 주장은 보조가설 없이 관찰 진술을 내지 않음 | 요약, 재도출 |
| I39 | 확률 진술과 결정 규칙(LScD 8장) | R1 D2; R2 P3c | 확인 불가 | 경미 | T20 | 기억 |
| I40 | 가벼운 대안(quaestio stress 안내 + conjecture 한 줄)이 주 권고가 되어야 한다 / 평가 먼저, 그다음 Step 0 수정, 새 스킬은 평가가 실패를 보일 때만 | R1 F; R2 반대 논거 | 부분 타당 | 중대 | 빈자리가 좁다는 점(I1, I5)과 기준선 증거 부재(I2)는 성립. 그러나 R1 스스로 router가 "is this falsifiable?"에 quaestio를 고르지 않는다고 적었고, 어느 쪽이 나은지는 출처로 정할 수 없음(빈도, 기준선). T는 이미 새 스킬을 조건부·3순위로 둠 | 도구, 재도출 |
| I41 | R1 "Checked and correct" 목록(T의 인용 다수가 정확함) | R1 C | 타당 | 경미 | 목록의 항목을 모두 다시 확인함 | 도구 |

## 5. 보고서의 오류

1. **R1 A2 / F, "고유 내용은 기록 필드 둘과 정렬뿐"**: 과장. R1 A1 자신의 문장 "a one-pass verdict on logical form … a `--target` for pasted text"와 맞지 않고, conjecture 56행("Record the answer as the criterion")에는 기준 전면 거부의 라벨이 없습니다.
2. **R1 C4, T가 시장 예는 "goes nowhere"라 했다**: 과장. T 50행 "`conjecture`는 몬스터 배제를 잡지만 엄격 보편명제에 한합니다."
3. **R1 B1, "don't manufacture doubt"**: 조건 밖 적용. 원문은 "If the idea is already precise (…), say so and offer …; don't manufacture doubt"(quaestio 43행)로, develop 모드 일반이 아닙니다. 경미.
4. **R2 P4, "한 메시지 한 질문"과 고정 라벨은 기계적으로 검사된다**: 과장. quaestio 20행 "two asks joined into one sentence still count as two, even under one question mark", conjecture 28행 "including labels and the fixed result values".
5. **R2 P2, severity 필드 규칙을 시험 엄격성 등급에 적용**: 조건 불일치. warrant 84–90행은 "When another agent fixes the output format"의 발견 심각도 필드입니다. 경미.
6. **R2 P1, IEP "consensus of the relevant scientific community"**: 조건 불일치. 기본 진술의 수용에 관한 문장이며 대화 두 당사자의 사전 합의가 아닙니다. 경미(요약 경유).
7. **R2 P5, "The plugin admits it has no evidence of effect"**: 출처보다 넓은 범위. theory.md 56행은 "No study has tested **this method** with users". 경미.
8. **R2 반대 논거 2, "skills loading in as few as 1 of 4 runs"**: 조건 불일치. evidence.md 123행 "Haiku loaded the skill under test in 1 of 4 runs of a baseline check". 경미.

## 6. 일관성 점검

고정한 읽기 ①–③과 "regula Rule 3·4의 스킬 간 확장은 유추", "adjudicate 재판정은 문면상 가능하나 빠듯함"을 T와 두 보고서에 똑같이 적용했는지 쌍으로 확인했습니다. 바꾼 것 둘: T30을 성립 → 부분 성립(I33과 같은 기준), I19(R2의 "기계적")를 타당 → 과장(T36·I18과 같은 기준).

## 7. 확인했고 문제없음

- T의 직접 인용: "A holding result must fill Tried", "in `stress`, at least one falsification pull", "the observation that would change the recommendation", "Support, not truth", "never whether the claim is true", "Favours the plan if: an observation", "Do not write the reports yourself", "Choose the one dia skill whose description … fits", "fixed numbers", "print the thirteen rows", "only Markdown, YAML and JSON files … no scripts, hooks, MCP servers or binaries", "strongest reasonable reading", "least warrant", "Fewer instructions". 모두 원문과 일치합니다(T6의 생략부만 예외).
- R1의 인용 전부(quaestio, conjecture, counterplan, warrant, negative, regula, adjudicate, emend, router), R2의 인용 전부(위 스킬과 elenchus, techne, theory.md, evidence.md, brief-template, record-template). 글자 단위 불일치는 찾지 못했습니다. 문제는 5절의 적용 범위뿐입니다.
- "Thirteen"은 README 3행과 `.claude-plugin/plugin.json`에 있고, 스킬 폴더는 14개(router 포함), 메뉴는 13행입니다.

## 8. 확인하지 못함

| 항목 | 찾아본 곳 | 막힌 이유 | 무엇이 해결하나 |
|---|---|---|---|
| (가-2) 빈자리의 실제 발생 빈도 (C가 기댐) | 플러그인 전체 | 사용 기록이 자료에 없음 | 사용자의 dia 사용 기록·요청 사례 |
| "is this falsifiable?"류 입력에 일반 답변(None fits)이 충분한가 (C가 기댐) | router, 두 보고서 | 아무도 실행하지 않음 | 라우팅 시험표 입력으로 스킬 없는 답과 비교 실행 |
| router가 각 입력에서 실제로 고르는 스킬 (I35) | router SKILL.md | 선택은 모델 판단 | `dia <입력>` 실제 실행 여러 번 |
| 저장소에 준수 검사용 평가 체계가 있는가 (T38) | 플러그인(단서만 있음) | 저장소는 이번 출처 범위 밖 | 저장소 `docs/research/` 확인 |
| 포퍼: 확률 진술은 엄밀히 반증 불가, 방법적 결정 필요 (T20, I39) | IEP·SEP에 직접 질문, 공개 검색 1회 | 요약에 해당 문장 없음. 원전 미열람 | *Logic of Scientific Discovery* 8장 원문 |
| arXiv:2506.07962, Huang et al. 2024의 실제 내용 (T40) | 플러그인의 인용만 | 열지 않음(T도 미검증 표시) | 논문 원문 |

## 9. 결정적 쟁점

**I1 + I2 (I4와 묶임): (가-2)의 빈자리가 새 스킬을 세울 만큼 남는가.** 이것이 고쳐지면 C의 (가-2) 항이 "새 스킬 후보"에서 "기존 스킬 수정"으로 바뀝니다.

- 출처로 확정되는 것: 빈자리는 T가 쓴 것보다 **좁습니다**. quaestio stress가 보유자에게 묻는 대화를 이미 갖고 있고, conjecture가 경험적 보편명제와 사전 기준을 이미 받습니다. T가 quaestio를 뺀 이유는 절반만 성립합니다.
- 출처로 확정되는 잔여: 비보편 경험적 주장에 "반증 가능한가"를 받는 스킬이 없고, 형식 판정·결정 규칙·고정 보조가설·기준 전면 거부의 라벨이나 기록이 어디에도 없으며, conjecture는 무기한 주장에서 오도하는 라벨로 끝날 수 있습니다(I6).
- 출처로 정할 수 없는 것: 그 잔여를 새 스킬로 채울지, 가벼운 수정으로 채울지. 빈도와 기준선 비교가 있어야 합니다. 따라서 T의 "조건부"는 유지되고, R1의 "가벼운 대안이 주 권고여야 한다"와 R2의 "새 스킬이 필요하다"는 둘 다 증거보다 한 걸음 더 나간 것입니다.
- I4의 관계: T가 대화형이어야 한다는 근거로 든 시장 예가 실제로는 형식 층의 예라서, 새 스킬을 만든다면 수정이 만족해야 할 조건은 "기한 없는 주장은 형식상 반증 불가로 판정하고, 기한을 붙인 판본은 주장 변경으로 기록한 뒤에만 보유자에게 묻는다"입니다.

(나)와 (가-1)의 방향은 두 보고서 모두에서 살아남았고 출처와 맞습니다. (가-1)에서는 Tried 추가가 사실상 이름 통일이라는 점(I10)만 좁혀집니다.

## 10. 사람이 확인할 것

**반드시 확인** (C에 대한 영향이 큰 순):

1. I2b: R1의 "고유 내용은 필드 둘뿐"을 과장으로 판정함. 결정적 쟁점에 직접 걸립니다.
2. 확인 불가(C가 기댐): 빈자리의 빈도.
3. 확인 불가(C가 기댐): 일반 답변이 충분한지(기준선).
4. I28: R1 C4를 과장으로 판정함(T 50행 읽기에 달림).
5. I19: R2의 "기계적 검사"를 과장으로 판정함. 6절에서 바꾼 판정입니다.
6. T30: 6절에서 성립 → 부분 성립으로 바꾼 판정입니다.
7. 5절 3번: R1 "don't manufacture doubt" 조건 밖 적용.
8. 5절 5번: R2 severity 필드 조건 불일치.
9. 5절 6번: R2 IEP "consensus" 조건 불일치(요약 경유).
10. 5절 7번: R2 "no evidence of effect" 범위.
11. 5절 8번: R2 "1 of 4 runs" 조건 불일치.

개수 대조: 과장 판정 3건(I2b, I19, I28) + 5절의 나머지 5건 + C가 기대는 확인 불가 2건 + 6절 변경 2건(그중 I19는 과장과 중복) = 11행. 위 목록과 일치합니다.

**요약에 기댐**: 판정 8건(T17, T18, T21, T23, I29의 IEP 부분, I36, I37, I38)이 요약 경유 웹 확인에 기댑니다. 원문 표현이 다르면 바뀔 수 있는 것은 T23/I37(보조가설의 정당한 도입 조건)과 5절 6번입니다. 요약만으로 보고서 항목을 "틀림"으로 판정한 것은 없습니다.

이 문서는 T의 주장과 두 보고서 항목의 증거를 판정한 것이며, C가 참이거나 거짓이라는 증명이 아닙니다.

출처(웹): [IEP, Karl Popper: Philosophy of Science](https://iep.utm.edu/pop-sci/), [SEP, Karl Popper](https://plato.stanford.edu/entries/popper/). 검색 결과로 나왔으나 근거로 쓰지 않은 것: [Applying Popper's Probability (arXiv:1412.7736)](https://arxiv.org/abs/1412.7736).
