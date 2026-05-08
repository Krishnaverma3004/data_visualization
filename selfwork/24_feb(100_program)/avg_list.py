# Input list
nums = []
print("Enter numbers one by one (type '0' to stop):")
while True:
    s = input("Number: ")
    # Validate digits only
    valid = True
    for c in s:
        if c < '0' or c > '9':
            valid = False
    if not valid:
        print("Invalid input, enter numbers only!")
        continue

    n = int(s)
    if n == 0:
        if len(nums) == 0:
            print("List cannot be empty.")
            continue
        break
    nums += [n]

# Calculate sum and average manually
total = 0
count = 0
for i in nums:
    total += i
    count += 1

average = total / count
print("Average of list:", average)
'''output
Enter numbers one by one (type '0' to stop):
Number: 3.2
Invalid input, enter numbers only!
Number: 33
Number: 33
Number: abc
Invalid input, enter numbers only!
Number: 34
Number: 33
Number: 22
Number: 44
Number: 33
Number: 0
Average of list: 33.142857142857146
'''