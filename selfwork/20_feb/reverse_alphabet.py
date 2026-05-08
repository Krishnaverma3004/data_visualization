rows = int(input("Enter rows: "))

for i in range(rows, 0, -1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

'''output:
Enter rows: 9
ABCDEFGHI
ABCDEFGH
ABCDEFG
ABCDEF
ABCDE
ABCD
ABC
AB
A'''