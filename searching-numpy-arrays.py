# You can search an array for a certain value, and return the indexes that get a match.
# To search an array, use the where() method.

import numpy as np

# Find the indexes where the value is 3:

a = np.array([1, 2, 4, 7, 3, 0, 3, 5, 3, 4, 1])
print(np.where(a == 3))