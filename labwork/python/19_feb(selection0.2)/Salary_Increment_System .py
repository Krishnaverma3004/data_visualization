performance = int(input("Enter performance rating (1-5): "))
experience = int(input("Enter years of experience: "))
attendance = float(input("Enter attendance percentage: "))

if performance < 1 or performance > 5 or experience < 0 or attendance < 0 or attendance > 100:
    print("Invalid input. Program terminated.")
else:
    increment = 0

    # Performance-based increment
    if performance == 5:
        increment = 20
    elif performance == 4:
        increment = 15
    elif performance == 3:
        increment = 10
    elif performance == 2:
        increment = 5
    else:
        increment = 0

    # Add experience bonus
    if experience >= 10:
        increment = increment + 5

    # Add attendance bonus
    if attendance >= 95:
        increment = increment + 5

    print("Total salary increment percentage:", increment, "%")
