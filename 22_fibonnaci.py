#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
total=int(input("Enter how many fibonnaci number  u want: "))
a=1
b=0
#if total>=1:
    #print(b,end=' ')

for i in range(0,total):
    c=a+b
    print(c,end=' ')
    a=b
    b=c
