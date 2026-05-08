# Input validation
lst = []
print("Enter numbers one by one. Type 'done' to finish:")
while True:
    s = input("Enter number: ")
    if s.lower() == "done":
        if len(lst) < 2:
            print("Enter at least two numbers.")
            continue
        break
    if all('0' <= c <= '9' for c in s) and s != "":
        lst.append(int(s))
    else:
        print("Invalid input, enter positive integer or 'done'.")

# Find second largest manually
max1 = max2 = -1
for x in lst:
    if x > max1:
        max2 = max1
        max1 = x
    elif x > max2 and x != max1:
        max2 = x

print("Second largest:", max2)

'''output:
Enter numbers one by one. Type 'done' to finish:
Enter number: 56
Enter number: 44
Enter number: 33
Enter number: 
Invalid input, enter positive integer or 'done'.
Enter number: 3.3
Invalid input, enter positive integer or 'done'.
Enter number: abc
Invalid input, enter positive integer or 'done'.
Enter number: 56
Enter number: 56
Enter number: 33
Enter number: 44
Enter number: done
Second largest: 44
'''