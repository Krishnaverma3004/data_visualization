# Input two lists manually
def input_list(name):
    lst = []
    print(f"Enter numbers for {name} (0 to stop):")
    while True:
        s = input("Number: ")
        if all('0' <= c <= '9' for c in s) and s != "":
            n = int(s)
            if n == 0:
                if len(lst) == 0:
                    print("List cannot be empty.")
                    continue
                break
            lst += [n]
        else:
            print("Invalid input!")
    return lst

lst1 = input_list("first list")
lst2 = input_list("second list")

# Find common elements manually
common = []
i = 0
while i < len(lst1):
    j = 0
    while j < len(lst2):
        if lst1[i] == lst2[j]:
            # check if already added
            add = True
            k = 0
            while k < len(common):
                if common[k] == lst1[i]:
                    add = False
                k += 1
            if add:
                common += [lst1[i]]
        j += 1
    i += 1

print("Common elements:", common)