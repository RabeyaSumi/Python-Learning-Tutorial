"""
Python Polymorphism: The word "polymorphism" means "many forms", and programming it
refers to methods/functions/operators with the same name that can be executed on many
objects or classes.
"""
"""
Function Polymorphism: An example of a python function that can be used on different objects
is the len() function.
For strings len() returns the number of characters.
For tuple len() returns the number of items in tuple.
For dictionaries len() returns the number of key/value pairs in the dictionary.

Another example is, say we have three classes: Car, Boat and Plane they all have a
method move().
"""
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")
class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")
class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    x.move()

"""
Inheritance Class Polymorphism: Create a class called vehicle and make Car, Boat, Plane
child classes of Vehicle:
"""
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    def move(self):
        print("Sail!")
class Plane(Vehicle):
    def move(self):
        print("Fly!")

car1 = Car("Ford", "Mustang")
boat1 = Boat("Ibiza", "Touring 20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()












