first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
if second_number <= first_number:
    print("The second number should be bigger")
else:
    while first_number < second_number:
        print(first_number)
        first_number += 1