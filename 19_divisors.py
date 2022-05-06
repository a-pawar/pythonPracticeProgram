#Create a program that asks the user for a number and then prints out a list of all the divisors of that number
a=int(input("Enter a number: "))
for i in range(1,a//2+1):
    if(a%i==0):
        print(i)
else:
    print(a)

'''
a=int(input("Enter a number: "))
l=[]
for i in range(1,a+1):
    if(a%i==0):
        l.append(i)
print(l)
'''
