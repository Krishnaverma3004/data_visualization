# Program: Count Occurrences in Tuple (User Input)
numbers = ()  # tuple to store user input

# Take number of elements
n = int(input("Enter the number of elements in the tuple: "))
i = 0
while i < n:
    num_str = input("Enter element #" + str(i + 1) + ": ")
    
    # manual validation: check if input is numeric
    is_valid = True
    j = 0
    while j < len(num_str):
        if not ('0' <= num_str[j] <= '9'):
            is_valid = False
            break
        j = j + 1
    
    if is_valid:
        # convert string to integer manually
        num = 0
        j = 0
        while j < len(num_str):
            num = num * 10 + (ord(num_str[j]) - ord('0'))
            j = j + 1
        numbers = numbers + (num,)
        i = i + 1
    else:
        print("Invalid input! Please enter a numeric value.")

# Count occurrences manually
occurrences = {}  # store counts
i = 0
while i < n:
    num = numbers[i]
    
    # check if num already in dictionary manually
    found = False
    for key in occurrences:
        if key == num:
            occurrences[key] = occurrences[key] + 1
            found = True
            break
    if not found:
        occurrences[num] = 1
    i = i + 1

print("Element occurrences:", occurrences)

''' Output
Enter the number of elements in the tuple: 5
Enter element #1: 10
Enter element #2: 20
Enter element #3: 10
Enter element #4: 30
Enter element #5: 20


output
Enter the number of elements in the tuple: 4
Enter element #1: 5
Enter element #2: 5
Enter element #3: 5
Enter element #4: abc
Invalid input! Please enter a numeric value.
Enter element #4: 5
Element occurrences: {5: 4}
'''