set1={45,67,89,45,67,89,34,90,45,59,120,34,90,45,59,120}
print("The set is: ")
print(set1)
#to insert 34 in set
set1.add(34)
print("The set after adding 34 is: ")
print(set1)

#-------------------------------
#creating an empty set
set4=set()
print(type(set4))
set4.add(45)
set4.add(67)
print(set4)




'''output:

The set is:
{34, 67, 89, 45, 120, 90, 59}

The set after adding 34 is:
{34, 67, 89, 45, 120, 90, 59}


output:
<class 'set'>
{67, 45}

'''