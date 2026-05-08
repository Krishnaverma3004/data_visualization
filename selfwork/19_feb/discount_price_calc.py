price_input = input("Enter original price: ")
v = 1
for ch in price_input:
    v = v * ((ch >= '0') * (ch <= '9'))
price = int(price_input) * v

discount_input = input("Enter discount %: ")
v = 1
for ch in discount_input:
    v = v * ((ch >= '0') * (ch <= '9'))
discount = int(discount_input) * v

final_price = price - (price * discount / 100)
print("Price after discount =", final_price)
