# -------------------------------------------------------
# Function to check if a given string contains only digits
# -------------------------------------------------------
def is_number(value):

    if value == "":
        return False

    for ch in value:
        if ch < '0' or ch > '9':
            return False

    return True


# -------------------------------------------------------
# Student Marks Analyzer (Optimized)
# -------------------------------------------------------
def student_marks_analyzer():

    data = input("Enter student marks separated by space: ").split()

    marks = []

    # Validate numbers
    for item in data:
        if is_number(item):
            marks.append(int(item))

    # Filter valid range (0–100)
    valid_marks = []

    for m in marks:
        if m >= 0 and m <= 100:
            valid_marks.append(m)

    if len(valid_marks) == 0:
        print("No valid marks found.")
        return

    # -----------------------------------
    # Manual total and max
    # -----------------------------------
    total = 0
    topper = valid_marks[0]

    for m in valid_marks:
        total = total + m
        if m > topper:
            topper = m

    count = len(valid_marks)
    avg = total / count

    # -----------------------------------
    # Display results
    # -----------------------------------
    print("\nValid Marks:", valid_marks)
    print("Average Marks:", round(avg, 2))

    print("Topper(s):", end=" ")
    for m in valid_marks:
        if m == topper:
            print(m, end=" ")
    print()

    # Grade logic
    if avg >= 90:
        grade = "A"
    elif avg >= 75:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 40:
        grade = "D"
    else:
        grade = "F"

    print("Grade:", grade)
    '''output:
    Enter student marks separated by space: 85 92 78 88 95 102 -5 
    Valid Marks: [85, 92, 78, 88, 95]
    Average Marks: 87.6
    Topper(s): 95
    Grade: A
    '''
