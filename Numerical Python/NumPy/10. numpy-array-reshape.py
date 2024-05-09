"""
Iterating Arrays:
Iterating means going through elements one by one.
As we deal with multi-dimensional arrays in numpy, we can do this using basic for loop of python.
If we iterate on a 1D array it will go through each element one by one.

"""
"""
Iterate on the elements of the following 1D array.
"""
import numpy as np
arr = np.array([1, 2, 3])
for x in arr:
    print(x)

"""
Iterating 2D Arrays:
In a 2D array it will go through all the rows.
Iterate on the elements of the following 2D array.
"""
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)

"""
But, To return the actual values, the scalars, we have to iterate the arrays in each dimension.
If we iterate on a n-D array it will go through n-1th dimension one by one.
"""
for x in arr:
    for y in x:
        print(y)


"""
Iterating 3D array by row and by the every scalar.
"""
arr = np.array([ [[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]] ])
for x in arr:
    for y in x:
        for z in y:
            print(z)

"""
Iterating Arrays Using nditer()
The function nditer() is a helping function that can be used from very basic to very
    advanced iterations. It solves some basic issues which we face in iteration, lets 
    go through it with examples.
Iterator print the array in scalar way.
"""
arr = np.array([ [[1, 2], [3, 4]], [[5, 6], [7, 8]] ])
for x in np.nditer(arr):
    print(x)

"""
Iteration array with different data types:
We can use op_dtypes argument and pass it the expected datatype to change the datatype
    of elements while iterating.
NumPy does not change the data type of the element in-place (where the element is in array)
    so it needs some other space to perform this action, that extra space is called buffer,
    and in order to enable it in nditer() we pass flags = ['buffered'].
"""
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags = ['buffered'], op_dtypes = ['S']):
    print(x)















