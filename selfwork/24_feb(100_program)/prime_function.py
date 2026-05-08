# Program to check if a number is prime using a function

def is_numeric_manual(s):
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    return len(s) > 0

# Function to check prime
def is_prime(num):
    if num <= 1:
        return False
    i = 2
    while i*i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

# Input number
while True:
    n_str = input("Enter a positive integer: ")
    if is_numeric_manual(n_str):
        n = int(n_str)
        if n > 0:
            break
        else:
            print("Number must be positive.")
    else:
        print("Enter valid value only.")

if is_prime(n):
    print(n, "is prime")
else:
    print(n, "is not prime")
    
'''output:
Enter a positive integer: -90
Enter valid value only.
Enter a positive integer: abc
Enter valid value only.
Enter a positive integer: 67
67 is prime'''    