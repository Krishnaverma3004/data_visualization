# Reverse a list manually with index-based input
lst = []
print("Enter numbers for the list. Type '0' to stop:")

while True:
    s = input("Number: ")
    # Validate: must be integer
    valid = True
    for ch in s:
        if ch < '0' or ch > '9':
            valid = False
    if not valid:
        print("Invalid! Enter a number only.")
        continue

    n = int(s)
    if n == 0 and len(lst) > 0:
        break
    elif n == 0 and len(lst) == 0:
        print("List cannot be empty.")
        continue
    lst.append(n)

# Reverse list manually
rev = []
i = len(lst)-1
while i >= 0:
    rev += [lst[i]]  # append manually without functions
    i -= 1

print("Reversed List:", rev)

'''output
Enter numbers for the list. Type '0' to stop:
Number: e
Invalid! Enter a number only.
Number: 2
Number: 3
Number: 2
Number: 3.3
Invalid! Enter a number only.
Number: 34
Number: 4
Number: 0
Reversed List: [4, 34, 2, 3, 2]
'''