#creating a blank list
list = []
#to ask user for number of elements in list
n = int(input("Enter number of elements in list: "))
#to ask user to input elements in list
for i in range(n):
    num = int(input())
    print("--------------------------")
    #appending number in list
    list.append(num)
    #displaying list after appending number
    print("List after appending number is: ")
    print(list)
    #to find sum of all elements in list
sum = 0
for i in list:
    sum += i
print("Sum of all elements in list is: ",sum)
#output:
#Enter number of elements in list: 5        
#45
#-----------------------------
#List after appending number is:       
#[45]
#47     
#-----------------------------
#List after appending number is:    
#[45, 47]
#89
#-----------------------------  
#List after appending number is:
#[45, 47, 89]
#34
#-----------------------------
#List after appending number is:
#[45, 47, 89, 34]
#56
#-----------------------------
#List after appending number is:
#[45, 47, 89, 34, 56]
#Sum of all elements in list is:  271
