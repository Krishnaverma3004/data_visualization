# Program: Merge Two Dictionaries 

dict1 = {}  # first dictionary
dict2 = {}  # second dictionary

# Input for first dictionary
n1 = int(input("Enter number of items in first dictionary: "))
i = 0
while i < n1:
    key = input("Enter key for first dictionary: ")
    value = input("Enter value for key '" + key + "': ")
    dict1[key] = value
    i = i + 1

# Input for second dictionary
n2 = int(input("Enter number of items in second dictionary: "))
i = 0
while i < n2:
    key = input("Enter key for second dictionary: ")
    value = input("Enter value for key '" + key + "': ")
    dict2[key] = value
    i = i + 1

merged_dict = {}  # empty dictionary

# merge manually
for key in dict1:
    merged_dict[key] = dict1[key]
for key in dict2:
    merged_dict[key] = dict2[key]

print("Merged dictionary:", merged_dict)

''' Output:
Enter number of items in first dictionary: 2
Enter key for first dictionary: name
Enter value for key 'name': Alice
Enter key for first dictionary: age
Enter value for key 'age': 25
Enter number of items in second dictionary: 2
Enter key for second dictionary: city
Enter value for key 'city': New York
Enter key for second dictionary: country
Enter value for key 'country': USA'
Merged dictionary: {'name': 'Alice', 'age': '25', 'city': 'New York', 'country': 'USA'}

output
Enter number of items in first dictionary: -1
Invalid input! Number of items cannot be negative.

Enter number of items in first dictionary: 2
Enter key for first dictionary: name
Enter value for key 'name': Bob
Enter key for first dictionary: age
Enter value for key 'age': 30
Enter number of items in second dictionary: -1
 Invalid input! Number of items cannot be negative.  '''