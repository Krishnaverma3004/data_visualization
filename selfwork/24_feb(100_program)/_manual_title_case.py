# Problem 91
# Convert string to title case manually

text = input("Enter a sentence: ")

if text == "":
    print("Error: Input cannot be empty.")
else:
    result = ""
    new_word = True
    i = 0

    while i < len(text):
        ch = text[i]

        if ch == " ":
            result += ch
            new_word = True
        else:
            if new_word and 'a' <= ch <= 'z':
                result += chr(ord(ch) - 32)  # convert to uppercase
                new_word = False
            else:
                result += ch
                new_word = False
        i += 1

    print("Title Case:", result)

    '''output
    Enter a sentence: hello world
Title Case: Hello World
    '''