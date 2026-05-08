# Input list
lst = []
print("Enter numbers one by one (0 to stop):")
while True:
    s = input("Number: ")
    if all('0' <= c <= '9' for c in s) and s != "":
        n = int(s)
        if n == 0:
            if len(lst) == 0:
                print("List cannot be empty.")
                continue
            break
        lst += [n]
    else:
        print("Invalid input!")

# Check palindrome manually using two-pointer approach
i = 0
j = len(lst) - 1
is_palindrome = True
while i < j:
    if lst[i] != lst[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1

if is_palindrome:
    print("The list is a palindrome.")
else:
    print("The list is not a palindrome.")

'''output:
Enter numbers one by one (0 to stop):
Number: 34
Number: 33
Number: 44
Number: 33
Number: 22
Number: 0
The list is not a palindrome.
   ''' 