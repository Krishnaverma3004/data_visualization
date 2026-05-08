# -------------------------------------------------------
# Sports Tournament Points Table (Optimized)
# - Replace negative points with 0
# - Sort leaderboard in descending order
# - Find winner and runner-up
# - No split(), no sort(), no max()
# -------------------------------------------------------

def sports_tournament():

    data = input("Enter team points separated by space: ")

    points = []
    number = ""

    # -----------------------------------
    # Manual parsing
    # -----------------------------------
    for i in range(len(data)):

        if data[i] != " ":
            number = number + data[i]
        else:
            if number != "":
                valid = True
                start = 0

                if number[0] == '-':
                    start = 1

                for j in range(start, len(number)):
                    if number[j] < '0' or number[j] > '9':
                        valid = False
                        break

                if valid and number != "-":
                    value = int(number)

                    if value < 0:
                        value = 0

                    points.append(value)

            number = ""

    # Add last number
    if number != "":
        valid = True
        start = 0

        if number[0] == '-':
            start = 1

        for j in range(start, len(number)):
            if number[j] < '0' or number[j] > '9':
                valid = False
                break

        if valid and number != "-":
            value = int(number)

            if value < 0:
                value = 0

            points.append(value)

    # -----------------------------------
    # Check empty list
    # -----------------------------------
    if len(points) == 0:
        print("No valid points entered.")
        return

    # -----------------------------------
    # Bubble Sort (Descending)
    # -----------------------------------
    for i in range(len(points)):
        for j in range(0, len(points) - 1 - i):
            if points[j] < points[j + 1]:
                temp = points[j]
                points[j] = points[j + 1]
                points[j + 1] = temp

    # -----------------------------------
    # Winner and Runner-Up
    # -----------------------------------
    winner = points[0]

    if len(points) > 1:
        runner_up = points[1]
    else:
        runner_up = "None"

    # -----------------------------------
    # Output
    # -----------------------------------
    print("\nSorted Leaderboard (High to Low):", points)
    print("Winner Points:", winner)
    print("Runner-Up Points:", runner_up)

    '''output:
    Enter team points separated by space: 10 -5 20 15  25
    Sorted Leaderboard (High to Low): [25, 20, 15, 10, 0]
    Winner Points: 25
    Runner-Up Points: 20
    
    '''