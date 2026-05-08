# Problem 92
# Find longest word manually

text = input("Enter a sentence: ")

if text == "":
    print("Error: Input cannot be empty.")
else:
    longest = ""
    current = ""
    i = 0

    while i < len(text):
        if text[i] != " ":
            current += text[i]
        else:
            if len(current) > len(longest):
                longest = current
            current = ""
        i += 1

    # Check last word
    if len(current) > len(longest):
        longest = current

    print("Longest word:", longest)

    '''output
    Enter a sentence: I love programming
Longest word: programming
    '''