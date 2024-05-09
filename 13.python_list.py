"""
When we say that lists are ordered, it means that the items have a defined order, and that order
will not change. if you add new items to list, the new items will be placed at the end of the list.
The list is changeable meaning that we can change, add, and remove items in a list after it has been created.
"""
"""
allow duplicates.

"""
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

"""
listlenght:
len(thislist)
"""
print(len(thislist))

"""
A list wit different types of data.
"""
list1 = ["abc", 34, True, 40, 'm']
print(list1)

"""
Access list:

"""
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist[1])

# print from last
#last one
print(thislist[-1])

#2nd from last
print(thislist[-2])

# 3rd to fifth
print(thislist[2:5])


#1st to fifth
print(thislist[:4])

print(thislist[2:])

print(thislist[-4:-1])

"""
Change Item Value
"""
thislist[2] = "blackcurrant"
thislist[1:2] = ["blackcurrant", "watermelon"]

"""
insert items
Output: ['apple', 'blackcurrant', 'watermelon', 'watermelon', 'blackcurrant', 'apple', 'cherry']
"""
thislist.insert(2, "watermelon")
print(thislist)


"""
Add items
"""
thislist.append("orange")
print(thislist)

"""
Insert items
"""
thislist.insert(1, "banana")

"""
Extend List:
tropical is another list extend of thislist
"""
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)

"""
Extend method also can extend with any iterable object(tuples, sets, dictionaries etc.)
"""
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)


"""
remove specified item
"""
thislist.remove("banana")

"""
pop() last item
pop(idx) specified item
"""
thislist.pop(1)
"""
clear the list
"""
thislist.clear()

"""
delete the entire list
"""
del thislist
#then it will shows "this list is not defined"

"""
Loop through a list
"""
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

"""
Loop through the index numbers
"""
for i in range (len(thislist)):
    print(thislist[i])

"""
Using a while loop
"""
while i<len(thislist):
    print(thislist[i])
    i = i+1

"""
Loop using list comprehension
"""
[print(x) for x in thislist]


"""
List Comprehension 
"""
newlist = []
for x in thislist:
    if "a" in x:
        newlist.append(x)

print(newlist)


"""
Sortlist:
"""
thislist.sort()
thislist.sort(reverse = True)

"""
make a copy of a list with the copy() method:
"""
mylist = thislist.copy()

"""
make a copy with list() method
"""
mylist = list(thislist)

"""
join list:
"""








