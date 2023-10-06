user_input_1 = input("Enter a number: ")
for i in range(1, int(user_input_1) + 1):
    print(" " * (int(user_input_1) - i) + "*" * (2 * i - 1))
