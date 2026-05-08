# Collect numbers
nums = []
print("Enter numbers one by one (0 to stop):")
while True:
    n = input("Num: ")
    if all('0' <= c <= '9' for c in n) and n != "":
        n = int(n)
        if n == 0:
            if len(nums) == 0:
                print("List cannot be empty.")
                continue
            break
        nums += [n]
    else:
        print("Invalid! Enter positive integer.")

# Even numbers
even = []
i = 0
while i < len(nums):
    if nums[i] % 2 == 0:
        even += [nums[i]]
    i += 1

# Odd numbers
odd = []
i = 0
while i < len(nums):
    if nums[i] % 2 != 0:
        odd += [nums[i]]
    i += 1

print("Even numbers:", even)
print("Odd numbers:", odd)
'''output
'''