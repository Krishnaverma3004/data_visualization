marks_input = input("Enter marks out of 100: ")

valid = 1
for ch in marks_input:
    valid = valid * ((ch >= '0') * (ch <= '9'))

marks = int(marks_input) * valid

if valid == 1:
    if marks >= 90:
        print("Grade: A")
    elif marks >= 75:
        print("Grade: B")
    elif marks >= 50:
        print("Grade: C")
    else:
        print("Grade: F")
