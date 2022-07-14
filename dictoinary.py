#creating dictionary
d = {"red":3,"blue":4,"green":5,"black":5,"yellow":5}
print(d)
#find length of dictionary
print(len(d))
#accessing items of dictionary
for i in d:
    print(i,":",d[i],end = " , ")
print()
for i,j in d.items():
    print(i,j, end = " ")
print()
print(d.get("red"))
#to print all the keys present in dictionary
print(d.keys())
#to print all the values present in dictionary
print(d.values())
#to change any key's value
d["red"] = 4
print(d)
#to update dictionary
d.update({"brown":5})
print(d)
#add items in dictionary
d["pink"]=4
print(d)
#to remove specific item from dictionary
d.pop('pink')
print(d)
del d['brown']
print(d)
#to remove last element from the dictionary 
d.popitem()
print(d)
#to copy dictionary 
e = d.copy()
f = dict(d)
print(e)
print(f)
#creating nested dictionary
company = {"emp1":{"id":12,"add":"nn"},
           "emp2":{"id":22,"add":"oo"},
           "emp3":{"id":32,"add":"pp"}}
print(company)
print(type(company))