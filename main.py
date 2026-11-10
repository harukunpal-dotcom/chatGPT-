import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise SystemExit(
        "APIキーが設定されていません。.env ファイルに OPENAI_API_KEY を設定してください。"
    )

client = OpenAI(api_key=api_key)
messages = [
    {"role": "system", "content": "あなたは親切で分かりやすい日本語のアシスタントです。"}
]

print("chatGPT- を起動しました！")
print("メッセージを入力してください。終了するには exit と入力します。")

while True:
    try:
        user_text = input("\nあなた: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\n終了します。")
        break

    if user_text.lower() in {"exit", "quit"}:
        print("またね！")
        break

    if not user_text:
        continue

    messages.append({"role": "user", "content": user_text})

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
        )
        answer = response.choices[0].message.content or ""
        print(f"\nAI: {answer}")
        messages.append({"role": "assistant", "content": answer})
    except Exception as error:
        print(f"\nエラー: {error}")
        messages.pop()
