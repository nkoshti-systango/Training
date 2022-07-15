class student:
    def __init__(self,fname,lname,address):
        self.fname = fname
        self.lname = lname
        self.address = address
x = student("Nikita","koshti","Indore")
print(x.fname)
print(x.lname)
print(x.address)