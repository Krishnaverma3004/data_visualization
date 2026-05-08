# Program: Find Maximum in Tuple (User Input)
# Description: Finds the largest number in a tuple manually from user input

numbers = ()  # empty tuple to store numbers

n = int(input("Enter the number of elements in the tuple: "))
i = 0
while i < n:
    num_str = input("Enter element #" + str(i + 1) + ": ")
    
    # manual validation: check if num_str is all digits
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

# assume first element is maximum
max_value = numbers[0]

# iterate through tuple manually
index = 0
while index < n:
    if numbers[index] > max_value:
        max_value = numbers[index]
    index = index + 1

print("Maximum value in the tuple is:", max_value)