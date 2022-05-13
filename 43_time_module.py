#program to find LCM
import time

print("Program to find LCM")
x=int(input("Enter First number: "))
y=int(input("Enter Second number: "))
z=int(input("Enter Third number: "))
initial=time.time()
a=x*y*z
k=1

if(x>=y and x>=z):
    k=x
elif(y>=x and y>=z):
    k=y
else:
    k=z
    
#k=max(x,y,z)
for i in range(k,a+1):
    if(i%x==0 and i%y==0 and i%z==0):
        print("LCM of ",x,",",y,"and",z,"is",i)
        break;
print("Time required for program is:",time.time()-initial)

