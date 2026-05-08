# Program to check whether a number lies within a given range

def is_numeric_manual(s):
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    return len(s) > 0

# Step 1: Input number
while True:
    num_str = input("Enter number: ")
    if is_numeric_manual(num_str):
        num = int(num_str)
        break
    else:
        print("Enter numeric value only.")

# Step 2: Input start of range
while True:
    start_str = input("Enter start of range: ")
    if is_numeric_manual(start_str):
        start = int(start_str)
        break
    else:
        print("Enter numeric value only.")

# Step 3: Input end of range
while True:
    end_str = input("Enter end of range: ")
    if is_numeric_manual(end_str):
        end = int(end_str)
        break
    else:
        print("Enter numeric value only.")

# Check if number is within range
if start <= num <= end:
    print("Number is within the range.")
else:
    print("Number is outside the range.")

'''output
Enter number: 34
Enter start of range: 23
Enter end of range: 338
Number is within the range.

'''    