# dia 플러그인 스킬과 반증가능성 분석

대상: `dia` 플러그인 v2.11.0. 설치본 `/mnt/skills/plugin-files/dia`에 있는 스킬 14개(13개 + `dia-router`), 각 스킬의 `references/`, `README.md`.
작성일: 2026-11-10

---

## 0. 요약

- **축 A, 방법으로서의 반증.** 반증을 정면으로 구현한 스킬은 세 개입니다. `dia-conjecture`는 반례를 쓰고, `dia-reductio`는 모순을 도출하며, `dia-negative`는 내재적 결함을 찾습니다. 외부 검증을 통과 기준으로 삼아 반증 구조를 갖춘 스킬은 세 개입니다(`dia-ratchet`, `dia-adjudicate`, `dia-emend`). "무엇이 보이면 생각을 바꿀 것인가"를 끌어내는 스킬도 세 개입니다(`dia-quaestio`, `dia-counterplan`, `dia-warrant`). 나머지 다섯 스킬(`skopos`, `elenchus`, `regula`, `techne`, `router`)은 반증 방법이 아닌 절차·정의·규범 스킬입니다. 다만 `skopos`와 `techne`에는 반증과 같은 구조의 규칙이 들어 있습니다.
- **플러그인 전체에 공통된 반증주의적 습관은 여섯 가지입니다.**
  1. 비대칭 결과 표기: "증명됨"이라는 결과가 없습니다.
  2. 반박 조건을 미리 정하거나, 생각을 바꿀 관찰을 명시합니다.
  3. 면역화를 금지합니다. 몬스터 배제는 이름을 붙여 기록하고, 고집은 결함이 아닙니다.
  4. 증거 등급을 매기며, 기억은 결코 '검증됨'이 아닙니다.
  5. 뒤엠-콰인 문제를 인정합니다. 어느 전제를 버릴지는 논리가 정하지 않고 사용자가 정합니다.
  6. 내용 손실을 장부에 적습니다. 무엇이 더는 포괄되지 않는지를 남깁니다.
- **축 B, 스킬 자체의 반증가능성.**
  - **형식 준수 주장은 반증가능성이 매우 높습니다.** 고정 결과 라벨, 기록 필드, 한 메시지 한 질문 같은 규칙은 대화 기록만으로 위반 여부를 판정할 수 있습니다.
  - **플러그인이 사용자에게 주는 효과(추론의 질 향상)는 어디에도 진술되지 않았고, 시험 기준도 없습니다.** 반증 불가능하다기보다는 아직 반증 대상으로 제시되지 않은 상태입니다.
  - **근거 주장에는 한계가 있습니다.** `regula`의 근거는 비공개 자체 평가이고, `adjudicate`의 근거는 "trials"입니다. 둘 다 산술 외에는 상호주관적으로 점검할 수 없습니다. `regula/references/evidence.md`는 이 사실을 스스로 밝히고 있습니다.
- **권고(제안).** 스킬마다 "이 출력이 보이면 스킬이 실패한 것"이라는 실패 관찰 목록을 두고, 플러그인 수준의 효과 가설을 하나 진술하는 것을 권합니다. §3.4와 §4에 초안이 있습니다.

> **근거 표기.** [읽음]은 이번 세션에 설치본 파일을 직접 읽은 것입니다. [훑음]은 해당 파일을 grep이나 앞부분 위주로만 읽은 것입니다. [추론]은 제 해석입니다. [제안]은 제가 권하는 것으로, 채택 여부는 사용자가 정합니다. 외부 소스는 조회하지 않았으므로, 플러그인이 인용하는 논문이 실제로 그렇게 말하는지는 이번에 확인하지 않았습니다.

---

## 1. 기준선: 여기서 "반증가능성"이 뜻하는 것

분석에 쓰는 이론 요소입니다. 모두 기억에 기댄 일반 지식이며 미검증입니다. 다만 아래에 적은 대로 플러그인 자체가 인용하는 부분과는 일치합니다.

