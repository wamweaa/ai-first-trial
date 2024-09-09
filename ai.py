def chatbot_response(user_input):
    user_input = user_input.lower()
    if 'hello' in user_input:
        return "hello! how can i assist you today?"
    elif 'how are you' in user_input:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif 'bye' in user_input:
        return "Goodbye! have a great day!"
    else:
        return "sorry,i don't understand that"

def start_chatbot():
    print("chatbot:hello! Type 'bye' to exit")

    while True:
        user_input = input('you: ')
        if user_input.lower() == 'bye':
            print("chatbot:Goodbye")
            break
        response = chatbot_response(user_input)
        print("chatbot:",response)

start_chatbot()