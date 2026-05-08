cp=float (input("Enter the cost Price (in Rs):"))
if(cp<=0):
    print("Invalid cost Price")
    exit()
sp=float(input("Enter the selling Price (in Rs):"))
if(sp<=0):
    print("Invalid selling Price")
    exit()
if(sp>cp):
    print("Profit: Rs",(sp-cp))
elif(cp>sp):
    print("Loss: Rs",(cp-sp))
else:
    print("No profit no loss")

  