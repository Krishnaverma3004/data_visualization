correct_username = "admin"
correct_password = "1234"
attempts = 0

while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username != correct_username:
        print("Invalid username.")
    elif password != correct_password:
        print("Invalid password.")
    else:
        print("Login successful!")
        break

    attempts = attempts + 1

    if attempts == 3:
        print("Account locked due to 3 failed attempts.")
