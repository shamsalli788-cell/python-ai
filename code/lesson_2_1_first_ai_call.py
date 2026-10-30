
"""Lesson 2.1: AI Tutor using LangChain and Ollama."""

import time
from langchain.chat_models import init_chat_model

# 1. Create the AI model
tutor = init_chat_model(
    "llama3.2:1b",
    model_provider="ollama",
    temperature=0.2
)

# 2. Get information from the student
topic = input("Enter a topic: ")
level = input("Enter your level (Beginner, Intermediate, Advanced): ")

# 3. Give instructions to AI
SYSTEM = f"""
You are a friendly Python AI tutor.
Teach the student about the given topic.
Student level: {level}
Use simple English and easy examples.
Explain step by step.
"""

# 4. Send the question to AI and measure time
start_time = time.perf_counter()

response = tutor.invoke([
    {"role": "system", "content": SYSTEM},
    {"role": "user", "content": f"Teach me about {topic}."}
])

end_time = time.perf_counter()

# 5. Display the AI answer
print("\n========== AI TUTOR ==========")
print(response.text)

# 6. Display token count and response time
tokens = response.usage_metadata["output_tokens"]
elapsed_time = end_time - start_time

print("\n========== USAGE REPORT ==========")
print(f"Output Tokens: {tokens}")
print(f"Response Time: {elapsed_time:.2f} seconds")
