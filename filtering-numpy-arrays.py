# Filtering Arrays
# Getting some elements out of an existing array and creating a new array out of them is called filtering.
# In NumPy, you filter an array using a boolean index list.
# If the value at an index is True that element is contained in the filtered array.
# If the value at that index is False that element is excluded from the filtered array.

import numpy as np

a = np.array([1, 2, 3, 4, 5])
b = [True, False, True, False, True]
print(a[b])

# Creating the Filter Array
# In the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions.