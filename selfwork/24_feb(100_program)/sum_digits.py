# Function to sum digits
def sum_digits(n):
    s=0
    while n>0:
        s += n%10
        n //= 10
    return s

# Input validation
while True:
    n = input("Enter positive integer: ")
    if all('0' <= c <= '9' for c in n):
        n = int(n)
        break
    else:
        print("Invalid input.")

print("Sum of digits:", sum_digits(n))

'''output
Enter positive integer: abc
Invalid input.
Enter positive integer: 23
Sum of digits: 5
'''