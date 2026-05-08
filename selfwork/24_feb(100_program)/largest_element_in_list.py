# Input validation
while True:
    lst_str = input("Enter numbers separated by space: ")
    if all(c.isdigit() or c==' ' for c in lst_str):
        lst = [int(x) for x in lst_str.split() if x]
        break
    else:
        print("Enter numbers only.")

# Find largest manually
max_val = lst[0]
for x in lst[1:]:
    if x > max_val: max_val = x
print("Largest:", max_val)

'''output
Enter numbers separated by space: abc
Enter numbers only.
Enter numbers separated by space: 1 2 3 4 5 
Largest: 5

'''

