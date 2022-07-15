def gen():
    n = 1
    print("first time")
    yield n

    n+=1
    print("second time")
    yield n

    n+=1
    print("third time")
    yield n

x = gen()
print(next(x))
print(next(x))
print(next(x))