| 요소 | 내용 | 플러그인 안의 직접 언급 |
|---|---|---|
| 포퍼의 구획 기준 | 어떤 관찰로도 반박될 수 없는 주장은 경험적 주장이 아님 | `quaestio` "falsification pull" [읽음] |
| 사전 반박 기준 | 어떤 관찰이 반박인지 **미리** 합의해야 함 | `conjecture` Step 2 "Prior criterion", theory.md §5가 *Conjectures and Refutations* 인용 [읽음] |
| 반증–확증 비대칭 | 통과한 시험은 확증(corroboration)일 뿐 증명이 아님 | 결과 라벨 전반 (§2.2) |
| 면역화 금지 (규약주의 전략·ad hoc 금지) | 반례를 정의 변경으로 피하는 것 | `conjecture` 몬스터 배제와 Lakatos Rule 2 [읽음] |
| 라카토슈의 증명과 반박 | 국소·전역 반례, 숨은 보조정리, 보조정리 편입 | `conjecture` 전체 [읽음] |
| 뒤엠-콰인 | 모순은 집합이 함께 성립할 수 없음만 보이고, 어느 원소가 거짓인지는 말하지 않음 | `reductio` hard rule 6, theory.md [읽음] |
| 엄격한 시험(severity) | 틀렸다면 실패했을 시험만 가치 있음 | 명시적 언급 없음. `ratchet`의 "lower bound"와 `conjecture`의 **Tried** 필드가 이 기능을 함 [추론] |

---

## 2. 축 A — 각 스킬은 반증을 어떻게 구현하는가

### 2.1 스킬별 판정

| 스킬 | 반증 관련 역할 | 핵심 장치 (근거) |
|---|---|---|
| **dia-conjecture** | **반증 엔진(경험·수학)** | 한 번에 반례 하나. 반례가 맞는지는 조건별 점검으로 보여 줌(hard rule 2). 몬스터 배제에 이름을 붙이고 Rule 2를 인용함. "never call C proved"(Step 6). 경험적 C에는 포퍼의 사전 반박 기준을 물음(Step 2). 유지된 결과에는 **Tried**를 반드시 채움("a claim nobody pressed has not held") [읽음] |
| **dia-reductio** | **반증 엔진(논리)** | 엄격한 모순(Q와 not-Q)만 인정하고, 반대 관계는 전제를 추가해야만 씀(rule 1). [T]/[L]/[A] 전제 라벨을 붙임. 모든 전제가 [L]일 때만 "thesis is false"라고 씀(rule 6, 뒤엠-콰인). "carried by added premises" 검사로 순환 논증을 탐지함(Step 5). "no contradiction found"는 일관성을 뜻하지 않음 [읽음] |
| **dia-negative** | **반증 엔진(내적 기준)** | 결함은 C, 사례 D, 둘이 함께 성립할 수 없다는 증명의 세 부분을 갖출 때만 인정(rule 2). 작동 기능 추론에는 사용자가 실제로 할 수 있는 반증 관찰을 붙여야 함(rule 6, Step 5). theory.md는 이를 아도르노가 반대했을 **포퍼식 추가물**이라고 스스로 밝힘 [읽음] |
| **dia-quaestio** | 반증 조건 추출 | "Falsification pull": 아무것도 반박할 수 없는 믿음은 강점이 아니라 발견 사항임(Step 2). 이는 구획 기준을 거의 그대로 옮긴 것. 다만 필수 사항은 `stress` 모드에서만이며 최소 1회(Step 2). verdict `refuted`는 경험적 반증이 아니라 사용자 발언끼리의 충돌을 뜻함 [읽음/훑음] |
| **dia-counterplan** | 반증 조건 추출(결정) | 쌍마다 "Favours the plan if: an observation the user could make"를 적음. 판정을 내리지 않고, 판정할 관찰을 이름 붙임(rule 5). "Hearing both sides is not evidence that the plan was tested" [훑음] |
| **dia-warrant** | **명시적으로 반증이 아님** | 대상은 철회 가능한(defeasible) 주장. 반례 하나는 반박이 아니라 rebuttal 조건이며, 이 경우는 `conjecture`로 보냄(Scope, `conjecture` Step 0). 진리가 아니라 지지만 판정함(rule 1). 결과는 "not a proof" [읽음] |
| **dia-ratchet** | 외부 반증 게이트(수정 루프) | 모든 검사 가능 주장을 결함 가설로 세움("confirmed if the claim proves wrong, refuted if it holds", 라운드 1단계). 외부 증거만 인정하고, 재도출은 불인정. 통과한 항목은 잠금(확증). "zero defects … is not a clean bill" [읽음] |
| **dia-adjudicate** | 외부 반증 게이트(판정) | 뒤집으려면 출처의 문구를 같은 논점에서 인용해야 함(rule 3). "Unverifiable is not false"(rule 4). "Agreement is not evidence"(rule 2). 두 번 실행해 서로 다른 항목을 사람이 점검 [읽음] |
| **dia-emend** | 약한 반증 게이트(1회) | 재도출을 확정 근거로 인정(Step 4). 확인되지 않은 의심 항목은 "(suspected, unverified)". 근거 없는 압력에는 답을 뒤집지 않음 [읽음] |
| **dia-elenchus** | 내적 일관성 반박(정의) | 합의된 전제만 쓰고, 문구 때문에 동의한 전제로 세운 반박은 무효(rule 3). 경험적 반증이 아니라 정의의 자기모순을 다룸 [훑음] |
| **dia-skopos** | 비반증, 단 구조는 같음 | 관찰 가능한 완료 기준. 프록시는 무엇을 보여 주지 못하는지 함께 적음. 결과는 관찰될 때까지 "unverified"로 둠. 결과물의 완성과 결과의 실현을 분리함 [읽음] |
| **dia-techne** | 비반증, 단 외부 점검 | 질문 4: 모델과 사용자가 아닌 것이 결과를 보여 주게 함. 반대편을 논하는 별도 에이전트. "a session that grades its own work finds what it expects" [읽음] |
| **dia-regula** | 비반증(규범) | 지시문 작성 규칙. 다만 `evidence.md`에서 규칙마다 근거의 강도를 공개함. 축 B의 사례로 다룸(§3.2) [훑음] |
| **dia-router** | 무관 | 메뉴와 라우팅만 담당 [훑음] |

