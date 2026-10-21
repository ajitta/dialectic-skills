# Dialectic Skills (`dia`)

[English](README.md) | [한국어](README.ko.md) | [日本語](README.ja.md) | **简体中文**

网站: [ajitta.github.io/dialectic-skills](https://ajitta.github.io/dialectic-skills/)

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
- [技能指南与示例](#技能指南与示例)
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

claude.ai（网页版）：Customize › Plugins › Add › Add marketplace，输入 `ajitta/dialectic-skills`，然后选择 Discover › `dia` › Add。这样网页版和移动应用都能使用。详细步骤见下文。

然后试试：`对这个论断用反证法：远程办公总能提高生产力。`

## 安装

**在哪里安装，决定了 dia 出现在哪里。** 在网页版（claude.ai、chatgpt.com）安装会保存到你的账号，并出现在网页版和移动应用中。在桌面应用（Claude 桌面版、ChatGPT 桌面应用中的 Codex）安装则只留在那台电脑上。想在所有地方使用，请在网页版安装一次，并在你使用的每个桌面应用中各安装一次；作者就是这样使用的。

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

**Claude 桌面版：** 虽然是同样的 Customize › Plugins 页面，但只会安装到那台电脑上。作者测试发现，在 Claude 桌面版添加的插件没有出现在移动应用中，在 claude.ai 添加的插件也没有出现在 Claude 桌面版中。两者都用的话，请分别安装。

### Claude 移动版（iOS、Android）

无需安装步骤。在 claude.ai（网页版）添加的插件会保存到你的账号，并自动出现在移动应用中；在 Claude 桌面版添加的则不会。移动版的 `/` 菜单不会列出插件技能，但完整输入名称仍可启动技能，例如 `/dia-brainstorm`。也可以用自然语言提出请求，或以技能名称开头发送消息。

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

有两种途径。网页版和移动版用第一种，桌面应用用第二种；作者两种都在用：

1. **在网页版上传 zip（网页版和移动版）：** 从最新发布版下载 [`dialectic-skills-openai.zip`](https://github.com/ajitta/dialectic-skills/releases/latest/download/dialectic-skills-openai.zip)，在 chatgpt.com 通过插件 zip 上传添加。插件会保存到你的账号，因此会出现在 ChatGPT 网页版和移动版中。这个 zip 包含 ChatGPT 用的展示信息（描述、起始提示词、图标）。上传的插件不会自动更新；每个新版本都需重新上传。
2. **在桌面应用中添加 marketplace（仅限本机）：** Codex 已包含在 ChatGPT 桌面应用中。通过 GitHub 仓库（`ajitta/dialectic-skills`）、Git URL（`https://github.com/ajitta/dialectic-skills.git`）或本地文件夹（本仓库的克隆）添加 marketplace，再在其插件列表中选择 `dia` 并安装。这只会安装到桌面应用本地的 Codex 文件夹，不会保存到账号，因此不会出现在移动版或网页版中。更新通过 marketplace 获取。

在 Business 和 Enterprise 工作区中，管理员还可以为整个工作区添加该插件（上传 zip 或导入 GitHub marketplace）。

### Windows

以上所有途径都适用于 Windows。技能不包含任何脚本，因此无需配置 Python 或 shell。

## 调用方式

共有三种方式，每个平台至少支持其中一种：

1. **用文字描述。** 直接要求使用某种方法："对……用反证法"、"对……做内在批判"、"请来一场苏格拉底式对话……"。这在所有平台上都有效，也是移动端的稳妥默认方式。适用于 `dia-reductio`、`dia-negative`、`dia-elenchus` 和 `dia-brainstorm`。
2. **在消息中写出名称。** 以技能名称开头：`dia-confirm …`、`dia-refine …`、`dia-iterate …`。从 1.2.0 起，在 Codex 上无需 `$`、在 ChatGPT 上无需 `@`（已由所有者在手机应用中确认） 即可这样启动，这是在手机上最快的方式。`dia-refine` 和 `dia-iterate` 设计为以这种方式或显式选择来启动：`dia-iterate` 从不由普通请求触发；在 Claude Code 上，"修改一下这份草稿"这类普通请求也很少会加载 `dia-refine`。
3. **显式选择**，各平台写法不同：

| 平台 | 语法 | 示例 |
|---|---|---|
| claude.ai、Claude 桌面版、Claude Code | `/dia:dia-<x>` | `/dia:dia-reductio` |
| Claude 移动版 | 完整输入 `/dia-<x>` 或 `/dia:dia-<x>`（`/` 菜单中不会列出） | `/dia-brainstorm`、`/dia:dia-brainstorm` |
| Codex（插件） | `$dia:dia-<x>` 后接一个空格 | `$dia:dia-confirm 写一个备份脚本` |
| Codex（复制的文件夹） | `$dia-<x>` | `$dia-refine` |
| ChatGPT | 输入 `@` 后选择技能 | `@dia-negative` |

从 1.2.0 起，Codex 和 ChatGPT 也与 Claude 一样，所有技能对模型可见。`dia-reductio`、`dia-negative`、`dia-elenchus`、`dia-brainstorm` 和 `dia-refine` 在你的请求与之匹配时可能自动启动；`dia-confirm` 和 `dia-iterate` 设计为仅在消息以其名称开头或被显式选择（`$dia:dia-<x>`、`@`）时启动。不过在 Codex 上，如果用文字直接要求 `dia-confirm` 的步骤（如“先整理我的目标并列出待决事项”），也可能加载该技能。

### 选项

选项可以写成标志（flag），也可以用任何语言的普通文字表达：

- `--target=user|claude|text|all`（`dia-reductio`、`dia-negative`）：检验对象。`user` 指你提出的论断，`claude` 指助手自己之前的回答（适用于所有助手），`text` 指粘贴的文本，`all` 指其中存在的每一项。不加此标志时，技能会自行推断对象并在第一行说明。
- `--max N`（`dia-iterate`）：轮数上限，默认 3。
- 模式与深度（`dia-brainstorm`）：`develop`（默认）或 `stress`（"挑毛病"），以及 `quick`、`standard`（默认）或 `deep`。
- 标准（`dia-refine`、`dia-iterate`）：名称之后的任何内容，例如 `dia-refine — 核对数字` 或 `dia-refine 侧重语气`。

## 技能指南与示例

使用这些技能不需要任何哲学背景。每个技能都是人们沿用已久的一种思考方式，被整理成助手可以一步步照做的流程。下面为每个技能提供一段通俗的解释、一个可以直接试用的提示，以及一段真实会话（已删减）。

这些会话是在装有本插件的 Claude Code（Sonnet）上运行的；两个对话示例中的用户回复来自模拟用户，而不是事先写好的脚本。会话原本用英文进行，这里展示的是译文。每次运行得到的措辞都会有所不同。所有提示用任何语言都有效，助手会用你所写的语言回复。

**按你想做的事选择技能**

| 你想要…… | 使用 |
|---|---|
| 在助手动手之前，确认它真的理解了任务 | `dia-confirm` |
| 弄清楚自己说某个词或某个想法时到底指什么 | `dia-elenchus` |
| 把一个粗略的想法变成几个选项和一份计划 | `dia-brainstorm` |
| 检查一个论断能否自圆其说 | `dia-reductio` |
| 看看一句口号、一项政策或一个承诺是否做到了它自己说的话 | `dia-negative` |
| 把一个回答或一份草稿中的错误修正一遍 | `dia-refine` |
| 一轮一轮地彻底核查事实 | `dia-iterate` |

### dia-confirm：开始工作前先对齐任务

**通俗地说。** 靠谱的师傅开工前，会先跟你把活儿过一遍：我打算做成这样，我默认了这些情况，这几件事只有你能拍板。`dia-confirm` 让助手也这样做，然后等你点头，而不是自己去猜。

**适合使用的情况：** 请求很短，但结果取决于只有你知道的事情，比如一篇致辞、一份计划、一个脚本、一封写给重要人物的邮件。**不必使用的情况：** 只有一个明显答案的简单问题。

**试试：**

```
dia-confirm 帮我写一篇在我弟弟婚礼上用的简短致辞。
```

**会话示例**（已删减）：

> **助手：**
> **目标与成功条件：** 一篇关于你弟弟的简短婚礼致辞，可以直接朗读，约 1–2 分钟，语气温暖，最后举杯祝酒。
> **依据与假设：** 我没有任何关于你弟弟或这对新人的信息。我假设他是新郎，语气温暖并带点轻松幽默，用英文写。
> **需要用户做的决定：** 1. 名字；2. 一两个真实的细节，比如一段共同的回忆；3. 语气；4. 需要避开的内容。没有这些，我只能写一篇带占位符的通用致辞。
> **确认：** 回复"继续"并附上你的答案，或者告诉我用通用模板。
>
> **你：** 我弟弟叫 Minho，要娶 Sara；我是伴郎。别看他比我小，教会我骑自行车的却是他。语气温暖，带一个轻松的玩笑，大约 3 分钟。继续
>
> **助手：** 这是你的致辞，约 400 词……*（随后是致辞正文，围绕骑自行车的故事展开）*……说明：故事里的一些小细节是我编的；与实际情况不符的地方请改掉。

**小贴士**

- 只回答你在意的问题，再加上"继续"就行。修正加"继续"即视为批准修正后的任务。
- "看起来不错"、不回复或点个赞都不算批准；助手会继续等待。
- 它只覆盖这一项任务及其直接后续。如果想对新任务做同样的确认，请再次用 `dia-confirm` 开头。

### dia-elenchus：弄清你真正的意思

**通俗地说。** 这是苏格拉底在柏拉图对话录中使用的方法。你先说出你认为某样东西是什么（"好老师就是……"）。助手不会反驳你，也不会给出自己的看法。它每次只拿一个具体例子来问你，而每个例子都经过挑选，让你自己的回答开始和你的定义互相拉扯。然后你用自己的话修正定义。很多时候你最后会卡住，希腊语管这种状态叫**困惑（aporia）**。在这里，卡住是一种结果，而不是失败：你现在清楚地知道自己究竟哪一部分不知道，就不会在错误的假设上继续往下搭建。

**适合使用的情况：** 你依赖某个看似不言自明、却实实在在左右着决定的词：好老师、公平的分配、成功的项目、健康的关系。**不适合：** 寻求建议；对话期间它一条建议也不给。

**试试：**

```
请来一场苏格拉底式对话。我认为好老师就是学生考试分数高的老师。
```

**会话示例**（真实运行，已删减）：

> **助手：** 我不知道什么才算好老师，所以我来检验一下你的定义。假设一位老师在考试前一天把试题和答案发给学生，结果大家都考了高分。这算好老师吗？
>
> **你：** 不算，那基本就是作弊。也许好老师是学生能考高分、*而且是因为真正学会了内容*的老师。
>
> **助手：** 你的说法已经从"考试分数高"变成了"因为真正学会了内容而分数高"。现在设想一位老师，学生确实学会了，但试卷出得很差，所以分数很低。这算好老师吗？
>
> **你：** 算，试卷出得差是试卷的问题。所以分数其实并不是决定老师好坏的东西。
>
> **助手：** ……再看这样一个班：每个学生都把内容全学会了，但完全是靠自己，靠一本书和一位私人家教。老师什么都没贡献。这算好老师吗？
>
> **你：** 不算。所以好老师是那种教学真正帮助了学生学习的老师。
>
> *……又问了三个例子：学生逃课的老师、讲得同样清楚但面对不同班级的两位老师、什么办法都试过却都不奏效的老师……*
>
> **助手：** 你前面说过，那位学生逃课的老师仍然是好老师。那些学生算不算"有合理的条件参与"？
>
> **你：** 他们本来可以参与，只是自己选择不来，所以按我的新想法，那位老师不算好老师。这和我前面说的矛盾了。我卡住了。那我现在算是走到哪一步了？
>
> **助手：** 你已经到达了困惑（aporia），这是一种结果，而不是失败。好老师究竟应该由学生最终学到了什么来定义，还是由老师做了什么来定义，对你来说仍然悬而未决……*（随后是一份记录：你的定义如何变化、你同意过的前提、你现在知道自己不知道什么，以及一个留给你带走的问题；结果：困惑）*

**小贴士**

- 简短、诚实的回答效果最好。"我不确定"也是很好的回答。
- 当它指出你的说法"变了"时，只是在让你看到你的措辞怎样变化。保留哪一个由你决定。
- 随时说"停"即可拿到记录。如果之后想要建议，直接提出；助手会说明苏格拉底式部分已经结束，并把它的想法标注为它自己的观点。

### dia-brainstorm：让粗略的想法成形，再做决定

**通俗地说。** 就像一位教练，先问你几个好问题，再把选项交给你。它先一次问一个问题，弄清你想要什么、已经知道什么（苏格拉底式提问）。然后你列出选项，它补充几个自己的，你选出自己看重的标准，最后它给出结论和一份可以照着行动的简短简报。与 `dia-elenchus` 不同，它在提问之后确实会给出建议。

**适合使用的情况：** 你有目标但还没有计划：副业收入、职业转向、一个小项目、一次旅行。**不适合：** 把东西真正做出来；它从不写代码，也不采取行动。

**试试：**

```
和我来一场苏格拉底式头脑风暴，简短一点：我想在周末赚点外快。
```

**会话示例**（真实运行，已删减）：

> **助手：** 快速模式，大约 4 个问题。你的想法是在现有工作之外，利用周末赚点外快。是这样吗，还是我假设了你没有的意思？
>
> **你：** 对。每个周末大约 8 小时，每月大约 300 美元，启动资金不超过 200 美元。
>
> **助手：** 每个周末 8 小时，一个月大约 32 小时，所以 300 美元相当于每小时约 9 美元。你已经会做的事情里，有哪些是别人可能愿意付钱的？
>
> **你：** 我摄影不错，还有一台像样的相机。也许可以给本地小店拍照片。
>
> **助手：** 有人夸你是个好兆头，但还没有人付过钱给你，所以最大的未知数是有没有店愿意……假设接下来几个周末你去联系这些店。你要看到什么情况，才会判定这条路行不通？
>
> **你：** 如果三个周末里我联系了大约 10 家店，连一次便宜的试拍都没人答应，我就认为行不通。
>
> *……你又补充了几个选项（在周末市集卖照片冲印、卖图库照片、拍职业形象照、办一场"宠物摄影早晨"）；助手补充了自己的选项（给婚礼当副摄影师、带新手的摄影漫步、什么都不做）；你选了三条标准：启动成本低、不用花太多无偿修图时间就能赚到约 300 美元、做起来开心……*
>
> **助手：** **结论：未定。** 这个想法在我检验过的地方都站得住，但核心假设——有人愿意为这些照片付钱——还没有经过检验……**下一步：** 这周在两个社区群里发帖，提供 3–4 个公园拍摄时段，并记录预约数量、实际收费以及每位客户的修图分钟数。

**小贴士**

- 说明它该推得多用力："简短一点"、"深入一点"，或者"挑毛病"来做更严格的压力测试。
- 任何时候说"收尾"即可直接跳到结论和简报。
- 结论为"未定"表示关键假设仍需在现实中检验，简报会写明是哪一个。

### dia-reductio：检查一个论断能否自圆其说

**通俗地说。** 归谬法（反证法）：先完全按字面接受一个论断，一步步推下去，看它会不会推出两句不可能同时为真的话。如果会，那么出发点中必定有某一处要让步。助手会列出它用到的每个前提，标明哪些是它自己补充的，并把放弃哪一个的选择权留给你。

**适合使用的情况：** 你听到一条带着"总是""从不""所有人"的自信规则，或者想在为自己的立场辩护之前先检验一下它。**不适合：** 判断一个想法整体上是否明智；它只检验是否自洽。

**试试：**

```
对这个论断用反证法：顾客永远是对的。
```

**你会得到**（真实运行，已删减）：

> **所检验的解读：** "对"指的是真实，所以顾客说的任何话都是正确的。
> **前提：** P1 [A] "对"的意思是"真"；P2 [A] 关于同一件大衣，顾客 C1 说是在这里买的，顾客 C2 说不是；P3 [L] 如果非 p 为真，则 p 不为真。
> **推导：** 1. 每位顾客的断言都为真（论断本身）。…… 4. p 为真。…… 6. p 不为真。
> **矛盾：** 第 4 行与第 6 行。**强度：** 它依赖补充的前提 P1 和 P2，这两者是普通的事实，而不是逻辑。
> **可选方案：** 放弃"永远"；给"对"另一种含义；否认顾客之间会有分歧；或者修补这个论断："顾客出于善意的投诉值得公正对待，并在商家力所能及时得到补救。"
> **建议：** 采用修补后的论断，因为它保留了这句口号的本意。决定权在你。

标注的含义：**[T]** 由论断本身陈述，**[L]** 逻辑规则，**[A]** 由助手补充。依赖 [A] 前提才成立的矛盾，强度只和那个前提一样，助手会明确说明这一点。

**小贴士**

- 要检验助手自己上一个回答，可以写"用反证法检查你上一个回答"，或加上 `--target=claude`。
- 如果你认为某个 [A] 前提有误，直接说出来；助手会去掉它，重新推一遍。选择其中某个可选方案也是同样的做法。

### dia-negative：用论断自己的标准来衡量它

**通俗地说。** 不用你的价值观去评判一个论断，而是用它自己的话来评判它。抓住它承诺的内容（"任何人都可以随时提出问题"），去找它没有兑现的真实情形。然后追问这个论断在实际中到底起了什么作用，并把答案当作一个可以核查的猜测。这个技能的名字来自哲学家阿多诺的"否定的辩证法"；它用的是他那套思想中一个范围更窄、更实用的版本，叫作内部批判。

**适合使用的情况：** 一句口号、一项政策、一份使命宣言或一个计划听起来很好，而你想看看它漏掉了什么。**不适合：** 解释代码、命令或设置的作用，或做一般性审查。

**试试：**

```
对这个论断做内在批判："我们实行开门政策，所以公司里任何人都可以随时向管理层反映问题。"
```

**你会得到**（真实运行，已删减）：

> **它自己的标准：** "任何人"（没有例外）、"随时"（没有时间限制）、"向管理层反映问题"（问题能传达到管理层），以及"所以"（单凭这项政策就足够）。
> **F1. 对涉及管理层本身的问题，"任何人"不成立。** 如果你的问题出在你的经理身上，敞开的门通向的正是你要投诉的那个人，而政策没有提供第二条渠道。*遗漏之物：* 最不可能被提出来的那些问题。
> **F2. "随时"敌不过真实的工作时间。** 上夜班或远程办公的员工，没法在凌晨 3 点*找到经理本人*来反映。
> **F3. "所以"说过头了。** 政策给的只是许可；人们能否真正开口，还取决于开口之后会发生什么，比如得不到回应或遭到报复。
> **它实际起到的作用（一种推论）：** 把沉默的责任推给了没有走进那扇门的人。*什么能证明这一点是错的：* 一份记录，显示有针对经理的投诉通过这项政策被提出并得到处理。
> **可选方案：** 收窄论断；改变做法（第二条渠道、非工作时间的反映途径、不打击报复的承诺）；保留论断并公开说明其局限；撤回论断；用一个真实案例来检验它。**建议：** 改变做法。决定权在你。

**小贴士**

- 标为"有条件"的发现取决于你所处情况的事实，所以请把这些事实告诉助手。如果你说某条标准其实不是这个论断自己的，它会删掉依赖这条标准的发现，再运行一遍。
- 它会推荐一个方案，但从不替你做选择。

### dia-refine：对回答或草稿做一次仔细的审查

**通俗地说。** 就像一位细心的编辑从头到尾看一遍。助手列出哪里有问题，逐条核查，只修正它能够确认的错误。它怀疑但无法确认的错误会单独列出，并附上可能的修正，因此不会有任何内容被悄悄改掉。

**适合使用的情况：** 你有一份草稿，或者助手的上一个回答，希望把其中的事实错误、逻辑漏洞和缺漏的部分修正一遍。消息以 `dia-refine` 开头，如果有想侧重的地方，接着说明即可。

**试试：**

```
dia-refine 核查事实：中国的长城是唯一一个在月球上用肉眼就能看到的人造建筑，而且它完全是在明朝修建的。
```

**你会得到**（真实运行，使用了网页搜索，已删减）：

> **① 已确认的错误：** "在月球上能看到"是错误的（经搜索核实）：从大约 384,000 公里外看不到任何单个人造建筑，宇航员也说过，在太空中不借助工具看不到长城。"完全在明朝修建"是错误的：约公元前 220 年秦朝时就已把各段城墙连接起来，其他朝代也增修过一些段落。
> **② 遗漏的需求：** 无。
> **③ 保留的正确内容：** 今天所见的石砌长城大部分是明朝修建的。
> **④ 尚存的不确定性：** 秦、汉时期的确切年代因来源而异；只核查了二手资料。
> **修订后的表述：** 在月球上用肉眼看不到中国的长城，也看不到任何单个人造建筑。长城并非完全修建于明朝……*（附来源列表）*

**小贴士**

- 没有搜索工具时，助手仍然能修正它可以重新推导的逻辑和算术错误，并把未经核查的事实放在 ④ 下。
- "用 dia-refine 的方式完成这项任务"会让它先写出回答，审查一次，只展示最终版本。

### dia-iterate：分轮核查并修正

**通俗地说。** 和 `dia-refine` 类似，但分多轮进行，而且每一处修正都需要外部证据：一次搜索、一次工具运行，或你提供的来源。通过核查的事实会被锁定，后面的轮次不能再推翻。当没有可修的内容、无法再核实任何东西，或达到轮数上限时，循环会自行停止。

**适合使用的情况：** 准确比速度更重要，比如你即将发布的事实和日期。消息以 `dia-iterate` 开头；它从不由普通请求启动。

**试试：**

```
dia-iterate --max 2 核查这段话里的日期和事实："第一代 iPhone 于 2008 年开售，App Store 在同一天上线，提供 500 款应用。"
```

**你会得到**（真实运行，使用了网页搜索，已删减）：

> **修改：** "于 2008 年开售" → "2007 年"（2007 年 6 月 29 日开售）。"App Store 在同一天上线" → "大约一年后，即 2008 年 7 月"。
> **各轮摘要：** 第 1 轮：通过网页搜索核查了 3 条陈述，2 条确认有误，1 条正确。已锁定：iPhone 的日期、App Store 的日期、上线时约 500 款应用。因已没有缺陷而停止，所以不需要第 2 轮。
> **未验证：** 上线时的确切应用数量（各来源说法在 500 到 552 之间），以及 App Store 是在 2008 年 7 月 10 日还是 11 日上线。
> **修正后的段落：** "第一代 iPhone 于 2007 年开售，App Store 大约一年后、即 2008 年 7 月上线，提供 500 款应用。"

**小贴士**

- `--max N` 设置轮数上限（默认 3）。
- 在没有搜索或工具的聊天中，它会在第 1 轮后停止，列出无法核实的内容，而不是去猜。

## 组合使用多个技能

- **在一个请求中同时使用 `dia-elenchus` 和 `dia-brainstorm`：** 先进行定义对话，第一条消息会说明这一点；当你要求给出选项或对话结束时，开始头脑风暴。两者从不交替进行。
- **在一个请求中同时使用 `dia-refine` 和 `dia-iterate`：** 二者作为两个独立的环节运行，分别输出。refine 环节自身的重新推导不算作 iterate 轮次的验证。
- **在一个请求中同时使用 `dia-reductio` 和 `dia-negative`：** 两者都会运行且回答都完整，因此输出很长（测试中约 9,000 个字符）。在手机上请一次只请求一个。
- **`dia-elenchus` 之后：** 如果你接着请求建议，助手会说明苏格拉底式部分已经结束，并把每条建议标注为它自己的建议。若要进行完整的选项与计划讨论，请点名 `dia-brainstorm`，它会接着那份记录继续。

## 故障排除

- **添加 marketplace 时出现 `Repository not found`。** 检查拼写：`ajitta/dialectic-skills`（是 dialectic，不是 dialectric）。该仓库是公开的，无需登录 GitHub。
- **Claude 移动版的 `/` 下没有 dia 技能。** 这是预期行为：移动版菜单不会列出插件技能。请完整输入名称（例如 `/dia-brainstorm`）、用文字描述请求，或以技能名称开头发送消息。
- **dia 在一台设备上能用，在另一台上不能用。** 在桌面应用安装的只留在那台电脑上；在网页版安装的会保存到账号，并同步到移动应用。请在网页版安装一次（供网页版和移动版使用），并在你使用的每个桌面应用中各安装一次（见“安装”）。
- **每个技能都出现了两次。** 插件通过两种途径安装了（例如 `dia@dialectic-skills` 和 `dia@ajitta`，或一次上传加一次 marketplace）。删除其中一个。
- **claude.ai 上的 Skills 部分缺失或显示为灰色。** 打开 Settings › Capabilities › Code execution and file creation。
- **找不到 `dia-intent`。** 它已在 1.1.0 中更名为 `dia-confirm`。
- **`dia-iterate` 无法启动。** 只有当 `dia-iterate` 是消息的第一个词，或被显式选择时（`/dia:dia-iterate`、`$dia:dia-iterate`、`@dia-iterate`），它才会启动。
- **在 Codex 上 `$dia:dia-confirm:` 无法解析。** 技能名称后面应加空格，而不是冒号。
- **在 claude.ai 上上传被拒绝。** 请使用 Customize › Plugins › Upload plugin，而不是 Customize › Skills。
- **在 claude.ai 上 Check for updates 后仍是旧版本。** 在 Customize › Plugins 中移除 `dia`，再从 `dialectic-skills` 市场重新安装；如需自动获取后续版本，请打开 Sync automatically。

哪些途径已经验证过、如何验证的，记录在 [docs/probes.md](docs/probes.md) 中。

## 仓库结构

```
skills/dia-<x>/                 source: plain skills (SKILL.md, references/, agents/openai.yaml)
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
