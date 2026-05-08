# Function to count vowels
def count_vowels(s):
    vowels = "aeiouAEIOU"
    c = 0
    for ch in s:
        if ch in vowels: c += 1
    return c

# Input validation
while True:
    s = input("Enter string: ")
    if len(s) > 0: break
    else: print("String cannot be empty.")

print("Vowels:", count_vowels(s))

'''output
Enter string: hello india
Vowels: 5
'''