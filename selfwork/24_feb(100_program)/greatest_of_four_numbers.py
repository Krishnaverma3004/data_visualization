# Program to find greatest of four numbers
# Sequential validation of each input

def is_numeric_manual(s):
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    return len(s) > 0

# Stepwise input
nums = []
for i in range(4):
    while True:
        n_str = input(f"Enter number {i+1}: ")
        if is_numeric_manual(n_str):
            nums.append(int(n_str))
            break
        else:
            print("Enter numeric value only.")

# Find greatest manually
greatest = nums[0]
if nums[1] > greatest:
    greatest = nums[1]
if nums[2] > greatest:
    greatest = nums[2]
if nums[3] > greatest:
    greatest = nums[3]

print("Greatest number is:", greatest)
'''output1:Enter number 1: 34
Enter number 2: 33
Enter number 3: 2
Enter number 4: 3
Greatest number is: 34


output2:
Enter number 1: abc
Enter numeric value only.
Enter number 1: 44
Enter number 2: er
Enter numeric value only.
Enter number 2: 44
Enter number 3: 67
Enter number 4: 89
Greatest number is: 89
'''