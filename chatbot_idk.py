import random

def simple_chatbot():
    """A simple chatbot that might be self aware idk honestly"""

    knowledge = {
        "hello": [
            "Hello, how can I assist you?",
            "Hi, what's up?",
            "Hey, what is going on?"
        ],
        "how are you": [
            "I am just lines of code, but I'm doing good.",
            "Thank you for asking!",
            "I'm running okay."
        ],
        "what is your name": [
            "My creator never gave me a name...", #No I did I just never wrote it in the code lol
        ],
        "bye": [
            "Goodbye! Have a nice day.",
            "See ya!",
            "As my creator used to say: Buh-bye!"
        ],
        "what is 2+2": [
        "That is 4"
        ],
    }

    print("Chatbot: Hi! How can I assist you? Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in knowledge:
            response = random.choice(knowledge[user_input])
            print("Chatbot:", response)
#I know you guys have the attention span of a goldfish so I made sure you can leave
            if user_input == "bye":
                break
        else:
            print("Chatbot: Sorry, I don't understand that. My creator gave me limited knowledge for... some reason.")

if __name__ == "__main__":
    simple_chatbot()
#This chatbot is not chatgpt jr and It cannot do your homework stop using ai
#SUB TO IMAKECODE TOO