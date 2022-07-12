#tuple are immutable data type and contains different type of data
from socket import CAN_RAW


t = (45,233,5,"yes",False,"nice",6.8)
#to accessing any element
print(t[3])
#to accessing sequence of element
print(t[2:6])
#join two tuples
t2 = (4,5,6,7)
t3 = t + t2
print(t3)
car = ("volvo","eicher","toyota")
#unpacking tuple
(volvo,eicher,toyota) = car 
print(volvo)
print(toyota)
#to iterate all element of tuple
for i in t:
    print(i, end = " ")
print()
#to count number of occurance of any element in tuple
print(t.count(45))
#to see the index of any value
print(t.index(6.8))
#to delete the tuple
del t
#print(t)
print("tuple has been deleted")