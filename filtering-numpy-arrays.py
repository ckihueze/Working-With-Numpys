# Filtering Arrays
# Getting some elements out of an existing array and creating a new array out of them is called filtering.
# In NumPy, you filter an array using a boolean index list.
# If the value at an index is True that element is contained in the filtered array.
# If the value at that index is False that element is excluded from the filtered array.

import numpy as np

arr = np.array([1, 2, 3, 4, 5])
b = [True, False, True, False, True]
print(arr[b])

# Creating the Filter Array
# In the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions.

filter_arr = []

# go through each element in arr

for x in arr:
    # if the element is higher than 2, set the value to True, otherwise False:
    if x > 2:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
new_arr = arr[filter_arr]
print(new_arr)
print(filter_arr)

# Create a filter array that will return only even elements from the original array:
filter_arr2 = []

for x in arr:
    if x % 2 == 0:
        filter_arr2.append(True)
    else:
        filter_arr2.append(False)
        
even_arr = arr[filter_arr2]
print(even_arr)
print(filter_arr2)

# Creating Filter Directly From Array
# We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.

# Create a filter array that will return only values higher than 2:

filter_arr3 = arr > 3
print(filter_arr3)
print(arr[filter_arr3])