"""
You can search an array for a certain value, and return the indexes that get match.
"""
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x) #return indexes where value == 4.

x = np.where(arr%2 == 0)
print(x) # prints even elements indexes.

"""
Search sorted:
There is a method called searchsorted() which performs a binary search in the array
and returns the index where the specified value would be inserted to maintain the search order.
The mathod is assumed to be used on sorted arrays.
"""
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 9) #should be inserted in index 3 from the left side
print(x)

"""
Search from the right side:
return right most index.
"""
arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr, 7, side = 'right')
print(x)  #should be inserted in index 2 from the right side.

"""
Insert multiple values.
"""
arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr, [2, 4, 6])
print(x)




























