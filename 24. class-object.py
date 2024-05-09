"""
A class is like an object constructor, or a "blueprint" for creating objects.
"""
class MyClass():
    x = 5

p1 = MyClass()
print(p1.x)

"""
in real life application we have to use __init__() function.
All classes have a function called __init__(), which is always executed when the class
is being initiated.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)
"""
The __str__() function: the __str__() function controls what should be returned when
the class object is represented as a string.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}({self.age})"

p1 = Person("John", 36)
print(p1)

"""
Object Methods:
Objects can also contain methods. Methods in objects are functions that belong to 
the object. 
myfunc() print a greeting and execute myfunc() for the p1 object.
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()

"""
The self Parameter: the self parameter is a reference to the current instance of the
class, and is used to access variables that belongs to the class.
It does not have to be named self, you can call it whatever you like, but it has to 
the first parameter of any function in the class.
used mysilyobject instead of init.

class Person:
    del __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    def myfunc(abc):
        print("Hello my name is " + abc.name)
p1 = Person("John", 36)
p1.myfunc()

"""

"""
Modify object property:
Delete object property: 
"""

p1.age = 40
print (p1.age)

del p1.age














