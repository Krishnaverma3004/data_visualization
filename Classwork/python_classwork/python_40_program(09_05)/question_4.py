# Q4. Write a menu-driven banking application using a while loop that allows users to deposit, withdraw, check balance, and exit only when the user chooses the exit option.
class BankAccount:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")

    def check_balance(self):
        print(f"Current balance: ${self.balance:.2f}")
def main(): 
    account = BankAccount()
    while True:
        print("\nMenu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)
        elif choice == '3':
            account.check_balance()
        elif choice == '4':
            print("Exiting the application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()
#--------------------- output:---------------------
# Menu:
# 1. Deposit
# 2. Withdraw
# 3. Check Balance
# 4. Exit
# Enter your choice (1-4): 1
# Enter amount to deposit: 100
# Deposited: $100.00
