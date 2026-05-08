# Input validation
lst = []
print("Enter numbers one by one. Type 'done' to finish:")
while True:
    s = input("Enter number: ")
    if s.lower() == "done":
        if len(lst) == 0:
            print("List cannot be empty.")
            continue
        break
    if all('0' <= c <= '9' for c in s) and s != "":
        lst.append(int(s))
    else:
        print("Invalid input, enter positive integer or 'done'.")

# Manual bubble sort
for i in range(len(lst)):
    for j in range(i+1,len(lst)):
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print("Sorted list:", lst)