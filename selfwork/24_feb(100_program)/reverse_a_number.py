# Program to reverse a number using while loop

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
        if num >= 0:
            break
        else:
            print("Number must be non-negative.")
    else:
        print("Enter numeric value only.")

# Step 2: Reverse the number
rev = 0
temp = num
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

print("Reversed number:", rev)
'''output:
Enter a positive integer: abc
Enter numeric value only.
Enter a positive integer: 30099
Reversed number: 99003
'''