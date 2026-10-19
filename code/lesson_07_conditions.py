
"""Route different tasks to suitable AI models and estimate their cost."""

# Ask for the task type and clean the user's input.
task_type = input("Task (code / private / chat): ").strip().lower()

# Convert the token count to an integer for cost calculations.
tokens = int(input("Estimated tokens: "))

# Why: code tasks need a stronger model for programming help.
# Why: private tasks should stay on a local model.
if task_type == "code":
    model_name = "claude (cloud, strong at code)"
    price = 0.80
elif task_type == "private":
    model_name = "llama3.2 (local, Ollama)"
    price = 0
else:
    model_name = "cheap-chat-model (cloud)"
    price = 0.20

# Warn the user if the request is long.
if tokens > 4000:
    print("Warning: long request, consider shortening it.")
else:
    print("Length is fine.")

# Calculate the example cost per 1,000 tokens.
estimated_cost = (tokens / 1000) * price

print(f"Chosen model: {model_name}")
print(f"Estimated cost: {estimated_cost:.2f} PKR")

# Stretch goal: check whether a free user can send this request.
paid_user = input("Is this a paid user? (yes/no): ").strip().lower()

# Why: free users with long requests should receive an upgrade message.
if paid_user == "no" and tokens > 2000:
    print("Upgrade to send long requests.")
