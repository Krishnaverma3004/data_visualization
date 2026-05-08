marks_input = input("Enter marks out of 100: ")

valid = 1
for ch in marks_input:
    valid = valid * ((ch >= '0') * (ch <= '9'))

marks = int(marks_input) * valid

if valid == 1:
    if marks >= 40:
        print("You passed")
    else:
        print("You failed")
