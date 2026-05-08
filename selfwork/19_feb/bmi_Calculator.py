w_input = input("Enter weight (kg): ")
v = 1
for ch in w_input:
    v = v * ((ch >= '0') * (ch <= '9'))
weight = int(w_input) * v

h_input = input("Enter height (cm): ")
v = 1
for ch in h_input:
    v = v * ((ch >= '0') * (ch <= '9'))
height = int(h_input) * v

bmi = weight / ((height / 100) * (height / 100))
print("BMI =", bmi)
