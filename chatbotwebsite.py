import random

# Define a dictionary of responses for the bot to choose from
responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you": ["I'm good, thanks for asking!", "I'm doing well, how about you?"],
    "what's your name": ["My name is Chatbot, nice to meet you!"],
    "bye": ["Goodbye!", "Bye! Take care!"],
    "default": ["Sorry, I don't understand. Can you please rephrase?", "I'm not sure what you mean."],
    "mits": ["Madhav Institute of Technology and Science, Gwalior."],
}

# Define a function to handle user input and generate bot responses
def respond(user_input):
    for key in responses:
        if key in user_input.lower():
            return random.choice(responses[key])
    return random.choice(responses["default"])

# Define a function to start the chatbot
def start_chatbot():
    print("Hello! I'm a chatbot. How can I assist you today?")
    while True:
        user_input = input("> ")
        if user_input.lower() == "exit":
            break
        bot_response = respond(user_input)
        print(bot_response)

# Call the start_chatbot function to begin the conversation
start_chatbot()
