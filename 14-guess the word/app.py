import random

print("\n=== 🔤 GUESS THE WORD! 🔤 ===")

print("🎉 Unscramble the letters to find the word! 🎉")

words = ["python", "coding", "game", "computer", "fun", "learn"]

while True:
    original_word = random.choice(words)
    letters = list(original_word)
    random.shuffle(letters)
    scrambled = "".join(letters)

    print(f"\n Scrambled word: {scrambled}")

    guess = input("🤔 What's the word?:  ").lower()

    if guess == original_word:
        print("🎉 Congrats! You win!")
    else:
        print(f"☹️ Sorry, the word was: {original_word}")

    again = input("Play again? (y/n): ").lower()
    if not again.startswith("y"):
        print("GoodBye! 👋🏼")
        break
