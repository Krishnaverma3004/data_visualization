# Create student marks dictionary manually

students = {}
print("Enter student name and marks (type n to stop):")

while True:
    name = input("Student Name: ")
    if name.lower() == "n":
        if len(students) == 0:
            print("At least one student required.")
            continue
        break

    marks = input("Marks: ")

    # Validate marks
    valid = True
    i = 0
    while i < len(marks):
        if marks[i] < '0' or marks[i] > '9':
            valid = False
        i += 1

    if not valid or marks == "":
        print("Invalid marks! Enter numeric value.")
        continue

    students[name] = int(marks)

# Find topper manually
top_name = ""
top_marks = -1

for key in students:
    if students[key] > top_marks:
        top_marks = students[key]
        top_name = key

print("Topper:", top_name)
print("Marks:", top_marks)
'''output
Enter student name and marks (type n to stop):     
Student Name: khushi
Marks: 98
Student Name: raj
Marks: 99
Student Name: n
Topper: raj
Marks: 99
'''