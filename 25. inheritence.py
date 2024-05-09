"""
Inheritance allows us to define a class that inherits all the methods and properties
from another class.
Parent class is the class being inherited from, also called base class.
Child clsss is the class that inherits from another class, also called derived class.
"""
"""
Create a parent class: 
"""
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

x = Person("John", "Doe")
x.printname()

"""
Create a child class:
To create a class that inherits the functionality from another class, send the parent
class as a parameter when creating the child class:
"""
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    pass
x = Student("Mike", "Olsen")
x.printname()

"""
Use the super() Function: Python also has a super() function that will make the chikd 
class inherit all the methods and properties from its parent:
"""
class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __int__(self, fname, lname):
        super().__init__(fname, lname)

x = Student("Mike", "Olsen")
x.printname()

"""
Add Properties:
Add a property called graduationyear to the Student class:
"""
c















