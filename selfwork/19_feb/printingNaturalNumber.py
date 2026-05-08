# Program to print numbers from 1 to N

while True:
    n = input("Enter a positive integer: ")
    if n.isdigit() and int(n) > 0:
        n = int(n)
        break
    else:
        print("Invalid input. Please enter a positive integer.")

i = 1
while i <= n:
    print(i)
    i = i + 1