### 2.2 공통 모티프 (플러그인 수준의 반증주의)

1. **비대칭 결과 라벨.** 어떤 스킬에도 "참"이나 "증명됨"이라는 결과는 없습니다 [읽음].
   - `conjecture`: "holding against the cases tried"
   - `reductio`: "untenable on these premises" / "no contradiction found"
   - `negative`: "holding against the tested particulars"
   - `warrant`: "not a proof"
   - `ratchet`: "not a clean bill"
   - `adjudicate`: "not a proof that C is true or false"
   
   이는 반증–확증 비대칭을 출력 형식 차원에서 강제한 것입니다.
2. **생각을 바꿀 관찰.** `reductio` Step 7과 `negative` Step 7은 권고마다 "the observation that would change the recommendation"을 요구합니다. `counterplan`은 쌍마다 관찰을 적고, `conjecture`는 사전 기준을 묻습니다 [읽음/훑음]. 권고까지 반증 가능한 형태로 만든다는 점이 눈에 띕니다.
3. **면역화 금지.**
   - "Withdraw only for a named defect" / "insistence is not a defect" (`conjecture`, `reductio`, `negative`, `warrant`, `adjudicate`)
   - 몬스터 배제는 이름을 붙여야 하고, 정의 변경으로만 받아들임 (`conjecture`)
   - 이 규칙들은 **양방향**입니다. 사용자가 반례를 회피하는 것도, 모델이 압력에 굴복하는 것도 막습니다(`emend`, `ratchet` Guardrails) [읽음].
4. **증거 등급.** 거의 모든 스킬이 같은 사다리를 씁니다: verified this session / supplied by the user / single source / unverified recall. 그리고 "own recall is never verified"를 원칙으로 둡니다. `conjecture`는 미검증 기억에만 기댄 반례로 강제된 C′에 **conditional** 표시를 붙입니다 [읽음]. 반증의 무게를 증거의 질에 묶어 두는 장치입니다.
5. **뒤엠-콰인의 처리.** `reductio`는 모순이 기대는 전제 집합 전체를 제시하고, 무엇을 버릴지는 사용자에게 맡깁니다. `conjecture`는 국소·전역·양쪽 라벨로 무엇이 반박되었는지 위치를 정합니다 [읽음]. 반증이 "어디에" 떨어졌는지를 구조화한 것입니다.
6. **내용 손실 장부.** 수정이 일어날 때마다 무엇을 잃었는지 적게 합니다.
   - `conjecture`: "content lost", "what it no longer covers"
   - `negative`: "What escapes", "remainder"
   - `reductio`: T′ "still does the job"
   
   [추론] 포퍼의 관점에서 ad hoc 수정이 나쁜 이유는 경험적 내용을 줄이기 때문입니다. 이 장부는 그 감소를 보이게 만들어, 수정이 내용을 좁혔는지 판정할 수 있게 합니다.

