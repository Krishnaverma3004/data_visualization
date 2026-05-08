# Problem 86
# Reverse string manually

text = input("Enter a string: ")

if text == "":
    print("Error: String cannot be empty.")
else:
    reversed_text = ""
    i = len(text) - 1

    while i >= 0:
        reversed_text = reversed_text + text[i]
        i -= 1

    print("Reversed String:", reversed_text)

    '''output
    
    Enter a string: hello
Reversed String: olleh'''