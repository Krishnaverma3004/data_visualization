# Problem 8: Check whether a number is even or odd without using modulus
num = input("Enter an integer to check Even/Odd: ")

# Step 1: Validate 
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
        ch = num[i]
        if ch < '0' or ch > '9':
            valid = False
            break
        i += 1

if not valid:
    print("Invalid Input")
else:
    # Step 2: Convert string to integer manually
    n = 0
    negative = False
    if num[0] == '-':
        negative = True
        num = num[1:]
    for ch in num:
        digit = ord(ch) - ord('0')
        n = n * 10 + digit
    if negative:
        n = -n

    # Step 3: Check even or odd using subtraction method
    temp = n
    if temp < 0:
        temp = -temp

    while temp >= 2:
        temp = temp - 2

    if temp == 0:
        print("Even")
    else:
        print("Odd")

'''output1:
Enter an integer to check Even/Odd: 45
Odd

output2
Enter an integer to check Even/Odd: 56
Even

output3:
Enter an integer to check Even/Odd: abc
Invalid Input
'''        