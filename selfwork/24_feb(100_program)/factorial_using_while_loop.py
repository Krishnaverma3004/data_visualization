# Program to find factorial of a number using while loop

def is_numeric_manual(s):
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    return len(s) > 0

# Step 1: Input number
while True:
    n_str = input("Enter a non-negative integer: ")
    if is_numeric_manual(n_str):
        n = int(n_str)
        if n >= 0:
            break
        else:
            print("Number must be non-negative.")
    else:
        print("Enter numeric value only.")

# Step 2: Calculate factorial
factorial = 1
i = 1
while i <= n:
    factorial *= i
    i += 1

print("Factorial:", factorial)

'''output:
Enter a non-negative integer: 2
Factorial: 2

output2:
Enter a non-negative integer: abc
Enter numeric value only.
Enter a non-negative integer: 5
Factorial: 120
'''