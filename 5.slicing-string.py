"""
a range of characters from string can be return by slicing syntax.
"""
b = "Hello, World!"
print (b[2:5])

"""
slice from the start.
"""
print(b[:5])

"""
By leaving out the end index, the range will go to the end:
"""
b = "Hello, World!"
print(b[2:])

"""
use negative indexing to start the slice from the end of the string.
"""
print(b[-5:-2])