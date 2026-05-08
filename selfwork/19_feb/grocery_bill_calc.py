total = 0

while True:
    n = input("Enter number of items: ")
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
        if n > 0:
            break

    print("Invalid input")

for i in range(1, n + 1):

    while True:
        price = input("Enter item price: ")
        valid = 1

        if price == "":
            valid = 0
        else:
            for ch in price:
                if ch < '0' or ch > '9':
                    valid = 0
                    break

        if valid == 1:
            price = int(price)
            break

        print("Invalid input")

    total = total + price

print("Total Bill =", total)
