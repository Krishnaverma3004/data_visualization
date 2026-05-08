temp_input = input("Enter temperature in Celsius: ")

valid = 1
for ch in temp_input:
    valid = valid * ((ch >= '0') * (ch <= '9') or ch == '.' or ch == '-')

temp = float(temp_input) * valid

if valid == 1:
    if temp < 0:
        print("Freezing")
    elif temp <= 30:
        print("Normal")
    else:
        print("Hot")
