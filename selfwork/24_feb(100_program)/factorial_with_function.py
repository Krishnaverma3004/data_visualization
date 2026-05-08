# Program to find factorial using a function

def is_numeric_manual(s):
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    return len(s) > 0

def factorial(num):
    result = 1
    i = 1
    while i <= num:
        result *= i
        i += 1
    return result

# Input number
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

print("Factorial of", n, "is:", factorial(n))
'''output
Enter a non-negative integer: 23
Factorial of 23 is: 25852016738884976640000

output2:
Enter a non-negative integer: ABC
Enter numeric value only.
Enter a non-negative integer: 2
Factorial of 2 is: 2
'''