# Units consumed
units_input = input("Enter water units consumed: ")
ch0 = (units_input + "0")[0]; ch1 = (units_input + "00")[1]
v = ((ch0 >= '0') * (ch0 <= '9')) * ((ch1 >= '0') * (ch1 <= '9'))
units = int(units_input) * v

# Rate per unit
rate_input = input("Enter rate per unit: ")
ch0 = (rate_input + "0")[0]; ch1 = (rate_input + "00")[1]
v2 = ((ch0 >= '0') * (ch0 <= '9')) * ((ch1 >= '0') * (ch1 <= '9'))
rate = int(rate_input) * v2

bill = units * rate
print("Water bill =", bill)
