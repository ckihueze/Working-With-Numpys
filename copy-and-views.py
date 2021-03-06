# The main difference between a copy & a view of an array is that the copy is a new array, and the view is just a view of the original array.
# Any changes made to the copy will not affect original array, and any changes made to the original array will not affect the copy.
# Any changes made to the view will affect the original array, and any changes made to the original array will affect the copy.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Make a copy, change the original array, and display both arrays:
# The copy SHOULD NOT be affected by the changes made to the original array.

a = arr.copy()
arr[0] = 20
print(arr)
print(a)

# Make a view, change the original array, and display both arrays:
# The view SHOULD be affected by the changes made to the original array.
arr1 = np.array([2, 1, 4, 7])

b = arr1.view()
arr1[0] = 20

print(arr1)
print(b)

# copies owns the data, and views does not own the data, but how can we check this?
# Every NumPy array has the attribute base that returns None if the array owns the data.
# Otherwise, the base attribute refers to the original object.

x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)




