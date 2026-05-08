# Input first set
set1 = []
print("Enter elements of first set (type 'n' to stop):")
while True:
    s = input("Element: ")
    if s.lower() == "n":
        if len(set1) == 0:
            print("Set cannot be empty.")
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
    set1.append(int(s))

# Input second set
set2 = []
print("Enter elements of second set (type 'n' to stop):")
while True:
    s = input("Element: ")
    if s.lower() == "n":
        if len(set2) == 0:
            print("Set cannot be empty.")
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
    set2.append(int(s))

# Union manually
union = []
for x in set1 + set2:
    add = True
    for y in union:
        if y == x:
            add = False
            break
    if add:
        union.append(x)

print("Union of sets:", union)
'''output
Enter elements of first set (type 'n' to stop):
Element: n
Set cannot be empty.
Element: 4
Element: n
Enter elements of second set (type 'n' to stop):
Element: 4
Element: n
Union of sets: [4]
'''