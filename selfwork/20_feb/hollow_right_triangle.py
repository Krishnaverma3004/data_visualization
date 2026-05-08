rows = int(input("Enter rows: "))

for i in range(1, rows + 1):
    if i == 1 or i == rows:
        print("*" * i)
    else:
        print("*" + " " * (i - 2) + "*")

'''output:
Enter rows: 6
*
**
* *
*  *
*   *
******'''