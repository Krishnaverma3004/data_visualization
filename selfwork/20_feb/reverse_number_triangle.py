rows = int(input("Enter rows: "))

for i in range(1, rows + 1):
    for j in range(i, 0, -1):
        print(j, end="")
    print()


'''output:
Enter rows: 6
1
21
321
4321
54321
654321'''