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

# Remove duplicates manually
unique = []
for x in lst:
    if x not in unique:
        unique.append(x)

print("List without duplicates:", unique)
'''output:
Enter numbers one by one. Type 'done' to finish:
Enter number: 45
Enter number: 34
Enter number: 2
Enter number: 22
Enter number: 44
Enter number: done
List without duplicates: [45, 34, 2, 22, 44]'''