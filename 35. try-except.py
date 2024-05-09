"""
Try block lets test a block of code for errors.
except block lets handle the error.
The elsw block lets execute cod when there is no error.
The finally block lets execute code, regardless of the result of the try and except blocks.
"""
"""
The try block will generate an exception, because x is not defined:
"""

try:
    print(x)
except:
    print("An exception occurred.")
#######
try:
    print(x)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")
#######
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

#######

try:
    f = open("demofile.txt")
    try:
        f.write("Lorum Ipsum")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")


"""
Raise an exception if occur:
"""
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

"""
Raise keyword is used to raise an exception.
You can define what kind of error to raise, and the text to print to the user.
"""
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")











