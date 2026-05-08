# Input credit score
credit_score = int(input("Enter credit score: "))

if credit_score < 0 or credit_score > 850:
    print("Invalid credit score. Program terminated.")
else:
    # Check credit score first
    if credit_score < 600:
        print("Loan Rejected: Credit score less than 600.")
    elif credit_score == 750:
        print("Loan Approved.")
    elif credit_score > 750:
        print("Loan Approved.")
    else:
        # Further check income
        monthly_income = float(input("Enter monthly income (₹): "))

        if monthly_income < 0:
            print("Invalid monthly income. Program terminated.")
        else:
            # Only take existing loans if income is valid
            existing_loans = float(input("Enter existing loan amount (₹): "))

            if existing_loans < 0:
                print("Invalid existing loan amount. Program terminated.")
            else:
                if monthly_income < 30000 and existing_loans > 500000:
                    print("Loan Rejected: Income less than ₹30,000 and existing loans above ₹5,00,000.")
                else:
                    print("Loan Approved.")