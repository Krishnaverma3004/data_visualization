rows = int(input("Enter rows: "))

for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * (2 * i - 1))

    
'''output:
Enter rows: 6
***********
 *********
  *******
   *****
    ***
     *
     '''