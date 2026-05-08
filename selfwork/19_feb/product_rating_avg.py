total = 0
n = input("Enter number of users: ")
valid = 1

if n == "":
    valid = 0
else:
    for ch in n:
        if ch < '0' or ch > '9':
            valid = 0
            break

if valid == 1:
    n = int(n)
    for i in range(1, n + 1):
        rating_input = input("Enter rating (1-5) for user " + str(i) + ": ")
        valid_rating = 1
        if rating_input == "":
            valid_rating = 0
        else:
            for ch in rating_input:
                if ch < '0' or ch > '9':
                    valid_rating = 0
                    break
        if valid_rating == 1:
            rating = int(rating_input)
            if rating >= 1 and rating <= 5:
                total = total + rating
            else:
                print("Rating out of range counted as 0")
        else:
            print("Invalid rating counted as 0")
    average = total / n
    print("Average Rating =", average)
else:
    print("Invalid number of users")
