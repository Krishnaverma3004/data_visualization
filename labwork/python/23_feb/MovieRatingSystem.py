def movie_rating_system():
    # Input ratings as a string
    data = input("Enter movie ratings (1-5) separated by space: ")

    ratings = []
    invalid_ratings = []  # To track invalid ratings
    number = ""

    # -----------------------------------
    # Manual parsing and validation
    # -----------------------------------
    for ch in data:
        if ch != " ":
            number += ch
        else:
            if number != "":
                if number.isdigit():
                    val = int(number)
                    if 1 <= val <= 5:
                        ratings.append(val)
                    else:
                        invalid_ratings.append(val)  # Invalid number
                else:
                    invalid_ratings.append(number)  # Non-numeric
                number = ""
    # Add last number
    if number != "":
        if number.isdigit():
            val = int(number)
            if 1 <= val <= 5:
                ratings.append(val)
            else:
                invalid_ratings.append(val)
        else:
            invalid_ratings.append(number)

    # Check if there are valid ratings
    if len(ratings) == 0:
        print("No valid ratings entered.")
        if invalid_ratings:
            print("Invalid Ratings Entered:", invalid_ratings)
        return

    # -----------------------------------
    # Find average rating
    # -----------------------------------
    total = 0
    for r in ratings:
        total += r
    average = total / len(ratings)

    # -----------------------------------
    # Count number of 5-star ratings
    # -----------------------------------
    five_star_count = 0
    for r in ratings:
        if r == 5:
            five_star_count += 1

    # -----------------------------------
    # Sort ratings (manual bubble sort ascending)
    # -----------------------------------
    for i in range(len(ratings)):
        for j in range(0, len(ratings) - i - 1):
            if ratings[j] > ratings[j + 1]:
                ratings[j], ratings[j + 1] = ratings[j + 1], ratings[j]

    # -----------------------------------
    # Display results
    # -----------------------------------
    print("\nValid Ratings (Ascending):", ratings)
    print(f"Average Rating: {average:.2f}")
    print(f"Number of 5-star Ratings: {five_star_count}")

    if invalid_ratings:
        print("Invalid Ratings Entered:", invalid_ratings)


# Run the system
movie_rating_system()
'''output:
Enter movie ratings (1-5) separated by space: 5 4 3 5 2 6 abc -1
Valid Ratings (Ascending): [2, 3, 4, 5, 5]
Average Rating: 3.80
Number of 5-star Ratings: 2
Invalid Ratings Entered: [6, 'abc', -1]
'''