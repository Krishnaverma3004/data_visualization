#creating a numeric list 
number =[45,47,89,34,56]
#displaying list 
print("Numbers are in this  way",number)

#displaying list without square brakets
print("Numbers are")
print(*number)
#------------------------------


##displaying elements by using for loop 
print("-----------------------------")
print("Numbers are")
for num in number:
    print(num)


#displaying element in reverse order by using forward index
length =len(number)
print ("Number in reverse order:")
for index in range(length-1,-1,-1):
    print(number[index],end=',')
#----------------------------------


# finding sum of all elements
sum=0
for num in number:
    sum=sum+num
print("Sum of all the number in list ",sum)


#finding the greatest number in list
max=number[0]
for index in range(1,length):
    if(max<number[index]):
        max=number[index]
print("Greatest number in list: ",max)        
#output of creating a numeric list:
#Numbers are in this  way [45, 47, 89, 34, 56]
#------------------------------
#displaying list without square brakets
#Numbers are    
#45 47 89 34 56
#----------------------------- 
# displaying elements by using for loop   
# output:
#Numbers are    45  47  89  34  56  
# -----------------------------
# displaying element in reverse order by using forward index
# output:
#Number in reverse order: 
# 56,34,89,47,45,     
# -----------------------------
# finding sum of all elements
# output:
# Sum of all the number in list  271 