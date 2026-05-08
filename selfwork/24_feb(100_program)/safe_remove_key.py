# Problem 82
# Safely remove key from dictionary

data = {"a": 10, "b": 20}

key = input("Enter key to remove: ")

if key in data:
    del data[key]
    print("Key removed successfully.")
else:
    print("Error: Key not found.")

print("Updated Dictionary:", data)

'''output:
Enter key to remove: a
Key removed successfully.
Updated Dictionary: {'b': 20}
'''