import numpy as np  

# You can index and slice NumPy arrays in the same ways you can slice Python lists.

a = np.array([1, 2, 3, 4, 5])

print(a[1])
print(a[-2])
print(a[:3])
print(a[2:])
print(a[1:4])
print(a[:-1])
print(a[:-2])
print(a[-2:])

# Access the 2nd element on 1st dim

b = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(b[0, 1])

# If you want to select values from your array that fulfill certain conditions, it’s straightforward with NumPy.

c = np.array([[1, 2, 3, 4], [6, 7, 8, 9]])
print(c[c < 6])
