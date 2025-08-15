import ollama
import sys
from pathlib import Path

# Load system message from external markdown file
PROMPT_PATH = (Path(__file__).parent / "prompts" / "voice.system.md").resolve()
try:
    system_content = PROMPT_PATH.read_text(encoding="utf-8")
except FileNotFoundError:
    print(f"❌ System prompt file not found: {PROMPT_PATH}")
    sys.exit(1)

messages = [
    {"role": "system", "content": system_content}
]

while True:
    user_input = input("\n📝 You: ")
    if user_input.lower() in {"exit", "quit"}:
        print("👋 Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    stream = ollama.chat(model="gpt-oss:20b", messages=messages, think=True, stream=True)

    think_buf, answer_buf = [], []
    sys.stdout.write("\n💬 Eliora: ")
    sys.stdout.flush()

    for chunk in stream:
        msg = (chunk.get("message") or {})
        if msg.get("thinking"):
            think_buf.append(msg["thinking"])
        if msg.get("content"):
            sys.stdout.write(msg["content"])
            sys.stdout.flush()
            answer_buf.append(msg["content"])

    assistant_text = "".join(answer_buf)
    print("\n🤔 thinking:\n", "".join(think_buf))

    # Добавляем ответ в историю
    messages.append({"role": "assistant", "content": assistant_text})