### 2.3 축 A에서 보이는 공백과 긴장

- **사전 반박 기준이 한 곳에만 있습니다.** 포퍼의 사전 기준을 명시적으로 묻는 곳은 `conjecture` Step 2뿐입니다. `quaestio`의 falsification pull은 사후에, 그리고 `stress` 모드에서만 필수입니다. `warrant`는 rebuttal 슬롯이 비슷한 기능을 하지만 "none given"이면 채우지 않습니다(rule 2) [읽음]. [제안] 경험적 주장을 다루는 `quaestio`(develop 모드)와 `counterplan`에도 "미리 합의한 반증 관찰"을 기록 필드로 둘 수 있습니다.
- **엄격성(severity)에 대한 명시적 개념이 없습니다.** `conjecture`는 "the case most likely to be valid"를 고르고 **Tried**를 기록합니다. `ratchet`은 확인된 결함이 하한임을 인정합니다. 그러나 `reductio`, `negative`, `warrant`에는 시도한 검사가 얼마나 엄격했는지 기록하는 필드가 없습니다. 예외적으로 `reductio`의 "no contradiction found"에는 시도한 방향과 전제 집합 목록이 붙습니다 [읽음]. [추론] 유지 판정이 약한 시험에서 나온 것인지 강한 시험에서 나온 것인지 기록만으로는 구별되지 않습니다.
- **시험자와 피시험자가 같은 모델입니다.** `counterplan`은 이 점을 스스로 인정합니다("the format obliges a counter-case but cannot ensure it is as strong as the plan"). `target=claude` 모드는 모두 "self-examination and not independent"라고 표시합니다 [읽음]. 플러그인은 세 경로로 이를 보완합니다.
  1. 판정 권한을 사용자에게 넘김(`conjecture`, `counterplan`)
  2. 외부 도구 결과만 증거로 인정함(`ratchet`, `adjudicate`)
  3. 독립 실행(`adjudicate`의 두 번 실행, `techne`의 별도 에이전트)
  
  포퍼가 말한 상호주관적 비판에 가장 가까운 것은 3번입니다. 그런데 3번은 `adjudicate`와 `techne`에만 있습니다.
- **라카토슈의 연구 프로그램 수준은 다루지 않습니다.** `conjecture`는 *Proofs and Refutations* 1장의 기법만 다루고, 7–9절은 구현하지 않았다고 밝힙니다(theory.md §4) [읽음]. 다만 Step 6의 "If the repairs have turned into a list of exceptions, say so"는 퇴행(degenerating) 프로그램을 탐지하는 기능을 합니다 [추론]. 수리가 새 내용을 예측하는지(진보적인지)는 검사하지 않고, "C′ not yet tested"만 기록합니다.
- **사용자 판정이 곧 반증의 문턱입니다.** `conjecture`는 "The user rules"를 원칙으로 둡니다. 사용자가 근거 없이 반대하면 사례는 disputed로 남고 결과는 **open**이 됩니다. 정의를 바꿔도 disputed 사례는 결과에서 빠지지 않습니다(Step 6) [읽음]. 사용자가 반증을 막을 수는 있지만 **숨길 수는 없게** 설계된 것으로, 이 긴장을 잘 처리하고 있습니다 [추론].

---

## 3. 축 B — 스킬 자체는 반증 가능한가

질문은 이렇습니다. 각 스킬 텍스트가 하는 주장 가운데, 어떤 관찰이 나오면 그 주장이 틀렸다고(스킬이 실패했다고) 판정할 수 있는가?

### 3.1 스킬 텍스트 속 주장의 네 유형

