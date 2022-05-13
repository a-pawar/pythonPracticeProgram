#write a program that prints out all the elements of the list that are lessthan 5.

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

temp=len(a)
'''
for i in range(0,temp):
    if(a[i]<5):
        print(a[i])
'''

for i in a:
    if i<5:
        print(i)

#Instead of printing the elements one by one,make a new list that has all the elements less than 5 from this list in it and print out this new list.
b=[]
'''
for i in range(0,temp):
    if(a[i]<5):
        b.append(a[i])     
temp1=len(b)
for j in range(0,temp1):
    print(b[j])
'''
'''
for i in a:
    if(i<5):
        b.append(i)
temp1=len(b)
for j in b:
    print(j)
'''
#Write this in one line of Python.
print( [ x for x in a if x<5 ] )
#Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.
x=int(input("Enter a number: "))
for i in a:
    if(i<x):
        b.append(i)

print(b)
