# Function to find max of three
def max3(a,b,c):
    m = a
    if b>m: m=b
    if c>m: m=c
    return m

# Input three numbers with validation
nums=[]
for i in range(3):
    while True:
        n = input(f"Enter number {i+1}: ")
        if all('0' <= c <= '9' for c in n):
            nums.append(int(n))
            break
        else:
            print("Enter numeric value.")

print("Maximum:", max3(*nums))

'''output
Enter number 1: 34
Enter number 2: 33
Enter number 3: ab
Enter numeric value.
Enter number 3: 34
Maximum: 34
'''