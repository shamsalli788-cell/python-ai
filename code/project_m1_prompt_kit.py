
"""
AI Prompt Kit for local businesses.

This tool helps small business owners create three professional
AI prompts for marketing, customer service, and business growth.
"""

# Business details help AI generate prompts relevant to the owner's needs.
business_name = input("Business name: ")
business_type = input("Business type: ")
city = input("City: ")
customers = input("Main customers: ")

# Converting the budget to an integer makes it easier to use as a number.
monthly_budget = int(input("Monthly budget (PKR): "))

# A clear heading makes the generated prompts easy to read and copy.
print("\n=========================================")
print(f"   AI Prompt Kit for {business_name}")
print("=========================================")

# Naming the platform and audience helps AI create more targeted marketing.
marketing_prompt = (
    f"Write a short Instagram post for {business_name}, "
    f"a {business_type} in {city}.\n"
    f"Target {customers}. Friendly tone, 1 call to action."
)

print("\n[1] Marketing")
print(marketing_prompt)

# A specific customer-service situation helps AI produce a useful reply.
customer_service_prompt = (
    f"You are the manager of {business_name}, a {business_type} in {city}. "
    f"Write a polite reply to an unhappy customer whose order arrived late. "
    f"Apologise and offer a small discount."
)

print("\n[2] Customer Service")
print(customer_service_prompt)

# Stating the budget helps AI focus on ideas the business can afford.
growth_prompt = (
    f"Suggest 3 low-cost AI tools a {business_type} in {city} can use "
    f"to attract {customers} with a budget of {monthly_budget} PKR per month. "
    f"Explain the purpose and estimated cost of each idea. "
    f"Clearly identify any prices that need verification."
)

print("\n[3] Growth")
print(growth_prompt)
print()
