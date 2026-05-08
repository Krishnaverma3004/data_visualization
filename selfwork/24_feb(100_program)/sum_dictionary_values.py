# Problem 85
# Find sum of all dictionary values

data = {"a": 5, "b": 15, "c": 20}

total = 0

for key in data:
    total = total + data[key]

print("Sum of dictionary values:", total)

'''output
Sum of dictionary values: 40
'''