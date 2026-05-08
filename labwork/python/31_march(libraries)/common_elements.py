def find_common_elements(list_one, list_two):
    # List to store common elements
    common_list = []

    # Compare each element of first list with second list
    for i in range(len(list_one)):
        for j in range(len(list_two)):
            if list_one[i] == list_two[j]:

                # Check if already added (to avoid duplicates)
                already_present = False
                for k in range(len(common_list)):
                    if common_list[k] == list_one[i]:
                        already_present = True
                        break

                # If not present, add to result
                if not already_present:
                    common_list.append(list_one[i])

    return common_list


# ----------- USER INPUT SECTION -----------

list_one = []
list_two = []

size_one = int(input("Enter size of first list: "))
for i in range(size_one):
    list_one.append(int(input("Enter element: ")))

size_two = int(input("Enter size of second list: "))
for i in range(size_two):
    list_two.append(int(input("Enter element: ")))

print("Common Elements:", find_common_elements(list_one, list_two))

'''output:
Enter size of first list: 20
Enter element: 56
Enter element: 45
Enter element: 34
Enter element: 23
Enter element: 12
Enter element: 22
Enter element: 33
Enter element: 44
Enter element: 55
Enter element: 66
Enter element: 77
Enter element: 88
Enter element: 99
Enter element: 22
Enter element: 33
Enter element: 44
Enter element: 55
Enter element: 66
Enter element: 99
Enter element: 70
Enter size of second list: 20
Enter element: 67
Enter element: 56
Enter element: 46
Enter element: 35
Enter element: 24
Enter element: 12
Enter element: 23
Enter element: 4
Enter element: 5
Enter element: 55
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
Common Elements: [56, 45, 34, 23, 12, 22, 33, 44, 55, 66, 77, 88, 99, 70]'''