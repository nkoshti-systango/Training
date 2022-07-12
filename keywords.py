#1. and - logical operator and returns true if both the operands are true else returns false
print("keyword 1 - and")
print(True and True)
print(True and False)
print(False and False)
print("\n")

#2. or - logical operator and returns false if both the operands are false else returs trueprint(True and True)
print("keyword 2 - or")
print(True and False)
print(False and False)
print(True and True)
print("\n")

#3. not - logical oprator and returns true if operand is false and returns false if operand is true
print("keyword 3- not")
print(not True)
print(not False) 
print("\n")

#4. if - it is a conditional statement and executes if condition written inside if is true
print("keyword 4 - if")
if 5>4:
    print("Nice")
print("\n")

#5. elif - it is a condition statement used with an if statement the elif statement is executed if the previous conditions were not true
print("keyword 5 - elif")
i = -10
if i > 0:
    print("positive")
elif i < 0:
    print("negative")
else:
    print("zero")
print("\n")

#6. else - it is a conditional statement and execute if condition written inside if is not true
print("keyword 6 - else")
if 45==43:
    print("Equal")
else:
    print("not equal")
print("\n")

#7. for - it is a loop used for iteration and use when no. of iteration is known
print("keyword 7 - for")
for  i in range(0,11):
    print(i,end = " ")
print("\n")

#8. while - it is a loop used for iteration and use when no. of iteration is not known
print("keyword 8 - while")
i = 9
while i<34:
    print(i, end = " ")
    i+=1
print("\n")

#9. break - it is use to terminate loop at specific condition
print("keyword 9 - break")
i = 1
for i in range(19):
    if i == 20:
        break
    else:
        print(i, end = " ")
print("\n")

#10. as - it is use for alias
print("keyword 10 - as")
from re import T
import pandas as pd
print("pandas imported as pd, here pd is alias for pandas")
print("\n")

#11. def - it is use to create a function
print("keyword 11 - def")
def add(x,r):
    print(x+r)
s = add(5,6)
print(s)
print("\n")

#12. return - it is use to return a value and exit from the function
print("keyword 12 - return")
def prod(w,r):
    return w*r
c = prod(34,65)
print(c)
print("\n")

#13. lembda - it is used to define anonymous function
print("keyword 13 - lembda")
x = lambda  a : a**2
print(x(9))
print("\n")

#14. pass - It is used when a statement is required syntactically but you do not want any command or code to execute
print("keyword 14 - pass")
for i in range(15):
    if i%2==0:
        pass
    else:
        print(i, end = " ")
print("\n")

#15. True - it is a boolean value
#16. False - it is also a boolean value
print("keyword 15 - True")
print("keyword 16 - False")
print(True or False)
print(True and False)
print("\n")

#17,18,19. try, except and raise is use for exception handling
print("keyword 17 - try")
print("keyword 18 - except")
print("keyword 19 - raise")
"""try:
	raise NameError("Hi there") # Raise Error
except NameError:
	print ("An exception")
	raise # To determine whether the exception was raised or not
print(fun(10))
print(fun(0))"""
print("\n")

#20. continue - It continues to the next iteration of a loop
print("keyword 20 - continue")
i = 3
for i in range(3*10):
    print(i+1,end = " ")
    if i % 5 == 0:
        continue
print("\n")
   
#21. del - it is used for deleting any object
print("keyword 21 - del")
t = (4,5,6,4,"ef",4.5,64)
print("tuple is created")
print(t)
del t 
#print(t)
print("tuple is deleted using del keyword")    
print("\n")   



