"""
File handling is an important part of any web application.
Python has several functions for creating, reading, updating, and deleting files.

open() function takes two parameters; filename and mode.

There are four different methods (modes for opening a file:
"r" - Read: default value. Opens file for reading, error if the file does not exist.
"a" - Append: Opens a file for appending, creates the file if it does not exist.
"w" - Write: Opens a file for writing, creates the file if it does not exist.
"x" - Create: Creates the specified file, returns an error if the file exists.

"t" - Text: Default value. Text mode.
"b" - Binary: Binary mode(e.g. images)
"""
f = open("demofile.txt")
f = open("demofile.txt", "rt")
