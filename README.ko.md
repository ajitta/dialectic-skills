# Dialectic Skills (`dia`)

[English](README.md) | **한국어**

웹사이트: [ajitta.github.io/dialectic-skills](https://ajitta.github.io/dialectic-skills/)

추론과 검토를 위한 스킬 열세 개와, 그 스킬들을 부르는 스킬 `dia` 하나를 담은 플러그인입니다. 스킬 하나하나는 함수입니다. 목적이 하나이고, 건네받은 것으로 일하며, 한 가지를 돌려줍니다. 서로를 알지 못합니다. 패키지는 지시문뿐입니다(Markdown, YAML, JSON). 스킬은 메시지가 그 이름으로 시작할 때만 시작합니다.

| 스킬 | 목적 | 건넬 것 | 돌려주는 것 | 답할 사람 |
|---|---|---|---|---|
| `dia-skopos` | 일을 시작하기 전에, 무엇을 요청받았는지와 그것이 어떤 결과를 위한 것인지를 보여 주고, 둘 중 무엇을 요청으로 삼을지 고르게 한다 | 요청(사용자의 말 그대로), 요청이 가리키는 프로젝트나 자료 | 검토: 만들 것, 그것이 위하는 결과, 찾은 것과 가정한 것, 사용자만 정할 수 있는 것, 선택. 일은 하지 않는다 | 필요: 사용자의 말을 기다린다 |
| `dia-techne` | 과제를 그것이 위하는 결과를 위해, 그 분야 최고의 실무자가 하듯 하고, 모델 밖에서 확인한다 | 요청, 그것이 무엇을 위한 것인지에 대한 사용자의 말, 사용자가 준 사실과 한계, 파일과 데이터. `--aim=request`는 요청한 것 자체에 머문다 | 끝낸 일, 그리고 겨냥한 결과, 비교한 방법, 만들거나 바꾼 것, 실제로 쓴 방법, 확인이 보여 준 것 | 불필요 |
| `dia-emend` | 초안을 한 번 검토해, 확인된 것은 고치고 의심만 되는 것은 표시한 수정본 하나를 돌려준다 | 초안 자체(글이나 파일), 기준, 초안의 목적, 대조할 자료 | 찾은 결함과 수정본 하나. 파일은 그 자리에서 고친다 | 불필요 |
| `dia-ratchet` | 모델 밖의 증거로만 움직이는 라운드로 고쳐서, 어떤 주장이 확인됐는지 사용자가 알게 한다 | 대상(글이나 파일), 기준, 목적, 사용자의 자료. `--max N`은 라운드 상한 | 바꾼 것, 라운드마다 잠근 것, 멈춘 이유, 확인하지 못한 것. 대상에 대한 판정은 없다 | 불필요 |
| `dia-regula` | 모델이 따르는 글(프롬프트, 지시문, 스킬)을 네 규칙에 비추어 쓰거나 검토한다 | 글 자체, 고쳤다면 이전 글, 그 글이 모델에게 시켜야 할 일에 대한 사용자의 말 | 위반마다 인용과 어긴 규칙을 적은 보고, 또는 쓰거나 고친 글과 뜻이 바뀐 곳의 보고 | 불필요 |
| `dia-negative` | 주장, 계획, 글을 그것이 스스로 내세운 기준에 비춘다 | 대상의 말 그대로(설명이 아닌 원문), 대상이나 사용자가 밝힌 목적 | 판정 먼저(열림, 또는 시험한 사례에서는 버팀), 확정·조건부 발견, 주장이 내세운 목적에 비추어 실제로 하는 일, 선택지와 권고 하나 | 불필요 |
| `dia-reductio` | 입장을 그 자신의 약속에 비춘다: 무엇에 기대야 하는지, 그 모두가 함께 참일 수 있는지 | 입장의 말 그대로, 그 주인이 같은 문제에 대해 전에 말하거나 약속한 것, 가리키는 파일, 입장의 목적 | 판정 먼저, 모순과 그에 필요한 전제, 드러난 것, 빠져나갈 길마다의 대가 | 불필요: 물었을 것을 열거한다 |
| `dia-warrant` | 결론을 그것을 떠받치는 단계에 비춘다: 단계마다 기대는 규칙과, 이 경우에 그 규칙이 서는지 | 논증의 말 그대로(결론과 이유), 가리키는 자료, 결론이 떠받쳐야 할 것 | 판정 먼저(결론을 어디까지 믿을 수 있는지), 갈리는 단계, 증거, 손에 있었는데 쓰지 않은 것 | 불필요: 물었을 것을 열거한다 |
| `dia-conjecture` | 모든 경우에 대한 주장을 가장 세게 누르는 사례에 비추고, 사례가 통하면 주장을 고친다 | 주장(출처의 말 그대로), 그것이 다루는 기록이나 코드, 그 위에 선 것 | 판정 먼저("모든"이 서는지), 가르는 사례, 고친 주장과 그것이 더는 다루지 않는 것 | 불필요: 물었을 것을 열거한다 |
| `dia-counterplan` | 계획을, 반대 가정에서 나오는 계획에 같은 사실 위에서 비춘다 | 계획의 글, 수치와 파일, 계획의 목적, 가정을 가르는 사용자의 말 | 판정 먼저(어느 길을 갈지, 무엇이 그것을 바꿀지), 가정마다의 반대 가정, 대안 계획 | 불필요: 물었을 것을 열거한다 |
| `dia-adjudicate` | 대상에 대한 보고들을 증거로 판정하고, 대상 자체의 주장을 확인하고, 결론에서 무엇이 남는지 판단한다 | 대상, 보고 전문, 둘이 가리키는 출처, 판정의 목적에 대한 사용자의 말 | 판정 먼저, 쟁점마다의 판정과 근거, 어느 보고도 제기하지 않은 것, 대상에서 바뀌어야 할 것 | 불필요: 물었을 것을 열거한다 |
| `dia-elenchus` | 생각이 딛고 선 개념을 정의, 합의한 전제, 모순, 수정으로 살펴, 답하는 이 자신의 생각 속 갈림을 드러낸다 | 생각(답하는 이의 말 그대로). 대화를 잇는다면 지금까지의 대화나 기록과 새 답 | 메시지마다 질문 하나. 끝에는 정의들, 합의한 전제, 새로 난 생각, 아직 모르는 것의 기록 | 필요(사람이든 에이전트든). 없으면 첫 질문만 준다 |
| `dia-quaestio` | 생각의 주인이 그것을 또렷이 볼 때까지 묻고, 선택지를 키워 고르도록 돕는다 | 생각(주인의 말 그대로)과 그 목적. `stress`는 더 세게 시험하고, `quick`과 `deep`은 길이를 정한다 | 메시지마다 질문 하나. 끝에는 평결과, 선택지와 다음 한 걸음을 담은 브리프 | 필요 |

## 목차

- [설치](#설치)
- [스킬 시작하기](#스킬-시작하기)
- [`dia`: 대상을 비판하고 판정하기](#dia-대상을-비판하고-판정하기)
- [스킬을 에이전트에게 맡기기](#스킬을-에이전트에게-맡기기)
- [문제 해결](#문제-해결)
- [저장소 구성](#저장소-구성)
- [개발](#개발)

## 설치

어디에 설치하느냐가 dia가 보이는 곳을 정합니다. 웹(claude.ai, chatgpt.com)에서 한 설치는 계정에 저장되어 웹과 모바일 앱에 나타납니다. 데스크톱 앱에서 한 설치는 그 컴퓨터에만 남습니다.

### Claude Code

```
/plugin marketplace add ajitta/dialectic-skills
/plugin install dia@dialectic-skills
```

- 업데이트: `/plugin marketplace update dialectic-skills` 뒤에 플러그인을 업데이트합니다(또는 마켓플레이스의 자동 업데이트를 켭니다).
- 제거: `/plugin uninstall dia@dialectic-skills`.
- claude.ai에서 추가한 플러그인은 같은 계정으로 로그인하면 Claude Code에도 동기화됩니다. 명령줄에서 한 번 더 설치하지 마세요.

### claude.ai 웹, Claude 데스크톱, 모바일

1. Settings › Capabilities에서 **Code execution and file creation**을 켭니다. 스킬에 필요합니다.
2. Customize › Plugins › Add › Add marketplace에 `ajitta/dialectic-skills`를 넣습니다.
3. Customize › Plugins에서 Discover를 열고 `dia`(Dialectic Skills)를 골라 Add를 누릅니다.
4. 메시지 칸에 `/dia`를 칩니다. 항목 열네 개(스킬 열세 개와 `dia:dia`)가 보여야 합니다.

2와 3 대신, 최신 릴리스의 [`dialectic-skills.zip`](https://github.com/ajitta/dialectic-skills/releases/latest/download/dialectic-skills.zip)을 Customize › Plugins › Add › Upload plugin으로 올릴 수 있습니다. 올린 것은 스스로 업데이트되지 않습니다.

Claude 데스크톱은 그 컴퓨터에만 설치합니다. 모바일 앱에는 설치 단계가 없습니다. claude.ai에서 추가한 플러그인이 계정을 통해 닿습니다. 모바일의 `/` 메뉴는 플러그인 스킬을 보여 주지 않으니, 메시지를 스킬 이름으로 시작하세요.

### Codex와 ChatGPT

```
codex plugin marketplace add ajitta/dialectic-skills
codex plugin add dia@dialectic-skills
```

웹과 모바일의 ChatGPT에는 최신 릴리스의 [`dialectic-skills-openai.zip`](https://github.com/ajitta/dialectic-skills/releases/latest/download/dialectic-skills-openai.zip)을 chatgpt.com에서 올립니다. ChatGPT 데스크톱 앱에서는 마켓플레이스 `ajitta/dialectic-skills`를 추가하고 플러그인 목록에서 `dia`를 설치합니다. 이 설치는 그 컴퓨터에만 남습니다.

## 스킬 시작하기

메시지를 스킬 이름으로 시작합니다: `dia-reductio 재택근무는 언제나 생산성을 높인다.` 스킬의 방법을 말로만 청하는 메시지("귀류법으로 따져 줘")는 어떤 스킬도 시작하지 않습니다.

각 서비스가 스킬을 고르는 방식으로도 고를 수 있습니다.

| 서비스 | 문법 | 예 |
|---|---|---|
| claude.ai, Claude 데스크톱, Claude Code | `/dia:dia-<x>` | `/dia:dia-reductio` |
| Codex | `$dia:dia-<x>` 뒤에 공백 | `$dia:dia-skopos 백업 스크립트를 써 줘` |
| ChatGPT | `@`를 치고 스킬을 고른다 | `@dia-negative` |

이름 뒤에 오는 것이 스킬이 일하는 재료입니다. 주장, 계획, 초안, 파일 경로, 그것이 무엇을 위한 것인지에 대한 여러분의 말입니다. 스킬마다 필요한 것은 맨 위의 표에 있습니다. 몇몇 스킬은 요청에서 옵션을 읽습니다.

- `--aim=request` (`dia-techne`): 요청 뒤의 결과를 위해 일하지 않고 요청한 것 자체에 머뭅니다.
- `--max N` (`dia-ratchet`): 라운드 상한. 주지 않으면 3입니다.
- `stress`, `quick`, `deep` (`dia-quaestio`): 생각을 더 세게 시험하거나, 대화의 길이를 정합니다.

`dia-skopos`, `dia-elenchus`, `dia-quaestio`는 대화를 합니다. 묻고 답을 기다립니다. 나머지는 결과 전체를 한 번의 답으로 주고, 여러분만 답할 수 있는 것은 질문으로 열거하면서 각 답이 무엇을 가르는지 적습니다.

## `dia`: 대상을 비판하고 판정하기

`dia`는 다른 스킬들을 부르는 스킬입니다.

- **`dia`만 쓰면** 위의 표와, 에이전트에게 일을 맡기는 규칙을 불러옵니다. 대화가 끝날 때까지 유지됩니다.
- **`dia` 뒤에 스킬 이름을 쓰거나, 표의 한 행이 말하는 일을 요청하면** 그 스킬을 돌리고 어느 스킬인지와 이유를 한 줄로 말합니다.
- **`dia` 뒤에 대상만 쓰고 스킬을 청하지 않으면**(`dia docs/plan.md`, 또는 `dia`와 붙여 넣은 주장) 독립된 에이전트 셋이 대상을 비판하고 넷째가 판정합니다. 세션이 대상, 대상이 가리키는 출처, 여러분이 그에 대해 한 말을 모두 모으고, 이 대상에 있을 수 있는 결함의 종류에 따라 비평가 셋을 고르고(맞는 dia 스킬이 있으면 그것, 없으면 그때 맞게 지시한 에이전트), 서로 떨어뜨려 시작한 뒤, 대상과 출처와 여러분의 말과 보고 셋의 전문을 별도 에이전트의 `dia-adjudicate`에게 건넵니다. 여러분은 판정자의 답을 판정자가 쓴 그대로 받습니다.
- **비평가를 직접 지정할 수 있습니다:** `dia docs/plan.md 비평가는 dia-counterplan, dia-warrant, 보안 검토자`.

에이전트를 시작할 수 없는 곳에서는 `dia`가 그렇게 말합니다. 한 대화 안에서 만든 비판들은 서로 독립이 아닙니다.

## 스킬을 에이전트에게 맡기기

에이전트는 여러분의 대화를 전혀 보지 못합니다. 건네받지 못한 것은 추측으로 채우고, 그 추측은 발견처럼 보이며 돌아옵니다. `dia`가 이 규칙들을 갖고 있고, 손으로 맡길 때도 따를 만합니다.

- 에이전트에게 출처 자체를 건넵니다(대상의 경로나 전문, 대상이 기대는 파일). 요약은 건네지 않습니다.
- 대화에만 있는 것은 말 그대로, 누구의 말인지 표시해서 넣습니다. 대상의 목적, 여러분이 말한 사실, 여러분이 정한 한계가 그렇습니다. 여러분의 말에 세션 자신이 하고 있는 일(비평가 여럿, 판정)을 청하는 부분이 있으면, 그중 에이전트가 맡은 자리가 어디인지를 지시문에 밝힙니다.
- 대상에 대한 세션 자신의 견해는 주지 않습니다.
- 지시문의 첫 줄에 스킬 이름만 쓰고, 스킬의 답 전체를 마지막 메시지로 달라고 합니다.
- 질문에 답할 사람이 없다고 알려서, 물었을 것이 열린 항목으로 돌아오게 합니다. 대화를 하는 스킬은 예외입니다. 그 에이전트를 이어 가거나 지금까지의 대화를 주어 다시 시작하면서, 답을 하나씩 건넵니다.
- 보고는 전문 그대로 넘깁니다.

## 문제 해결

- **스킬이 시작되지 않았다.** 말로만 한 요청은 dia 스킬을 시작하지 않습니다. 메시지를 스킬의 전체 이름으로 시작하세요.
- **`dia` 뒤에 글을 썼더니 예상과 다른 일이 일어났다.** `dia` 뒤에 대상만 있고 스킬을 청하지 않으면 그 대상을 에이전트 셋이 비판하고 넷째가 판정합니다. 스킬 하나만 돌리려면 그 스킬의 이름으로 메시지를 시작하세요.
- **마켓플레이스를 추가할 때 `Repository not found`가 나온다.** 철자를 확인하세요: `ajitta/dialectic-skills`.
- **스킬이 모두 두 번씩 보인다.** 플러그인이 두 경로로 설치돼 있습니다(예: 업로드와 마켓플레이스). 하나를 지우세요.
- **한 기기에서는 되는데 다른 기기에서는 안 된다.** 데스크톱 설치는 그 컴퓨터에만 남고, 웹 설치는 계정에 저장되어 모바일 앱에 닿습니다.
- **claude.ai에서 Skills 항목이 없거나 회색이다.** Settings › Capabilities › Code execution and file creation을 켜세요.

## 저장소 구성

```
skills/<skill>/                 source: plain skills (SKILL.md, references/, agents/openai.yaml)
plugin-manifest.json            source for .claude-plugin/plugin.json
packaging/plugin-README.md      source for plugins/dia/README.md
packaging/openai/               OpenAI directory listing fields and images
plugin-release.json             content digest for the current version (not shipped)
.claude-plugin/marketplace.json marketplace "dialectic-skills" -> ./plugins/dia
plugins/dia/                    generated, shipped
releases/dialectic-skills.zip   generated, shipped (top-level folder dia/)
releases/dialectic-skills-openai.zip
                                generated, OpenAI directory upload
tools/package.py                validate and build (developer-only)
tests/                          developer-only
upstream/                       material the seven original skills were rebuilt from; never shipped
docs/spec.md                    the package rules
docs/handoff.md                 the current state and what is open
```

## 개발

```bash
python tools/package.py            # validate, write plugins/dia/ and the zips
python tools/package.py --check    # validate; fail if the committed output lags the source
python -m unittest discover -s tests -v
claude plugin validate --strict plugins/dia
```

`skills/`를 고치고, 생성된 결과물은 손대지 않습니다. 배포되는 파일이 바뀌면 `plugin-manifest.json`의 `version`을 새로 올리고, 스킬이 바뀌면 그 스킬의 `metadata.version`도 올립니다. 이 README가 바뀌면 같은 커밋에서 `README.md`와 구조를 맞춥니다. 테스트가 같은 구조인지 확인합니다.

## 라이선스

MIT
