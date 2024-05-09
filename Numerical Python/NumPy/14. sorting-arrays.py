"""
Sorting means putting elements in an ordered sequence.
Ordered sequence is any sequence that has an order corresponding to elements, like
numeric or alphabetical, ascending or descending.
"""
import numpy as np
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

"""
Sort strings, alphabetically.
"""
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))

"""
If we use the sort() method on a 2D array, both arrays will be sorted.
"""
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

