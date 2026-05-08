# Problem 95
# Remove duplicate characters

text = input("Enter a string: ")

if text == "":
    print("Error: Input cannot be empty.")
else:
    result = ""
    i = 0

    while i < len(text):
        ch = text[i]
        if ch not in result:
            result += ch
        i += 1

    print("String without duplicates:", result)


    '''output

    Enter a string: programming
String without duplicates: progamin
    '''