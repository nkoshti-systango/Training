#set is a group of non repeated elements and it is unordered
s = {"a", "b", "c",4,5,6,7,5,3,5,6,7}
print(s)
#for accessing elements of set
for i in s:
  print(i, end = " ")
print()
#to add elements in set
s.add("e")
print(s)
#to add iterable items in set
s1 = {101,102,103,104}
s.update(s1)
print(s)
#to remove any element from the set
s.remove(101)#if item is not present in the set remove will raise the error
s.discard(101)#if item is not present in the set remove will not raise the error
#s.remove(101)
s4 = {3,4,5,6,7}
s5 = {101,3,4,5,4,4,5,6,78,9,7,65}
t = s4.union(s5)
print(t)
t2 = s4.intersection(s5)
print(t2)
t4 = s4.difference(s5)
print(t4)