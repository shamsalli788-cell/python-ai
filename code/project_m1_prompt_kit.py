
"""
AI Prompt Kit for a Local Business.

This tool asks for basic business details and creates three
professional AI prompts for marketing, customer service, and growth.
It is designed for small business owners who need help writing prompts.
"""

# Ask the business owner for five details.
business_name = input("Business name: ")
business_type = input("Business type (e.g. bakery): ")
city = input("City: ")
customers = input("Main customers (e.g. students, families): ")
budget = int(input("Monthly budget (PKR): "))

# A clear header helps the user identify their personalised prompt kit.
print()
print("=" * 41)
print(f"  AI Prompt Kit for {business_name}")
print("=" * 41)

# Why 1: Naming the platform, audience, and tone makes marketing prompts specific.
marketing_prompt = (
    f"Write a short Instagram post for {business_name}, "
    f"a {business_type} in {city}.\n"
    f"Target audience: {customers}. "
    f"Use a friendly tone and include 1 clear call to action."
)

# Why 2: Giving the AI a role and a real customer problem guides its reply.
customer_service_prompt = (
    f"You are the customer service manager of {business_name}, "
    f"a {business_type} in {city}.\n"
    f"Write a polite, empathetic reply to a customer whose order "
    f"arrived late. Apologise sincerely and offer a small discount. "
    f"Do not invent a discount percentage or company policy."
)

# Why 3: Setting a number and budget makes growth suggestions practical.
growth_prompt = (
    f"Suggest exactly 3 low-cost AI ideas for a {business_type} "
    f"in {city} to attract {customers}.\n"
    f"Monthly budget: {budget} PKR. "
    f"For each idea, explain how it works, its estimated monthly cost "
    f"in PKR, and how to get started. "
    f"Clearly label estimates and do not invent verified prices."
)

# Print the three prompts in a clean, copy-friendly format.
print("\n[1] Marketing")
print("-" * 41)
print(marketing_prompt)

print("\n[2] Customer Service")
print("-" * 41)
print(customer_service_prompt)

print("\n[3] Growth")
print("-" * 41)
print(growth_prompt)

print("\n" + "=" * 41)
print("Your three AI prompts are ready to use!")
print("=" * 41)
