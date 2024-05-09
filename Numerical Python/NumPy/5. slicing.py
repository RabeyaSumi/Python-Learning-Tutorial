"""
Slicing in python means taking elements from one given index to another given index.
We pass slice instead of index like this:[start:end].
We can also define the step, like this: [start:end:step].
If we don't pass start its considered 0.
If we don't pass end its considered length of array in that dimension.
If we don't pass step its considered 1.
"""
"""
Slice elements from index 1 to index 5 from the following array.
"""
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

"""
Slice elements from index 4 to the ens of the array.
"""
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[4:])

"""
Slice elements from the beginning to index 4 (not included).
"""
print(arr[:4])

"""
Use the step value to determine the step of the slicing.
"""
print(arr[1:5:2])

"""
Slicing 2D array:
From the second element, slice elements from index 1 to index 4 (not included).
"""
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4]) #from the second element from index 1 to index 4.
























