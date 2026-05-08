# Program: Find Maximum in List (User Input with Validation)
# Description: Takes a list of numbers from the user and finds the maximum manually

# Take number of elements with validation
while True:
    n_str = input("Enter the number of elements in the list: ")
    is_valid = True
    j = 0
    while j < len(n_str):
        if not ('0' <= n_str[j] <= '9'):
            is_valid = False
            break
        j = j + 1
    if is_valid and n_str != "0":
        n = 0
        j = 0
        while j < len(n_str):
            n = n * 10 + (ord(n_str[j]) - ord('0'))
            j = j + 1
        break
    else:
        print("Invalid input! Please enter a positive number.")

# Take elements for the list with validation
numbers = []  # empty list
i = 0
while i < n:
    num_str = input("Enter element #" + str(i + 1) + ": ")
    # validate numeric input
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
        numbers.append(num)
        i = i + 1
    else:
        print("Invalid input! Please enter a numeric value.")

# Find maximum manually
max_value = numbers[0]
i = 1
while i < n:
    if numbers[i] > max_value:
        max_value = numbers[i]
    i = i + 1

print("The list you entered:", numbers)
print("Maximum value in the list is:", max_value)

''' Output
Enter the number of elements in the list: 5
Enter element #1: 10
Enter element #2: 25
Enter element #3: 7
Enter element #4: 40
Enter element #5: 15
The list you entered: [10, 25, 7, 40, 15
Maximum value in the list is: 40


output
Enter the number of elements in the list: 4
Enter element #1: 5
Enter element #2: abc
Invalid input! Please enter a numeric value.
Enter element #2: 12
Enter element #3: 8
Enter element #4: 20
The list you entered: [5, 12, 8, 20]
Maximum value in the list is: 20

'''