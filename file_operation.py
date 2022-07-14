import os
#creating file 
#f = open("file3.txt", "x")
#open a file from current directory
#f = open("file1.txt")
#reading that file
#print(f.read())
#closing the file
#f.close()
"""
#open a file from different directory
f = open("/home/ubox96/Documents/file2.txt")
print(f.read())
f.close()

#opening file in different mode"""
#opening file in write mode
f = open("file3.txt",'w')
f.write("This is file 3")
f.close()
#opening file after writing new contant in it
print("file3 after writing data into it")
f = open("file3.txt")
print(f.read())
f.close()

#appending data into file2
f = open("file3.txt",'a')
f.write("\band appending new data in it")
f.close()


#reading file data after appending new data
print("file3 after appending data into it")
f = open("file3.txt")
print(f.read())
print("position of file")
print(type(f.tell()))
s = f.tell()
print(f.read(s))
f.close()
f.fileno
#deleting file
os.remove("file3.txt")

print("Execution done")
#f = open("file3.txt") - this line of code will show error because it has been deleted.
