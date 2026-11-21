
import ollama

MODEL = "deepseek-r1:7b"

messages = []

print("\n===== STREAMING AI CHATBOT =====")
print("Type 'exit' to quit.\n")

while True:

    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    messages.append({
        "role": "user",
        "content": user_input
    })

    stream = ollama.chat(
        model=MODEL,
        messages=messages,
        stream=True
    )

    print("\nAI: ", end="", flush=True)

    full_response = ""

    for chunk in stream:

        text = chunk.message.content

        print(text, end="", flush=True)

        full_response += text

    print("\n")

    messages.append({
        "role": "assistant",
        "content": full_response
    })
