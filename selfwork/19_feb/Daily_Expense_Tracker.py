# Daily Expense Tracker (Improved Version)


total = 0

while True:
    expense = input("Enter daily expense (-1 to stop): ")
    valid = 1

    # Stop condition
    if expense == "-1":
        break

    # Empty check
    if expense == "":
        valid = 0
    else:
        i = 0

        # Check for negative sign
        if expense[0] == '-':
            i = 1
            # If only "-" entered → invalid
            if expense[1:2] == "":
                valid = 0

        # Manual digit validation without len()
        while expense[i:i+1] != "":
            if expense[i] < '0' or expense[i] > '9':
                valid = 0
                break
            i = i + 1

    if valid == 1:
        total = total + int(expense)
    else:
        print("Invalid input")

print("Total Expense =", total)

