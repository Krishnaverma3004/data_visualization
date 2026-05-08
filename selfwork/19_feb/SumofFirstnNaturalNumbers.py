n_input = input("Enter a positive integer n: ")
valid = 1

# Validate digits
for ch in n_input:
    valid = valid * ((ch >= '0') * (ch <= '9'))

# Convert to number
n = int(n_input) * valid

# Ensure positive using max arithmetic
n = n + ((0 - n) * (n <= 0))  # if n <= 0, becomes 0

# Sum using loop
total = 0
for i in range(1, n + 1):
    total = total + i

# Print
print("Sum of first", n, "natural numbers =", total + (0 * (valid == 0)))  # if invalid, prints 0
