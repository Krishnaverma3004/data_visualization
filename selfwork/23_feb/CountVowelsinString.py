# Program: Check Vowels in String and Count
# Description: Displays a message if the string has no vowels or counts the number of vowels

# Take input from user with validation
while True:
    text = input("Enter a string: ")
    if text == "":
        print("Input cannot be empty. Please enter a valid string.")
    else:
        break

i = 0
vowel_count = 0  # count of vowels

while i < len(text):
    char = text[i]
    
    # manually check if char is a vowel
    if char == 'a' or char == 'A' or char == 'e' or char == 'E' or char == 'i' or char == 'I' or char == 'o' or char == 'O' or char == 'u' or char == 'U':
        vowel_count = vowel_count + 1
    
    i = i + 1

# Display message based on vowel count
if vowel_count == 0:
    print("The string contains NO vowels!")
else:
    print("The string contains", vowel_count, "vowel(s).")