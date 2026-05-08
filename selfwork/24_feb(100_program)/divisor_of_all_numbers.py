# Program to print all divisors of a number

# Manual numeric input validation
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
        if num > 0:
            break
        else:
            print("Number must be positive.")
    else:
        print("Enter numeric value only.")

# Step 2: Print all divisors
i = 1
while i <= num:
    if num % i == 0:
        print(i, end=' ')
    i += 1
print()

'''output:
Enter a positive integer: ac
Enter numeric value only.
Enter a positive integer: 34
1 2 17 34

output:
Enter a positive integer: 34
1 2 17 34 
'''