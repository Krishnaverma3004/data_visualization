# Q1. Write a Python program that accepts a paragraph from the user and calculates the number of uppercase letters, lowercase letters, digits, spaces, and special characters. Display the result in descending order based on frequency.
text = input("Enter a paragraph: ")

counts = {
    "Uppercase": sum(1 for c in text if c.isupper()),
    "Lowercase": sum(1 for c in text if c.islower()),
    "Digits": sum(1 for c in text if c.isdigit()),
    "Spaces": sum(1 for c in text if c.isspace()),
    "Special": sum(1 for c in text if not (c.isalnum() or c.isspace()))
}

# Sort by count (value) descending
for k, v in sorted(counts.items(), key=lambda x: x[1], reverse=True):
    print(f"{k}: {v}")

#--------------------- output:---------------------
# Enter a paragraph: Hello World! 123         
# Lowercase: 8
# Spaces: 5
# Uppercase: 2
# Digits: 3
# Special: 1