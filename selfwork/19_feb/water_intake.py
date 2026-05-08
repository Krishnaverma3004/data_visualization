age_input = input("Enter your age: ")

valid = 1
for ch in age_input:
    valid = valid * ((ch >= '0') * (ch <= '9'))

age = int(age_input) * valid

if valid == 1:
    if age < 10:
        print("Drink 1 liter of water")
    else:
        if age <= 50:
            print("Drink 2 liters of water")
        else:
            print("Drink 1.5 liters of water")
