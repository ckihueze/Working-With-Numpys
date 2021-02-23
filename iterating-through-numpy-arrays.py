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
        
# Iterating 3-D Arrays
# In a 3-D array it will go through all the 2-D arrays.

arr2 = np.array([[[1, 2, 3], [4, 5, 6]], [[2, 4, 5], [1, 6, 8]]])
for x in arr2:
    print(x)
    
for x in arr2:
    for y in x:
        for z in y:
            print(z)
            
# Iterating Arrays Using nditer()
# The function nditer() is a helping function that can be used from very basic to very advanced iterations. 
# It solves some basic issues which we face in iteration, lets go through it with examples.
# In basic for loops, iterating through each scalar of an array we need to use n for loops which can be difficult to write for arrays with very high dimensionality.

arr3 = np.array([[1, 2, 3], [4, 5, 6]])
for x in np.nditer(arr3):
    print(x)
    
arr4 = np.array([[[1, 2, 3], [4, 5, 6]], [[2, 4, 5], [1, 6, 8]]])
for x in np.nditer(arr4):
    print(x)