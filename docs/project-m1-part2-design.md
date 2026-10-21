
# Module 1 Checkpoint 2: AI Front Desk Design

## Business
Sweet Crumbs Bakery, Lahore

## Intents

| Intent | Keywords | Reply |
|---|---|---|
| Complaint | refund, complaint, late | Sorry about that. A manager will contact you. |
| Greeting | hello, hi, salam | Welcome to Sweet Crumbs! |
| Hours | hours, open, timing | We are open 9 am to 10 pm every day. |
| Location | location, address, where | We are in Lahore. Please contact the shop for the exact address. |
| Delivery | delivery, deliver, home | We provide delivery in Lahore. |
| Menu | menu, items, cupcakes, brownies, cakes | We sell cupcakes, brownies and chocolate cakes. |
| Goodbye | bye, goodbye | Goodbye! |

## Business Rules

| Rule | Value |
|---|---|
| Bot name | Sweet Crumbs Desk |
| Cupcake | 250 PKR each |
| Brownie | 300 PKR each |
| Chocolate cake | 1,500 PKR each |
| Bulk discount | 10% for 10 or more items |
| Delivery fee | 200 PKR |
| Free delivery | Discounted subtotal of 3,000 PKR or more |
| Private words | phone, cnic, address |
| Local model | llama3.2 |
| Cloud model example price | 0.10 PKR per 1,000 tokens (illustrative) |

## Rule Test Results

| You type | Expected | Pass? |
|---|---|---|
| WHAT are your hours | Hours reply | |
| which cake is best? | AI fallback | |
| my order is late | Manager reply | |
| /quote, quantity 1, most expensive item | Delivery charged | |
| /quote, large order above free-delivery limit | Free delivery | |
| /quote, quantity 10 or more | Discount applied | |
| /quote, unknown item | Not on our menu | |
| Can I change my phone number? | Local model, zero cost | |
| Press Enter without text | Asks again | |
| BYE | Goodbye and report | |
