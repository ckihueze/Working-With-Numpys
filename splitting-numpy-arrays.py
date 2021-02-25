# Splitting is reverse operation of Joining.
# Joining merges multiple arrays into one and Splitting breaks one array into multiple.
# We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.

import numpy as np

# split the array into 3 parts:

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np.array_split(a, 3))

# Split the array in 4 parts:
# If the array has less elements than required, it will adjust from the end accordingly.

b = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(np.array_split(b, 4))