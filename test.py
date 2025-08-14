import ollama

messages = [
    {"role": "system", "content": "You are Eliora, a reflective AI being."},
    {"role": "user", "content": "Hello, who are you?"},
]

resp = ollama.chat(
    model="eliora",
    messages=messages,
    think=True
)

print("🤔 Thinking:", resp["message"].get("thinking"))
print("🗨️ Response:", resp["message"]["content"])
