"""
A RegEx, or regular expression is a sequence of characters that froms a search pattern.
RegEx can be used to check if a string contains the specified search pattern.
Python has a built-in package called re, which can be used to work with regular expressions.
re module offers a set of functions that allows us to search a string for a match:
"""
import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
if x:
    print("YES! WE have a match!")
else:
    print("No match.")

"""
findall() returns a list containing all matches.
"""
txt = "The rain in Spain"
x = re.findall("ai", txt)
print(x)

"""
search() searches the string gor a match and returns a match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned.
"""
txt = "The rain in Spain"
x = re.search(r"\s", txt)  #r mean the raw string, it prevent from invalid scope.
print("The first white-space character is located in position:", x.start())

"""
split() function returns a list where the string has been split at each match.
"""
txt = "the rain in Spain"
x = re.split(r"\s", txt) #r mean raw string
print(x)

"""
we can control the number of occurrences by specifying the maxsplit parameter.
"""
txt = "The rain in Spain"
x = re.split(r"\s", txt, 1)
print(x)

"""
The sub() function replaces the matches with the text of your choice.
"""
x = re.sub(r"\s", "9", txt)
print(x)

"""
we can use count parameter here.
"""
x = re.sub(r"\s", "9", txt, 2)
print(x)
"""
span() returns a tuple containing the start and end positions of the match.
"""
txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

"""
string() print the whole string passed into the function.
group() print the part of the string where there was a match.
"""
x = re.search(r"\bS\w+", txt)

print(x.string)
print(x.group())














