# Function to find GCD
def gcd(a,b):
    while b != 0:
        a, b = b, a%b
    return a

# Input validation
nums = []
for i in range(2):
    while True:
        n = input(f"Enter  positive number {i+1}: ")
        if all('0' <= c <= '9' for c in n) and n != "0":
            nums.append(int(n))
            break
        else:
            print("Enter valid integer.")

print("GCD:", gcd(nums[0], nums[1]))
'''output:
Enter valid integer.
Enter  positive number 1: a
Enter valid integer.
Enter  positive number 1: -978
Enter valid integer.
Enter  positive number 1: 45
Enter  positive number 2: 5
GCD: 5'''