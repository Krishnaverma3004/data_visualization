while True:
    n = input("Enter a non-negative integer: ")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Invalid input.")

i = 1
fact = 1

while i <= n:
    fact = fact * i
    i = i + 1

print("Factorial =", fact)
