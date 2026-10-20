# Dialectic Skills (`dia`)

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | **简体中文**

一个插件内含七个推理与审查技能，无需修改即可在任何加载 Agent Skills 的助手上运行：Claude（网页版、桌面版、移动版、Claude Code）、Codex 和 ChatGPT。整个包只包含指令（Markdown、YAML、JSON），因此每个技能在没有任何工具的聊天中也能使用。技能文件用英文编写；每个技能都会用你消息所用的语言回复。

| 技能 | 作用 | 启动方式 |
|---|---|---|
| `dia-confirm` | 工作开始前：复述目标，说明重要假设，只列出必须由你做的决定，然后等待你的批准。 | 仅通过名称 |
| `dia-elenchus` | 柏拉图的诘问法（elenchus）：追问"X 是什么？"，一次一个问题地确认前提，揭示矛盾，每次修正都成为你的新想法。通常以困惑（aporia）告终；不提供建议。 | 通过名称，或请求苏格拉底式对话 |
| `dia-brainstorm` | 现代苏格拉底式提问，一次一个问题；然后给出你的选项外加最多三个带标注的选项，按标准收敛，给出结论和简报。从不动手实现。 | 通过名称，或请求苏格拉底式头脑风暴 |
| `dia-reductio` | 一次完成的严格归谬法（reductio ad absurdum，反证法）：带标注的前提，推出 Q 与非 Q 且每行注明规则的推导，分级的强度，可选方案和记录。 | 通过名称，或用文字描述 |
| `dia-negative` | 一次完成的内部批判（比阿多诺的内在批判范围更窄）：对象自身的标准，附具体案例和"遗漏之物"的严格落差，附可证伪条件的实际目的，不强求综合的可选方案。 | 通过名称，或用文字描述 |
| `dia-refine` | 对上一个回答或草稿做一轮审查：事实错误、逻辑跳跃、遗漏的需求、重复。只修正已确认的缺陷。 | 首词为 `dia-refine`，或通过名称 |
| `dia-iterate` | 多轮重复审查，每轮都以外部验证把关；在出现退化、零缺陷、验证手段用尽、达到不动点或 `--max N`（默认 3）时停止。 | 首词为 `dia-iterate`，或仅通过名称 |

## 目录

