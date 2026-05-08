weight_input = input("Enter weight (kg): ")
height_input = input("Enter height (m): ")

valid = 1
for ch in weight_input + height_input:
    valid = valid * ((ch >= '0') * (ch <= '9') or ch == '.')

weight = float(weight_input) * valid
height = float(height_input) * valid

if valid == 1:
    bmi = weight / (height * height)
    if bmi < 18.5:
        print("Underweight")
    elif bmi < 25:
        print("Normal weight")
    else:
        print("Overweight")
