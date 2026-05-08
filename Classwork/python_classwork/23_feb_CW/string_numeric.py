sentence = "Hello world"
# .isalnum() returns True if all characters are letters or numbers (no spaces or symbols)
print(sentence.isalnum())  # False, because of the space

str3 = 'hello 123'
# Contains letters, numbers, and a space, so it's not fully alphanumeric
print(str3.isalnum())      # False

str4 = "123"
# Only numbers, which are considered alphanumeric
print(str4.isalnum())      # True
'''#output
False
False
True
'''