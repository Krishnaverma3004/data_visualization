# Input tuple
tpl = []
print("Enter numbers for tuple (type 'n' to stop):")
while True:
    s = input("Number: ")
    if s.lower() == "n":
        if len(tpl) == 0:
            print("Tuple cannot be empty.")
            continue
        break
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

# Check uniqueness manually
unique = True
i = 0
while i < len(tpl):
    j = i + 1
    while j < len(tpl):
        if tpl[i] == tpl[j]:
            unique = False
            break
        j += 1
    if not unique:
        break
    i += 1

if unique:
    print("All elements are unique.")
else:
    print("Tuple contains duplicate elements.")
'''output
Enter numbers for tuple (type 'n' to stop):
Number: 45
Number: 33
Number: 33
Number: 23
Number: n
Tuple contains duplicate elements.
    '''