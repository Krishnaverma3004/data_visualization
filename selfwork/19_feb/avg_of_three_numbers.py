num1 = input("Enter number 1: ")
v1 = 1
for ch in num1:
    v1 = v1 * ((ch >= '0') * (ch <= '9'))
num1 = int(num1) * v1

num2 = input("Enter number 2: ")
v2 = 1
for ch in num2:
    v2 = v2 * ((ch >= '0') * (ch <= '9'))
num2 = int(num2) * v2

num3 = input("Enter number 3: ")
v3 = 1
for ch in num3:
    v3 = v3 * ((ch >= '0') * (ch <= '9'))
num3 = int(num3) * v3

average = (num1 + num2 + num3) / 3
print("Average =", average)
