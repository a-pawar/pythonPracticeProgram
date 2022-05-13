#area and perimeter of rectangle
print("Program to find area and perimeter of rectangle.")
l=float(input("Enter length of rectangle: "))
w=float(input("Enter width of rectangle: "))

if(l<0 or w<0):
    print("Distance cannot be negative")
area=l*w
perimeter=2*(l+w)
print("Area of rectangle: ",area)
print("perimeter of rectangle: ",perimeter)
    
