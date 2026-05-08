rows = int(input("Enter rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="")
    print()


'''output:
Enter rows: 8
1
12
123
1234
12345
123456
1234567
12345678'''