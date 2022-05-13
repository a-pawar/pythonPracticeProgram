#class object

class cars:
    def __init__(self
                 ,b_name,model,type1):
        self.b_name=b_name
        self.model=model
        self.type1=type1
car1=cars("Maruti","Ciaz","Sedan")
print(car1.model)
print(car1.b_name,car1.model,car1.type1)

class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
    def circumference(self):
        return 2*3.14*self.radius

num=int(input("Enter radius: "))
c1=circle(num)
a=c1.area()
b=c1.circumference()
print(a)
print(b)

c2=circle(num)
c=c2.area()
d=c2.circumference()

print(c)
print(d)
