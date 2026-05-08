rows = int(input("Enter rows: "))

for i in range(1, rows + 1):
    if i == 1 or i == rows:
        print("*" * rows)
    else:
        print("*" + " " * (rows - 2) + "*")

'''output:
Enter rows: 5
*****
*   *
*   *
*   *
*****'''