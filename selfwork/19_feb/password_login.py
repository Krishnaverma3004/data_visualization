correct = "1234"
attempts = 0

while attempts < 3:
    password = input("Enter password: ")

    if password == correct:
        print("Login Successful")
        break
    else:
        print("Wrong Password")
        attempts = attempts + 1

if attempts == 3:
    print("Account Locked")
