# Problem 99
# Generate all substrings

text = input("Enter a string: ")

if text == "":
    print("Error: Input cannot be empty.")
else:
    print("Substrings:")
    i = 0
    while i < len(text):
        j = i + 1
        while j <= len(text):
            print(text[i:j])
            j += 1
        i += 1

        '''output
        Enter a string: abc
Substrings:
a
ab
abc
b
bc
c

        '''