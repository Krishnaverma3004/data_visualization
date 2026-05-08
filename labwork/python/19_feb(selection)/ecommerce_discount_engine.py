cart_value = float(input("Enter cart value (in Rs): "))

if cart_value < 0:
    print("Invalid cart value. Program terminated.")

else:
    membership = input("Enter membership (Silver/Gold/Platinum): ")

    if membership != "Silver" and membership != "Gold" and membership != "Platinum":
        print("Invalid membership type. Program terminated.")

    else:
        festival = input("Is it festival season? (yes/no): ")

        if festival != "yes" and festival != "no":
            print("Invalid festival input. Program terminated.")

        else:
            discount = 0

            # Cart value discount
            if cart_value >= 10000:
                discount = 20
            elif cart_value >= 5000:
                discount = 10

            # Membership discount
            if membership == "Silver" and discount < 5:
                discount = 5
            elif membership == "Gold" and discount < 10:
                discount = 10
            elif membership == "Platinum" and discount < 15:
                discount = 15

            # Festival discount
            if festival == "yes" and discount < 12:
                discount = 12

            final_amount = cart_value - (cart_value * discount / 100)

            print("Highest Discount Applied:", discount, "%")
            print("Final Payable Amount: Rs", final_amount)
