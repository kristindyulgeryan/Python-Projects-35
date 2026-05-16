import time
import os
import platform


def clear_screen():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")


def format_time(seconds):
    # format(30)=>00:30
    minutues = seconds // 60
    seconds_remainder = seconds % 60
    return (f"{minutues:02d}:{seconds_remainder:02d}")


def countdown(seconds, label):
    for remaining in range(seconds, 0, -1):
        clear_screen()
        print(f"\n {label}")
        print(f"\nTime remaining: {format_time(remaining)}")

        if label == "Work Session":
            print("Focus on your task!")
        elif "Break" in label:
            print("Take a breath...")

        time.sleep(1)

    clear_screen()
    print(f"\n {label} completed!")

    if platform.system() == "Windows":
        import winsound
        # hertz, duration
        winsound.Beep(1000, 500)


def pomodoro_timer():
    try:

        clear_screen()
        print("\n==== Pomodoro Timer ====")

        # default settings
        work_minutes = 25
        short_break_minutes = 5
        long_break_minutes = 15
        cycles = 4

        customize = input(
            "\n Use default settings (25min work, 5min short break, 15min long break?) (yes/no):").lower()

        if customize.startswith("n"):
            try:
                work_minutes = int(
                    input("\nEnter work session length (minutes): "))
                short_break_minutes = int(
                    input("Enter short break length (minutes): "))
                long_break_minutes = int(
                    input("Enter long break length (minutes): "))
                cycles = int(
                    input("Enter number of cycles before a long break: "))
            except ValueError:
                print("\nInvalid input! Using default settings")
                time.sleep(2)

        clear_screen()

        print(f"\nStarting Pomodoro Timer with:")
        print(f". {work_minutes} minute work sessions")
        print(f". {short_break_minutes} minute short sessions")
        print(f". {long_break_minutes} minute long sessions")
        print(f". Press Ctrl+C at any time to exit")
        input("\nPress Enter to begin...")

        # convert minutes to seconds
        work_seconds = work_minutes*60
        short_break_seconds = short_break_minutes*60
        long_break_seconds = long_break_minutes*60

        comleted_cycles = 0

        while True:
            countdown(work_seconds, "Work Session")
            completed_cycles += 1
            if comleted_cycles % cycles == 0:
                input("\nTime for a long break! Press Enter to start your break...")
                countdown(long_break_seconds, "Long Break")
                input(
                    "\nLong break complete! Press Enter to start the next work session...")
            else:
                input("\nTime for a short break! Press Enter to start your break...")
                countdown(short_break_seconds, "Short Break")
                input(
                    "\nShort break complete! Press Enter to start the next work session...")
    except KeyboardInterrupt:
        clear_screen()
        print("Goodbye!")


pomodoro_timer()
