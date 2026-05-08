def flatten_list(data):
    """Return a flattened version of a nested list."""
    result = []

    for item in data:
        if isinstance(item, list):
            result += flatten_list(item)  # recursive call
        else:
            result.append(item)

    return result


def build_list():
    """Create a nested list from user input."""
    result = []
    size = int(input("Enter number of elements: "))

    for _ in range(size):
        choice = input("Enter 'n' (number) or 'l' (list): ").lower()

        if choice == 'n':
            result.append(int(input("Enter number: ")))
        elif choice == 'l':
            result.append(build_list())  # recursive input

    return result


# Main execution
nested_list = build_list()
print("Flattened List:", flatten_list(nested_list))

'''output:
Enter number of elements: 20
Enter 'n' (number) or 'l' (list): n
Enter number: 1
Enter 'n' (number) or 'l' (list): n
Enter number: 2
Enter 'n' (number) or 'l' (list): l
Enter number of elements: 3
Enter 'n' (number) or 'l' (list): n
Enter number: 3
Enter 'n' (number) or 'l' (list): n 
Enter number: 4
Enter 'n' (number) or 'l' (list): n
Enter number: 5
Enter 'n' (number) or 'l' (list): n
Enter number: 6 
Enter 'n' (number) or 'l' (list): n
Enter number: 7
Enter 'n' (number) or 'l' (list): n
Enter number: 8
Enter 'n' (number) or 'l' (list): n
Enter number: 9
Enter 'n' (number) or 'l' (list): n
Enter number: 10
Enter 'n' (number) or 'l' (list): n
Enter number: 11
Enter 'n' (number) or 'l' (list): n
Enter number: 12
Enter 'n' (number) or 'l' (list): n
Enter number: 13
Enter 'n' (number) or 'l' (list): n
Enter number: 14
Enter 'n' (number) or 'l' (list): n
Enter number: 15
Enter 'n' (number) or 'l' (list): n
Enter number: 16
Enter 'n' (number) or 'l' (list): n
Enter number: 17
Enter 'n' (number) or 'l' (list): n
Enter number: 18
Enter 'n' (number) or 'l' (list): n
Enter number: 19
Enter 'n' (number) or 'l' (list): n
Enter number: 20
Flattened List: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''