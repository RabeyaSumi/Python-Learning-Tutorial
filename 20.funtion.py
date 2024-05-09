"""
A function is a block of code which only runs when it is called.
You can pass data, known as parameters, into a function.
A function can return fata as a result.
In python s function is defined using the def keyword:
"""
def my_function():
    print("Hello from a function.")

my_function()

"""
Arguments pass:
"""
def my_function(fname):
    print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

def my_funtion(fname, lname):
    print(fname + " " + lname)

my_funtion("Rihana", "Tabassum")

"""
if we pass one argument compile will shows error, because this function deserve two arguments.
-Arbitrary arguments: *args that will actually set parameter as a block of memory.
If you fon know how many arguments that will be passed into your function,
add a '*' before the parameter name.
"""
def my_function(*kids):
    print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

"""
Keyword arguments: we can also send arguments with key = value syntax.
"""
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")

"""
-Arbitrary keyword arguments: **kwargs.
If we do not know how many keyword arguments that will be passed into your function
    and two asterisd: ** vefore the parameter mane in the function definition.
This way the function will receive a dictionary of arguments, and can access the items accordingly.
"""
def my_function(**kid):
    print("His last name is " + kid["lname"])

my_function(fname = "Tovias", lname = "Refsnes")

"""
Default Parameter Value: Thr following example shows how to use a default parameter value. If we call the 
function without argument, it uses the default value:
"""
def my_function(country = "Norway"):
    print ("I am from " + country)

my_function("Sweden")
my_function("Indis")
my_function()
my_function("Brazil")

"""
Passing a List as an Argument: We can senf any date types of argument to a function (string, number,
list, dictionary etc.), and it willbe treated as the same data type inside the function.
"""
def my_function(food):
    for x in food:
        print(x)

fruits = ["apple", "banana", "cherry"]
my_function(fruits)

"""
Return Values: To let a function return a value, use the return statement.
"""
def my_function(x):
    return 5*x

print (my_function(3))


"""
The pass statement: if someone want no content in the function can white pass statement.
"""

def myfunction():
    pass

"""
Positional-Only Arguments: To specify that a function can only have positional arguments, add, , / after the arguments.
"""
def my_function(x, /):
    print(x)

my_function(3)

"""
Combine Positional-Only and keyword-only:
"""

def my_function(a, b, /, *, c, d):
    print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)




















