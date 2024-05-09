"""
variable declared outside of the function is global variable.
"""
x = "awesome"

def myfunc():
    x = "fantastic"
    print ("Python is " + x)

myfunc()
print("Python is " + x)