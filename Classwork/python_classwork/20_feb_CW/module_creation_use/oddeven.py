from numeric_calculation import calculate_remainder
num=int(input("Enter a number: "))
if(calculate_remainder(num,2)==0):
    print(num,"is a even number")
else:
    print(num,"is an odd number")    

'''output:
Enter a number: 10
10 is a even number
Enter a number: 15
15 is an odd number'''