#factorial
def fact(x):
    if x == 1:
        return x
    else:
        return x * fact(x-1)
r = fact(6)
print(r)
