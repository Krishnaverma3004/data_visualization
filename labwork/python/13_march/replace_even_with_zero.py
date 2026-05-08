import numpy as np   # Import NumPy library

# Create a NumPy array from 1 to 10
arr = np.array([1,2,3,4,5,6,7,8,9,10])

# Replace all even numbers with 0
arr[arr % 2 == 0] = 0

# Print the modified array
print(arr)

'''output:
[1 0 3 0 5 0 7 0 9 0]
'''