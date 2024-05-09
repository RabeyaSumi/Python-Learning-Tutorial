a = 33
b = 33

if b > a:
    print("b is greater than a")

elif a < b:
    print("a is less than b.")
else:
    print("a is greater than b.")

"""
One line if else statement:
This technique is known as Ternary Operators, or Conditional Expressions.
"""
a = 2
b = 330
print("A") if a > b else print("B")

#One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a==b else print("B")

"""
or :
"""
c = 155
if a > b or a > c:
    print("At least on e of the conditions id True.")

"""
not:
"""
if not a > b:
    print("a is NOT greater than b.")

"""
Nested condition:
"""

"""
pass: If statements cannot be empty, but if you for some reason have an if statement 
with no content, put in the pass statement to avoid getting an error.
"""
a = 33
b = 200

if b > a:
    pass


