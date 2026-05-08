# -------------------------------------------------------
# Temperature Monitoring System
# - Find hottest and coldest temperature
# - Replace temperature > 45 with "Heat Alert"
# - Count extreme days (> 40)
# - No split(), no max(), no min()
# -------------------------------------------------------

def temperature_monitoring():

    # Take full input string
    data = data = "38 42 45 47 39 41 46"

    temperatures = []
    number = ""

    # -----------------------------------
    # Manual parsing (no split)
    # -----------------------------------
    for i in range(len(data)):

        if data[i] != " ":
            number = number + data[i]
        else:
            # Manual digit validation
            valid = True
            for ch in number:
                if ch < '0' or ch > '9':
                    valid = False

            if valid and number != "":
                temperatures.append(int(number))

            number = ""

    # Add last number
    valid = True
    for ch in number:
        if ch < '0' or ch > '9':
            valid = False

    if valid and number != "":
        temperatures.append(int(number))

    # -----------------------------------
    # Check if data exists
    # -----------------------------------
    if len(temperatures) == 0:
        print("No valid temperature data entered.")
        return

    # -----------------------------------
    # Find hottest and coldest manually
    # -----------------------------------
    hottest = temperatures[0]
    coldest = temperatures[0]

    for i in range(1, len(temperatures)):
        if temperatures[i] > hottest:
            hottest = temperatures[i]

        if temperatures[i] < coldest:
            coldest = temperatures[i]

    # -----------------------------------
    # Count extreme days (> 40)
    # Replace > 45 with "Heat Alert"
    # -----------------------------------
    extreme_days = 0

    for i in range(len(temperatures)):

        if temperatures[i] > 40:
            extreme_days = extreme_days + 1

        if temperatures[i] > 45:
            temperatures[i] = "Heat Alert"

    # -----------------------------------
    # Display results
    # -----------------------------------
    print("\nHottest Temperature:", hottest)
    print("Coldest Temperature:", coldest)
    print("Number of Extreme Days (>40°C):", extreme_days)
    print("Updated Temperature List:", temperatures)

    '''output:
    Enter daily temperatures separated by space: 38 42 45 47 39 41 46
    Hottest Temperature: 47
    Coldest Temperature: 38
    Number of Extreme Days (>40°C): 5
    Updated Temperature List: [38, 42, 45, 'Heat Alert', 39, 41, 'Heat Alert']
    '''