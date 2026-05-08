# Read Principal
P = input("Enter principal amount (in Rs)")
valid = True
i = 0
if len(P) == 0:
    valid = False
else:
    if P[0] == '-':
        if len(P) == 1:
            valid = False
        i = 1
    while i < len(P):
        if (P[i] < '0' or P[i] > '9') and P[i] != '.':
            valid = False
            break
        i += 1

if not valid:
    print("Invalid Input")
else:
    # Read Rate
    R = input("Enter rate (in %)")
    valid = True
    i = 0
    if len(R) == 0:
        valid = False
    else:
        if R[0] == '-':
            if len(R) == 1:
                valid = False
            i = 1
        while i < len(R):
            if (R[i] < '0' or R[i] > '9') and R[i] != '.':
                valid = False
                break
            i += 1

    if not valid:
        print("Invalid Input")
    else:
        # Read Time
        T = input("Enter time (in years)")
        valid = True
        i = 0
        if len(T) == 0:
            valid = False
        else:
            if T[0] == '-':
                if len(T) == 1:
                    valid = False
                i = 1
            while i < len(T):
                if (T[i] < '0' or T[i] > '9') and T[i] != '.':
                    valid = False
                    break
                i += 1

        if not valid:
            print("Invalid Input")
        else:
            P = float(P)
            R = float(R)
            T = float(T)
            if P < 0 or R < 0 or T < 0:
                print("Invalid Input")
            else:
                CI = P * (1 + R/100)**T - P
                print(CI)

'''output
Enter principal amount (in Rs)3400000
Enter rate (in %)5
Enter time (in years)2
348500.0

output 2:
Enter principal amount (in Rs)abc
Invalid Input
'''                