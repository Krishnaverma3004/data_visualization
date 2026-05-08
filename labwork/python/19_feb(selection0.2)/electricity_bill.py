units = float(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid input. Program terminated.")
else:
    senior = input("Are you a senior citizen? (yes/no): ")

    if senior != "yes" and senior != "no":
        print("Invalid input for senior citizen. Program terminated.")
    else:
        # Calculate bill
        if units <= 100:
            bill = units * 5
        elif units <= 300:
            bill = units * 7
        else:
            bill = units * 10

        # Apply discount for senior citizen
        if senior == "yes":
            bill = bill - (bill * 10 / 100)

        print("Total electricity bill: Rs", bill)
