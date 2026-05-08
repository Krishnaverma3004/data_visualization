age_input = input("Enter your age: ")

valid = 1
for ch in age_input:
    valid = valid * ((ch >= '0') * (ch <= '9'))

age = int(age_input) * valid

if valid == 1:
    if age < 12:
        print("Ticket price: $5")
    else:
        if age < 60:
            print("Ticket price: $10")
        else:
            print("Ticket price: $7")
