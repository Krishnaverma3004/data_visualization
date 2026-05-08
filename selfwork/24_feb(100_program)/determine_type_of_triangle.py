# Function to check if input string is numeric
def is_numeric_manual(s):
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    return True

# Input sides manually
while True:
    a_str = input("Enter side a: ")
    b_str = input("Enter side b: ")
    c_str = input("Enter side c: ")
    if is_numeric_manual(a_str) and is_numeric_manual(b_str) and is_numeric_manual(c_str):
        a = int(a_str)
        b = int(b_str)
        c = int(c_str)
        if a > 0 and b > 0 and c > 0:
            break
        else:
            print("Sides must be positive numbers.")
    else:
        print("Invalid input. Enter numeric values only.")

# Check triangle type
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Equilateral triangle")
    elif a == b or b == c or a == c:
        print("Isosceles triangle")
    else:
        print("Scalene triangle")
else:
    print("Not a valid triangle")

'''output
Enter side a: 34
Enter side b: 3
Enter side c: 44
Not a valid triangle

output2:
Enter side a: 45
Enter side b: 56
Enter side c: 55
Scalene triangle
'''    