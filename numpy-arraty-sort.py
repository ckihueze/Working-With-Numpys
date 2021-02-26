# Sorting Arrays
# Sorting means putting elements in an ordered sequence.
# Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.
# The NumPy ndarray object has a function called sort(), that will sort a specified array.

import numpy as np

a = np.array([3, 7, 1, 0, 2, 6])
print(np.sort(a))

# You can also sort arrays of strings, or any other data type:

name = np.array(['Ihueze', 'Kingsley', 'Chima'])
print(np.sort(name))

# Sorting a 2-D Array
# If you use the sort() method on a 2-D array, both arrays will be sorted:

b = np.array([[3, 1, 8], [5, 2, 6]])
print(np.sort(b))