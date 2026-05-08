# Program to count digits in a number

def is_numeric_manual(s):
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    return len(s) > 0

# Step 1: Input number
while True:
    n_str = input("Enter a positive integer: ")
    if is_numeric_manual(n_str):
        num = int(n_str)
        if num >= 0:
            break
        else:
            print("Number must be non-negative.")
    else:
        print("Enter numeric value only.")

# Step 2: Count digits using while loop
count = 0
temp = num
if temp == 0:
    count = 1  # Special case: 0 has 1 digit
else:
    while temp > 0:
        temp //= 10
        count += 1

print("Number of digits:", count)
'''output
Enter a positive integer: 45
Number of digits: 2
output 2:
Enter a positive integer: abc12
Enter numeric value only.
Enter a positive integer: 12q
Enter numeric value only.
Enter a positive integer: 2334
Number of digits: 4
'''