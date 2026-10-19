
"""Create an AI model profile card and estimate chat cost."""

# Store the model profile using the four required data types.
model_name = "llama3.2"
context_window = 128000
price_per_1k_tokens = 0.5  # Example price in PKR, not a verified market price.
runs_locally = True

print("--- AI Model Profile Card ---")

# Why: type() helps us understand how Python stores each value.
print(f"Model: {model_name} {type(model_name)}")
print(f"Context window: {context_window} tokens {type(context_window)}")
print(f"Price per 1K tokens: {price_per_1k_tokens} PKR {type(price_per_1k_tokens)}")
print(f"Runs locally: {runs_locally} {type(runs_locally)}")

# Why: int() converts the user's token count from text to a number.
tokens_per_chat = int(input("Tokens per chat: "))

# Why: dividing by 1000 matches the example price's unit.
estimated_cost = (tokens_per_chat / 1000) * price_per_1k_tokens
print(f"Estimated cost: {round(estimated_cost, 2)} PKR")

# Stretch goal: estimate monthly cost for 30 days.
chats_per_day = int(input("Chats per day: "))
monthly_cost = estimated_cost * chats_per_day * 30
print(f"Estimated monthly cost: {round(monthly_cost, 2)} PKR")
