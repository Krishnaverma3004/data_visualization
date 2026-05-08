# Function to generate Fibonacci series
def fibonacci(n):
    a, b, res = 0, 1, []
    for _ in range(n):
        res.append(a)
        a, b = b, a+b
    return res

# Input validation
while True:
    t = input("Enter number of terms: ")
    if all('0' <= c <= '9' for c in t) and t != "0":
        t = int(t)
        break
    else:
        print("Invalid input.")

print(*fibonacci(t))

'''output
Enter number of terms: 5
0 1 1 2 3
output 2:
Enter number of terms: ab
Invalid input.
Enter number of terms: 3
0 1 1
'''