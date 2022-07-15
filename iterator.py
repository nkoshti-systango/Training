import time
start = time.time()
l = ["apple", "banana", "cherry","pineapple","guvava"]
myit = iter(l)
for i in l:
    print(next(myit))
end = time.time()
print(end - start)

#or we can print it manually
start = time.time()
l = ["apple", "banana", "cherry","pineapple","guvava"]
"""myit = iter(l)

print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))
print(next(myit))

print(end - start)"""
for i in l:
    print(i)
end = time.time()
print(end - start)