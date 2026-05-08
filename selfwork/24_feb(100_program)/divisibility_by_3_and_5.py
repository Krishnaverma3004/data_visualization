# Problem 15: Check if number is divisible by both 3 and 5
num = input("Enter an integer: ")

# Step 1: Validate input manually
valid = True
i = 0
if len(num) == 0:
    valid = False
else:
    if num[0] == '-':
        if len(num) == 1:
            valid = False
        i = 1
    while i < len(num):
        if num[i] < '0' or num[i] > '9':
            valid = False
            break
        i += 1

if not valid:
    print("Invalid Input")
else:
    # Step 2: Convert to integer
    n = 0
    negative = False
    if num[0] == '-':
        negative = True
        num = num[1:]
    for ch in num:
        n = n * 10 + (ord(ch) - ord('0'))
    if negative:
        n = -n

    # Step 3: Check divisibility by 3 and 5
    temp = n
    if temp < 0:
        temp = -temp

    # Check divisible by 3
    sum3 = 0
    t = temp
    while t > 0:
        sum3 += t - (t // 10) * 10
        t = t // 10
    divisible_by_3 = False
    if sum3 % 3 == 0:
        divisible_by_3 = True

    # Check divisible by 5
    last_digit = temp - (temp // 10) * 10
    divisible_by_5 = False
    if last_digit == 0 or last_digit == 5:
        divisible_by_5 = True

    if divisible_by_3 and divisible_by_5:
        print("Divisible by both 3 and 5")
    else:
        print("Not divisible by both 3 and 5")
'''output1:
Enter an integer: 45
Divisible by both 3 and 5
output 2
Enter an integer: 3
Not divisible by both 3 and 5
output3:
Enter an integer: abxc
Invalid Input
'''        
