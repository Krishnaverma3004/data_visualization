
# Program to generate Fibonacci series using for loop

def is_numeric_manual(s):
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    return len(s) > 0

# Input number of terms
while True:
    n_str = input("Enter number of terms: ")
    if is_numeric_manual(n_str):
        N = int(n_str)
        if N > 0:
            break
        else:
            print("Number must be positive.")
    else:
        print("Enter numeric value only.")

# Fibonacci series using for loop
a, b = 0, 1
for _ in range(N):
    print(a, end=' ')
    c = a + b
    a = b
    b = c
print()

'''output:
Enter number of terms: ab
Enter numeric value only.
Enter number of terms: 3
0 1 1 '''