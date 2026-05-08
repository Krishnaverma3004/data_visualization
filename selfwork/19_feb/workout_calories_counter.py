total = 0
n = input("Enter number of exercises: ")
valid = 1

if n == "":
    valid = 0
else:
    for ch in n:
        if ch < '0' or ch > '9':
            valid = 0
            break

if valid == 1:
    n = int(n)
    for i in range(1, n + 1):
        cal_input = input("Enter calories burned for exercise " + str(i) + ": ")
        valid_cal = 1
        if cal_input == "":
            valid_cal = 0
        else:
            for ch in cal_input:
                if ch < '0' or ch > '9':
                    valid_cal = 0
                    break
        if valid_cal == 1:
            total = total + int(cal_input)
        else:
            print("Invalid calories counted as 0")
    print("Total Calories Burned =", total)
else:
    print("Invalid number of exercises")
