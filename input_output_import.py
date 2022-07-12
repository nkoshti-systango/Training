#to take any input from user
num = input("Enter a number: ")
print(type(num))
#by default it takes as string but for changing we can use datatype or 'eval' keyword'
num = eval(input("Enter a number: "))
print(type(num))
#to show the output
print(num)

#import is used to import any module in python file
import os
print("os module is imported")