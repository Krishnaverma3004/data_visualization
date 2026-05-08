def find_second_largest(numbers):
    # Check if list has at least two elements
    if len(numbers) < 2:
        return None

    # Initialize first and second largest using first two elements
    first_largest = numbers[0]
    second_largest = numbers[1]

    # Arrange first two elements so that:
    # first_largest >= second_largest
    if second_largest > first_largest:
        temp = first_largest
        first_largest = second_largest
        second_largest = temp

    # Traverse remaining elements starting from index 2
    for index in range(2, len(numbers)):
        current_number = numbers[index]

        # If current number is greater than largest
        if current_number > first_largest:
            # Update second largest before changing largest
            second_largest = first_largest
            first_largest = current_number

        # If number is between largest and second largest
        elif current_number > second_largest and current_number != first_largest:
            second_largest = current_number

    # Return the second largest value
    return second_largest


# ----------- USER INPUT SECTION -----------

numbers = []

# Take size of list
size = int(input("Enter number of elements: "))

# Input elements one by one
for i in range(size):
    value = int(input("Enter element: "))
    numbers.append(value)

# Call function and store result
result = find_second_largest(numbers)

# Display result
if result is None:
    print("List must contain at least 2 elements")
else:
    print("Second Largest Element:", result)

'''output:
Enter number of elements: 20
Enter element: 90  
Enter element: 78
Enter element: 67
Enter element: 56
Enter element: 45
Enter element: 34
Enter element: 3
Enter element: 12
Enter element: 23
Enter element: 45
Enter element: 56
Enter element: 78
Enter element: 78
Enter element: 89
Enter element: 90
Enter element: 23
Enter element: 12
Enter element: 23
Enter element: 34
Enter element: 45
Second Largest Element: 89'''   