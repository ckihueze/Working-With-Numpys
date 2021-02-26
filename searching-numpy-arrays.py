# You can search an array for a certain value, and return the indexes that get a match.
# To search an array, use the where() method.

import numpy as np

# Find the indexes where the value is 3:

a = np.array([1, 2, 4, 7, 3, 0, 3, 5, 3, 4, 1])
print(np.where(a == 3))

# Find the indexes where the values are even:

print(np.where(a % 2 == 0))

# # Find the indexes where the values are odd:

print(np.where(a % 2 == 1))

# Search Sorted
# There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.
# The searchsorted() method is assumed to be used on sorted arrays.

# Find the indexes where the value 7 should be inserted:

b = np.array([6, 7, 8, 9])
print(np.searchsorted(b, 7))
# The method starts the search from the left and returns the first index where the number 7 is no longer larger than the next value.


# Multiple Values
# To search for more than one value, use an array with the specified values.

c = np.array([2, 4, 6, 8])
print(np.searchsorted(c, [1, 3, 5, 7]))
# The return value is an array: [0 1 2 3] containing the three indexes where 1, 3, 5, 7 would be inserted in the original array to maintain the order.