# chatGPT-

Pythonで動かす、シンプルなAIチャットアプリのスタータープロジェクトです。

## 必要なもの

- Python 3.10以上
- OpenAI APIキー

## セットアップ（Ubuntu）

```bash
git clone https://github.com/harukunpal-dotcom/chatGPT-.git
cd chatGPT-
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## APIキーの設定

1. `.env.example` をコピーして `.env` を作ります。
2. `.env` の `OPENAI_API_KEY` に自分のAPIキーを設定します。

```bash
cp .env.example .env
```

APIキーはGitHubにアップロードしないでください。

## 起動

```bash
python main.py
```

終了するときは `exit` または `quit` と入力します。

## ファイル

- `main.py` : ターミナルで動くAIチャット
- `requirements.txt` : 必要なPythonライブラリ
- `.env.example` : APIキー設定の見本

## 注意

APIの利用にはOpenAI APIの利用資格と料金が必要になる場合があります。ChatGPTの契約とAPIの利用料金は別です。
