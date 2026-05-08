# Manual symmetric difference

a = []
b = []

print("Enter first set (n to stop):")
while True:
    s = input("Value: ")
    if s.lower() == "n":
        break
    ok = True
    i = 0
    if s[0] == '-':
        i = 1
    while i < len(s):
        if s[i] < '0' or s[i] > '9':
            ok = False
        i += 1
    if ok and s != "-":
        a.append(int(s))
    else:
        print("Invalid!")

print("Enter second set (n to stop):")
while True:
    s = input("Value: ")
    if s.lower() == "n":
        break
    ok = True
    i = 0
    if s[0] == '-':
        i = 1
    while i < len(s):
        if s[i] < '0' or s[i] > '9':
            ok = False
        i += 1
    if ok and s != "-":
        b.append(int(s))
    else:
        print("Invalid!")

result = []

for x in a:
    found = False
    for y in b:
        if x == y:
            found = True
    if not found:
        result.append(x)

for x in b:
    found = False
    for y in a:
        if x == y:
            found = True
    if not found:
        result.append(x)

print("Symmetric Difference:", result)
'''output
Enter first set (n to stop):
Value: 56
Value: 4
Value: 33
Value: n
Enter second set (n to stop):
Value: 45
Value: 44
Value: n
Symmetric Difference: [56, 4, 33, 45, 44]'''