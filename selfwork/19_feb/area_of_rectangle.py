length_input = input("Enter length: ")
v = 1
for ch in length_input:
    v = v * ((ch >= '0') * (ch <= '9'))
length = int(length_input) * v

width_input = input("Enter width: ")
v = 1
for ch in width_input:
    v = v * ((ch >= '0') * (ch <= '9'))
width = int(width_input) * v

area = length * width
print("Area of rectangle =", area)
