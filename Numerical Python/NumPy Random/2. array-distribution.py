"""
Data distribution is a list of all possible values, and how often each value occurs.

Such lists are important when working with statistics and data science.

The random module offer methods that returns randomly generated data distributions.

Probability Density Function:
 A function that describes a continuous probability.
"""
from numpy import random
x = random.choice([3, 5, 7, 9], p = [0.1, 0.3, 0.6, 0.0], size = (10))
print(x)

"""
For 2D arrays:
"""
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size = (3, 5))
print("\n\n", x)






















