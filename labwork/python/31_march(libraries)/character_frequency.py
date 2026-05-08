def calculate_character_frequency(text):
    # Create empty dictionary to store frequency
    frequency = {}

    # Traverse each character in the string
    for index in range(len(text)):
        character = text[index]

        # If character already exists, increase count
        if character in frequency:
            frequency[character] += 1
        else:
            # Otherwise initialize count as 1
            frequency[character] = 1

    # Return the frequency dictionary
    return frequency


# ----------- USER INPUT SECTION -----------

text = input("Enter a string: ")

# Display result
print("Character Frequency:", calculate_character_frequency(text))

'''output:
Enter a string: hello this is python
Character Frequency: {'h': 3, 'e': 1, 'l': 2, 'o': 2, ' ': 3, 't': 2, 'i': 2, 's': 2, 'p': 1, 'y': 1, 'n': 1}'''