class emp:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def display(self):
        print("name is:",self.name)
        print("email is:",self.email)
class add(emp):
    def printn(self):
        print("printing  something else")
class salary(emp):
    def salary(self,amount):
        self.amount = amount
        print("salary is",self.amount)
"""x = add("nikita","nkoshti@")
x.display()
x.printn()
"""
y = salary("nikita","nkoshti@")
y.display()
y.salary(23456)