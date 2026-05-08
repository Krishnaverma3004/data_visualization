
# Problem 100
# Compress string using character counts

text = input("Enter a string: ")

if text == "":
    print("Error: Input cannot be empty.")
else:
    compressed = ""
    count = 1
    i = 1

    while i <= len(text):
        if i < len(text) and text[i] == text[i - 1]:
            count += 1
        else:
            compressed += text[i - 1] + str(count)
            count = 1
        i += 1

    print("Compressed string:", compressed)


    '''output
    Enter a string: aaabbc
Compressed string: a3b2c1
    '''