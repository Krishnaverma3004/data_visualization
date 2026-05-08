# Problem 87
# Check whether string is palindrome

text = input("Enter a string: ")

if text == "":
    print("Error: String cannot be empty.")
else:
    reversed_text = ""
    i = len(text) - 1

    while i >= 0:
        reversed_text = reversed_text + text[i]
        i -= 1

    if text == reversed_text:
        print("The string is a Palindrome.")
    else:
        print("The string is NOT a Palindrome.")

        '''output:
        Enter a string: madam
The string is a Palindrome.
        '''