# Merge two lists manually with proper validation, stop with 'n'
lst1, lst2 = [], []

# Input first list
print("Enter numbers for first list (type 'n' to stop):")
while True:
    s = input("Number: ")
    # Stop signal first
    if s.lower() == "n":
        if len(lst1) == 0:
            print("List cannot be empty. Enter at least one number.")
            continue
        break
    # Validate number (allow negative)
    valid = True
    start = 0
    if s[0] == '-':
        start = 1
    for i in range(start, len(s)):
        if s[i] < '0' or s[i] > '9':
            valid = False
    if not valid or s == "-":
        print("Invalid input! Enter a valid number.")
        continue
    lst1.append(int(s))

# Input second list
print("Enter numbers for second list (type 'n' to stop):")
while True:
    s = input("Number: ")
    if s.lower() == "n":
        if len(lst2) == 0:
            print("List cannot be empty. Enter at least one number.")
            continue
        break
    # Validate number
    valid = True
    start = 0
    if s[0] == '-':
        start = 1
    for i in range(start, len(s)):
        if s[i] < '0' or s[i] > '9':
            valid = False
    if not valid or s == "-":
        print("Invalid input! Enter a valid number.")
        continue
    lst2.append(int(s))

# Merge and remove duplicates manually
merged = []
for x in lst1 + lst2:
    add = True
    for y in merged:
        if y == x:
            add = False
            break
    if add:
        merged.append(x)

print("Merged unique list:", merged)