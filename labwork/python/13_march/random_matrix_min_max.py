import numpy as np   # Import NumPy library

# Generate a 5x5 matrix with random integers between 1 and 100
matrix = np.random.randint(1, 101, (5,5))

# Display the generated matrix
print("Matrix:")
print(matrix)

# Find the minimum value in the matrix
min_value = matrix.min()

# Find the maximum value in the matrix
max_value = matrix.max()

# Print minimum and maximum values
print("Min =", min_value)
print("Max =", max_value)

'''output:

[[ 4 91 88 50 72]
 [30 89 85 26 59]
 [38 83 34 97 32]
 [53 92 17 46 13]
 [75 15 64 91 98]]
Min = 4
Max = 98
'''