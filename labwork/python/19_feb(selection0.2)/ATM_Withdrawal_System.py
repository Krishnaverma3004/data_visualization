account_balance = float(input("Enter account balance (₹): "))
daily_limit = 50000
atm_cash = float(input("Enter ATM available cash (₹): "))
withdraw_amount = float(input("Enter withdrawal amount (₹): "))

if withdraw_amount < 0:
    print("Invalid withdrawal amount. Program terminated.")
elif withdraw_amount > account_balance:
    print("Transaction failed: Insufficient account balance.")
elif withdraw_amount > daily_limit:
    print("Transaction failed: Daily withdrawal limit exceeded.")
elif withdraw_amount > atm_cash:
    print("Transaction failed: ATM does not have sufficient cash.")
else:
    account_balance = account_balance - withdraw_amount
    atm_cash = atm_cash - withdraw_amount
    print("Transaction successful. Remaining balance: ₹", account_balance)
