import numpy as np

# Create an even-numbered array from 2 to 32
arr = np.arange(2, 34, 2)
# Reshape the array to a 4x4 matrix
arr_dim = arr.reshape((4, 4))
# Find mean and standard deviation
mean = np.mean(arr_dim)
st = np.std(arr_dim)

print(arr_dim)
# Using nested loops to iterate and print the elements within half a standard deviation from the mean
for row in arr_dim:
    for element in row:
        if (element > (mean - 0.5 * st)) and (element < (mean + 0.5 * st)):
            print(element)
