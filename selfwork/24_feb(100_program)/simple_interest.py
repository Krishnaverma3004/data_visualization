# Read Principal amount
P = input("Enter the principal amount(in Rs)")

# Step 1: Validate the first input
valid = True
i = 0

if len(P) == 0:
    valid = False
else:
    # Check for optional leading negative sign
    if P[0] == '-':
        if len(P) == 1:  # "-" alone is invalid
            valid = False
        i = 1
    # Check each character to be a digit or '.'
    while i < len(P):
        if (P[i] < '0' or P[i] > '9') and P[i] != '.':
            valid = False
            break
        i += 1

# If first input invalid, print error
if not valid:
    print("Invalid Input")
else:
    # Read Rate of Interest
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

    # If second input invalid, print error
    if not valid:
        print("Invalid Input")
    else:
        # Read Time period
        T = input("Enter time (in year)")
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

        # If third input invalid, print error
        if not valid:
            print("Invalid Input")
        else:
            # Convert inputs to float
            P = float(P)
            R = float(R)
            T = float(T)

            # Check for negative values
            if P < 0 or R < 0 or T < 0:
                print("Invalid Input")
            else:
                # Calculate Simple Interest
                SI = (P * R * T) / 100
                print(SI)

'''output
 Enter the principal amount(in Rs)340000
Enter rate (in %)5
Enter time (in year)4
68000.0

output 2
Enter the principal amount(in Rs)500000
Enter rate (in %)5
Enter time (in year)ab
Invalid Input'''               