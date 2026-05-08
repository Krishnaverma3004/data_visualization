# Program to find GCD of two numbers using Euclidean algorithm

# Function to check numeric input
def is_numeric_manual(s):
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    return len(s) > 0

# Step 1: Input first number
while True:
    a_str = input("Enter first number: ")
    if is_numeric_manual(a_str):
        a = int(a_str)
        break
    else:
        print("Enter numeric value only.")

# Step 2: Input second number
while True:
    b_str = input("Enter second number: ")
    if is_numeric_manual(b_str):
        b = int(b_str)
        break
    else:
        print("Enter numeric value only.")

# Step 3: Compute GCD using while loop
x, y = a, b
while y != 0:
    temp = y
    y = x % y
    x = temp

print("GCD of", a, "and", b, "is:", x)
'''output
Enter first number: 45
Enter second number: 33
GCD of 45 and 33 is: 3

output2:
Enter first number: abc
Enter numeric value only.
Enter first number: 3
Enter second number: 88
GCD of 3 and 88 is: 1'''
