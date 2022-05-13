#Method Overloading
'''
class compute:
    
    def avg(self,a=None,b=None,c=None):
        average=0
        if(a!=None and b!=None and c!=None):
            average=(a+b+c)/3
        elif(a!=None  and b!=None  and c==None):
            average=(a+b)/2
        elif(a!=None and b==None  and c==None):
            average=a
        else:
            average="No value"
        return average


c1=compute()
avg1=c1.avg(12,13,14)
avg2=c1.avg(12,13)
avg3=c1.avg(12)
avg4=c1.avg()

'''
class compute:
    def avg(self,*x):
        average=0
        sum=0
        if len(x)==0:
            average = "No Value"
        else:
            for i in x:
                
                sum+=i
            average = sum/len(x)
        return average

c1=compute()

avg1=c1.avg(12,13,14)
avg2=c1.avg(12,13)
avg3=c1.avg(12)
avg4=c1.avg()
a=[2,3,4]



print(avg1)
print(avg2)
print(avg3)
print(avg4)


