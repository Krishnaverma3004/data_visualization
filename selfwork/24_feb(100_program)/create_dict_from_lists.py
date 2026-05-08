# Problem 84
# Create dictionary from two lists

keys = ["a", "b", "c"]
values = [10, 20, 30]

# Validate equal length
if len(keys) != len(values):
    print("Error: Lists must be of same length.")
else:
    result = {}
    i = 0

    while i < len(keys):
        result[keys[i]] = values[i]
        i += 1

    print("Created Dictionary:", result)

    '''output
    Created Dictionary: {'a': 10, 'b': 20, 'c': 30}
    
    '''