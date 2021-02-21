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

# Access the 4th element on 2nd dim

print(b[1, 3])

# Or you can select elements that satisfy two conditions using the & operator:

print(b[(b > 2) & (b < 12)])

# # Or you can select elements that satisfy two conditions using the | operator:

print((b > 2) | (b == 10))

# You can select elements that are divisible by 2

print(b[b % 2 == 0])

# If you want to select values from your array that fulfill certain conditions, it’s straightforward with NumPy.

c = np.array([[1, 2, 3, 4], [6, 7, 8, 9]])
print(c[c < 6])

# You can also use np.nonzero() to select elements or indices from an array.

d = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
e = np.nonzero(d > 5)
f = np.nonzero(d < 5)
print(e)
print(f)

# If you want to generate a list of coordinates where the elements exist, you can zip the arrays, iterate over the list of coordinates, and print them.

list_of_cordinates = list(zip(e[0], e[1]))
print(list_of_cordinates)
for cord in list_of_cordinates:
    print(cord)
    
# You can also use np.nonzero() to print the elements in an array that are less than 5

print(d[f])

# You can also use np.nonzero() to print the elements in an array that are greater than 5

print(d[e])

# If the element you’re looking for doesn’t exist in the array, then the returned array of indices will be empty.

not_there = np.nonzero(d == 50)
print(not_there)