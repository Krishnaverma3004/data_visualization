income_input = input("Enter income: ")
valid = 1
for ch in income_input:
    valid = valid * ((ch >= '0') * (ch <= '9'))

income = int(income_input) * valid

# Tax calculation using arithmetic only
tax = income * ((income > 250000) * (income <= 500000) * 0.05 \
    + (income > 500000) * (income <= 1000000) * 0.20 \
    + (income > 1000000) * 0.30)

# Print
print("Tax =", tax + (0 * (valid == 0)))  # prints 0 if invalid
