# Problem 13: Check whether a character is vowel or consonant
ch = input("Enter a single alphabet character: ")

# Step 1: Validate input length and alphabet manually
if len(ch) != 1:
    print("Invalid Input")
else:
    c = ch
    # Check uppercase A-Z or lowercase a-z
    if (c < 'A' or (c > 'Z' and c < 'a') or c > 'z'):
        print("Invalid Input")
    else:
        # Step 2: Check manually for vowels
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u' or \
           c == 'A' or c == 'E' or c == 'I' or c == 'O' or c == 'U':
            print("Vowel")
        else:
            print("Consonant")
'''output
Enter a single alphabet character: a
Vowel

output2:
Enter a single alphabet character: abs
Invalid Input

output3:
Enter a single alphabet character: v
Consonant
'''            