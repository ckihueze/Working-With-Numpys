# We pass a sequence of arrays that we want to join to the concatenate() function, along with the axis.
# If axis is not explicitly passed, it is taken as 0.

import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(np.concatenate((a, b)))

# Join two 2-D arrays along rows (axis=1):

c = np.array([[1, 2, 4, 7], [3, 9, 0, 6]])
d = np.array([[3, 1, 5, 2], [0, 4, 7, 1]])
print(np.concatenate((c, d), axis = 1))