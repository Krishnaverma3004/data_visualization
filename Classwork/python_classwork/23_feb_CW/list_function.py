# ------------------------
#List function in python
#-------------------------
#count(x) - returns the number of times x appears in the list
#reverse(x) - reverses the order of the list
#create a list of 20 numbers given by user

numbers = []

# Take 20 numbers from user
print("Enter 20 numbers:")
for i in range(20):
    num = int(input(" "))
    numbers.append(num)
#display the list
print("--------------------------------")
print()
remove_num = int(input("Enter a number to remove from the list: "))
#------------------------------------------
print("List is :")
print(numbers)
print("--------------------------------")
#frequency of the number in the list
frequency = numbers.count(remove_num)
if(frequency == 0):
    print(remove_num, " not present in the list.")
elif(frequency == 1):
    print("As it is unique so ,cannot be removed")
else:
    # to reverse the list
     numbers.reverse() 

     for i in range(1,frequency):
          numbers.remove(remove_num)
          #again reverse the list to maintain the original order
          numbers.reverse()
print("The list after removing ", remove_num, " is: ")
print(numbers)
'''output:
Enter 20 numbers:
 7
 9
 7
 6
 6
 4
 4
 5
 6
 6
 8
 4
 4
 5
 3
 3
 5
 5
 3
 4
--------------------------------

Enter a number to remove from the list: 7
List is :
[7, 9, 7, 6, 6, 4, 4, 5, 6, 6, 8, 4, 4, 5, 3, 3, 5, 5, 3, 4]
--------------------------------
The list after removing  7  is:
[7, 9, 6, 6, 4, 4, 5, 6, 6, 8, 4, 4, 5, 3, 3, 5, 5, 3, 4]



#output2:
# Enter 20 numbers:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# 11
# 12
# 13
# 14
# 15
# 16
# 17
# 18
# 19
# 20
# --------------------------------
# Enter a number to remove from the list: 21
# List is :
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
# The number you entered is not in the list.'''