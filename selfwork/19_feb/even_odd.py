num_input = input("Enter a number: ")

valid = 1
for ch in num_input:
    valid = valid * ((ch >= '0') * (ch <= '9'))

num = int(num_input) * valid

if valid == 1:
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
