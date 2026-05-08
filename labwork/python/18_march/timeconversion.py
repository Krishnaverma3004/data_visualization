#input of time in seconds 
second=int(input("Enter time in seconds"))
minute=0
hour=0
#condition checking for hsecond to hour conversion
if(second>=3600):
    hour=second//3600
    second=second%3600
#checking condition for conversion of seconds into minutes
if(second>=60):
    minute=second//60
    second=second%60  
    #printing the conversion
print("Time in hours: ",hour)    
print("Time in minutes: ",minute)    
print("Time in seconds: ",second)      
