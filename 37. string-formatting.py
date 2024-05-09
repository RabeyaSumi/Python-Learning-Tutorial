"""
To make sure a string will display as expected, we can format the result with the format()
method.
To control such values, add placeholders (curly brackets {} ) in the text, and run the values through the format()
method.

"""

price = 49
txt = "The price is {} dollars"
print(txt.format(price))

"""
Format the price to be displayed as a number with two decimals.
"""
txt = "The price is {:.2f} dollars"
print(txt.format(price))

"""
If we want to use more values, just add more values to the format() method.
"""
quantity = 3
itemno = 567
price = 49
myorder = "I want {} pieces of item number {} for {:.2f} collars."
print (myorder.format(quantity, itemno, price))

"""
We can use index numbers (a number inside the curly brackets {0} ) to be sure the values are
placed in the correct placeholders.
"""
quantity = 3
itemno = 567
price = 49
myorder = "I want {0} pieces of item {1} for {2:.2f} dollars."
print(myorder.format(quantity, itemno, price))

"""
Named indexes:
we can also use named 
"""

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Ford", model = "Mustang"))














