income = float(input("Enter your annual income (in Rs): "))
age = int(input("Enter your age: "))

if income < 0 or age < 0:
    print("Invalid input. Program terminated.")

else:
    # Set exemption limit
    if age >= 60:
        exemption = 300000
    else:
        exemption = 250000

    # Tax calculation
    if income <= exemption:
        tax = 0

    elif income <= 500000:
        tax = (income - exemption) * 0.05

    elif income <= 1000000:
        tax = ((500000 - exemption) * 0.05) + ((income - 500000) * 0.20)

    else:
        tax = ((500000 - exemption) * 0.05) + (500000 * 0.20) + ((income - 1000000) * 0.30)

    print("Income Tax to be paid: Rs", tax)
