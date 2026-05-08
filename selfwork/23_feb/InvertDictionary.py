# Program: Invert Dictionary 

original_dict = {}  # dictionary to store user input

# Input number of items
n = int(input("How many items do you want in the dictionary? "))
i = 0
while i < n:
    key = input("Enter key #" + str(i + 1) + ": ")
    if key == "":
        print("Key cannot be empty. Please enter a valid key.")
        continue
    value = input("Enter value for key '" + key + "': ")
    if value == "":
        print("Value cannot be empty. Please enter a valid value.")
        continue
    original_dict[key] = value
    i = i + 1

# Invert dictionary manually
inverted_dict = {}
for key in original_dict:
    value = original_dict[key]
    # check if value already exists as a key to avoid overwriting
    if value in inverted_dict:
        print("Warning: Duplicate value '" + value + "' detected. Previous key '" + inverted_dict[value] + "' will be overwritten.")
    inverted_dict[value] = key

print("Original dictionary:", original_dict)
print("Inverted dictionary:", inverted_dict)

''' Output
How many items do you want in the dictionary? 3
Enter key #1: name
Enter value for key 'name': Alice
Enter key #2: age
Enter value for key 'age': 25
Enter key #3: city
Enter value for key 'city': New York
Original dictionary: {'name': 'Alice', 'age': '25', 'city': 'New York'}
Inverted dictionary: {'Alice': 'name', '25': 'age', 'New York': 'city'}


output
How many items do you want in the dictionary? 0
Original dictionary: {}
Inverted dictionary: {}

output
How many items do you want in the dictionary? 2
Enter key #1: name
Enter value for key 'name': Bob
Enter key #2: name
Value cannot be empty. Please enter a valid value.
Enter key #2: age
Enter value for key 'age': 30
Original dictionary: {'name': 'Bob', 'age': '30'}
Inverted dictionary: {'Bob': 'name', '30': 'age'}
'''