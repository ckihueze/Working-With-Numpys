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

# Joining Arrays Using Stack Functions
# Stacking is same as concatenation, the only difference is that stacking is done along a new axis.
# We can concatenate two 1-D arrays along the second axis which would result in putting them one over the other, ie. stacking.
# We pass a sequence of arrays that we want to join to the stack() method along with the axis. 
# If axis is not explicitly passed it is taken as 0.

print(np.stack((a, b), axis = 1))
print(np.stack((c, d), axis = 1))
# Stacking Along Rows
# NumPy provides a helper function: hstack() to stack along rows.

print(np.hstack((a, b)))
print(np.hstack((c, d)))

# Stacking Along Columns
# NumPy provides a helper function: vstack() to stack along columns.

print(np.vstack((a, b)))
print(np.vstack((c, d)))

# Stacking Along Height (depth)
# NumPy provides a helper function: dstack() to stack along height, which is the same as depth.

print(np.dstack((a, b)))
print(np.dstack((c, d)))