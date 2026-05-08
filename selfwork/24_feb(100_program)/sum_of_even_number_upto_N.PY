# Program to find sum of even numbers up to N

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

# Step 2: Sum even numbers
sum_even = 0
i = 2
while i <= N:
    sum_even += i
    i += 2  # Only even numbers

print("Sum of even numbers up to", N, "is:", sum_even)
'''OUTPUT
Enter N: 345
Sum of even numbers up to 345 is: 29756

OUTPUT2:
Enter N: ABC
Enter numeric value only.
Enter N: 4
Sum of even numbers up to 4 is: 6'''