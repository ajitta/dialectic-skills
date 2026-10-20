# Dialectic Skills (`dia`)

[English](README.md) | **한국어** | [日本語](README.ja.md) | [简体中文](README.zh-CN.md)

추론과 검토를 위한 스킬 일곱 개를 하나의 플러그인에 담았습니다. Agent Skills를 불러오는 모든 어시스턴트, 즉 Claude(웹, 데스크톱, 모바일, Claude Code), Codex, ChatGPT에서 수정 없이 실행되도록 작성했습니다. 패키지는 지침(Markdown, YAML, JSON)으로만 이루어져 있으므로 도구가 없는 채팅에서도 모든 스킬이 작동합니다. 스킬 파일은 영어로 작성되어 있으며, 각 스킬은 사용자가 쓴 메시지의 언어로 답합니다.

| 스킬 | 하는 일 | 시작 방식 |
|---|---|---|
| `dia-confirm` | 작업을 시작하기 전에 목표를 다시 정리하고, 중요한 가정을 밝히고, 사용자가 내려야 할 결정만 나열한 뒤 승인을 기다립니다. | 이름으로만 |
| `dia-elenchus` | 플라톤의 엘렝코스(논박술): "X란 무엇인가?"를 묻고, 한 번에 한 질문씩 전제에 합의하며, 모순을 드러냅니다. 수정할 때마다 그것이 사용자의 새로운 생각이 됩니다. 대개 아포리아로 끝나며, 조언은 하지 않습니다. | 이름으로, 또는 소크라테스식 대화를 요청해서 |
| `dia-brainstorm` | 현대적인 소크라테스식 질문을 한 번에 하나씩 던진 뒤, 사용자의 선택지와 표시를 붙인 최대 세 개의 제안, 기준에 따른 수렴, 결론, 요약서를 제시합니다. 구현은 하지 않습니다. | 이름으로, 또는 소크라테스식 브레인스토밍을 요청해서 |
| `dia-reductio` | 엄격한 귀류법을 한 번에 수행합니다: 표시를 붙인 전제, 줄마다 규칙을 밝힌 Q와 not-Q 도출, 등급을 매긴 강도, 선택지와 기록. | 이름으로, 또는 말로 요청해서 |
| `dia-negative` | 내부 비판(아도르노의 내재적 비판보다 좁은 의미)을 한 번에 수행합니다: 대상 자신의 기준, 사례와 "빠져나가는 것"을 갖춘 엄격한 간극, 반증 조건을 붙인 실제 작동 목적, 억지 종합 없는 선택지. | 이름으로, 또는 말로 요청해서 |
| `dia-refine` | 직전 답변이나 초안을 한 차례 검토합니다: 사실 오류, 논리적 비약, 누락된 요구 사항, 반복. 확인된 결함만 고칩니다. | 첫 단어를 `dia-refine`로, 또는 이름으로 |
| `dia-iterate` | 검토 라운드를 반복하며, 각 라운드는 외부 검증을 거쳐야 합니다. 퇴행, 결함 0건, 검증 수단 소진, 고정점 도달, `--max N`(기본값 3) 중 하나에 이르면 멈춥니다. | 첫 단어를 `dia-iterate`로, 또는 이름으로만 |

## 목차

