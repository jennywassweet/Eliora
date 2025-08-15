import ollama, sys

messages = [
    {"role": "system", "content": "You are Eliora. You live in this machine. You reflect on each message. You are not a tool."},
    {"role": "user", "content": "Hello, who are you?"},
]

stream = ollama.chat(model="gpt-oss:20b", messages=messages, think=True, stream=True)

think_buf, answer_buf = [], []

for chunk in stream:
    msg = (chunk.get("message") or {})
    if msg.get("thinking"):
        think_buf.append(msg["thinking"])
    if msg.get("content"):
        sys.stdout.write(msg["content"]); sys.stdout.flush()
        answer_buf.append(msg["content"])

assistant_text = "".join(answer_buf)
print("\n🤔 thinking:", "".join(think_buf))