# Problem 9: Find sum of digits of a number
num = input("Enter an integer to calculate sum of digits: ")

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
    # Step 2: Convert  and calculate sum
    total = 0
    if num[0] == '-':
        num = num[1:]
    for ch in num:
        digit = ord(ch) - ord('0')
        total = total + digit
    print ("the sum of digits are :")    
    print(total)
'''outpu1:
Enter an integer to calculate sum of digits: 34556
the sum of digits are :
23

output2:
Enter an integer to calculate sum of digits: abc
Invalid Input
'''
