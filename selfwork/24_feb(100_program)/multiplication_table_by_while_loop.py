
# Program to print multiplication table for a number

def is_numeric_manual(s):
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    return len(s) > 0

# Step 1: Input number
while True:
    n_str = input("Enter a number: ")
    if is_numeric_manual(n_str):
        num = int(n_str)
        break
    else:
        print("Enter numeric value only.")

# Step 2: Print multiplication table up to 10
i = 1
while i <= 10:
    print(num, "x", i, "=", num * i)
    i += 1
'''output:
Enter a number: 3
3 x 1 = 3
3 x 2 = 6
3 x 3 = 9
3 x 4 = 12
3 x 5 = 15
3 x 6 = 18
3 x 7 = 21
3 x 8 = 24
3 x 9 = 27
3 x 10 = 30

output2:
Enter a number: 3.4
Enter numeric value only.
Enter a number: abc
Enter numeric value only.
Enter a number: 56
56 x 1 = 56
56 x 2 = 112
56 x 3 = 168
56 x 4 = 224
56 x 5 = 280
56 x 6 = 336
56 x 7 = 392
56 x 8 = 448
56 x 9 = 504
56 x 10 = 560
'''
