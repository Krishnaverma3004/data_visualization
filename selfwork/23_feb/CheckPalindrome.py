# Program: Check Palindrome (User Input with Validation)
# Description: Checks if a string is a palindrome manually, case-insensitive

# Take input from user with validation
while True:
    text = input("Enter a string to check for palindrome: ")
    if text == "":
        print("Input cannot be empty. Please enter a valid string.")
    else:
        break

# Convert all characters to lowercase manually for case-insensitive check
lower_text = ""
i = 0
while i < len(text):
    char = text[i]
    # manually convert uppercase letters to lowercase
    if 'A' <= char <= 'Z':
        lower_char = chr(ord(char) + 32)  # 'A'->'a', 'B'->'b', etc.
    else:
        lower_char = char
    lower_text = lower_text + lower_char
    i = i + 1

# manually reverse the string
reversed_text = ""
length = 0
for char in lower_text:
    length = length + 1

i = length - 1
while i >= 0:
    reversed_text = reversed_text + lower_text[i]
    i = i - 1

# compare original and reversed
if lower_text == reversed_text:
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")

''' Output
Enter a string to check for palindrome: Madam
The string is a palindrome

Enter a string to check for palindrome: Hello
The string is not a palindrome

Enter a string to check for palindrome
Input cannot be empty. Please enter a valid string.
Enter a string to check for palindrome: A man a plan a canal Panama
The string is a palindrome'''    