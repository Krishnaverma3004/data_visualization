# Check if string is numeric with optional decimal
def is_numeric_float_manual(s):
    dot_count = 0
    for char in s:
        if char == '.':
            dot_count += 1
            if dot_count > 1:
                return False
        elif not ('0' <= char <= '9'):
            return False
    return len(s) > 0

# Step 1: Weight input
while True:
    weight_str = input("Enter weight in kg: ")
    if is_numeric_float_manual(weight_str):
        # Convert manually to float
        weight = 0
        frac = 0
        decimal = False
        for char in weight_str:
            if char == '.':
                decimal = True
                frac = 0.1
            elif not decimal:
                weight = weight * 10 + (ord(char) - ord('0'))
            else:
                weight += (ord(char) - ord('0')) * frac
                frac /= 10
        if weight > 0:
            break
        else:
            print("Weight must be positive.")
    else:
        print("Enter numeric value only.")

# Step 2: Height input
while True:
    height_str = input("Enter height in meters: ")
    if is_numeric_float_manual(height_str):
        # Convert manually to float
        height = 0
        frac = 0
        decimal = False
        for char in height_str:
            if char == '.':
                decimal = True
                frac = 0.1
            elif not decimal:
                height = height * 10 + (ord(char) - ord('0'))
            else:
                height += (ord(char) - ord('0')) * frac
                frac /= 10
        if height > 0:
            break
        else:
            print("Height must be positive.")
    else:
        print("Enter numeric value only.")

# BMI calculation and category
bmi = weight / (height * height)
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal weight")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")


'''output1:
Enter weight in kg: 45
Enter height in meters: abc
Invalid input. Enter numeric values only.

output2:Enter weight in kg: 34
Enter height in meters: 44
Underweight
'''    