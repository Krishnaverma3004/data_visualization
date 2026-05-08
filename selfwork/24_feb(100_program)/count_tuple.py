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

# Input element to count
while True:
    elem = input("Enter element to count in tuple: ")
    valid = True
    start = 0
    if elem[0] == '-':
        start = 1
    for i in range(start, len(elem)):
        if elem[i] < '0' or elem[i] > '9':
            valid = False
    if not valid or elem == "-":
        print("Invalid input!")
        continue
    elem = int(elem)
    break

# Count occurrences manually
count = 0
i = 0
while i < len(tpl):
    if tpl[i] == elem:
        count += 1
    i += 1

print(f"Element {elem} occurs {count} times in tuple.")
'''output
Enter numbers for tuple (type 'n' to stop):
Number: 34
Number: 33
Number: rt
Invalid input!
Number: e3
Invalid input!
Number: 33
Number: n
Enter element to count in tuple: 3
Element 3 occurs 0 times in tuple.
'''