import numpy as np  

a = np.array([[[1, 2, 3, 7], [4, 5, 6, 2]], [[3, 5, 8, 9], [4, 5, 7, 2]], [[1, 2, 5, 6], [4, 7, 1, 9]]])
b = np.array([[1, 2], [3, 4], [5, 6]])
c = np.array([[1, 2, 3, 4, 7], [5, 6, 7, 2, 8], [9, 10, 11, 12, 19], [13, 14, 15, 20, 16]])

# ndarray.ndim will tell you the number of axes, or dimensions, of the array.

print(a.ndim)
print(b.ndim)
print(c.ndim)

# ndarray.size will tell you the total number of elements of the array.

print(a.size)
print(b.size)
print(c.size)

# ndarray.shape will display a tuple of integers that indicate the number of elements stored along each dimension of the array.
# If, for example, you have a 2-D array with 2 rows and 3 columns, the shape of your array is (2, 3).

print(a.shape)
print(b.shape)
print(c.shape)
