# Input first set
set1 = []
print("First set input (n to stop):")
while True:
    s = input("Number: ")
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

    if valid and s != "-":
        set1.append(int(s))
    else:
        print("Invalid input!")

# Input second set
set2 = []
print("Second set input (n to stop):")
while True:
    s = input("Number: ")
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

    if valid and s != "-":
        set2.append(int(s))
    else:
        print("Invalid input!")

# Difference set1 - set2
diff = []
for x in set1:
    present = False
    for y in set2:
        if x == y:
            present = True
    if not present:
        diff.append(x)

print("Difference (Set1 - Set2):", diff)
'''output:
First set input (n to stop):
Number: 45
Number: 55
Number: 44
Number: 56
Number: 67
Number: n
Second set input (n to stop):
Number: 34
Number: 3
Number: 34
Number: n
Difference (Set1 - Set2): [45, 55, 44, 56, 67]'''