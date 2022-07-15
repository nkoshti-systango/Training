class cal:
    def area(self, x = None, y = None):
        if x!=None and y!=None:
            return x*y
        elif x!=None and y==None:
            return 3.14*x*x
        else:
            return "atleast one argument is required"
    

x = cal()
print(x.area(4,6))
print(x.area(5))
print(x.area())