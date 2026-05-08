age_input = input("Enter your age: ")

# Validate input
valid = 1
for ch in age_input:
    valid = valid * ((ch >= '0') * (ch <= '9'))

age = int(age_input) * valid

if valid == 1 and age >= 18:
    print("You are eligible to vote")
