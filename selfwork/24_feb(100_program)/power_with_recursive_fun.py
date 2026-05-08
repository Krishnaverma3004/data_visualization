# Recursive power function
def power(b,e):
    if e==0: return 1
    return b*power(b,e-1)

# Input validation
while True:
    b = input("Base: "); e = input("Exponent: ")
    if all('0' <= c <= '9' for c in b+e):
        b, e = int(b), int(e)
        break
    else: print("Enter non-negative integers.")

print("Result:", power(b,e))

'''output
Base: a
Exponent: b
Enter non-negative integers.
Base: 23
Exponent: 4
Result: 279841
'''