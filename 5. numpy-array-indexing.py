"""
Array indexing is the same as accessing an array element.

"""
import numpy as np
arr = np.array([ [1, 2, 3, 4, 5], [6, 7, 8, 9, 10] ])
print('2nd element on 1st row: ', arr[0, 1]) #2nd element of 1st row.

"""
3D array.
"""
#1st dimension contain two value. 2nd dimension contain two value. 3rd dimension
#contain three value.
arr = np.array([ [[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]] ])
print(arr[0, 1, 2]) # 6 will be printed.

"""
Use negative indexing to access array from the end.
"""
print(arr[-1, -1, -3]) #10 will be printed
#in 1st dimension last array, 2nd dimension last array, 3rd dimension -3 is first column.














