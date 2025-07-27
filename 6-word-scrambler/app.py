import random


print("🔤 WORD SCRAMBLER 🔤")


while True:
    word = input("\nEnter a word to scramble (or 'quit'):")
    if word.lower() == "quit":
        print("👋🏼 Goodbye!")
        break

# "everyone" => ["e","v","e","r","y","o","n","e"]
# shuffle => ["v","e","y","r","e","o","n","e"] => join => veyreone

    letters = list(word)
    random.shuffle(letters)
    print(f"Scrambled: {''.join(letters)}")
