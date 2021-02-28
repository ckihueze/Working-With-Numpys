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

