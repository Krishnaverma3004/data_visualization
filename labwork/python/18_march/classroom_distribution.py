total_students = int(input("Enter total number of students: "))
students_per_class = int(input("Enter number of students per class: "))

full_classes = total_students // students_per_class
remaining_students = total_students % students_per_class

print("Full classes:", full_classes)
print("Students without class:", remaining_students)


