# Take first set input
a = []
print("Enter elements for first set (press n to stop):")
while True:
    s = input("Value: ")
    if s.lower() == "n":
        if len(a) == 0:
            print("First set cannot be empty.")
            continue
        break

    ok = True
    i = 0
    if s[0] == '-':
        i = 1
    while i < len(s):
        if s[i] < '0' or s[i] > '9':
            ok = False
        i += 1

    if not ok or s == "-":
        print("Invalid number!")
    else:
        a.append(int(s))

# Take second set input
b = []
print("Enter elements for second set (press n to stop):")
while True:
    s = input("Value: ")
    if s.lower() == "n":
        if len(b) == 0:
            print("Second set cannot be empty.")
            continue
        break

    ok = True
    i = 0
    if s[0] == '-':
        i = 1
    while i < len(s):
        if s[i] < '0' or s[i] > '9':
            ok = False
        i += 1

    if not ok or s == "-":
        print("Invalid number!")
    else:
        b.append(int(s))

# Find intersection manually
result = []
for x in a:
    for y in b:
        if x == y:
            found = False
            for z in result:
                if z == x:
                    found = True
            if not found:
                result.append(x)

print("Intersection:", result)
'''output:Enter elements for first set (press n to stop):
Value: 1
Value: 2
Value: 3
Value: n
Enter elements for second set (press n to stop):
Value: 2
Value: 3
Value: 5
Value: n
Intersection: [2, 3]'''