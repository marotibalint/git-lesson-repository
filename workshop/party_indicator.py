# Write a program that asks for two numbers
# The first number represents the number of girls that comes to a party, the
# second represents the number of boys
#
# If the the number of girls and boys are equal and 20 or more people are coming to the party
# it should print: The party is excellent!
#
# If there are 20 or more people coming to the party but the girl - boy ratio is not 1-1
# it should print: Quite a cool party!
#
# If there are less people coming than 20
# it should print: Average party...
#
# If no girls are coming, regardless the count of the people
# it should print: Sausage party

boys_number = int(input("Enter the number of boys at the party: "))
girls_number = int(input("Enter the number of gurls at the party: "))
together = boys_number + girls_number
if boys_number == girls_number and together >= 20:
    print("The party is excellent!")

elif together >= 20 and boys_number < girls_number:
    print("Quite a cool party!")

elif together < 20:
    print("Average party...")
else:
    print("Sausage party")