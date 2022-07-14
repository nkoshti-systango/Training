import os
print("python directory")
print("current working directory is: ",os.getcwd())
print("cwd as bite object is: ",os.getcwdb())
print(os.listdir())
#for making new directory
#os.mkdir("/home/ubox96/downloads/new")
print(os.getcwd())
#for changing working directory
os.chdir("/home/ubox96/downloads/new")
print(os.getcwd())
os.remove("file1.txt")
f = open("file1.txt")
print(f.read())
