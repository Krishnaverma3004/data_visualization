# Problem 78
# Merge two dictionaries manually

dict1 = {}
dict2 = {}

print("Enter first dictionary (type n to stop):")

while True:
    key = input("Key: ")
    if key.lower() == "n":
        break

    value = input("Value (number only): ")

    # Validate numeric value
    valid = True
    i = 0
    while i < len(value):
        if value[i] < '0' or value[i] > '9':
            valid = False
        i += 1

    if valid and value != "":
        dict1[key] = int(value)
    else:
        print("Invalid value!")

print("Enter second dictionary (type n to stop):")

while True:
    key = input("Key: ")
    if key.lower() == "n":
        break

    value = input("Value (number only): ")

    valid = True
    i = 0
    while i < len(value):
        if value[i] < '0' or value[i] > '9':
            valid = False
        i += 1

    if valid and value != "":
        dict2[key] = int(value)
    else:
        print("Invalid value!")

# Manual merge
for k in dict2:
    dict1[k] = dict2[k]

print("Merged Dictionary:", dict1)

'''output
Key: a
Value (number only): 10
Key: n
Key: b
Value (number only): 20
Key: n
Merged Dictionary: {'a': 10, 'b': 20}
'''