#classifying number if it is positive, negative or zero
#taking input 
num = input("Enter a number")
# validating the number
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
    num = int(num)

    if num > 0:
        print("Positive")
    elif num < 0:
        print("Negative")
    else:
        print("Zero")


'''Output
Enter a number45
Positive


output 2
Enter a numberabc
Invalid Input

output 3
Enter a number-98
Negative
'''        

