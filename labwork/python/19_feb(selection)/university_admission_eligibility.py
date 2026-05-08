# Input marks and subjects
percentage = float(input("Enter 12th grade percentage: "))

if percentage < 0 or percentage > 100:
    print("Invalid percentage. Program terminated.")
else:
    subject_math = input("Did you study Mathematics? (yes/no): ")
    
    if subject_math != "yes" and subject_math != "no":
        print("Invalid input for Mathematics. Program terminated.")
    else:
        exam_score = float(input("Enter entrance exam score: "))
        
        if exam_score < 0 or exam_score > 100:
            print("Invalid exam score. Program terminated.")
        else:
            # Check eligibility conditions
            if percentage < 75:
                print("Not eligible: 12th grade percentage less than 75%.")
            elif subject_math != "yes":
                print("Not eligible: Must have studied Mathematics.")
            elif exam_score < 80:
                print("Not eligible: Entrance exam score less than 80.")
            else:
                print("Congratulations! You are eligible for admission.")
