print("Triangle Validator Program")
print("---------------------------")

try:
    side1 = float(input("Enter length of Side 1: "))
    side2 = float(input("Enter length of Side 2: "))
    side3 = float(input("Enter length of Side 3: "))

    # Validation: sides must be positive
    if side1 <= 0 or side2 <= 0 or side3 <= 0:
        print("Error: All sides must be greater than 0.")

    # Triangle Inequality Theorem check
    elif (side1 + side2 > side3) and \
         (side1 + side3 > side2) and \
         (side2 + side3 > side1):

        print("\nThe given sides form a VALID triangle.")

        # Type based only on sides
        if side1 == side2 == side3:
            print("Triangle Type: Equilateral")
        elif side1 == side2 or side2 == side3 or side1 == side3:
            print("Triangle Type: Isosceles")
        else:
            print("Triangle Type: Scalene")

    else:
        print("\nThe given sides DO NOT form a valid triangle.")

except ValueError:
    print("Error: Please enter numeric values only.")
