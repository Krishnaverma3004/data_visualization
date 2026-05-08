# -------------------------------------------------------
# Bank Transaction Analyzer
# - Calculate total balance (3 decimal places)
# - Find largest withdrawal
# - Count deposits greater than 10000
# - No split(), no sum(), no max()
# -------------------------------------------------------

def bank_transaction_analyzer():

    # Take full input string
    data = input("Enter transactions (positive=deposit, negative=withdrawal): ")

    transactions = []
    number = ""

    # -----------------------------------
    # Manual parsing (handle negative numbers)
    # -----------------------------------
    for i in range(len(data)):

        if data[i] != " ":
            number = number + data[i]
        else:
            valid = True

            if number != "":
                start = 0

                if number[0] == '-':
                    start = 1

                for j in range(start, len(number)):
                    if number[j] < '0' or number[j] > '9':
                        valid = False

                if valid and not (number == "-" or number == ""):
                    transactions.append(int(number))

            number = ""

    # Add last number
    valid = True
    if number != "":
        start = 0

        if number[0] == '-':
            start = 1

        for j in range(start, len(number)):
            if number[j] < '0' or number[j] > '9':
                valid = False

        if valid and not (number == "-" or number == ""):
            transactions.append(int(number))

    # -----------------------------------
    # Calculate total balance manually
    # -----------------------------------
    balance = 0

    for i in range(len(transactions)):
        balance = balance + transactions[i]

    # Format balance to 3 decimal places
    formatted_balance = format(balance, ".3f")

    # -----------------------------------
    # Find largest withdrawal manually
    # -----------------------------------
    largest_withdrawal = 0
    withdrawal_found = False

    for i in range(len(transactions)):
        if transactions[i] < 0:
            withdrawal_amount = -transactions[i]

            if not withdrawal_found or withdrawal_amount > largest_withdrawal:
                largest_withdrawal = withdrawal_amount
                withdrawal_found = True

    # -----------------------------------
    # Count deposits greater than 10000
    # -----------------------------------
    large_deposits = 0

    for i in range(len(transactions)):
        if transactions[i] > 10000:
            large_deposits = large_deposits + 1

    # -----------------------------------
    # Display results
    # -----------------------------------
    print("\nTotal Balance:", formatted_balance)

    if withdrawal_found:
        print("Largest Withdrawal:", largest_withdrawal)
    else:
        print("Largest Withdrawal: None")

    print("Deposits greater than 10000:", large_deposits)
    
    
'''output:
Enter transactions (positive=deposit, negative=withdrawal): 15000 -5000 20000 -3000 500
Total Balance: 37000.000
Largest Withdrawal: 5000
Deposits greater than 10000: 2
'''