"""
The normal distribution is one of the most important distributions.
It is also called the Gaussian distribution aster the german mathematician carl
    Feiedrich Gauss.
It fits the probability distribution of many events, eg. IQ Scores, Hearbeat etc.
Use the random.normal() method to get a normal data distribution.
It has theree parameters:
 -loc: ( mean) where the peak of the bell exists
 -scale:(Standard Deviation)how flat the graph distribution should be.
 -size: The shape of the returned array.
"""

from numpy import random
x = random.normal(size=(2, 3))
print(x)

"""
Generate a randon normal distribution of size 2*3 with mean at 1 and standard
deviation of 2.
"""
x = random.normal(loc = 1, scale = 2, size = (2, 3))
print(x)
