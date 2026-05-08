# Program to calculate factorial using for loop

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

# Step 2: Compute factorial using for loop
factorial = 1
for i in range(1, n+1):
    factorial *= i

print("Factorial:", factorial)

'''output
Enter a non-negative integer: abc
Enter numeric value only.
Enter a non-negative integer: 3
Factorial: 6

output2:
Enter a non-negative integer: 34
Factorial: 295232799039604140847618609643520000000
'''