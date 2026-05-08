rows = int(input("Enter rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end="")
    print()



'''output:
Enter rows: 8
12345678
1234567
123456
12345
1234
123
12
1'''