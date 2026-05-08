# Input tuple elements
tpl = []
print("Enter numbers for tuple, type 'done' to stop:")
while True:
    s = input("Number: ")
    if s.lower() == "done":
        if len(tpl) == 0:
            print("Tuple cannot be empty.")
            continue
        break
    if all('0' <= c <= '9' for c in s) and s != "":
        tpl += [int(s)]
    else:
        print("Invalid input!")

# Convert list to tuple
tpl = tuple(tpl)

# Find maximum manually using iterator style
max_val = tpl[0]
i = 1
while i < len(tpl):
    if tpl[i] > max_val:
        max_val = tpl[i]
    i += 1

print("Maximum value in tuple:", max_val)
'''output
Enter numbers for tuple, type 'done' to stop:
Number: 1
Number: ww
Invalid input!
Number: 33
Number: 2,2
Invalid input!
Number: 2.2
Invalid input!
Number: 3
Number: 3
Number: done
Maximum value in tuple: 33
'''