# Input validation: accept list of positive integers without split
lst = []
print("Enter numbers one by one. Type 'done' to finish:")
while True:
    s = input("Enter number: ")
    if s.lower() == "done":
        if len(lst) == 0:
            print("List cannot be empty.")
            continue
        break
    # Validate: all chars are digits
    if all('0' <= c <= '9' for c in s) and s != "":
        lst.append(int(s))
    else:
        print("Invalid input, enter positive integer or 'done'.")

# Find smallest manually
min_val = lst[0]
for x in lst[1:]:
    if x < min_val:
        min_val = x

print("Smallest element:", min_val)

'''outputEnter numbers one by one. Type 'done' to finish:
Enter number: r
Invalid input, enter positive integer or 'done'.
Enter number: 1
Enter number: 2
Enter number: 3
Enter number: 4
Enter number: done
Smallest element: 1'''