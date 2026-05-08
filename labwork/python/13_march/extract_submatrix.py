import numpy as np   # Import NumPy library

# Create an array containing numbers from 1 to 25
arr = np.array([1,2,3,4,5,
                6,7,8,9,10,
                11,12,13,14,15,
                16,17,18,19,20,
                21,22,23,24,25])

# Reshape the array into a 5x5 matrix
matrix = arr.reshape(5,5)

# Extract the middle 3x3 sub-matrix using slicing
sub_matrix = matrix[1:4,1:4]

# Print the extracted sub-matrix
print(sub_matrix)

'''output:
[[ 7  8  9]
 [12 13 14]
 [17 18 19]]
'''