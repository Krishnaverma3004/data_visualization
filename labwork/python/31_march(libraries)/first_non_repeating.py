def find_first_non_repeating(text):
    # Dictionary to store frequency
    frequency = {}

    # Count frequency of each character
    for index in range(len(text)):
        character = text[index]

        if character in frequency:
            frequency[character] += 1
        else:
            frequency[character] = 1

    # Find first character with frequency 1
    for index in range(len(text)):
        if frequency[text[index]] == 1:
            return text[index]

    return None


# ----------- USER INPUT SECTION -----------

text = input("Enter string: ")

print("First Non-Repeating Character:", find_first_non_repeating(text))

'''output:
Enter string: this is a lab
First Non-Repeating Character: t
'''