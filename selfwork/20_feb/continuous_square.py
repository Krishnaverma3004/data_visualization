rows = int(input("Enter rows: "))
num = 1

for i in range(rows):
    for j in range(rows):
        print(num, end=" ")
        num += 1
    print()

'''output:
Enter rows: 5
1 2 3 4 5
6 7 8 9 10
11 12 13 14 15
16 17 18 19 20
21 22 23 24 25
'''