# Input speed of vehicle
speed_input = input("Enter speed of vehicle (km/h): ")

# Validate input
valid = 1
for ch in speed_input:
    valid = valid * ((ch >= '0') * (ch <= '9'))

speed = int(speed_input) * valid

# Calculate fine based on speed
if valid == 1:
    if speed <= 60:
        print("No fine")
    else:
        if speed <= 80:
            print("Fine: $50")
        else:
            print("Fine: $100")
