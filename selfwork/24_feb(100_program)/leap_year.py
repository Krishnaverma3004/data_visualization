# Problem 11: Check whether a given year is a leap year
year = input("Enter a year: ")

# Step 1: Validate input (must be digits only)
valid = True
i = 0
if len(year) == 0:
    valid = False
else:
    while i < len(year):
        if year[i] < '0' or year[i] > '9':
            valid = False
            break
        i += 1

if not valid:
    print("Invalid Input")
else:
    # Step 2: Convert  to integer
    y = 0
    for ch in year:
        y = y * 10 + (ord(ch) - ord('0'))

    # Step 3: Check leap year rules 
    if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
        print("Leap Year")
    else:
        print("Not a Leap Year")

'''output:
Enter a year: 65564
Leap Year


output2:
Enter a year: abc
Invalid Input

output3:
Enter a year: 2023
Not a Leap Year
'''        