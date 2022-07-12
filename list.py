#list is a sequence data type in python which contains different type of items, list is mutable data type
l1 = [34,56,543,6,7,43,"hi", "yes", True,34.56]
print(l1)
#accessing list elements
print(l1[3])
#accessing sequence of elements
print(l1[3:8:2])
#to append new data into the list
l1.append(34)
print(l1)
#insert element
l1.insert(4,"bye")
print(l1)
#insert sequence of elements
l2 = ["hey","how","are","you"]
l1.extend(l2)
print(l1)
#to remove specific element from the list
l1.remove(56)
print(l1)
#to remove from index
l1.pop(7)
print(l1)
#to delete all the element from the list
l1.clear()
print(l1)
#to delete entire list
del l1
#print(l1)
#accessing all the element of list l2
for i in l2:
    print(i, end = " ")
print()
l3 = [1,2,3,4,5,6,5,34,23,4,5,6,6,56,4,3,4,5,6,7]
#count any element of the list
print(l3.count(4))
#to sort list
l3.sort()
print(l3)
#to reverse list
l3.reverse()
print(l3)
#to copy the list
l4 = l3.copy()
print(l4)