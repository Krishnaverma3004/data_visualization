# Input numbers for list
lst = []
print("Enter numbers (0 to stop):")
while True:
    n = input("Number: ")
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

# Sum manually
total = 0
i = 0
while i < len(lst):
    total += lst[i]
    i += 1

print("Sum of list:", total)
'''outputEnter numbers (0 to stop):
Number: 3
Number: 4
Number: 4
Number: 3
Number: 32
Number: 0
Sum of list: 46'''