- [快速开始](#快速开始)
- [安装](#安装)
- [调用方式](#调用方式)
- [示例](#示例)
- [组合使用多个技能](#组合使用多个技能)
- [故障排除](#故障排除)
- [仓库结构](#仓库结构)
- [开发](#开发)
- [许可证](#许可证)

## 快速开始

Claude Code：

```
/plugin marketplace add ajitta/dialectic-skills
/plugin install dia@dialectic-skills
```

Codex CLI：

```
codex plugin marketplace add ajitta/dialectic-skills
codex plugin add dia@dialectic-skills
```

claude.ai 或 Claude 桌面版：Customize › Plugins › Add › Add marketplace，输入 `ajitta/dialectic-skills`，然后选择 Discover › `dia` › Add。详细步骤见下文。

然后试试：`对这个论断用反证法：远程办公总能提高生产力。`

## 安装

### claude.ai 网页版与 Claude 桌面版

1. Settings › Capabilities：打开 **Code execution and file creation**。技能依赖此项，尽管没有任何 dia 技能会运行代码。
2. **添加 marketplace。** 打开 Customize › Plugins › Add › Add marketplace，输入：

   ```
   ajitta/dialectic-skills
   ```

   也可以输入 Git URL `https://github.com/ajitta/dialectic-skills.git`，Claude 桌面版还可以指定本地文件夹（本仓库的克隆）。请复制粘贴而不要手动输入：像 `dialectric` 这样的拼写错误会以 "Repository not found" 失败。
3. **添加插件。** 只添加 marketplace 还不会安装任何东西。在 Customize › Plugins 中打开 Discover，选择 `dia`（Dialectic Skills），然后选择 Add。
4. **检查。** 在消息框中输入 `/dia`，应出现从 `dia:dia-brainstorm` 到 `dia:dia-refine` 共七项。更新通过 marketplace 获取（Check for updates，或 Sync automatically）。

也可以不走第 2、3 步，直接上传插件：在 Customize › Plugins › Add › Upload plugin 上传最新发布版中的 [`dialectic-skills.zip`](https://github.com/ajitta/dialectic-skills/releases/latest/download/dialectic-skills.zip)。请使用 Customize › Plugins，而不是 Customize › Skills：Skills 页面会拒绝带有插件清单的 zip。上传的插件不会自动更新；每个新版本都需重新上传。

### Claude 移动版（iOS、Android）

无需安装步骤。在 claude.ai 或 Claude 桌面版添加的插件属于你的账号，会自动同步到移动应用。移动版的 `/` 菜单不会列出插件技能；请用文字描述请求，或在消息中写出技能名称。

### Claude Code

```
/plugin marketplace add ajitta/dialectic-skills
/plugin install dia@dialectic-skills
```

- 更新：`/plugin marketplace update dialectic-skills`，然后更新插件（或为该 marketplace 开启自动更新）。
- 卸载：`/plugin uninstall dia@dialectic-skills`。
- 在 claude.ai 添加的插件，用同一账号登录 Claude Code 时也会同步过来。不要再从命令行重复安装。
- 也可以通过目录安装：`/plugin marketplace add ajitta/claude-plugins`，然后 `/plugin install dia@ajitta`。代码相同，安装名称不同。

### Codex CLI 与 IDE

```
codex plugin marketplace add ajitta/dialectic-skills
codex plugin add dia@dialectic-skills
```

- 更新：`codex plugin marketplace upgrade` 刷新 marketplace；`codex plugin list` 显示已安装的版本。
- 不使用插件：将 `skills/dia-<x>/` 文件夹复制到 `~/.agents/skills/`。以这种方式复制的技能名为 `$dia-<x>`，而不是 `$dia:dia-<x>`。

### ChatGPT 桌面版（含 Codex）与移动版

Codex 已包含在 ChatGPT 桌面应用中。在应用中按以下步骤安装：

1. **添加 marketplace：** 通过 GitHub 仓库（`ajitta/dialectic-skills`）、Git URL（`https://github.com/ajitta/dialectic-skills.git`）或本地文件夹（本仓库的克隆）添加。
2. **添加插件：** 在该 marketplace 的插件列表中选择 `dia` 并安装。只添加 marketplace 不会安装任何东西。

之后即可在 Codex 中使用这些技能；若你的套餐允许插件，也可在桌面版、网页版和移动版 ChatGPT 中使用。作者已在 Pro 套餐的桌面版和移动版上运行过。在 Business 和 Enterprise 工作区中，管理员还可以为整个工作区添加该插件（上传 zip 或导入 GitHub marketplace）。

### Windows

以上所有途径都适用于 Windows。技能不包含任何脚本，因此无需配置 Python 或 shell。

### 从早期版本迁移

- **从 1.0.0 迁移：** `dia-intent` 现已更名为 `dia-confirm`（1.1.0）。请使用新名称调用。通过 marketplace 安装的会在更新时获得此变更；上传的 zip 则须先删除，再上传新版本。
- **从作者早期的独立技能迁移：** 先删除旧副本，否则每种方法都会以两个名称加载两次。在 claude.ai 上：Customize › Skills 中删除 `reductio`、`negative-dialectics`、`self-refine`、`recursive-refine` 和 `confirm-intent`；Customize › Plugins 中删除 `socratic`。在 Claude Code 中：`/plugin uninstall socratic@ajitta-socratic`，并删除 `~/.claude/skills/` 下的副本。对于 Codex 和 ChatGPT 桌面版：删除 `~/.agents/skills/` 下的旧副本。

## 调用方式

共有三种方式，每个平台至少支持其中一种：

1. **用文字描述。** 直接要求使用某种方法："对……用反证法"、"对……做内在批判"、"请来一场苏格拉底式对话……"。这在所有平台上都有效，也是移动端的稳妥默认方式。适用于 `dia-reductio`、`dia-negative`、`dia-elenchus` 和 `dia-brainstorm`。
2. **在消息中写出名称。** 以技能名称开头：`dia-confirm …`、`dia-refine …`、`dia-iterate …`。`dia-refine` 和 `dia-iterate` 设计为以这种方式或显式选择来启动：`dia-iterate` 从不由普通请求触发；在 Claude Code 上，"修改一下这份草稿"这类普通请求也很少会加载 `dia-refine`。
3. **显式选择**，各平台写法不同：

| 平台 | 语法 | 示例 |
|---|---|---|
| claude.ai、Claude 桌面版、Claude Code | `/dia:dia-<x>` | `/dia:dia-reductio` |
| Codex（插件） | `$dia:dia-<x>` 后接一个空格 | `$dia:dia-confirm 写一个备份脚本` |
| Codex（复制的文件夹） | `$dia-<x>` | `$dia-refine` |
| ChatGPT | 输入 `@` 后选择技能 | `@dia-negative` |

在 Codex 上，`dia-confirm`、`dia-elenchus`、`dia-brainstorm` 和 `dia-iterate` 从不自动启动；请用 `$dia:dia-<x>` 选择。`dia-reductio`、`dia-negative` 和 `dia-refine` 在你的请求与之匹配时也可能自动启动。

### 选项

选项可以写成标志（flag），也可以用任何语言的普通文字表达：

- `--target=user|claude|text|all`（`dia-reductio`、`dia-negative`）：检验对象。`user` 指你提出的论断，`claude` 指助手自己之前的回答（适用于所有助手），`text` 指粘贴的文本，`all` 指其中存在的每一项。不加此标志时，技能会自行推断对象并在第一行说明。
- `--max N`（`dia-iterate`）：轮数上限，默认 3。
- 模式与深度（`dia-brainstorm`）：`develop`（默认）或 `stress`（"挑毛病"），以及 `quick`、`standard`（默认）或 `deep`。
- 标准（`dia-refine`、`dia-iterate`）：名称之后的任何内容，例如 `dia-refine — 核对数字` 或 `dia-refine 侧重语气`。

## 示例

以下提示均用中文书写；同样的请求用任何语言都有效，回复会跟随你所用的语言。输出说明已作简化。

### dia-confirm：开始工作前先对齐任务

```
dia-confirm 写一个脚本，把我所有的照片按日期重命名。
```

你会得到四个简短的部分，此时尚未开始工作：

- **目标与成功条件：** 要构建什么，以及如何判断已经完成。
- **依据与假设：** 助手核查了什么、假设了什么（例如，日期取自照片的元数据）。
- **需要用户做的决定：** 只列出必须由你决定的事项（操作系统、是否包含子文件夹、使用哪个日期）。
- **确认：** 回复什么即可继续。

回复你的答案并加上"继续"。修正加"继续"即视为批准修正后的任务；只给修正则会得到一份修订后的审查。该技能仅适用于这项任务及其直接后续。

### dia-elenchus：检验你对一个词的理解

```
请来一场苏格拉底式对话，先让我下定义。我想做一个午餐菜单推荐应用。
```

助手每条消息只问一个简短的问题，例如"好的推荐"是什么。它只依据你同意过的内容进行论证；当你的两个陈述无法同时成立时，它会把它们并列展示，并问你愿意修改哪一个。对话期间它不提供建议。当你停止、你的定义已穷尽（困惑，aporia）、或某个定义经受住多次检验时，对话结束，随后输出一份带结果的记录：困惑、成立（暂定）、部分检验、或检验前已停止。

### dia-brainstorm：用提问发展想法，然后做决定

```
和我来一场苏格拉底式头脑风暴：我需要一个周末副业项目的点子。简短一点。
```

在探究想法的过程中每条消息只问一个问题（`quick` 约 4 个问题，`standard` 8–10 个）。然后给出你自己的选项外加最多三个带标注的建议，按你设定的标准进行比较，给出结论，并可选附上简报。它从不编写代码或采取行动。随时说"停"或"收尾"即可直接跳到结论。

### dia-reductio：找出矛盾

```
对这个论断用反证法：远程办公总能提高生产力。
```

一次回复给出完整链条：论题；每个前提按来源标注（[T] 由对象陈述，[L] 逻辑或数学定律，[A] 由助手补充，如未明说的假设、定义或事实）；编号的推导行，每行注明所用规则；矛盾 Q 与非 Q 及其强度；你可以放弃的前提；一条建议；以及一份记录。助手不会替你做决定。要检验它自己的上一个回答：`--target=claude`，或说"用反证法检查你上一个回答"。

### dia-negative：用论断自身的标准检验它

```
对这个论断做内在批判：我们公司是扁平化的，所以任何人都可以自由发言。
```

引用论断自身的标准；列出其主张与实际兑现之间出现落差的发现，每条附一个具体案例；论断遗漏了什么；它实际起到什么作用，表述为可核查的推论，并附上能证明其错误的观察；然后是可选方案、一条建议和一份记录。它不会强行给出一个新的总定义。若想了解代码、命令或设置的作用，或只需一般性审查，请直接正常提问。

### dia-refine：一轮审查

```
dia-refine 核查事实：珠穆朗玛峰是世界第二高峰，所以攀登者最多。
```

一份分为四部分的缺陷清单（① 已确认的错误，② 遗漏的需求，③ 保留的正确内容，④ 尚存的不确定性），然后是一份修订版。只修正有确凿依据的缺陷：实际运行过的工具、你的指示或材料、或助手自己的重新推导。无法确认的疑似错误会连同疑似的修正一起列在 ④ 下，而不是被悄悄改掉。没有草稿时，"用 dia-refine 的方式完成这项任务"会先写出回答、检查一次，只展示最终版本。

### dia-iterate：多轮审查，每轮都经过核查

```
dia-iterate --max 2 核查你上一个回答中的日期和数字
```

每一轮都会指出缺陷，通过外部核查（搜索、运行工具、你提供的来源）逐一判定，只修正已确认的缺陷，并锁定已通过的内容。循环在出现退化、不再有缺陷、验证手段用尽、达到不动点或达到轮数上限时停止，并报告所做的修改、各轮摘要以及仍未验证的内容。在没有工具的聊天中，它会在第 1 轮后停止，并列出无法验证的条目。在句子中间提到 `dia-iterate` 不会启动循环；助手会请你发送一条以该名称开头的消息。

## 组合使用多个技能

- **在一个请求中同时使用 `dia-elenchus` 和 `dia-brainstorm`：** 先进行定义对话，第一条消息会说明这一点；当你要求给出选项或对话结束时，开始头脑风暴。两者从不交替进行。
- **在一个请求中同时使用 `dia-refine` 和 `dia-iterate`：** 二者作为两个独立的环节运行，分别输出。refine 环节自身的重新推导不算作 iterate 轮次的验证。
- **在一个请求中同时使用 `dia-reductio` 和 `dia-negative`：** 两者都会运行且回答都完整，因此输出很长（测试中约 9,000 个字符）。在手机上请一次只请求一个。
- **`dia-elenchus` 之后：** 如果你接着请求建议，助手会说明苏格拉底式部分已经结束，并把每条建议标注为它自己的建议。若要进行完整的选项与计划讨论，请点名 `dia-brainstorm`，它会接着那份记录继续。

## 故障排除

- **添加 marketplace 时出现 `Repository not found`。** 检查拼写：`ajitta/dialectic-skills`（是 dialectic，不是 dialectric）。该仓库是公开的，无需登录 GitHub。
- **Claude 移动版的 `/` 下没有 dia 技能。** 这是预期行为：移动版菜单不会列出插件技能。请用文字描述请求，或以技能名称开头发送消息。
- **每个技能都出现了两次。** 插件通过两种途径安装了（例如 `dia@dialectic-skills` 和 `dia@ajitta`，或一次上传加一次 marketplace）。删除其中一个。
- **claude.ai 上的 Skills 部分缺失或显示为灰色。** 打开 Settings › Capabilities › Code execution and file creation。
- **找不到 `dia-intent`。** 它已在 1.1.0 中更名为 `dia-confirm`。
- **`dia-iterate` 无法启动。** 只有当 `dia-iterate` 是消息的第一个词，或被显式选择时（`/dia:dia-iterate`、`$dia:dia-iterate`、`@dia-iterate`），它才会启动。
- **在 Codex 上 `$dia:dia-confirm:` 无法解析。** 技能名称后面应加空格，而不是冒号。
- **在 claude.ai 上上传被拒绝。** 请使用 Customize › Plugins › Upload plugin，而不是 Customize › Skills。

哪些途径已经验证过、如何验证的，记录在 [docs/probes.md](docs/probes.md) 中。

## 仓库结构

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

## 开发

```bash
python tools/package.py            # validate, write plugins/dia/ and the zip
python tools/package.py --check    # validate; fail if the committed output lags the source
python -m unittest discover -s tests -v
claude plugin validate --strict plugins/dia
```

请编辑 `skills/`，切勿编辑生成的输出。对技能文件的任何修改都需要在 `plugin-manifest.json` 中更新 `version`（以及该技能的 `metadata.version`）：Claude Code 仅在版本变化时才会更新已安装的插件，否则检查会失败。在发布的包中，韩文字符（Hangul）只允许出现在 `skills/<skill>/references/ko/` 下。本 README 有改动时，请在同一次提交中更新各译本；有测试会检查它们是否保持相同的结构。

## 许可证

MIT