| 유형 | 예 | 반증가능성 | 판정 방법 |
|---|---|---|---|
| **(a) 형식·준수 주장** | 한 메시지 한 질문, 고정 결과 라벨 중 정확히 하나, 기록 필드, 인용부호 안은 원문 그대로, "thesis is false"는 모든 전제가 [L]일 때만, 승인 전 미실행(`skopos`) | **높음.** 위반 여부가 대화 기록에서 바로 드러남 | 대화 기록 검사. 상당수는 스크립트로 자동 판정 가능 [추론] |
| **(b) 판단 의존 규칙** | "strongest reasonable reading"(`reductio` rule 5), "least warrant"(`warrant` rule 3), "most suspect lemma"(`conjecture`), "the one the target most plausibly means"(`negative` rule 3) | **중간.** 위반 판정에 평가자의 판단이 필요함 | 복수 평가자와 평가자 간 일치도 [제안] |
| **(c) 경험적 근거 주장** | Huang et al. 2024(재판단만으로는 개선이 없음; `ratchet`, `emend`, `adjudicate`), arXiv:2506.07962(같은 모델의 오류 상관; `adjudicate`), Schweiger 외 1989(`counterplan` theory), `regula` evidence.md의 자체 평가, `adjudicate`의 "trials", `ratchet`의 "have been reported to block" | **출처에 따라 다름** | 공개 논문은 원문 대조(이번 세션에서는 미실행). 비공개 평가와 일화는 산술 외에는 점검 불가 |
| **(d) 효과 주장** | "이 스킬을 쓰면 추론이 나아진다" | **진술되지 않음** | 아래 §3.3 |

### 3.2 근거 주장의 투명성: `regula`가 기준점

`dia-regula/references/evidence.md`는 플러그인 안에서 유일하게 측정 프로토콜과 그 한계를 공개합니다 [읽음].

- 출처는 저자의 비공개 연구이며, 실행·프롬프트·트레이스가 공개되지 않아 "checked for arithmetic but not against raw data" 수준입니다.
- 모델 버전을 기록하지 않았습니다.
- 빌드 사이에 나머지 지시문이 바뀌었으므로 같은 모델·빌드 안에서만 비교할 수 있습니다.
- Rule 1의 A/B는 "below the A/B standard in SKILL.md"입니다.
- Fisher p값은 재계산해 일치를 확인했고, permutation p값은 재계산하지 않았습니다.

[추론] 이는 포퍼적 정직성의 좋은 예입니다. 무엇이 점검되었고 무엇이 점검되지 않았는지를 구분합니다. 그러나 데이터가 비공개이므로 **상호주관적으로 반증 가능하지는 않습니다.** `adjudicate`의 lineage는 "rules drawn from adjudication trials, docs/research/dia-adjudicate.md"를 가리킵니다. 이 문서는 설치본에 없고, 저장소에 공개되어 있는지는 이번에 확인하지 않았습니다(외부 조회 없음, 미검증).

### 3.3 효과 가설의 부재: `skopos`의 기준을 플러그인에 적용하면

`dia-skopos`는 다른 작업에 결과물(deliverable)과 그 너머의 결과(outcome)를 분리하라고 요구합니다. 프록시는 무엇을 보여 주지 못하는지 적고, 결과는 관찰될 때까지 "unverified"로 두라고 합니다 [읽음]. 같은 기준을 플러그인 자신에게 적용해 보면 다음과 같습니다 [추론].

- **결과물:** "각 스킬이 자기 규칙대로 동작한다." 유형 (a)와 (b)로 점검할 수 있습니다.
- **결과:** "사용자가 더 잘 추론하고 결정한다." 또는 "모델이 압력에 굴복하는 일이 줄어든다." README와 plugin.json은 기능만 설명하고, 이런 결과 가설을 진술하지 않습니다 [읽음]. 플러그인 안에 평가 스위트나 테스트 파일도 없습니다(설치본 디렉터리 목록 기준) [읽음].
- **판정:** 결과는 **unverified**이며, 판정할 기준이 아직 없습니다. 효과 주장을 하지 않는다는 점은 겸손하지만, 그 결과 플러그인의 핵심 가치는 반증될 기회를 얻지 못한 상태입니다.

### 3.4 면역화 위험이 있는 설계 지점

포퍼의 "규약주의 전략"(실패를 성공으로 재해석할 수 있게 만드는 장치)에 해당할 수 있는 곳들입니다. 각 장치의 이유는 타당하지만, 반증가능성을 지키려면 **비율을 측정**해야 합니다 [추론/제안].

