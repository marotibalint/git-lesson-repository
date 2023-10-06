print("I will ask you for a number and then I will ask you to enter that many integers.")
print("I will then print the sum and average of the integers you entered.")

input_number = int(input("Enter a number: "))
sum = 0
for i in range(1, input_number + 1):
    sum += int(input("Enter an integer: "))
print("Sum: " + str(sum) + ", Average: " + str(sum / input_number))