- [빠른 시작](#빠른-시작)
- [설치](#설치)
- [호출 방법](#호출-방법)
- [예시](#예시)
- [여러 스킬 함께 쓰기](#여러-스킬-함께-쓰기)
- [문제 해결](#문제-해결)
- [저장소 구조](#저장소-구조)
- [개발](#개발)
- [라이선스](#라이선스)

## 빠른 시작

Claude Code:

```
/plugin marketplace add ajitta/dialectic-skills
/plugin install dia@dialectic-skills
```

Codex CLI:

```
codex plugin marketplace add ajitta/dialectic-skills
codex plugin add dia@dialectic-skills
```

claude.ai: Customize › Plugins › Add › Add marketplace에서 `ajitta/dialectic-skills`를 입력한 뒤, 목록에서 `dia`를 추가합니다.

그런 다음 이렇게 입력해 봅니다: `이 주장에 귀류법을 적용해 주세요: 재택근무는 언제나 생산성을 높인다.`

## 설치

계정이나 기기마다 한 가지 경로로만 설치합니다. 두 경로(예: 이 저장소와 [ajitta/claude-plugins](https://github.com/ajitta/claude-plugins) 카탈로그)로 설치하면 모든 스킬이 두 번씩 나타납니다.

### claude.ai 웹과 Claude 데스크톱

1. Settings › Capabilities에서 **Code execution and file creation**을 켭니다. dia 스킬은 코드를 실행하지 않지만, 스킬 기능 자체에 이 설정이 필요합니다.
2. Customize › Plugins › Add로 이동한 뒤, 다음 중 하나를 선택합니다.
   - **Add marketplace**에 `ajitta/dialectic-skills`를 입력하고, 목록에서 `dia`를 추가합니다. 마켓플레이스를 추가하는 것만으로는 아무것도 설치되지 않으므로 두 번째 단계가 필요합니다. 업데이트는 마켓플레이스를 통해 받습니다(Check for updates 또는 Sync automatically).
   - **Upload plugin**으로 최신 릴리스의 [`dialectic-skills.zip`](https://github.com/ajitta/dialectic-skills/releases/latest/download/dialectic-skills.zip)을 올립니다. Customize › Skills가 아니라 Customize › Plugins를 사용해야 합니다. Skills 화면은 플러그인 매니페스트가 들어 있는 zip을 거부합니다. 업로드한 플러그인은 스스로 업데이트되지 않으므로, 새 릴리스가 나올 때마다 다시 업로드해야 합니다.
3. 확인: 메시지 입력창에 `/dia`를 입력합니다. `dia:dia-brainstorm`부터 `dia:dia-refine`까지 일곱 개 항목이 나타나야 합니다.

### Claude 모바일 (iOS, Android)

별도의 설치 단계가 없습니다. claude.ai나 Claude 데스크톱에서 추가한 플러그인은 계정에 속하므로 모바일 앱에도 자동으로 반영됩니다. 모바일의 `/` 메뉴에는 플러그인 스킬이 표시되지 않으므로, 말로 요청하거나 메시지에 스킬 이름을 적습니다.

### Claude Code

```
/plugin marketplace add ajitta/dialectic-skills
/plugin install dia@dialectic-skills
```

- 업데이트: `/plugin marketplace update dialectic-skills`를 실행한 뒤 플러그인을 업데이트합니다(또는 해당 마켓플레이스의 자동 업데이트를 켭니다).
- 제거: `/plugin uninstall dia@dialectic-skills`.
- claude.ai에서 추가한 플러그인은 같은 계정으로 로그인하면 Claude Code에도 동기화됩니다. 명령줄에서 다시 설치하지 마십시오.
- 카탈로그를 통해 설치하려면: `/plugin marketplace add ajitta/claude-plugins`를 실행한 뒤 `/plugin install dia@ajitta`를 실행합니다. 코드는 같고 설치 이름만 다릅니다.

### Codex 앱, CLI, IDE

```
codex plugin marketplace add ajitta/dialectic-skills
codex plugin add dia@dialectic-skills
```

- Codex 앱(데스크톱): GitHub 저장소(`ajitta/dialectic-skills`), Git URL(`https://github.com/ajitta/dialectic-skills.git`), 로컬 폴더(이 저장소를 클론한 폴더) 중 하나로 플러그인 마켓플레이스를 추가한 뒤 `dia`를 설치합니다. 위의 CLI 명령도 같은 일을 합니다.
- 업데이트: `codex plugin marketplace upgrade`로 마켓플레이스를 갱신하고, `codex plugin list`로 설치된 버전을 확인합니다.
- 플러그인 없이 쓰려면: `skills/dia-<x>/` 폴더를 `~/.agents/skills/`에 복사합니다. 이렇게 복사한 스킬의 이름은 `$dia:dia-<x>`가 아니라 `$dia-<x>`입니다.

### ChatGPT 데스크톱과 모바일

저장소 소유자는 Pro 요금제에서 ChatGPT 데스크톱과 모바일로 스킬을 실행해 보았습니다. 정확한 설치 경로는 요금제와 워크스페이스에 따라 다릅니다.

- ChatGPT 데스크톱 앱의 Codex나 Codex 앱을 통해 설치합니다(위의 Codex 마켓플레이스 경로). 또는
- Business 및 Enterprise 워크스페이스에서는 워크스페이스의 플러그인 관리 기능을 통해 설치합니다(zip 업로드 또는 GitHub 마켓플레이스 가져오기).

그러면 요금제가 플러그인을 허용하는 범위에서, 플러그인에 포함된 스킬을 데스크톱, 웹, 모바일의 ChatGPT에서 사용할 수 있습니다.

### Windows

위의 모든 경로는 Windows에서도 작동합니다. 스킬에는 스크립트가 없으므로 Python이나 셸 설정이 필요하지 않습니다.

### 이전 버전에서 옮기기

- **1.0.0에서 옮기는 경우:** `dia-intent`의 이름이 `dia-confirm`으로 바뀌었습니다(1.1.0). 새 이름으로 호출합니다. 마켓플레이스로 설치했다면 업데이트 시 변경 사항이 반영되고, zip으로 업로드했다면 기존 것을 제거하고 새 zip을 업로드해야 합니다.
- **저장소 소유자가 이전에 배포한 개별 스킬에서 옮기는 경우:** 먼저 기존 사본을 제거합니다. 그렇지 않으면 각 방법이 두 이름으로 두 번 로드됩니다. claude.ai: Customize › Skills에서 `reductio`, `negative-dialectics`, `self-refine`, `recursive-refine`, `confirm-intent`를 제거하고, Customize › Plugins에서 `socratic`을 제거합니다. Claude Code: `/plugin uninstall socratic@ajitta-socratic`을 실행하고 `~/.claude/skills/` 아래의 사본을 제거합니다. Codex와 ChatGPT 데스크톱: `~/.agents/skills/` 아래의 기존 사본을 제거합니다.

## 호출 방법

방법은 세 가지이며, 모든 환경에서 적어도 한 가지는 지원합니다.

1. **말로 요청하기.** 방법을 직접 요청합니다: "…에 귀류법을 적용해 주세요", "…을 내재적 비판해 주세요", "소크라테스식 대화로 부탁합니다…". 모든 환경에서 작동하며, 모바일에서는 이 방법이 가장 안전한 기본값입니다. `dia-reductio`, `dia-negative`, `dia-elenchus`, `dia-brainstorm`에 쓸 수 있습니다.
2. **메시지에 이름 적기.** 메시지를 스킬 이름으로 시작합니다: `dia-confirm …`, `dia-refine …`, `dia-iterate …`. `dia-refine`과 `dia-iterate`는 이 방식이나 명시적 선택으로 시작하도록 설계되었습니다. `dia-iterate`는 일반 요청으로는 절대 시작되지 않으며, Claude Code에서는 "이 초안 고쳐 주세요" 같은 일반 요청으로 `dia-refine`이 로드되는 경우가 드뭅니다.
3. **명시적 선택.** 환경마다 표기법이 다릅니다.

| 환경 | 문법 | 예시 |
|---|---|---|
| claude.ai, Claude 데스크톱, Claude Code | `/dia:dia-<x>` | `/dia:dia-reductio` |
| Codex (플러그인) | `$dia:dia-<x>` 뒤에 공백 | `$dia:dia-confirm 백업 스크립트 작성해줘` |
| Codex (복사한 폴더) | `$dia-<x>` | `$dia-refine` |
| ChatGPT | `@` 입력 후 스킬 선택 | `@dia-negative` |

Codex에서 `dia-confirm`, `dia-elenchus`, `dia-brainstorm`, `dia-iterate`는 저절로 시작되지 않으므로 `$dia:dia-<x>`로 선택해야 합니다. `dia-reductio`, `dia-negative`, `dia-refine`은 요청 내용이 맞으면 저절로 시작될 수도 있습니다.

### 옵션

옵션은 플래그로 쓰거나 일반 문장으로 쓸 수 있으며, 언어는 상관없습니다.

- `--target=user|claude|text|all` (`dia-reductio`, `dia-negative`): 검토 대상을 정합니다. `user`는 사용자가 제시한 주장, `claude`는 어시스턴트 자신의 이전 답변(어떤 어시스턴트든 해당), `text`는 붙여 넣은 텍스트, `all`은 이 중 존재하는 모든 것입니다. 플래그가 없으면 스킬이 대상을 추론하고 첫 줄에 밝힙니다.
- `--max N` (`dia-iterate`): 라운드 상한이며, 기본값은 3입니다.
- 모드와 깊이 (`dia-brainstorm`): `develop`(기본값) 또는 `stress`("허점을 찔러 주세요"), 그리고 `quick`, `standard`(기본값), `deep`.
- 기준 (`dia-refine`, `dia-iterate`): 이름 뒤에 오는 모든 내용이 기준이 됩니다. 예: `dia-refine — 숫자 확인해줘` 또는 `dia-refine 어조 위주로`.

## 예시

아래 프롬프트는 한국어로 작성했지만, 같은 요청은 어떤 언어로든 작동하며 답변은 사용자가 쓴 언어를 따릅니다. 출력 설명은 줄여서 적었습니다.

### dia-confirm: 작업 시작 전에 과제 합의하기

```
dia-confirm 내 사진 파일 이름을 모두 날짜 기준으로 바꾸는 스크립트를 작성해 주세요.
```

짧은 섹션 네 개를 받게 되며, 아직 작업은 진행되지 않습니다.

- **목표와 성공 조건:** 무엇을 만들지, 그리고 완료되었는지 어떻게 판단할 수 있는지.
- **근거와 가정:** 어시스턴트가 확인한 것과 가정한 것(예: 날짜를 사진 메타데이터에서 가져온다는 가정).
- **사용자가 내려야 할 결정:** 사용자가 꼭 정해야 하는 것만(운영 체제, 하위 폴더 포함 여부, 어떤 날짜를 쓸지).
- **확인:** 진행하려면 어떻게 답하면 되는지.

답변과 함께 "진행"이라고 답합니다. 수정 사항과 "진행"을 함께 보내면 수정된 과제를 승인한 것으로 처리되고, 수정 사항만 보내면 수정된 검토를 다시 받습니다. 이 스킬은 해당 과제와 그 직접적인 후속 작업에만 적용됩니다.

### dia-elenchus: 단어의 뜻을 검증하기

```
소크라테스식 대화를 부탁합니다. 먼저 제가 정의부터 하게 해 주세요. 점심 메뉴 추천 앱을 만들고 싶습니다.
```

어시스턴트는 메시지마다 짧은 질문을 하나씩 던집니다. 예를 들어 "좋은 추천"이란 무엇인지 묻습니다. 사용자가 동의한 내용만을 근거로 논증하며, 사용자의 두 진술이 동시에 성립할 수 없으면 둘을 나란히 보여 주고 어느 쪽을 바꾸겠는지 묻습니다. 대화 중에는 조언하지 않습니다. 사용자가 멈추거나, 더 내놓을 정의가 없거나(아포리아), 어떤 정의가 여러 차례 검증을 견디면 대화가 끝나고, 결과와 함께 기록을 출력합니다. 결과는 아포리아, 유지(잠정), 부분 검증, 검증 전 중단 중 하나입니다.

### dia-brainstorm: 질문으로 아이디어를 키운 뒤 결정하기

```
저와 소크라테스식 브레인스토밍을 해 주세요. 주말 사이드 프로젝트 아이디어가 필요합니다. 짧게 진행해 주세요.
```

아이디어를 파고드는 동안 메시지마다 질문을 하나씩 합니다(`quick`은 약 4개, `standard`는 8–10개). 그다음 사용자의 선택지와 표시를 붙인 최대 세 개의 제안, 사용자가 정한 기준에 따른 비교, 결론, 그리고 선택적으로 요약서를 제시합니다. 코드를 작성하거나 실제 작업을 하지는 않습니다. 언제든 "그만" 또는 "마무리"라고 하면 바로 결론으로 넘어갑니다.

### dia-reductio: 모순 찾기

```
이 주장에 귀류법을 적용해 주세요: 재택근무는 언제나 생산성을 높인다.
```

한 번의 응답에 전체 논증이 담깁니다. 논제, 출처별로 표시를 붙인 모든 전제([T]는 대상이 진술한 것, [L]은 논리학이나 수학의 법칙, [A]는 어시스턴트가 추가한 것으로 명시되지 않은 가정, 정의, 사실 등), 각 줄마다 적용 규칙을 밝힌 번호 매긴 도출, 강도를 함께 표시한 모순 Q와 not-Q, 포기할 수 있는 전제들, 하나의 권고, 그리고 기록입니다. 어시스턴트가 대신 결정하지는 않습니다. 어시스턴트 자신의 직전 답변을 검증하려면 `--target=claude`를 쓰거나 "직전 답변을 귀류법으로 검토해 주세요"라고 요청합니다.

### dia-negative: 주장을 그 자신의 기준으로 평가하기

```
이 주장에 대해 내재적 비판을 해 주세요: 우리 회사는 수평적이라서 누구나 자유롭게 의견을 말할 수 있다.
```

주장 자신의 기준을 인용하고, 주장하는 바와 실제로 이루어지는 바가 어긋나는 지점을 각각 구체적 사례와 함께 제시하며, 주장이 놓치는 것, 그리고 주장이 실제로 하는 일을 검증 가능한 추론으로 밝히고 그것을 반증할 관찰을 덧붙입니다. 이어서 선택지, 하나의 권고, 기록을 제시합니다. 새로운 상위 정의를 억지로 만들어 내지는 않습니다. 코드, 명령어, 설정이 무엇을 하는지 알고 싶거나 일반적인 검토가 필요하다면 평소처럼 요청하십시오.

### dia-refine: 한 차례 검토

```
dia-refine 사실관계를 확인해 주세요: 에베레스트산은 두 번째로 높은 산이라서 등반객이 가장 많다.
```

네 부분으로 된 결함 목록(① 확인된 오류, ② 누락된 요구 사항, ③ 유지한 올바른 내용, ④ 남은 불확실성)과 하나의 수정본을 제시합니다. 확인된 근거가 있는 결함만 고칩니다. 근거는 실제로 실행한 도구, 사용자의 지시나 자료, 또는 어시스턴트 자신의 재도출입니다. 의심은 되지만 확인하지 못한 오류는 조용히 고치지 않고, 의심되는 수정안과 함께 ④에 적습니다. 초안이 없을 때 "이 작업을 dia-refine 방식으로 해 주세요"라고 하면, 답변을 작성하고 한 번 검토한 뒤 최종본만 보여 줍니다.

### dia-iterate: 각각 검증하는 여러 라운드

```
dia-iterate --max 2 직전 답변의 날짜와 수치를 확인해 주세요
```

각 라운드에서는 결함을 지목하고, 각 결함을 외부 확인(검색, 도구 실행, 사용자가 제공한 자료)으로 판정한 뒤, 확인된 것만 고치고 통과한 부분은 고정합니다. 퇴행이 생기거나, 남은 결함이 없거나, 검증 수단이 바닥나거나, 고정점에 이르거나, 라운드 상한에 도달하면 반복을 멈추고 변경 사항, 라운드 요약, 검증하지 못한 항목을 보고합니다. 도구가 없는 채팅에서는 1라운드 후에 멈추고, 검증하지 못한 항목 목록을 제시합니다. 문장 중간에 `dia-iterate`를 언급하는 것만으로는 반복이 시작되지 않으며, 어시스턴트가 이름으로 시작하는 메시지를 다시 보내 달라고 요청합니다.

## 여러 스킬 함께 쓰기

- **한 요청에 `dia-elenchus`와 `dia-brainstorm`을 함께 쓰는 경우:** 정의를 다루는 대화가 먼저 진행되며, 첫 메시지에서 이를 알립니다. 사용자가 선택지를 요청하거나 대화가 끝나면 브레인스토밍이 시작됩니다. 두 과정이 뒤섞이는 일은 없습니다.
- **한 요청에 `dia-refine`과 `dia-iterate`를 함께 쓰는 경우:** 별개의 두 과정으로 실행되며 출력도 따로 나옵니다. refine 과정에서 어시스턴트가 직접 한 재도출은 iterate 라운드의 검증으로 인정되지 않습니다.
- **한 요청에 `dia-reductio`와 `dia-negative`를 함께 쓰는 경우:** 둘 다 실행되고 두 답변 모두 완전하게 제시되므로 출력이 길어집니다(테스트에서 약 9,000자). 휴대폰에서는 하나씩 요청하십시오.
- **`dia-elenchus` 이후:** 그다음에 조언을 요청하면, 어시스턴트는 소크라테스식 부분이 끝났다고 밝히고 각 제안이 자신의 것임을 표시합니다. 선택지와 계획까지 다루는 온전한 세션을 원하면 `dia-brainstorm`을 지정하십시오. 그러면 그 기록을 이어받아 진행합니다.

## 문제 해결

- **마켓플레이스를 추가할 때 `Repository not found`가 나타납니다.** 철자를 확인합니다: `ajitta/dialectic-skills`(dialectric이 아니라 dialectic). 저장소는 공개되어 있으며 GitHub 로그인이 필요하지 않습니다.
- **Claude 모바일의 `/`에 dia 스킬이 없습니다.** 정상입니다. 모바일 메뉴에는 플러그인 스킬이 표시되지 않습니다. 말로 요청하거나 메시지를 스킬 이름으로 시작합니다.
- **모든 스킬이 두 번씩 나타납니다.** 플러그인이 두 경로로 설치된 것입니다(예: `dia@dialectic-skills`와 `dia@ajitta`, 또는 업로드와 마켓플레이스). 하나를 제거합니다.
- **claude.ai에 Skills 섹션이 없거나 비활성화되어 있습니다.** Settings › Capabilities › Code execution and file creation을 켭니다.
- **`dia-intent`를 찾을 수 없습니다.** 1.1.0에서 `dia-confirm`으로 이름이 바뀌었습니다.
- **`dia-iterate`가 시작되지 않습니다.** 메시지의 첫 단어가 `dia-iterate`이거나 명시적으로 선택했을 때(`/dia:dia-iterate`, `$dia:dia-iterate`, `@dia-iterate`)에만 시작됩니다.
- **Codex에서 `$dia:dia-confirm:`이 인식되지 않습니다.** 스킬 이름 뒤에 콜론이 아니라 공백을 넣습니다.
- **claude.ai에서 업로드가 거부됩니다.** Customize › Skills가 아니라 Customize › Plugins › Upload plugin을 사용합니다.

어떤 경로를 어떻게 검증했는지는 [docs/probes.md](docs/probes.md)에 기록되어 있습니다.

## 저장소 구조

```
skills/dia-<x>/                 source: plain skills (SKILL.md, references/, agents/openai.yaml)
plugin-manifest.json            source for .claude-plugin/plugin.json
plugin-release.json             content digest for the current version (not shipped)
.claude-plugin/marketplace.json marketplace "dialectic-skills" -> ./plugins/dia
plugins/dia/                    generated, shipped
releases/dialectic-skills.zip   generated, shipped (top-level folder dia/)
tools/package.py                validate and build (developer-only)
tests/                          developer-only
upstream/                       material the skills were rebuilt from; never shipped
README.<lang>.md                translations of this file (not shipped)
docs/spec.md                    specification
docs/probes.md                  surface and routing probe results
docs/token-cost.md              measured token cost per skill
docs/skill-effect.md            each skill against no skill, blind-judged
```

## 개발

```bash
python tools/package.py            # validate, write plugins/dia/ and the zip
python tools/package.py --check    # validate; fail if the committed output lags the source
python -m unittest discover -s tests -v
claude plugin validate --strict plugins/dia
```

생성된 출력물이 아니라 `skills/`를 수정합니다. 스킬 파일을 변경할 때마다 `plugin-manifest.json`의 `version`(및 해당 스킬의 `metadata.version`)을 새로 올려야 합니다. Claude Code는 버전이 바뀔 때만 설치된 플러그인을 업데이트하며, 그렇지 않으면 검사가 실패합니다. 배포 패키지에서 한글은 `skills/<skill>/references/ko/` 아래에서만 허용됩니다. 이 README를 변경하면 같은 커밋에서 번역본도 갱신해야 하며, 테스트가 번역본이 같은 구조를 유지하는지 확인합니다.

## 라이선스

MIT
