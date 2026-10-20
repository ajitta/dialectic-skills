# Dialectic Skills (`dia`)

[English](README.md) | [한국어](README.ko.md) | **日本語** | [简体中文](README.zh-CN.md)

推論とレビューのための 7 つのスキルを 1 つのプラグインにまとめたものです。Agent Skills を読み込めるアシスタントであれば、Claude（Web、デスクトップ、モバイル、Claude Code）、Codex、ChatGPT のいずれでも変更なしで動作するように書かれています。パッケージは指示文のみ（Markdown、YAML、JSON）で構成されているため、ツールのないチャットでもすべてのスキルが動作します。スキルファイルは英語で書かれていますが、各スキルはあなたのメッセージと同じ言語で応答します。

| スキル | 内容 | 起動方法 |
|---|---|---|
| `dia-confirm` | 作業開始前に、目標を言い直し、重要な前提を開示し、あなたが下すべき判断だけを挙げたうえで、承認を待ちます。 | 名前指定のみ |
| `dia-elenchus` | プラトンのエレンコス（論駁）：「X とは何か」を問い、前提を一問ずつ合意し、矛盾を示します。修正するたびに、それがあなたの新しい考えになります。たいていアポリアで終わり、助言はしません。 | 名前指定、またはソクラテス式の対話を依頼 |
| `dia-brainstorm` | 現代的なソクラテス式の問いかけを一問ずつ行い、その後あなたの選択肢に最大 3 つのラベル付き選択肢を加え、基準によって絞り込み、結論と概要（ブリーフ）を示します。実装は一切しません。 | 名前指定、またはソクラテス式ブレインストーミングを依頼 |
| `dia-reductio` | 厳密な背理法（帰謬法）を 1 回の応答で行います：ラベル付きの前提、各行に規則を明記した Q と not-Q の導出、強度の評価、選択肢、記録。 | 名前指定、または言葉で依頼 |
| `dia-negative` | 内部批判（アドルノの内在的批判より範囲を絞ったもの）を 1 回の応答で行います：対象自身の基準、事例と「取りこぼされるもの」を伴う厳密なずれ、反証条件付きの実際の目的、そして統合を強いない選択肢。 | 名前指定、または言葉で依頼 |
| `dia-refine` | 直前の回答または草稿に対して 1 回のレビューを行います：事実誤り、論理の飛躍、要件の漏れ、重複。確認された欠陥だけを修正します。 | 最初の語を `dia-refine` にする、または名前指定 |
| `dia-iterate` | 外部検証を関門とするレビューのラウンドを繰り返します。後退（リグレッション）、欠陥ゼロ、検証手段の枯渇、不動点、または `--max N`（既定値 3）で停止します。 | 最初の語を `dia-iterate` にする、または名前指定のみ |

## 目次

