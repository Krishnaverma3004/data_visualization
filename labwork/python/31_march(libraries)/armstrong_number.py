def check_armstrong_number(number):
    temp = number
    digit_count = 0

    # Count number of digits
    while temp > 0:
        digit_count += 1
        temp = temp // 10

    temp = number
    total_sum = 0

    # Calculate sum of digits raised to power
    while temp > 0:
        digit = temp % 10

        power_value = 1
        for i in range(digit_count):
            power_value = power_value * digit

        total_sum += power_value
        temp = temp // 10

    # Check if Armstrong
    return total_sum == number


# ----------- USER INPUT SECTION -----------

number = int(input("Enter number: "))

if check_armstrong_number(number):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")

'''output:
Enter number: 342
Not Armstrong Number

output2:
Enter number: 153
Armstrong Number
'''    