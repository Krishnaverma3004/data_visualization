# Program to accept numbers until 0 is entered and print sum

def is_numeric_manual(s):
    for char in s:
        if not ('0' <= char <= '9'):
            return False
    return len(s) > 0

sum_total = 0

while True:
    num_str = input("Enter number (0 to stop): ")
    if is_numeric_manual(num_str):
        num = int(num_str)
        if num == 0:
            break
        sum_total += num
    else:
        print("Enter numeric value only.")

print("Sum of entered numbers:", sum_total)

'''output
Enter number (0 to stop): 3
Enter number (0 to stop): 3
Enter number (0 to stop): 2
Enter number (0 to stop): 1
Enter number (0 to stop): 4
Enter number (0 to stop): 0
Sum of entered numbers: 13

output2:
Enter number (0 to stop): ae
Enter numeric value only.
Enter number (0 to stop): 33
Enter number (0 to stop): 0
Sum of entered numbers: 33
'''