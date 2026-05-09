# Q2. Develop a grading system where marks of five subjects are entered by the user. The program should calculate percentage, assign grades using nested if-else conditions, and identify whether the student qualifies for a scholarship.
# Function to calculate percentage and grade
def calculate_grade(marks):
    total_marks = sum(marks)
    percentage = (total_marks / 500) * 100

    if percentage >= 90:
        grade = 'A'
    elif percentage >= 80:
        grade = 'B'
    elif percentage >= 70:
        grade = 'C'
    elif percentage >= 60:
        grade = 'D'
    else:
        grade = 'F'

    return percentage, grade
# Function to check scholarship eligibility
def check_scholarship(percentage):
    if percentage >= 85:
        return "Eligible for scholarship"
    else:
        return "Not eligible for scholarship"       
# Main program
marks = []
for i in range(1, 6):
    mark = float(input(f"Enter marks for subject {i}: "))
    marks.append(mark)
percentage, grade = calculate_grade(marks)
scholarship_status = check_scholarship(percentage)
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(scholarship_status)

#--------------------- output:---------------------
# Enter marks for subject 1: 85
# Enter marks for subject 2: 90
# Enter marks for subject 3: 80
# Enter marks for subject 4: 70
# Enter marks for subject 5: 95
# Percentage: 84.00%
# Grade: B
# Not eligible for scholarship
