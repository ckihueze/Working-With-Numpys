# Once you’ve created your arrays, you can start to work with them.
# Let’s say, for example, that you’ve created two arrays, one called “data” and one called “ones”

import numpy as np

data = np.array([2, 4])
ones = np.ones(2, dtype = int)
data2 = np.array([4, 6])

print(data + ones)

# You can, of course, do more than just addition!

print(data - ones)
print(data * ones)
print(data2 ** data)
print(data / data2)

