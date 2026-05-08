# Function to get unique elements
def unique(lst):
    res = []
    for x in lst:
        if x not in res: res.append(x)
    return res

# Input validation
while True:
    lst_str = input("Enter numbers separated by space: ")
    if all(c.isdigit() or c==' ' for c in lst_str):
        lst = [int(x) for x in lst_str.split() if x]
        break
    else:
        print("Enter only numbers separated by space.")

print("Unique elements:", unique(lst))
'''output:
Enter numbers separated by space: 1,2,33,4,5,3,4
Enter only numbers separated by space.
Enter numbers separated by space:  a d 1 2 3
Enter only numbers separated by space.
Enter numbers separated by space: 1 2 3 3 4 5 56 7 8
Unique elements: [1, 2, 3, 4, 5, 56, 7, 8]'''