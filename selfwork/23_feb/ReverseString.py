# Program: Reverse String 


# take input from user
text = input("Enter a string to reverse: ")

reversed_text = ""  # start with empty string
index = 0

# count length manually
length = 0
for char in text:
    length = length + 1

index = length - 1

# iterate backwards manually
while index >= 0:
    reversed_text = reversed_text + text[index]
    index = index - 1

print("Original string:", text)
print("Reversed string:", reversed_text)

''' Output
Enter a string to reverse: Hello this is Python
Original string: Hello this is Python
Reversed string: nohtyP si siht olleH'''