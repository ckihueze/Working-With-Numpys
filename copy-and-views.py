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





