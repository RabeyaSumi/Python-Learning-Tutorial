"""
A variable created inside a function belongs to the local scope that function
    and can only be used inside the function and can use in any function of that function
"""
def myfunc():
    x = 300
    def myinnerfunc():
        print(x)
    myinnerfunc()

myfunc()

"""
A variable created in the main body of the python code is a global variable and belongs
    to the global scope. Global variables are available from within any scope, global and local.
    
"""
x = 300

def myfunc():
    print(x)

myfunc()
print(x)

"""
If we create a variable with same name one is globally and another is locally, 
    then local function will take the local one and global one will behave globally.
"""
x = 300
def myfunc():
    x = 200
    print(x)

myfunc()

print(x)

"""
If we need to create a global variable locally, we need to use global keyword.
"""
def myfunc():
    global x
    x = 300
myfunc()
print(x)

"""
If we nee to change a global variable in the local function, we need to 
refer variable by using the global keyword.
"""
x = 300
def myfunc():
    global x
    x = 200

myfunc()
print(x)    #will print 200.





















