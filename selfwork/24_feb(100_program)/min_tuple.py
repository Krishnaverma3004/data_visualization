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
    # Validate integer (allow negative)
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

tpl = tuple(tpl)  # convert to tuple

# Find minimum manually
min_val = tpl[0]
i = 1
while i < len(tpl):
    if tpl[i] < min_val:
        min_val = tpl[i]
    i += 1

print("Minimum value in tuple:", min_val)
'''output
Number: n
Tuple cannot be empty.
Number: 3
Number: 3
Number: 3
Number: 2
Number: 2
Number: 3
Number: 4
Number: 9
Number: 1
Number: n
Minimum value in tuple: 1
'''