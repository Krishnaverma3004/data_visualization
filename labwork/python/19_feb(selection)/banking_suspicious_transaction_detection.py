amount = float(input("Enter transaction amount: "))

if amount < 0:
    print("Invalid amount. Program terminated.")

else:
    account_age = float(input("Enter account age (in months): "))

    if account_age < 0:
        print("Invalid account age. Program terminated.")

    else:
        international = input("Is it international? (yes/no): ").strip().lower()

        if international != "yes" and international != "no":
            print("Invalid input. Program terminated.")

        elif amount > 200000 and account_age < 6 and international == "yes":
            print("Transaction FLAGGED for manual verification.")

        else:
            print("Transaction is normal.")
