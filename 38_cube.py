
class cube:
    def __init__(self,side):
        self.side=side
    def sur_area(self):         #function for  suface area
        return 6*self.side*self.side
    def lat_area(self):         #function for lateral suface area
        return 4*self.side*self.side
    def volume(self):           #function for volume
        return self.side*self.side*self.side
num=int(input("Side of cube: "))
c1=cube(num)
print("Surface area of cube: ",c1.sur_area(),"sq unit")
print("Lateral surface area of cube: ",c1.lat_area(),"sq unit")
print("Volume of cube: ",c1.volume(),"cube unit")

    
