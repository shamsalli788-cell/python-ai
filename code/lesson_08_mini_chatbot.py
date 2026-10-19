

"""A simple customer helper bot for a local tuition centre."""

business_name = "Bright Future Tuition Centre"

# Design the intents first: keywords connect common questions to replies.
greeting_words = ["hi", "hello", "hey"]
course_words = ["course", "subjects", "teach", "classes"]
timing_words = ["timing", "time", "open", "schedule"]
fee_words = ["fee", "fees", "price", "cost"]
location_words = ["location", "address", "where"]
complaint_words = ["complaint", "problem", "issue", "late", "bad service"]

# Why: a name lets the bot make its replies more personal.
customer_name = input("City Bot: What is your name? ").strip().title()

message_count = 0
unanswered_count = 0
complaint_count = 0

print(
    f"{business_name} Bot: Hi, {customer_name}! "
    "Ask about courses, timings, fees or location. "
    "Type 'bye' to exit."
)

while True:
    message = input(f"{customer_name}: ").strip().lower()

    # Why: count each message so we can report activity at the end.
    if message == "bye":
        break

    message_count += 1

    # Why: complaints must be handled before ordinary questions.
    if any(word in message for word in complaint_words):
        complaint_count += 1
        print(
            f"{business_name} Bot: Sorry to hear that, {customer_name}. "
            "A staff member can help you with this issue."
        )

    elif message in greeting_words or message.startswith("hello"):
        print(f"{business_name} Bot: Hello, {customer_name}! How can I help?")

    elif any(word in message for word in course_words):
        print(
            f"{business_name} Bot: We offer tuition in Mathematics, "
            "English, Science and Computer Studies."
        )

    elif any(word in message for word in timing_words):
        print(
            f"{business_name} Bot: Our example timings are "
            "3 pm to 7 pm, Monday to Saturday."
        )

    elif any(word in message for word in fee_words):
        print(
            f"{business_name} Bot: Fees depend on the course. "
            "Please contact the centre for the current fee."
        )

    elif any(word in message for word in location_words):
        print(
            f"{business_name} Bot: Please contact the centre "
            "for its exact address."
        )

    elif "agent" in message or "human" in message:
        print("Connecting you to a human...")
        break

    else:
        unanswered_count += 1

        # Why: this prompt can be sent to an AI model in Module 2.
        ai_prompt = (
            f"You are the friendly assistant of {business_name}. "
            f"Answer in 2 short lines: {message}"
        )

        print(
            f"{business_name} Bot: I don't know that answer yet. "
            f"In Module 2, an AI could answer: {ai_prompt}"
        )

print(f"Take care, {customer_name}!")
print("=" * 40)
print(
    f"Chat summary: {message_count} messages, "
    f"{unanswered_count} unanswered, {complaint_count} complaints."
)
