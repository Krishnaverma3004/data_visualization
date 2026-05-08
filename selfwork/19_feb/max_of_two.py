a_input = input("Enter first number: ")
b_input = input("Enter second number: ")

valid = 1
for ch in a_input + b_input:
    valid = valid * ((ch >= '0') * (ch <= '9'))

a = int(a_input) * valid
b = int(b_input) * valid

if valid == 1:
    if a > b:
        print("Maximum is", a)
    else:
        print("Maximum is", b)
