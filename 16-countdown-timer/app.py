import time


print("\n=== ⏰ COUNTDOWN TIME ⏰ ===")
print("✨ Count down from your chosen seconds! ✨")


while True:
    try:
        seconds = int(input("\n Enter seconds to countdown from: "))

        if seconds <= 0:
            print("❌ Please enter a positive number.")
            continue

        print(f"⌛ Starting countdown from {seconds} seconds!")

        for i in range(seconds, 0, -1):
            print(f"{i} seconds remaining...")
            time.sleep(1)

        print("\n🎉 COUNTDOWN COMPLETE! 🎉")

        again = input("\n🔀 STart another countdown? (yes/no)").lower()
        if not again.startswith("y"):
            print("Goodbye! 👋🏼")
            break

    except ValueError:
        print("❌ Please enter a number.")
