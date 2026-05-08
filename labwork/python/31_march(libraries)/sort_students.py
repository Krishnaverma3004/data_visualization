def sort_students_by_marks(student_list):
    # Sort list using marks (second value of tuple)
    return sorted(student_list, key=lambda student: student[1])


# ----------- USER INPUT SECTION -----------

student_list = []
size = int(input("Enter number of students: "))

for i in range(size):
    student_name = input("Enter name: ")
    student_marks = int(input("Enter marks: "))
    student_list.append((student_name, student_marks))
print("Sorted List:", sort_students_by_marks(student_list))

'''output:
'''