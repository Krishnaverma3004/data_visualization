# -------------------------------------------------------
# Attendance Tracker (3 Decimal Precision Version)
# - Calculates attendance percentage (3 decimal places)
# - Identifies below 75%
# - Marks consecutive absences as "Warning"
# - No split() used
# - Only len() allowed
# -------------------------------------------------------

def attendance_tracker():

    # Take input as full string
    data = input("Enter attendance (1 for present, 0 for absent, separated by space): ")

    attendance = []
    number = ""

    # -----------------------------------
    # Manual parsing (no split)
    # -----------------------------------
    for i in range(len(data)):

        if data[i] != " ":
            number = number + data[i]
        else:
            if number == "0" or number == "1":
                attendance.append(int(number))
            number = ""

    # Add last number
    if number == "0" or number == "1":
        attendance.append(int(number))

    # -----------------------------------
    # Check valid input
    # -----------------------------------
    if len(attendance) == 0:
        print("No valid attendance data entered.")
        return

    # -----------------------------------
    # Calculate attendance percentage
    # -----------------------------------
    total_days = len(attendance)
    present_days = 0

    for i in range(len(attendance)):
        present_days = present_days + attendance[i]

    percentage = (present_days * 100) / total_days

    # Format to 3 decimal places
    formatted_percentage = format(percentage, ".3f")

    print("\nAttendance Percentage:", formatted_percentage, "%")

    # -----------------------------------
    # Identify below 75%
    # -----------------------------------
    if percentage < 75:
        print("Status: Below 75% - Attendance Warning")
    else:
        print("Status: Good Attendance")

    # -----------------------------------
    # Create updated list
    # -----------------------------------
    updated_attendance = []

    i = 0
    while i < len(attendance):

        if i < len(attendance) - 1 and attendance[i] == 0 and attendance[i + 1] == 0:
            updated_attendance.append("Warning")
            updated_attendance.append("Warning")
            i = i + 2
        else:
            updated_attendance.append(attendance[i])
            i = i + 1

    # -----------------------------------
    # Display updated record
    # -----------------------------------
    print("Updated Attendance Record:", updated_attendance)


'''output:
Enter attendance (1 for present, 0 for absent, separated by space): 1 0 1 0 0 1 1
Attendance Percentage: 66.667 %
Status: Below 75% - Attendance Warning
Updated Attendance Record: [1, 'Warning', 'Warning', 1, 1]
'''