import numpy as np

arr = np.ones((3, 3), dtype=int)

for i in range(3):
    arr[i, i] = 9

print(arr)
