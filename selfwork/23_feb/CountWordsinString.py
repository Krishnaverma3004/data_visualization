# Program: Count Words in String 


# Take input from user
text = input("Enter a string: ")

count = 0  # initialize word count
in_word = False  # flag to track if we are inside a word

i = 0
while i < len(text):
    char = text[i]
    # If character is not a space, we are inside a word
    if char != " ":
        if not in_word:
            count = count + 1  # new word found
            in_word = True
    else:
        in_word = False  # we hit a space, so we are outside a word
    i = i + 1

print("Number of words in the string:", count)

''' Output
Enter a string: Hello world this is Python
Number of words in the string: 6

'''