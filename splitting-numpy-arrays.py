# Splitting is reverse operation of Joining.
# Joining merges multiple arrays into one and Splitting breaks one array into multiple.
# We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

import numpy as np

# split the array into 3 parts:

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np.array_split(a, 3))

# Split the array in 4 parts:
# If the array has less elements than required, it will adjust from the end accordingly.

b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np.array_split(b, 4))

# Accessing the splited Arrays
# If you split an array into 3 arrays, you can access them from the result just like any array element:

c = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
splited_array = np.array_split(c, 3)

print(splited_array[0])
print(splited_array[1])
print(splited_array[2])

# Splitting 2-D Arrays
# Use the same syntax when splitting 2-D arrays.
# Use the array_split() method, pass in the array you want to split and the number of splits you want to do.

d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [3, 6, 1, 0], [2, 6, 1, 0]])
print(np.array_split(d, 2))

# In addition, you can specify which axis you want to do the split around.
# The example below also returns three 2-D arrays, but they are split along the row (axis=1).

print(np.array_split(d, 2, axis = 1))