# Take first set
a = []
print("Enter first set (n to stop):")
while True:
    s = input("Value: ")
    if s.lower() == "n":
        if len(a) == 0:
            print("Set cannot be empty.")
            continue
        break
    good = True
    i = 0
    if s[0] == '-':
        i = 1
    while i < len(s):
        if s[i] < '0' or s[i] > '9':
            good = False
        i += 1
    if good and s != "-":
        a.append(int(s))
    else:
        print("Invalid!")

# Take second set
b = []
print("Enter second set (n to stop):")
while True:
    s = input("Value: ")
    if s.lower() == "n":
        if len(b) == 0:
            print("Set cannot be empty.")
            continue
        break
    good = True
    i = 0
    if s[0] == '-':
        i = 1
    while i < len(s):
        if s[i] < '0' or s[i] > '9':
            good = False
        i += 1
    if good and s != "-":
        b.append(int(s))
    else:
        print("Invalid!")

# Check subset
subset = True
for x in a:
    exists = False
    for y in b:
        if x == y:
            exists = True
    if not exists:
        subset = False

if subset:
    print("First set is subset of second set.")
else:
    print("First set is NOT subset of second set.")
'''output:
Enter first set (n to stop):
Value: 34
Value: 33
Value: n
Enter second set (n to stop):
Value: 33
Value: 4
Value: n
First set is NOT subset of second set.'''