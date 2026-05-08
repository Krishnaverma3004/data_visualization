# Problem 89
# Find frequency of each character in string

text = input("Enter text: ")

if text == "":
    print("Error: Input cannot be empty.")
else:
    freq = {}

    i = 0
    while i < len(text):
        ch = text[i]

        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

        i += 1

    print("Character Frequencies:")
    for key in freq:
        print(key, ":", freq[key])
'''output
Enter text: apple
Character Frequencies:
a : 1
p : 2
l : 1
e : 1
        '''