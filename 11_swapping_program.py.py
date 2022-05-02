#Swapping Program
print("This script is intended to swap the values of two data variable using a third temporary variable")
a=int(input("Enter a Number : "))
b=int(input("Enter other Number : "))

print("Before swapping: a=",a ," b=",b)

c=a
a=b
b=c

print("After swapping:",a,b)

#--------------------------------------#

print("Before swapping: a=",a ," b=",b)

a=a+b
b=a-b
a=a-b

print("After swapping:",a,b)


#---------------------------------------#

print("Before swapping: a=",a ," b=",b)

a,b=b,a
print("After swapping:",a,b)
