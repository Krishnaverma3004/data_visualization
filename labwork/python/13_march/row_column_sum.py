import numpy as np   # Import NumPy library

# Create a 4x4 matrix
matrix = np.array([[1,2,3,4],
                   [5,6,7,8],
                   [9,10,11,12],
                   [13,14,15,16]])

# Calculate sum of each row
row_sum = matrix.sum(axis=1)

# Calculate sum of each column
column_sum = matrix.sum(axis=0)

# Display row-wise sum
print("Row Sum:")
print(row_sum)

# Display column-wise sum
print("Column Sum:")
print(column_sum)
'''output:
Row Sum:
[10 26 42 58]
Column Sum:
[28 32 36 40]
'''