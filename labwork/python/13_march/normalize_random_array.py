import numpy as np   # Import NumPy library

# Generate 10 random numbers between 0 and 1
arr = np.random.rand(10)

# Normalize the array between 0 and 1
normalized = (arr - arr.min()) / (arr.max() - arr.min())

# Round values to 2 decimal places
arr = np.round(arr, 2)
normalized = np.round(normalized, 2)

# Print the original array
print("Original Array:")
print(arr)

# Print the normalized array
print("Normalized Array:")
print(normalized)

'''output:
Original Array:
[0.83 0.38 0.81 0.02 0.92 0.79 0.26 0.35 0.15 0.5 ]
Normalized Array:
[0.9  0.4  0.88 0.   1.   0.86 0.27 0.37 0.15 0.54]
'''