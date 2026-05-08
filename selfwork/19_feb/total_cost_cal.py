total = 0
n_input = input("Enter number of items: ")
valid = 1

for ch in n_input:
    valid = valid * ((ch >= '0') * (ch <= '9'))

n = int(n_input) * valid

for i in range(1, n + 1):
    price_input = input("Enter price of item " + str(i) + ": ")
    v = 1
    for ch in price_input:
        v = v * ((ch >= '0') * (ch <= '9'))
    price = int(price_input) * v
    total = total + price

print("Total cost =", total)
