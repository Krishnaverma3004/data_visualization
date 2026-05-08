# Program to generate Fibonacci series up to N terms

def is_numeric_manual(s):
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    return len(s) > 0

# Step 1: Input number of terms
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

# Step 2: Generate Fibonacci series
a, b = 0, 1
count = 1
while count <= N:
    print(a, end=' ')
    c = a + b
    a = b
    b = c
    count += 1
print()

'''output
Enter number of terms: 5
0 1 1 2 3 
Enter number of terms: wee
Enter numeric value only.
Enter number of terms: 34
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765 10946 17711 28657 46368 75025 121393 196418 317811 514229 832040 1346269 2178309 3524578 
'''