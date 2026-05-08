# Problem 88
# Count words in sentence manually

sentence = input("Enter a sentence: ")

if sentence == "":
    print("Error: Input cannot be empty.")
else:
    count = 0
    in_word = False
    i = 0

    while i < len(sentence):
        if sentence[i] != ' ' and not in_word:
            count += 1
            in_word = True
        elif sentence[i] == ' ':
            in_word = False
        i += 1

    print("Number of words:", count)
    '''output

    Enter a sentence: I love Python
Number of words: 3    '''