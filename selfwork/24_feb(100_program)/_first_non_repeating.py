# Problem 96
# Find first non-repeating character

text = input("Enter a string: ")

if text == "":
    print("Error: Input cannot be empty.")
else:
    freq = {}

    # Count frequency
    i = 0
    while i < len(text):
        ch = text[i]
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
        i += 1

    # Find first non-repeating
    i = 0
    found = False
    while i < len(text):
        if freq[text[i]] == 1:
            print("First non-repeating character:", text[i])
            found = True
            break
        i += 1

    if not found:
        print("No non-repeating character found.")


        '''output
        Enter a string: swiss
First non-repeating character: w
        '''