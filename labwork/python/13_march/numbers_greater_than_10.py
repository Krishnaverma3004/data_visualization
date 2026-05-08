import numpy as np   # Import NumPy library

# Create an array from 1 to 15
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

# Find numbers greater than 10
result = arr[arr > 10]

# Print the result
print(result)

'''output:
[11 12 13 14 15]
'''