# Program to validate username and password without using predefined functions

# Username and password rules:
# Username: at least 3 characters, only letters and digits
# Password: at least 6 characters

# Function to check if a string contains only letters and digits
def is_alnum_manual(s):
    for char in s:
        if not ((ord('a') <= ord(char) <= ord('z')) or
                (ord('A') <= ord(char) <= ord('Z')) or
                (ord('0') <= ord(char) <= ord('9'))):
            return False
    return True

# Input validation for username
while True:
    username = input("Enter username (min 3 chars, letters/digits only): ")
    if len(username) >= 3 and is_alnum_manual(username):
        break
    else:
        print("Invalid username. Try again.")

# Input validation for password
while True:
    password = input("Enter password (min 6 chars): ")
    if len(password) >= 6:
        break
    else:
        print("Password too short. Try again.")

print("Username and password are valid!")

'''output
Enter username (min 3 chars, letters/digits only): admin
Enter password (min 6 chars): 123@m
Password too short. Try again.
Enter password (min 6 chars): Mins@223
Username and password are valid!
'''