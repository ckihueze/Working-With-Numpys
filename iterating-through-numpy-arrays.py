# Iterating means going through elements one by one.
# As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
# If we iterate on a 1-D array it will go through each element one by one.

import numpy as np

arr = np.array([1, 2, 3, 4])
for x in arr:
    print(x)
    
# Iterating 2-D Arrays
# In a 2-D array it will go through all the rows.

arr1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for y in arr1:
    print(y)
    
for z in arr1:
    for a in z:
        print(a)