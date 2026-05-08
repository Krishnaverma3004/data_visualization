# Problem 14: Check whether character is digit or alphabet
ch = input("Enter a single character: ")

# Step 1: Validate single character
if len(ch) != 1:
    print("Invalid Input")
else:
    c = ch
    # Step 2: Check  if digit
    if c >= '0' and c <= '9':
        print("Digit")
    # Step 3: Check if alphabet
    elif (c >= 'A' and c <= 'Z') or (c >= 'a' and c <= 'z'):
        print("Alphabet")
    else:
        print("Invalid Input")
'''output1:
Enter a single character: 5
Digit

output2:
Enter a single character: a
Alphabet

output 3:
Enter a single character:  
Invalid Input
'''        