class NegativeValueError(Exception):

    """Raised when the denominator value is negative"""
    pass

a = int(input("enter value of a: "))
b = int(input("enter value of b: "))

try:
    if b < 0:

        raise NegativeValueError
    d = a/b 
   
except ZeroDivisionError:            #pre-defined exception
    print("denominator can't be zero")
except NegativeValueError:
    print("denominator can't be negative")
else:
    print(d)
finally:
    print("execution done")