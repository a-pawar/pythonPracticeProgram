#create a program to find the factorial of a user defined integer with Recurssive method

print("Program to find factorial of a positive number.")

#with recurssion
def fact(x):
    y=1
    if x==1 or x==0:
        return y
    
    else:
        y=x*fact(x-1)
        return y
val=int(input("Enter a value: "))
funct_val=fact(val)
print("Factorial of {} is {} ".format(val,funct_val))


