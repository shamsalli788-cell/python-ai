
"""AI front desk for Sweet Crumbs bakery.
Answers common questions, calculates quotes, and prepares AI prompts.
"""

BOT_NAME = "Sweet Crumbs Desk"
BUSINESS_NAME = "Sweet Crumbs bakery"
DELIVERY_FEE = 200
FREE_DELIVERY_LIMIT = 3000
CLOUD_PRICE_PER_1K_TOKENS = 0.10

CUPCAKE_PRICE = 250
BROWNIE_PRICE = 300
CHOCOLATE_CAKE_PRICE = 1500
BULK_DISCOUNT_RATE = 0.10
FREE_DELIVERY_TOKENS = 0

message_count = 0
rules_answered = 0
unanswered_count = 0
quote_count = 0
total_quoted_value = 0
total_ai_cost = 0.0

print("=" * 50)
print(f"   {BUSINESS_NAME.title()} Desk: rules, quotes and AI prompts")
print("=" * 50)
print("Ask anything, type /quote for a price, or bye to exit.")

customer_name = input(f"{BOT_NAME}: What is your name? ").strip().title()

while True:
        
      question = input(f"{customer_name}: ").strip().lower()

      if question == "":
        print(f"{BOT_NAME}: Please type a question.")
        continue

      message_count += 1

    # Complaints come first so unhappy customers reach a human.
      if ("refund" in question or "complaint" in question
            or "late" in question):
        print(f"{BOT_NAME}: Sorry about that. A manager will contact you.")
        rules_answered += 1

      elif question == "bye" or question == "goodbye":
        print(f"{BOT_NAME}: Goodbye, {customer_name}!")
        break

    # Exact greeting checks avoid matching words inside other questions.
      elif (question == "hi" or question.startswith("hi ")
          or question == "hello" or question.startswith("hello ")
          or question == "salam" or question.startswith("salam ")):
        print(f"{BOT_NAME}: Welcome to Sweet Crumbs!")
        rules_answered += 1

      elif "hours" in question or "timing" in question or "open" in question:
        print(f"{BOT_NAME}: We are open 9 am to 10 pm every day.")
        rules_answered += 1

      elif "location" in question or "where" in question:
        print(f"{BOT_NAME}: We are in Lahore. Contact the shop for our exact address.")
        rules_answered += 1

      elif "delivery" in question or "deliver" in question:
        print(f"{BOT_NAME}: Delivery costs 200 PKR. Orders of 3,000 PKR or more after discount get free delivery.")
        rules_answered += 1

      elif ("menu" in question or "items" in question
          or "cupcake" in question or "brownie" in question
          or "cake" in question):
        print(f"{BOT_NAME}: Cupcake: 250 PKR, brownie: 300 PKR, chocolate cake: 1,500 PKR.")
        rules_answered += 1

      elif question == "/quote":
        item = input(f"{BOT_NAME}: Which item? ").strip().lower()

        if item == "":
            print(f"{BOT_NAME}: Please enter an item next time.")
            continue

        quantity_text = input(f"{BOT_NAME}: How many? ").strip()

try:
       quantity = int(quantity_text)
except ValueError:
         print(f"{BOT_NAME}: Please enter a whole number for quantity.")
         

if quantity <= 0:
            print(f"{BOT_NAME}: Quantity must be greater than zero.")
           

if item == "cupcake" or item == "cupcakes":
            unit_price = CUPCAKE_PRICE
elif item == "brownie" or item == "brownies":
            unit_price = BROWNIE_PRICE
elif item == "chocolate cake" or item == "chocolate cakes":
            unit_price = CHOCOLATE_CAKE_PRICE
else:
            print(f"{BOT_NAME}: Sorry, {item} is not on our menu.")
    
subtotal = unit_price * quantity
discount = 0

        # Bulk orders receive a discount before delivery is calculated.
if quantity >= 10:
            discount = subtotal * BULK_DISCOUNT_RATE

discounted_subtotal = subtotal - discount

if discounted_subtotal >= FREE_DELIVERY_LIMIT:
            delivery = 0
else:
            delivery = DELIVERY_FEE

            total = discounted_subtotal + delivery

            print(f"{BOT_NAME}: {quantity:,} x {item} = {subtotal:,.0f} PKR")
            print(f"     Discount: -{discount:,.0f} PKR | Delivery: {delivery:,.0f} PKR")
            print(f"     Total: {total:,.0f} PKR")

            quote_count += 1
            rules_answered += 1
            total_quoted_value += total
         else:
        # Keep the prompt short to limit token use and protect privacy.
        clean_question = question.capitalize()[:150]
        estimated_tokens = round(len(clean_question) / 4)

        if ("phone" in question or "cnic" in question
                or "address" in question):
            chosen_model = "llama3.2 (local, private)"
            estimated_cost = 0.0
        else:
            chosen_model = "small cloud model (cheap)"
            estimated_cost = (
                estimated_tokens / 1000
            ) * CLOUD_PRICE_PER_1K_TOKENS

        total_ai_cost += estimated_cost
        unanswered_count += 1

        print(f"{BOT_NAME}: Good question! Routed to: {chosen_model} "
              f"(~{estimated_tokens} tokens)")
        print(f"""     Prompt: You are the assistant of {BUSINESS_NAME}.
     Answer {customer_name} in 2 short lines.
     Do not invent prices, timings, or promises.
     Question: {clean_question}""")

print("=" * 50)
print("Session report")
print(f"Messages: {message_count} | Answered by rules: {rules_answered} | Unanswered: {unanswered_count}")
print(f"Quotes: {quote_count} | Quoted value: {total_quoted_value:,.0f} PKR")
print(f"Estimated AI cost for unanswered questions: {total_ai_cost:.4f} PKR")
print("=" * 50)
 