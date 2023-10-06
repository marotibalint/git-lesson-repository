rows = int(input("Add a number and I will create a chess table :" ))
for i in range(0, rows):
    if i % 2 == 0:
        print("% " * rows)
    else:
        print(" %" * rows)