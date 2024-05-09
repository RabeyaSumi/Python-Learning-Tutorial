"""
capitalize(), converts the first character to upper case.
"""
str = "string"
print(str.capitalize())

"""
casefold(), converts string into lower case.
"""
print(str.casefold())

"""
center(), return a centered string.
"""
print(str.center(11, '*'))

"""
count(), returns the number of times a specified value occurs in a string.
"""
txt = "I love strawberry, strawberry is my favorite food."

print(txt.count("strawberry"))

"""
cncode(), rreturns and enncoded version of the string
"""
print(txt.encode())

"""
endswith(), returns true if the string ends with the specified value
"""
print(txt.endswith(" food."))

"""
expandtabs(), sets tab size of the string, its substitute all \t, replace with tab size 
"""
txt = "I love strawberry, \t strawberry is my favorite food."
print(txt.expandtabs(30))

"""
find(), searches the string for a specified value and returns the position 
 of where it was found
"""
print(txt.find("love"))

"""
rfind(), returns the rightmost index of the substring if found in the given string.
If not found then it returns -1.
Output: 
"""

"""
format(), formats specified values in a string
"""
txt = "I need {} quantity of pencils, which size {} inch of price {}."
print (txt.format(3, 5, 20))

"""
format_map(), formats specified values in a string
"""
mp = {'x':'Jogn', 'y':'Wick'}
txt = "{x}'s last name is {y}."
print(txt.format_map(mp))

"""
The main difference is that Python find() produces -1 as output 
if it is unable to find the substring, whereas index() throws a ValueError exception.
"""
txt = "I love strawberry, strawberry is my favorite food."
print (txt.find("him"))

"""
isalnum(), returns true if all characters in the string are in the alphebet
"""
print (txt.isalpha())

"""
isascii(), returns true if all characters in the string aer ascii characters
"""
print(txt.isascii())

"""
isdecimal(), returns true if all characters in the string are decimals
"""
decall = "123567890"
print(txt.isdecimal())
print(decall.isdecimal())

"""
isdigit(), return true if all characters in the string are digits
"""
print(decall.isdigit())

"""
isidentifier(), returns true if the string is an identifier
"""
str_all = "age_25"
print(str_all.isidentifier())

"""
islower(), returns true if all characters in the string are numeric
"""
print(decall.isnumeric())

"""
isprintable(), return true if all character in the string are printable
"""
str = "my name is \n Rabeya."
print(str.isprintable())

"""
isspace(), returns true if all characters in the string are whitespace
"""
str = "            "
print(str.isspace())

"""
istitle(), returns true if the string follows the rules of a title
"""
str = "Rabeya Sumi"
print(str.istitle())

"""
isupper(), return true if all characters in the string are upper case
"""
str = "RABEYA"
print(str.isupper())

"""
join(), joins the elements of an iterable to the end of the string
"""
"""
join all items in a tuple int a string, using a hash character as separator
"""
"""
join all items in a dictionary into a string, using the word "TEST" 
as separator
"""
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
print(x)

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"
x = mySeparator.join(myDict)
print(x)

"""
ljust(), returns a left justified version of the string with set spaces.
Also can use a padding character.
"""
str = "This is"
print(str.ljust(10))

print(str.ljust(20, "P")) #width and fillchar

txt = "banana"
x = txt.ljust(20, "O")
print(x)

"""
lower(), convert a string into lower case character.
"""
str = "Have To Convert In Lowercase"
print(str.lower())

"""
strip(), returns a trim version of the string.
lstrip(), returns a left trim version of the string.
rstrip(), returns a right trim version of the string.
"""
str = "   mystring     "
print(str.lstrip())
print(str.rstrip())
print(str.strip())

"""
maketrans(), returns a translation table to be used in translations.
str.maketrans(x, y):
str.maketrans(x, y, z):
x: Specifies the list of characters that need to be replaced.
y: Specifies the list of characters with which the characters need to be replaced.
z: Specifies the list of characters that need to be deleted.
"""
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))

"""
partition(), spilits the string at the first occurrence of the separator and returns a tuple.
Output: ('I love', 'skate', ' dancing.')
"""
str = "I love skate dancing."
print(str.partition("skate"))

"""
replace(), returns a copy of the string where occurrences of a substring are replaced with another substring.
Output: Good Bye World 
"""
str = "Hello World"
pat = str.replace("Hello", "Good Bye")


"""
rfind(), rindex() searches the string for a specified value and returns the last position of where it was found
output: 2
"""
print(str.rfind("llo"))
print(str.rindex("llo"))



"""
rjust(), returns a right justified version of the string.
"""
print(str.rjust(30))


"""
rpartition(), returns a tuple where the string is parted into therr parts.
"""
print(str.rpartition("llo"))


"""
rstrip(), remove the trailing cheracters if they are commas, periods, s, q, w.
"""
txt = "banana,,,,,ssqqqww....."
x = txt.rstrip(",.qsw")
print(x)


"""
split(), splits the string at the specified separator, and returns a list.
"""
print(str.split("o"))

"""
splitlines(), splits the string at line breaks and a list.
"""
txt = "my string\nanother line\nmore line"
print(txt.splitlines())


"""
startwith(), returns true if the string starts with the specified value.
"""
print(txt.startswith("m"))


"""
swapcase(), lower case becomes upper case and vice versa.
"""
print(str.swapcase())


"""
title(), converts the first character of each woed to upper case
output: correct name.
"""
str = "suMi Sultana"
print(str.title())

"""
translate(), returns a translated string.
"""
#use a dictionary with ascii codes to replace 83 (S) with 80 (P):
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))
#third parameter in the mapping table describes characters that you want to remove from the string
txt = "Good night Sam!"
x = "mSa"
y = "eJo"
z = "odnght"
mytable = str.maketrans(x, y, z)
print(txt.translate(mytable))

txt = "Good night Sam!"
mydict = {109: 101, 83: 74, 97: 111, 111: None, 100: None, 110: None, 103: None, 104: None, 116: None}
print(txt.translate(mydict))



"""
zfill(), fills the string with a specified number of 0 values at the beginning
"""
text = "geeks for geeks"

print(text.zfill(25))

print(text.zfill(20))

# Given length is less than
# the length od original string
print(text.zfill(10))