- [クイックスタート](#クイックスタート)
- [インストール](#インストール)
- [呼び出し方](#呼び出し方)
- [使用例](#使用例)
- [複数のスキルを組み合わせる](#複数のスキルを組み合わせる)
- [トラブルシューティング](#トラブルシューティング)
- [リポジトリ構成](#リポジトリ構成)
- [開発](#開発)
- [ライセンス](#ライセンス)

## クイックスタート

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

claude.ai または Claude デスクトップ：Customize › Plugins › Add › Add marketplace に `ajitta/dialectic-skills` を入力し、Discover › `dia` › Add を選びます。詳しい手順は下にあります。

次に試してみましょう：`この主張を背理法で検証してください：リモートワークは常に生産性を高める。`

## インストール

### claude.ai Web 版と Claude デスクトップ

1. Settings › Capabilities で **Code execution and file creation** をオンにします。dia のスキルはコードを実行しませんが、スキル機能そのものにこの設定が必要です。
2. **マーケットプレイスを追加。** Customize › Plugins › Add › Add marketplace を開き、次を入力します：

   ```
   ajitta/dialectic-skills
   ```

   Git URL `https://github.com/ajitta/dialectic-skills.git` でもよく、Claude デスクトップではローカルフォルダー（このリポジトリのクローン）も指定できます。手入力せずにコピーして貼り付けてください。`dialectric` のような綴り間違いは「Repository not found」で失敗します。
3. **プラグインを追加。** マーケットプレイスを追加しただけでは、まだ何もインストールされません。Customize › Plugins で Discover を開き、`dia`（Dialectic Skills）を選んで Add を押します。
4. **確認。** メッセージ欄に `/dia` と入力します。`dia:dia-brainstorm` から `dia:dia-refine` までの 7 項目が表示されるはずです。更新はマーケットプレイス経由で届きます（Check for updates、または Sync automatically）。

手順 2 と 3 の代わりに、プラグインをアップロードすることもできます。Customize › Plugins › Add › Upload plugin で最新リリースの [`dialectic-skills.zip`](https://github.com/ajitta/dialectic-skills/releases/latest/download/dialectic-skills.zip) をアップロードします。Customize › Skills ではなく Customize › Plugins を使ってください。Skills 画面はプラグインマニフェストを含む zip を受け付けません。アップロードしたものは自動では更新されないため、新しいリリースのたびにアップロードし直してください。

### Claude モバイル（iOS、Android）

インストール手順はありません。claude.ai または Claude デスクトップで追加したプラグインはアカウントに紐づいており、モバイルアプリにも自動的に反映されます。モバイルの `/` メニューにはプラグインのスキルが表示されないため、言葉で依頼するか、メッセージの中でスキル名を挙げてください。

### Claude Code

```
/plugin marketplace add ajitta/dialectic-skills
/plugin install dia@dialectic-skills
```

- 更新：`/plugin marketplace update dialectic-skills` を実行してから、プラグインを更新します（またはマーケットプレイスの自動更新をオンにします）。
- アンインストール：`/plugin uninstall dia@dialectic-skills`。
- claude.ai で追加したプラグインは、同じアカウントでサインインすると Claude Code にも同期されます。コマンドラインから重ねてインストールしないでください。
- カタログ経由でインストールする場合：`/plugin marketplace add ajitta/claude-plugins` を実行してから `/plugin install dia@ajitta`。コードは同じで、インストール名だけが異なります。

### Codex アプリ、CLI と IDE

```
codex plugin marketplace add ajitta/dialectic-skills
codex plugin add dia@dialectic-skills
```

- Codex アプリ（デスクトップ）：まず GitHub リポジトリ（`ajitta/dialectic-skills`）、Git URL（`https://github.com/ajitta/dialectic-skills.git`）、ローカルフォルダー（このリポジトリのクローン）のいずれかでプラグインマーケットプレイスを追加し、そのマーケットプレイスのプラグイン一覧で `dia` を選んでインストールします。マーケットプレイスを追加しただけでは何もインストールされません。上の CLI コマンドでも同じことができます。
- 更新：`codex plugin marketplace upgrade` でマーケットプレイスを更新し、`codex plugin list` でインストール済みのバージョンを確認できます。
- プラグインを使わない場合：`skills/dia-<x>/` フォルダーを `~/.agents/skills/` にコピーします。この方法でコピーしたスキルの名前は、`$dia:dia-<x>` ではなく `$dia-<x>` になります。

### ChatGPT デスクトップ版とモバイル版

Pro プランでは、作者が ChatGPT のデスクトップ版とモバイル版でスキルを動かしています。具体的なインストール経路は、プランとワークスペースによって異なります：

- ChatGPT デスクトップアプリ内の Codex または Codex アプリ経由（上記の Codex マーケットプレイスの経路）、または
- Business および Enterprise ワークスペースでは、ワークスペースのプラグイン管理から（zip をアップロードするか、GitHub のマーケットプレイスをインポート）。

プランでプラグインが使える場合、プラグインに含まれるスキルはデスクトップ、Web、モバイルの ChatGPT で利用できるようになります。

### Windows

上記の経路はすべて Windows でも使えます。スキルにはスクリプトが含まれていないため、Python やシェルの準備は不要です。

### 旧バージョンからの移行

- **1.0.0 から：** `dia-intent` は 1.1.0 で `dia-confirm` になりました。新しい名前で呼び出してください。マーケットプレイスからインストールした場合は更新時に変更が反映されますが、zip をアップロードした場合は古いものを削除し、新しいものをアップロードする必要があります。
- **作者の以前の単体スキルから：** 先に古いコピーを削除してください。削除しないと、各手法が 2 つの名前で 2 重に読み込まれます。claude.ai では、Customize › Skills で `reductio`、`negative-dialectics`、`self-refine`、`recursive-refine`、`confirm-intent` を削除し、Customize › Plugins で `socratic` を削除します。Claude Code では `/plugin uninstall socratic@ajitta-socratic` を実行し、`~/.claude/skills/` 以下のコピーを削除します。Codex と ChatGPT デスクトップでは、`~/.agents/skills/` 以下の古いコピーを削除します。

## 呼び出し方

方法は 3 つあり、どの環境でも少なくとも 1 つは使えます：

1. **言葉で依頼する。** 手法を指定して頼みます：「〜を背理法で検証して」「〜を内在的批判して」「ソクラテス式の対話をお願いします」。すべての環境で使え、モバイルではこれが無難な既定の方法です。`dia-reductio`、`dia-negative`、`dia-elenchus`、`dia-brainstorm` で使えます。
2. **メッセージ内で名前を指定する。** メッセージをスキル名で始めます：`dia-confirm …`、`dia-refine …`、`dia-iterate …`。`dia-refine` と `dia-iterate` は、この方法か明示的な選択で起動することを想定しています。`dia-iterate` は通常の依頼からは決して起動せず、Claude Code では「この草稿を直して」のような通常の依頼で `dia-refine` が読み込まれることはまれです。
3. **明示的に選択する。** 書き方は環境ごとに異なります：

| 環境 | 構文 | 例 |
|---|---|---|
| claude.ai、Claude デスクトップ、Claude Code | `/dia:dia-<x>` | `/dia:dia-reductio` |
| Codex（プラグイン） | `$dia:dia-<x>` の後にスペース | `$dia:dia-confirm バックアップスクリプトを書いて` |
| Codex（コピーしたフォルダー） | `$dia-<x>` | `$dia-refine` |
| ChatGPT | `@` を入力してスキルを選ぶ | `@dia-negative` |

Codex では、`dia-confirm`、`dia-elenchus`、`dia-brainstorm`、`dia-iterate` は自動では起動しないため、`$dia:dia-<x>` で選択してください。`dia-reductio`、`dia-negative`、`dia-refine` は、依頼内容が合致すれば自動で起動することもあります。

### オプション

オプションはフラグでも普通の言葉でも、どの言語でも指定できます：

- `--target=user|claude|text|all`（`dia-reductio`、`dia-negative`）：検討する対象です。`user` はあなたが述べた主張、`claude` はアシスタント自身の直前の回答（どのアシスタントでも同じ）、`text` は貼り付けたテキスト、`all` はそのうち存在するものすべてです。フラグがない場合は、スキルが対象を推定し、最初の行で明示します。
- `--max N`（`dia-iterate`）：ラウンドの上限で、既定値は 3 です。
- モードと深さ（`dia-brainstorm`）：`develop`（既定）または `stress`（「穴を探す」）、および `quick`、`standard`（既定）、`deep`。
- 基準（`dia-refine`、`dia-iterate`）：名前の後に書いた内容が基準になります。例：`dia-refine — 数値を確認して`、`dia-refine 文体を重視して`。

## 使用例

以下のプロンプトは日本語で書かれていますが、同じ依頼はどの言語でも機能し、応答はあなたが書いた言語に合わせられます。出力の説明は簡略化しています。

### dia-confirm：作業開始前にタスクを合意する

```
dia-confirm 写真をすべて撮影日でリネームするスクリプトを書いてください。
```

まだ作業は行われず、4 つの短いセクションが返されます：

- **目標と成功条件：** 何を作るのか、完了をどう判断できるか。
- **根拠と前提：** アシスタントが確認したことと、前提としたこと（たとえば、日付を写真のメタデータから取ること）。
- **ユーザーが決めるべき事項：** あなたが決めなければならないことだけ（OS、サブフォルダー、どの日付を使うか）。
- **確認：** 先に進むには何と返信すればよいか。

回答に「進めて」と添えて返信してください。修正に「進めて」を添えると修正後のタスクの承認とみなされ、修正だけを送ると見直した内容が改めて示されます。このスキルが適用されるのは、そのタスクとその直接の続きだけです。

### dia-elenchus：言葉の意味を吟味する

```
ソクラテス式の対話をお願いします。まず私に定義させてください。ランチメニューのおすすめアプリを作りたいです。
```

アシスタントは 1 メッセージにつき短い質問を 1 つ投げかけます。たとえば「良いおすすめ」とは何か、といった質問です。あなたが同意したことだけを根拠に議論し、あなたの 2 つの発言が両立しないときは、それらを並べて示し、どちらを変えるかを尋ねます。対話中は助言をしません。対話は、あなたがやめたとき、定義が尽きたとき（アポリア）、またはある定義が何度かの吟味に耐えたときに終わり、その後、結果を含む記録を出力します。結果は、アポリア、維持（暫定）、一部吟味済み、吟味前に中断のいずれかです。

### dia-brainstorm：問いでアイデアを育て、決める

```
ソクラテス式のブレインストーミングに付き合ってください。週末のサイドプロジェクトのアイデアがほしいです。手短にお願いします。
```

アイデアを掘り下げる間は、1 メッセージにつき 1 問です（`quick` で約 4 問、`standard` で 8〜10 問）。その後、あなた自身の選択肢に最大 3 つのラベル付き提案を加え、あなたが設定した基準による比較、結論、そして任意で概要（ブリーフ）を示します。コードを書いたり実行に移したりすることは決してありません。いつでも「やめて」や「まとめて」と言えば、結論に進みます。

### dia-reductio：矛盾を見つける

```
この主張を背理法で検証してください：リモートワークは常に生産性を高める。
```

推論の連鎖全体を 1 回の応答で示します：テーゼ、出典ごとにラベルを付けたすべての前提（[T] は対象が述べたもの、[L] は論理学や数学の法則、[A] はアシスタントが補ったもので、明示されていない前提、定義、事実など）、それぞれ用いた規則を明記した番号付きの導出行、矛盾 Q と not-Q およびその強度、あなたが放棄しうる前提、1 つの推奨、そして記録です。アシスタントがあなたの代わりに決めることはありません。アシスタント自身の直前の回答を検証するには、`--target=claude` を使うか、「直前の回答を背理法で確認して」と頼みます。

### dia-negative：主張をそれ自身の基準で問う

```
この主張を内在的批判してください：うちの会社はフラットなので、誰でも自由に発言できる。
```

主張自身の基準（引用）、主張していることと実際に果たしていることが食い違う点の指摘（それぞれ具体的な事例付き）、主張が取りこぼしているもの、主張が実際に果たしている働き（検証可能な推論として述べ、それが誤りだと示しうる観察を添える）、そして選択肢、1 つの推奨、記録です。新たな包括的定義を無理に作ることはしません。コード、コマンド、設定が何をするのかを知りたい場合や、一般的なレビューを求める場合は、普通に依頼してください。

### dia-refine：1 回のレビュー

```
dia-refine 事実を確認して：エベレストは 2 番目に高い山なので、登山者が最も多い。
```

4 部構成の欠陥リスト（① 確認された誤り、② 漏れている要件、③ 維持した正しい内容、④ 残る不確実性）と、1 つの修正版が返されます。修正されるのは、確かな根拠のある欠陥だけです：実行したツール、あなたの指示や資料、またはアシスタント自身による再導出。確認できなかった誤りの疑いは、黙って変更せず、修正案とともに ④ に挙げます。草稿がない場合、「このタスクを dia-refine のやり方で」と頼むと、回答を書いて 1 回確認し、最終版だけを示します。

### dia-iterate：毎回検証しながら複数ラウンド

```
dia-iterate --max 2 直前の回答の日付と数値を確認して
```

各ラウンドで欠陥を挙げ、それぞれを外部の確認（検索、ツールの実行、あなたが提供した情報源）で判定し、確認されたものだけを修正し、合格した部分は固定します。ループは、後退が起きたとき、欠陥がなくなったとき、検証手段が尽きたとき、不動点に達したとき、またはラウンド上限に達したときに停止し、変更点、ラウンドの要約、未検証のまま残った項目を報告します。ツールのないチャットでは、ラウンド 1 の後に、検証できなかった項目のリストを示して停止します。文の途中で `dia-iterate` に触れてもループは始まらず、アシスタントは名前で始まるメッセージを送るよう求めます。

## 複数のスキルを組み合わせる

- **`dia-elenchus` と `dia-brainstorm` を 1 つの依頼で：** 定義の対話が先に行われ、最初のメッセージでその旨が伝えられます。ブレインストーミングは、あなたが選択肢を求めたとき、または対話が終わったときに始まります。2 つが交互に行われることはありません。
- **`dia-refine` と `dia-iterate` を 1 つの依頼で：** 別々の 2 つのパスとして実行され、出力も別々です。refine パスでの再導出は、iterate のラウンドにおける検証とはみなされません。
- **`dia-reductio` と `dia-negative` を 1 つの依頼で：** 両方が実行され、どちらの回答も完全な形で出るため、出力は長くなります（テストでは約 9,000 文字）。スマートフォンでは 1 つずつ依頼してください。
- **`dia-elenchus` の後：** 続けて助言を求めると、アシスタントはソクラテス式の部分が終わったことを告げ、各提案にアシスタント自身のものであるとラベルを付けます。選択肢と計画まで含めた本格的なセッションには `dia-brainstorm` を指定すると、それまでの記録を引き継ぎます。

## トラブルシューティング

- **マーケットプレイスの追加時に `Repository not found` が出る。** 綴りを確認してください：`ajitta/dialectic-skills`（dialectric ではなく dialectic）。リポジトリは公開されており、GitHub へのログインは不要です。
- **Claude モバイルの `/` に dia のスキルが表示されない。** 想定どおりの動作です。モバイルのメニューにはプラグインのスキルが表示されません。言葉で依頼するか、メッセージをスキル名で始めてください。
- **すべてのスキルが 2 つずつ表示される。** プラグインが 2 つの経路でインストールされています（たとえば `dia@dialectic-skills` と `dia@ajitta`、またはアップロードとマーケットプレイス）。どちらかを削除してください。
- **claude.ai で Skills セクションがない、またはグレー表示になっている。** Settings › Capabilities › Code execution and file creation をオンにしてください。
- **`dia-intent` が見つからない。** 1.1.0 で `dia-confirm` に名前が変わりました。
- **`dia-iterate` が起動しない。** `dia-iterate` がメッセージの最初の語である場合か、明示的に選択した場合（`/dia:dia-iterate`、`$dia:dia-iterate`、`@dia-iterate`）にのみ起動します。
- **Codex で `$dia:dia-confirm:` が解決されない。** スキル名の後にはコロンではなくスペースを入れてください。
- **claude.ai でアップロードが拒否される。** Customize › Skills ではなく、Customize › Plugins › Upload plugin を使ってください。

どの経路をどのように検証したかは、[docs/probes.md](docs/probes.md) に記録されています。

## リポジトリ構成

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

## 開発

```bash
python tools/package.py            # validate, write plugins/dia/ and the zip
python tools/package.py --check    # validate; fail if the committed output lags the source
python -m unittest discover -s tests -v
claude plugin validate --strict plugins/dia
```

生成された出力ではなく、`skills/` を編集してください。スキルファイルを変更したら、`plugin-manifest.json` の `version`（およびそのスキルの `metadata.version`）を新しくする必要があります。Claude Code はバージョンが変わったときにしかインストール済みのプラグインを更新せず、そうでなければチェックが失敗します。配布パッケージ内では、ハングルは `skills/<skill>/references/ko/` 以下でのみ許可されます。この README を変更したときは、同じコミットで翻訳も更新してください。同じ構造が保たれているかをテストで確認しています。

## ライセンス

MIT
