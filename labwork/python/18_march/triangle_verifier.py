#program to verify whether three angles can form a triangle or not
#input of three angles
angle1 = float(input("Enter first angle: "))
#validating whether the angle is valid or not   
if(angle1 <= 0):
    print("Invalid angle")  
    exit() #exiting the program if angle is invalid
else:
    angle2 = float(input("Enter second angle: "))
    #validating whether the angle is valid or not
    if(angle2 <= 0):    
        print("Invalid angle")  
        exit() #exiting the program if angle is invalid
    else:
        angle3 = float(input("Enter third angle: "))
        #validating whether the angle is valid or not
        if(angle3 <= 0):
            print("Invalid angle")
            exit() #exiting the program if angle is invalid
        else:
            #verifying whether three angles can form a triangle or not
            if(angle1 + angle2 + angle3 == 180):
                print("The three angles can form a triangle")
            else:
                print("The three angles cannot form a triangle")