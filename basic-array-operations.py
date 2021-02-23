# Once you’ve created your arrays, you can start to work with them.
# Let’s say, for example, that you’ve created two arrays, one called “data” and one called “ones”

import numpy as np

data = np.array([2, 4])
ones = np.ones(2, dtype = int)
data2 = np.array([4, 6])

print(data + ones)

# You can, of course, do more than just addition!

print(data - ones)
print(data * ones)
print(data2 ** data)
print(data / data2)

# Basic operations are simple with NumPy.
# If you want to find the sum of the elements in an array, you’d use sum().
# This works for 1D arrays, 2D arrays, and arrays in higher dimensions.

print(data.sum())
print(data2.sum())

# Sum of Array Elements Along the Axis
# If we specify the axis value, the sum of elements along that axis is returned.
# If the array shape is (X, Y) then the sum along 0-axis will be of shape (1, Y).
# The sum along 1-axis will be of shape (1, X).

arr = np.array([[1, 2,], [4, 5], [6, 7]])
print(arr.sum(axis = 0))
print(arr.sum(axis = 1))

arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr1.sum(axis = 0))
print(arr1.sum(axis = 1))