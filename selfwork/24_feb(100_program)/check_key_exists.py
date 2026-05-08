# Problem 83
# Check whether a key exists in dictionary

data = {"x": 100, "y": 200, "z": 300}

key = input("Enter key to check: ")

# Validate input
if key == "":
    print("Error: Key cannot be empty.")
else:
    if key in data:
        print("Key exists in dictionary.")
    else:
        print("Key does not exist.")

'''output
Enter key to check: x
Key exists in dictionary.
'''        