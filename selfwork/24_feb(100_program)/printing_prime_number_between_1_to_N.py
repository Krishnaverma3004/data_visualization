# Program to print all prime numbers from 1 to N

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
        if N >= 2:
            break
        else:
            print("N must be at least 2.")
    else:
        print("Enter numeric value only.")

# Step 2: Print primes
num = 2
while num <= N:
    # Check if num is prime
    divisor = 2
    is_prime = True
    while divisor * divisor <= num:
        if num % divisor == 0:
            is_prime = False
            break
        divisor += 1
    if is_prime:
        print(num, end=' ')
    num += 1
print()

'''output
Enter N: abc
Enter numeric value only.
Enter N: 3
2 3

output2:
Enter N: 45
2 3 5 7 11 13 17 19 23 29 31 37 41 43 
'''