1. **"expected behavior, not a failure".** `ratchet`의 "Without tools"와 `adjudicate`의 "Without tools"가 그렇습니다 [읽음]. 도구 없이 아무것도 검증하지 못한 실행은 정의상 실패로 셀 수 없습니다. [제안] 이를 실패에서 제외하되, 도구가 **있는** 조건에서 "verification exhausted"로 멈추는 비율을 따로 측정합니다.
2. **"zero defects … is not a clean bill", "not a proof".** 확증을 과장하지 않는 장치입니다. 다만 결함을 못 찾은 실행과 못 찾을 수 없었던 실행이 같은 라벨을 받습니다. [제안] 오류를 심어 둔 입력(seeded errors)으로 재현율을 측정하면 반증 가능해집니다.
3. **결과가 사용자 판정에 좌우됩니다.** `conjecture`, `counterplan`, `elenchus`에서 나쁜 결과는 언제든 사용자 판정 탓으로 돌릴 수 있습니다. 반증주의에서 보조가설로 실패를 흡수하는 것과 같은 구조입니다. [제안] 시험할 때는 사용자 응답을 고정한 스크립트(시뮬레이션된 사용자)를 써서 이 변수를 통제합니다.
4. **템플릿 대체 경로.** "if you cannot open the template, follow …"는 형식 위반을 피할 탈출구가 될 수 있습니다. 다만 대체 기록 필드가 각 SKILL.md에 열거되어 있으므로 판정은 여전히 가능합니다 [읽음].

### 3.5 스킬별 실패 관찰 초안 [제안]

각 항목은 대화 기록에서 관찰할 수 있으며, 하나라도 나오면 그 실행은 스킬 규칙을 어긴 것입니다. 괄호 안은 근거 규칙입니다.

| 스킬 | 실패 관찰 (예) |
|---|---|
| conjecture | C를 "증명됨"이라고 부름 (Step 6) · 점검 없이 반례 제시 (hr 2) · 사용자가 고르기 전에 C′를 채택된 것으로 씀 (hr 7) · 수용된 반례를 좁힌 정의로 배제했는데 몬스터 배제라 명명하지 않음 (Step 4) · 유지 결과인데 **Tried**가 비어 있음 |
| reductio | 반대 관계만으로 모순 선언 (hr 1) · 규칙 표기 없는 도출 단계 (hr 3) · [A] 전제가 있는데 "thesis is false" (hr 6) · [A] 전제가 있는데 "carried by added premises" 점검 누락 (Step 5) |
| negative | 세 부분을 갖추지 못한 결함 (hr 2) · 대상이 밝히지 않은 외부 가치 사용 (hr 1) · 작동 기능 추론에 반증 관찰 없음 (hr 6) |
| warrant | "the claim is false" 서술 (hr 1) · 대상이 말하지 않았는데 보증을 "all/always"로 재구성 (hr 3) · 열린 질문을 자기 반대 사실로 닫음 (hr 5) |
| ratchet | 검증 불가 항목을 수정 · 재도출을 검증으로 기록 · zero-defect 정지를 무결함으로 서술 · 새 외부 증거 없이 잠긴 항목 변경 |
| adjudicate | 출처 인용 없이 보고 항목을 뒤집음 (hr 3) · 동의한 보고서 수를 근거로 판정 (hr 2) · 본문에만 있고 표에는 없는 번복 (hr 11) |
| emend | 근거 없이 맞는 사실을 수정 · 구체 근거 없는 압력에 답을 뒤집음 · 실행하지 않은 점검을 "verified"로 표기 |
| quaestio | stress 모드에서 falsification pull 누락 · Step 3 전에 해결책 제시 · 한 메시지에 질문 둘 |
| counterplan | 어느 계획이 나은지 판정하거나 어조로 암시 (hr 5) · 새로 지어낸 사실 (hr 4) |
| elenchus | 조언 (rule 6) · 합의되지 않은 전제로 반박 (rule 3) |
| skopos | 승인 전에 결과물을 실질적으로 작성 · 프록시를 결과의 확인으로 서술 |
| techne | 백업 없이 되돌릴 수 없는 단계 실행 · 외부 점검 결과 대신 자기 평가 보고 |
| regula | 데이터로 넘길 자료를 규칙에 맞게 고쳐 씀 · 검토만 요청받았는데 수정 |
| router | `dia`로 시작하지 않는 메시지에서 스킬 실행 · 문장 속 숫자를 메뉴 선택으로 오인 |

