# Program to print right-angled triangle star pattern

def is_numeric_manual(s):
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    return len(s) > 0

# Step 1: Input number of rows
while True:
    n_str = input("Enter number of rows: ")
    if is_numeric_manual(n_str):
        rows = int(n_str)
        if rows > 0:
            break
        else:
            print("Number must be positive.")
    else:
        print("Enter numeric value only.")

# Step 2: Print pattern
for i in range(1, rows + 1):
    for j in range(i):
        print("*", end='')
    print()  # New line after each row

'''Output
Enter number of rows: 6
*
**
***
****
*****
******'''    