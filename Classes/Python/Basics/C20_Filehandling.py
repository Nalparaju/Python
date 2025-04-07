#File handling
''' This is used to store data permanently.
A process of creating, opening, reading, writing, appending and closing files '''

#Types of files in file handling
'''
1. Text file
2. Csv file
3. Json file
4. Excel file'''

#Steps for file handling
'''
1. open
2. read/write
3. process
4. close'''

#Syntax:
'''file = open("filename.txt",mode)'''

#modes:
'''6 Modes of opening a file
1. r    >>> read mode
2. w    >>> write mode (If file doesnt exist, it will create a new file... If file exist and data exist >> it will override the data in it)
3. a    >>> append mode (This won't erase existing information) ne
4. rb   >>> read binary
5. wb   >>> write binary
6. r+   >>> read & write
'''

#Built-in methods:

#read()         >>> To read entire content at once
#readline()     >>> To read only 1 line at a time
#readlines()    >>> Reads all lines and returns as a list

#write()        >>> To write data into a file and overrides the old data
#Syntax: .write("data")

#append()       >>> To append the data at the end of the file, without deleting the old data
#syntax: .append("xyz")

#close()        >>> To close the file

#tell()         >>> It will show the current cursor position

#seek()         >>> To move the cursor position to a specific position

