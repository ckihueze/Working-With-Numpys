import numpy as np 

# initializing numpy arrays

a = np.array([1, 2, 3, 4, 5])
b = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
print(a)
print(b)

# Besides creating an array from a sequence of elements, you can easily create an array filled with 0’s:

c = np.zeros(3)
print(c)

# Or an array filled with 1’s:

d = np.ones(3)
print(d)

# You can also create an array of empty elements
# The reason to use empty over zeros (or something similar) is speed - just make sure to fill every element afterwards!

e = np.empty(2)
print(e)

# You can create an array with a range of elements:

f = np.arange(5)
print(f)

g = np.arange(2, 8)
print(g)

# And even an array that contains a range of evenly spaced intervals. 
# To do this, you will specify the first number, last number, and the step size.

h = np.arange(2, 12, 2)
print(h)

# You can also use np.linspace() to create an array with values that are spaced linearly in a specified interval:

i = np.linspace(0, 10, num = 5)
print(i)

j = np.linspace(2, 20, num = 4)
print(j)

# While the default data type is floating point (np.float64), you can explicitly specify which data type you want using the dtype keyword.

k = np.ones(3, dtype = np.int64)
print(k)




