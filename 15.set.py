"""
Sets are used to store multiple items in a single variable.
Sers used to store collections of data.
Three others objects which used to store collection list, tuple and dictionary.
A ser is a collection which is unordered, unchangeable*, and unindexed.
Set are written with curly brackets.
"""
thisset = {"apple", "banana", "cherry"}
print(thisset)

"""
Set items are unordered, unchangeable, and do not allow duplicate values.
-Unordered means that the items in a set do *not have a defined order*.
    set items can appear in a different order every time you use them, and cannot be 
    referred to by index or key.
-Unchangeable: set items are unchangeable, meaning that we cannot we cannot change
    the items after the set has been created.
    once set is created, you cannot change its items, but you can remove items and add new items.
-Duplicate: duplicate not allowed in set. Duplicate values will be ignored.
"""
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

thisset = {"apple", "banana", True, 1, 2}
print(thisset) #True and 1 consider as same and also for False and 0.

"""
-Datatype: set can in any datatype.
"""
set1 = {"abc", 34, True, 40, "male"}
print(set1)

"""
-Set constructor: 
"""
thisset = set(("apple", "banana", "cherry"))
print(thisset)

"""
-Access set items: 
"""
for x in thisset:
    print(x)

print("banana" in thisset) #return true as banana in thisset.

"""
-Add set items:
"""
thisset.add("orange")
print(thisset)

"""
-Update element by another tropical set.
-Update element by another list mylist.
"""
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

mylist = ["kise", "orange"]
print(thisset)

"""
-To remove an items use the remove() or the discard() method.
 If item which to remove does not exist, discard() will not raise an error.
 We can use pop() method to remove an item, but this method will remove a rendom item.
"""
thisset.remove("banana")
print(thisset)
thisset.discard("banaba")

"""
-clear() method empty the set.
-del keyword will delete entire set.
"""
thisset.clear()
del thisset

"""
Loop items:
"""
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

"""
-Join set:
union() method, update() method.
"""
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

set1.update(set2)
print(set1)

"""
-difference(), return a set containing the difference of first set.
-difference_update(), update the set with difference items.
"""

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
x.difference_update(y)
print(z)
print(x)

"""
-intersertion(), return the intersection of two or more sets.
-intersection_update(), 
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
x.intersection_update(y)
print(z)
print(x)
# x has only item "apple".
"""
-isdisjoint(), returns whether two sets have a intersection or not.
    Output: for x, y output is False.
-issubset(), return whether another set contains this set or not.
"""
print(x.isdisjoint(y))
print(x.issubset(y))

"""
-issuperset(), 
"""
A = {1, 4, 8, 2, 5}
B = {1, 5, 4}
print(A.issuperset(B))

"""
-symmetric_difference(), return a set with the symmetric difference of two set.
 take all differences from both sets.
-symmetric_difference_update(), update with symmetric difference.
"""
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.symmetric_difference(y)
x.symmetric_difference_update(y)

print(z)
print(x)






























