def simple_chatbot():
    print("Welcome to the Simple Chatbot!")
    print("You can start chatting. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        # Check user input and respond accordingly
        if user_input == 'hello':
            print("Chatbot: Hi there!")
        elif user_input == 'how are you?':
            print("Chatbot: I'm good, thank you!")
        elif user_input == 'bye':
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I didn't understand that.")

if __name__ == "__main__":
    simple_chatbot()
