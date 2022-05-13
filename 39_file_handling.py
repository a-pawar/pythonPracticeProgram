import time
#print("Program to find factorial of a positive number.")

def itr_fact(x):
    fact_pos=1
    k=0
    while(k>1000):
        trr1=k
        k=k+1
    if(x>0):
        for i in range(1,x+1):
            fact_pos=fact_pos*i
        return str(fact_pos)
        
    

#with recurssion
def rec_fact(x):
    y=1
    k=0
    while(k>1000):
        trr1=k
        k=k+1
    if x==1 or x==0:
        return y
    
    else:
        y=x*rec_fact(x-1)
        return y
#ans=[]    
f=open("myfirst_file.txt","w")
for i in range(5,1000,5):
    val=i

    initial=time.time()
    val1=itr_fact(val)
    final=time.time()
    t1=round(final,6)-round(initial,6)
    
    print(val,round(t1,5),"\n")
    initial=time.time()
    val2=rec_fact(val)
    final=time.time()
    t2=round(final,6)-round(initial,6)
    print(val,round(t2,8),"\n")
    #print("Factorial of {} is {} ".format(val,funct_val))

    f.write(str(val))
    
    f.write('\t')
    f.write(str(t1))
    f.write('\t')
    f.write(str(t2))
    f.write('\n')
f.close()


