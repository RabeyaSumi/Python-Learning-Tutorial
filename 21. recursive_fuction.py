"""
recursion means a defined function can call itself. The developer should be very careful with
recursion as it can be quite easy to slip into writing a function which never terminates or one that
uses excess amounts of memory or processor power.
"""
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print (result)
    else:
        result = 0
    return result

print("\n\nRecursion Example Results")
tri_recursion(6)

