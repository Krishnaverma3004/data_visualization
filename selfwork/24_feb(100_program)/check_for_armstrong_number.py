# Program to check if a number is Armstrong

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

# Step 2: Count digits
temp = num
digits = 0
if temp == 0:
    digits = 1
else:
    while temp > 0:
        temp //= 10
        digits += 1

# Step 3: Calculate Armstrong sum
sum_arm = 0
temp = num
while temp > 0:
    digit = temp % 10
    power = 1
    for _ in range(digits):
        power *= digit
    sum_arm += power
    temp //= 10

# Step 4: Check if Armstrong
if sum_arm == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")

'''output
 Enter a positive integer: 34
34 is not an Armstrong number

output2:
Enter a positive integer: ab23
Enter numeric value only.
Enter a positive integer: 100
100 is not an Armstrong number
'''