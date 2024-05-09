"""
A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
lambda arguments : expression
"""
x = lambda a : a + 10
print(x(5))

"""
Multiple arguments.
"""
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

"""
myfunc(n) return double. a lambda arguments return.
"""
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))