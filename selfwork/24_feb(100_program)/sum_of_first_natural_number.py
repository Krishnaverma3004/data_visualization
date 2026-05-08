# Program to find sum of first N natural numbers

def is_numeric_manual(s):
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    return len(s) > 0

# Step 1: Input N
while True:
    n_str = input("Enter N: ")
    if is_numeric_manual(n_str):
        N = int(n_str)
        if N > 0:
            break
        else:
            print("N must be positive.")
    else:
        print("Enter numeric value only.")

# Step 2: Compute sum
sum_total = 0
i = 1
while i <= N:
    sum_total += i
    i += 1

print("Sum of first", N, "natural numbers is:", sum_total)
'''output
Enter N: 43
Sum of first 43 natural numbers is: 946

output:
Enter N: anc
Enter numeric value only.
Enter N: 99
Sum of first 99 natural numbers is: 4950'''
