import numpy as np

# You can easily use create a new array from a section of an existing array.

a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

arr1 = a[3:8]
arr2 = a[2:5]

print(arr1)
print(arr2)

# You can also stack two existing arrays, both vertically and horizontally. Let’s say you have two arrays, a1 and a2:

a1 = np.array([[1, 2], [3, 4], [4, 9]])
a2 = np.array([[5, 6], [7, 8], [4, 7]])

# you can stack them vertically with vstack()
 
print(np.vstack((a1, a2)))

#  you can stack them horizontally with hstack()

print(np.hstack((a1, a2)))

# You can split an array into several smaller arrays using hsplit. 
# You can specify either the number of equally shaped arrays to return or the columns after which the division should occur.

b1 = np.arange(20).reshape(2, 10)
print(b1)

print(np.hsplit(b1, 2))
