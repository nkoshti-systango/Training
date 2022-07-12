#Arithmetic operators
print("addition +")
print(3 + 5)
print("subtraction -")
print(56-12)
print("multiplication *")
print(56 * 2)
print("division /")
print(34/23)
print("modulus %")
print(123%10)
print("Exponential **")
print(3**5)
print("floor division //")
print(345//54)

#Assignment operators
x = 5
x+=4
x-=2
x*=2
x/=3
print(x)
#Comparison operators
if 5 == 5:
    print(True)
if 5>=4:
    print(True)
if 6<=4:
    print(False)
#Logical operators
print("and")
x = 5
print(x > 3 and x < 10)
print("or")
x = 5
print(x > 3 or x < 10)
print("not")
x = True
print(not x)
#Identity operators
x = 45
y = 67
print(x is y)
print(x is not y)
#Membership operators
t = {3,4,5,67,8,5,3}
print(3 in t)
print(345 not in t)
#Bitwise operators
# & AND	Sets each bit to 1 if both bits are 1
print(7 & 1)
# |	OR	Sets each bit to 1 if one of two bits is 1
print(9 | 0)
# ^	XOR	Sets each bit to 1 if only one of two bits is 1
print(34 ^ 45)
# ~ NOT	Inverts all the bits
print(~ 45)
print(~0)
# << Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
print(23<<2)
# >> Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
print(123<<2)