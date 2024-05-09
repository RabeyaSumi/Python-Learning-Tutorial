"""
Shape of an array:
The shape of an array is the number of elements in each dimension.
Get the Shape of an Array:
NumPy arrays have an attribute called shape that returns a tuple with each index having
 the number of corresponding elements.
"""
"""
Print the shape of a 2D array.
Shape tuple represent the numbers of elements in every dimension.
"""
import numpy as np
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

arr = np.array([1, 2, 3, 4], ndmin = 5)

print(arr)
print('shape of array :', arr.shape)