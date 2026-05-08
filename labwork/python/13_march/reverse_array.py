import numpy as np   # Import NumPy library

# Create an array from 1 to 10
arr = np.array([1,2,3,4,5,6,7,8,9,10])

# Reverse the array using slicing
reversed_arr = arr[::-1]

# Print the reversed array
print(reversed_arr)

'''output:
[10  9  8  7  6  5  4  3  2  1]
'''