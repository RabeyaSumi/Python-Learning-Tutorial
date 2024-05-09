"""
Splitting Numpy Arrays:
Splitting is reverse operation of Joining.
"""
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

"""
If the array has less elements than required, it will adjust from the end
accordingly. and if slipts greater than elements then remaining slipts 
will take empty arrays.
"""
newarr = np.array_split(arr, 4)
print(newarr)

"""
Splitting 2D arrays:
use the same syntax when splitting 2D arrays.
"""
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)

"""
The example above returns three 2D array.
Let's look at another example, this time each element in the 2D arrays contains 3 elements.
"""
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print("\n\n" , newarr)

"""
The example below also returns three 2D arrays, but they are split along the row(axis = 1).
"""

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr = np.array_split(arr, 3, axis=1)

print("\n\n" , newarr)

"""
An alternate solution is using hsplit() opposite of hstack(). 
"""
newarr = np.hsplit(arr, 3)
print("\n\n" , newarr)















