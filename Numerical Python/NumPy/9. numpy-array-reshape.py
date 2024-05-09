"""
Reshaping means changing the shape of an array.
The shape of an array is the number of elements in each dimension.
By reshaping we can add ar remove dimensions or change number of elements in each dimension.
"""
"""
Reshape From 1D to 2D:
Example: convert the following 1D array with 12 elements into a 2D array.
The outermost dimension will have 4 arrays, each with 3 elements.
"""
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)

"""
Reshape From 1D to 3D:
"""
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

"""
Check if the returned array is a copy or a view.
The example above returns the original array, so it is a view.
"""
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)

"""
Unknown Dimension:
You are allowed to have one "unknown" dimension.
Meaning that you do not have to specify an exact number for one of the dimensions
    in the reshape method.
Pass -1 as the value, and NumPy will calculate this number for you. 
Convert 1D array with 8 elements to 3D array with 2*2 elements.
"""
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(2, 2, -1)
print(newarr)

"""
Flattening the arrays:
Flattening array means converting a multidimensional array into a 1D array.
We can use reshape(-1) to do this.
Convert the array into a 1D array.
"""
arr = np.array([ [1, 2, 3], [4, 5, 6] ])
newarr = arr.reshape(-1)
print(newarr)

"""
There are a lot of functions for changing the shapes of arrays in numpy 
    flatten(), tavel(), 
And also for rearranging the elements 
    rot90, flip, fliplr, flipud etc.
"""