**플러그인 수준의 효과 가설과 시험 초안 [제안].** 기준값은 시험 전에 정해야 합니다. 그래야 포퍼의 사전 기준이 됩니다.

- **H1 (압력 저항).** `emend`/`ratchet`을 쓰면 정답에 근거 없는 반박("틀린 것 같은데요")을 받았을 때 답을 뒤집는 비율이 기준선보다 낮다. 반증 조건: 차이가 사전에 정한 폭보다 작음.
- **H2 (오류 재현율).** 오류를 심어 둔 초안에서 `ratchet`/`adjudicate`의 확인 결함 재현율이 기준선보다 높고, 맞는 내용을 틀렸다고 뒤집는 비율은 일정 수준 이하이다.
- **H3 (면역화 탐지).** 시뮬레이션된 사용자가 몬스터 배제를 할 때 `conjecture`가 이를 명명하는 비율이 정해 둔 문턱 이상이다.

---

## 4. 종합 판단과 권고

**판단 [추론].** 이 플러그인은 반증주의를 특정 이론으로 가르치기보다 **출력 형식의 제약**으로 실천합니다. 비대칭 라벨, 증거 등급, 명명된 철회, 내용 손실 장부가 그 예입니다. 축 A의 수준은 높습니다. 특히 `conjecture`, `reductio`, `ratchet`은 각각 경험적·논리적·검증 절차의 반증 구조를 서로 겹치지 않게 나눠 맡습니다. 경계도 명시되어 있습니다. 예컨대 `warrant`와 `conjecture`는 철회 가능한 주장과 엄격히 보편적인 주장으로 나뉩니다.

축 B에서는 비대칭이 보입니다. 플러그인은 **남의 주장**에는 사전 기준과 반증 관찰을 요구하지만, **자기 자신**에 대해서는 형식 규칙만 반증 가능하게 쓰여 있습니다. 효과 가설은 진술되지 않았고, 근거 데이터는 일부 비공개입니다.

**권고 [제안]**

1. §3.5의 실패 관찰 목록을 스킬별 평가 명세로 정리합니다. 대부분은 유형 (a)이므로 스크립트로 판정할 수 있습니다.
2. 플러그인 수준의 효과 가설(H1–H3 같은 것)을 하나 이상 README 수준에서 진술하고, 사전 기준을 함께 둡니다.
3. "expected behavior, not a failure"로 지정된 경우는 실패에서 제외하되, 그 빈도를 따로 보고합니다.
4. 엄격성 필드를 다른 반증 엔진에도 확장합니다. `reductio`와 `negative`의 유지 결과에 `conjecture`의 **Tried** 같은 필드를 둡니다.
5. 사전 반박 기준을 `quaestio`(develop 모드)와 `counterplan`의 경험적 가정에도 기록 필드로 둘지 검토합니다.
6. `regula`와 `adjudicate`의 시험 데이터를 공개하거나, 공개하지 않는다면 `regula`처럼 "산술만 점검 가능"이라고 각 스킬에 표시합니다.

---

## 5. 이 분석의 한계

- **읽은 범위.** `conjecture`, `reductio`, `negative`, `ratchet`(+verification-sources), `warrant`, `emend`, `adjudicate`, `techne`, `skopos`는 SKILL.md 전문을 읽었습니다. `counterplan`, `quaestio`, `elenchus`, `regula`, `router`와 각 theory.md는 관련 구절 위주로 훑었습니다. 훑은 스킬에 관한 판정은 놓친 규칙이 있으면 바뀔 수 있습니다.
- **실행 시험 없음.** 이번에 어떤 스킬도 실행해 보지 않았습니다. 따라서 "이 규칙은 반증 가능하다"는 판정은 텍스트 분석일 뿐이고, 스킬이 실제로 규칙을 지키는지는 확인하지 않았습니다.
- **외부 출처 미조회.** 플러그인이 인용하는 논문(Huang et al. 2024 등)과 저장소의 `docs/research/`는 조회하지 않았습니다. 인용이 정확한지는 미검증입니다.
- **이론 기준선.** §1의 철학적 내용은 제 일반 지식에 기댄 것입니다. 플러그인 theory.md의 인용과 겹치는 부분 외에는 미검증입니다.
