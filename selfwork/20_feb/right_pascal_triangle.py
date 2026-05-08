rows = int(input("Enter rows: "))

for i in range(1, rows + 1):
    print("*" * i)

for i in range(rows - 1, 0, -1):
    print("*" * i)

'''output:
Enter rows: 7
*
**
***
****
*****
******
*******
******
*****
****
***
**
*
'''