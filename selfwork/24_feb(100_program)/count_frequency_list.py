# Input list manually
lst = []
print("Enter numbers one by one. Type 'done' when finished:")
while True:
    s = input("Enter number: ")
    if s.lower() == "done":
        if len(lst) == 0:
            print("List cannot be empty.")
            continue
        break
    # Validate positive integers
    if all('0' <= c <= '9' for c in s) and s != "":
        lst.append(int(s))
    else:
        print("Invalid input. Enter a positive integer or 'done'.")

# Count frequency manually
freq = {}
for x in lst:
    if x in freq:
        freq[x] += 1
    else:
        freq[x] = 1

print("Element frequencies:", freq)
'''output:
Enter numbers one by one. Type 'done' when finished:
Enter number: 34
Enter number: 33
Enter number: 22
Enter number: 44
Enter number: 
Invalid input. Enter a positive integer or 'done'.
Enter number: 3
Enter number: 2
Enter number: 3
Enter number: 2
Enter number: done
Element frequencies: {34: 1, 33: 1, 22: 1, 44: 1, 3: 2, 2: 2}
'''