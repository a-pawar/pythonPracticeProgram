class compute_area:
    def area(self,para1=None,para2=None,para3=None):
        x=0
        if(para1 != None and para2 != None and para3 !=None):
            x=para1*para2*para3
        elif(para1 != None and para2 != None and para3 ==None):
            x=para1*para2
        elif(para1 != None and para2 == None and para3 ==None):
            x=para1*para1
        else:
            x="No value"
        return x

c1=compute_area()
print("Area of Triangle",c1.area(2,4,6))
print("Area of Rectangle",c1.area(3,5))
print("Area of Square",c1.area(9))


            
    
        
        
        
