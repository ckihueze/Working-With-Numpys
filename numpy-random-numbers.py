# Random number does NOT mean a different number every time.
# Random means something that can not be predicted logically.
# Computers work on programs, and programs are definitive set of instructions.
# So it means there must be some algorithm to generate a random number as well.
# If there is a program to generate random number it can be predicted, thus it is not truly random.
# Random numbers generated through a generation algorithm are called pseudo random.
# In order to generate a truly random number, we need to get the random data from some outside source.
# This outside source is generally our keystrokes, mouse movements, data on network etc.
# We do not need truly random numbers, unless its related to security (e.g. encryption keys) or the basis of application is the randomness (e.g. Digital roulette wheels).
# Here, we will be using pseudo random numbers.

#  NumPy offers the random module to work with random numbers.

from numpy import random

x = random.randint(50)
print(x)

# Generate Random Float
# The random module's rand() method returns a random float between 0 and 1.

y = random.rand()
print(y)

# Generate Random Array
# In NumPy we work with arrays, and you can use the two methods from the above examples to make random arrays.
# The randint() method takes a size parameter where you can specify the shape of an array.

# Generate a 1-D array containing 5 random integers from 0 to 100:

z = random.randint(50, size = (5))
print(z)

# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:

j = random.randint(100, size = (3, 5))
print(j)

# Floats
# The rand() method also allows you to specify the shape of the array.
# Generate a 1-D array containing 5 random floats:

k = random.rand(5)
print(k)

# Generate Random Number From Array
# The choice() method allows you to generate a random value based on an array of values.
# The choice() method takes an array as a parameter and randomly returns one of the values.
# Return one of the values in an array:

print(random.choice([1, 2, 4, 6, 9, 5, 7]))


# The choice() method also allows you to return an array of values.
# Add a size parameter to specify the shape of the array.
# Generate a 2-D array that consists of the values in the array parameter (1, 2, 3, 4, 5, 7, 9, and 0):

print(random.choice([1, 2, 3, 4, 5, 7, 9, 0], size = (2, 5)))





