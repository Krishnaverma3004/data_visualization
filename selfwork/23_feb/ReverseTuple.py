# Program: Reverse Tuple with Manual Validation
# Description: Takes tuple input from user, validates it, and reverses it
# All done manually without predefined functions or try/except

numbers = ()  # initialize empty tuple

while True:
    user_input = input("Enter tuple elements separated by commas: ")
    current_num = ""  # build each number character by character
    temp_numbers = ()  # temporary tuple to store numbers
    valid = True  # flag for validation

    i = 0
    while i < len(user_input):
        char = user_input[i]

        if char == ',':
            if current_num != "":
                # manually check if current_num is a valid integer
                is_digit = True
                j = 0
                while j < len(current_num):
                    if not ('0' <= current_num[j] <= '9'):
                        is_digit = False
                        break
                    j = j + 1
                if is_digit:
                    # convert to integer manually
                    num = 0
                    j = 0
                    while j < len(current_num):
                        num = num * 10 + (ord(current_num[j]) - ord('0'))
                        j = j + 1
                    temp_numbers = temp_numbers + (num,)
                    current_num = ""
                else:
                    valid = False
                    break
            i = i + 1
            continue

        elif char != ' ':  # ignore spaces
            current_num = current_num + char
        i = i + 1

    # process the last number after loop
    if current_num != "":
        is_digit = True
        j = 0
        while j < len(current_num):
            if not ('0' <= current_num[j] <= '9'):
                is_digit = False
                break
            j = j + 1
        if is_digit:
            num = 0
            j = 0
            while j < len(current_num):
                num = num * 10 + (ord(current_num[j]) - ord('0'))
                j = j + 1
            temp_numbers = temp_numbers + (num,)
        else:
            valid = False

    if valid and temp_numbers != ():
        numbers = temp_numbers
        break
    else:
        print("Invalid input! Please enter only numbers separated by commas.")

# manually reverse the tuple
reversed_tuple = ()
index = 0
length = 0

# calculate length manually
for _ in numbers:
    length = length + 1

index = length - 1
while index >= 0:
    reversed_tuple = reversed_tuple + (numbers[index],)
    index = index - 1

print("Original tuple:", numbers)
print("Reversed tuple:", reversed_tuple)


''' Output
Enter tuple elements separated by commas: 1, 2, 3, 4, 5
Original tuple: (1, 2, 3, 4, 5)
Reversed tuple: (5, 4, 3, 2, 1)

Enter tuple elements separated by commas: 10, 20, 30, abc
Invalid input! Please enter only numbers separated by commas.'''
