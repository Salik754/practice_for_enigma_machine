def send_messages(messages, sent_messages):
    """Print each message and move it to sent_messages."""
    while messages:
        current_message = messages.pop(0) # Pop from front to maintain order
        print(f"Sending: {current_message}")
        sent_messages.append(current_message)

messages = ["Hello there!", "How are you?", "Lunch at 12?"]
sent_messages = []

send_messages(messages, sent_messages)

# Verification
print("\nFinal lists:")
print(f"Original messages: {messages}")
print(f"Sent messages: {sent_messages}")
