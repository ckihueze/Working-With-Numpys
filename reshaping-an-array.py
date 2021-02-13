import numpy as np  

# Using arr.reshape() will give a new shape to an array without changing the data.
# Just remember that when you use the reshape method, the array you want to produce needs to have the same number of elements as the original array.
# If you start with an array with 12 elements, you’ll need to make sure that your new array also has a total of 12 elements.

# If you only use the arange function, it will output a one-dimensional array.

a = np.arange(12)
print(a)
print(" ")

# To make it a two-dimensional array, chain its output with the reshape
# First, 12 integers will be created and then it will convert the array into a two-dimensional array with 4 rows and 3 columns. 

b = a.reshape(4, 3)
print(b)
print(" ")

# To create a three-dimensional array, specify 3 parameters to the reshape function.

c = a.reshape(3, 2, 2)
print(c)
print(" ")

# You are allowed to have one "unknown" dimension.
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.

d = a.reshape(2, 3, -1)
print(d)
print(" ")