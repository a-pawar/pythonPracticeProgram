#Area and Circumference of circle
print("Program to find area and circumference of circle.")
r=float(input("Enter radius of circle: "))


def area_circle(r,pi=3.14):
    if(r>=0):
        #pi=3.14
        area=pi*r*r
        cir=2*pi*r
        print("Area of circle is: ",round(area,4))
        print("Circumference of circle is: ",round(cir,4))
    else:
        print("Radius can not be negative.")

area_circle(r)
