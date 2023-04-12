#1 - Opening a file open()
file_object = open("File_Name", "Access_Mode")

#Access modes:
# r / w / a / r+ / w+ / a+

#2 - Reading a file read()

#3 - Closing a file close()

#4 - Writing a file write()

#"a" - append
#"w" - write

#Opening/writing
f = open("test.txt", "w")
print(f)
f.write("Now it is the time")
f.write(" to close the file")
f.close()

#Opening/reading
f = open("test.txt", "r")
text = f.read()
print(text)
f = open("test.txt", "r")
print(f.read(5))
print(f.read(100006))

#Open/read/write
fo = open("foo.txt", "w")
fo.write("Python is a great language. \nYeah it's great")
fo = open("foo.txt", "r")
print(fo.read())
fo.close()

#Tell and Seek Methods
#Tell()
#Seek()

fo = open("foo.txt", "r+")
str = fo.read(17)
print("Our string is: ", str)
position = fo.tell();
print("Current file position ", position)

position = fo.seek(0,0)
print("Current file position ", position)
str = fo.read(17)
print("Again our string is: ", str)
fo.close()

#Try and expect clauses
try:
    fh = open("restfileee", "r")
    fh.write("this is my file for exception handling")
except IOError:
    print("Error: can not find file or read data")
else:
    print("Written content in the file successfully")

try:
    fh = open("testfile1", "w")
    fh.write("this is my file for exception handling")
finally:
    print("Finally!")
              
    

