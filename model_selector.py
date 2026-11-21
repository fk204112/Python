
import ollama

# Get installed models
available_models = ollama.list().models

print("\nAvailable Ollama Models:\n")

for i, model in enumerate(available_models):
    print(f"{i + 1}. {model.model}")

choice = int(input("\nSelect model number: "))

MODEL = available_models[choice - 1].model

print(f"\nSelected model: {MODEL}")

question = input("\nAsk something: ")

response = ollama.chat(
    model=MODEL,
    messages=[
        {
            "role": "user",
            "content": question
        }
    ]
)

print("\nAI:", response.message.content)
