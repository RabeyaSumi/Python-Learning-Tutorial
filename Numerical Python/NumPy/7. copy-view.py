"""
The main difference between a copy and view of an array is that the copy is a new array,
and the view is just a view of the original array.
The copy owns the data and any changes made to the copy will not affect original array, and any changes made
 to the original array will not affect the copy.

The view does not own the data and any changes made to the view will affect the
original array, and any changes made to the original array will affect the view.

"""
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr)
print(x)

"""
The view should be affected by the changes made to the original array.
"""
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
x[0] = 31
print(arr)
print(x)

"""
As mentioned above, copies owns the data, and views does not own(...) the data, but how can we check this?
Check if array owns its data: 
Every NumPy array has the attribute base that returns None if the array owns the data.
Otherwise, the base attribute refers to the original object.
"""
x = arr.copy()
y = arr.view()

print(x.base)
print(y.base)












