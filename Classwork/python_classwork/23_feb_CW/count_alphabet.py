sentence=input("Enter a sentence: ")
#to count number of  alphabets in the sentence
count=0
for x in sentence:
    if x.isalpha():
        count += 1
print("Number of alphabets:", count)

'''#output
Enter a sentence: Hello world 123
Number of alphabets: 10
'''