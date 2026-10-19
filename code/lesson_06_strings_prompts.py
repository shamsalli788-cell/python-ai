
"""Clean user input and build a clear AI prompt."""

# Ask the user for a name and a question.
messy_name = input("Enter your name: ")
messy_question = input("Enter your question: ")

# Remove extra spaces and make the name easier to read.
clean_name = " ".join(messy_name.split()).title()

# Remove extra spaces and limit the question to 150 characters.
clean_question = " ".join(messy_question.split())[:150]

# Estimate tokens using the simple rule of roughly 1 token per 4 characters.
estimated_tokens = (len(clean_question) + 3) // 4

# Check for the word "python", ignoring uppercase/lowercase.
mentions_python = "python" in clean_question.lower()

print("\n--- Prompt Cleaner Results ---")
print(f"Clean name: {clean_name}")
print(f"Clean question: {clean_question}")
print(f"Question characters: {len(clean_question)}")
print(f"Estimated tokens: {estimated_tokens}")
print(f"Mentions Python: {mentions_python}")

# Build a multi-line prompt for an AI model.
prompt = f"""
You are a helpful programming tutor.
The user's name is {clean_name}.
Answer the following question clearly and simply:
{clean_question}
"""

print("\n--- Generated AI Prompt ---")
print(prompt.strip())

# Stretch goal: show how many characters were removed.
print(f"\nOriginal question length: {len(messy_question)}")
print(f"Clean question length: {len(clean_question)}")
