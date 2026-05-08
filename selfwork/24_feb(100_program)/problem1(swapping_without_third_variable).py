# Read first input
a = input("Enter first number ")
#validation of first number

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
    # Read second input
    b = input("Enter second number")
    #validation of second number
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
        a = int(a)
        b = int(b)

        # Swap without third variable
        a = a + b
        b = a - b
        a = a - b

        print(a)
        print(b)
'''output
Enter first number 54
Enter second number44
44
54

output 2:
Enter first number abc
Invalid Input'''
