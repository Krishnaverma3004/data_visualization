# Program to calculate power 

def is_numeric_manual(s):
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    return len(s) > 0

# Input base
while True:
    base_str = input("Enter base (integer): ")
    if is_numeric_manual(base_str):
        base = int(base_str)
        break
    else:
        print("Enter numeric value only.")

# Input exponent
while True:
    exp_str = input("Enter exponent (non-negative integer): ")
    if is_numeric_manual(exp_str):
        exp = int(exp_str)
        if exp >= 0:
            break
        else:
            print("Exponent must be non-negative.")
    else:
        print("Enter numeric value only.")

# Calculate power manually
result = 1
i = 0
while i < exp:
    result *= base
    i += 1

print(base, "raised to", exp, "is:", result)
'''output
Enter base (integer): abc
Enter numeric value only.
Enter base (integer): 23
Enter exponent (non-negative integer): abc
Enter numeric value only.
Enter exponent (non-negative integer): 3
23 raised to 3 is: 12167'''
