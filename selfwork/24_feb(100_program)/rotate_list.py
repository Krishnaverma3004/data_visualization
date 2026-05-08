# Input list
lst = []
print("Enter numbers one by one (0 to stop):")
while True:
    n = input("Num: ")
    if all('0' <= c <= '9' for c in n) and n != "":
        n = int(n)
        if n == 0:
            if len(lst) == 0:
                print("List cannot be empty.")
                continue
            break
        lst += [n]
    else:
        print("Invalid input!")

# Input rotation
while True:
    k = input("Enter rotation count: ")
    if all('0' <= c <= '9' for c in k) and k != "":
        k = int(k)
        break
    else:
        print("Invalid input!")

# Rotate manually using modulo
rotated = []
i = 0
while i < len(lst):
    rotated += [lst[(i + k) % len(lst)]]
    i += 1

print("Rotated list:", rotated)