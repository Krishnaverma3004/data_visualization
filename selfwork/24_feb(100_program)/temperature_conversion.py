# enter temperature in Celsius
C = input("Enter temperature in Celsius: ")  


valid = True
i = 0
dot_count = 0  # Track number of decimal points

if len(C) == 0:
    valid = False
else:
    if C[0] == '-':
        if len(C) == 1:  # "-" alone is invalid
            valid = False
        i = 1
    while i < len(C):
        if C[i] == '.':
            dot_count += 1
            if dot_count > 1:  # More than one dot is invalid
                valid = False
                break
        elif C[i] < '0' or C[i] > '9':
            valid = False
            break
        i += 1

if not valid:
    print("Invalid Input")
else:
    C = float(C)
    if C < -273.15: 
        print("Invalid Input")
    else:
        F = (C * 9/5) + 32
        print ("Temperature in Fereheit is:")
        print(round(F, 2))  # Rounded to 2 decimal places

'''output
Enter temperature in Celsius: abc
Invalid Input

output 2:
Enter temperature in Celsius: 78
Temperature in Fereheit is:
172.4
'''        