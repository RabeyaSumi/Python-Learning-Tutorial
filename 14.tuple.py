"""
tuple are used to multiple items in a single variable.
tuple are written with round bracket.
tuple items are indexed.
take lower memery than list.
tuple can be accessed by negative index.
-Ordered: tuples are ordered, it means that the items have a defined order, and
    that order will not change.
-Unchangeable: cannot change, add or remove items after tuple has been created.
-Unpacking: tuple unpacking is taking every index value with variables.
"""
mytuple = ("apple", "banana", "cherry")

"""
access tuple items.
"""
print(mytuple[1])
print(mytuple[-2])



"""
-Unpacking: tuple unpacking it taking all items to the variables.
"""
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

"""
-Tuple loop: 
"""
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)


for i in range(len(thistuple)):
  print(thistuple[i])

"""
-One item's tuple: to create one item's tuple need to add a comma,
     otherwise python can't recognize it as a tuple.
"""
tpl1 = ("banana",)
print(tpl1)

"""
-Data type: tuple items can any data.
"""
tuple = ("abc", 45, "Thue", "female")
print(tuple)


"""
-Join tuple: to join tuple we can use '+' operator.
"""
t1 = ("a", "b", "c")
t2 = (1, 3, 3)
t3 = t1 + t2
print(t3)

"""
-count() method: count the occurence.
-index() method: return index of a value.
"""
print(t3.count(3))
print(t3.index('c'))









