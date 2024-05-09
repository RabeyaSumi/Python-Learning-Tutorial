import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

"""
To create an ndarray, we can pass a list, tuple or any array-like object into the 
array() method, and it will be converted into an ndarray.
Use a tuple to create a NumPy array.
"""
arr = np.array((1, 2, 3, 4, 5))
print(arr)

"""
Arrays dimension:
0-D arrays- OD arrays pr scalars are the elements in an array. Each value in an array
is a 0D array. create a 0D array with value 43.

An array that has 0D arrays as its elements is called uni-dimensional.
"""
#0D array
import numpy as np
arr0 = np.array(42)
print(arr0)

#1D array
arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)

#D array

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)

#3D array
arr3 = np.array([[ [1, 2, 3], [4, 5, 6], [7, 8, 0] ]])
print(arr3)

#check how many dimension the array have.
print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

"""
Create an array with 5 dimensions and verify that it has 5 dimensions:
"""
arr = np.array([1, 2, 3, 4], ndmin = 5)
print(arr)
print("numbe of dimenwions : ", arr.ndmin)



















