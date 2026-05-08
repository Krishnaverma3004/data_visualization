# Function to check palindrome
def is_palindrome(s):
    i, j = 0, len(s)-1
    while i < j:
        if s[i] != s[j]: return False
        i += 1
        j -= 1
    return True

# Input validation
while True:
    s = input("Enter string: ")
    if len(s) > 0: break
    else: print("String cannot be empty.")

print("Palindrome" if is_palindrome(s) else "Not palindrome")
'''output:
Enter string: hello world
Not palindrome


output:
Enter string: mom
Palindrome
'''