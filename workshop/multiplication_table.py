# Create a program that asks for a number and prints the multiplication table with that number

base_to_multiply = int(input("Enter a number and this program will provide you its multiplication table: "))
for i in range(1, 11):
    print (base_to_multiply, "*", i, "=", base_to_multiply * i)
