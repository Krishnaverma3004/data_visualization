#a list of 5 numbers
list1 =[45,47,89,34,56]
#displaying the list
print("Numbers are: ",list1)
print("-----------------------------")


#creaating a list of 5 names
list2=[23,56,78,90,12]
#to insert list2 in list1 we can use + operator
list1.append(list2)
print("After inserting list2 in list1: ",list1)
print("-----------------------------")


#creating a list of 5 names
list3 = ["23","56","78","90","12"]
list1.extend(list3)
print("After inserting list3 in list1: ",list1)
#insert 240 at index 3 in numbered list
list1.insert(3,240)
print("After inserting 240 at index 3 in list1: ",list1)
#output:
#Numbers are:  [45, 47, 89, 240, 34, 56]
#output:
#After inserting list2 in list1:  [45, 47, 89, 240, 34, 56, [23, 56, 78, 90, 12]]
#output:        
#After inserting list3 in list1:  [45, 47, 89, 240, 34, 56, [23, 56, 78, 90, 12], '23', '56', '78', '90', '12']
#output:
#After inserting 240 at index 3 in list1:  [45, 47, 89, 240, 34, 56, [23, 56, 78, 90, 12], '23', '56', '78', '90', '12']    

