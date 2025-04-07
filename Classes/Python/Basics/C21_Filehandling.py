#Opening a file in read mode
f = open("/Users/pranith/Python/Screenshots&Files/file.txt","r")
print(f.read())
f.close()

f = open("/Users/pranith/Python/Screenshots&Files/filewrite.txt","w")
f.write("Writing Example from class 21")
f.close()

f = open("/Users/pranith/Python/Screenshots&Files/filewrite.txt","r")
print(f.read())
f.close()

f = open("/Users/pranith/Python/Screenshots&Files/filewrite.txt","a")
f.write("\nAppend example for exisiting file")
f.close()

f = open("/Users/pranith/Python/Screenshots&Files/filewrite.txt","r")
print(f.read())
f.close()

f = open("/Users/pranith/Python/Screenshots&Files/filewrite.txt","r")
print("Current Cursor Position", f.tell())
f.close()

f = open("/Users/pranith/Python/Screenshots&Files/filewrite.txt","r")
print("Current Cursor Position", f.tell())
f.seek(10)
print("Current position is", f.read())
f.close()

# %%
#Readlines function example
f = open("/Users/pranith/Python/Screenshots&Files/filewrite.txt","r")
print("Line 1:",f.readlines())
f.close()
# %%
# %%
#Insert a specific position example
f = open("/Users/pranith/Python/Screenshots&Files/file2Position.txt","w")
f.write("Hello Pranith!!")
f.close()

f = open("/Users/pranith/Python/Screenshots&Files/file2Position.txt","r+")
data = f.read()
print("before inserting:",data)

f.seek(5)
f.write("Good boy!!")
f.write(data[5:])
f.close()

f = open("/Users/pranith/Python/Screenshots&Files/file2Position.txt","r")
print("after insertion:",f.read())
f.close()
