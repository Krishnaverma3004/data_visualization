# Input tuple elements
tpl = []
print("Enter numbers for tuple (type 'n' to stop):")
while True:
    s = input("Number: ")
    if s.lower() == "n":
        if len(tpl) == 0:
            print("Tuple cannot be empty.")
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
        print("Invalid input!")
        continue
    tpl.append(int(s))

tpl = tuple(tpl)
print("Tuple:", tpl)

# Convert to list manually
lst = []
i = 0
while i < len(tpl):
    lst.append(tpl[i])
    i += 1

print("Converted list:", lst)
'''output
Enter numbers for tuple (type 'n' to stop):
Number: 45
Number: 45
Number: 33
Number: 2222
Number: n
Tuple: (45, 45, 33, 2222)
Converted list: [45, 45, 33, 2222]
'''