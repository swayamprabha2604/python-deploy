import random

# Dictionary of responses based on user queries
responses = {
    "flight_delayed": ["I'm sorry to hear that. Could you please provide your flight details?", 
                       "Let me assist you. Can you share your flight number and departure time?"],
    "lost_luggage": ["I understand your concern. Please provide your baggage claim ticket number.",
                     "Let's solve this. Can you share your baggage claim ticket number?"],
    "booking_issue": ["I apologize for the inconvenience. Could you please provide your booking reference?",
                      "I'm here to help. Can you share your booking reference?"],
    "general_issue": ["I'm here to assist you. Please provide more details about your issue.",
                      "Let me know how I can help you."],
    "fare_inquiry": ["Sure, I can help with that. Please provide your departure and destination cities.",
                     "I can assist you with fare information. What are your departure and destination cities?"],
    "flight_status": ["To check your flight status, please provide your flight number and departure date.",
                      "Sure, I can help with that. What is your flight number and departure date?"],
    "cancel_booking": ["To cancel your booking, please provide your booking reference.",
                       "To proceed with the cancellation, I'll need your booking reference."]
}

# Function to classify user input and generate a response
def get_response(user_input):
    if "delayed" in user_input:
        return random.choice(responses["flight_delayed"])
    elif "lost" in user_input and "luggage" in user_input:
        return random.choice(responses["lost_luggage"])
    elif "booking" in user_input or "reservation" in user_input:
        return random.choice(responses["booking_issue"])
    elif "fare" in user_input or "price" in user_input:
        return random.choice(responses["fare_inquiry"])
    elif "status" in user_input or "schedule" in user_input:
        return random.choice(responses["flight_status"])
    elif "cancel" in user_input or "refund" in user_input:
        return random.choice(responses["cancel_booking"])
    else:
        return random.choice(responses["general_issue"])

# Main loop for the chatbot
print("Welcome to the Airline Help Desk! How can I assist you today?")
while True:
    user_input = input("You: ").lower()
    if user_input == 'quit':
        print("Thank you for using the Airline Help Desk. Goodbye!")
        break
    response = get_response(user_input)
    print("Bot:", response)

