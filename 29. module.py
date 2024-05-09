"""
Consider a module to be the same as a code library.
Module need to be save with a python extension.
Then we can use the module by using the import statement.
Module can be renamed like "import mymodule as mx"
There are several built-in modules in Python, which you can import.
    for built-in module "import platform".
"""
"""
There is a built-in function to list all the function names in a module. The dir() function.
"""
import platform   #platform is a built-in module.
x = dir(platform)
print(x)

"""
You can choose to import only parts from a module, by using the from keyword.
"""
def greeting(name):
    print("Hello, " + name)

person1 = {
    "name": "John",
    "age": 36,
    "country": "Norway"
}

#We can import like :
#from mymodule import person1





