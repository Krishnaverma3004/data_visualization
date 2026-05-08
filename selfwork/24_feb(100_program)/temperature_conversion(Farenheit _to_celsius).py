# Problem 7: Convert Fahrenheit to Celsius
# User instruction: Enter a temperature in Fahrenheit (e.g., 98, -40, 32.5)
F = input("Enter temperature in Fahrenheit: ")

# Step 1: Validate input manually
valid = True
i = 0
dot_counted = False  # We will track decimal manually using simple variable

if len(F) == 0:
    valid = False
else:
    # Check for negative sign
    if F[0] == '-':
        if len(F) == 1:
            valid = False
        i = 1
    # Check each character manually
    while i < len(F):
        ch = F[i]
        if ch == '.':
            # Only allow a single decimal manually
            if dot_counted:
                valid = False
                break
            dot_counted = True
        elif ch < '0' or ch > '9':
            valid = False
            break
        i += 1

if not valid:
    print("Invalid Input")
else:
    # Step 2: Convert manually to float
    num = 0  # Integer part and decimal part
    decimal = 0  # Flag: 0 = integer, 1 = decimal
    decimal_div = 10  # Divisor for decimal digits
    negative = False

    # Remove negative sign for easier processing
    if F[0] == '-':
        negative = True
        F = F[1:]

    for ch in F:
        if ch == '.':
            decimal = 1
            continue
        digit = ord(ch) - ord('0')
        if decimal == 0:
            num = num * 10 + digit
        else:
            num = num + digit / decimal_div
            decimal_div *= 10

    if negative:
        num = -num

    # Step 3: Absolute zero check
    if num < -459.67:
        print("Invalid Input")
    else:
        # Step 4: Convert Fahrenheit to Celsius
        C = (num - 32) * 5 / 9

        # Step 5: 
        C = int(C * 100 + 0.5) / 100

        # Step 6: Print result
        print ("temperatur in celsius is :")
        print(C)
'''Output
 Enter temperature in Fahrenheit: 223
temperatur in celsius is :
106.11

output 2:
Enter temperature in Fahrenheit: abc
Invalid Input
'''       