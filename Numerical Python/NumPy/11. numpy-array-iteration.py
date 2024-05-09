"""
iterating means going thouhg element one by one.
as we deal with multi-dimensional arrays in numpy, we can do this using basic for loop
of python.
"""
"""
Iterate on the elements of the following 1D array.
"""
import numpy as np

arr = np.array([1, 2, 3])
for x in arr:
    print(x)

"""
Iterate on the elements of the following 2D array.
"""
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)

"""
Iterate on each scalar element of the 2D array.
"""
for x in arr:
    for y in x:
        print(y)

"""
In a 3D array it go through all the 2D arrays.
"""
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

for x in arr:
    print(x)

"""
To return the actual values, the scalars.
"""
for x in arr:
    for y in x:
        for z in y:
            print(z)

"""
Iterating arrays using nditer():
The nditer() is a helping function that can be used from very basic to very advanced
iterations. It solves some basic issues which we face in iteration, lets go through it with
examples.

it's goes by elements.
"""
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])

for x in np.nditer(arr):
    print(x)

"""
Iterating array with different data types:
We can use op_dtypes argument and pass it the expected datatype to change the datatype of 
elements while iterating.
Numpy does not change the data type of the element in-place(where the element is in array)
so it needs some other space to perform this action, we pass flags = ['buffered'].
"""

for x in np.nditer(arr, flags = ['buffered'], op_dtypes=['S']):
    print(x)

"""
Iterating with different step size:
we can use filtering and followed by iteration.
Iterate through every scalar element of the 2D array skipping(missing) 1 element.
"""
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
    print(x)

"""
Enumerated Iteration using ndenumerate()
Enumeration means mentioning sequence number of something one by one.
Sometimes we require corresponding index of the element while iterating, the ndenumerate()
    method can be used for those usecases.
"""
for idx, x in np.ndenumerate(arr):
    print(idx)










