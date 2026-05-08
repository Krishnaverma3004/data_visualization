rows = int(input("Enter rows: "))

for i in range(rows, 0, -1):
    print(" " * (rows - i) + "*" * i)


#output:
#Enter rows: 6
#******
# *****
#  ****
#   ***
#    **
#     *
