"""
Assume we have the following file, located in the same folder as python.

To open the file, use the built-in open() function.
The open() function returns a file object, which has a read() method for reading the content
of the file.
"""
f = open("demofile.txt", "r")
print(f.read())

"""
If the file on a different location, we need to specify the file path.
"""
"""
return the 5 first characters of the file on the read mode.
"""
print (f.read(5)) #whole file read already. so the pointer is on the end of the file.

"""
By calling readline() two times , you can read the two first lines.
"""
f = open("demofile.txt", "r")
print(f.readline())
print(f.readline())

"""
By looping through the lines of the file, you can read the whole file, line by line.
"""
f = open("demofile.txt", "r")
for x in f:
    print(x)

"""
Close the file when are finish with it.
"""
print(f.readline())
f.close()

