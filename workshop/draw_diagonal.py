n = int(input("Add a number and i will write u a big N depending on how big like it: "))
for i in range(1, n + 1):
    if i == 1 or i == int(n):
        print("%" * n)
    else:
        print("%" + " " * (i - 2) + "%" + " " * (n - i - 1) + "%") 