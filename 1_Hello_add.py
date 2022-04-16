
import time
initial=time.time()
print(initial)
for i in range(50):
    print("Anshul pawar: ")
print("for loop timing: ",time.time()-initial)

initial2=time.time()
print(initial2)
k=0
while(k<50):
    print("Anshul pawar: ")
    k+=1
print("while loop timing: ",time.time()-initial2)

'''
#timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000, globals=None)
import timeit
initial=timeit.timeit()
print(initial)
for i in range(202):
    print("Anshul pawar: ")
print("for loop timing: ",timeit.timeit()-initial)

initial2=timeit.timeit()
print(initial2)
k=0
while(k<202):
    print("Anshul pawar: ")
    k+=1
print("while loop timing: ",timeit.timeit()-initial2)


#timeit.timeit(print("Hello World!!!",2+3 ), number=10000)

'''
'''
print("Anshul")
i=10
print(i)
a=input("Write Your name")
print(a)
'''
'''
      
#Write a python script to ADD two numbers
a=10
b=20
c=a+b
print(c)
#print(10+20)
'''
