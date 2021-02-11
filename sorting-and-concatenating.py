import numpy as np

# Sorting an element is simple with np.sort(). 
# You can specify the axis, kind, and order when you call the function.

a = np.array([2, 1, 3, 8, 5])
print(np.sort(a))

# You can concatenate with np.concatenate().

b = np.array([2, 3, 4, 6, 8, 9])
c = np.array([10, 12, 51, 5, 7])
conc = np.concatenate((b, c))
print(conc)

# Or, you can concatenate it this way:
d = np.array([[2, 3, 6], [6, 9, 0]])
e = np.array([[7, 1, 2]])
conc2 = np.concatenate((d, e))
print(conc2)
