"""
Random number NOT mean a different number every time. Random means something that
predicted logically.

Pseudo Random and True Random:
Computers work on programs, and programs are definitive set of instructions. So it
means there must be some algorithm to generate a random number as well.
"""
"""
If there is a program to generate random number it can be predicted, thus it is not
truely random.
Random numbers generated through a generation algorithm are called pseudo random.

Can we make a truly random numbers?

Yes. In order to generate a truly random number on our computers we need to get 
the random data from some outside source. This outside source is generally our 
keystrokes, mouse movements, data on network etc.

We do not need truly random numbers, unless it is related to security (e.g. encryption
keys) or the basis of application is the randomness (e.g. Digital roulette wheels).

In this tutorial we will be using pseudo random numbers.

NumPy offers the random module to work with ransom numbers.
"""
from numpy import random
x = random.randint(100)
print(x)

"""
The random module's rand() method returns a random float between 0 and 1.
"""
x = random.rand()
print(x)

"""
Generate Random Array:
In NumPy we work with arrays, and we can use the two methods from the above example
to make random arrays.
"""
x = random.randint(100, size = (5))
print(x)

"""
Generate a 2D array with 3 rows, each row containing 5 random integers from 0 to 100.
"""
x = random.randint(100, size = (3, 5))
print(x)

"""
The rand() method also allows us to specify the shape of the array.
Generate a 1D array containing 5 random floats.
"""
x = random.rand(5)
print("\n\n", x)

"""
Generate Random Number From Array:
The choice() method allows you to generate a random value based on an array of values.

"""
x = random.choice([3, 5, 7, 9])
print(x)

"""
The choice() method also allows you to return an array of values.
Add a size parameter to specify the shape of the array.
Output:
[[5 7 7 9 3]
 [9 9 9 9 3]
 [3 9 5 9 7]]
"""
x = random.choice([3, 5, 7, 9], size = (3, 5))
print("\n\n" , x)















