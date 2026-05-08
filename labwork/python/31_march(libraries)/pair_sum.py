def find_pairs_with_sum(numbers, target_sum):
    # List to store pairs
    pairs = []

    # Check all possible pairs
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == target_sum:
                pairs.append((numbers[i], numbers[j]))

    return pairs


# ----------- USER INPUT SECTION -----------

numbers = []
size = int(input("Enter number of elements: "))

for i in range(size):
    numbers.append(int(input("Enter element: ")))

target_sum = int(input("Enter target sum: "))

print("Pairs:", find_pairs_with_sum(numbers, target_sum))


'''output:
Enter number of elements: 10
Enter element: 67
Enter element: 56
Enter element: 46
Enter element: 35
Enter element: 24
Enter element: 12
Enter element: 23
Enter element: 4
Enter element: 5
Enter element: 55
Enter target sum: 60
Pairs: [(56, 4), (5, 55)]
'''