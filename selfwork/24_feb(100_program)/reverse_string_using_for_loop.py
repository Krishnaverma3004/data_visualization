# Program to reverse a string using for loop

# Input string
while True:
    text = input("Enter a string: ")
    if len(text) > 0:
        break
    else:
        print("String cannot be empty.")

# Reverse string manually
reversed_str = ""
for i in range(len(text)-1, -1, -1):
    reversed_str += text[i]

print("Reversed string:", reversed_str)

'''output
Enter a string: hello there i am python
Reversed string: nohtyp ma i ereht olleh

output2:
Enter a string: 
String cannot be empty.
Enter a string: hello
Reversed string: olleh


'''