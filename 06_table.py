
#printing table of user defined integer
n=int(input("Enter a number: "))
i=1
f=11
#for p in range(i,f):
    #print(n,"*",p,"=",n*p)

m=n*10
count=1
for i in range(n,m+1,n):
    print("{} * {} = {}".format(n,count,i))
    count=count+1

