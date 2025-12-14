import random
import time


def chatbot():
    greetings = ["Hello there! 🫱", "Hi friend! 😊",
                 "Hey! Nice to meet you! 🎉", "Howdy! 😀"]

    farewells = ["Goodbye! 🫲", "See you later! 🚀",
                 "Bye bye! 😉", "See you next time! 🤩"]

    jokes = ["Why do programmers prefer dark mode? Because light attracts bugs.",
             "I would tell you a Python joke, but it might take too long to compile.",
             "There are 10 kinds of people in the world: those who understand binary and those who don’t.",
             "My code works… I have no idea why."]
    facts = [
        "Python was created by Guido van Rossum and released in 1991.",
        "The name Python comes from Monty Python, not the snake.",
        "The first computer bug was an actual moth found in a computer in 1947.",
        "The world’s first programmer was Ada Lovelace."
    ]

    bot_name = "Chatbot"
    print(f"🤖 {bot_name} is starting up...")
    time.sleep(1)

    print(f"""
       🤖 Welcome to {bot_name}! 🤖

       I can chat about:
       'joke' - Hear a funny joke
       'fact' - Learn something new
       'color' - My favorite color
       'bye' - Endour chat
""")

    chatting = True

    user_name = input("What's your name: ").lower()
    print(f" {bot_name}: Nice to meet you, {user_name}! How can I help you today?")

    while chatting:
        user_input = input("😀 You: ").strip()

        if user_input in ["hi", "hello", "hey", "howdy"]:
            print(f"🤖 {bot_name}: {random.choice(greetings)}")

        elif "joke" in user_input:
            print(f"🤖 {bot_name}: {random.choice(jokes)}")

        elif "fact" in user_input:
            print(f"🤖 {bot_name}: {random.choice(facts)}")

        elif "color" in user_input:
            print(f"🤖 {bot_name}: My favorite color is robot blue! 🔵 What's yours?")
            color = input("😊 You: ").strip()
            print(f"🤖 {bot_name}: {color} is a great color!")

        elif user_input in ["bye", "goodbye", "exit", "quit"]:
            print(f"🤖 {bot_name}: {random.choice(farewells)}")
            print(f"🤖 {bot_name}: It was fun chatting with you, {user_name}")
            chatting = False

        else:
            response = ["That's interesting! Tell me more.",
                        "I'm not sure I understand. Can you try again?",
                        "Hmm, let's talk about something else.Try asking for a joke or fact!",
                        "Beep boop! My robot brain is processing that ... 🤔"]
            print(f"🤖 {bot_name}: {random.choice(response)}")

    print("Thanks for chatting! Run the program again to talk to me later!")


chatbot()
