"""
Getting some elements out of an existing array and creating a new array out of them
is called filtering.

In NumPy we folter an array using boolean index list.
"""
import numpy as np
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
newarr = arr[x]
print(newarr)

"""
Create a filter array that will return only values higher than 42.
"""
arr = np.array([41, 42, 43, 44])
filter_arr = []

for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)

"""
Create a filter array directly from the main arr.
"""
arr = np.array([41, 42, 43, 44])
filter_arr = arr > 42 #here array amazing created in python.
newarr = arr[filter_arr]
print(filter_arr)
print(newarr)


filter_arr = arr % 2 == 0 # Only take even elements.




















