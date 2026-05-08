# Read first number
a = input("Enter first number :")

# Validate first number
valid = True
i = 0
if len(a) == 0:
    valid = False
else:
    if a[0] == '-':
        if len(a) == 1:
            valid = False
        i = 1
    while i < len(a):
        if a[i] < '0' or a[i] > '9':
            valid = False
            break
        i += 1

if not valid:
    print("Invalid Input")
else:
    # First number valid, read second number
    b = input("Enter second number :")
    valid = True
    i = 0
    if len(b) == 0:
        valid = False
    else:
        if b[0] == '-':
            if len(b) == 1:
                valid = False
            i = 1
        while i < len(b):
            if b[i] < '0' or b[i] > '9':
                valid = False
                break
            i += 1

    if not valid:
        print("Invalid Input")
    else:
        # Second number valid, read third number
        c = input("Enter third number :")
        valid = True
        i = 0
        if len(c) == 0:
            valid = False
        else:
            if c[0] == '-':
                if len(c) == 1:
                    valid = False
                i = 1
            while i < len(c):
                if c[i] < '0' or c[i] > '9':
                    valid = False
                    break
                i += 1

        if not valid:
            print("Invalid Input")
        else:
            # All numbers valid
            a = int(a)
            b = int(b)
            c = int(c)

            largest = a
            if b > largest:
                largest = b
            if c > largest:
                largest = c

            print(largest)

'''output
Enter first number :45
Enter second number :33
Enter third number :5
45

output 2
Enter first number :67
Enter second number :34
Enter third number :q
Invalid Input
'''           