"""
By default python have these data types:
    strings, integer, float, boolean, complex.
Numpy has some extra data types, and refer to data types with one character like i
for integers, u fpr unsigned integers etc.
    i-integer, b-boolean, f-float, c-complex float, m-timedelta, m-datetime, o-object
    s-string, u-unicode string, v-fixed chunk of memory for other type(void)
"""

"""
Checking the data type: the numpy array object has a property called dtype that rerurns
the data type of the array.
"""
import numpy as np
arr = np.array([1, 2, 3, 5])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

"""
Creating arrays with a defined data type.
"""
arr = np.array([1, 2, 3, 4], dtype = 'S')
print(arr)
print(arr.dtype)

"""
For i, u, f, s, U we can define size as well.
here, create an array with data type 4 bytes integer.
"""
arr = np.array([1, 2, 3, 4], dtype = 'i4')
print(arr)
print(arr.dtype)

"""
what if a value can not be converted?
If a type is given in which elements can't be casted then numpy will raise a valueerror.

arr = np.array(['a', '2', '3'], dtype = 'i') ; can't be processed as integer.
"""

"""
Converting data type on existing arrays:
The best way to change the data type of an existing array, is to make a copy of the
    array with the astype() method.
"""
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)
print(newarr.dtype)

"""
change data type integer to boolean.
"""

arr = np.array([1, 0, 3])

newarr = arr.astype(bool)

print(newarr)
print(newarr.dtype)















