total = 0

# Input number of students
n = input("Enter number of students: ")
valid = 1

# Validate input
if n == "":
    valid = 0
else:
    for ch in n:
        if ch < '0' or ch > '9':
            valid = 0
            break

if valid == 1:
    n = int(n)

    # Input marks for each student
    for i in range(1, n + 1):

        # Validate marks until proper value
        marks_input = input("Enter marks for student " + str(i) + ": ")
        valid_marks = 1

        if marks_input == "":
            valid_marks = 0
        else:
            for ch in marks_input:
                if ch < '0' or ch > '9':
                    valid_marks = 0
                    break

        if valid_marks == 1:
            marks = int(marks_input)

            # Check for non-negative marks
            if marks >= 0:
                total = total + marks
            else:
                print("Marks cannot be negative. Counting as 0.")
        else:
            print("Invalid marks entered. Counting as 0.")

    # Compute average
    average = total / n
    print("Average marks =", average)

else:
    print("Invalid number of students")
