"""
"a" - Append: will append to the end of the file.
"w" - Write: will overwrite any existing content.
"""
f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()
f = open("demofile.txt", "r")
print(f.read())


f = open("demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()
f= open("demofile.txt", "r")
print(f.read())

"""
To create a new file in python, use the open() method, with one of the following parameters.
"x" - Create: will create file, returns an error if an file exist with the same name.
"a" - Append: will create a file if the specified file does not exist.
"w" - Write: will create  a file if the specified file does not exist.
"""
f = open("newfile2", "x")
open("newfile3", "w")
"""
second time running the code not create the same file rather it's throw exception.
"""