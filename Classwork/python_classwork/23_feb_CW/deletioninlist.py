#create a list of 10 elements with repeated numbers
number=[45,67,89,45,23,67,89,45,23,67]
#displaying the list
print("The list is: ")
print(number)
print("---------------------------------------")
#to delete the element from index 5
number.pop(5)
print("The list after deleting the element at index 5 is: ")
print(number)
number.pop()
print("The list after deleting the last element is: ")
print(number)
print("----------------------------------")
#to delete 45
number.remove(45)
print("The list after deleting the first occurrence of 45 is: ")
print(number)


'''output:
The list is: 
[45, 67, 89, 45, 23, 67, 89, 45, 23, 67]
---------------------------------------
The list after deleting the element at index 5 is: 
[45, 67, 89, 45, 23, 89, 45, 23, 67]
The list after deleting the last element is: 
[45, 67, 89, 45, 23, 89, 45, 23]
 ---------------------------------------
The list after deleting the first occurrence of 45 is:  
[67, 89, 45, 23, 89, 45, 23]
'''