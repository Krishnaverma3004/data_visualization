#right angled triangle pattern(right aligned)
rows=5
for i in range(1,rows+1):
    print("x"*i)
print("-----------------------------")
#right angled triangle using input from user
rows=int(input("Enter number of rows: "))
if(rows>0):
    for i in range(1,rows+1):
        print("x"*i)

print("-----------------------------")
#right angled triangle pattern(left aligned)
rows=int(input("Enter number of rows: "))
if(rows>0):
    for i in range(1,rows+1):
        print(" "*(rows-i)+"x"*i)
print("-----------------------------")

# triangle pattern
rows=int(input("Enter number of rows: "))
if(rows>0):
    for i in range(1,rows+1):
        print(" "*(rows-i)+"x"*(i*2-1))

# printing diamond pattern

rows=int(input("Enter number of rows: "))
if (rows>0):
    for i in range(1,rows+1):
      print(" "*(rows-i)+"x"*(i*2-1))
    for i in range(rows-1,0,-1):
      print(" "*(rows-i)+"x"*(i*2-1)) 
           
    
#output:
#x
#xx
#xxx
#xxxx
#xxxxx
#-----------------------------
#Enter number of rows: 5
#x
#xx
#xxx
#xxxx
#xxxxx
#-----------------------------
#Enter number of rows: 5
#    x
#   xx
#  xxx
# xxxx
#xxxxx
#-----------------------------
#output of triangle pattern
# Enter number of rows: 5
#    x
#   xxx
#  xxxxx
# xxxxxxx
#xxxxxxxxx
#------------------------------
#output of diamond pattern
#Enter number of rows: 5
#    x
#   xxx
#  xxxxx
# xxxxxxx
#xxxxxxxxx
# xxxxxxx
#  xxxxx
#   xxx
#    x
