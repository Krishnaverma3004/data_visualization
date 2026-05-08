# Problem 79
# Sort dictionary by keys manually

data = {}

print("Enter dictionary (type n to stop):")

while True:
    key = input("Key: ")
    if key.lower() == "n":
        break

    value = input("Value (number): ")

    valid = True
    i = 0
    while i < len(value):
        if value[i] < '0' or value[i] > '9':
            valid = False
        i += 1

    if valid and value != "":
        data[key] = int(value)
    else:
        print("Invalid value!")

# Store keys in list
keys = []
for k in data:
    keys.append(k)

# Bubble sort keys
i = 0
while i < len(keys):
    j = i + 1
    while j < len(keys):
        if keys[i] > keys[j]:
            temp = keys[i]
            keys[i] = keys[j]
            keys[j] = temp
        j += 1
    i += 1

print("Sorted Dictionary by Keys:")
for k in keys:
    print(k, ":", data[k])
    '''output:
    Key: b
Value (number): 20
Key: a
Value (number): 10
Key: n
Sorted Dictionary by Keys:
a : 10
b : 20
    '''