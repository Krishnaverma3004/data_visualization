# Program to print numbers from 1 to N using while loop

# Function to check if input is numeric
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

# Step 2: Print numbers from 1 to N using while loop
i = 1
while i <= N:
    print(i, end=' ')
    i += 1
print()  # For newline

'''output:
Enter N: abc
Enter numeric value only.
Enter N: 23
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 '''