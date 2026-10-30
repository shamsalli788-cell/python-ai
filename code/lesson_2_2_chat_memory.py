
"""Lesson 2.2: Personal Tutor with Memory."""

from langchain.chat_models import init_chat_model

# Maximum conversation messages to remember
MAX_MESSAGES = 6

# Create AI model once
llm = init_chat_model(
    "llama3.2:1b",
    model_provider="ollama",
    temperature=0.2
)

# Store conversation history
messages = [
    {
        "role": "system",
        "content": (
            "You are a friendly personal AI tutor. "
            "Answer in simple English with easy examples. "
            "Remember the student's conversation."
        )
    }
]

print("\n===== PERSONAL AI TUTOR =====")
print("Commands: /reset, /count, bye")

while True:
    text = input("\nYou: ").strip()

    # Exit chatbot
    if text.lower() == "bye":
        print("Tutor: Goodbye! Keep learning.")
        break

    # Reset conversation memory
    elif text.lower() == "/reset":
        messages = [messages[0]]
        print("Tutor: Memory cleared successfully.")

    # Show memory count
    elif text.lower() == "/count":
        print(f"Tutor: Total messages in memory: {len(messages)}")
        print(f"Tutor: Conversation messages: {len(messages) - 1}")

    # Handle empty input
    elif text == "":
        print("Tutor: Please type something.")

    else:
        # Save user's message
        messages.append({
            "role": "user",
            "content": text
        })

        # Keep system instructions and latest 6 messages
        messages = [messages[0]] + messages[1:][-MAX_MESSAGES:]

        # Send complete history to AI
        response = llm.invoke(messages)

        # Save AI response
        answer = response.text

        messages.append({
            "role": "assistant",
            "content": answer
        })

        # Display answer and token usage
        print(f"Tutor: {answer}")
        print(
            f"     Tokens sent: "
            f"{response.usage_metadata['input_tokens']}"
        )
        print(f"     Memory: {len(messages) - 1} conversation messages")
