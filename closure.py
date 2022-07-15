def outer():
    x = 3
    def inner():
        return x + 4
    return inner
print(outer)

a = outer()
print(a.__name__)
print(a.__qualname__)
print(type(a))