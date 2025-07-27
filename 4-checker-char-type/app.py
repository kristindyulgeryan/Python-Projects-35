print("✍🏻 CHARACTER TYPE CHECKER ✍🏻")
char = input("ENter a single character: ")

if char.isalpha():
    print("This is a letter")
elif char.isdigit():
    print("This is a digit")
else:
    print("This is a special character")
