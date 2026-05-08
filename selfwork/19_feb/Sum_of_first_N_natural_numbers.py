#sum off first n numbers

while True:
    n = input("Enter a positive integer: ")
    if n.isdigit() and int(n) > 0:
        n = int(n)
        break
    else:
        print("Invalid input.")

i = 1
total = 0

while i <= n:
    total = total + i
    i = i + 1

print("Sum =", total)

