# Problem 80
# Sort dictionary by values manually

data = {"a": 30, "b": 10, "c": 20}

# Convert dictionary to list of [key, value]
items = []

for k in data:
    items.append([k, data[k]])

# Bubble sort by value
i = 0
while i < len(items):
    j = i + 1
    while j < len(items):
        if items[i][1] > items[j][1]:
            temp = items[i]
            items[i] = items[j]
            items[j] = temp
        j += 1
    i += 1

print("Sorted by Values:")
for item in items:
    print(item[0], ":", item[1])

    '''output:
    Sorted by Values:
b : 10
c : 20
a : 30
    '''