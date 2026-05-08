# Problem 12: Assign grade based on marks
marks = input("Enter marks (0-100): ")

# Step 1: Validate input 
valid = True
i = 0
if len(marks) == 0:
    valid = False
else:
    while i < len(marks):
        if marks[i] < '0' or marks[i] > '9':
            valid = False
            break
        i += 1

if not valid:
    print("Invalid Input")
else:
    # Step 2: Convert to integer
    m = 0
    for ch in marks:
        m = m * 10 + (ord(ch) - ord('0'))

    # Step 3: Check valid range
    if m < 0 or m > 100:
        print("Invalid Input")
    else:
        # Step 4: Assign grade 
        if m >= 90:
            print("A")
        elif m >= 80:
            print("B")
        elif m >= 70:
            print("C")
        elif m >= 60:
            print("D")
        else:
            print("F")
'''output
Enter marks (0-100): 98
A

output2:
Enter marks (0-100): a
Invalid Input
'''            