# ufuncs stands for "Universal Functions" and they are NumPy functions that operates on the ndarray object.
# ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.
# They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.
# ufuncs also take additional arguments, like:

# where boolean array or condition defining where the operations should take place.
# dtype defining the return type of elements.
# out output array where the return value should be copied.

# What is Vectorization?
# Converting iterative statements into a vector based operation is called vectorization.
# It is faster as modern CPUs are optimized for such operations.
# Add the Elements of Two Lists
# list 1: [1, 2, 3, 4]
# list 2: [4, 5, 6, 7]

# One way of doing it is to iterate over both of the lists and then sum each elements.
# Without ufunc, we can use Python's built-in zip() method:
import numpy as np

x = [4, 6, 2, 7]
y = [4, 9, 6, 7]
z = []

for a, b in zip(x, y):
    z.append(a + b)
print(z)

# NumPy has a ufunc for this, called add(x, y) that will produce the same result.
# With ufunc, we can use the add() function:

print(np.add(x, y))
print(np.add(y, x))