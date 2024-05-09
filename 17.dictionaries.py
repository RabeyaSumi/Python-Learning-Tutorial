"""
Dictionaries are used to store date values in key:value pairs like structure.
A dictionary is a collection which is ordered*, changeable and do not allow duplicates keys.
Dictionary are written with curly bracket and have keys and values.
A dictionary items are ordered and changeable, and do not allow duplicate.
In current versions dictionary are ordered.
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

print(len(thisdict))

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)

"""
The dict() constructor:
"""
thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)

"""
-Accessing Items:
"""

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys() #list return.
print(x)
car["color"] = "white" #added another item.
print(x) #keys will update autometically.

x = car.values() #get values().
print(x)

car["color"] = "gray" #change a key value.

x = car.items() #get a list of the key:value pairs.
print(x)

"""
Check if key exists.
"""
if "model" in car:
    print("Yes, 'model' is one of the keys in the car dictionary")

"""
Change item by update.
"""
car.update({"color": "silver"})
print(car["color"])

"""
pop(), popitem() , clear(), and del :
"""
car.pop("year")
car.popitem() #pop last item.
car.clear()
del car #delete entire dictionary.

"""
Loop dictionaries.
"""
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

for x in thisdict:
    print(x)             #x take keys, print keys.

for x in thisdict:
    print(thisdict[x])   #print key values.

for x in thisdict.values():
    print(x)             #x takes values.

for x in thisdict.keys():
    print(x)

for x, y in thisdict.items():
    print(x, y)

"""
To copy we can use copy() or dict() method.
"""
mydict = thisdict. copy()
print(mydict)
mydict = dict(thisdict)
print(mydict)


"""
Nested dictionary.
"""
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2025
    },
    "child2": {
        "name": "Nehma",
        "year": 2029
    },
    "child3": {
        "name": "Linus",
        "year": 2033
    }
}

print(myfamily["child2"]["name"])

child1 = {
    "name": "Emil",
    "year": 2025
}
child2 = {
    "name": "Nehma",
    "year": 2029
}
child3 = {
    "name": "Linus",
    "year": 2033
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

"""
fromkeys() method.
always take whole value of y.
"""
x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print(thisdict)

"""
get() method use to assign a value from dictionary.
"""
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

x = car.get("model")
print(x)

x = car.get("price", 150000)
print(car)

"""
setdefault() method returns the value of the item with the specified key. If the key 
does not exist, insert the key, wth the specified value, see example below.
"""
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.setdefault("color", "white")
print(x)















