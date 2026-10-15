
"""
Business Prompt Builder

Collects basic business information from the user
and creates a ready-to-use AI prompt.
"""

# Personal details make the welcome message more friendly.
name = input("Your name: ")

# Business type helps AI suggest relevant solutions.
business = input("Business type: ")

# Knowing the problem helps AI generate useful suggestions.
problem = input("Biggest problem: ")

print(f"\nWelcome, {name}!")

print("--- Your AI Prompt ---")

# An f-string inserts the user's business details into the prompt.
prompt = f"Suggest 3 AI solutions for a {business} that struggles with {problem}."

print(prompt)

