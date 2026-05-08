def remove_duplicates_from_list(numbers):
    # List to store unique elements
    unique_list = []

    # Traverse original list
    for i in range(len(numbers)):
        found = False

        # Check if element already exists
        for j in range(len(unique_list)):
            if numbers[i] == unique_list[j]:
                found = True
                break

        # If not found, add to unique list
        if not found:
            unique_list.append(numbers[i])

    return unique_list


# ----------- USER INPUT SECTION -----------

numbers = []
size = int(input("Enter number of elements: "))

for i in range(size):
    numbers.append(int(input("Enter element: ")))

print("List without duplicates:", remove_duplicates_from_list(numbers))


'''output:
Enter number of elements: 5
Enter element: 56
Enter element: 78
Enter element: 89
Enter element: 34
Enter element: 23
List without duplicates: [56, 78, 89, 34, 23]
'''