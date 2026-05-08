# Program: Sum Values in Dictionary (User Input)


scores = {}  # empty dictionary to store subjects and marks

n = int(input("Enter number of subjects: "))  # number of key-value pairs

# take input for each subject
for i in range(n):
    key = input("Enter subject name: ")
    value = int(input("Enter marks for " + key + ": "))
    scores[key] = value

total = 0  # initialize sum

# iterate through dictionary values manually
for key in scores:
    total = total + scores[key]

print("Total sum of values:", total)

'''output example:
Enter number of subjects: 3
Enter subject name: Math
Enter marks for Math: 85
Enter subject name: Science
Enter marks for Science: 90
Enter subject name: English
Enter marks for English: 78
Total sum of values: 253'''
