# Multiplication Table with Manual Validation


while True:
    n = input("Enter a positive integer: ")
    valid = 1

    # Check empty input
    if n == "":
        valid = 0
    else:
        i = 0

        # Manual digit validation
        while n[i:i+1] != "":
            if n[i] < '0' or n[i] > '9':
                valid = 0
                break
            i = i + 1

    # Final validation check
    if valid == 1:
        n = int(n)
        if n > 0:
            break

    print("Invalid input. Please enter a positive integer.")

# Print multiplication table
i = 1
while i <= 10:
    print(n, "x", i, "=", n * i)
    i = i + 1

