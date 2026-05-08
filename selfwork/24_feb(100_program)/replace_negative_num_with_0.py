# Input list
lst = []
print("Enter numbers (negative or positive), type 'done' to stop:")
while True:
    s = input("Number: ")
    if s.lower() == "done":
        if len(lst) == 0:
            print("List cannot be empty.")
            continue
        break

    # Validate integer manually (allow negative)
    neg = False
    start = 0
    if s[0] == '-':
        neg = True
        start = 1
    valid = True
    for i in range(start, len(s)):
        if s[i] < '0' or s[i] > '9':
            valid = False
    if not valid or s == "-" or s == "":
        print("Invalid input!")
        continue
    n = int(s)
    lst += [n]

# Replace negatives manually
for i in range(len(lst)):
    if lst[i] < 0:
        lst[i] = 0

print("Updated list:", lst)

'''output
Enter numbers (negative or positive), type 'done' to stop:
Number: -44
Number: 33
Number: 2.3
Invalid input!
Number: abc
Invalid input!
Number: 0
Number: done
Updated list: [0, 33, 0]
'''