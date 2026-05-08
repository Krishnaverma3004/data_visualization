def swap_keys_and_values(original_dict):
    # Create new dictionary
    swapped_dict = {}

    # Traverse original dictionary
    for key in original_dict:
        value = original_dict[key]

        # Swap key and value
        swapped_dict[value] = key

    return swapped_dict


# ----------- USER INPUT SECTION -----------

original_dict = {}
size = int(input("Enter number of pairs: "))

for i in range(size):
    key = input("Enter key: ")
    value = input("Enter value: ")
    original_dict[key] = value

print("Swapped Dictionary:", swap_keys_and_values(original_dict))

'''output:
Enter number of pairs: 10
Enter key: 23
Enter value: 67
Enter key: 34
Enter value: 2y
Enter key: 23
Enter value: rr
Enter key: 66
Enter value: thv
Enter key: 12
Enter value: jk
Enter key: 13 
Enter value: sg
Enter key: 14
Enter value: jn
Enter key: 15
Enter value: jp
Enter key: 16
Enter value: v
Enter key: 18
Enter value: bh
Swapped Dictionary: {'rr': '23', '2y': '34', 'thv': '66', 'jk': '12', 'sg': '13', 'jn': '14', 'jp': '15', 'v': '16', 'bh': '18'}
'''